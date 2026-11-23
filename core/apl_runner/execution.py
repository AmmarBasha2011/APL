"""Compilation, source-aware diagnostics and local APL imports."""
import difflib
import importlib.abc
import importlib.util
import linecache
from pathlib import Path
import sys
import traceback
from contextlib import contextmanager

from core.apl_runner.source import source_line


class Compilation:
    def __init__(self, source, filename):
        from core.apl_runner.main import transpile
        self.source, self.filename = source, filename
        self.python = ''
        try:
            from core.apl_runner import cache
            path = Path(filename)
            if path.is_file():
                self.python = cache.load_cached(path, source) or ''
            if not self.python:
                self.python = transpile(source)
            self.code = compile(self.python, filename, 'exec')
            if path.is_file():
                cache.store(path, source, self.python)
                cache.prune(path)
        except SyntaxError as error:
            if self.python:
                error.lineno = source_line(self.python, error.lineno or 1)
                # Translation changes token widths; never claim a fake column.
                error.offset = 1
            error.filename = filename
            lines = source.splitlines()
            error.text = lines[(error.lineno or 1) - 1] if 0 < (error.lineno or 0) <= len(lines) else ''
            raise


def diagnostic(error, compilation=None, source='', filename='<apl>'):
    from core.apl_runner.main import _get_error_ar
    line, column = 1, 1
    if compilation:
        source, filename = compilation.source, compilation.filename
    if isinstance(error, SyntaxError):
        line, column = error.lineno or 1, error.offset or 1
        filename = error.filename or filename
    elif compilation:
        for frame in traceback.extract_tb(error.__traceback__):
            if frame.filename == filename:
                line = source_line(compilation.python, frame.lineno)
    lines = source.splitlines()
    excerpt = lines[line - 1] if 0 < line <= len(lines) else ''
    # Column is the first source token for rewritten statements. Python token
    # offsets cannot be reused after Arabic -> Python translation.
    if not isinstance(error, SyntaxError) or column == 1:
        column = len(excerpt) - len(excerpt.lstrip()) + 1
    text = f'APL-{type(error).__name__}: {filename}:{line}:{column}\n{_get_error_ar(error)}\n{excerpt}\n' + ' ' * (column - 1) + '^'
    if isinstance(error, NameError) and error.name:
        import re
        names = set(re.findall(r'[^\W\d]\w*', source)) - {error.name}
        matches = difflib.get_close_matches(error.name, names, n=1, cutoff=.65)
        if matches:
            text += '\nهل تقصد: ' + matches[0] + '؟'
    return text


def execute(compilation, namespace):
    from core.apl_runner.main import _RUNTIME
    exec(compile(_RUNTIME, '<apl-runtime>', 'exec'), namespace)
    # Keep original source for traceback/debug consumers, generated code for maps.
    linecache.cache[compilation.filename] = (len(compilation.source), None,
                                            compilation.source.splitlines(True), compilation.filename)
    exec(compilation.code, namespace)


class APLLoader(importlib.abc.Loader):
    def __init__(self, path):
        self.path = path

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        source = self.path.read_text(encoding='utf-8')
        compilation = Compilation(source, str(self.path))
        module.__file__ = str(self.path)
        try:
            execute(compilation, module.__dict__)
        except Exception as error:
            # Preserve the failing module's source context through caller frames.
            error.add_note(diagnostic(error, compilation))
            raise


class APLFinder(importlib.abc.MetaPathFinder):
    def __init__(self, root):
        self.root = str(root)

    def find_spec(self, fullname, path=None, target=None):
        name = fullname.rsplit('.', 1)[-1]
        for entry in path if path is not None else [self.root]:
            base = Path(entry)
            package = base / name / '__init__.apl'
            file = base / (name + '.apl')
            if package.is_file():
                return importlib.util.spec_from_file_location(fullname, package, loader=APLLoader(package), submodule_search_locations=[str(package.parent)])
            if file.is_file():
                return importlib.util.spec_from_file_location(fullname, file, loader=APLLoader(file))
        return None


@contextmanager
def project_imports(root):
    finder = APLFinder(root)
    sys.meta_path.insert(0, finder)
    try:
        yield
    finally:
        sys.meta_path.remove(finder)


def execute_file(filepath, args=(), debug=False):
    path = Path(filepath).resolve()
    source = path.read_text(encoding='utf-8')
    compilation = None
    old_argv, old_path = sys.argv[:], sys.path[:]
    try:
        compilation = Compilation(source, str(path))
        sys.argv = [str(path), *args]
        sys.path.insert(0, str(path.parent))
        with project_imports(path.parent):
            execute(compilation, {'__name__': '__main__', '__file__': str(path), '__package__': None})
    except Exception as error:
        if debug:
            traceback.print_exc()
        print(diagnostic(error, compilation, source, str(path)), file=sys.stderr)
        for note in getattr(error, '__notes__', ()):
            print(note, file=sys.stderr)
        raise SystemExit(1) from None
    finally:
        sys.argv, sys.path = old_argv, old_path

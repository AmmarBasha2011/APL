"""Library registry: what is installed, and how one library is loaded.

APL itself ships no libraries. This package holds only the machinery: the
folder installed libraries live in, the loader the transpiler uses to read a
library's vocabulary, and the import discovery that a library feeds.

A library is one Python file, `<name>_funcs.py`, holding the Arabic vocabulary
tables for one Python module. It carries its own IMPORT_CHECK,
IMPORT_STATEMENT and `<NAME>_SUBSTITUTE`, so a file dropped into the library
folder is usable without any index. Nothing is bundled with the language.
"""
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import types

_HERE = Path(__file__).resolve().parent


def _data_file(name):
    """Find an optional data file next to this module, or in a frozen build."""
    candidates = [_HERE / name]
    bundle = getattr(sys, '_MEIPASS', None)
    if bundle:
        candidates.append(Path(bundle) / 'core' / 'libraries' / name)
    for path in candidates:
        if path.is_file():
            return path
    return None


def _read_json(name):
    """Read an optional JSON file, returning [] when it is absent or broken."""
    path = _data_file(name)
    if path is None:
        return []
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return []


def library_home():
    """Folder that holds installed libraries (APL_LIBRARIES overrides it)."""
    override = os.environ.get('APL_LIBRARIES')
    return Path(override) if override else Path.home() / '.apl' / 'libraries'


# Optional metadata a library store can ship: index.json (catalog of what the
# store offers) and registry.json (full entry metadata for those files).
CATALOG = {item['module']: item for item in _read_json('index.json')}
_META = {entry['module']: entry for entry in _read_json('registry.json')}


def _discovered(path):
    """Build an entry for a library file that no catalog describes."""
    module = path.stem
    name = module[:-6] if module.endswith('_funcs') else module
    return {'name': name, 'module': module,
            'substitute': f'{name.upper()}_SUBSTITUTE',
            'import_check': None, 'import_statement': None,
            'import_modules': [], 'docs': None, 'bundled': False}


def installed_modules():
    """Module files present in the library folder, catalog order first.

    Two layouts are accepted:
      <home>/<name>_funcs.py              one loose file
      <home>/<name>/apl-library.json      a package folder, as the package
                                          manager installs it
    """
    home = library_home()
    found = []
    for module in CATALOG:
        if (home / (module + '.py')).is_file():
            found.append(module)
    if home.is_dir():
        for path in sorted(home.glob('*_funcs.py')):
            if path.stem not in found:
                found.append(path.stem)
        for config in sorted(home.glob('*/apl-library.json')):
            module = package_module(config.parent)
            if module and module not in found:
                found.append(module)
    return found


def read_config(folder):
    """The apl-library.json of an installed package, or {} when unreadable."""
    path = Path(folder) / 'apl-library.json'
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return {}


def package_module(folder):
    """Module name of a package folder, taken from its config."""
    meta = read_config(folder)
    entry = meta.get('entry') or ''
    if entry.endswith('.py'):
        return Path(entry).stem
    name = meta.get('name') or Path(folder).name
    return f'{name}_funcs'


def library_path(entry):
    """Where one installed library's Python file actually lives."""
    home = library_home()
    direct = home / (entry['module'] + '.py')
    if direct.is_file():
        return direct
    for folder in (home / entry.get('name', ''), home / entry['module']):
        meta = read_config(folder)
        if not meta:
            continue
        candidate = folder / (meta.get('entry') or (entry['module'] + '.py'))
        try:
            inside = folder.resolve() in candidate.resolve().parents
        except (OSError, RuntimeError):
            inside = False
        if inside and candidate.is_file():
            return candidate
    return direct


def entries():
    """Registry entries usable right now, package metadata included."""
    result = []
    home = library_home()
    for module in installed_modules():
        entry = _META.get(module) or _discovered(home / (module + '.py'))
        entry = dict(entry, bundled=False)
        for folder in (home / entry.get('name', ''), home / module):
            meta = read_config(folder)
            if meta:
                entry.setdefault('name', meta.get('name') or entry['name'])
                entry['version'] = meta.get('version')
                entry['title'] = meta.get('title')
                entry['requires'] = meta.get('requires') or []
                entry['folder'] = str(folder)
                break
        result.append(entry)
    return result


ENTRIES = entries()


def refresh():
    """Re-read the library folder after an install, without a new process."""
    global ENTRIES
    ENTRIES = entries()
    return ENTRIES


def module(entry):
    """Import one installed library module."""
    name = 'apl_library.' + entry['module']
    existing = sys.modules.get(name)
    if isinstance(existing, types.ModuleType):
        return existing
    if existing is not None:
        # A lazy proxy registered by core.libraries.lazy: load the real one.
        del sys.modules[name]
    path = library_path(entry)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f'library file missing: {path}')
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    # A file without a catalog entry carries its own import metadata.
    entry['import_check'] = entry.get('import_check') or getattr(mod, 'IMPORT_CHECK', None)
    entry['import_statement'] = (entry.get('import_statement')
                                 or getattr(mod, 'IMPORT_STATEMENT', None))
    entry['import_modules'] = (entry.get('import_modules')
                               or list(getattr(mod, 'IMPORT_MODULES', []) or []))
    return mod


def _vocabulary(mod, prefix):
    """The pattern/table pairs one library module exposes.

    A library declares its Arabic keys as tables plus the regex that finds them:
        MATH_FUNCS = {"جذر": "math.sqrt", ...}      with MATH_PATTERN
        FILE_METHODS = {"اقرأ": "read", ...}        with FILE_METHOD_PATTERN
        TZ_PROPS = {"المنطقة": "key"}               with TZ_PROP_PATTERN
        PI_CONSTANTS = {"ط": "math.pi"}             with PI_CONSTANT_PATTERN
    Nothing about the library is hard-coded in the language: whatever a module
    exposes under its own prefix is applied for every installed library.
    """
    for suffix, table_suffix, opens_call in (
            ('METHOD_PATTERN', 'METHODS', True),
            ('PROP_PATTERN', 'PROPS', False),
            ('CONSTANT_PATTERN', 'CONSTANTS', False),
            ('PATTERN', 'FUNCS', True)):
        pattern = getattr(mod, prefix + suffix, None)
        table = getattr(mod, prefix + table_suffix, None)
        if isinstance(pattern, str) and pattern and isinstance(table, dict) and table:
            yield pattern, table, opens_call


def _apply_vocabulary(text, mod, prefix):
    import re as _re
    for pattern, table, opens_call in _vocabulary(mod, prefix):
        try:
            compiled = _re.compile(pattern)
        except _re.error:
            continue

        def replace(match, table=table, opens_call=opens_call):
            if match.groups():
                word = match.group(1)
            else:
                # A pattern without a group matches the whole spelling, e.g.
                # "جذر(" — the table is keyed by the word alone.
                word = match.group(0).strip()
                while word.endswith(('(', ' ')):
                    word = word[:-1].strip()
            target = table.get(word)
            if target is None:
                return match.group(0)
            return f'{target}(' if opens_call else str(target)

        text = compiled.sub(replace, text)
    return text


def substitute_all(text, user_names):
    """Apply every installed library's Arabic vocabulary.

    A library either ships a ready <NAME>_SUBSTITUTE function or the pattern and
    table pairs described in _vocabulary; both are applied here, so a library
    from any repository works without a line of code added to the language.
    """
    for entry in ENTRIES:
        mod = module(entry)
        substitute = getattr(mod, entry['substitute'], None) if entry.get('substitute') else None
        if callable(substitute):
            mod.USER_NAMES = user_names
            text = substitute(text)
            continue
        text = _apply_vocabulary(text, mod, entry['name'].upper() + '_')
    return text


def imports_for(code):
    """Import lines the generated Python needs for the libraries it mentions."""
    from core.runner import regex_cache as re
    needs = []
    for entry in ENTRIES:
        check = entry.get('import_check')
        if not check or not re.search(check, code):
            continue
        if entry.get('import_modules'):
            modules = [name for name in entry['import_modules']
                       if re.search(r'(?<![\w.])' + re.escape(name) + r'\.', code)
                       and ('import ' + name) not in code]
            if modules:
                needs.append('import ' + ', '.join(modules))
        elif entry.get('import_statement'):
            needs.append(entry['import_statement'])
    # Names the generated code can mention without any library installed.
    if re.search(r'(?<![\w.])dataclasses\.', code):
        needs.append('import dataclasses')
    for name in ('enum', 'abc', 'json', 'os', 'datetime', 'time', 'shutil'):
        if re.search(r'(?<![\w.])' + name + r'\.', code):
            needs.append('import ' + name)
    if '_apl_fetch' in code:
        needs.append('import urllib.request')
    if '@dataclass' in code:
        needs.append('from dataclasses import dataclass, field, asdict, astuple, replace')
    if '@functools.' in code:
        needs.append('import functools')
    if re.search(r'(?<![\w.])(?:contextlib|tempfile|queue|copy|struct|io|codecs|base64|zipfile|pathlib|secrets)\.', code):
        for name in ('contextlib', 'tempfile', 'queue', 'copy', 'struct', 'io',
                     'codecs', 'base64', 'zipfile', 'pathlib', 'secrets'):
            if re.search(r'(?<![\w.])' + name + r'\.', code):
                needs.append('import ' + name)
    return list(dict.fromkeys(needs))


def symbols():
    """Normalized vocabulary index for editor tools; empty without libraries."""
    for entry in ENTRIES:
        mod = module(entry)
        for attr in sorted(dir(mod)):
            value = getattr(mod, attr)
            if attr.isupper() and isinstance(value, dict):
                for name, target in value.items():
                    if isinstance(name, str) and isinstance(target, str):
                        yield {'name': name, 'target': target,
                               'library': entry['name'],
                               'kind': attr.rsplit('_', 1)[-1].lower(),
                               'signature': None, 'docs': entry.get('docs')}

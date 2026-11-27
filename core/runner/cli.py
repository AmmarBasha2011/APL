"""Installed CLI, retaining python apl.py compatibility."""
import argparse
from pathlib import Path
import sys


def main(argv=None):
    from core.runner.main import print_help, run_repl, __version__, transpile
    from core.runner.execution import Compilation, diagnostic, execute, execute_file
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ('help', '--help', '-h', '-?'):
        print('apl run FILE [args...] | check FILE | transpile FILE | repl | --version')
        print_help()
        return 0
    if argv[0] in ('--version', '-v', 'version'):
        print(f'APL v{__version__} - Ammar Programming Language')
        return 0
    if argv[0] in ('clear-cache', '--clear-cache'):
        from core.runner.cache import clear
        print(f'تم حذف {clear()} ملف ترجمة مخزنة')
        return 0
    if argv[0] in ('repl', 'interactive', 'shell'):
        run_repl()
        return 0
    if argv[0] in ('-c', '--code'):
        if len(argv) < 2:
            raise SystemExit('Usage: apl -c CODE')
        source, compilation = argv[1], None
        try:
            compilation = Compilation(source, '<command>')
            execute(compilation, {'__name__': '__main__'})
        except Exception as error:
            print(diagnostic(error, compilation, source, '<command>'), file=sys.stderr)
            raise SystemExit(1) from None
        return 0
    command = argv.pop(0) if argv[0] in ('run', 'check', 'transpile') else 'run'
    parser = argparse.ArgumentParser(prog=f'apl {command}')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('file')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    options = parser.parse_args(argv)
    if command == 'run':
        try:
            execute_file(options.file, options.args, options.debug)
        except OSError as error:
            print(diagnostic(error, filename=options.file), file=sys.stderr)
            raise SystemExit(1) from None
        return 0
    source, compilation = '', None
    try:
        source = Path(options.file).read_text(encoding='utf-8')
        compilation = Compilation(source, options.file)
    except Exception as error:
        print(diagnostic(error, compilation, source, options.file), file=sys.stderr)
        raise SystemExit(1) from None
    if command == 'check':
        print(f'OK: {options.file}')
    else:
        from core.runner.main import _RUNTIME
        print(_RUNTIME + '\n' + compilation.python)
    return 0

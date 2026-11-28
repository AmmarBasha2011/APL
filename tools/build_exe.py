#!/usr/bin/env python3
# APL - لغة عمار البرمجية
# Copyright (c) 2026 Ammar Elkhateeb (AmmarBasha2011)
# Distributed under the Python Software Foundation License Version 2 (PSF-2.0).
"""Build one single-file executable for the platform this runs on.

    python tools/build_exe.py

The result lands in dist/ as `apl` (or `apl.exe` on Windows). PyInstaller is
only needed to build; APL itself still runs with nothing but the standard
library.

Two kinds of import have to be declared by hand, because the engine reaches
them without a static `import` statement:

* the modules the runtime prologue imports from inside a string (_RUNTIME), and
* the library modules, which the registry loads by name.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'core' / 'libraries'

#: Imported by the _RUNTIME prologue in core/runner/main.py (a string, so
#: PyInstaller cannot see these imports).
RUNTIME_MODULES = ['sys', 'builtins', 'pathlib', 'zoneinfo', 'decimal',
                   'fractions', 'string', 'enum', 'secrets', 'getpass',
                   'operator', 'pprint']
#: The runtime string uses these as well.
RUNTIME_MODULES += ['core.apps', 'core.apps.web', 'core.apps.common', 'core.apps.terminal',
                    'core.apps.docs', 'core.apps.examples', 'core.apps.bench', 'core.console_bidi']
RUNTIME_MODULES += ['datetime', 'time', 'os', 'shutil', 'json']


def bundled_modules():
    """Library modules shipped in the tree, if the repository has any."""
    path = DATA / 'index.json'
    if not path.is_file():
        return []
    catalog = json.loads(path.read_text(encoding='utf-8'))
    return [item['module'] for item in catalog if item.get('bundled')]


def main():
    separator = ';' if sys.platform == 'win32' else ':'
    command = [sys.executable, '-m', 'PyInstaller', '--onefile', '--console',
               '--name', 'apl', '--paths', str(ROOT), '--noconfirm']
    for name in ('registry.json', 'index.json'):
        if (DATA / name).is_file():
            command += ['--add-data', f'core/libraries/{name}{separator}core/libraries']
    for module in RUNTIME_MODULES:
        command += ['--hidden-import', module]
    for module in bundled_modules():
        command += ['--hidden-import', f'core.libraries.{module}']
    # zoneinfo needs the tzdata package on Windows; bundle it when installed.
    try:
        import tzdata  # noqa: F401
    except ImportError:
        pass
    else:
        command += ['--collect-data', 'tzdata']
    command.append(str(ROOT / 'apl.py'))
    print('building with PyInstaller ...')
    return subprocess.call(command, cwd=str(ROOT))


if __name__ == '__main__':
    raise SystemExit(main())

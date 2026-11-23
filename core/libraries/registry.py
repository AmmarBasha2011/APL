"""One registration source for lazy modules, dispatch, imports and tools.

The ordered JSON file is the registration contract. Existing *_funcs.py tables
remain the vocabulary source and compatibility API. No optional dependencies
are imported just to read registration metadata.
"""
import importlib
import json
from pathlib import Path
import re

ENTRIES = json.loads(Path(__file__).with_name('registry.json').read_text(encoding='utf-8'))


def module(entry):
    return importlib.import_module('core.libraries.' + entry['module'])


def substitute_all(text, user_names):
    for entry in ENTRIES:
        if entry['substitute']:
            mod = module(entry)
            mod.USER_NAMES = user_names
            text = getattr(mod, entry['substitute'])(text)
    return text


def imports_for(code):
    needs = []
    for entry in ENTRIES:
        check = entry['import_check']
        if not check or not re.search(check, code):
            continue
        if entry['import_modules']:
            modules = [name for name in entry['import_modules']
                       if re.search(r'(?<![\w.])' + re.escape(name) + r'\.', code)
                       and ('import ' + name) not in code]
            if modules:
                needs.append('import ' + ', '.join(modules))
        elif entry['import_statement']:
            needs.append(entry['import_statement'])
    # Runtime helpers and legacy aliases whose import usage is not represented
    # by an ordinary module prefix in their library's IMPORT_CHECK.
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
        for name in ('contextlib', 'tempfile', 'queue', 'copy', 'struct', 'io', 'codecs', 'base64', 'zipfile', 'pathlib', 'secrets'):
            if re.search(r'(?<![\w.])' + name + r'\.', code):
                needs.append('import ' + name)
    return list(dict.fromkeys(needs))


def symbols():
    """Normalized vocabulary index for editor/tools; unknown signatures stay null.

    Do not import target packages or infer signatures by calling user code.
    Compatibility tables are read, never copied into a second editable index.
    """
    for entry in ENTRIES:
        mod = module(entry)
        for attr in sorted(dir(mod)):
            value = getattr(mod, attr)
            if attr.isupper() and isinstance(value, dict):
                for name, target in value.items():
                    if isinstance(name, str) and isinstance(target, str):
                        yield {'name': name, 'target': target, 'library': entry['name'],
                               'kind': attr.rsplit('_', 1)[-1].lower(),
                               'signature': None, 'docs': entry['docs']}

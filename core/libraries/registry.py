import base64
import hashlib
import importlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import sys
import tokenize
import types

_HERE = Path(__file__).resolve().parent


def _data_file(name):
    """Find a data file next to this module, including inside a frozen build."""
    candidates = [_HERE / name]
    bundle = getattr(sys, '_MEIPASS', None)
    if bundle:
        candidates.append(Path(bundle) / 'core' / 'libraries' / name)
    for path in candidates:
        if path.is_file():
            return path
    raise FileNotFoundError(f'APL data file missing: {name}')


def library_home():
    """Folder that holds libraries installed with `عمار مكتبة تحميل`."""
    override = os.environ.get('APL_LIBRARIES')
    return Path(override) if override else Path.home() / '.apl' / 'libraries'


# Full metadata for every library APL knows about, bundled or downloadable.
REGISTRY = json.loads(_data_file('registry.json').read_text(encoding='utf-8'))
# Small catalog: name, module, bundled flag, size and one-line title.
CATALOG = {item['module']: item for item in
           json.loads(_data_file('index.json').read_text(encoding='utf-8'))}
_META = {entry['module']: entry for entry in REGISTRY}


def bundled_modules():
    """Libraries that ship with APL: standard library vocabulary only."""
    return [module for module, item in CATALOG.items() if item['bundled']]


def downloaded_modules():
    """Libraries already installed in the user library folder."""
    home = library_home()
    return [module for module, item in CATALOG.items()
            if not item['bundled'] and (home / (module + '.py')).is_file()]


def entries():
    """Registry entries usable right now, in catalog order."""
    usable = set(bundled_modules()) | set(downloaded_modules())
    return [dict(entry, bundled=CATALOG[entry['module']]['bundled'])
            for entry in REGISTRY if entry['module'] in usable]


ENTRIES = entries()


def refresh():
    """Re-read the library folder after an install, without a new process."""
    global ENTRIES
    ENTRIES = entries()
    return ENTRIES


def module(entry):
    """Import one library module, whether bundled or downloaded."""
    if entry.get('bundled', True):
        name = 'core.libraries.' + entry['module']
        existing = sys.modules.get(name)
        if isinstance(existing, types.ModuleType):
            return existing
        if existing is not None:
            # A lazy proxy registered by core.libraries.lazy: load the real one.
            del sys.modules[name]
        return importlib.import_module(name)
    name = 'apl_library.' + entry['module']
    existing = sys.modules.get(name)
    if existing is not None:
        return existing
    spec = importlib.util.spec_from_file_location(name, library_home() / (entry['module'] + '.py'))
    if spec is None or spec.loader is None:
        raise ImportError(f'library file missing: {entry["module"]}.py')
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def substitute_all(text, user_names):
    words = re.findall(r"[^\W\d][\w\u064B-\u065F\u0670]*", text)
    hashes = [hashlib.blake2b(word.encode(), digest_size=16).digest()
              for word in words if not word.startswith('_APL_')]
    for entry in ENTRIES:
        if entry['substitute']:
            encoded = entry.get('token_filter')
            if encoded:
                bits = base64.b64decode(encoded)
                size = len(bits) * 8
                if not any(all(bits[(n := int.from_bytes(digest[off:off + 4], 'little') % size) // 8]
                               & (1 << (n % 8)) for off in (0, 4, 8)) for digest in hashes):
                    continue
            mod = module(entry)
            mod.USER_NAMES = user_names
            text = getattr(mod, entry['substitute'])(text)
    return text


def imports_for(code):
    from core.runner import regex_cache as re
    # Text mentioning "numpy.x" is data, not an import request. Python 3.14
    # exposes f-string expression tokens separately, so those stay visible.
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(code).readline))
        hidden = {tokenize.STRING, tokenize.COMMENT,
                  getattr(tokenize, 'FSTRING_MIDDLE', -1)}
        code = tokenize.untokenize([token._replace(string=' ' * len(token.string))
                                   if token.type in hidden else token for token in tokens])
    except (tokenize.TokenError, IndentationError, SyntaxError):
        pass  # Compilation will report malformed generated code separately.
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

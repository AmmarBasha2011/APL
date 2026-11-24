"""One registration source for lazy modules, dispatch, imports and tools.

The ordered JSON file is the registration contract. Existing *_funcs.py tables
remain the vocabulary source and compatibility API. No optional dependencies
are imported just to read registration metadata.
"""
import importlib
import base64
import hashlib
import json
from pathlib import Path
import re
import sys
import io
import tokenize

ENTRIES = json.loads(Path(__file__).with_name('registry.json').read_text(encoding='utf-8'))


def module(entry):
    name = 'core.libraries.' + entry['module']
    existing = sys.modules.get(name)
    return existing if existing is not None else importlib.import_module(name)


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
    from core.apl_runner import regex_cache as re
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

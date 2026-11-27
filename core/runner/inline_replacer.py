"""
APL - Inline Replacer
Handles all inline text replacements during transpilation
"""

from core.runner import regex_cache as re
from core.runner.patterns import (
    TYPE_ALIASES, _TYPE_PATTERN, _INLINE_FUNCS, _INLINE_FUNC_PATTERN,
    _METHOD_ALIASES, _METHOD_PATTERN, _TYPE_NAMES, _CONSTANTS, _CONSTANT_PATTERN,
    _LOGICAL_PATTERNS, _KW_ALIASES, _IO_ALIASES, _IO_PATTERN, _UDF_NAMES
)
from core.libraries.datetime_funcs import DATETIME_KWARGS
from core.libraries.pathlib_funcs import PATHLIB_KWARGS
from core.libraries.xml_funcs import XML_KWARGS
from core.libraries.argparse_funcs import ARGPARSE_KWARGS
from core.libraries.archive_funcs import ARCHIVE_KWARGS
from core.libraries.net_funcs import NET_KWARGS
from core.libraries.registry import ENTRIES, module, substitute_all


class _MissingLibrary:
    """Stand-in for a library that is not installed: it never matches."""

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item.endswith('_HELP'):
            return []
        if item.endswith(('_PATTERN', '_METHOD_PATTERN', '_PROP_PATTERN',
                          '_CONSTANT_PATTERN', '_METHODS', '_PROPS')):
            return _NEVER_MATCH
        return {}


#: Pattern that matches nothing, so an absent library stays silent.
_NEVER_MATCH = re.compile(r'(?!)')


class _LibraryMap(dict):
    """Library modules by name; a missing library yields a no-op stand-in."""

    def __missing__(self, name):
        stub = _MissingLibrary(name)
        self[name] = stub
        return stub


_library_modules = _LibraryMap({entry['name']: module(entry) for entry in ENTRIES})
globals().update({entry['module']: _library_modules[entry['name']] for entry in ENTRIES})

# Arabic names usable both as methods (.علوي) and standalone (علوي("x"))
_STANDALONE_METHODS = {
    "علوي": "upper", "سفلي": "lower", "تقليم": "strip",
    "تقسيم": "split", "استبدال": "replace", "عدد": "count",
    "يبدأ": "startswith", "ينتهي": "endswith", "ضم": "join",
    "فرز": "sort", "عكس": "reverse", "نسخ": "copy",
}



def _replace_type_names(text: str) -> str:
    for arabic, english in _TYPE_NAMES.items():
        text = re.sub(rf"(?<!\w){arabic}(?!\\w)", english, text)
    return text


# Names the user defines in the file being transpiled (functions, classes,
# variables, loop targets). A library word must never rewrite a name the user
# owns: `def رئيسي():` or `المتغير مستخدم = ...` stay exactly as written.
USER_NAMES: set[str] = set()
USER_ATTRIBUTES: set[str] = set()


def _safe(table, key):
    """Look up `key` in a library table, but never touch a user-defined name."""
    if key in USER_NAMES:
        return key
    return table[key]

def decorator_target(name: str):
    """Resolve an Arabic decorator name through the library vocabularies.

    Library FUNCS values that begin with "@" are decorator templates, e.g.
    مسار_فلاسك -> "@app.route" and مسار_جيت -> "@app.get". Returns the Python
    name (without the "@") or None when `name` is not a library decorator.
    """
    from core.libraries import LIBRARIES
    for lib_name, mod in LIBRARIES.items():
        funcs = getattr(mod, lib_name.upper() + "_FUNCS", None)
        if isinstance(funcs, dict):
            val = funcs.get(name)
            if isinstance(val, str) and val.startswith("@"):
                return val[1:]
    return None

def _inline_replace(text: str) -> str:
    if not text or not text.strip():
        return text
    # Fast gate: with no Arabic letter before a "(", "." or "," none of the ~66
    # library patterns can match, so skip the whole chain. Most real lines
    # (assignments, literals, pure-Latin code) exit here.
    from core.runner.fastpath import needs_scan
    if not needs_scan(text):
        return text

    _name_tokens = {}
    for _index, _name in enumerate(sorted(USER_NAMES, key=len, reverse=True)):
        _token = f"_APL_NAME_{_index}_END_"
        text, _count = re.subn(rf"(?<![\w.\u0600-\u06FF]){re.escape(_name)}(?![\w\u0600-\u06FF]|\s*=)", _token, text)
        if _count:
            _name_tokens[_token] = _name

    for _index, _name in enumerate(sorted(USER_ATTRIBUTES, key=len, reverse=True)):
        _token = f"_APL_ATTRIBUTE_{_index}_END_"
        text = re.sub(rf"(?<=\.){re.escape(_name)}(?![\w\u0600-\u06FF])", _token, text)
        _name_tokens[_token] = _name

    strings = {}
    def _save(m):
        idx = len(strings)
        strings[idx] = m.group(0)
        return f"\x00APL{idx}\x00"
    
    # Save f-strings, triple-quoted strings, then normal strings
    text = re.sub(r'f"[^"]*"', _save, text)
    text = re.sub(r"f'[^']*'", _save, text)
    text = re.sub(r'"""[\s\S]*?"""', _save, text)
    text = re.sub(r"'''[\s\S]*?'''", _save, text)
    text = re.sub(r'"[^"]*"', _save, text)
    text = re.sub(r"'[^']*'", _save, text)

    # Type hints: translate Arabic types in function signatures
    for arabic_type, english_type in _TYPE_NAMES.items():
        text = re.sub(rf':\s*{arabic_type}\b', f': {english_type}', text)
    for arabic_type, english_type in _TYPE_NAMES.items():
        text = re.sub(rf'->\s*{arabic_type}\b', f'-> {english_type}', text)

    # List comprehensions: [expr لكل var in iterable]
    text = re.sub(r'\[(.+?)\sلكل\s(\w+)\sفي\s(.+?)\]', lambda m: f'[{m.group(1)} for {m.group(2)} in {m.group(3)}]', text)

    # Decorator with args: @مزخرف(حجة1, حجة2)
    if text.strip().startswith('مزخرف('):
        text = re.sub(r'(\s*)مزخرف\((.+)\)', lambda m: f'{m.group(1)}@مزخرف({m.group(2)})', text)

    text = re.sub(r"ادخل\s*\(", "input(", text)
    
    # Library patterns first (more specific, longer names)
    text = re.compile(_library_modules['datetime'].DATETIME_PATTERN).sub(lambda m: f"{_safe(_library_modules['datetime'].DATETIME_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['pathlib'].PATHLIB_PATTERN).sub(lambda m: f"{_safe(_library_modules['pathlib'].PATHLIB_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['pathlib'].PATHLIB_METHOD_PATTERN).sub(lambda m: f".{_library_modules['pathlib'].PATHLIB_METHODS[m.group(1)]}(", text)
    text = re.compile(_library_modules['shutil'].SHUTIL_PATTERN).sub(lambda m: f"{_safe(_library_modules['shutil'].SHUTIL_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['textwrap'].TEXTWRAP_PATTERN).sub(lambda m: f"{_safe(_library_modules['textwrap'].TEXTWRAP_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['uuid'].UUID_PATTERN).sub(lambda m: f"{_safe(_library_modules['uuid'].UUID_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['datetime'].DATETIME_PROP_PATTERN).sub(lambda m: f".{_safe(_library_modules['datetime'].DATETIME_PROPS, m.group(1))}", text)
    text = re.compile(_library_modules['pathlib'].PATHLIB_PROP_PATTERN).sub(lambda m: f".{_safe(_library_modules['pathlib'].PATHLIB_PROPS, m.group(1))}", text)
    text = re.compile(_library_modules['uuid'].UUID_PROP_PATTERN).sub(lambda m: f".{_safe(_library_modules['uuid'].UUID_PROPS, m.group(1))}", text)
    text = re.compile(_library_modules['base64'].BASE64_PATTERN).sub(lambda m: f"{_safe(_library_modules['base64'].BASE64_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['urllib'].URLLIB_PATTERN).sub(lambda m: f"{_safe(_library_modules['urllib'].URLLIB_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['functools'].FUNCTOOLS_PATTERN).sub(lambda m: f"{_safe(_library_modules['functools'].FUNCTOOLS_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['math'].MATH_CONSTANT_PATTERN).sub(lambda m: _safe(_library_modules['math'].MATH_CONSTANTS, m.group(1)), text)
    text = re.compile(_library_modules['math'].MATH_PATTERN).sub(lambda m: f"{_safe(_library_modules['math'].MATH_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['random'].RANDOM_PATTERN).sub(lambda m: f"{_safe(_library_modules['random'].RANDOM_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['time'].TIME_PATTERN).sub(lambda m: f"{_safe(_library_modules['time'].TIME_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['time'].TIME_PROP_PATTERN).sub(lambda m: f"{_safe(_library_modules['time'].TIME_PROPS, m.group(1))}", text)
    text = re.compile(_library_modules['statistics'].STATISTICS_PATTERN).sub(lambda m: f"{_safe(_library_modules['statistics'].STATISTICS_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['os'].OS_PROP_PATTERN).sub(lambda m: f"({_safe(_library_modules['os'].OS_PROPS, m.group(1))})", text)
    text = re.compile(_library_modules['os'].OS_PATTERN).sub(lambda m: f"{_safe(_library_modules['os'].OS_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['re'].RE_CONSTANT_PATTERN).sub(lambda m: f"{_safe(_library_modules['re'].RE_CONSTANTS, m.group(1))}", text)
    text = re.compile(_library_modules['re'].RE_PATTERN).sub(lambda m: f"{_safe(_library_modules['re'].RE_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['collections'].COLLECTIONS_PATTERN).sub(lambda m: f"{_safe(_library_modules['collections'].COLLECTIONS_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['itertools'].ITERTOOLS_PATTERN).sub(lambda m: f"{_safe(_library_modules['itertools'].ITERTOOLS_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['json'].JSON_PATTERN).sub(lambda m: f"{_safe(_library_modules['json'].JSON_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['hashlib'].HASHLIB_PATTERN).sub(lambda m: f"{_safe(_library_modules['hashlib'].HASHLIB_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['flask'].FLASK_PATTERN).sub(lambda m: f"{_safe(_library_modules['flask'].FLASK_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['fastapi'].FASTAPI_PATTERN).sub(lambda m: f"{_safe(_library_modules['fastapi'].FASTAPI_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['requests'].REQUESTS_PATTERN).sub(lambda m: f"{_safe(_library_modules['requests'].REQUESTS_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['sqlite3'].SQLITE3_PATTERN).sub(lambda m: f"{_safe(_library_modules['sqlite3'].SQLITE3_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['sqlite3'].SQLITE3_METHOD_PATTERN).sub(lambda m: f".{_library_modules['sqlite3'].SQLITE3_METHODS[m.group(1)]}(", text)
    text = re.compile(_library_modules['asyncio'].ASYNCIO_PATTERN).sub(lambda m: f"{_safe(_library_modules['asyncio'].ASYNCIO_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['threading'].THREADING_PATTERN).sub(lambda m: f"{_safe(_library_modules['threading'].THREADING_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['unittest'].UNITTEST_PATTERN).sub(lambda m: f"{_safe(_library_modules['unittest'].UNITTEST_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['csv'].CSV_PATTERN).sub(lambda m: f"{_safe(_library_modules['csv'].CSV_FUNCS, m.group(1))}(", text)
    text = re.compile(r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(_library_modules['logging'].LOGGING_VERBS, key=len, reverse=True)) + r")\s*\(").sub(lambda m: _library_modules['logging'].LOGGING_VERBS[m.group(1)] + "(", text)
    text = re.compile(_library_modules['logging'].LOGGING_CONSTANT_PATTERN).sub(lambda m: _safe(_library_modules['logging'].LOGGING_CONSTANTS, m.group(1)), text)
    text = re.compile(_library_modules['logging'].LOGGING_PATTERN).sub(lambda m: f"{_safe(_library_modules['logging'].LOGGING_FUNCS, m.group(1))}(", text)
    text = re.compile(r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(_library_modules['argparse'].ARGPARSE_STANDALONE, key=len, reverse=True)) + r")\s*\(").sub(lambda m: _library_modules['argparse'].ARGPARSE_STANDALONE[m.group(1)] + "(", text)
    text = re.compile(_library_modules['argparse'].ARGPARSE_PATTERN).sub(lambda m: f"{_safe(_library_modules['argparse'].ARGPARSE_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['subprocess'].SUBPROCESS_PATTERN).sub(lambda m: f"{_safe(_library_modules['subprocess'].SUBPROCESS_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['configparser'].CONFIGPARSER_PATTERN).sub(lambda m: f"{_safe(_library_modules['configparser'].CONFIGPARSER_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['dataclasses'].DATACLASSES_PATTERN).sub(lambda m: f"{_safe(_library_modules['dataclasses'].DATACLASSES_FUNCS, m.group(1))}(", text)
    text = re.compile(r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(_library_modules['advanced'].ADVANCED_ORD_FUNCS, key=len, reverse=True)) + r")\s*\(").sub(lambda m: _safe(_library_modules['advanced'].ADVANCED_ORD_FUNCS, m.group(1)) + "(", text)
    text = re.compile(r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(_library_modules['advanced'].ADVANCED_BUILTIN_FUNCS, key=len, reverse=True)) + r")\s*\(").sub(lambda m: _safe(_library_modules['advanced'].ADVANCED_BUILTIN_FUNCS, m.group(1)) + "(", text)
    text = re.compile(r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(_library_modules['advanced'].ADVANCED_STR_FUNCS, key=len, reverse=True)) + r")\s*\(").sub(lambda m: _safe(_library_modules['advanced'].ADVANCED_STR_FUNCS, m.group(1)) + "(", text)
    text = re.compile(_library_modules['advanced'].ADVANCED_METHOD_PATTERN).sub(lambda m: f".{_library_modules['advanced'].ADVANCED_METHODS[m.group(1)]}(", text)
    text = re.compile(_library_modules['advanced'].ADVANCED_PATTERN).sub(lambda m: f"{_safe(_library_modules['advanced'].ADVANCED_FUNCS, m.group(1))}(", text)
    
    text = re.compile(_library_modules['datetime'].DATETIME_CONSTANT_PATTERN).sub(lambda m: _safe(_library_modules['datetime'].DATETIME_CONSTANTS, m.group(1)), text)
    text = re.compile(_library_modules['uuid'].UUID_CONSTANT_PATTERN).sub(lambda m: _safe(_library_modules['uuid'].UUID_CONSTANTS, m.group(1)), text)

    text = re.compile(_library_modules['decimal'].DECIMAL_PATTERN).sub(lambda m: f"{_safe(_library_modules['decimal'].DECIMAL_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['decimal'].DECIMAL_CONSTANT_PATTERN).sub(lambda m: _safe(_library_modules['decimal'].DECIMAL_CONSTANTS, m.group(1)), text)
    text = re.compile(_library_modules['fractions'].FRACTIONS_PATTERN).sub(lambda m: f"{_safe(_library_modules['fractions'].FRACTIONS_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['fractions'].FRACTIONS_METHOD_PATTERN).sub(lambda m: f".{_library_modules['fractions'].FRACTIONS_METHODS[m.group(1)]}(", text)
    text = re.compile(_library_modules['fractions'].FRACTIONS_PROP_PATTERN).sub(lambda m: f".{_safe(_library_modules['fractions'].FRACTIONS_PROPS, m.group(1))}", text)
    text = re.compile(_library_modules['string'].STRING_CONSTANT_PATTERN).sub(lambda m: _safe(_library_modules['string'].STRING_CONSTANTS, m.group(1)), text)
    text = re.compile(_library_modules['string'].STRING_PATTERN).sub(lambda m: f"{_safe(_library_modules['string'].STRING_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['secrets'].SECRETS_PATTERN).sub(lambda m: f"{_safe(_library_modules['secrets'].SECRETS_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['zoneinfo'].ZONEINFO_PATTERN).sub(lambda m: f"{_safe(_library_modules['zoneinfo'].ZONEINFO_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['zoneinfo'].ZONEINFO_CONSTANT_PATTERN).sub(lambda m: _safe(_library_modules['zoneinfo'].ZONEINFO_CONSTANTS, m.group(1)), text)
    text = re.compile(_library_modules['zoneinfo'].ZONEINFO_PROP_PATTERN).sub(lambda m: f".{_safe(_library_modules['zoneinfo'].ZONEINFO_PROPS, m.group(1))}", text)
    text = re.compile(_library_modules['getpass'].GETPASS_PATTERN).sub(lambda m: f"{_safe(_library_modules['getpass'].GETPASS_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['operator'].OPERATOR_PATTERN).sub(lambda m: f"{_safe(_library_modules['operator'].OPERATOR_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['pprint'].PPRINT_PATTERN).sub(lambda m: f"{_safe(_library_modules['pprint'].PPRINT_FUNCS, m.group(1))}(", text)
    text = re.compile(_library_modules['enum'].ENUM_PATTERN).sub(
        lambda m: f"{_safe(_library_modules['enum'].ENUM_FUNCS, m.group(1))}(", text)
    # --- xml.etree: methods and properties run before the module-level calls,
    # so `عنصر.ابحث_الكل(...)` is not mistaken for a bare function call.
    text = re.compile(_library_modules['xml'].XML_METHOD_PATTERN).sub(
        lambda m: f".{_library_modules['xml'].XML_METHODS[m.group(1)]}(", text)
    text = re.compile(_library_modules['xml'].XML_PROP_PATTERN).sub(
        lambda m: f".{_safe(_library_modules['xml'].XML_PROPS, m.group(1))}", text)
    text = re.compile(_library_modules['xml'].XML_CONSTANT_PATTERN).sub(
        lambda m: _safe(_library_modules['xml'].XML_CONSTANTS, m.group(1)), text)
    text = re.compile(_library_modules['xml'].XML_PATTERN).sub(
        lambda m: f"{_safe(_library_modules['xml'].XML_FUNCS, m.group(1))}(", text)

    # --- archives: methods and properties first, then bare names
    text = re.compile(_library_modules['archive'].ARCHIVE_METHOD_PATTERN).sub(
        lambda m: f".{_library_modules['archive'].ARCHIVE_METHODS[m.group(1)]}(", text)
    text = re.compile(_library_modules['archive'].ARCHIVE_PROP_PATTERN).sub(
        lambda m: f".{_safe(_library_modules['archive'].ARCHIVE_PROPS, m.group(1))}", text)
    text = re.compile(_library_modules['archive'].ARCHIVE_CONSTANT_PATTERN).sub(
        lambda m: _safe(_library_modules['archive'].ARCHIVE_CONSTANTS, m.group(1)), text)
    text = re.compile(_library_modules['archive'].ARCHIVE_PATTERN).sub(
        lambda m: f"{_safe(_library_modules['archive'].ARCHIVE_FUNCS, m.group(1))}(", text)

    # Core language spellings have precedence over library exports. Library
    # additions must not turn conjunctions or the self alias into objects.
    _core_tokens = {}
    _core_words = {"ذات": "ذات", "و": "and", "أو": "or", "ليس": "not",
                   "صواب": "True", "خطأ": "False", "لا_شيء": "None", "لو": "if"}
    for _index, (_word, _target) in enumerate(_core_words.items()):
        _token = f"_APL_CORE_{_index}_END_"
        text = re.sub(rf"(?<![\w\u0600-\u06FF]){_word}(?![\w\u0600-\u06FF])", _token, text)
        _core_tokens[_token] = _target
    text = substitute_all(text, USER_NAMES)
    for _token, _target in _core_tokens.items():
        text = text.replace(_token, _target)

    # --- f-string interpolation: translate expressions inside {...} ---
    _APL_FSTR_RE = re.compile(r'(?P<pre>[fF])"[^"\\]*(?:\\.[^"\\]*)*"')

    def _apl_fstr_sub(_m):
        whole = _m.group(0)
        body = whole[2:-1]          # drop the f and the quotes
        out = []
        buf = ""
        depth = 0
        for ch in body:
            if ch == "{":
                if depth == 0:
                    out.append(("lit", buf))
                    buf = ""
                else:
                    buf += ch
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    out.append(("expr", buf))
                    buf = ""
                else:
                    buf += ch
            else:
                buf += ch
        out.append(("lit", buf))
        pieces = []
        for kind, val in out:
            if kind == "lit" or not val:
                pieces.append(val)
                continue
            m_spec = re.match(r"^(.*?)(:[^{}]*)?$", val, re.S)
            e = m_spec.group(1)
            spec = m_spec.group(2) or ""
            pieces.append("{" + _inline_replace(e) + spec + "}")
        return whole[0] + '"' + "".join(pieces) + '"'

    # Lambda inside an expression: "(س) => س * 2" -> "lambda س: س * 2"
    if "=>" in text:
        _APL_LAMBDA_RE = re.compile(r"\(\s*([^()]*?)\s*\)\s*=>\s*")
        def _apl_lambda_sub(m):
            params = m.group(1).strip()
            return f"lambda {params}: "
        text = _APL_LAMBDA_RE.sub(_apl_lambda_sub, text)

    text = _APL_FSTR_RE.sub(_apl_fstr_sub, text)

    # Library-specific keyword arguments (e.g. timedelta(days=3))
    for _kmap in (DATETIME_KWARGS, PATHLIB_KWARGS, XML_KWARGS, ARCHIVE_KWARGS, NET_KWARGS, ARGPARSE_KWARGS, _library_modules['devtools'].DEVTOOLS_KWARGS):
        for _ar, _en in _kmap.items():
            text = re.sub(rf"(?<![\w\u0600-\u06FF]){_ar}(?=\s*=)", _en, text)


    # Standalone form of method aliases: علوي("x") -> "x".upper()
    for _ar, _en in _STANDALONE_METHODS.items():
        text = re.sub(rf"(?<![\w.\u0600-\u06FF]){_ar}\s*\(", f'_APL_SELF("{_en}", ', text)

    # Then type aliases, inline funcs, methods
    # Translate context manager protocol methods
    text = text.replace("__دخل__", "__enter__")
    text = text.replace("__خرج__", "__exit__")
    text = text.replace("__دخل_سياق__", "__enter__")
    text = text.replace("__خرج_سياق__", "__exit__")
    
    text = _TYPE_PATTERN.sub(lambda m: f"{_safe(TYPE_ALIASES, m.group(1))}(", text)
    text = _INLINE_FUNC_PATTERN.sub(lambda m: f"{_safe(_INLINE_FUNCS, m.group(1))}(", text)
    text = _METHOD_PATTERN.sub(lambda m: f".{_METHOD_ALIASES[m.group(1)]}(", text)
    text = _IO_PATTERN.sub(lambda m: f"{_safe(_IO_ALIASES, m.group(1))}(", text)
    text = re.sub(r"من\s*\(([^()]+)\)", lambda m: f"isinstance({_replace_type_names(m.group(1))})", text)
    text = _CONSTANT_PATTERN.sub(lambda m: _safe(_CONSTANTS, m.group(1)), text)
    for pat, repl in _LOGICAL_PATTERNS:
        text = pat.sub(repl, text)

    for ar, en in _KW_ALIASES.items():
        text = re.sub(rf"(?<!\w){ar}(?=\s*=)", en, text)

    text = re.sub(r"(?<!\w)سهم\s+(.+?):\s*(.+)", lambda m: f"lambda {m.group(1)}: {m.group(2)}", text)
    text = re.sub(r"(.+?)\sإذا\s(.+?)\sوالا\s(.+)", r"\1 if \2 else \3", text)


    # Translate expressions inside f-string interpolations: f"...{expr}..."
    def _apl_translate_fstring(_s):
        if not _s or _s[0] not in "fF":
            return _s
        quote = _s[1]
        body = _s[2:-1]
        out = []
        buf = ""
        depth = 0
        for ch in body:
            if ch == "{":
                if depth == 0:
                    out.append(("lit", buf))
                    buf = ""
                else:
                    buf += ch
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    out.append(("expr", buf))
                    buf = ""
                else:
                    buf += ch
            else:
                buf += ch
        out.append(("lit", buf))
        pieces = []
        for kind, val in out:
            if kind == "lit" or not val:
                pieces.append(val)
                continue
            m_spec = re.match(r"^(.*?)(:[^{}]*)?$", val, re.S)
            e = _inline_replace(m_spec.group(1))
            pieces.append("{" + e + (m_spec.group(2) or "") + "}")
        return _s[0] + quote + "".join(pieces) + quote

    for idx in sorted(strings.keys(), reverse=True):
        raw = strings[idx]
        text = text.replace(f"\x00APL{idx}\x00", _apl_translate_fstring(raw))
    for _token, _name in _name_tokens.items():
        text = text.replace(_token, _name)
    return text

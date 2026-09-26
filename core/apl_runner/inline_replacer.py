"""
APL - Inline Replacer
Handles all inline text replacements during transpilation
"""

import re
from core.apl_runner.patterns import (
    TYPE_ALIASES, _TYPE_PATTERN, _INLINE_FUNCS, _INLINE_FUNC_PATTERN,
    _METHOD_ALIASES, _METHOD_PATTERN, _TYPE_NAMES, _CONSTANTS, _CONSTANT_PATTERN,
    _LOGICAL_PATTERNS, _KW_ALIASES, _IO_ALIASES, _IO_PATTERN, _UDF_NAMES
)
from core.libraries.datetime_funcs import DATETIME_KWARGS
from core.libraries.pathlib_funcs import PATHLIB_KWARGS
from core.libraries import decimal_funcs, fractions_funcs, string_funcs, secrets_funcs, zoneinfo_funcs, getpass_funcs, operator_funcs, pprint_funcs

# Arabic names usable both as methods (.علوي) and standalone (علوي("x"))
_STANDALONE_METHODS = {
    "علوي": "upper", "سفلي": "lower", "تقليم": "strip",
    "تقسيم": "split", "استبدال": "replace", "عدد": "count",
    "يبدأ": "startswith", "ينتهي": "endswith", "ضم": "join",
    "فرز": "sort", "عكس": "reverse", "نسخ": "copy",
}
from core.libraries import math_funcs, random_funcs, time_funcs, statistics_funcs, os_funcs, re_funcs, collections_funcs, itertools_funcs, json_funcs, hashlib_funcs, flask_funcs, fastapi_funcs, requests_funcs, sqlite3_funcs, asyncio_funcs, threading_funcs, unittest_funcs, csv_funcs, logging_funcs, argparse_funcs, subprocess_funcs, configparser_funcs, dataclasses_funcs, advanced_funcs, datetime_funcs, pathlib_funcs, shutil_funcs, textwrap_funcs, uuid_funcs, base64_funcs, urllib_funcs, functools_funcs


def _replace_type_names(text: str) -> str:
    for arabic, english in _TYPE_NAMES.items():
        text = re.sub(rf"(?<!\w){arabic}(?!\\w)", english, text)
    return text


def _inline_replace(text: str) -> str:
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
    text = re.compile(datetime_funcs.DATETIME_PATTERN).sub(lambda m: f"{datetime_funcs.DATETIME_FUNCS[m.group(1)]}(", text)
    text = re.compile(pathlib_funcs.PATHLIB_PATTERN).sub(lambda m: f"{pathlib_funcs.PATHLIB_FUNCS[m.group(1)]}(", text)
    text = re.compile(pathlib_funcs.PATHLIB_METHOD_PATTERN).sub(lambda m: f".{pathlib_funcs.PATHLIB_METHODS[m.group(1)]}(", text)
    text = re.compile(shutil_funcs.SHUTIL_PATTERN).sub(lambda m: f"{shutil_funcs.SHUTIL_FUNCS[m.group(1)]}(", text)
    text = re.compile(textwrap_funcs.TEXTWRAP_PATTERN).sub(lambda m: f"{textwrap_funcs.TEXTWRAP_FUNCS[m.group(1)]}(", text)
    text = re.compile(uuid_funcs.UUID_PATTERN).sub(lambda m: f"{uuid_funcs.UUID_FUNCS[m.group(1)]}(", text)
    text = re.compile(datetime_funcs.DATETIME_PROP_PATTERN).sub(lambda m: f".{datetime_funcs.DATETIME_PROPS[m.group(1)]}", text)
    text = re.compile(pathlib_funcs.PATHLIB_PROP_PATTERN).sub(lambda m: f".{pathlib_funcs.PATHLIB_PROPS[m.group(1)]}", text)
    text = re.compile(uuid_funcs.UUID_PROP_PATTERN).sub(lambda m: f".{uuid_funcs.UUID_PROPS[m.group(1)]}", text)
    text = re.compile(base64_funcs.BASE64_PATTERN).sub(lambda m: f"{base64_funcs.BASE64_FUNCS[m.group(1)]}(", text)
    text = re.compile(urllib_funcs.URLLIB_PATTERN).sub(lambda m: f"{urllib_funcs.URLLIB_FUNCS[m.group(1)]}(", text)
    text = re.compile(functools_funcs.FUNCTOOLS_PATTERN).sub(lambda m: f"{functools_funcs.FUNCTOOLS_FUNCS[m.group(1)]}(", text)
    text = re.compile(math_funcs.MATH_CONSTANT_PATTERN).sub(lambda m: math_funcs.MATH_CONSTANTS[m.group(1)], text)
    text = re.compile(math_funcs.MATH_PATTERN).sub(lambda m: f"{math_funcs.MATH_FUNCS[m.group(1)]}(", text)
    text = re.compile(random_funcs.RANDOM_PATTERN).sub(lambda m: f"{random_funcs.RANDOM_FUNCS[m.group(1)]}(", text)
    text = re.compile(time_funcs.TIME_PATTERN).sub(lambda m: f"{time_funcs.TIME_FUNCS[m.group(1)]}(", text)
    text = re.compile(time_funcs.TIME_PROP_PATTERN).sub(lambda m: f"{time_funcs.TIME_PROPS[m.group(1)]}", text)
    text = re.compile(statistics_funcs.STATISTICS_PATTERN).sub(lambda m: f"{statistics_funcs.STATISTICS_FUNCS[m.group(1)]}(", text)
    text = re.compile(os_funcs.OS_PROP_PATTERN).sub(lambda m: f"({os_funcs.OS_PROPS[m.group(1)]})", text)
    text = re.compile(os_funcs.OS_PATTERN).sub(lambda m: f"{os_funcs.OS_FUNCS[m.group(1)]}(", text)
    text = re.compile(re_funcs.RE_CONSTANT_PATTERN).sub(lambda m: f"{re_funcs.RE_CONSTANTS[m.group(1)]}", text)
    text = re.compile(re_funcs.RE_PATTERN).sub(lambda m: f"{re_funcs.RE_FUNCS[m.group(1)]}(", text)
    text = re.compile(collections_funcs.COLLECTIONS_PATTERN).sub(lambda m: f"{collections_funcs.COLLECTIONS_FUNCS[m.group(1)]}(", text)
    text = re.compile(itertools_funcs.ITERTOOLS_PATTERN).sub(lambda m: f"{itertools_funcs.ITERTOOLS_FUNCS[m.group(1)]}(", text)
    text = re.compile(json_funcs.JSON_PATTERN).sub(lambda m: f"{json_funcs.JSON_FUNCS[m.group(1)]}(", text)
    text = re.compile(hashlib_funcs.HASHLIB_PATTERN).sub(lambda m: f"{hashlib_funcs.HASHLIB_FUNCS[m.group(1)]}(", text)
    text = re.compile(flask_funcs.FLASK_PATTERN).sub(lambda m: f"{flask_funcs.FLASK_FUNCS[m.group(1)]}(", text)
    text = re.compile(fastapi_funcs.FASTAPI_PATTERN).sub(lambda m: f"{fastapi_funcs.FASTAPI_FUNCS[m.group(1)]}(", text)
    text = re.compile(requests_funcs.REQUESTS_PATTERN).sub(lambda m: f"{requests_funcs.REQUESTS_FUNCS[m.group(1)]}(", text)
    text = re.compile(sqlite3_funcs.SQLITE3_PATTERN).sub(lambda m: f"{sqlite3_funcs.SQLITE3_FUNCS[m.group(1)]}(", text)
    text = re.compile(sqlite3_funcs.SQLITE3_METHOD_PATTERN).sub(lambda m: f".{sqlite3_funcs.SQLITE3_METHODS[m.group(1)]}(", text)
    text = re.compile(asyncio_funcs.ASYNCIO_PATTERN).sub(lambda m: f"{asyncio_funcs.ASYNCIO_FUNCS[m.group(1)]}(", text)
    text = re.compile(threading_funcs.THREADING_PATTERN).sub(lambda m: f"{threading_funcs.THREADING_FUNCS[m.group(1)]}(", text)
    text = re.compile(unittest_funcs.UNITTEST_PATTERN).sub(lambda m: f"{unittest_funcs.UNITTEST_FUNCS[m.group(1)]}(", text)
    text = re.compile(csv_funcs.CSV_PATTERN).sub(lambda m: f"{csv_funcs.CSV_FUNCS[m.group(1)]}(", text)
    text = re.compile(r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(logging_funcs.LOGGING_VERBS, key=len, reverse=True)) + r")\s*\(").sub(lambda m: logging_funcs.LOGGING_VERBS[m.group(1)] + "(", text)
    text = re.compile(logging_funcs.LOGGING_PATTERN).sub(lambda m: f"{logging_funcs.LOGGING_FUNCS[m.group(1)]}(", text)
    text = re.compile(r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(argparse_funcs.ARGPARSE_STANDALONE, key=len, reverse=True)) + r")\s*\(").sub(lambda m: argparse_funcs.ARGPARSE_STANDALONE[m.group(1)] + "(", text)
    text = re.compile(argparse_funcs.ARGPARSE_PATTERN).sub(lambda m: f"{argparse_funcs.ARGPARSE_FUNCS[m.group(1)]}(", text)
    text = re.compile(subprocess_funcs.SUBPROCESS_PATTERN).sub(lambda m: f"{subprocess_funcs.SUBPROCESS_FUNCS[m.group(1)]}(", text)
    text = re.compile(configparser_funcs.CONFIGPARSER_PATTERN).sub(lambda m: f"{configparser_funcs.CONFIGPARSER_FUNCS[m.group(1)]}(", text)
    text = re.compile(dataclasses_funcs.DATACLASSES_PATTERN).sub(lambda m: f"{dataclasses_funcs.DATACLASSES_FUNCS[m.group(1)]}(", text)
    text = re.compile(r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(advanced_funcs.ADVANCED_ORD_FUNCS, key=len, reverse=True)) + r")\s*\(").sub(lambda m: advanced_funcs.ADVANCED_ORD_FUNCS[m.group(1)] + "(", text)
    text = re.compile(r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(advanced_funcs.ADVANCED_BUILTIN_FUNCS, key=len, reverse=True)) + r")\s*\(").sub(lambda m: advanced_funcs.ADVANCED_BUILTIN_FUNCS[m.group(1)] + "(", text)
    text = re.compile(r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(advanced_funcs.ADVANCED_STR_FUNCS, key=len, reverse=True)) + r")\s*\(").sub(lambda m: advanced_funcs.ADVANCED_STR_FUNCS[m.group(1)] + "(", text)
    text = re.compile(advanced_funcs.ADVANCED_METHOD_PATTERN).sub(lambda m: f".{advanced_funcs.ADVANCED_METHODS[m.group(1)]}(", text)
    text = re.compile(advanced_funcs.ADVANCED_PATTERN).sub(lambda m: f"{advanced_funcs.ADVANCED_FUNCS[m.group(1)]}(", text)
    
    text = re.compile(datetime_funcs.DATETIME_CONSTANT_PATTERN).sub(lambda m: datetime_funcs.DATETIME_CONSTANTS[m.group(1)], text)
    text = re.compile(uuid_funcs.UUID_CONSTANT_PATTERN).sub(lambda m: uuid_funcs.UUID_CONSTANTS[m.group(1)], text)

    text = re.compile(decimal_funcs.DECIMAL_PATTERN).sub(lambda m: f"{decimal_funcs.DECIMAL_FUNCS[m.group(1)]}(", text)
    text = re.compile(decimal_funcs.DECIMAL_CONSTANT_PATTERN).sub(lambda m: decimal_funcs.DECIMAL_CONSTANTS[m.group(1)], text)
    text = re.compile(fractions_funcs.FRACTIONS_PATTERN).sub(lambda m: f"{fractions_funcs.FRACTIONS_FUNCS[m.group(1)]}(", text)
    text = re.compile(fractions_funcs.FRACTIONS_METHOD_PATTERN).sub(lambda m: f".{fractions_funcs.FRACTIONS_METHODS[m.group(1)]}(", text)
    text = re.compile(fractions_funcs.FRACTIONS_PROP_PATTERN).sub(lambda m: f".{fractions_funcs.FRACTIONS_PROPS[m.group(1)]}", text)
    text = re.compile(string_funcs.STRING_CONSTANT_PATTERN).sub(lambda m: string_funcs.STRING_CONSTANTS[m.group(1)], text)
    text = re.compile(string_funcs.STRING_PATTERN).sub(lambda m: f"{string_funcs.STRING_FUNCS[m.group(1)]}(", text)
    text = re.compile(secrets_funcs.SECRETS_PATTERN).sub(lambda m: f"{secrets_funcs.SECRETS_FUNCS[m.group(1)]}(", text)
    text = re.compile(zoneinfo_funcs.ZONEINFO_PATTERN).sub(lambda m: f"{zoneinfo_funcs.ZONEINFO_FUNCS[m.group(1)]}(", text)
    text = re.compile(zoneinfo_funcs.ZONEINFO_CONSTANT_PATTERN).sub(lambda m: zoneinfo_funcs.ZONEINFO_CONSTANTS[m.group(1)], text)
    text = re.compile(zoneinfo_funcs.ZONEINFO_PROP_PATTERN).sub(lambda m: f".{zoneinfo_funcs.ZONEINFO_PROPS[m.group(1)]}", text)
    text = re.compile(getpass_funcs.GETPASS_PATTERN).sub(lambda m: f"{getpass_funcs.GETPASS_FUNCS[m.group(1)]}(", text)
    text = re.compile(operator_funcs.OPERATOR_PATTERN).sub(lambda m: f"{operator_funcs.OPERATOR_FUNCS[m.group(1)]}(", text)
    text = re.compile(pprint_funcs.PPRINT_PATTERN).sub(lambda m: f"{pprint_funcs.PPRINT_FUNCS[m.group(1)]}(", text)

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

    text = _APL_FSTR_RE.sub(_apl_fstr_sub, text)
    if 'f"' in text and 'مقرب' in text: print('FSTR-PASS-RAN', file=__import__('sys').stderr)

    # Library-specific keyword arguments (e.g. timedelta(days=3))
    for _kmap in (DATETIME_KWARGS, PATHLIB_KWARGS):
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
    
    text = _TYPE_PATTERN.sub(lambda m: f"{TYPE_ALIASES[m.group(1)]}(", text)
    text = _INLINE_FUNC_PATTERN.sub(lambda m: f"{_INLINE_FUNCS[m.group(1)]}(", text)
    text = _METHOD_PATTERN.sub(lambda m: f".{_METHOD_ALIASES[m.group(1)]}(", text)
    text = _IO_PATTERN.sub(lambda m: f"{_IO_ALIASES[m.group(1)]}(", text)
    text = re.sub(r"من\s*\(([^()]+)\)", lambda m: f"isinstance({_replace_type_names(m.group(1))})", text)
    text = _CONSTANT_PATTERN.sub(lambda m: _CONSTANTS[m.group(1)], text)
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
    return text

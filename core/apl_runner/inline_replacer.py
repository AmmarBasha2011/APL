"""
APL - Inline Replacer
Handles all inline text replacements during transpilation
"""

import re
from core.apl_runner.patterns import (
    TYPE_ALIASES, _TYPE_PATTERN, _INLINE_FUNCS, _INLINE_FUNC_PATTERN,
    _METHOD_ALIASES, _METHOD_PATTERN, _TYPE_NAMES, _CONSTANTS, _CONSTANT_PATTERN,
    _LOGICAL_PATTERNS, _KW_ALIASES, _IO_ALIASES, _IO_PATTERN
)
from core.libraries import math_funcs, random_funcs, time_funcs, statistics_funcs, os_funcs, re_funcs, collections_funcs, itertools_funcs, json_funcs, hashlib_funcs, flask_funcs, fastapi_funcs, requests_funcs


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
    
    # Then type aliases, inline funcs, methods
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

    for idx in sorted(strings.keys(), reverse=True):
        text = text.replace(f"\x00APL{idx}\x00", strings[idx])
    return text

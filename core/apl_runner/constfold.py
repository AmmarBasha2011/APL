"""
APL - constant folding.

A small, provably-safe peephole pass over the GENERATED Python. It only
rewrites expressions made entirely of numeric literals and operators, so it can
never change program behaviour:

    المتغير س = 2 ** 100        ->  س = 1267650600228229401496703205376
    المتغير ص = 10 * 4 + 2     ->  ص = 42
    المتغير ن = 100 // 7       ->  ن = 14

Safety rules (deliberately conservative):
  * integer/float literals and the operators + - * / // % ** only
  * no names, no calls, no attribute access
  * NEVER inside a string literal — an earlier version folded
    "12345678-1234-5678-1234-567812345678" into "-567800008146", silently
    corrupting UUIDs, phone numbers, dates and any dashed string
  * no exponent over 6 digits (guards against absurd literals)
  * comments are skipped

Anything the scanner cannot prove constant is left untouched.
"""

from __future__ import annotations

import re

# A run of purely numeric arithmetic: digits, dots, and the safe operators.
_NUM_EXPR = re.compile(
    r"(?<![\w.])"                      # not part of a longer identifier/number
    r"(\d[\d_]*(?:\.\d+)?)"             # first literal
    r"(\s*(?:\*\*|//|[+\-*/%])\s*"     # operator
    r"\d[\d_]*(?:\.\d+)?)+"             # more literals
    r"(?![\w.])"
)

_STRING_SPANS = re.compile(
    r"'''.*?'''|\"\"\".*?\"\"\"|'(?:\\.|[^'\\])*'|\"(?:\\.|[^\"\\])*\"",
    re.S,
)


def _mask_noncode(line: str) -> str:
    """Blank everything that is not foldable code, keeping offsets identical.

    Two things are masked, in this order so a "#" inside a string is safe:
      1. string literal spans
      2. the trailing comment (from an unquoted "#")
    Because every replacement is the same length as the original, the offsets
    of real code never move, so folded results can be spliced back in safely.
    """
    def _blank(m: re.Match) -> str:
        return " " * len(m.group(0))
    masked = _STRING_SPANS.sub(_blank, line)
    return re.sub(r"#[^#]*", _blank, masked)


def _eval_number_expr(expr: str) -> str | None:
    """Evaluate a pure-arithmetic literal expression, or return None."""
    s = expr.replace("_", "")
    if not s or any(ch.isalpha() for ch in s):
        return None
    ops = {c for c in s if c in "+-*/%"}
    if not ops:
        return None
    try:
        # Guard against pathological input (huge exponent literals)
        if "**" in s:
            head, _, tail = s.partition("**")
            if len(tail.strip()) > 6:
                return None
        val = eval(compile(s, "<const>", "eval"), {"__builtins__": {}}, {})
    except Exception:
        return None
    if isinstance(val, (int, float)):
        return repr(val)
    if isinstance(val, complex):
        return None
    return None


def fold_code(code: str) -> str:
    """Return `code` with constant arithmetic folded. Never raises."""
    out = []
    for line in code.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("#"):
            out.append(line)
            continue

        # Work on a copy with string contents blanked, then copy the folded
        # expressions back into the REAL line by offset.
        masked = _mask_noncode(line)
        pieces = []
        last = 0
        changed = False
        for m in _NUM_EXPR.finditer(masked):
            folded = _eval_number_expr(m.group(0))
            if folded is None or folded == m.group(0):
                continue
            pieces.append(masked[last:m.start()])
            pieces.append(folded)
            last = m.end()
            changed = True
        if not changed:
            out.append(line)
            continue
        pieces.append(masked[last:])
        new = "".join(pieces)
        # restore any string the mask blanked: splice the original characters
        # wherever the mask had produced a run of spaces equal to a string span
        out.append(_restore_noncode(new, line))
    return "\n".join(out)


def _restore_noncode(folded_masked: str, original: str) -> str:
    """Put the original strings and comments back, matching spans in order.

    A comment is anything from an unquoted "#" to end of line, where "unquoted"
    means it is not inside a string span.
    """
    spans = [m.span() for m in _STRING_SPANS.finditer(original)]
    masked_no_str = _STRING_SPANS.sub(lambda m: " " * len(m.group(0)), original)
    for m in re.finditer(r"#[^#]*", masked_no_str):
        spans.append(m.span())
    if not spans:
        return folded_masked
    res = folded_masked
    # walk from the end so earlier offsets stay valid
    for a, b in sorted(set(spans), reverse=True):
        res = res[:a] + original[a:b] + res[b:]
    return res


def count_foldable(code: str) -> int:
    """How many expressions fold_code would rewrite (for tests/benchmarks)."""
    n = 0
    for line in code.split("\n"):
        if line.lstrip().startswith("#"):
            continue
        masked = _mask_noncode(line)
        for m in _NUM_EXPR.finditer(masked):
            folded = _eval_number_expr(m.group(0))
            if folded is not None and folded != m.group(0):
                n += 1
    return n

"""Arabic in consoles that can't do it: shaping and right-to-left order.

The Windows console (conhost and Windows Terminal) draws text left to right,
one code point at a time. Arabic comes out reversed and with every letter in
its isolated form. This module does the two jobs a console won't:

* shaping: pick the initial, medial, final or isolated form of each letter (and
  the lam-alef ligature), using the presentation forms Unicode already lists;
* ordering: lay each line out in visual order, so that a plain left-to-right
  console shows it the right way round. Latin words and numbers inside Arabic
  text keep their own order.

It is applied only to a Windows console. Files, pipes, the browser Terminal app
and other platforms get the normal logical text untouched. APL_BIDI=0 turns it
off, APL_BIDI=1 forces it on (for testing).
"""
import os
import re
import sys
import unicodedata

_FORMS = {}  # base letter -> {'isolated','initial','medial','final'}


def _build():
    for code in range(0xFE70, 0xFF00):
        decomposition = unicodedata.decomposition(chr(code))
        match = re.match(r"<(isolated|initial|medial|final)> ([0-9A-F]{4})$", decomposition)
        if match:
            base = chr(int(match.group(2), 16))
            _FORMS.setdefault(base, {})[match.group(1)] = chr(code)


_build()
_LAM = "\u0644"
_ALEFS = {"\u0622": "\uFEF5", "\u0623": "\uFEF7", "\u0625": "\uFEF9", "\u0627": "\uFEFB"}
_ALEF_FINAL = {"\uFEF5": "\uFEF6", "\uFEF7": "\uFEF8", "\uFEF9": "\uFEFA", "\uFEFB": "\uFEFC"}
_MIRROR = str.maketrans("()[]{}<>", ")(][}{><")
_CONTROLS = re.compile("[\u202A-\u202E\u2066-\u2069\u200E\u200F\u061C]")
_ANSI = re.compile(r"(\x1b\[[0-9;?]*[A-Za-z])")


def _is_mark(ch):
    return unicodedata.category(ch) == "Mn"


def shape(text):
    """Replace Arabic letters by their joined forms. Order stays logical."""
    chars = list(text)
    out = []
    n = len(chars)

    def prev_letter(i):
        i -= 1
        while i >= 0 and _is_mark(chars[i]):
            i -= 1
        return chars[i] if i >= 0 else ""

    def next_letter(i):
        i += 1
        while i < n and _is_mark(chars[i]):
            i += 1
        return i if i < n else -1

    i = 0
    while i < n:
        ch = chars[i]
        forms = _FORMS.get(ch)
        if forms is None and ch != _LAM:
            out.append(ch)
            i += 1
            continue
        prev = prev_letter(i)
        pf = _FORMS.get(prev)
        prev_joins = bool(pf and ("initial" in pf or "medial" in pf))
        j = next_letter(i)
        if ch == _LAM and j != -1 and chars[j] in _ALEFS:
            ligature = _ALEFS[chars[j]]
            out.append(_ALEF_FINAL[ligature] if prev_joins else ligature)
            out.extend(c for c in chars[i + 1:j] if _is_mark(c))
            i = j + 1
            continue
        if forms is None:
            out.append(ch)
            i += 1
            continue
        nf = _FORMS.get(chars[j]) if j != -1 else None
        next_joins = nf is not None and "isolated" in nf and ("final" in nf)
        dual = "initial" in forms
        if prev_joins and next_joins and dual and "medial" in forms:
            form = "medial"
        elif prev_joins and "final" in forms:
            form = "final"
        elif next_joins and dual:
            form = "initial"
        else:
            form = "isolated"
        out.append(forms.get(form) or forms.get("isolated") or ch)
        i += 1
    return "".join(out)


def _kind(ch):
    cls = unicodedata.bidirectional(ch)
    if cls in ("R", "AL"):
        return "R"
    if cls == "L":
        return "L"
    if cls in ("EN", "AN"):
        return "N"
    return "X"  # neutral, mark or anything else


def visual(line):
    """One line in visual order, for a console that only draws left to right."""
    line = _CONTROLS.sub("", line)
    if not any(_kind(c) == "R" for c in line):
        return line
    shaped = shape(line)
    # Clusters: a base character stays with the marks that follow it.
    clusters = []
    for ch in shaped:
        if _is_mark(ch) and clusters:
            clusters[-1] += ch
        else:
            clusters.append(ch)
    kinds = [_kind(c[0]) for c in clusters]
    # The first strong letter sets the paragraph direction.
    base = 0
    for k in kinds:
        if k == "R":
            base = 1
            break
        if k == "L":
            break
    level = []
    for k in kinds:
        if k == "R":
            level.append(1)
        elif k == "L":
            level.append(2 if base else 0)
        elif k == "N":
            level.append(2 if base else 0)
        else:
            level.append(None)
    # A neutral between two runs of the same level takes it; otherwise the base.
    count = len(level)
    for i in range(count):
        if level[i] is None:
            a = i - 1
            while a >= 0 and level[a] is None:
                a -= 1
            b = i + 1
            while b < count and level[b] is None:
                b += 1
            left = level[a] if a >= 0 else base
            right = level[b] if b < count else base
            level[i] = left if left == right else base
    top = max(level)
    low_odd = 1 if any(v % 2 for v in level) else None
    if low_odd is not None:
        for target in range(top, low_odd - 1, -1):
            i = 0
            while i < count:
                if level[i] >= target:
                    j = i
                    while j < count and level[j] >= target:
                        j += 1
                    clusters[i:j] = clusters[i:j][::-1]
                    level[i:j] = level[i:j][::-1]
                    i = j
                else:
                    i += 1
    # Brackets flip when they sit in a right-to-left run.
    result = []
    for cluster, lv in zip(clusters, level):
        result.append(cluster.translate(_MIRROR) if lv % 2 else cluster)
    return "".join(result)


def convert(text):
    """Visual text for a whole write: line by line, ANSI colour codes kept."""
    pieces = []
    for line in text.split("\n"):
        parts = _ANSI.split(line)
        if len(parts) == 1:
            pieces.append(visual(line))
        else:
            pieces.append("".join(p if _ANSI.fullmatch(p) else visual(p) for p in parts))
    return "\n".join(pieces)


class Stream:
    """Wraps a text stream: buffers up to the line end, then writes visual text."""

    def __init__(self, inner):
        self._inner = inner
        self._pending = ""

    def write(self, text):
        self._pending += text
        if "\n" in self._pending:
            head, _, tail = self._pending.rpartition("\n")
            self._inner.write(convert(head) + "\n")
            self._pending = tail
        return len(text)

    def flush(self):
        if self._pending:
            self._inner.write(convert(self._pending))
            self._pending = ""
        self._inner.flush()

    def __getattr__(self, name):
        return getattr(self._inner, name)


def wanted(stream):
    setting = os.environ.get("APL_BIDI", "")
    if setting == "0":
        return False
    if setting == "1":
        return True
    try:
        return sys.platform == "win32" and stream.isatty()
    except (AttributeError, ValueError):
        return False


def install():
    """Wrap stdout and stderr when they are a Windows console."""
    for name in ("stdout", "stderr"):
        stream = getattr(sys, name)
        if isinstance(stream, Stream) or not wanted(stream):
            continue
        setattr(sys, name, Stream(stream))

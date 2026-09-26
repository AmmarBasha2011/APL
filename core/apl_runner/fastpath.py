"""
APL - fast identifier gate for the inline replacer.

The inline replacer runs up to 66 compiled regex passes per source line. Almost
every line in a real program contains no library call at all, yet all 66
patterns still scan it.

`needs_scan()` is a single cheap check: if the line has no Arabic letter
followed by "(" / "." / a space, none of those patterns can match, so the
caller can skip the whole chain.

This is a pure short-circuit — it never changes output, only avoids work.
"""

from __future__ import annotations

import re

# Any Arabic letter anywhere. This is the only safe gate: bare constants
# (صواب / خطأ / لا_شيء) have no "(" or "." after them, so a stricter check
# silently skipped them.
_HAS_ARABIC = re.compile(r"[\u0600-\u06FF]")


def has_arabic(text: str) -> bool:
    return bool(_HAS_ARABIC.search(text))


def needs_scan(text: str) -> bool:
    """True when a library pattern could possibly match this text.

    Every library pattern keys on an Arabic identifier, so the presence of any
    Arabic letter is both necessary and sufficient as a pre-filter. An earlier
    version required a following "(" / "." / "," and wrongly skipped bare
    constants like صواب and خطأ.
    """
    return bool(_HAS_ARABIC.search(text))

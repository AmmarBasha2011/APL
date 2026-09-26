"""
APL - transpilation cache.

Running `apl program.apl` used to re-transpile the source on every launch. For
a 10,000-line program that is ~1.6 s of pure regex work, repeated for no reason:
the source never changed.

This module caches the TRANSPLED PYTHON next to the source (in __pycache__),
keyed by a SHA-256 of the APL source plus an engine tag. On a cache hit the
transpile step is skipped entirely. CPython then compiles the cached .py to its
own .pyc on the first run and reuses that afterwards, so a warm run does no
transpile AND no parse.

Set APL_NO_CACHE=1 to disable. `python apl.py --clear-cache` removes entries.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path

ENV_DISABLE = "APL_NO_CACHE"
CACHE_DIRNAME = "__pycache__"
# Cache key inputs. The engine fingerprint means ANY change to the transpiler
# automatically invalidates every cached translation — a hand-written version
# string is always forgotten at some point (it was: a stale cache kept serving
# translations from before a bug fix and failed 7 example tests).
_SRC_ROOT = Path(__file__).resolve().parents[2]


def _engine_fingerprint() -> str:
    """SHA-256 over every engine source file that affects translation."""
    h = hashlib.sha256()
    for rel in (
        "core/apl_runner/main.py",
        "core/apl_runner/transpiler.py",
        "core/apl_runner/inline_replacer.py",
        "core/apl_runner/patterns.py",
        "core/apl_runner/fastpath.py",
    ):
        p = _SRC_ROOT / rel
        try:
            h.update(rel.encode("utf-8"))
            h.update(p.read_bytes())
        except OSError:
            h.update(rel.encode("utf-8"))
    return h.hexdigest()[:12]


_ENGINE_TAG = "apl-cache-v1"


def enabled() -> bool:
    return os.environ.get(ENV_DISABLE, "") not in ("1", "true", "yes")


def _key(source: str) -> str:
    h = hashlib.sha256()
    h.update(_ENGINE_TAG.encode("ascii"))
    h.update(_engine_fingerprint().encode("ascii"))
    h.update(b"\x00")
    h.update(source.encode("utf-8"))
    return h.hexdigest()[:32]


def cache_dir(source_path: Path) -> Path:
    d = source_path.parent / CACHE_DIRNAME
    d.mkdir(parents=True, exist_ok=True)
    return d


def cache_path(source_path: Path, source: str) -> Path:
    return cache_dir(source_path) / (source_path.stem + "." + _key(source) + ".py")


def load_cached(source_path: Path, source: str) -> str | None:
    """Return the cached Python translation, or None on a miss."""
    if not enabled():
        return None
    p = cache_path(source_path, source)
    try:
        if p.is_file():
            return p.read_text(encoding="utf-8")
    except OSError:
        return None
    return None


def store(source_path: Path, source: str, python_code: str) -> None:
    """Save a successful translation. Never raises."""
    if not enabled():
        return
    try:
        p = cache_path(source_path, source)
        tmp = p.with_suffix(".py.tmp")
        tmp.write_text(python_code, encoding="utf-8")
        os.replace(tmp, p)
    except OSError:
        pass


def clear(source_path: Path | None = None) -> int:
    """Delete cached translations. Returns how many files were removed."""
    removed = 0
    if source_path is not None:
        d = source_path.parent / CACHE_DIRNAME
        pat = source_path.stem + ".*.py"
        for f in (d.glob(pat) if d.is_dir() else []):
            try:
                f.unlink()
                removed += 1
            except OSError:
                pass
        return removed

    for d in Path.cwd().rglob(CACHE_DIRNAME):
        if not d.is_dir():
            continue
        for f in d.glob("*.py"):
            # only our generated files, never a real .pyc
            if len(f.name.split(".")) >= 3 and f.name.endswith(".py"):
                try:
                    f.unlink()
                    removed += 1
                except OSError:
                    pass
    return removed


def prune(source_path: Path, keep: int = 3) -> None:
    """Keep only the newest `keep` cache entries for a source file."""
    d = source_path.parent / CACHE_DIRNAME
    if not d.is_dir():
        return
    entries = sorted(
        d.glob(source_path.stem + ".*.py"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    for old in entries[keep:]:
        try:
            old.unlink()
        except OSError:
            pass

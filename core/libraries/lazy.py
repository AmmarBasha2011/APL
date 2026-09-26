"""
APL - lazy library loading.

The engine used to import all 41 library modules on EVERY start and build
1,956 regex patterns before running a single line. That cost ~106 ms per
process — paid even by `apl.py -c "اطبع 1"`.

This module loads a library module only when its Arabic key is actually seen in
the source. A program that only does arithmetic never touches `flask_funcs`,
`requests_funcs` or `sqlite3_funcs`.

The public surface stays identical: `lazy.<name>_funcs` returns the real module,
and `dir()`/`getattr()` still work, so existing code (patterns, audit scripts,
docs tooling) is unaffected.
"""

from __future__ import annotations

import importlib
import sys
from types import ModuleType

# module basename -> library key it defines (module name without "_funcs")
_MODULE_NAMES = [
    "math", "random", "time", "statistics", "os", "re", "collections", "itertools",
    "json", "hashlib", "flask", "fastapi", "requests", "sqlite3", "asyncio",
    "threading", "unittest", "csv", "logging", "argparse", "subprocess",
    "configparser", "dataclasses", "advanced", "datetime", "pathlib", "shutil",
    "textwrap", "uuid", "base64", "urllib", "functools", "decimal", "fractions",
    "string", "secrets", "zoneinfo", "getpass", "operator", "pprint", "enum",
]

_loaded: dict[str, ModuleType] = {}
_loading: set[str] = set()


def loaded_modules() -> list[str]:
    """Names of the library modules actually imported so far (sorted)."""
    return sorted(_loaded)


def load(name: str) -> ModuleType:
    """Import one library module by its short name (e.g. "math")."""
    if name in _loaded:
        return _loaded[name]
    mod = importlib.import_module("core.libraries." + name + "_funcs")
    _loaded[name] = mod
    return mod


def is_loaded(name: str) -> bool:
    return name in _loaded


class _LazyModule:
    """Module proxy that imports the real module on first attribute access."""

    __slots__ = ("_lazy_name", "_lazy_real")

    def __init__(self, name: str) -> None:
        object.__setattr__(self, "_lazy_name", name)
        object.__setattr__(self, "_lazy_real", None)

    def _resolve(self) -> ModuleType:
        real = object.__getattribute__(self, "_lazy_real")
        if real is None:
            real = load(object.__getattribute__(self, "_lazy_name"))
            object.__setattr__(self, "_lazy_real", real)
        return real

    def __getattr__(self, item):
        return getattr(self._resolve(), item)

    def __setattr__(self, key, value):
        setattr(self._resolve(), key, value)

    def __dir__(self):
        return dir(self._resolve())

    def __repr__(self):
        state = "loaded" if object.__getattribute__(self, "_lazy_real") else "lazy"
        return f"<APL lazy module {object.__getattribute__(self, '_lazy_name')!r} ({state})>"


def install() -> None:
    """Register a lazy proxy for every library module in sys.modules.

    Call this BEFORE any `from core.libraries import x_funcs` so the import
    statement itself becomes free — it only creates a proxy object.
    """
    import core.libraries as _pkg

    for name in _MODULE_NAMES:
        full = f"core.libraries.{name}_funcs"
        if full in sys.modules:
            continue
        proxy = _LazyModule(name)
        sys.modules[full] = proxy
        setattr(_pkg, f"{name}_funcs", proxy)


def unload_all() -> None:
    """Testing helper: forget every cached module."""
    _loaded.clear()

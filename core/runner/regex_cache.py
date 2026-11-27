"""Local regex facade with a bounded cache for stable dispatch patterns.

Large optional libraries exceed re's process-wide cache. Keep their import
and replacement patterns here so scanning one library does not repeatedly
recompile the translator's syntax patterns. Never change the global re cache.
"""
from functools import lru_cache
import re as _re


@lru_cache(maxsize=8192)
def compile(pattern, flags=0):
    return _re.compile(pattern, flags)


def search(pattern, string, flags=0):
    return compile(pattern, flags).search(string)


def match(pattern, string, flags=0):
    return compile(pattern, flags).match(string)


def fullmatch(pattern, string, flags=0):
    return compile(pattern, flags).fullmatch(string)


def sub(pattern, repl, string, count=0, flags=0):
    return compile(pattern, flags).sub(repl, string, count)


def __getattr__(name):
    return getattr(_re, name)

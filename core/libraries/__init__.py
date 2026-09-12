"""
APL Libraries Package
Each module provides transpilation for a Python standard library module.
"""

from . import math_funcs
from . import random_funcs
from . import time_funcs
from . import statistics_funcs
from . import os_funcs
from . import re_funcs
from . import collections_funcs
from . import itertools_funcs
from . import json_funcs
from . import hashlib_funcs
from . import flask_funcs
from . import fastapi_funcs
from . import requests_funcs

# Registry: module references for easy access
LIBRARIES = {
    "math": math_funcs,
    "random": random_funcs,
    "time": time_funcs,
    "statistics": statistics_funcs,
    "os": os_funcs,
    "re": re_funcs,
    "collections": collections_funcs,
    "itertools": itertools_funcs,
    "json": json_funcs,
    "hashlib": hashlib_funcs,
    "flask": flask_funcs,
    "fastapi": fastapi_funcs,
    "requests": requests_funcs,
}

def get_all_funcs():
    """Return a dict of {pattern_name: (funcs_dict, pattern, import_info)}"""
    result = {}
    for name, mod in LIBRARIES.items():
        pattern_name = name.upper() + "_PATTERN"
        result[name] = {
            "funcs": getattr(mod, name.upper() + "_FUNCS"),
            "pattern": getattr(mod, pattern_name),
            "import_name": mod.IMPORT_NAME,
            "import_check": mod.IMPORT_CHECK,
            "import_statement": mod.IMPORT_STATEMENT,
        }
    return result

def get_all_help():
    """Return help text lines for all libraries"""
    lines = []
    for name, mod in LIBRARIES.items():
        lines.append(f"# {name} library")
        for help_line in mod.HELP:
            lines.append(help_line)
        lines.append("")
    return lines

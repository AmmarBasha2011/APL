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
from . import sqlite3_funcs
from . import asyncio_funcs
from . import threading_funcs
from . import unittest_funcs
from . import csv_funcs
from . import logging_funcs
from . import argparse_funcs
from . import subprocess_funcs
from . import configparser_funcs
from . import dataclasses_funcs
from . import advanced_funcs

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
    "sqlite3": sqlite3_funcs,
    "asyncio": asyncio_funcs,
    "threading": threading_funcs,
    "unittest": unittest_funcs,
    "csv": csv_funcs,
    "logging": logging_funcs,
    "argparse": argparse_funcs,
    "subprocess": subprocess_funcs,
    "configparser": configparser_funcs,
    "dataclasses": dataclasses_funcs,
    "advanced": advanced_funcs,
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

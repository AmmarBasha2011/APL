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
from . import decimal_funcs
from . import fractions_funcs
from . import string_funcs
from . import secrets_funcs
from . import zoneinfo_funcs
from . import getpass_funcs
from . import operator_funcs
from . import pprint_funcs
from . import enum_funcs
from . import datetime_funcs
from . import pathlib_funcs
from . import shutil_funcs
from . import textwrap_funcs
from . import uuid_funcs
from . import base64_funcs
from . import urllib_funcs
from . import functools_funcs

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
    "datetime": datetime_funcs,
    "pathlib": pathlib_funcs,
    "shutil": shutil_funcs,
    "textwrap": textwrap_funcs,
    "uuid": uuid_funcs,
    "base64": base64_funcs,
    "urllib": urllib_funcs,
    "functools": functools_funcs,
    "decimal": decimal_funcs,
    "fractions": fractions_funcs,
    "string": string_funcs,
    "secrets": secrets_funcs,
    "zoneinfo": zoneinfo_funcs,
    "getpass": getpass_funcs,
    "operator": operator_funcs,
    "pprint": pprint_funcs,
    "enum": enum_funcs,
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


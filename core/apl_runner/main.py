import sys, os, re, io
from core.apl_runner import _inline_replace
from core.apl_runner.transpiler import transpile_line
from core.libraries import math_funcs, random_funcs, time_funcs, statistics_funcs, os_funcs, re_funcs, collections_funcs, itertools_funcs, json_funcs, hashlib_funcs, flask_funcs, fastapi_funcs, requests_funcs, sqlite3_funcs, asyncio_funcs, threading_funcs, unittest_funcs, csv_funcs, logging_funcs, argparse_funcs, subprocess_funcs, configparser_funcs, dataclasses_funcs, advanced_funcs

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.platform == "win32":
    import ctypes
    try:
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleOutputCP(65001)
        kernel32.SetConsoleCP(65001)
    except Exception:
        pass


def transpile(source: str) -> str:
    lines = source.split("\n")
    result = []
    for line in lines:
        try:
            result.append(transpile_line(line))
        except SyntaxError as e:
            result.append(f"# ERROR: {e}")
    code = "\n".join(result)

    needs = []
    if re.search(math_funcs.IMPORT_CHECK, code) and "import math" not in code:
        needs.append("import math")
    if re.search(random_funcs.IMPORT_CHECK, code) and "import random" not in code:
        needs.append("import random")
    if re.search(time_funcs.IMPORT_CHECK, code) and "import time" not in code:
        needs.append("import time")
        needs.append("import datetime")
    if re.search(statistics_funcs.IMPORT_CHECK, code) and "import statistics" not in code:
        needs.append("import statistics")
    if re.search(os_funcs.IMPORT_CHECK, code) and "import os" not in code:
        needs.append("import os")
        needs.append("import shutil")
    if re.search(re_funcs.IMPORT_CHECK, code) and "import re" not in code:
        needs.append("import re")
    if re.search(collections_funcs.IMPORT_CHECK, code) and "import collections" not in code:
        needs.append("import collections")
    if re.search(itertools_funcs.IMPORT_CHECK, code) and "import itertools" not in code:
        needs.append("import itertools")
    if re.search(json_funcs.IMPORT_CHECK, code) and "import json" not in code:
        needs.append("import json")
    if re.search(hashlib_funcs.IMPORT_CHECK, code) and "import hashlib" not in code:
        needs.append("import hashlib")
    if re.search(flask_funcs.IMPORT_CHECK, code) and "from flask import" not in code:
        needs.append("from flask import Flask, request, jsonify, render_template, redirect, url_for, abort, session, make_response")
    if re.search(fastapi_funcs.IMPORT_CHECK, code) and "from fastapi import" not in code:
        needs.append("from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, Request, Response, BackgroundTasks, WebSocket, File, UploadFile, Security")
    if re.search(requests_funcs.IMPORT_CHECK, code) and "import requests" not in code:
        needs.append("import requests")
    if re.search(sqlite3_funcs.IMPORT_CHECK, code) and "import sqlite3" not in code:
        needs.append("import sqlite3")
    if re.search(asyncio_funcs.IMPORT_CHECK, code) and "import asyncio" not in code:
        needs.append("import asyncio")
    if re.search(threading_funcs.IMPORT_CHECK, code) and "import threading" not in code:
        needs.append("import threading")
    if re.search(unittest_funcs.IMPORT_CHECK, code) and "import unittest" not in code:
        needs.append("import unittest")
    if re.search(csv_funcs.IMPORT_CHECK, code) and "import csv" not in code:
        needs.append("import csv")
    if re.search(logging_funcs.IMPORT_CHECK, code) and "import logging" not in code:
        needs.append("import logging")
    if re.search(argparse_funcs.IMPORT_CHECK, code) and "import argparse" not in code:
        needs.append("import argparse")
    if re.search(subprocess_funcs.IMPORT_CHECK, code) and "import subprocess" not in code:
        needs.append("import subprocess")
    if re.search(configparser_funcs.IMPORT_CHECK, code) and "import configparser" not in code:
        needs.append("import configparser")
    if re.search(dataclasses_funcs.IMPORT_CHECK, code) and "import dataclasses" not in code:
        needs.append("from dataclasses import dataclass, field, asdict, astuple, replace; from enum import Enum, IntEnum, IntFlag, Flag, auto, unique; from abc import ABC, abstractmethod")
    if re.search(advanced_funcs.IMPORT_CHECK, code) and "import functools" not in code:
        needs.append("import functools, multiprocessing, concurrent.futures, typing, contextlib, tempfile, zipfile, pathlib, heapq, bisect, queue, weakref, copy, secrets, struct, io, codecs, base64")
    if "json." in code and "import json" not in code:
        needs.append("import json")
    if "os." in code and "import os" not in code:
        needs.append("import os")
    if "datetime." in code and "import datetime" not in code:
        needs.append("import datetime")
    if "_apl_fetch" in code and "import urllib.request" not in code:
        needs.append("import urllib.request")
    if "time." in code and "import time" not in code:
        needs.append("import time")
    if "shutil." in code and "import shutil" not in code:
        needs.append("import shutil")

    if needs:
        code = "\n".join(needs) + "\n\n" + code
    return code


_RUNTIME = """
import sys
import builtins

_apl_orig_print = builtins.print

def _apl_has_arabic(v):
    return any('\\u0600' <= c <= '\\u06FF' or '\\u0750' <= c <= '\\u07FF' or '\\u08A0' <= c <= '\\u08FF' or '\\uFB50' <= c <= '\\uFDFF' for c in str(v))

def _apl_print(*args, **kwargs):
    if any(_apl_has_arabic(a) for a in args):
        _apl_orig_print('\\u202B', *args, '\\u202C', **kwargs)
    else:
        _apl_orig_print(*args, **kwargs)

builtins.print = _apl_print

_ERROR_AR = {
    "SyntaxError": "خطأ في الصياغة",
    "NameError": "خطأ: متغير غير معروف",
    "TypeError": "خطأ في نوع البيانات",
    "ValueError": "خطأ في القيمة",
    "IndexError": "خطأ: الفهرس خارج النطاق",
    "KeyError": "خطأ: المفتاح غير موجود",
    "ZeroDivisionError": "خطأ: القسمة على صفر",
    "FileNotFoundError": "خطأ: الملف غير موجود",
    "ImportError": "خطأ: استيراد فاشل",
    "AttributeError": "خطأ: الخاصية غير موجودة",
    "EOFError": "خطأ: لا توجد بيانات إدخال",
    "IndentationError": "خطأ: مشكلة في المسافات",
    "StopIteration": "تم التوقف",
    "RuntimeError": "خطأ في التشغيل",
    "PermissionError": "خطأ: صلاحية مرفوضة",
    "TimeoutError": "خطأ: انتهاء الوقت",
    "ConnectionError": "خطأ: فشل الاتصال",
    "OSError": "خطأ: نظام التشغيل",
    "OverflowError": "خطأ: تجاوز السعة",
    "RecursionError": "خطأ: استدعاء متكرر عميق",
    "ModuleNotFoundError": "خطأ: الوحدة غير موجودة",
    "AssertionError": "خطأ: التأكيد فشل",
    "KeyboardInterrupt": "توقف بواسطة المستخدم",
}

_old_excepthook = sys.excepthook
def _apl_excepthook(typ, val, tb):
    name = _ERROR_AR.get(typ.__name__, typ.__name__)
    import traceback
    traceback.print_exception(typ, val, tb)
    sys.stderr.write(f"\\u202B{name}: {val}\\u202C\\n")
sys.excepthook = _apl_excepthook

def _apl_read(f):
    return f.read()

def _apl_write(f, s):
    return f.write(s)

def _apl_close(f):
    f.close()

def _apl_fetch(url):
    return urllib.request.urlopen(url).read().decode("utf-8")
"""


def run_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
    python_code = _RUNTIME + "\n" + transpile(source)
    try:
        exec(python_code, {})
    except Exception as e:
        msg = _get_error_ar(e)
        print(f"\u202B{msg}\u202C", file=sys.stderr)


def _get_error_ar(e: Exception) -> str:
    name = type(e).__name__
    ar_name = {
        "SyntaxError": "خطأ في الصياغة",
        "NameError": "خطأ: متغير غير معروف",
        "TypeError": "خطأ في نوع البيانات",
        "ValueError": "خطأ في القيمة",
        "IndexError": "خطأ: الفهرس خارج النطاق",
        "KeyError": "خطأ: المفتاح غير موجود",
        "ZeroDivisionError": "خطأ: القسمة على صفر",
        "FileNotFoundError": "خطأ: الملف غير موجود",
        "ImportError": "خطأ: استيراد فاشل",
        "AttributeError": "خطأ: الخاصية غير موجودة",
        "EOFError": "خطأ: لا توجد بيانات إدخال",
        "IndentationError": "خطأ: مشكلة في المسافات",
        "RuntimeError": "خطأ في التشغيل",
        "PermissionError": "خطأ: صلاحية مرفوضة",
        "OSError": "خطأ: نظام التشغيل",
        "ConnectionError": "خطأ: فشل الاتصال",
        "ModuleNotFoundError": "خطأ: الوحدة غير موجودة",
        "OverflowError": "خطأ: تجاوز السعة",
    }.get(name, name)
    return f"{ar_name}: {e}"


def transpile_to_code(source: str) -> str:
    return transpile(source)


def print_help():
    """Print help information"""
    print("APL - Ammar Programming Language")
    print()
    print("Usage:")
    print("  python apl.py <file.apl>    Run an APL file")
    print("  python apl.py -c '<code>'   Execute code directly")
    print("  python apl.py help          Show this help")
    print("  python apl.py repl          Start interactive REPL")
    print("  python apl.py               Show help")
    print()
    print("Language keywords:")
    lang_cmds = [
        "المتغير x = y       - متغير",
        "اطبع / اطبع_بدون     - طباعة",
        "ادخل(...)            - إدخال",
        "لو / الا لو / الا    - شرط",
        "سإذا شرط والا ص     - شرط ثلاثي",
        "طالما شرط:           - while",
        "لكل x في y:          - for",
        "دالة / ارجع          - function / return",
        "سهم x, y: expr       - lambda",
        "مولد / توقف / اكمل   - yield / break / continue",
        "حاول / إمسك          - try / except",
        "تأكد(شرط)            - assert",
        "خاصية / محدد / محدد_حذف - property/setter/deleter",
        "صنف/قاعدة / تمرير    - class / pass",
        "خاص / عام            - private / public",
        "حالة / قيمة / افتراضي - match / case",
        "مع .. مثل            - with .. as",
        "حذف / أبدا           - del / while True",
        "اخرج(0)              - exit",
        "نسخ ملف / نقل ملف    - shutil.copy/move",
        "حجم ملف / قائمة ملفات - os.path.getsize/listdir",
        "احذف ملف / انشئ مجلد - os.remove/mkdir",
        "استورد / من..استورد   - import",
        "فتح / اقرأ / اكتب / اغلق - ملفات",
        "طلب(url)             - HTTP",
        "جسون / جسون_تحويل    - JSON",
        "كل / أي / خريطة / فلترة / تجميع - all/any/map/filter/zip",
        "انتظر(ثوان) / وقت()  - time.sleep/time.time",
        "تمثيل / ثنائي / سداسي / ترتيب / رمز - repr/bin/hex/ord/chr",
        "من(س, نوع)           - isinstance",
        "صحيح/نص/عشري/منطق   - int/str/float/bool",
        "قائمة/مجموعة/مصفوفة/قاموس - list/tuple/set/dict",
        "نطاق/طول            - range/len",
        "نوع/عدد              - type/enumerate",
        "مطلق/قوة/جذر        - abs/pow/sqrt",
        "أكبر/أصغر/مقرب      - max/min/round",
        "مجموع/مفرز          - sum/sorted",
        "ط/ه/تاو/لانهائي_موجب - pi/e/tau/inf",
        ".تقسيم/.أضف/.ضم     - .split/.append/.join",
        ".علوي/.سفلي/.تقليم  - .upper/.lower/.strip",
        ".استبدال/.بداية/.نهاية - .replace/.startswith/.endswith",
        ".اتحاد/.تقاطع/.فرق   - .union/.intersection/.difference",
        "و / أو / ليس / مثل / في - and/or/not/as/in",
        "صواب / خطأ / لا_شيء  - True / False / None",
    ]
    for cmd in lang_cmds:
        print(f"  {cmd}")
    
    print()
    print("Libraries:")
    print("  # math library (50+ functions)")
    for line in math_funcs.MATH_HELP:
        print(f"    {line}")
    print()
    print("  # random library (20+ functions)")
    for line in random_funcs.RANDOM_HELP:
        print(f"    {line}")
    print()
    print("  # time/datetime library (20+ functions)")
    for line in time_funcs.TIME_HELP:
        print(f"    {line}")
    print()
    print("  # statistics library (15+ functions)")
    for line in statistics_funcs.STATISTICS_HELP:
        print(f"    {line}")
    print()
    print("  # os/path library (30+ functions)")
    for line in os_funcs.OS_HELP:
        print(f"    {line}")
    print()
    print("  # re library (10+ functions)")
    for line in re_funcs.RE_HELP:
        print(f"    {line}")
    print()
    print("  # collections library (10+ functions)")
    for line in collections_funcs.COLLECTIONS_HELP:
        print(f"    {line}")
    print()
    print("  # itertools library (20+ functions)")
    for line in itertools_funcs.ITERTOOLS_HELP:
        print(f"    {line}")
    print()
    print("  # json library (4+ functions)")
    for line in json_funcs.JSON_HELP:
        print(f"    {line}")
    print()
    print("  # hashlib library (5+ functions)")
    for line in hashlib_funcs.HASHLIB_HELP:
        print(f"    {line}")
    print()
    print("  # flask library (50+ functions)")
    for line in flask_funcs.FLASK_HELP:
        print(f"    {line}")
    print()
    print("  # fastapi library (100+ functions)")
    for line in fastapi_funcs.FASTAPI_HELP:
        print(f"    {line}")
    print()
    print("  # requests library (150+ functions)")
    for line in requests_funcs.REQUESTS_HELP:
        print(f"    {line}")
    print()
    print("  # sqlite3 library (20+ functions)")
    for line in sqlite3_funcs.SQLITE3_HELP:
        print(f"    {line}")
    print()
    print("  # asyncio library (50+ functions)")
    for line in asyncio_funcs.ASYNCIO_HELP:
        print(f"    {line}")
    print()
    print("  # threading library (20+ functions)")
    for line in threading_funcs.THREADING_HELP:
        print(f"    {line}")
    print()
    print("  # unittest library (40+ functions)")
    for line in unittest_funcs.UNITTEST_HELP:
        print(f"    {line}")
    print()
    print("  # csv library (10+ functions)")
    for line in csv_funcs.CSV_HELP:
        print(f"    {line}")
    print()
    print("  # logging library (30+ functions)")
    for line in logging_funcs.LOGGING_HELP:
        print(f"    {line}")
    print()
    print("  # argparse library (30+ functions)")
    for line in argparse_funcs.ARGPARSE_HELP:
        print(f"    {line}")
    print()
    print("  # subprocess library (20+ functions)")
    for line in subprocess_funcs.SUBPROCESS_HELP:
        print(f"    {line}")
    print()
    print("  # configparser library (20+ functions)")
    for line in configparser_funcs.CONFIGPARSER_HELP:
        print(f"    {line}")
    print()
    print("  # dataclasses library (30+ functions)")
    for line in dataclasses_funcs.DATACLASSES_HELP:
        print(f"    {line}")
    print()
    print("  # advanced library (100+ functions)")
    for line in advanced_funcs.ADVANCED_HELP:
        print(f"    {line}")
    print()
    print("Examples:")
    print("  python apl.py calculator.apl")
    print("  python apl.py help")
    print("  python apl.py repl")


def run_repl():
    """Run interactive REPL"""
    print("APL - Ammar Programming Language")
    print("Interactive REPL (type 'exit' or Ctrl+C to quit)")
    print()
    
    while True:
        try:
            line = input(">>> ")
            if line.strip().lower() in ('exit', 'اخرج', 'quit'):
                print("Goodbye! 👋")
                break
            if not line.strip():
                continue
            
            # Transpile and execute single line
            python_code = _RUNTIME + "\n" + transpile(line)
            exec(python_code, {})
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except Exception as e:
            msg = _get_error_ar(e)
            print(f"\u202B{msg}\u202C", file=sys.stderr)


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()
    
    if command in ('help', '--help', '-h', '-?'):
        print_help()
        return
    
    if command in ('repl', 'interactive', 'shell'):
        run_repl()
        return

    # Execute code directly: python apl.py -c "اطبع 'مرحباً'"
    if command in ('-c', '--code'):
        if len(sys.argv) < 3:
            print("Usage: python apl.py -c '<code>'")
            sys.exit(1)
        code = sys.argv[2]
        # Split by newlines and semicolons for multi-statement support
        lines = code.replace(';', '\n').split('\n')
        python_code = _RUNTIME + "\n"
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:
                python_code += transpile_line(stripped_line) + "\n"
        try:
            exec(python_code, {})
        except Exception as e:
            msg = _get_error_ar(e)
            print(f"\u202B{msg}\u202C", file=sys.stderr)
        return

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Error: file '{filepath}' not found")
        sys.exit(1)

    run_file(filepath)


if __name__ == "__main__":
    main()

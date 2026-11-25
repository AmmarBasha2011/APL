#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_library_behavior.py — هل المفتاح العربي يرجّع نفس نتيجة دالة Python الأصلية؟

check_libraries.py بيتأكد إن المفتاح بيتحوّل ويُحلّ. هنا بنشغّل الدالة فعلاً:
لكل مفتاح عربي هدفه دالة نقيّة في وحدة آمنة (math / statistics / json /
base64 / hashlib / textwrap ...) نجرّب مجموعة مدخلات ثابتة. لو دالة Python
الأصلية نجحت على مدخل، لازم مفتاح APL (بعد التحويل والتنفيذ) يرجّع نفس
النتيجة بالظبط (repr متطابق). أي اختلاف يفشل الفحص.

الأخطاء القديمة مسجّلة في scripts/baselines/behavior_issues.txt (يفشل على
الجديد فقط).

الاستخدام:
    python scripts/check_library_behavior.py
    python scripts/check_library_behavior.py --update-baseline
    python scripts/check_library_behavior.py --quiet
"""

import argparse
import importlib
import math
import os
import signal
import sys
import warnings

warnings.filterwarnings("ignore")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from core.libraries import LIBRARIES                  # noqa: E402
from core.apl_runner.main import transpile            # noqa: E402

BASELINE = os.path.join(ROOT, "scripts", "baselines", "behavior_issues.txt")

# وحدات نقيّة وحتمية فقط (بلا ملفات ولا شبكة ولا وقت ولا عشوائية)
SAFE_MODULES = {
    "math", "cmath", "statistics", "string", "json", "base64", "binascii",
    "hashlib", "textwrap", "fractions", "decimal", "operator", "bisect",
    "heapq", "unicodedata", "html", "urllib.parse", "zlib", "struct",
    "difflib", "shlex", "colorsys", "fnmatch", "calendar", "itertools",
    "functools", "copy", "keyword", "ipaddress", "re",
}
SKIP_TARGETS = {"itertools.count", "itertools.cycle", "itertools.repeat",
                "calendar.prcal", "calendar.prmonth", "calendar.pryear",
                "calendar.setfirstweekday", "calendar.main", "re.purge",
                "heapq.merge"}

PROBES = [
    (), (0,), (1,), (4,), (7,), (10,), (-3,), (2.5,), (-1.5,), (0.5,),
    (2, 3), (10, 4), (7, 2), (12, 18), (5, 0),
    ("abc",), ("Hello World",), ("  x y  ",), ("12",), ("",),
    ("a", "b"), ("abc", "b"), ("a,b,c", ","),
    ([3, 1, 2],), ([1, 2, 3, 4],), ([2.5, 3.5, 9.0],), ([],),
    ([1, 2, 3], 2), ([1, 3, 5], 4), ([1, 2, 3], [4, 5, 6]),
    ({"a": 1, "b": [1, 2]},), ('{"a": 1, "b": [1, 2]}',),
    (b"hello",), (b"aGVsbG8=",), ("hello",),
]


def resolve(path):
    parts = path.split(".")
    for cut in range(len(parts), 0, -1):
        mod = ".".join(parts[:cut])
        if mod not in SAFE_MODULES:
            continue
        try:
            obj = importlib.import_module(mod)
        except Exception:
            continue
        try:
            for p in parts[cut:]:
                obj = getattr(obj, p)
        except Exception:
            return None
        return obj
    return None


class Timeout(Exception):
    pass


def _alarm(*_):
    raise Timeout()


def run_python(fn, args):
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(2)
    try:
        return "ok", repr(fn(*args))
    except Timeout:
        return "timeout", None
    except BaseException as e:   # noqa: BLE001
        return "err", type(e).__name__
    finally:
        signal.alarm(0)


def run_apl(key, args):
    src = "نتيجة_فحص = " + key + "(" + ", ".join(repr(a) for a in args) + ")"
    try:
        code = transpile(src)
    except BaseException as e:   # noqa: BLE001
        return "err", "transpile:" + type(e).__name__
    env = {"__name__": "__apl_check__"}
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(3)
    try:
        exec(compile(code, "<apl>", "exec"), env)
        return "ok", repr(env["نتيجة_فحص"])
    except Timeout:
        return "timeout", None
    except BaseException as e:   # noqa: BLE001
        return "err", type(e).__name__
    finally:
        signal.alarm(0)


RECEIVERS = [
    ("نص", "Hello, World 123"), ("نص", "  a b  c "), ("نص", "abc,def"),
    ("قائمة", [3, 1, 2]), ("قائمة", [1, 2, 2, 3]), ("قاموس", {"a": 1, "b": 2}),
    ("مجموعة", {1, 2, 3}), ("صحيح", 255), ("عشري", 2.75), ("بايت", b"hello"),
]
METHOD_ARGS = [(), ("l",), (",",), ("a", "b"), (1,), (2,), (0,), (1, 2),
               ("a",), ("a", 1), ({4, 5},), ([4, 5],)]


def _stable(v):
    r = repr(v)
    return r if " at 0x" not in r and "<" not in r else None


def collect_methods(checked_keys, issues):
    calls = 0
    for lib, mod in LIBRARIES.items():
        d = getattr(mod, lib.upper() + "_METHODS", {})
        for ar, val in d.items():
            if not isinstance(val, str) or not ar.isidentifier() \
                    or not val.isidentifier():
                continue
            for _, recv in RECEIVERS:
                if not hasattr(recv, val) or not callable(getattr(recv, val)):
                    continue
                if val in ("clear", "pop", "popitem", "remove", "discard"):
                    continue
                for args in METHOD_ARGS:
                    import copy
                    try:
                        want = _stable(getattr(copy.deepcopy(recv), val)(*args))
                    except BaseException:   # noqa: BLE001
                        continue
                    if want is None:
                        continue
                    calls += 1
                    checked_keys.add((lib, "." + ar))
                    src = "نتيجة_فحص = س." + ar + "(" + ", ".join(repr(a) for a in args) + ")"
                    try:
                        code = transpile(src)
                        env = {"س": copy.deepcopy(recv)}
                        exec(compile(code, "<apl>", "exec"), env)
                        got = _stable(env["نتيجة_فحص"])
                    except BaseException as e:   # noqa: BLE001
                        got = "ERR:" + type(e).__name__
                    if got != want:
                        issues.append(f"{lib}\t.{ar}\t{val}\t{recv!r}{args!r}")
                    break
    return calls


def collect_consts(checked_keys, issues):
    calls = 0
    for lib, mod in LIBRARIES.items():
        for kind in ("CONSTS", "CONSTANTS"):
            d = getattr(mod, lib.upper() + "_" + kind, {})
            for ar, target in d.items():
                if not isinstance(target, str) or not ar.isidentifier():
                    continue
                obj = resolve(target)
                if obj is None or callable(obj):
                    continue
                want = _stable(obj)
                if want is None:
                    continue
                calls += 1
                checked_keys.add((lib, ar))
                st, got = run_apl_expr(ar)
                if (st, got) != ("ok", want):
                    issues.append(f"{lib}\t{ar}\t{target}\t-")
    return calls


def run_apl_expr(src_expr):
    try:
        code = transpile("نتيجة_فحص = " + src_expr)
        env = {"__name__": "__apl_check__"}
        exec(compile(code, "<apl>", "exec"), env)
        return "ok", _stable(env["نتيجة_فحص"])
    except BaseException as e:   # noqa: BLE001
        return "err", type(e).__name__


def collect():
    issues, checked_keys, calls = [], set(), 0
    calls += collect_methods(checked_keys, issues)
    calls += collect_consts(checked_keys, issues)
    for lib, mod in LIBRARIES.items():
        d = getattr(mod, lib.upper() + "_FUNCS", {})
        for ar, target in d.items():
            if not isinstance(target, str) or target.startswith("@") \
                    or target in SKIP_TARGETS or not ar.isidentifier():
                continue
            fn = resolve(target)
            if fn is None or not callable(fn) or isinstance(fn, type):
                continue
            for args in PROBES:
                st, want = run_python(fn, args)
                if st != "ok":
                    continue
                st2, want2 = run_python(fn, args)
                if (st2, want2) != (st, want):
                    continue          # غير حتمية: نتجاهلها
                if "0x" in want or " at 0x" in want:
                    continue
                calls += 1
                checked_keys.add((lib, ar))
                got_st, got = run_apl(ar, args)
                if (got_st, got) != ("ok", want):
                    issues.append(f"{lib}\t{ar}\t{target}\t{args!r}")
                    break
    from scripts.library_golden import GOLDEN
    for expr, want in GOLDEN:
        calls += 1
        st, got = run_apl_expr(expr)
        if got != want:
            issues.append(f"golden\t{expr}\t{want}\t-")
    return issues, len(checked_keys), calls


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--update-baseline", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    issues, keys, calls = collect()
    if a.update_baseline:
        os.makedirs(os.path.dirname(BASELINE), exist_ok=True)
        with open(BASELINE, "w", encoding="utf-8") as f:
            f.write("".join(i.rsplit("\t", 1)[0] + "\n" for i in sorted(issues)))
        print(f"baseline: {len(issues)} مشكلة")
        return 0
    known = set()
    if os.path.exists(BASELINE):
        known = {l.rstrip("\n") for l in open(BASELINE, encoding="utf-8") if l.strip()}
    new = [i for i in issues if i.rsplit("\t", 1)[0] not in known]
    print(f"سلوك المكتبات: {keys} مفتاحاً، {calls} استدعاء، "
          f"{len(issues)} اختلاف ({len(issues) - len(new)} قديم مسجّل)")
    if keys < 300:
        print(f"✗ عدد المفاتيح المفحوصة قليل جداً ({keys} < 300)")
        return 1
    for i in new:
        print("✗ جديد:", i)
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())

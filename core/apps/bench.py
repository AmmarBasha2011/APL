"""APL Benchmark: how fast APL runs compared with the same program in Python.

Each test is one APL program and the Python program that does the same work.
Every program runs a few times and the best time counts. The APL time includes
translating the program to Python (the cache is off), which is what a first
run costs. Numbers depend on the machine; they are for comparing, not a
standard.
"""
import os
import tempfile
import time
from pathlib import Path

from core.apps import common

TESTS = [
    ("حلقة جمع (3 مليون مرة)",
     "المتغير مجموع = 0\nالمتغير ن = 0\nطالما ن < 3000000:\n    مجموع += ن\n    ن += 1\nاطبع مجموع\n",
     "s = 0\nn = 0\nwhile n < 3000000:\n    s += n\n    n += 1\nprint(s)\n"),
    ("فيبوناتشي بالتكرار الذاتي (ن=27)",
     "دالة فيب(ن):\n    لو ن < 2:\n        ارجع ن\n    ارجع فيب(ن - 1) + فيب(ن - 2)\nاطبع فيب(27)\n",
     "def fib(n):\n    if n < 2:\n        return n\n    return fib(n - 1) + fib(n - 2)\nprint(fib(27))\n"),
    ("بناء قائمة وفرزها (200 ألف)",
     "المتغير ق = []\nالمتغير ن = 0\nطالما ن < 200000:\n    ق.أضف((ن * 7919) % 100003)\n    ن += 1\nق.فرز()\nاطبع ق[0], ق[-1]\n",
     "l = []\nn = 0\nwhile n < 200000:\n    l.append((n * 7919) % 100003)\n    n += 1\nl.sort()\nprint(l[0], l[-1])\n"),
    ("نصوص: ضم وتقسيم (100 ألف)",
     "المتغير أجزاء = []\nالمتغير ن = 0\nطالما ن < 100000:\n    أجزاء.أضف(\"ع\" + نص(ن))\n    ن += 1\nالمتغير كبير = \",\".ضم(أجزاء)\nاطبع طول(كبير.تقسيم(\",\"))\n",
     "p = []\nn = 0\nwhile n < 100000:\n    p.append('ع' + str(n))\n    n += 1\nbig = ','.join(p)\nprint(len(big.split(',')))\n"),
    ("قاموس: إدخال وبحث (100 ألف)",
     "المتغير د = {}\nالمتغير ن = 0\nطالما ن < 100000:\n    د[ن] = ن * 2\n    ن += 1\nالمتغير ع = 0\nن = 0\nطالما ن < 100000:\n    ع += د[ن]\n    ن += 1\nاطبع ع\n",
     "d = {}\nn = 0\nwhile n < 100000:\n    d[n] = n * 2\n    n += 1\nt = 0\nn = 0\nwhile n < 100000:\n    t += d[n]\n    n += 1\nprint(t)\n"),
]


def best_of(fn, runs):
    best = None
    for _ in range(runs):
        start = time.perf_counter()
        fn()
        took = time.perf_counter() - start
        best = took if best is None or took < best else best
    return best


def python_time(source, runs):
    import contextlib
    import io

    def go():
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(source, "<py>", "exec"), {"__name__": "__bench__"})
    return best_of(go, runs)


def apl_time(source, runs, folder):
    path = Path(folder) / "bench.apl"
    path.write_text(source, encoding="utf-8")
    result = {}

    def go():
        code, output = common.run_apl(["شغل", str(path)], timeout=120, cwd=folder)
        result["code"], result["out"] = code, output
    best = best_of(go, runs)
    return best, result.get("code"), result.get("out", "")


def run(argv):
    runs = 3
    for item in argv:
        if item.isdigit():
            runs = max(1, min(int(item), 10))
    os.environ["APL_NO_CACHE"] = "1"
    print("APL Benchmark: أحسن وقت من %d محاولات لكل اختبار\n" % runs)
    print("%-38s %10s %10s %8s" % ("الاختبار", "APL (ث)", "Python (ث)", "النسبة"))
    failed = 0
    with tempfile.TemporaryDirectory() as folder:
        for name, apl_source, py_source in TESTS:
            py = python_time(py_source, runs)
            apl, code, output = apl_time(apl_source, runs, folder)
            if code != 0:
                failed += 1
                print("%-38s فشل: %s" % (name, output.strip().splitlines()[-1:] or code))
                continue
            print("%-38s %10.3f %10.3f %7.1fx" % (name, apl, py, apl / py if py else 0))
    print("\nالنسبة = وقت APL ÷ وقت Python. وقت APL فيه بدء البرنامج وترجمته.")
    return 1 if failed else 0

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_examples.py — يشغّل كل أمثلة APL ويتأكد أنها تعمل بلا أخطاء.

الاستخدام:
    python test_examples.py             # كل الأمثلة
    python test_examples.py 61 62       # أرقام محددة
    python test_examples.py --verbose   # إظهار مخرجات كل مثال

المعيار: خروج بحالة 0 وبدون رسالة خطأ عربية (‫...‬) على stderr.
بعض الأمثلة تحتاج إدخالاً من لوحة المفاتيح، فتُغذّى بمدخل ثابت.
"""

import glob
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
EXAMPLES = os.path.join(ROOT, "examples")

# أمثلة تقرأ من لوحة المفاتيح: الملف -> المدخل الثابت
STDIN = {
    "01-calculator.apl": "1\n5\n3\n",
}

# مهلة كل مثال بالثواني
TIMEOUT = 180


def run_one(path, verbose=False):
    name = os.path.basename(path)
    stdin = STDIN.get(name, "")
    try:
        proc = subprocess.run(
            [sys.executable, os.path.join(ROOT, "apl.py"), path],
            input=stdin,
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            cwd=ROOT,
        )
    except subprocess.TimeoutExpired:
        return False, "انتهت المهلة", ""

    err = proc.stderr or ""
    # علامة الخطأ العربي ‫ تظهر فقط عند حقيقي؛ بعض الأمثلة تطبع كلمة «خطأ»
    # في مخرجاتها (مثل مثال التسجيل) فليست دليلاً على فشل.
    failed = proc.returncode != 0 or "‫" in err
    return (not failed), err, proc.stdout


def main():
    argv = [a for a in sys.argv[1:]]
    verbose = "--verbose" in argv or "-v" in argv
    argv = [a for a in argv if not a.startswith("-")]

    files = sorted(glob.glob(os.path.join(EXAMPLES, "*.apl")))
    if argv:
        files = [f for f in files
                 if any(os.path.basename(f).startswith(a) for a in argv)]

    if not files:
        print("لا توجد أمثلة مطابقة")
        return 1

    print(f"اختبار {len(files)} مثالاً من {EXAMPLES}\n")
    results = []
    t0 = time.time()
    for path in files:
        name = os.path.basename(path)
        ok, err, out = run_one(path, verbose)
        results.append((name, ok, err))
        print(f"  {'✓' if ok else '✗'} {name}")
        if not ok:
            first = next((ln for ln in err.splitlines() if ln.strip()), "")
            print(f"      {first}")

    ok_n = sum(1 for _, ok, _ in results if ok)
    dt = time.time() - t0
    print(f"\nالنتيجة: {ok_n}/{len(results)} مثالاً ناجحاً في {dt:.1f} ثانية")

    if ok_n != len(results):
        print("\nالأمثلة الفاشلة:")
        for name, ok, err in results:
            if not ok:
                print(f"  - {name}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_examples.py — يشغّل كل أمثلة APL ويتأكد أنها تعمل وبأنها تُنتج المخرجات الصح.

الاستخدام:
    python test_examples.py             # كل الأمثلة
    python test_examples.py 61 62       # أرقام محددة
    python test_examples.py --verbose   # إظهار مخرجات كل مثال

معيار النجاح:
  1. خروج بحالة 0 (apl.py يخرج 1 عند أي خطأ تشغيل).
  2. مفيش رسالة خطأ عربية (‫...‬) على stderr.
  3. بالنسبة للأمثلة في EXPECTED: كل النصوص المتوقعة موجودة في stdout.

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

TIMEOUT = 180

# نصوص لازم تظهر في stdout — حماية من «المثال شغال لكنه بيطلع حاجة غلط»
EXPECTED = {
    "01-calculator.apl": ["النتيجة (جمع): 80"],
    "02-sales-report.apl": ["الإجمالي بعد خصم 19%: 797.85", "متوسط الفاتورة: 159.57"],
    "06-search-sort.apl": ["بحث عن 22: الفهرس 3", "أكبر عنصر: 90"],
    "11-fibonacci.apl": ["فيب(10) تكراري: 55", "فيب(50) تكراري: 12586269025"],
    "12-prime-check.apl": ["عددها: 15", "97 أولي؟ True"],
    "22-temperature-converter.apl": ["98.6", "310.1"],
    "23-palindrome-check.apl": ["racecar: متناظرة", "hello: ليست متناظرة"],
    "24-roman-numerals.apl": ["1990 = MCMXC", "2024 = MMXXIV"],
    "28-binary-search.apl": ["13: الفهرس 6", "99: غير موجود"],
    "61-devtools-inspect.apl": ["توقيع_الدالة(ضرب): (س, ص)", "هو_دالة(ضرب): True"],
    "62-devtools-ast.apl": ["نوع الشجرة: <class 'ast.Module'>", "عدد العقد: 12"],
    "63-devtools-dis.apl": ["عدد التعليمات: 4", "اسم الجدول: top"],
    "64-devtools-traceback.apl": ["ZeroDivisionError: division by zero",
                                 "نتيجة_اختبار صفرية: TestResults(failed=0, attempted=0)"],
    "65-devtools-profile.apl": ["هو_مفعّل: True", "عدد_الأجيال: 3"],
    "66-devtools-import.apl": ["ترجم_أمراً('1 + 2'): <class 'code'>",
                               "هو_وحدة(رياضيات): True"],
    "67-web-http-status.apl": ["ناجح: 200", "غير موجود: 404",
                               "404 -> غير موجود"],
    "68-web-url-parse.apl": ["اسم_المضيف: example.com", "المنفذ: 8080",
                             "https://example.com/a/c/d"],
    "69-web-email-build.apl": ["النوع: text/utf-8",
                               "المحتوى: مرحباً من مكتبة الويب",
                               "عدد عناصر الترويسة: 3"],
    "70-web-mailbox-mime.apl": ["صورة.png -> image/png",
                                "application/pdf -> .pdf"],
    "71-web-html-cookies.apl": ["&lt;b&gt;مرحباً&lt;/b&gt;", "الاسم: ahmed"],
    "72-web-xmlrpc-wsgi.apl": ["القاموس: {'مفتاح': True}",
                               "Content-Type: text/plain; charset=utf-8"],
    "73-web-robots-maildir.apl": ["يستطيع الزحف /public: True",
                                  "يستطيع الزحف /private: False"],
    "74-df-paths.apl": ["المسار: /tmp/apl-df-dir", "الامتداد: ('تقرير', '.pdf')"],
    "75-df-archive.apl": ["الأعضاء: ['echo.txt']", "مقروء: نص مضغوط بالعربية"],
    "76-df-serialize.apl": ["مفكوك: {'الاسم': 'أحمد', 'الأعمار': [3, 7, 11]}",
                            "marshal: [1, 'نص', {'م': True}]"],
    "77-df-structures.apl": ["العناصر: [1, 2, 3]", "مفكوك: (7,)",
                             "موضع 6: 4"],
    "78-df-xml.apl": ["الوسم: كتاب", "اسم العقدة: #document"],
    "79-df-text.apl": ["اسم المحرف A: LATIN CAPITAL LETTER A",
                       "فئة المحرف ع: Lo"],
    "80-df-refs.apl": ["القيمة: أول", "عدد العناصر: 1"],
}


def run_one(path, verbose=False):
    """يرجع (ok, problems, stdout)."""
    name = os.path.basename(path)
    problems = []
    # APL_NO_CACHE=1: الاختبارات لازم تترجم من أول وجديد. الكاش مظلوم في
    # الاستخدام العادي، لكن هنا ترجمة قديمة ممكن تخفي اسم اتشال من مكتبة.
    env = dict(os.environ, APL_NO_CACHE="1")
    try:
        proc = subprocess.run(
            [sys.executable, os.path.join(ROOT, "apl.py"), path],
            input=STDIN.get(name, ""),
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            cwd=ROOT,
            env=env,
        )
    except subprocess.TimeoutExpired:
        return False, ["انتهت المهلة"], ""

    err = proc.stderr or ""
    out = proc.stdout or ""
    if proc.returncode != 0:
        problems.append(f"rc={proc.returncode}")
    if "\u202b" in err:            # علامة الخطأ العربي
        problems.append(next((ln for ln in err.splitlines() if ln.strip()), ""))
    for want in EXPECTED.get(name, []):
        if want not in out:
            problems.append(f"مخرجات ناقصة: «{want}»")
    if verbose:
        print(out)
    return (not problems), problems, out


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
        ok, problems, out = run_one(path, verbose)
        results.append((name, ok, problems))
        print(f"  {'✓' if ok else '✗'} {name}")
        for p in problems:
            print(f"      {p}")

    ok_n = sum(1 for _, ok, _ in results if ok)
    dt = time.time() - t0
    print(f"\nالنتيجة: {ok_n}/{len(results)} مثالاً ناجحاً في {dt:.1f} ثانية")

    if ok_n != len(results):
        print("\nالأمثلة الفاشلة:")
        for name, ok, problems in results:
            if not ok:
                print(f"  - {name}: {problems}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_example_perf.py — حارس أداء الأمثلة.

يشغّل كل مثال مع قياس الوقت، ويفشل (exit 1) لو:
  - أي مثال استغرق أكثر من 30 ثانية (أو فشل تشغيله).
  - الزمن الكلي تجاوز 30 دقيقة.

يعرض أبطأ 10 أمثلة في النهاية.

الوضع التزايدي: مع --base REF (يُستعمل في الـ pull request) يشغّل فقط الأمثلة
الجديدة أو المعدّلة. ولو تغيّر أي ملف خارج examples/ و README.md و docs/ و website/
(كود أو مكتبات أو متطلبات أو سكربتات) أو فشل حساب الفرق يشغّل كل الأمثلة.
على push إلى main وفي الجدولة الليلية يُشغَّل كل شيء (بدون --base).
"""

import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from test_examples import STDIN  # مدخلات الأمثلة التفاعلية
EXAMPLES = os.path.join(ROOT, "examples")
MAX_ONE = 30.0        # ثانية لكل مثال
MAX_TOTAL = 30 * 60   # 30 دقيقة للكل


SAFE_PREFIXES = ("examples/", "docs/", "website/")
SAFE_FILES = ("README.md",)


def select_files(base):
    """أسماء الأمثلة المطلوب فحصها، أو None لو لازم الفحص الكامل."""
    r = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=d", base, "HEAD"],
        capture_output=True, text=True, cwd=ROOT,
    )
    if r.returncode != 0:
        print("تعذّر حساب الفرق، فحص كامل.")
        return None
    changed = [c for c in r.stdout.split("\n") if c.strip()]
    for c in changed:
        if not (c.startswith(SAFE_PREFIXES) or c in SAFE_FILES):
            print(f"تغيّر ملف غير مثال ({c})، فحص كامل.")
            return None
    return sorted(
        os.path.basename(c) for c in changed
        if c.startswith("examples/") and c.endswith(".apl")
    )


def main():
    files = sorted(f for f in os.listdir(EXAMPLES) if f.endswith(".apl"))
    if "--base" in sys.argv:
        picked = select_files(sys.argv[sys.argv.index("--base") + 1])
        if picked is not None:
            files = [f for f in picked if os.path.exists(os.path.join(EXAMPLES, f))]
            print(f"فحص تزايدي: {len(files)} مثال جديد أو معدّل.")
    start = time.monotonic()
    timings = []
    failures = 0
    for fn in files:
        t0 = time.monotonic()
        rc = subprocess.run(
            [sys.executable, os.path.join(ROOT, "apl.py"), os.path.join(EXAMPLES, fn)],
            input=STDIN.get(fn, ""), capture_output=True, text=True,
            timeout=MAX_ONE + 30, cwd=ROOT,
            env=dict(os.environ, APL_NO_CACHE="1"),
        ).returncode
        dt = time.monotonic() - t0
        timings.append((dt, fn))
        if rc != 0:
            print(f"✗ فشل تشغيل: {fn}")
            failures += 1
        elif dt > MAX_ONE:
            print(f"✗ بطيء: {fn} ({dt:.1f}s > {MAX_ONE:.0f}s)")
            failures += 1
    total = time.monotonic() - start
    timings.sort(reverse=True)
    print("\nأبطأ 10 أمثلة:")
    for dt, fn in timings[:10]:
        print(f"  {dt:6.2f}s  {fn}")
    print(f"\nالزمن الكلي: {total:.0f}s لـ {len(files)} مثال")
    if total > MAX_TOTAL:
        print(f"✗ الزمن الكلي تجاوز {MAX_TOTAL / 60:.0f} دقيقة")
        failures += 1
    if failures:
        return 1
    print("✓ أداء الأمثلة ضمن الحدود")
    return 0


if __name__ == "__main__":
    sys.exit(main())

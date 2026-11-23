#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_example_perf.py — حارس أداء الأمثلة.

يشغّل كل مثال مع قياس الوقت، ويفشل (exit 1) لو:
  - أي مثال استغرق أكثر من 30 ثانية (أو فشل تشغيله).
  - الزمن الكلي تجاوز 15 دقيقة.

يعرض أبطأ 10 أمثلة في النهاية.
"""

import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMPLES = os.path.join(ROOT, "examples")
MAX_ONE = 30.0        # ثانية لكل مثال
MAX_TOTAL = 15 * 60   # 15 دقيقة للكل


def main():
    files = sorted(f for f in os.listdir(EXAMPLES) if f.endswith(".apl"))
    start = time.monotonic()
    timings = []
    failures = 0
    for fn in files:
        t0 = time.monotonic()
        rc = subprocess.run(
            [sys.executable, os.path.join(ROOT, "apl.py"), os.path.join(EXAMPLES, fn)],
            capture_output=True, timeout=MAX_ONE + 30,
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

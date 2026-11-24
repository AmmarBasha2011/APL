#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_repo_size.py — حارس أحجام الريبو.

يفشل (exit 1) لو:
  - أي ملف متتبَّع في git أكبر من 4 ميجابايت (الحد الحالي أعلى من
    أكبر ملف موجود اليوم ~2MB، ليكشف النمو المفاجئ فقط).
  - حجم شجرة العمل كاملة (بدون .git) أكبر من 200 ميجابايت.
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_FILE = 4 * 1024 * 1024      # 4 MB لكل ملف
MAX_TOTAL = 200 * 1024 * 1024   # 200 MB للريبو كله


def main():
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.splitlines()
    total = 0
    broken = 0
    for rel in out:
        full = os.path.join(ROOT, rel)
        try:
            size = os.path.getsize(full)
        except OSError:
            continue
        total += size
        if size > MAX_FILE:
            print(f"✗ ملف ضخم: {rel} ({size / 1048576:.1f} MB > 4 MB)")
            broken += 1
    if total > MAX_TOTAL:
        print(f"✗ حجم الريبو: {total / 1048576:.0f} MB > 200 MB")
        broken += 1
    if broken:
        return 1
    print(f"✓ أحجام الريبو سليمة ({total / 1048576:.0f} MB، أكبر ملف تحت 4 MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

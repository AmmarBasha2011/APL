#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_docs.py — تغطية توثيق المكتبات.

يفشل (exit 1) لو:
  1. مكتبة في LIBRARIES مفيهاش ملف docs/<name>-library.md.
  2. مفتاح عربي (دالة أو خاصية) في المكتبة مش موجود في ملف التوثيق.
  3. مفتاح موثّق في الملف ومش موجود في المكتبة (توثيق قديم/غلط).

الاستخدام:
    python scripts/check_docs.py          # تقرير + exit 1 عند النقص
    python scripts/check_docs.py --quiet
"""

import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from core.libraries import LIBRARIES  # noqa: E402

BACKTICK = re.compile(r"`([^`]+)`")
HAS_ARABIC = re.compile(r"[\u0600-\u06FF]")


def library_keys(mod):
    keys = set()
    for attr in dir(mod):
        if attr.isupper() and isinstance(getattr(mod, attr), dict):
            keys.update(k.strip() for k in getattr(mod, attr).keys())
    return keys


FENCED = re.compile(r"```.*?```", re.S)
TABLE_KEY = re.compile(r"^\|\s*`([^`]+)`")


def documented_keys(doc_path):
    with open(doc_path, encoding="utf-8") as f:
        text = f.read()
    text = FENCED.sub("", text)
    keys = set()
    for line in text.splitlines():
        m = TABLE_KEY.match(line)
        if m:
            keys.add(m.group(1).strip().lstrip("."))
    return keys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    failures = 0
    for name, mod in sorted(LIBRARIES.items()):
        doc_path = os.path.join(ROOT, "docs", f"{name}-library.md")
        keys = library_keys(mod)
        if not os.path.isfile(doc_path):
            print(f"✗ {name}: ملف التوثيق docs/{name}-library.md غير موجود "
                  f"({len(keys)} عنصر بلا توثيق)")
            failures += 1
            continue
        documented = documented_keys(doc_path)
        missing = sorted(keys - documented)
        stale = sorted(documented - keys)
        if missing or stale:
            failures += 1
            print(f"✗ {name}: {len(missing)} غير موثّق، {len(stale)} موثّق بلا وجود")
            if not args.quiet:
                for k in missing[:20]:
                    print(f"    - غير موثّق: {k}")
                for k in stale[:20]:
                    print(f"    - بلا وجود: {k}")

    if failures:
        print(f"\nفشل: {failures} مكتبة فيها نقص توثيق")
        return 1
    print(f"✓ توثيق المكتبات مكتمل ({len(LIBRARIES)} مكتبة)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

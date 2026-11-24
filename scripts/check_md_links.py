#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_md_links.py — فحص الروابط النسبية في ملفات Markdown.

يمشي على كل ملفات ‎.md في الريبو ويفحص إن الروابط النسبية
(مثل examples/01.apl أو docs/time-library.md) تشير لملفات موجودة فعلاً.
الروابط الخارجية (http/https) والمراسي (#) لا تُفحص.

يفشل (exit 1) لو لقي رابطاً مكسوراً.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def iter_md_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__", "node_modules")]
        for fn in filenames:
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)


def main():
    broken = 0
    for path in sorted(iter_md_files()):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        for m in LINK.finditer(text):
            target = m.group(1).split("#")[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            target = target.replace("%20", " ")
            full = os.path.normpath(os.path.join(os.path.dirname(path), target))
            if not os.path.exists(full):
                rel = os.path.relpath(path, ROOT)
                print(f"✗ {rel}: رابط مكسور -> {m.group(1)}")
                broken += 1
    if broken:
        print(f"\nفشل: {broken} رابط مكسور")
        return 1
    print("✓ كل روابط الماركداون النسبية سليمة")
    return 0


if __name__ == "__main__":
    sys.exit(main())

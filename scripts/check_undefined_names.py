#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_undefined_names.py — لا اسم غير معرَّف في الأمثلة والتوثيق.

بعد حذف التكرار صارت أسماء كثيرة (المحذوفة) غير موجودة. أي مثال أو كتلة
```apl في التوثيق ما زالت تستعمل اسماً محذوفاً (أو اسماً خاطئاً) تُنتج بعد
التحويل اسماً غير معرَّف في Python. هذا الفحص يحوّل كل ملف .apl وكل كتلة
```apl في README والتوثيق ثم يمرّر الناتج على ruff بقاعدة F821 فقط.

الاستخدام:
    python scripts/check_undefined_names.py
"""

import glob
import os
import re
import subprocess
import sys
import tempfile
import warnings

warnings.filterwarnings("ignore")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from core.apl_runner.main import transpile  # noqa: E402

# أمثلة توثيقية تُظهر خطأً متعمَّداً أو اسماً خاصاً: (ملف، رقم الكتلة) -> أسماء مسموحة
ALLOWED = {
    ("docs/error-messages.md (كتلة 2)"): {"س"},
    ("docs/language-reference.md (كتلة 17)"): {"سر"},
    ("docs/language-reference.md (كتلة 23)"): {"س"},
}

BLOCK = re.compile(r"```apl\n(.*?)```", re.S)


def sources():
    for f in sorted(glob.glob(os.path.join(ROOT, "examples", "*.apl"))
                    + glob.glob(os.path.join(ROOT, "projects", "**", "*.apl"), recursive=True)):
        yield os.path.relpath(f, ROOT), open(f, encoding="utf-8").read()
    docs = [os.path.join(ROOT, "README.md")] + sorted(glob.glob(os.path.join(ROOT, "docs", "*.md")))
    for f in docs:
        if f.endswith("-library.md"):
            continue
        t = open(f, encoding="utf-8").read()
        for i, m in enumerate(BLOCK.finditer(t), 1):
            yield f"{os.path.relpath(f, ROOT)} (كتلة {i})", m.group(1)


def main():
    bad = []
    n = 0
    with tempfile.TemporaryDirectory() as tmp:
        for name, code in sources():
            try:
                py = transpile(code)
            except Exception:
                continue  # أخطاء التحويل يغطيها فحص الأمثلة وREADME
            p = os.path.join(tmp, "t.py")
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(py)
            n += 1
            r = subprocess.run(
                ["ruff", "check", "--isolated", "--select", "F821", "--output-format", "concise", p],
                capture_output=True, text=True)
            if r.returncode != 0:
                names = sorted(n for n in set(re.findall(r"Undefined name `([^`]+)`", r.stdout)) if not n.lower().startswith("_apl_"))
                names = [x for x in names if x not in ALLOWED.get(name, ())]
                if names:
                    bad.append((name, names))
    for name, names in bad:
        print(f"✗ {name}: أسماء غير معرَّفة: {', '.join(names)}")
    if bad:
        print(f"\nفشل: {len(bad)} مصدر يستعمل أسماء غير معرَّفة (غالباً اسم محذوف بسبب التكرار؛ استعمل الاسم المتبقي في docs/<مكتبة>-library.md).")
        return 1
    print(f"✓ لا أسماء غير معرَّفة في {n} مصدراً (أمثلة + توثيق)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

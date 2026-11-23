#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""يشغّل لعبة «كنز الواحة» بمدخل ثابت ويتأكد من النهايتين: الفوز والخروج المبكر."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GAME = os.path.join(ROOT, "demos", "treasure-game", "game.apl")


def play(commands):
    r = subprocess.run([sys.executable, os.path.join(ROOT, "apl.py"), GAME],
                       input="\n".join(commands) + "\n", capture_output=True,
                       text=True, encoding="utf-8", timeout=60)
    return r.returncode, r.stdout


def main():
    win = ["شرق", "افتح", "غرب", "خذ", "شمال", "خذ", "جنوب", "شرق", "جنوب",
           "خذ", "شمال", "افتح"]
    rc, out = play(win)
    assert rc == 0, rc
    assert "الصندوق مقفل" in out
    assert "وجدت الكنز" in out and "7 خطوة" in out, out

    rc, out = play(["خذ", "خروج"])
    assert rc == 0 and "أخذت: حبل" in out and "مع السلامة" in out

    rc, out = play(["جنوب", "كلام"])  # اتجاه غير موجود وأمر مجهول ثم نهاية الإدخال
    assert rc == 0 and out.count("لا أفهم") == 2, out
    print("✓ لعبة كنز الواحة تعمل")


if __name__ == "__main__":
    main()

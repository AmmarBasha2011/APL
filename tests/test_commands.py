"""Smoke-test every command the README documents.

The command table is the first thing a user reads, and a command that quietly
stops working (or starts needing an argument) is only noticed when someone
tries it. Each check here runs the real command line in a temp folder and
looks for the behaviour the README promises.

Usage:  python tests/test_commands.py
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APL = ROOT / "apl.py"  # the same entry point as ./عمار, but portable

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

FAILURES = []
CHECKS = []


def check(name, condition, detail=""):
    CHECKS.append(name)
    if condition:
        print("PASS  " + name)
    else:
        FAILURES.append(name)
        print("FAIL  " + name + ("\n" + detail if detail else ""))


def clean(text: str) -> str:
    return text.replace("\u202b", "").replace("\u202c", "").replace("\u200f", "")


def main() -> int:
    work = Path(tempfile.mkdtemp(prefix="apl-commands-"))
    (work / "hello.apl").write_text('المتغير س = 5\nاطبع("أهلاً")\nاطبع(س * 2)\n', encoding="utf-8")
    (work / "broken.apl").write_text("لو س = 5:\n    اطبع(س)\n", encoding="utf-8")
    (work / "messy.apl").write_text("المتغير   س=5\nاطبع(  س )\n", encoding="utf-8")
    # The checks must not depend on what this machine happens to have
    # installed: an empty library folder makes every run identical (the
    # Windows runner caught this when مساعدة مكتبات printed a different
    # sentence there than on a developer machine with libraries).
    libraries = work / "libraries"
    libraries.mkdir()
    env = dict(os.environ, APL_NO_CACHE="1", PYTHONIOENCODING="utf-8",
               APL_LIBRARIES=str(libraries))

    def run(args, stdin=""):
        result = subprocess.run([sys.executable, str(APL), *args], cwd=str(work),
                                input=stdin, capture_output=True, text=True,
                                encoding="utf-8", env=env, timeout=120)
        return result.returncode, clean(result.stdout + result.stderr)

    def expect(name, args, want, stdin="", code=0):
        status, text = run(args, stdin)
        check(name, status == code and want in text,
              f"exit={status} (wanted {code})\n{text}")

    expect("عمار شغل runs a program", ["شغل", "hello.apl"], "أهلاً")
    expect("عمار شغل prints the arithmetic", ["شغل", "hello.apl"], "10")
    expect("عمار فحص accepts a valid program", ["فحص", "hello.apl"], "", code=0)
    expect("عمار فحص rejects a broken program", ["فحص", "broken.apl"], "خطأ", code=1)
    expect("عمار ترجمة prints Python", ["ترجمة", "hello.apl"], "print")
    expect("عمار -c runs code", ["-c", "اطبع(2 + 3)"], "5")
    expect("عمار نسخة prints the version", ["نسخة"], "APL v")
    expect("عمار مساعدة prints usage", ["مساعدة"], "الاستخدام")
    expect("عمار مساعدة مكتبات prints the libraries help", ["مساعدة", "مكتبات"], "مكتبات")
    expect("عمار مسح-الكاش reports what it cleared", ["مسح-الكاش"], "ملف")
    expect("عمار تنسيق formats a program", ["تنسيق", "messy.apl"], "اطبع")
    expect("عمار تتبع shows the lines it runs", ["تتبع", "hello.apl"], ":")
    expect("عمار مصحح steps through a program", ["مصحح", "hello.apl"], "خطوة", stdin="\nك\n")
    expect("عمار بناء asks for a file", ["بناء"], "حدد الملف", code=1)
    expect("عمار مشروع تشغيل asks for a project", ["مشروع", "تشغيل"], "apl-project.json", code=1)
    expect("عمار مكتبة قائمة lists the library folder", ["مكتبة", "قائمة"], "المكتبات")
    expect("عمار مكتبة قفل describes the lock", ["مكتبة", "قفل"], "قفل")
    expect("عمار مكتبة تحميل asks for a name", ["مكتبة", "تحميل"], "حدد اسم المكتبة", code=1)
    expect("عمار مسار explains the PATH setup", ["مسار"], "PATH")
    expect("عمار طرفية answers a line", ["طرفية"], "5", stdin="اطبع(2 + 3)\n")
    expect("عمار طرفية greets in Arabic", ["طرفية"], "الطرفية التفاعلية", stdin="")
    expect("عمار طرفية quits on an Arabic word", ["طرفية"], "مع السلامة", stdin="خروج\n")
    expect("عمار طرفية runs a multi-line block", ["طرفية"], "16",
           stdin="دالة مربع(س):\n    ارجع س * س\n\nاطبع(مربع(4))\n")
    expect("an unknown command is refused", ["ززز"], "أمر غير معروف", code=1)

    print()
    total = len(CHECKS)
    print(f"{total - len(FAILURES)}/{total} command checks passed")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

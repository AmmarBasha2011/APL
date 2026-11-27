"""Check that a missing library is named in the error.

The language ships no vocabulary: a program that uses a library word without
the library installed fails as an unknown name. The error must say which
library provides the word and how to install it, so the fix is one command
instead of a hunt.

Usage:  python tests/test_library_words.py
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APL = ROOT / "apl.py"
sys.path.insert(0, str(ROOT))

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


def run(program: str):
    work = Path(tempfile.mkdtemp(prefix="apl-words-"))
    path = work / "program.apl"
    path.write_text(program, encoding="utf-8")
    result = subprocess.run([sys.executable, str(APL), "شغل", str(path)],
                            capture_output=True, text=True, encoding="utf-8", timeout=60)
    return result, (result.stderr or result.stdout).replace("\u202b", "").replace("\u202c", "")


def main() -> int:
    from core.library_words import library_for, table

    words = table()
    check("the word map is shipped", len(words) > 100, str(len(words)))
    check("words map to a library name",
          all(isinstance(value, str) and value for value in list(words.values())[:50]))
    check("an Arabic word is mapped", library_for("جذر") is not None, str(library_for("جذر")))
    check("a word nobody defines is not mapped", library_for("ززززز") is None)

    result, text = run("اطبع(جذر(4))\n")
    check("an unknown library word still fails", result.returncode != 0, text)
    check("the error names the library", "apl-math" in text, text)
    check("the error gives the install command",
          "عمار مكتبة تحميل math" in text, text)

    result, text = run("اللستة = [1]\nاللستة.ألحق(2)\n")
    check("a missing library method names its library", "apl-advanced" in text, text)

    result, text = run("المتغير مجموع = 5\nاطبع(مجموعع)\n")
    check("a plain typo still suggests the nearby name", "هل تقصد" in text, text)
    check("a plain typo claims no library", "مكتبة apl" not in text, text)

    print()
    total = len(CHECKS)
    print(f"{total - len(FAILURES)}/{total} library word checks passed")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Check `عمار بناء` without waiting for a real build.

A full PyInstaller build takes seconds and needs PyInstaller installed, so the
suite checks the parts that decide whether a build would be right: the command
line, the generated entry program, and the refusals (a missing file, a program
that does not compile).

Usage:  python tests/test_build.py
"""
from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "tools" / "build_program.py"

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


def load():
    spec = importlib.util.spec_from_file_location("apl_build_program", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    work = Path(tempfile.mkdtemp(prefix="apl-build-test-"))
    program = work / "sample.apl"
    program.write_text('دالة ترحيب(الاسم):\n    ارجع f"أهلاً يا {الاسم}"\n\nاطبع(ترحيب("عمار"))\n',
                       encoding="utf-8")

    outcome = module.build(program, dry_run=True)
    check("a program that compiles plans a build", outcome.get("ok") is True,
          str(outcome))
    command = outcome.get("command") or []
    check("the build is one file", "--onefile" in command, " ".join(command))
    check("it packs the interpreter's package",
          any("core" in str(item) for item in command), " ".join(command))
    check("it uses the program name by default", "sample" in command, " ".join(command))
    entry = Path(outcome.get("entry") or "")
    check("it writes an entry program", entry.is_file())
    text = entry.read_text(encoding="utf-8") if entry.is_file() else ""
    check("the entry program carries the source",
          'اطبع(ترحيب("عمار"))' in text, text[:200])
    check("the entry program runs the real engine",
          "Compilation" in text and "execute" in text, text[:200])

    named = module.build(program, name="أداة", dry_run=True)
    check("a chosen name reaches the command", "أداة" in (named.get("command") or []),
          str(named.get("command")))

    broken = work / "broken.apl"
    broken.write_text('لو س = 5\n    اطبع(س)\n', encoding="utf-8")
    outcome = module.build(broken, dry_run=True)
    check("a program that does not compile is refused",
          outcome.get("ok") is False and "خطأ" in str(outcome.get("error")), str(outcome))

    missing = module.build(work / "nothing.apl", dry_run=True)
    check("a missing file is refused",
          missing.get("ok") is False and "مفيش ملف" in str(missing.get("error")), str(missing))

    cli = subprocess.run([sys.executable, str(ROOT / "apl.py"), "بناء"],
                         capture_output=True, text=True, encoding="utf-8")
    check("the command asks for a file when given none",
          cli.returncode != 0 and "حدد الملف" in (cli.stdout + cli.stderr),
          cli.stdout + cli.stderr)

    print()
    total = len(CHECKS)
    print(f"{total - len(FAILURES)}/{total} build checks passed")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

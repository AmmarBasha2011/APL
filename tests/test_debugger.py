"""Check عمار تتبع and عمار مصحح.

Both are driven through the real command line, the way a user drives them, with
stdin piped in for the stepper's commands.

Usage:  python tests/test_debugger.py
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APL = ROOT / "apl.py"

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

FAILURES = []
CHECKS = []

PROGRAM = '''دالة مربع(س):
    ارجع س * س

لكل رقم في [2, 3]:
    اطبع(مربع(رقم))
'''


def check(name, condition, detail=""):
    CHECKS.append(name)
    if condition:
        print("PASS  " + name)
    else:
        FAILURES.append(name)
        print("FAIL  " + name + ("\n" + detail if detail else ""))


def run(args, stdin="", timeout=60):
    return subprocess.run([sys.executable, str(APL), *args], input=stdin,
                          capture_output=True, text=True, encoding="utf-8",
                          timeout=timeout)


def clean(text: str) -> str:
    return text.replace("\u202b", "").replace("\u202c", "").replace("\u200f", "")


def main() -> int:
    work = Path(tempfile.mkdtemp(prefix="apl-debug-test-"))
    program = work / "trace.apl"
    program.write_text(PROGRAM, encoding="utf-8")

    trace = clean(run(["تتبع", str(program)]).stdout)
    check("the trace shows the function line with its number",
          "1: دالة مربع(س):" in trace, trace)
    check("the trace follows the loop", "4: لكل رقم في [2, 3]:" in trace, trace)
    check("the trace goes inside the function", "2: ارجع س * س" in trace, trace)
    check("the program still prints its output", "4" in trace and "9" in trace, trace)
    order = [trace.find("4: لكل"), trace.find("5: اطبع"), trace.find("2: ارجع")]
    check("lines are reported in the order they run", order == sorted(order) and -1 not in order,
          str(order))

    stepped = clean(run(["مصحح", str(program)], stdin="\nم\nك\n").stdout)
    check("the stepper stops before the first line", "1: دالة مربع(س):" in stepped, stepped)
    check("the stepper asks for a command", "خطوة" in stepped, stepped)
    check("vars shows the program's own names", "مربع = <function" in stepped, stepped)
    check("vars hides the runtime's machinery", "builtins =" not in stepped, stepped)
    check("continue runs the program to the end", "4" in stepped and "9" in stepped, stepped)

    at_break = clean(run(["مصحح", str(program), "--توقف", "2"], stdin="ك\nك\nك\n").stdout)
    check("a breakpoint stops inside the function",
          at_break.count("2: ارجع س * س") >= 2, at_break)

    broken = work / "broken.apl"
    broken.write_text("اطبع(ناقص)\n", encoding="utf-8")
    result = run(["تتبع", str(broken)])
    check("an error in a traced program is reported in Arabic",
          result.returncode != 0 and "خطأ" in clean(result.stderr), clean(result.stderr))

    nothing = run(["تتبع"])
    check("the command asks for a file when given none",
          nothing.returncode != 0 and "حدد الملف" in clean(nothing.stdout + nothing.stderr),
          clean(nothing.stdout + nothing.stderr))

    print()
    total = len(CHECKS)
    print(f"{total - len(FAILURES)}/{total} debugger checks passed")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

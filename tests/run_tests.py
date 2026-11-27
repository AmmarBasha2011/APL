"""APL test suite: run every cases/*.apl and compare its output.

Each case is a pair:
    cases/<name>.apl   the program
    cases/<name>.out   the exact stdout it must print

A case whose name ends with "_error" instead expects a failing exit code and a
stderr that contains the matching .out text.

Usage:  python tests/run_tests.py [-v]
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

# Windows consoles default to a legacy code page; Arabic test names would crash
# the reporter before it could report anything.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
CASES = Path(__file__).resolve().parent / "cases"
APL = ROOT / "apl.py"


def clean(text: str) -> str:
    """Drop the RTL marks the Arabic console wrapper adds, and trailing space."""
    text = text.replace("\u202b", "").replace("\u202c", "").replace("\u200f", "")
    lines = [line.strip() for line in text.replace("\r\n", "\n").split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def run_case(program: Path) -> tuple[bool, str]:
    expected_file = program.with_suffix(".out")
    expected = clean(expected_file.read_text(encoding="utf-8"))
    env = dict(os.environ, PYTHONIOENCODING="utf-8", APL_NO_CACHE="1")
    proc = subprocess.run(
        [sys.executable, str(APL), "شغل", program.name],
        cwd=str(CASES), capture_output=True, text=True, encoding="utf-8", env=env,
    )
    wants_error = program.stem.endswith("_error")
    if wants_error:
        stderr = clean(proc.stderr)
        ok = proc.returncode != 0 and expected in stderr
        detail = "" if ok else f"exit={proc.returncode} stderr={stderr!r}"
        return ok, detail
    out = clean(proc.stdout)
    ok = proc.returncode == 0 and out == expected
    if ok:
        return True, ""
    return False, f"exit={proc.returncode}\n--- expected ---\n{expected}\n--- got ---\n{out}\n--- stderr ---\n{clean(proc.stderr)}"


def main(argv: list[str]) -> int:
    verbose = "-v" in argv or "--verbose" in argv
    programs = sorted(CASES.glob("*.apl"))
    if not programs:
        print("no test cases found")
        return 1
    failures = 0
    for program in programs:
        if not program.with_suffix(".out").is_file():
            print("SKIP  " + program.stem + "  (no .out)")
            continue
        ok, detail = run_case(program)
        print(("PASS  " if ok else "FAIL  ") + program.stem)
        if not ok:
            failures += 1
            print(detail)
        elif verbose:
            print("      " + clean(program.with_suffix(".out").read_text(encoding="utf-8")))
    print()
    print(f"{len(programs) - failures}/{len(programs)} passed")

    # Parts of the project are checked by their own scripts: the language
    # server (a separate process speaking LSP) and the browser playground
    # (a page with a Python half no Python tool would otherwise run).
    extras = (
        ("language server", "test_lsp.py"),
        ("playground", "test_playground.py"),
        ("عمار بناء", "test_build.py"),
        ("debugger", "test_debugger.py"),
        ("lockfile", "test_lockfile.py"),
        ("مشروع", "test_project.py"),
        ("library words", "test_library_words.py"),
        ("pip dependencies", "test_pip_deps.py"),
        ("commands", "test_commands.py"),
    )
    for label, script in extras:
        path = Path(__file__).resolve().parent / script
        if not path.is_file():
            continue
        result = subprocess.run([sys.executable, str(path)], capture_output=True,
                                text=True, encoding="utf-8", cwd=str(ROOT))
        ok = result.returncode == 0
        print(("PASS  " if ok else "FAIL  ") + label)
        if not ok:
            failures += 1
            print(clean(result.stdout) + "\n" + clean(result.stderr))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

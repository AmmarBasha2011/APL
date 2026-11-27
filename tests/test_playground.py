"""Check the browser playground without a browser.

Three things can rot quietly in `playground/`:

1. the file manifest, when a module is added or renamed;
2. the page's wiring, if an element id or the Pyodide URL changes;
3. the Python half of the page, which no Python tool runs by default.

So this test regenerates the manifest and compares it, reads the page for the
pieces it must contain, and then runs the page's own bootstrap code here in
CPython against a copy of `core/` - the same calls the browser makes after it
writes the files into Pyodide's filesystem.

Usage:  python tests/test_playground.py
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "playground" / "index.html"
MANIFEST = ROOT / "playground" / "manifest.json"

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


def bootstrap_source(page: str) -> str:
    """Pull the page's BOOTSTRAP template literal out and unescape it."""
    match = re.search(r"const BOOTSTRAP = `(.*?)`;", page, re.S)
    if not match:
        return ""
    code = match.group(1)
    return code.replace("\\\\n", "\\n").replace('\\\\"', '\\"').replace("\\\\", "\\")


def main() -> int:
    page = PAGE.read_text(encoding="utf-8") if PAGE.is_file() else ""
    check("the playground page exists", bool(page))
    check("it loads Pyodide from a pinned version",
          bool(re.search(r"pyodide/v\d+\.\d+\.\d+/full/pyodide\.js", page)))
    for element in ("source", "output", "run", "status"):
        check(f"the page has the #{element} element", f'id="{element}"' in page)
    check("it reads the generated manifest", "manifest.json" in page)
    check("it falls back to the raw sources when the page is hosted elsewhere",
          "raw.githubusercontent.com/AmmarBasha2011/APL/main/" in page)
    # The page is served from playground/, so the sources are one level up. A
    # base of "./" silently 404s on every module: that was a real bug, and this
    # check is what makes it visible without a browser.
    check("it looks for the sources one level above the page, not beside it",
          'new URL("../", location.href).href' in page
          and 'new URL("./", location.href)' not in page,
          "the page must resolve the interpreter from ../, the repository root")
    check("it probes a file that really exists before trusting a base",
          'const PROBE = "core/__init__.py"' in page
          and (ROOT / "core" / "__init__.py").is_file())

    check("manifest.json exists", MANIFEST.is_file())
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.is_file() else {"files": []}
    listed = {item["path"] for item in manifest.get("files", [])}
    on_disk = {path.relative_to(ROOT).as_posix()
               for path in (ROOT / "core").rglob("*.py")
               if "__pycache__" not in path.parts}
    check("the manifest lists exactly the interpreter's modules", listed == on_disk,
          f"missing={sorted(on_disk - listed)} extra={sorted(listed - on_disk)}")
    check("the manifest lists the transpiler and the runtime",
          "core/runner/main.py" in listed and "core/runner/transpiler.py" in listed)

    fresh = subprocess.run([sys.executable, str(ROOT / "tools" / "build_playground.py"), "--check"],
                           capture_output=True, text=True, encoding="utf-8")
    check("the manifest is not stale", fresh.returncode == 0, fresh.stdout + fresh.stderr)

    code = bootstrap_source(page)
    check("the page carries its Python bootstrap", "def apl_run" in code)
    if not code:
        return 1

    # Run the page's own Python here: copy the sources the browser would write
    # into Pyodide's filesystem, then call the same function the page calls.
    work = Path(tempfile.mkdtemp(prefix="apl-playground-"))
    try:
        shutil.copytree(ROOT / "core", work / "core",
                        ignore=shutil.ignore_patterns("__pycache__"))
        check("the bootstrap puts the downloaded sources on the path", '"/apl"' in code)
        # The browser writes the sources to /apl inside Pyodide's filesystem;
        # here they live in the temporary directory, so point the same line at it.
        local_code = code.replace('"/apl"', json.dumps(str(work)))
        namespace: dict = {}
        exec(compile(local_code, "<playground-bootstrap>", "exec"), namespace)
        run = namespace.get("apl_run")
        check("the bootstrap defines apl_run", callable(run))
        if not callable(run):
            return 1

        good = 'اطبع("أهلاً")\nاطبع(طول("أربعة"))\nاطبع(٢+٢)\n'
        output = run(good)
        check("a working program prints its output",
              "أهلاً" in output and "5" in output and "4" in output, repr(output))

        bad = 'لو س = 5:\n    اطبع(س)\n'
        output = run(bad)
        check("a broken program reports the compiler's error",
              "APL-" in output or "خطأ" in output, repr(output))

        empty = run("# كومنت بس\n")
        check("a program that prints nothing returns empty text", empty.strip() == "", repr(empty))
    finally:
        shutil.rmtree(work, ignore_errors=True)

    print()
    total = len(CHECKS)
    print(f"{total - len(FAILURES)}/{total} playground checks passed")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

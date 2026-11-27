"""Check that installing a library never installs Python packages on its own.

A library's apl-library.json can name the Python packages it needs. Installing
those packages is the user's decision, so the install only does it with
--مع-الاعتمادات, and says which packages it is about to install first. The pip
command itself is replaced here by a stub, so the suite needs no network.

Usage:  python tests/test_pip_deps.py
"""
from __future__ import annotations

import json
import os
import shlex
import shutil
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
    work = Path(tempfile.mkdtemp(prefix="apl-pip-"))
    library = work / "lib"
    library.mkdir()
    (library / "apl-library.json").write_text(json.dumps({
        "name": "demo", "version": "1.0.0", "entry": "demo_funcs.py",
        "requires": ["tabulate"], "libraries": [],
    }), encoding="utf-8")
    (library / "demo_funcs.py").write_text('"""demo"""\n', encoding="utf-8")

    record = work / "record.txt"
    stub = work / "stub.py"
    stub.write_text(
        "import sys, pathlib\n"
        "pathlib.Path(sys.argv[1]).write_text(' '.join(sys.argv[2:]), encoding='utf-8')\n",
        encoding="utf-8")
    failing = work / "failing.py"
    failing.write_text("import sys\nsys.exit(3)\n", encoding="utf-8")

    base = dict(os.environ, APL_NO_CACHE="1", APL_LIBRARIES=str(work / "home"),
                PYTHONIOENCODING="utf-8")

    def install(*args, pip_command):
        env = dict(base, APL_PIP_CMD=pip_command)
        result = subprocess.run([sys.executable, str(APL), "مكتبة", "تحميل", str(library), *args],
                                capture_output=True, text=True, encoding="utf-8", env=env)
        return result, clean(result.stdout + result.stderr)

    def command(*parts):
        # A Windows path needs its quotes kept, a POSIX one needs shell quoting.
        if os.name == "nt":
            return subprocess.list2cmdline([str(part) for part in parts])
        return " ".join(shlex.quote(str(part)) for part in parts)

    stub_command = command(sys.executable, stub, record)

    result, text = install(pip_command=stub_command)
    check("a plain install succeeds", result.returncode == 0, text)
    check("it does not install Python packages", not record.exists(),
          "pip was called: " + (record.read_text(encoding="utf-8") if record.exists() else ""))
    check("it names the packages the library needs", "tabulate" in text, text)
    check("it offers the opt-in flag", "--مع-الاعتمادات" in text, text)

    shutil.rmtree(work / "home", ignore_errors=True)
    record.unlink(missing_ok=True)
    result, text = install("--مع-الاعتمادات", pip_command=stub_command)
    check("the flag installs the packages", record.exists()
          and record.read_text(encoding="utf-8").strip() == "tabulate", text)
    check("it says what it is about to install", "بنسطّب حزم Python" in text, text)

    shutil.rmtree(work / "home", ignore_errors=True)
    result, text = install("--مع-الاعتمادات", pip_command=command(sys.executable, failing))
    check("a failed pip run keeps the library", result.returncode == 0
          and (work / "home" / "demo" / "apl-library.json").is_file(), text)
    check("a failed pip run says what to do", "فشل تثبيت حزم Python" in text, text)

    shutil.rmtree(work / "home", ignore_errors=True)
    (library / "apl-library.json").write_text(json.dumps({
        "name": "demo", "version": "1.0.0", "entry": "demo_funcs.py", "requires": [],
    }), encoding="utf-8")
    record.unlink(missing_ok=True)
    result, text = install("--مع-الاعتمادات", pip_command=stub_command)
    check("a library with no Python packages never calls pip", not record.exists(), text)

    print()
    total = len(CHECKS)
    print(f"{total - len(FAILURES)}/{total} dependency checks passed")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

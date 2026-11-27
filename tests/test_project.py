"""Check `عمار مشروع جديد` and `عمار مشروع تشغيل`.

A new project has to be a real folder a user can immediately run, so the suite
creates one in a temp dir, runs it through the real command line, and checks
the refusals (an existing non-empty folder, a missing project file).

Usage:  python tests/test_project.py
"""
from __future__ import annotations

import json
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


def run(args, cwd):
    return subprocess.run([sys.executable, str(APL), *args], cwd=str(cwd),
                          capture_output=True, text=True, encoding="utf-8", timeout=60)


def clean(text: str) -> str:
    return text.replace("\u202b", "").replace("\u202c", "").replace("\u200f", "")


def main() -> int:
    work = Path(tempfile.mkdtemp(prefix="apl-project-test-"))

    made = run(["مشروع", "جديد", "تجريبي"], work)
    folder = work / "تجريبي"
    check("عمار مشروع جديد creates the folder", folder.is_dir(), clean(made.stdout + made.stderr))
    check("the project has a program", (folder / "main.apl").is_file())
    check("the project has a config", (folder / "apl-project.json").is_file())
    check("the project has a README", (folder / "README.md").is_file())
    check("the project has a .gitignore", (folder / ".gitignore").is_file())

    config = json.loads((folder / "apl-project.json").read_text(encoding="utf-8"))
    check("the config names the entry file", config.get("entry") == "main.apl", json.dumps(config))
    check("the config carries the project name", config.get("name") == "تجريبي", json.dumps(config))

    ran = run(["مشروع", "تشغيل"], folder)
    check("عمار مشروع تشغيل runs the project",
          ran.returncode == 0 and "أهلاً بالعالم" in clean(ran.stdout), clean(ran.stdout + ran.stderr))

    bare = run(["مشروع"], folder)
    check("عمار مشروع alone runs the project", bare.returncode == 0 and "أهلاً بالعالم" in clean(bare.stdout),
          clean(bare.stdout + bare.stderr))

    again = run(["مشروع", "جديد", "تجريبي"], work)
    check("a non-empty folder is refused",
          again.returncode != 0 and "موجود" in clean(again.stderr), clean(again.stderr))

    nowhere = run(["مشروع", "تشغيل"], work)
    check("running outside a project is refused",
          nowhere.returncode != 0 and "apl-project.json" in clean(nowhere.stderr), clean(nowhere.stderr))

    # A config that points at a file nobody wrote must say so, not crash.
    broken = work / "مكسور"
    broken.mkdir()
    (broken / "apl-project.json").write_text(
        json.dumps({"name": "مكسور", "entry": "ناقص.apl"}), encoding="utf-8")
    missing = run(["مشروع", "تشغيل"], broken)
    check("a missing entry file is reported",
          missing.returncode != 0 and "ناقص.apl" in clean(missing.stderr), clean(missing.stderr))

    print()
    total = len(CHECKS)
    print(f"{total - len(FAILURES)}/{total} project checks passed")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

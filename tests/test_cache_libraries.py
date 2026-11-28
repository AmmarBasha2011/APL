"""The transpile cache must notice a library being installed.

Usage:  python tests/test_cache_libraries.py
"""
import os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
failures = 0


def check(name, ok, detail=""):
    global failures
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok else "  " + detail))
    failures += 0 if ok else 1


work = Path(tempfile.mkdtemp())
libs = work / "libs"
libs.mkdir()
prog = work / "p.apl"
prog.write_text('اطبع ثلاثة_مرات(-2)\n', encoding="utf-8")
env = dict(os.environ, APL_LIBRARIES=str(libs), PYTHONIOENCODING="utf-8")
env.pop("APL_NO_CACHE", None)


def run():
    return subprocess.run([sys.executable, str(ROOT / "apl.py"), "شغل", str(prog)],
                          capture_output=True, text=True, encoding="utf-8", env=env, cwd=str(work))


first = run()
check("without the library the word is unknown", first.returncode != 0, first.stdout)
(libs / "x_funcs.py").write_text(
    'X_FUNCS = {"ثلاثة_مرات": "abs"}\nX_PATTERN = r"(?<!\\w)ثلاثة_مرات\\s*\\("\n'
    'def X_SUBSTITUTE(text):\n    import re\n    return re.sub(r"(?<!\\w)ثلاثة_مرات\\s*\\(", "abs(", text)\n',
    encoding="utf-8")
second = run()
check("the cached translation is not reused after the install",
      second.returncode == 0 and second.stdout.strip().replace("\u202b", "").replace("\u202c", "").strip() == "2",
      second.stdout + second.stderr)
print()
raise SystemExit(1 if failures else 0)

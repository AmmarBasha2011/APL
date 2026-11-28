"""مسح-الكاش looks next to the program and at the project root.

Usage:  python tests/test_clear_cache.py
"""
import os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
failures = 0


def check(name, ok, detail=""):
    global failures
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok else "  " + detail))
    failures += 0 if ok else 1


work = Path(tempfile.mkdtemp()).resolve()
(work / "apl-project.json").write_text('{"name":"p","entry":"main.apl"}', encoding="utf-8")
sub = work / "src" / "deep"
sub.mkdir(parents=True)
elsewhere = Path(tempfile.mkdtemp()).resolve()
env = dict(os.environ, APL_LIBRARIES=str(work / "libs"), PYTHONIOENCODING="utf-8")
env.pop("APL_NO_CACHE", None)


def apl(*args, cwd):
    return subprocess.run([sys.executable, str(ROOT / "apl.py"), *args], capture_output=True,
                          text=True, encoding="utf-8", env=env, cwd=str(cwd))


def entries(folder):
    return [p for p in Path(folder).rglob("__pycache__/*.py")]


(work / "main.apl").write_text('اطبع 1\\n'.replace("\\n", "\n"), encoding="utf-8")
(sub / "m.apl").write_text("اطبع 2\n", encoding="utf-8")
apl("شغل", str(work / "main.apl"), cwd=elsewhere)
apl("شغل", str(sub / "m.apl"), cwd=elsewhere)
check("running programs left cache files", len(entries(work)) >= 2, str(entries(work)))

out = apl("مسح-الكاش", cwd=elsewhere)
check("from an unrelated folder nothing is found", "0" in out.stdout and len(entries(work)) >= 2, out.stdout)

out = apl("مسح-الكاش", str(sub / "m.apl"), cwd=elsewhere)
check("given a program, its folder and the project root are cleared",
      len(entries(work)) == 0 and "0 ملف" not in out.stdout, out.stdout + str(entries(work)))

apl("شغل", str(sub / "m.apl"), cwd=elsewhere)
out = apl("مسح-الكاش", cwd=sub)
check("from inside the project the project root is searched",
      len(entries(work)) == 0, out.stdout + str(entries(work)))
out = apl("مسح-الكاش", str(work / "nope"), cwd=elsewhere)
check("a path that does not exist is an error", out.returncode != 0, out.stdout + out.stderr)
print()
raise SystemExit(1 if failures else 0)

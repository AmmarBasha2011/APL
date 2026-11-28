"""Installing a library must not touch anything outside the library home.

A manifest is untrusted input: its name picks the install folder and its entry
picks the file that runs. Every case here builds a hostile manifest and checks
that the install is refused and that nothing was deleted or written outside.

Usage:  python tests/test_install_safety.py
"""
import json, os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
failures = 0


def check(name, ok, detail=""):
    global failures
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok else "  " + detail))
    failures += 0 if ok else 1


base = Path(tempfile.mkdtemp()).resolve()
home = base / "home" / "libs"
home.mkdir(parents=True)
victim = base / "home" / "precious"
victim.mkdir()
(victim / "keep.txt").write_text("keep", encoding="utf-8")
secret = base / "secret.py"
secret.write_text("X = 1\n", encoding="utf-8")
env = dict(os.environ, APL_LIBRARIES=str(home), PYTHONIOENCODING="utf-8")


def make(folder_name, manifest, entry_text="X_FUNCS = {}\n", entry_file="ok_funcs.py"):
    folder = base / "src" / folder_name
    folder.mkdir(parents=True)
    (folder / "apl-library.json").write_text(json.dumps(manifest), encoding="utf-8")
    if entry_file:
        (folder / entry_file).write_text(entry_text, encoding="utf-8")
    return folder


def install(folder):
    return subprocess.run([sys.executable, str(ROOT / "apl.py"), "مكتبة", "تحميل", str(folder)],
                          capture_output=True, text=True, encoding="utf-8", env=env, cwd=str(base))


def untouched():
    return (victim / "keep.txt").read_text(encoding="utf-8") == "keep" and secret.exists()


good = install(make("good", {"name": "ok", "entry": "ok_funcs.py", "version": "1.0.0"}))
check("a normal library installs", good.returncode == 0 and (home / "ok").is_dir(), good.stdout + good.stderr)

bad_names = {
    "dotdot": "../precious",
    "deep dotdot": "../../home/precious",
    "absolute": str(victim),
    "slash": "a/b",
    "backslash": "a\\b",
    "dot": ".",
    "dots": "..",
    "hyphen": "my-lib",
    "space": "my lib",
    "empty": "",
    "dunder": "__x",
    "number": 5,
}
for label, value in bad_names.items():
    folder = make("n_" + label.replace(" ", "_"), {"name": value, "entry": "ok_funcs.py"})
    result = install(folder)
    if value == "":
        # An empty name falls back to the folder name, which is valid here.
        check("empty name falls back to the folder name", untouched(), result.stdout + result.stderr)
        continue
    check(f"name {label} is refused", result.returncode != 0 and untouched(), result.stdout + result.stderr)

bad_entries = {
    "parent": "../secret.py",
    "absolute": str(secret),
    "not python": "ok_funcs.txt",
    "nested up": "sub/../../secret.py",
}
for label, value in bad_entries.items():
    folder = make("e_" + label.replace(" ", "_"), {"name": "entrytest", "entry": value})
    result = install(folder)
    check(f"entry {label} is refused", result.returncode != 0 and not (home / "entrytest").exists()
          and untouched(), result.stdout + result.stderr)

# The existing install of a name must survive a refused reinstall.
before = sorted(p.name for p in (home / "ok").iterdir())
install(make("bad_again", {"name": "ok", "entry": "../secret.py"}))
check("a refused reinstall leaves the existing library alone",
      sorted(p.name for p in (home / "ok").iterdir()) == before)

# A symlink inside the library is refused.
linked = make("linked", {"name": "linked", "entry": "ok_funcs.py"})
try:
    os.symlink(str(secret), str(linked / "link.py"))
    result = install(linked)
    check("a library containing a symlink is refused",
          result.returncode != 0 and not (home / "linked").exists(), result.stdout + result.stderr)
except (OSError, NotImplementedError):
    print("SKIP  symlinks unavailable here")

# A symlinked install target is never deleted through.
os.symlink(str(victim), str(home / "evil"))
result = install(make("evil_src", {"name": "evil", "entry": "ok_funcs.py"}))
check("an install target that is a symlink is refused", result.returncode != 0 and untouched(),
      result.stdout + result.stderr)

# Removal takes the same care.
for hostile in ("../precious", "..", "a/b", str(victim)):
    result = subprocess.run([sys.executable, str(ROOT / "apl.py"), "مكتبة", "حذف", hostile],
                            capture_output=True, text=True, encoding="utf-8", env=env, cwd=str(base))
    check(f"removing {hostile!r} is refused", result.returncode != 0 and untouched(),
          result.stdout + result.stderr)
result = subprocess.run([sys.executable, str(ROOT / "apl.py"), "مكتبة", "حذف", "evil"],
                        capture_output=True, text=True, encoding="utf-8", env=env, cwd=str(base))
check("removing a symlinked entry does not delete what it points to", untouched(),
      result.stdout + result.stderr)

print()
raise SystemExit(1 if failures else 0)

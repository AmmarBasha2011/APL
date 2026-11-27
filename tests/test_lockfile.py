"""Check version pinning and the lockfile, without touching the network.

`عمار مكتبة تحميل numpy@1.0.0` must fetch that tag, and `عمار مكتبة قفل` /
`عمار مكتبة استعادة` must record and replay exactly what is installed. The
suite replaces the downloader with an in-memory tarball, so it checks the
refs the package manager asks for and the lock it writes without a network
call.

Usage:  python tests/test_lockfile.py
"""
from __future__ import annotations

import io
import json
import os
import sys
import tarfile
import tempfile
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
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


def tarball(version="1.0.0", name="demo"):
    """A GitHub-shaped tarball holding one library."""
    meta = {
        "name": name,
        "version": version,
        "title": "مكتبة تجريبية",
        "entry": f"{name}_funcs.py",
        "requires": [],
        "libraries": [],
    }
    code = '"""Demo library."""\n'
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
        for path, text in ((f"{name}-{version}/apl-library.json", json.dumps(meta)),
                           (f"{name}-{version}/{name}_funcs.py", code)):
            data = text.encode("utf-8")
            info = tarfile.TarInfo(path)
            info.size = len(data)
            archive.addfile(info, io.BytesIO(data))
    return buffer.getvalue()


def main():
    home = Path(tempfile.mkdtemp(prefix="apl-lock-home-"))
    # Path.home() reads HOME on POSIX and USERPROFILE on Windows; set both so
    # the lockfile this test writes never lands in the real home folder.
    os.environ["HOME"] = str(home)
    os.environ["USERPROFILE"] = str(home)
    os.environ["APL_LIBRARIES"] = str(home / ".apl" / "libraries")
    os.environ["APL_NO_CACHE"] = "1"

    import core.cli as cli

    # --- pinning syntax ---------------------------------------------------
    check("numpy@1.0.0 pins a version", cli._split_version("numpy@1.0.0") == ("numpy", "1.0.0"))
    check("numpy==1.0.0 pins a version", cli._split_version("numpy==1.0.0") == ("numpy", "1.0.0"))
    check("a bare name pins nothing", cli._split_version("numpy") == ("numpy", None))

    # --- the refs a pinned install asks codeload for ----------------------
    seen = {}

    def fake_download(owner, repo, refs=None):
        seen["owner"], seen["repo"], seen["refs"] = owner, repo, refs
        return tarball("1.0.0")

    real_download = cli._download_tarball
    cli._download_tarball = fake_download
    try:
        out = io.StringIO()
        with redirect_stdout(out):
            code = cli._library_install("demo@1.0.0")
        check("pinned install succeeds", code == 0, out.getvalue())
        check("pinned install fetches the tag by name",
              seen.get("refs") == ("v1.0.0", "1.0.0"), repr(seen.get("refs")))
        check("pinned install lands in the library home",
              (home / ".apl" / "libraries" / "demo" / "apl-library.json").is_file())

        lock = json.loads((home / ".apl" / "lock.json").read_text(encoding="utf-8"))
        check("lock records the version", lock.get("demo", {}).get("version") == "1.0.0", json.dumps(lock))
        check("lock records the source",
              lock.get("demo", {}).get("source") == "https://github.com/AmmarBasha2011/apl-demo",
              json.dumps(lock))

        # --- showing the lock --------------------------------------------
        out = io.StringIO()
        with redirect_stdout(out):
            code = cli._library_lock()
        text = out.getvalue()
        check("عمار مكتبة قفل lists the pinned version", code == 0 and "demo 1.0.0" in text, text)

        # --- restoring from the lock -------------------------------------
        import shutil
        shutil.rmtree(home / ".apl" / "libraries" / "demo")
        cli._download_tarball = fake_download
        out = io.StringIO()
        with redirect_stdout(out):
            code = cli._library_sync()
        text = out.getvalue()
        check("عمار مكتبة استعادة reinstalls a missing library",
              code == 0 and (home / ".apl" / "libraries" / "demo").is_dir(), text)
        check("restore asks for the locked version",
              seen.get("refs") == ("v1.0.0", "1.0.0"), repr(seen.get("refs")))

        out = io.StringIO()
        with redirect_stdout(out):
            code = cli._library_sync()
        check("restore skips what is already installed",
              code == 0 and "متسطبة بالفعل" in out.getvalue(), out.getvalue())

        # --- a version that does not exist -------------------------------
        cli._download_tarball = lambda owner, repo, refs=None: None
        err, out = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = cli._library_install("demo@9.9.9")
        check("a missing version fails", code == 1, out.getvalue())
        check("a missing version says which one", "9.9.9" in err.getvalue(), err.getvalue())

        # --- removing clears the lock entry ------------------------------
        cli._library_remove("demo")
        lock = json.loads((home / ".apl" / "lock.json").read_text(encoding="utf-8"))
        check("removing a library clears its lock entry", "demo" not in lock, json.dumps(lock))
    finally:
        cli._download_tarball = real_download

    print()
    print(f"{len(CHECKS) - len(FAILURES)}/{len(CHECKS)} checks passed")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Helpers the companion apps share."""
import os
import subprocess
import sys
from pathlib import Path


def apl_command():
    """The command line that runs APL itself, frozen or from source."""
    if getattr(sys, "frozen", False):
        return [sys.executable]
    return [sys.executable, str(Path(__file__).resolve().parents[2] / "apl.py")]


def child_env():
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    env["PYTHONUNBUFFERED"] = "1"
    # `عمار` and `apl` work inside the Terminal app.
    if getattr(sys, "frozen", False):
        env["PATH"] = str(Path(sys.executable).resolve().parent) + os.pathsep + env.get("PATH", "")
    return env


def run_apl(args, timeout=20, cwd=None):
    """Run APL with args. Returns (exit code or None on timeout, output text)."""
    try:
        done = subprocess.run(apl_command() + list(args), stdin=subprocess.DEVNULL,
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              timeout=timeout, cwd=cwd, env=child_env())
    except subprocess.TimeoutExpired as error:
        return None, (error.stdout or b"").decode("utf-8", "replace")
    return done.returncode, done.stdout.decode("utf-8", "replace")

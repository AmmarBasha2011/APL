#!/usr/bin/env python3
"""Start every companion app from a built executable and check that it answers.

    python tools/smoke_apps.py path/to/apl[.exe] [docs-snapshot-folder]

Exit code 0 only when the REPL, Benchmark, Terminal, Docs, Libraries and
Examples all behave. Used by the build workflow on Windows and Linux.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

EXE = os.path.abspath(sys.argv[1])
ENV = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8", BROWSER="true",
           APL_HOME=tempfile.mkdtemp(prefix="aplhome"))
failures = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok else "  " + str(detail)[:300]), flush=True)
    if not ok:
        failures.append(name)


def fetch(url, data=None, cookie=None):
    request = urllib.request.Request(url, data=data, headers={"Cookie": cookie} if cookie else {})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8"), response.headers.get("Set-Cookie")


def start(name):
    proc = subprocess.Popen([EXE, name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            env=ENV, cwd=ENV["APL_HOME"])
    url = None
    deadline = time.time() + 90
    seen = ""
    while time.time() < deadline and url is None:
        line = proc.stdout.readline().decode("utf-8", "replace")
        if not line:
            break
        seen += line
        match = re.search(r"http://127\.0\.0\.1:\d+/\S*", line)
        if match:
            url = match.group(0)
    return proc, url, seen


def stop(proc):
    proc.kill()
    proc.wait()


# REPL: pipe two lines in, expect the answer.
done = subprocess.run([EXE, "repl"], input="اطبع 20 + 22\nخروج\n".encode("utf-8"),
                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=ENV, timeout=60)
check("repl", b"42" in done.stdout, done.stdout.decode("utf-8", "replace"))

# Benchmark.
done = subprocess.run([EXE, "benchmark", "1"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                      env=ENV, timeout=600)
text = done.stdout.decode("utf-8", "replace")
check("benchmark", done.returncode == 0 and "Python" in text, text[-300:])

# Terminal: run a command through the page's own API.
proc, url, seen = start("terminal")
try:
    check("terminal starts", url is not None, seen)
    if url:
        base = url.split("?")[0]
        _, cookie = fetch(url)
        cookie = cookie.split(";")[0]
        started = json.loads(fetch(base + "api/start", json.dumps({"cmd": "echo مرحبا"}).encode(), cookie)[0])
        out = ""
        for _ in range(40):
            part = json.loads(fetch(base + "api/read", json.dumps({"id": started["id"]}).encode(), cookie)[0])
            out += part["out"]
            if part["done"]:
                break
            time.sleep(.25)
        check("terminal runs Arabic", "مرحبا" in out, out)
        apl_out = ""
        started = json.loads(fetch(base + "api/start", json.dumps({"cmd": "apl نسخة"}).encode(), cookie)[0])
        for _ in range(60):
            part = json.loads(fetch(base + "api/read", json.dumps({"id": started["id"]}).encode(), cookie)[0])
            apl_out += part["out"]
            if part["done"]:
                break
            time.sleep(.25)
        check("terminal finds apl", "APL" in apl_out, apl_out)
finally:
    stop(proc)

# Docs and Libraries.
for name in ("docs", "libraries"):
    proc, url, seen = start(name)
    try:
        check(name + " starts", url is not None, seen)
        if url:
            body, _ = fetch(url)
            check(name + " page", "<h1>" in body, body[:200])
            check(name + " offline or synced", "اتصال" in seen or "متصل" in seen, seen)
    finally:
        stop(proc)

# Examples.
proc, url, seen = start("examples")
try:
    check("examples starts", url is not None, seen)
    if url:
        base = url.split("?")[0]
        _, cookie = fetch(url)
        cookie = cookie.split(";")[0]
        data = json.loads(fetch(base + "api/list?q=", cookie=cookie)[0])
        check("examples list", data["total"] > 0, data)
        if data["items"]:
            name = urllib.request.quote(data["items"][0]["file"])
            code, _ = fetch(base + "api/code?f=" + name, cookie=cookie)
            check("examples code", len(code) > 5, code)
finally:
    stop(proc)

print("\n%d failures" % len(failures))
sys.exit(1 if failures else 0)

"""Companion apps: markdown, docs sync, examples safety, terminal, token check."""
import os
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
os.environ["APL_HOME"] = tempfile.mkdtemp(prefix="aplhome")

from core.apps import docs, examples, terminal, web  # noqa: E402

failures = []


def check(name, ok, detail=""):
    if not ok:
        failures.append(name)
        print("FAIL", name, detail)


# git blob hash matches what git itself computes for "hello\n".
check("git sha", docs.git_sha(b"hello\n") == "ce013625030ba8dba906f756967f9e9ca394464a")

# Markdown: heading, code, table, link, list, escaping.
html = web.markdown("# عنوان\n\n```\n<x>\n```\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n- بند\n\n[رابط](https://x.y) و `كود` <script>")
check("md heading", "<h1>عنوان</h1>" in html)
check("md code escaped", "&lt;x&gt;" in html)
check("md table", "<th>a</th>" in html and "<td>2</td>" in html)
check("md list", "<li>بند</li>" in html)
check("md link", '<a href="https://x.y">رابط</a>' in html)
check("md no raw script", "<script>" not in html)

# Docs sync with no network: reports offline, keeps the local copy.
docs.CACHE.mkdir(parents=True, exist_ok=True)
(docs.CACHE / "README.md").write_bytes("# تجربة\n".encode("utf-8"))


def offline(*args, **kwargs):
    raise urllib.error.URLError("offline")


docs._get = offline
result = docs.sync()
check("sync offline", result["online"] is False)
check("copy kept offline", (docs.CACHE / "README.md").is_file())

# Docs sync with a fake repository: only the changed file is fetched.
import json  # noqa: E402
fetched = []
remote = {"README.md": "# تجربة\n".encode("utf-8"), "docs/a.md": b"# a\n"}


def fake(url, timeout=8):
    if "git/trees" in url:
        return json.dumps({"tree": [
            {"path": p, "type": "blob", "sha": docs.git_sha(d)} for p, d in remote.items()
        ] + [{"path": "../evil.md", "type": "blob", "sha": "0" * 40}]}).encode()
    fetched.append(url)
    name = url.split("/main/")[1]
    from urllib.parse import unquote
    return remote[unquote(name)]


docs._get = fake
first = docs.sync()
check("sync fetches only the changed file", first["updated"] == ["docs/a.md"], first)
check("sync ignores escaping path", not (docs.CACHE.parent / "evil.md").exists())
second = docs.sync()
check("second sync fetches nothing", second["updated"] == [] and second["same"] == 2, second)
remote.pop("docs/a.md")
third = docs.sync()
check("sync removes deleted file", third["removed"] == ["docs/a.md"], third)
check("render rejects path escape", docs.render("../x.md") is None)

# Examples: file names are validated.
for bad in ("../x.apl", "a/b.apl", "x.py", "..\\x.apl"):
    check("example name " + bad, examples.code_of(bad) is None)
items = [{"number": "01", "name": "calculator", "file": "01-c.apl", "summary": "آلة حاسبة"}]
check("example search", examples.search(items, "حاسبة") == items and examples.search(items, "zzz") == [])

# Terminal: commands, cd, stdin.
session = terminal.Session()
job = session.start("echo مرحبا")
time.sleep(1.5)
check("terminal echo", "مرحبا" in session.read(job)["out"])
sub = tempfile.mkdtemp()
session.start("cd " + sub)
check("terminal cd", os.path.realpath(session.cwd) == os.path.realpath(sub), session.cwd)
job = session.start('"%s" -c "print(input())"' % sys.executable)
session.send(job, "أهلاً")
out = ""
for _ in range(30):
    part = session.read(job)
    out += part["out"]
    if part["done"]:
        break
    time.sleep(.2)
check("terminal stdin", "أهلاً" in out, out)

# The web server demands its token.
server, url = web.serve(lambda h, m, p, q, b: (200, "text/plain", b"ok"), "t", block=False, quiet=True)
base = url.split("?")[0]
try:
    urllib.request.urlopen(base)
    check("token required", False)
except urllib.error.HTTPError as error:
    check("token required", error.code == 403)
check("token accepted", urllib.request.urlopen(url).status == 200)
server.shutdown()

sys.exit(1 if failures else 0)

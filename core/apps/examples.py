"""APL Examples: browse, copy and run the examples from APL-Examples.

The list comes from the repository's index.json (cached for a day, and used as
it is when offline). An example's code is fetched when you open it and kept in
~/.apl/examples, so the ones you've looked at work offline.
"""
import json
import os
import re
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from core.apps import common, web

REPO = os.environ.get("APL_EXAMPLES_REPO", "AmmarBasha2011/APL-Examples")
BRANCH = "main"
HOME = Path(os.environ.get("APL_HOME", str(Path.home() / ".apl")))
CACHE = HOME / "examples"
SAFE_NAME = re.compile(r"^[\w.\- ]+\.apl$", re.UNICODE)


def _get(url, timeout=20):
    request = urllib.request.Request(url, headers={"User-Agent": "APL-examples"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def index():
    """The example list: fresh when a day old or less, else refetched."""
    cache = HOME / "examples-index.json"
    fresh = cache.is_file() and time.time() - cache.stat().st_mtime < 86400
    if not fresh:
        try:
            data = _get("https://raw.githubusercontent.com/%s/%s/index.json" % (REPO, BRANCH))
            HOME.mkdir(parents=True, exist_ok=True)
            cache.write_bytes(data)
        except (urllib.error.URLError, OSError):
            pass
    if cache.is_file():
        return json.loads(cache.read_text(encoding="utf-8"))
    return []


def code_of(file_name):
    """An example's source, from the cache or the repository."""
    if not SAFE_NAME.match(file_name) or ".." in file_name:
        return None
    target = CACHE / file_name
    if target.is_file():
        return target.read_text(encoding="utf-8")
    try:
        data = _get("https://raw.githubusercontent.com/%s/%s/examples/%s"
                    % (REPO, BRANCH, urllib.parse.quote(file_name)))
    except (urllib.error.URLError, OSError):
        return None
    CACHE.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return data.decode("utf-8")


def search(items, word):
    needle = (word or "").strip().lower()
    if not needle:
        return items
    return [i for i in items if needle in " ".join(
        str(i.get(k) or "") for k in ("number", "name", "file", "summary")).lower()]


SCRIPT = """<script>
const q=document.getElementById('q'),list=document.getElementById('list');
async function load(){const r=await fetch('/api/list?q='+encodeURIComponent(q.value));const d=await r.json();
list.innerHTML=d.items.map(i=>`<div class="row" data-f="${i.file}"><b>${i.number}</b> ${i.summary||i.name}</div>`).join('')+(d.more?`<p class="muted">فيه ${d.more} نتيجة كمان، اكتب بحث أدق.</p>`:'');
document.getElementById('count').textContent=d.total+' مثال';}
q.oninput=()=>{clearTimeout(window.t);window.t=setTimeout(load,200)};
list.onclick=async e=>{const row=e.target.closest('.row');if(!row)return;const f=row.dataset.f;
const r=await fetch('/api/code?f='+encodeURIComponent(f));const t=await r.text();
document.getElementById('name').textContent=f;document.getElementById('code').textContent=t;
document.getElementById('out').textContent='';window.cur=f;document.getElementById('view').hidden=false;};
document.getElementById('copy').onclick=async()=>{await navigator.clipboard.writeText(document.getElementById('code').textContent);
document.getElementById('copy').textContent='اتنسخ ✓';setTimeout(()=>document.getElementById('copy').textContent='نسخ',1500)};
document.getElementById('run').onclick=async()=>{const o=document.getElementById('out');o.textContent='بيشتغل...';
const r=await fetch('/api/run?f='+encodeURIComponent(window.cur),{method:'POST'});o.textContent=await r.text();};
load();</script>"""

BODY = """<style>.row{padding:8px 12px;border:1px solid var(--line);border-radius:10px;margin:6px 0;cursor:pointer}
.row:hover{border-color:var(--g)}#q{width:100%;margin-bottom:10px}.bar{display:flex;gap:10px;align-items:center;margin:10px 0}</style>
<input id="q" placeholder="ابحث في الأمثلة: رقم أو اسم أو وصف"><p class="muted" id="count"></p>
<div id="list"></div>
<div id="view" hidden><hr><div class="bar"><b id="name"></b><button id="copy">نسخ</button><button id="run">شغّل</button></div>
<pre><code id="code"></code></pre><b>الناتج</b><pre><code id="out"></code></pre></div>"""


def run(argv):
    items = index()
    if not items:
        print("مفيش قائمة أمثلة محفوظة ومفيش اتصال بالإنترنت.")
        return 1

    def routes(handler, method, path, query, body):
        if path == "/":
            return 200, "text/html; charset=utf-8", web.page("APL Examples", BODY, "", SCRIPT).encode("utf-8")
        if path == "/api/list":
            found = search(items, (query.get("q") or [""])[0])
            shown = found[:200]
            return 200, "application/json", web.json_bytes(
                {"total": len(found), "more": len(found) - len(shown), "items": shown})
        if path == "/api/code":
            text = code_of((query.get("f") or [""])[0])
            if text is None:
                return 404, "text/plain; charset=utf-8", "تعذر جلب المثال".encode("utf-8")
            return 200, "text/plain; charset=utf-8", text.encode("utf-8")
        if path == "/api/run" and method == "POST":
            name = (query.get("f") or [""])[0]
            text = code_of(name)
            if text is None:
                return 404, "text/plain; charset=utf-8", "تعذر جلب المثال".encode("utf-8")
            with tempfile.TemporaryDirectory() as folder:
                program = Path(folder) / "example.apl"
                program.write_text(text, encoding="utf-8")
                code, output = common.run_apl(["شغل", str(program)], timeout=20, cwd=folder)
            tail = "\n[خلص بعد 20 ثانية: اتوقف]" if code is None else ("" if code == 0 else "\n[كود الخروج %s]" % code)
            return 200, "text/plain; charset=utf-8", (output + tail).encode("utf-8")
        return 404, "text/plain; charset=utf-8", b"not found"

    _, url = web.serve(routes, "APL Examples", block=False)
    web.open_browser(url)
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        pass
    return 0

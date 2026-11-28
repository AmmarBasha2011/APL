"""APL Docs and APL Libraries: the official docs, offline, kept in sync.

The docs live in the APL-Docs repository. The app keeps a copy in
~/.apl/docs. When the machine is online it compares each file's git hash with
the repository's and downloads only the files that changed, so a sync after a
small edit moves one file, not the whole set. Offline it just opens the copy it
has. The Windows/Linux package ships a snapshot to start from, so the very
first run works offline too.
"""
import hashlib
import json
import os
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from core.apps import web

REPO = os.environ.get("APL_DOCS_REPO", "AmmarBasha2011/APL-Docs")
BRANCH = "main"
HOME = Path(os.environ.get("APL_HOME", str(Path.home() / ".apl")))
CACHE = HOME / "docs"
WANTED = ("docs/", "README.md")


def git_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def _wanted(path):
    return path == "README.md" or path.startswith("docs/")


def seed_folder():
    """The snapshot shipped next to the executable (or in a source checkout)."""
    here = Path(sys.executable).resolve().parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parents[2]
    for name in ("APL-Docs", "docs-snapshot"):
        if (here / name).is_dir():
            return here / name
    return None


def prepare_cache():
    """Copy the shipped snapshot in when there is no local copy yet."""
    CACHE.mkdir(parents=True, exist_ok=True)
    if any(CACHE.rglob("*.md")):
        return
    seed = seed_folder()
    if seed:
        shutil.copytree(seed, CACHE, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns(".git", ".github"))


def local_hashes():
    found = {}
    for path in CACHE.rglob("*"):
        if path.is_file():
            rel = path.relative_to(CACHE).as_posix()
            if _wanted(rel):
                found[rel] = git_sha(path.read_bytes())
    return found


def _get(url, timeout):
    request = urllib.request.Request(url, headers={"User-Agent": "APL-docs"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def sync(timeout=8):
    """Download only what differs from the repository. Returns a result dict.

    {'online': False} when the repository can't be reached, which is fine: the
    local copy is used as it is.
    """
    api = "https://api.github.com/repos/%s/git/trees/%s?recursive=1" % (REPO, BRANCH)
    try:
        tree = json.loads(_get(api, timeout).decode("utf-8"))["tree"]
    except (urllib.error.URLError, OSError, ValueError, KeyError):
        return {"online": False, "updated": [], "removed": [], "same": 0}
    remote = {t["path"]: t["sha"] for t in tree if t.get("type") == "blob" and _wanted(t["path"])}
    have = local_hashes()
    updated, removed = [], []
    for path, sha in sorted(remote.items()):
        if have.get(path) == sha:
            continue
        # Never let a path from the network leave the cache folder.
        target = (CACHE / path).resolve()
        if CACHE.resolve() not in target.parents:
            continue
        try:
            data = _get("https://raw.githubusercontent.com/%s/%s/%s"
                        % (REPO, BRANCH, urllib.parse.quote(path)), timeout)
        except (urllib.error.URLError, OSError):
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        updated.append(path)
    for path in sorted(set(have) - set(remote)):
        try:
            (CACHE / path).unlink()
            removed.append(path)
        except OSError:
            pass
    return {"online": True, "updated": updated, "removed": removed,
            "same": len(remote) - len(updated)}


def pages():
    """[(title, relative path)] for every Markdown page, README first."""
    items = []
    for path in sorted(CACHE.rglob("*.md")):
        rel = path.relative_to(CACHE).as_posix()
        if rel == "README.md":
            items.insert(0, ("الرئيسية", rel))
        else:
            items.append((path.stem, rel))
    return items


def render(rel):
    target = (CACHE / rel).resolve()
    if CACHE.resolve() not in target.parents and target != CACHE.resolve():
        return None
    if not target.is_file() or target.suffix != ".md":
        return None
    text = target.read_text(encoding="utf-8")

    def rewrite(body):
        # Relative links between pages stay inside the app.
        def fix(m):
            href = m.group(1)
            if href.startswith(("http://", "https://", "#", "mailto:")):
                return m.group(0)
            return 'href="/doc/%s"' % urllib.parse.quote(
                (Path(rel).parent / href).as_posix().lstrip("./") if not href.startswith("/") else href)
        import re
        return re.sub(r'href="([^"]+)"', fix, body)

    return web.markdown(text, rewrite)


def run(argv, libraries=False):
    prepare_cache()
    status = sync()
    if status["online"]:
        print("متصل: %d ملف اتحدّث، %d اتشال، %d زي ما هو."
              % (len(status["updated"]), len(status["removed"]), status["same"]))
        for path in status["updated"]:
            print("  تحديث:", path)
    else:
        print("مفيش اتصال: هنفتح النسخة الموجودة على الجهاز.")
    if not any(CACHE.rglob("*.md")):
        print("مفيش نسخة محلية من التوثيق ومفيش نت. اتصل بالإنترنت مرة واحدة.")
        return 1

    def routes(handler, method, path, query, body):
        if path in ("/", ""):
            items = pages()
            first = next((r for t, r in items if "مكتب" in t), items[0][1]) if libraries else items[0][1]
            return (200, "text/html; charset=utf-8",
                                      _shell(first, items, status).encode("utf-8"))
        if path.startswith("/doc/"):
            rel = path[len("/doc/"):]
            if render(rel) is None:
                return 404, "text/plain; charset=utf-8", "الصفحة مش موجودة".encode("utf-8")
            return 200, "text/html; charset=utf-8", _shell(rel, pages(), status).encode("utf-8")
        return 404, "text/plain; charset=utf-8", b"not found"

    server, url = web.serve(routes, "APL Libraries" if libraries else "APL Docs", block=False)
    web.open_browser(url)
    try:
        import time
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        pass
    return 0


def _shell(rel, items, status):
    nav = "".join('<a href="/doc/%s">%s</a>' % (urllib.parse.quote(r), t) for t, r in items)
    note = ("آخر مزامنة: %d ملف اتحدّث" % len(status["updated"])) if status["online"] \
        else "بدون إنترنت: النسخة المحفوظة على جهازك"
    body = render(rel) + '<p class="muted">%s</p>' % note
    return web.page("APL Docs", body, nav)

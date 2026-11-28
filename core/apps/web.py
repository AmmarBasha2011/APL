"""A tiny local web app server shared by the companion apps.

It listens on 127.0.0.1 only, picks a free port, and demands a random token on
every request, so no other page or program on the machine can drive it. The
Terminal app runs commands, so that check matters.
"""
import html
import json
import re
import secrets
import threading
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<style>
:root{{--bg:#07130e;--card:#0e241c;--ink:#eaf6f0;--muted:#8fb0a2;--g:#3ddc97;--line:rgba(255,255,255,.12)}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.8 "Segoe UI","Noto Naskh Arabic",Tahoma,sans-serif}}
a{{color:var(--g)}}header{{display:flex;gap:18px;align-items:center;padding:12px 22px;border-bottom:1px solid var(--line);background:var(--card);position:sticky;top:0;z-index:5}}
header b{{font-size:1.2rem}}header a{{text-decoration:none;color:var(--muted)}}header a:hover{{color:var(--g)}}
main{{max-width:980px;margin:0 auto;padding:24px 22px 80px}}
pre,code{{direction:ltr;unicode-bidi:plaintext;text-align:left;font-family:Consolas,"Cascadia Code",monospace}}
pre{{background:#050d0a;border:1px solid var(--line);border-radius:12px;padding:14px;overflow:auto}}
code{{background:rgba(255,255,255,.08);padding:1px 6px;border-radius:6px}}pre code{{background:none;padding:0}}
table{{border-collapse:collapse;width:100%;margin:14px 0}}td,th{{border:1px solid var(--line);padding:8px 10px;text-align:start}}th{{background:var(--card)}}
button,input,select{{font:inherit;background:var(--card);color:var(--ink);border:1px solid var(--line);border-radius:10px;padding:8px 14px}}
button{{cursor:pointer;background:var(--g);color:#04150e;font-weight:700;border:0}}button.g{{background:var(--card);color:var(--ink);border:1px solid var(--line)}}
.muted{{color:var(--muted)}}
</style></head><body><header><b>{title}</b>{nav}</header><main>{body}</main>{script}</body></html>"""


def page(title, body, nav="", script=""):
    return PAGE.format(title=html.escape(title), body=body, nav=nav, script=script)


def _inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  lambda m: '<a href="%s">%s</a>' % (m.group(2).replace('"', '%22'), m.group(1)), text)
    return text


def markdown(source, link_rewrite=None):
    """Enough Markdown for the docs: headings, code, lists, tables, links."""
    out, lines, i, in_list = [], source.replace("\r\n", "\n").split("\n"), 0, False

    def close():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            close()
            i += 1
            block = []
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(lines[i])
                i += 1
            out.append("<pre><code>%s</code></pre>" % html.escape("\n".join(block)))
        elif re.match(r"^#{1,6} ", line):
            close()
            n = len(line) - len(line.lstrip("#"))
            out.append("<h%d>%s</h%d>" % (n, _inline(line[n:].strip()), n))
        elif line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?\s*$", lines[i + 1]):
            close()
            rows = [line]
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            i -= 1
            def cells(r):
                return [c.strip() for c in r.strip().strip("|").split("|")]
            out.append("<table><tr>%s</tr>" % "".join("<th>%s</th>" % _inline(c) for c in cells(rows[0])))
            for r in rows[1:]:
                out.append("<tr>%s</tr>" % "".join("<td>%s</td>" % _inline(c) for c in cells(r)))
            out.append("</table>")
        elif re.match(r"^\s*[-*] ", line):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>%s</li>" % _inline(re.sub(r"^\s*[-*] ", "", line)))
        elif not line.strip():
            close()
        else:
            close()
            out.append("<p>%s</p>" % _inline(line))
        i += 1
    close()
    body = "\n".join(out)
    if link_rewrite:
        body = link_rewrite(body)
    return body


def serve(routes, title, open_path="/", port=0, block=True, quiet=False):
    """Run `routes(handler, method, path, query, body) -> (status, type, bytes)`.

    Returns (server, url). With block=False the server runs in a thread.
    """
    token = secrets.token_urlsafe(16)

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def _go(self, method):
            host = (self.headers.get("Host") or "").split(":")[0]
            if host not in ("127.0.0.1", "localhost"):
                return self._send(403, "text/plain", b"forbidden")
            parsed = urllib.parse.urlparse(self.path)
            query = urllib.parse.parse_qs(parsed.query)
            cookie = self.headers.get("Cookie") or ""
            given = (query.get("t") or [""])[0]
            if given == token:
                pass
            elif ("apl_t=" + token) not in cookie:
                return self._send(403, "text/plain", b"forbidden")
            length = int(self.headers.get("Content-Length") or 0)
            body = self.rfile.read(length) if length else b""
            try:
                status, ctype, data = routes(self, method, urllib.parse.unquote(parsed.path), query, body)
            except Exception as error:  # a broken page must not kill the app
                status, ctype, data = 500, "text/plain; charset=utf-8", ("خطأ: %s" % error).encode("utf-8")
            self._send(status, ctype, data, cookie=(given == token))

        def _send(self, status, ctype, data, cookie=False):
            self.send_response(status)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            if cookie:
                self.send_header("Set-Cookie", "apl_t=%s; Path=/; HttpOnly; SameSite=Strict" % token)
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            self._go("GET")

        def do_POST(self):
            self._go("POST")

    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.daemon_threads = True
    url = "http://127.0.0.1:%d%s?t=%s" % (server.server_address[1], open_path, token)
    if not quiet:
        print("%s شغّال على: %s" % (title, url), flush=True)
        print("اضغط Ctrl+C للإغلاق.", flush=True)
    if block:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    else:
        threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, url


def open_browser(url):
    try:
        webbrowser.open(url)
    except Exception:
        pass


def json_bytes(obj):
    return json.dumps(obj, ensure_ascii=False).encode("utf-8")

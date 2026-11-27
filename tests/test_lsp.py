"""Drive the APL language server over its protocol and check what it answers.

The server is a separate process speaking LSP on stdin/stdout, so this test
talks to it the way an editor would: framed JSON-RPC, no shortcuts into its
internals.

Usage:  python tests/test_lsp.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVER = ROOT / "editors" / "lsp" / "apl_lsp.py"

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")


class Client:
    def __init__(self):
        env = dict(os.environ, PYTHONIOENCODING="utf-8", APL_HOME=str(ROOT))
        self.proc = subprocess.Popen(
            [sys.executable, str(SERVER)],
            cwd=str(ROOT), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, env=env,
        )
        self.next_id = 0

    def send(self, method, params=None, request=True):
        self.next_id += 1
        message = {"jsonrpc": "2.0", "method": method, "params": params or {}}
        if request:
            message["id"] = self.next_id
        body = json.dumps(message, ensure_ascii=False).encode("utf-8")
        self.proc.stdin.write(b"Content-Length: " + str(len(body)).encode() + b"\r\n\r\n" + body)
        self.proc.stdin.flush()
        if not request:
            return None
        return self.wait()

    def wait(self):
        """Read messages until a response (one with an id) arrives."""
        while True:
            headers = {}
            while True:
                line = self.proc.stdout.readline()
                if not line:
                    raise RuntimeError("server closed: " + self.proc.stderr.read().decode("utf-8", "replace"))
                line = line.strip()
                if not line:
                    break
                key, _, value = line.decode().partition(":")
                headers[key.strip().lower()] = value.strip()
            body = self.proc.stdout.read(int(headers["content-length"]))
            message = json.loads(body.decode("utf-8"))
            if "id" in message:
                return message

    def notify_and_diagnostics(self, uri, text):
        self.send("textDocument/didOpen", {
            "textDocument": {"uri": uri, "languageId": "apl", "version": 1, "text": text},
        }, request=False)
        # The next framed message is the publishDiagnostics notification.
        while True:
            headers = {}
            while True:
                line = self.proc.stdout.readline()
                if not line:
                    raise RuntimeError("no diagnostics")
                line = line.strip()
                if not line:
                    break
                key, _, value = line.decode().partition(":")
                headers[key.strip().lower()] = value.strip()
            message = json.loads(self.proc.stdout.read(int(headers["content-length"])).decode("utf-8"))
            if message.get("method") == "textDocument/publishDiagnostics":
                return message["params"]["diagnostics"]

    def close(self):
        try:
            self.send("shutdown")
            self.send("exit", request=False)
        except Exception:
            pass
        try:
            self.proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            self.proc.kill()


FAILURES = []
CHECKS = []


def check(name, condition, detail=""):
    CHECKS.append(name)
    if condition:
        print("PASS  " + name)
    else:
        FAILURES.append(name)
        print("FAIL  " + name + ("\n" + detail if detail else ""))


def main() -> int:
    client = Client()
    try:
        response = client.send("initialize", {"rootUri": "file://" + str(ROOT)})
        caps = (response.get("result") or {}).get("capabilities") or {}
        check("initialize advertises diagnostics, completion and hover",
              caps.get("textDocumentSync") == 1 and caps.get("completionProvider")
              and caps.get("hoverProvider"), json.dumps(caps, ensure_ascii=False))
        client.send("initialized", {}, request=False)

        broken = 'لو س = 5:\n    اطبع("خمسة"\n'
        diagnostics = client.notify_and_diagnostics("file:///tmp/broken.apl", broken)
        errors = [d for d in diagnostics if d["severity"] == 1]
        check("a broken file gets one compiler error", len(errors) == 1, json.dumps(diagnostics, ensure_ascii=False))
        if errors:
            check("the error points at the opening line", errors[0]["range"]["start"]["line"] == 0,
                  json.dumps(errors[0], ensure_ascii=False))
            check("the error message is in Arabic", "خطأ" in errors[0]["message"] or "Error" in errors[0]["message"],
                  errors[0]["message"])

        linted = 'لو س = 5:\n    اطبع(س)\t\n# TODO لسه\n'
        diagnostics = client.notify_and_diagnostics("file:///tmp/linted.apl", linted)
        warnings = [d for d in diagnostics if d["severity"] == 2]
        messages = " ".join(d["message"] for d in warnings)
        check("lint reports the tab", "تاب" in messages, messages)
        check("lint reports trailing space", "مسافات" in messages, messages)
        check("lint reports '=' in a condition", '"=="' in messages or "==" in messages, messages)
        check("lint reports the TODO", "TODO" in messages, messages)

        good = 'دالة ضعف(س):\n    ارجع س * 2\n\nاطبع(ضعف(4))\n'
        diagnostics = client.notify_and_diagnostics("file:///tmp/good.apl", good)
        check("a clean file has no diagnostics", diagnostics == [], json.dumps(diagnostics, ensure_ascii=False))

        uri = "file:///tmp/good.apl"
        completion = client.send("textDocument/completion", {
            "textDocument": {"uri": uri}, "position": {"line": 3, "character": 8},
        })
        labels = [item["label"] for item in (completion.get("result") or {}).get("items", [])]
        check("completion offers language words", "اطبع" in labels, str(labels[:10]))
        check("completion offers the file's own function", "ضعف" in labels, str(labels[:10]))
        check("completion offers library names", "numpy" in labels, str([l for l in labels if l.isascii()][:10]))

        hover = client.send("textDocument/hover", {
            "textDocument": {"uri": uri}, "position": {"line": 3, "character": 2},
        })
        value = ((hover.get("result") or {}).get("contents") or {}).get("value", "")
        check("hover explains اطبع", "اطبع" in value, value)

        symbols = client.send("textDocument/documentSymbol", {"textDocument": {"uri": uri}})
        names = [item["name"] for item in (symbols.get("result") or [])]
        check("outline lists the function", names == ["ضعف"], str(names))
    finally:
        client.close()

    print()
    total = len(CHECKS)
    print(f"{total - len(FAILURES)}/{total} lsp checks passed")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

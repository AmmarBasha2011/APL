#!/usr/bin/env python3
"""Language server for APL (لغة عمار).

Standard library only: it speaks LSP over stdin/stdout with Content-Length
framing, so any editor that can start a language server can use it (Neovim,
Emacs/eglot, VS Code, Kate, ...). It gives you:

  * diagnostics from the real compiler, not a lookalike: every save runs the
    same transpile+compile step as `عمار فحص`, so what the server reports is
    what the interpreter would say;
  * the cheap lint notes `عمار فحص` prints (tabs, trailing spaces, `=` inside a
    condition, leftover TODOs) as warnings;
  * completion for language words, built-in function names, library names and
    the functions/classes defined in the file you are editing;
  * hover text for every word in that catalog;
  * a document outline of the functions and classes in the file.

The server never executes a program. Compilation only.

Run it from the repository root:

    python editors/lsp/apl_lsp.py

or point APL_HOME at the checkout:

    APL_HOME=/path/to/APL python /path/to/APL/editors/lsp/apl_lsp.py
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# Protocol plumbing
# --------------------------------------------------------------------------

# The interpreter's import chain reconfigures sys.stdout and the libraries may
# print while loading. Our protocol writer keeps its own handle on the original
# byte stream so nothing can slip into the middle of a message.
_OUT = sys.stdout.buffer


def _read_message(stream):
    """Read one LSP message; None on end of input."""
    length = None
    while True:
        line = stream.readline()
        if not line:
            return None
        line = line.strip()
        if not line:
            break
        if line.lower().startswith(b"content-length:"):
            length = int(line.split(b":", 1)[1].strip())
    if length is None:
        return None
    body = stream.read(length)
    if not body:
        return None
    return json.loads(body.decode("utf-8"))


def _write(payload: dict) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    _OUT.write(b"Content-Length: " + str(len(body)).encode("ascii") + b"\r\n\r\n")
    _OUT.write(body)
    _OUT.flush()


def _result(request_id, value) -> None:
    _write({"jsonrpc": "2.0", "id": request_id, "result": value})


def _notify(method: str, params: dict) -> None:
    _write({"jsonrpc": "2.0", "method": method, "params": params})


# --------------------------------------------------------------------------
# Repository access (the compiler lives in the checkout this file ships in)
# --------------------------------------------------------------------------

ROOT = Path(os.environ.get("APL_HOME") or Path(__file__).resolve().parents[2])
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

_ARABIC_WORD = re.compile(r"[^\W\d]\w*", re.UNICODE)


def _quiet():
    """Silence anything the interpreter prints while we import or compile."""

    class _Sink:
        def write(self, *_args, **_kwargs):
            return 0

        def flush(self):
            pass

        def isatty(self):
            return False

        def reconfigure(self, *_args, **_kwargs):
            pass

        encoding = "utf-8"

    class _Ctx:
        def __enter__(self):
            self._saved = sys.stdout
            sys.stdout = _Sink()
            return self

        def __exit__(self, *_exc):
            sys.stdout = self._saved
            return False

    return _Ctx()


def _compiler():
    from core.runner.execution import Compilation  # noqa: F401  (import probe)

    return Compilation


def _error_text(error) -> str:
    """The Arabic explanation the interpreter itself would print."""
    try:
        from core.runner.main import _get_error_ar

        return _get_error_ar(error)
    except Exception:
        return str(error)


# --------------------------------------------------------------------------
# Diagnostics: compile, then the cheap lint pass
# --------------------------------------------------------------------------

_LINT_TODO = re.compile(r"TODO", re.IGNORECASE)


def lint_notes(text: str):
    """Same checks as `عمار فحص`, as (line_index, message) with 0-based lines."""
    notes = []
    for number, line in enumerate(text.split("\n")):
        if "\t" in line:
            notes.append((number, "فيه تاب، استخدم مسافات"))
        if line.rstrip() != line:
            notes.append((number, "مسافات زيادة في آخر السطر"))
        stripped = line.strip()
        if stripped.startswith("لو ") and re.search(r"(?<![=!<>])=(?!=)", stripped):
            notes.append((number, '"=" جوه شرط، يمكن تقصد "=="'))
        if stripped.startswith("#") and _LINT_TODO.search(stripped):
            notes.append((number, "TODO لسه موجود"))
    return notes


def diagnose(text: str, path: str):
    """Return LSP diagnostics for one document."""
    diagnostics = []
    line_count = max(1, len(text.split("\n")))

    for line, message in lint_notes(text):
        diagnostics.append({
            "range": {
                "start": {"line": line, "character": 0},
                "end": {"line": line, "character": 0},
            },
            "severity": 2,  # Warning
            "source": "عمار",
            "message": message,
        })

    with _quiet():
        try:
            Compilation = _compiler()
            Compilation(text, path)
        except SyntaxError as error:
            line = max(0, (error.lineno or 1) - 1)
            column = max(0, (error.offset or 1) - 1)
            diagnostics.append({
                "range": {
                    "start": {"line": line, "character": column},
                    "end": {"line": line, "character": column + 1},
                },
                "severity": 1,  # Error
                "source": "عمار",
                "message": _error_text(error),
            })
        except Exception as error:  # the transpiler itself blew up
            diagnostics.append({
                "range": {
                    "start": {"line": 0, "character": 0},
                    "end": {"line": line_count - 1, "character": 0},
                },
                "severity": 1,
                "source": "عمار",
                "message": f"{type(error).__name__}: {_error_text(error)}",
            })
    return diagnostics


# --------------------------------------------------------------------------
# Catalog: language words, built-ins and library names
# --------------------------------------------------------------------------

KEYWORDS = {
    "اطبع": "يطبع على الشاشة",
    "اطبع_بدون": "يطبع بدون سطر جديد",
    "لو": "شرط: لو الشرط صح ينفّذ اللي بعده",
    "إذا": "شرط (نفس لو)",
    "والا": "الفرع البديل للشرط",
    "والا_لو": "شرط تاني بعد والا",
    "الا": "الفرع البديل للشرط",
    "الا_لو": "شرط تاني بعد الا",
    "لكل": "حلقة على عناصر: لكل ع في القائمة",
    "طالما": "حلقة بتتكرر طالما الشرط صح",
    "ارجع": "إرجاع قيمة من الدالة",
    "توقف": "الخروج من الحلقة",
    "اكمل": "تخطي الدورة الحالية",
    "دالة": "تعريف دالة",
    "صنف": "تعريف صنف",
    "دالة_إنشاء": "دالة إنشاء الكائن (constructor)",
    "ذات": "الكائن نفسه (self)",
    "استورد": "استيراد ملف أو مكتبة",
    "من": "استيراد جزء محدد: من X استورد Y",
    "حاول": "بداية معالجة الأخطاء",
    "امسك": "التقاط الخطأ: امسك مثل خطأ",
    "أخيراً": "كود بيتنفّذ في كل الحالات",
    "في": "داخل الحلقة أو البحث",
    "و": "و المنطقية",
    "أو": "أو المنطقية",
    "ليس": "نفي منطقي",
    "صواب": "True",
    "خطأ": "False",
    "لا_شيء": "None",
    "قيمة": "مطابقة قيمة (match)",
    "اقرأ": "قراءة ملف",
    "اكتب": "كتابة ملف",
    "ادخل": "قراءة إدخال من المستخدم",
    "طول": "عدد عناصر شيء",
    "مدى": "نطاق أرقام: مدى(10)",
    "مجموع": "مجموع العناصر",
    "أقصى": "أكبر عنصر",
    "أدنى": "أصغر عنصر",
    "جذر": "الجزر التربيعي",
    "مطلق": "القيمة المطلقة",
    "دائري": "تقريب الرقم",
    "ترتيب": "ترتيب العناصر",
    "عشوائي": "رقم عشوائي",
    "نوع": "نوع القيمة",
    "نص": "تحويل إلى نص",
    "عدد": "تحويل إلى عدد صحيح",
    "عشري": "تحويل إلى عدد عشري",
    "قائمة": "تحويل إلى قائمة",
}

LIBRARY_NAMES_CACHE = None


def library_names():
    """The published library names, from the index shipped in the repo."""
    global LIBRARY_NAMES_CACHE
    if LIBRARY_NAMES_CACHE is None:
        LIBRARY_NAMES_CACHE = []
        index = ROOT / "data" / "libraries.json"
        try:
            data = json.loads(index.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            data = []
        if isinstance(data, dict):
            data = data.get("libraries", [])
        for entry in data:
            if isinstance(entry, dict) and entry.get("name"):
                LIBRARY_NAMES_CACHE.append((entry["name"], entry.get("title", "")))
    return LIBRARY_NAMES_CACHE


_DEF_FUNC = re.compile(r"^\s*دالة\s+([^\s(:]+)\s*\(")
_DEF_FUNC_PY = re.compile(r"^\s*(?:async\s+)?def\s+([^\s(:]+)\s*\(")
_DEF_CLASS = re.compile(r"^\s*صنف\s+([^\s(:]+)")
_DEF_CLASS_PY = re.compile(r"^\s*class\s+([^\s(:]+)")


def local_symbols(text: str):
    """Functions and classes defined in this document."""
    found = []
    for number, line in enumerate(text.split("\n")):
        for pattern, kind in ((_DEF_FUNC, 12), (_DEF_FUNC_PY, 12),
                              (_DEF_CLASS, 5), (_DEF_CLASS_PY, 5)):
            match = pattern.match(line)
            if match:
                name = match.group(1)
                if name in ("__init__",) or name.startswith("_"):
                    continue
                found.append((name, kind, number, line))
                break
    return found


def _word_at(text: str, line: int, character: int):
    lines = text.split("\n")
    if not 0 <= line < len(lines):
        return ""
    current = lines[line]
    start = min(character, len(current))
    while start > 0 and (current[start - 1].isalnum() or current[start - 1] == "_"):
        start -= 1
    end = min(character, len(current))
    while end < len(current) and (current[end].isalnum() or current[end] == "_"):
        end += 1
    return current[start:end]


# --------------------------------------------------------------------------
# Server state
# --------------------------------------------------------------------------


class Server:
    def __init__(self):
        self.documents = {}  # uri -> text
        self.root_uri = None
        self.shutdown = False

    # -- diagnostics -------------------------------------------------------
    def publish(self, uri: str) -> None:
        text = self.documents.get(uri)
        if text is None:
            return
        path = uri[len("file://"):] if uri.startswith("file://") else uri
        path = path.replace("%20", " ")
        _notify("textDocument/publishDiagnostics", {
            "uri": uri,
            "diagnostics": diagnose(text, path),
        })

    # -- requests ----------------------------------------------------------
    def initialize(self, params):
        self.root_uri = params.get("rootUri")
        return {
            "capabilities": {
                "textDocumentSync": 1,  # full text on every change
                "completionProvider": {"resolveProvider": False,
                                       "triggerCharacters": [" ", ".", "م"]},
                "hoverProvider": True,
                "documentSymbolProvider": True,
            },
            "serverInfo": {"name": "apl-lsp", "version": "1.0"},
        }

    def completion(self, params):
        uri = params["textDocument"]["uri"]
        text = self.documents.get(uri, "")
        items = []
        for name, doc in KEYWORDS.items():
            items.append({
                "label": name,
                "kind": 14,  # Keyword
                "detail": "كلمة في اللغة",
                "documentation": doc,
            })
        for name, kind, _line, source in local_symbols(text):
            items.append({
                "label": name,
                "kind": kind,  # Function / Class
                "detail": "معرّف في الملف",
                "documentation": source.strip(),
            })
        for name, title in library_names():
            items.append({
                "label": name,
                "kind": 9,  # Module
                "detail": "مكتبة",
                "documentation": (title or name) + f"\nعمار مكتبة تحميل {name}",
            })
        return {"isIncomplete": False, "items": items}

    def hover(self, params):
        uri = params["textDocument"]["uri"]
        position = params["position"]
        text = self.documents.get(uri, "")
        word = _word_at(text, position["line"], position["character"])
        if not word:
            return None
        if word in KEYWORDS:
            body = KEYWORDS[word]
        else:
            body = ""
            for name, _kind, _line, source in local_symbols(text):
                if name == word:
                    body = "معرّف في الملف\n\n    " + source.strip()
                    break
        if not body:
            return None
        return {
            "contents": {"kind": "markdown", "value": f"**{word}**\n\n{body}"},
            "range": {
                "start": {"line": position["line"], "character": position["character"]},
                "end": {"line": position["line"], "character": position["character"] + len(word)},
            },
        }

    def symbols(self, params):
        uri = params["textDocument"]["uri"]
        text = self.documents.get(uri, "")
        out = []
        for name, kind, line, _source in local_symbols(text):
            out.append({
                "name": name,
                "kind": kind,
                "location": {
                    "uri": uri,
                    "range": {
                        "start": {"line": line, "character": 0},
                        "end": {"line": line, "character": 0},
                    },
                },
            })
        return out

    # -- dispatch ----------------------------------------------------------
    def handle(self, message) -> bool:
        """Handle one message; False means 'exit'."""
        method = message.get("method")
        request_id = message.get("id")
        params = message.get("params") or {}

        if method == "initialize":
            _result(request_id, self.initialize(params))
        elif method == "initialized":
            pass
        elif method == "shutdown":
            self.shutdown = True
            _result(request_id, None)
        elif method == "exit":
            return False
        elif method == "textDocument/didOpen":
            doc = params["textDocument"]
            self.documents[doc["uri"]] = doc["text"]
            self.publish(doc["uri"])
        elif method == "textDocument/didChange":
            uri = params["textDocument"]["uri"]
            changes = params.get("contentChanges") or []
            if changes:
                self.documents[uri] = changes[-1]["text"]
            self.publish(uri)
        elif method == "textDocument/didSave":
            self.publish(params["textDocument"]["uri"])
        elif method == "textDocument/didClose":
            uri = params["textDocument"]["uri"]
            self.documents.pop(uri, None)
            _notify("textDocument/publishDiagnostics", {"uri": uri, "diagnostics": []})
        elif method == "textDocument/completion":
            _result(request_id, self.completion(params))
        elif method == "textDocument/hover":
            _result(request_id, self.hover(params))
        elif method == "textDocument/documentSymbol":
            _result(request_id, self.symbols(params))
        elif request_id is not None:
            # Unknown request: answer null so the client does not hang.
            _result(request_id, None)
        return True


def main() -> int:
    server = Server()
    stream = sys.stdin.buffer
    while True:
        message = _read_message(stream)
        if message is None:
            return 0
        if not server.handle(message):
            return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Regenerate playground/manifest.json.

The playground page runs APL in the browser: it downloads the interpreter's
Python files, writes them into the browser's filesystem and imports them. That
needs a list of files, and a hand-written list rots the first time a module is
added or renamed, so the page reads this generated manifest instead.

    python tools/build_playground.py          # write the manifest
    python tools/build_playground.py --check  # fail if it is stale
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "playground" / "manifest.json"
SOURCES = ROOT / "core"


def source_files() -> list[Path]:
    return sorted(path for path in SOURCES.rglob("*.py") if "__pycache__" not in path.parts)


def build() -> dict:
    files = []
    digest = hashlib.sha256()
    for path in source_files():
        relative = path.relative_to(ROOT).as_posix()
        # Line endings must not change the manifest: git checks the same file
        # out with CRLF on Windows and LF everywhere else, and a manifest that
        # differs per platform fails the Windows job for no real reason.
        data = path.read_bytes().replace(b"\r\n", b"\n")
        digest.update(relative.encode("utf-8"))
        digest.update(data)
        files.append({"path": relative, "bytes": len(data)})
    return {
        "version": 1,
        "files": files,
        "total_bytes": sum(item["bytes"] for item in files),
        "sha256": digest.hexdigest(),
    }


def main(argv: list[str]) -> int:
    manifest = build()
    text = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    if "--check" in argv:
        current = MANIFEST.read_text(encoding="utf-8") if MANIFEST.is_file() else ""
        if current != text:
            print("playground/manifest.json is stale; run python tools/build_playground.py")
            return 1
        print(f"playground/manifest.json is current ({len(manifest['files'])} files)")
        return 0
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(text, encoding="utf-8")
    print(f"wrote playground/manifest.json: {len(manifest['files'])} files, "
          f"{manifest['total_bytes']} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

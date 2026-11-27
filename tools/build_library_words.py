#!/usr/bin/env python3
"""Regenerate data/library_words.json: which library provides which word.

When a program uses a word from a library that is not installed, the compiler
only sees an unknown name. The libraries themselves know their vocabulary, so
this tool collects every published library's word tables into one small map,
and the error message can then say which library the word belongs to and how
to install it.

Point it at folders holding `<name>_funcs.py` files (a checkout of the library
repos, or the old bundled sources):

    python tools/build_library_words.py /path/to/libraries /another/folder
"""
from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data" / "library_words.json"
SUFFIXES = ("FUNCS", "CONSTANTS", "CONSTS", "METHODS", "PROPS")
# Only plain Arabic words are worth a suggestion. The published libraries also
# carry tens of thousands of transliterated names ("ABC_إنشاء_tcp_مُستمع") for
# Python's own API; they say nothing a user would type, and they would turn a
# 50 KB file into 15 MB.
ARABIC_WORD = re.compile(r"^[\u0600-\u06FF][\u0600-\u06FF\s]*$")


def words_in(path: Path) -> dict[str, str]:
    """Word → library name for one library's source file."""
    library = path.stem[: -len("_funcs")]
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError):
        return {}
    found = {}
    for node in tree.body:
        if not (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)):
            continue
        name = node.targets[0].id
        if not isinstance(node.value, ast.Dict) or not name.endswith(SUFFIXES):
            continue
        try:
            table = ast.literal_eval(node.value)
        except (ValueError, SyntaxError):
            continue
        if isinstance(table, dict):
            for word in table:
                if (isinstance(word, str) and 1 < len(word.strip()) <= 20
                        and ARABIC_WORD.match(word.strip())):
                    found.setdefault(word.strip(), library)
    return found


def collect(folders) -> dict[str, str]:
    table: dict[str, str] = {}
    for folder in folders:
        for path in sorted(Path(folder).glob("*_funcs.py")):
            for word, library in words_in(path).items():
                table.setdefault(word, library)
    return table


def main(argv: list[str]) -> int:
    folders = argv or [ROOT / "core" / "libraries"]
    table = collect(folders)
    if not table:
        print("no library words found in: " + ", ".join(str(f) for f in folders))
        return 1
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(json.dumps(table, ensure_ascii=False, indent=0, sort_keys=True) + "\n",
                      encoding="utf-8")
    libraries = len(set(table.values()))
    print(f"wrote {TARGET.relative_to(ROOT)}: {len(table)} words from {libraries} libraries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

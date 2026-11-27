"""Check how `عمار مثال قائمة` and `عمار مثال بحث` present the examples.

The examples repository is thousands of examples, so the list has to be a page
with a way to narrow it, not a wall of text. The index is replaced with a fake
one here, so the suite needs no network.

Usage:  python tests/test_examples_list.py
"""
from __future__ import annotations

import io
import sys
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

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
    import core.cli as cli

    items = [{"number": f"{number:03d}", "name": f"example-{number}",
              "file": f"{number:03d}-example.apl",
              "summary": f"مثال {number}" + (" مصفوفة" if number % 7 == 0 else "")}
             for number in range(1, 201)]
    cli._examples_index = lambda force=False: items

    def run(*args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = cli._example(list(args))
        return code, out.getvalue(), err.getvalue()

    code, out, _ = run("قائمة")
    lines = out.splitlines()
    check("the list is a page, not the whole repository",
          len(lines) < 50 and "200" in lines[0], out[:200])
    check("it says how many are left and how to see them",
          "وفيه 160 كمان" in out and "--الكل" in out, out[-200:])

    code, out, _ = run("قائمة", "--الكل")
    check("--الكل prints every example", len(out.splitlines()) >= 201, str(len(out.splitlines())))

    code, out, _ = run("بحث", "مصفوفة")
    check("search finds the matching examples", code == 0 and "أمثلة فيها" in out, out[:200])
    check("search shows only matches", "مثال 7" in out and "مثال 8 " not in out, out[:300])

    code, out, err = run("بحث", "ززززز")
    check("a search with no match fails clearly", code == 1 and "مفيش مثال" in err, err)

    code, out, err = run("بحث")
    check("search without a word asks for one", code == 1 and "الكلمة" in err, err)

    check("the search helper ignores an empty word", cli._search_examples(items, "  ") == [])

    print()
    total = len(CHECKS)
    print(f"{total - len(FAILURES)}/{total} example list checks passed")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

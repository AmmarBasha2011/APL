"""The verifier's spread-out sample.

A sample that only takes the first N programs says nothing about the rest of
the folder, which is what CI needs to check.

Usage:  python tests/test_verifier.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from verify_examples import classify, report, spread  # noqa: E402

failures = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global failures
    if condition:
        print("PASS  " + name)
    else:
        failures += 1
        print("FAIL  " + name + ("  " + detail if detail else ""))


items = [f"{i:04d}-x.apl" for i in range(1, 121)]

same = spread(items, 120)
check("a sample as big as the folder is the whole folder", same == items)

bigger = spread(items, 500)
check("a sample bigger than the folder stays the whole folder", bigger == items)

none = spread(items, 0)
check("a sample of zero is empty", none == [], repr(none))

one = spread(items, 1)
check("a sample of one is the first program", one == [items[0]], repr(one))

sample = spread(items, 12)
check("the sample has the requested size", len(sample) == 12, str(len(sample)))
check("the sample has no duplicates", len(set(sample)) == len(sample))
check("the sample starts at the beginning", sample[0] == items[0])
check("the sample reaches the end", sample[-1] >= items[110], sample[-1])
gaps = [items.index(b) - items.index(a) for a, b in zip(sample, sample[1:])]
check("the sample is evenly spaced", max(gaps) - min(gaps) <= 1, str(gaps))

# What a failure means: an example that needs something is not a broken example.
kind, extra = classify("NameError: name 'مفرز' is not defined")
check("a word from an uninstalled library is a library need", kind == "library", str((kind, extra)))
kind, _ = classify('الكلمة "ألحق" من مكتبة apl-advanced.')
check("the language's own hint names the library", kind == "library", kind)
kind, _ = classify("EOFError: EOF when reading a line")
check("a program waiting for input is an input need", kind == "input", kind)
kind, _ = classify("ConnectionError: no route to host")
check("a program reaching the network is a network need", kind == "network", kind)
kind, _ = classify("NameError: name 'س' is not defined")
check("a plain typo is not explained away", kind is None, str(kind))


def record(name, ok, needs=None):
    stage = {"ok": ok, "stage": "run", "detail": ""}
    if needs:
        stage["needs"] = needs
    return {"example": name, "interpreter": stage}


import contextlib  # noqa: E402
import io  # noqa: E402


def verdict(results, baseline=None):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        code = report(results, False, False, baseline)
    return code, buffer.getvalue()


code, _ = verdict([record("a.apl", True), record("b.apl", False)])
check("a failure fails the run", code == 1, str(code))

code, _ = verdict([record("a.apl", False, "library"), record("b.apl", True)])
check("a library need does not fail the run", code == 0, str(code))

code, _ = verdict([record("a.apl", False)], baseline=["a.apl"])
check("a known-broken example does not fail the run", code == 0, str(code))

code, text = verdict([record("a.apl", False)], baseline=["a.apl"])
check("a known-broken example is reported as known", "معروف" in text, text)

code, text = verdict([record("a.apl", True)], baseline=["a.apl"])
check("an example that got fixed is pointed at the baseline", "شيله" in text, text)

code, _ = verdict([record("a.apl", False)], baseline=["other.apl"])
check("a new failure still fails next to a baseline", code == 1, str(code))

total = 8 + 12
print()
print(f"{total - failures}/{total} checks passed")
raise SystemExit(1 if failures else 0)

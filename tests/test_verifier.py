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

from verify_examples import spread  # noqa: E402

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

print()
print(f"{8 - failures}/8 checks passed")
raise SystemExit(1 if failures else 0)

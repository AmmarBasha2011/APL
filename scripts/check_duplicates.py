#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_duplicates.py — لا تكرار في عناصر المكتبات.

عنصران مكرران = مفتاحان عربيان (في أي مكتبة) يشيران إلى نفس الكائن الحقيقي في
Python، حتى لو اختلف المسار المكتوب. أمثلة على نفس الكائن:
  - نفس الدالة أو الصنف مستورَدين من وحدتين (pkg.a.f و pkg.b.f).
  - نفس الطريقة المعرَّفة في صنف أب ومكتوبة تحت كل صنف ابن.

يفشل (exit 1) عند أي تكرار. لا يوجد baseline ولا قائمة استثناءات.

الاستخدام:
    python scripts/check_duplicates.py            # فحص
    python scripts/check_duplicates.py --list     # اطبع كل المجموعات
"""

import argparse
import collections
import importlib
import inspect
import os
import sys
import types
import warnings

warnings.filterwarnings("ignore")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from core.libraries import LIBRARIES  # noqa: E402


def resolve(path):
    parts = path.split(".")
    for cut in range(len(parts), 0, -1):
        try:
            obj = importlib.import_module(".".join(parts[:cut]))
        except Exception:
            continue
        chain = [obj]
        try:
            for p in parts[cut:]:
                obj = getattr(obj, p)
                chain.append(obj)
        except Exception:
            continue
        return chain, parts[cut:]
    return None


def canonical(path):
    """مفتاح الهوية الحقيقية للكائن، أو None لو غير قابل للحل/غير مناسب للمقارنة."""
    if not path or path.startswith("@"):
        return None
    r = resolve(path)
    if r is None:
        return None
    chain, rest = r
    obj = chain[-1]
    if rest and inspect.isclass(chain[-2]):
        owner = chain[-2]
        for k in owner.__mro__:
            if rest[-1] in k.__dict__:
                return ("member", k.__module__, k.__qualname__, rest[-1])
        return ("member", owner.__module__, owner.__qualname__, rest[-1])
    if isinstance(obj, types.ModuleType):
        return None
    if (inspect.isclass(obj) or inspect.isfunction(obj) or inspect.isbuiltin(obj)
            or inspect.ismethoddescriptor(obj)):
        mod = getattr(obj, "__module__", None)
        qn = getattr(obj, "__qualname__", getattr(obj, "__name__", None))
        if mod and qn:
            return ("object", mod, qn)
    return None


def library_items():
    for lib, mod in LIBRARIES.items():
        for attr in dir(mod):
            d = getattr(mod, attr)
            if attr.isupper() and isinstance(d, dict):
                for ar, val in d.items():
                    if isinstance(val, str):
                        yield lib, attr, ar, val


def find_groups():
    groups = collections.defaultdict(list)
    for lib, attr, ar, val in library_items():
        c = canonical(val)
        if c:
            groups[c].append((lib, attr, ar, val))
    return {c: g for c, g in groups.items() if len({x[2] for x in g}) > 1}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    groups = find_groups()
    extra = sum(len({x[2] for x in g}) - 1 for g in groups.values())
    if not groups:
        print("✓ لا يوجد تكرار في عناصر المكتبات")
        return 0
    print(f"✗ {extra} عنصراً مكرراً في {len(groups)} كائناً")
    for c, g in list(groups.items())[: (None if args.list else 25)]:
        print("  " + "/".join(map(str, c)))
        for lib, attr, ar, val in g:
            print(f"      [{lib}] {ar} -> {val}")
    return 1


if __name__ == "__main__":
    sys.exit(main())

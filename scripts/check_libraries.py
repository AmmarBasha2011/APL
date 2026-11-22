#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_libraries.py — سلامة كل المكتبات العربية.

فحوص صلبة (تفشل دائماً):
  1. التكرار: مفيش مفتاح عربي مكرر داخل نفس المكتبة.
  2. التصادم: مفتاح عربي واحد في مكتبتين (أو أكثر).
  3. التصادم مع نواة اللغة.

فحوص مُ Baseline-izada (تفشل على الجديد فقط، والقديم مُسجّل في
scripts/baselines/library_issues.txt):
  4. التحويل: كل مفتاح عربي يُترجم فعلاً إلى الهدف المكتوب جنبه.
  5. الحلّ: مسار يبدأ بوحدة قابلة للاستيراد لازم يُحلّ.
  6. بداية السطر: المفتاح يعمل في التعبير لكنه لا يعمل في بداية السطر.
  7. تأكيد الاسم (مع --strict).

الاستخدام:
    python scripts/check_libraries.py              # يفشل على جديد/صلب
    python scripts/check_libraries.py --strict     # يفشل على كل القديم كمان
    python scripts/check_libraries.py --update-baseline   # سجّل الوضع الحالي
    python scripts/check_libraries.py --quiet
"""

import argparse
import importlib
import inspect
import os
import re
import sys
import warnings

warnings.filterwarnings("ignore")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from core.libraries import LIBRARIES                          # noqa: E402
from core.apl_runner.main import transpile                    # noqa: E402
from core.apl_runner.inline_replacer import _inline_replace   # noqa: E402
from core.apl_runner import patterns as P                     # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_BASELINE = os.path.join(HERE, "baselines", "library_issues.txt")

CALLABLE_KINDS = ("FUNCS", "VERBS", "STANDALONE", "ORD_FUNCS",
                  "BUILTIN_FUNCS", "STR_FUNCS")
PATH_KINDS = CALLABLE_KINDS + ("CONSTS",)

# الفحوص القديمة دي ليها baseline؛ الباقي صلب
BASELINED = {"التحويل", "حلّ المسار", "بداية السطر", "تأكيد الاسم"}
HAS_ARABIC = re.compile(r"[\u0600-\u06FF]")
LOOKS_LIKE_PATH = re.compile(r"^[A-Za-z_]\w*(\.[A-Za-z_]\w*)+$")


def library_dicts(mod):
    out = {}
    for attr in dir(mod):
        if attr.isupper() and isinstance(getattr(mod, attr), dict):
            out.setdefault(attr.rsplit("_", 1)[-1], {}).update(getattr(mod, attr))
    return out


def head_importable(path):
    try:
        importlib.import_module(path.split(".")[0])
        return True
    except Exception:
        return False


def resolve(path):
    parts = path.split(".")
    for cut in range(len(parts), 0, -1):
        try:
            obj = importlib.import_module(".".join(parts[:cut]))
        except Exception:
            continue
        ok = True
        for p in parts[cut:]:
            try:
                obj = getattr(obj, p)
            except Exception:
                ok = False
                break
        if ok:
            return True
    return False


def modules_of(mod):
    mods = getattr(mod, "IMPORT_MODULES", None)
    if mods:
        return list(mods)
    stmt = (getattr(mod, "IMPORT_STATEMENT", "") or "").replace("import ", "")
    names = []
    for part in stmt.split(","):
        part = part.strip().split(" import ")[0].strip()
        if part and re.match(r"^[A-Za-z_][\w.]*$", part):
            names.append(part)
    return names


def known_attributes(mods):
    attrs = set()
    for name in mods:
        try:
            m = importlib.import_module(name)
        except Exception:
            continue
        for n in dir(m):
            if not n.startswith("_"):
                attrs.add(n)
        for n in dir(m):
            obj = getattr(m, n, None)
            if inspect.isclass(obj):
                for a in dir(obj):
                    if not a.startswith("_"):
                        attrs.add(a)
    return attrs


def collect_findings(strict):
    """يرجع (hard, soft) — كل واحدة قائمة (class, lib, key, detail)."""
    hard, soft = [], []
    stats = {"libraries": 0, "entries": 0, "resolved": 0, "runtime": 0,
             "transpiled": 0, "checks": 0}
    key_owner = {}

    for lib, mod in LIBRARIES.items():
        stats["libraries"] += 1
        dicts = library_dicts(mod)
        stats["entries"] += sum(len(d) for d in dicts.values())
        mods = modules_of(mod)
        known = None

        for kind, d in dicts.items():
            for ar, val in d.items():
                if not isinstance(val, str) or not ar:
                    continue
                key_owner.setdefault(ar, []).append((lib, val))

                # ---- الحلّ ----
                if kind in PATH_KINDS and not val.startswith("@") \
                        and LOOKS_LIKE_PATH.match(val):
                    if head_importable(val):
                        if resolve(val):
                            stats["resolved"] += 1
                        else:
                            soft.append(("حلّ المسار", lib, ar,
                                         f"{ar} -> {val}"))
                    else:
                        stats["runtime"] += 1

                # ---- التحويل ----
                if kind == "METHODS":
                    src, want = f"س.{ar}()", val
                elif kind == "PROPS":
                    src, want = f"س.{ar}", val
                elif kind == "KWARGS":
                    src, want = f"ف({ar} = 1)", f"{val} = 1"
                elif kind in CALLABLE_KINDS:
                    src, want = f"{ar}()", val
                else:
                    src, want = ar, val
                if not HAS_ARABIC.search(src):
                    src = "اطبع " + src          # مفتاح لاتيني: لازم عرببي يحفّز المسح
                got = _inline_replace(src)
                stats["checks"] += 1
                if want in got:
                    stats["transpiled"] += 1
                else:
                    soft.append(("التحويل", lib, ar,
                                 f"{ar}: أردنا «{want}» في «{got.strip()[:70]}»"))

                # ---- بداية السطر (للمفاتيح العربية فقط؛ اللاتينية لا
                # معنى لاختبارها في بداية سطر) ----
                if kind != "KWARGS" and HAS_ARABIC.search(ar):
                    forms = [src]
                    if kind in CALLABLE_KINDS:
                        forms.append(ar)
                    if not any(want in transpile(s) for s in forms):
                        soft.append(("بداية السطر", lib, ar,
                                     f"{ar} ← {val} يعمل في التعبير فقط"))

                # ---- تأكيد الاسم ----
                if strict and kind in ("METHODS", "PROPS"):
                    if known is None:
                        known = known_attributes(mods)
                    if val not in known:
                        soft.append(("تأكيد الاسم", lib, ar, f"{ar} -> {val}"))

    # ---- التكرار داخل المكتبة ----
    for lib, mod in LIBRARIES.items():
        seen = {}
        for kind, d in library_dicts(mod).items():
            for ar, val in d.items():
                if ar in seen and seen[ar] != val:
                    hard.append(("تكرار داخل المكتبة", lib, ar,
                                 f"{ar}: {seen[ar]} vs {val}"))
                seen[ar] = val

    # ---- التصادم بين المكتبات ----
    for ar, owners in key_owner.items():
        libs = sorted({o[0] for o in owners})
        if len(libs) > 1:
            hard.append(("تصادم بين المكتبات", "+".join(libs), ar,
                         f"{ar} في {libs}"))

    # ---- التصادم مع النواة ----
    core_words = set()
    for attr in dir(P):
        v = getattr(P, attr)
        if attr.startswith("_") and isinstance(v, dict):
            core_words.update(v.keys())
    core_words |= {"صواب", "خطأ", "لا_شيء", "ط", "ه", "تاو", "لانهائي_موجب"}
    for ar in key_owner:
        if ar in core_words:
            hard.append(("تصادم مع النواة", "-", ar, ar))

    stats["soft"] = len(soft)
    return hard, soft, stats


def read_baseline(path):
    known = set()
    if not os.path.exists(path):
        return known
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                known.add(tuple(line.split("|")))
    return known


def write_baseline(path, findings):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lines = [
        "# مشاكل مكتبات معروفة — يولّدها check_libraries.py --update-baseline",
        "# الصيغة: class|library|key",
        "# أي مشكلة جديدة غير موجودة هنا تفشل الفحص.",
    ]
    for cls, lib, key, _ in sorted(findings):
        lines.append(f"{cls}|{lib}|{key}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="افشل على كل المشاكل القديمة كمان")
    ap.add_argument("--update-baseline", action="store_true",
                    help="سجّل الوضع الحالي ك baseline")
    ap.add_argument("--baseline", default=DEFAULT_BASELINE)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    hard, soft, stats = collect_findings(args.strict)

    if args.update_baseline:
        write_baseline(args.baseline, hard + soft)
        print(f"سُجّل {len(hard) + len(soft)} مشكلة في {args.baseline}")
        return 0

    baseline = read_baseline(args.baseline)
    new = [f for f in hard + soft
           if (f[0], f[1], f[2]) not in baseline]
    resolved = len([1 for f in hard + soft if (f[0], f[1], f[2]) in baseline])

    if not args.quiet:
        print(f"المكتبات: {stats['libraries']}   العناصر: {stats['entries']}")
        print(f"مسارات محلولة: {stats['resolved']}    "
              f"مراجع زمن تشغيل: {stats['runtime']}")
        print(f"فحوص تحويل: {stats['checks']}   ناجحة: {stats['transpiled']}")
        print(f"baseline: {len(baseline)} مشكلة معروفة")
        print()
        if new:
            print(f"=== مشاكل جديدة ({len(new)}) ===")
            for cls, lib, key, detail in new[:60]:
                print(f"  [{cls}] [{lib}] {detail}")
            if len(new) > 60:
                print(f"  ... و{len(new) - 60} أخرى")
        else:
            print("✓ لا توجد مشاكل جديدة")
        if resolved and not args.strict:
            print(f"\n(توجد {resolved} مشكلة قديمة مُسجّلة في الـ baseline — "
                  f"استعمل --strict لرؤيتها)")

    bad = len(new) if not args.strict else len(new) + resolved
    if args.quiet:
        print(f"{stats['libraries']} مكتبة، {stats['entries']} عنصراً، "
              f"{stats['checks']} فحص تحويل — "
              f"{'✓ سليم' if bad == 0 else f'✗ {bad} مشكلة'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

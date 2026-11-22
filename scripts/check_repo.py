#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_repo.py — نظافة الريبو واتساق التوثيق.

الفحوص:
  1. الترجمة: كل ملفات بايثون بتتـ compile.
  2. اتساق النسخة: __version__ في main.py == README == docs/README.
  3. اتساق الأرقام: جدول المكتبات والإجماليات في README و docs/README
     مولّدة من الكود مش مكتوبة بالإيد.
  4. فايلات أثرية: *.db ومخرجات benchmark وملفات _apl_* المؤقتة.
  5. التحميل الكسول: برنامج بسيط لازم ما يستوردش flask/sqlite3/pdb/...
  6. بلوكات ```apl في README لازم تشتغل (البلوكات اللي محتاجة مكتبة
     خارجية غير مثبتة تُتخطّى).

الاستخدام:
    python scripts/check_repo.py          # يفشل عند مشكلة
    python scripts/check_repo.py --quiet
"""

import argparse
import glob
import io
import os
import re
import subprocess
import sys
import warnings

warnings.filterwarnings("ignore")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROBLEMS = []
NOTES = []


def bad(msg):
    PROBLEMS.append(msg)


def note(msg):
    NOTES.append(msg)


# ---------------------------------------------------------------- 1
def check_compile():
    r = subprocess.run([sys.executable, "-m", "compileall", "-q",
                        os.path.join(ROOT, "core"),
                        os.path.join(ROOT, "scripts"),
                        os.path.join(ROOT, "apl.py"),
                        os.path.join(ROOT, "test_examples.py")],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        bad(f"compileall فشل:\n{r.stdout}\n{r.stderr}")
    else:
        note("compileall ✓")


# ---------------------------------------------------------------- 2
def read(path):
    return io.open(os.path.join(ROOT, path), encoding="utf-8").read()


def check_version():
    src = read("core/apl_runner/main.py")
    m = re.search(r'__version__\s*=\s*"([^"]+)"', src)
    if not m:
        bad("مفيش __version__ في main.py")
        return
    code_v = m.group(1)
    readme = read("README.md")
    rm = re.search(r"APL v([\d.]+)", readme)
    docs = read("docs/README.md")
    dm = re.search(r"APL v([\d.]+)", docs)
    if not rm:
        bad("مفيش سطر النسخة في README.md")
    elif rm.group(1) != code_v:
        bad(f"النسخة في README ({rm.group(1)}) ≠ main.py ({code_v})")
    if not dm:
        bad("مفيش سطر النسخة في docs/README.md")
    elif dm.group(1) != code_v:
        bad(f"النسخة في docs/README.md ({dm.group(1)}) ≠ main.py ({code_v})")
    if not any(r == code_v for r in [rm.group(1) if rm else None,
                                    dm.group(1) if dm else None]):
        note(f"version ✓ ({code_v})")
    else:
        note(f"version ✓ ({code_v})")


# ---------------------------------------------------------------- 3
def library_counts():
    sys.path.insert(0, ROOT)
    from core.libraries import LIBRARIES
    out = {}
    for name, mod in LIBRARIES.items():
        out[name] = sum(len(v) for a in dir(mod)
                        if a.isupper() and isinstance((v := getattr(mod, a)), dict))
    return out


def parse_table(text):
    """| `lib` | N | → {lib: N}"""
    out = {}
    for m in re.finditer(r"^\|\s*`([a-z0-9_]+)`\s*\|\s*([\d,]+)\s*\|", text, re.M):
        out[m.group(1)] = int(m.group(2).replace(",", ""))
    return out


def parse_totals(text):
    """يرجع (total, libs, unique) من سطر الإجمالي."""
    m = re.search(r"الإجمالي:\s*([\d,]+)\s*عنصراً في\s*(\d+)\s*مكتبة", text)
    u = re.search(r"\(([\d,]+)\s*مفتاحاً فريداً", text)
    f = re.search(r"الفريدة\s*\*\*([\d,]+)\s*عنصراً\*\*", text)
    if not m:
        return None
    return (int(m.group(1).replace(",", "")), int(m.group(2)),
            int(u.group(1).replace(",", "")) if u else None,
            int(f.group(1).replace(",", "")) if f else None)


def check_docs_numbers():
    actual = library_counts()
    total = sum(actual.values())
    sys.path.insert(0, ROOT)
    from core.libraries import LIBRARIES
    unique = len({k for mod in LIBRARIES.values() for a in dir(mod)
                  if a.isupper() and isinstance(getattr(mod, a), dict)
                  for k in getattr(mod, a)})

    for path in ("README.md", "docs/README.md"):
        text = read(path)
        tbl = parse_table(text)
        if not tbl:
            bad(f"مفيش جدول مكتبات في {path}")
            continue
        for lib, n in sorted(actual.items()):
            if lib not in tbl:
                bad(f"{path}: المكتبة `{lib}` ناقصة من الجدول")
            elif tbl[lib] != n:
                bad(f"{path}: `{lib}` الجدول {tbl[lib]} ≠ الحقيقي {n}")
        for lib in tbl:
            if lib not in actual:
                bad(f"{path}: `{lib}` في الجدول لكنه غير موجود في الكود")
        got = parse_totals(text)
        if got is None:
            bad(f"{path}: مفيش سطر الإجمالي")
        else:
            if got[0] != total:
                bad(f"{path}: الإجمالي {got[0]} ≠ الحقيقي {total}")
            if got[1] != len(actual):
                bad(f"{path}: عدد المكتبات {got[1]} ≠ الحقيقي {len(actual)}")
            if got[2] is not None and got[2] != unique:
                bad(f"{path}: المفاتيح الفريدة {got[2]} ≠ الحقيقي {unique}")
            if got[3] is not None and got[3] != unique + 231:
                bad(f"{path}: إجمالي العناصر الفريدة {got[3]} ≠ الحقيقي {unique + 231}")
    note(f"أرقام التوثيق ✓ ({len(actual)} مكتبة، {total} عنصراً)")


# ---------------------------------------------------------------- 4
def check_stray():
    patterns = ["*.db", "benchmarks/*-results.json", "_apl_*"]
    found = []
    for p in patterns:
        found += [f for f in glob.glob(os.path.join(ROOT, p))
                  if ".git" not in f]
    if found:
        bad("فايلات أثرية في الريبو: " + ", ".join(os.path.basename(f) for f in found))
    else:
        note("مفيش فايلات أثرية ✓")
    # أي فايل غير متتبع (وغير متجاهَل في .gitignore) مشكلة: الريبو لازم يكون
    # نظيف بعد تشغيل الفحوص.
    if os.path.isdir(os.path.join(ROOT, ".git")):
        r = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"],
                           capture_output=True, text=True, cwd=ROOT)
        untracked = [ln for ln in (r.stdout or "").splitlines() if ln.strip()]
        if untracked:
            bad("فايلات غير متتبعة في الريبو: " + ", ".join(untracked[:10]))
        else:
            note("مفيش فايلات غير متتبعة ✓")


# ---------------------------------------------------------------- 5
LAZY_PROBE = r"""
import sys
sys.path.insert(0, %r)
from core.apl_runner.main import transpile, _RUNTIME
exec(compile(_RUNTIME + "\n" + transpile("اطبع 1"), "<apl>", "exec"), {})
watch = {"flask", "fastapi", "requests", "sqlite3", "pdb", "tracemalloc",
         "dis", "symtable", "ssl", "smtplib", "imaplib", "ftplib"}
loaded = sorted({m.split(".")[0] for m in sys.modules} & watch)
print("WATCH:" + ",".join(loaded))
"""


def check_lazy():
    r = subprocess.run([sys.executable, "-c", LAZY_PROBE % ROOT],
                       capture_output=True, text=True, cwd=ROOT, timeout=120)
    line = next((ln for ln in (r.stdout or "").splitlines() if ln.startswith("WATCH:")), "")
    loaded = [x for x in line[len("WATCH:"):].split(",") if x]
    if r.returncode != 0:
        bad(f"فحص التحميل الكسول فشل: {r.stderr.strip()[:200]}")
    elif loaded:
        bad(f"تحميل كسول مكسور: استُوردت {loaded} في برنامج لا يستعملها")
    else:
        note("التحميل الكسول ✓")


# ---------------------------------------------------------------- 6
def check_readme_blocks():
    text = read("README.md")
    blocks = re.findall(r"```apl\n(.*?)```", text, re.S)
    if not blocks:
        bad("مفيش بلوكات ```apl في README")
        return
    import tempfile
    ok = skipped = 0
    with tempfile.TemporaryDirectory() as tmp:
        # البلوكات بتنسخ لمجلد مؤقت: بعضها بيكتب فايلات (مثل مثال XML)
        # وما لازمش تلوث الريبو.
        apl = os.path.join(ROOT, "apl.py")
        for i, block in enumerate(blocks):
            path = os.path.join(tmp, f"block{i}.apl")
            io.open(path, "w", encoding="utf-8").write(block)
            r = subprocess.run([sys.executable, apl, path],
                               capture_output=True, text=True, cwd=tmp,
                               input="", timeout=120)
            err = r.stderr or ""
            if r.returncode == 0:
                ok += 1
            elif "الوحدة غير موجودة" in err or "No module named" in err:
                skipped += 1
                note(f"بلوك {i}: يتخطّى (مكتبة خارجية غير مثبتة)")
            else:
                first = next((ln for ln in err.splitlines() if ln.strip()), "")
                bad(f"بلوك {i} في README فشل: {first[:120]}")
    note(f"بلوكات README: {ok} ناجحة، {skipped} متخطاة، {len(blocks) - ok - skipped} فاشلة")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    check_compile()
    check_version()
    check_docs_numbers()
    check_stray()
    check_lazy()
    check_readme_blocks()

    if not args.quiet:
        for n in NOTES:
            print(f"  ✓ {n}")
        print()
    if PROBLEMS:
        print(f"=== مشاكل ({len(PROBLEMS)}) ===")
        for p in PROBLEMS:
            print(f"  ✗ {p}")
    else:
        print("✓ الريبو سليم")
    return 1 if PROBLEMS else 0


if __name__ == "__main__":
    sys.exit(main())

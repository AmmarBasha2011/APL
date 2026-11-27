"""Run every APL example and report what is actually broken.

Two runs per example, because they fail differently:

  interpreter   `عمار فحص` then `عمار شغل`, with a timeout. This is what a user
                gets on their machine, with whatever libraries are installed.
  playground    the same program through the playground's own Python bootstrap
                (the code inside playground/index.html), in a browser-like
                setting: no libraries installed, no stdin, no files.

A problem is reported with the example's name and the first line that explains
it, so the list can be worked through instead of guessed at.

    python tools/verify_examples.py --dir /path/to/examples
    python tools/verify_examples.py --dir . --json > report.json
    python tools/verify_examples.py --dir . --only 12-  # examples 12 and up
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APL = ROOT / "apl.py"
PAGE = ROOT / "playground" / "index.html"

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

# Programs that cannot work in the browser playground: they wait for input, read
# or write files, or reach the network.
NEEDS_STDIN = re.compile(r"(?<![\w\u0600-\u06FF])(?:ادخل|input)\s*\(")
NEEDS_FILES = re.compile(r"(?<![\w\u0600-\u06FF])(?:اقرأ|اكتب|open|فتح)\s*\(")
NEEDS_NET = re.compile(r"(?<![\w\u0600-\u06FF])(?:requests|urllib|fetch|جلب)\b")


def bootstrap() -> str:
    """The playground's Python bootstrap, read out of the page itself."""
    page = PAGE.read_text(encoding="utf-8")
    match = re.search(r"const BOOTSTRAP = `(.*?)`;", page, re.S)
    if not match:
        raise SystemExit("could not find the playground bootstrap in playground/index.html")
    code = match.group(1)
    return code.replace("\\\\n", "\\n").replace('\\\\"', '\\"').replace("\\\\", "\\")


PLAYGROUND_RUNNER = """
import io, json, sys, traceback
sys.path.insert(0, {root!r})
{bootstrap}
source = open({source!r}, encoding="utf-8").read()
try:
    print(json.dumps({{"output": apl_run(source)}}))
except BaseException:
    print(json.dumps({{"output": "", "error": traceback.format_exc()[-600:]}}))
"""


VOCABULARY = {}


def vocabulary():
    """Word → library name, for every word the published libraries define.

    The example folder is not the place to notice that a program needs a
    library: this map turns a failure into "this example needs apl-<name>",
    which is a decision (rewrite the example, or install the library).
    """
    if VOCABULARY:
        return VOCABULARY
    import ast
    # Point this at a folder of <name>_funcs.py files (a checkout of the
    # library repos) to get "this example needs apl-<name>" instead of a bare
    # error. Without it, every failure is still reported, just not classified.
    home = Path(os.environ.get("APL_LIBRARY_SOURCES", ""))
    if not home.is_dir():
        return VOCABULARY
    for path in sorted(home.glob("*_funcs.py")):
        library = path.stem[:-len("_funcs")]
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        for node in tree.body:
            if not (isinstance(node, ast.Assign) and len(node.targets) == 1
                    and isinstance(node.targets[0], ast.Name)):
                continue
            name = node.targets[0].id
            if not isinstance(node.value, ast.Dict) or not any(
                    name.endswith(suffix) for suffix in
                    ("FUNCS", "CONSTANTS", "CONSTS", "METHODS", "PROPS")):
                continue
            try:
                table = ast.literal_eval(node.value)
            except (ValueError, SyntaxError):
                continue
            if isinstance(table, dict):
                for word in table:
                    if isinstance(word, str):
                        VOCABULARY.setdefault(word, library)
    return VOCABULARY


WORD_IN_ERROR = re.compile(r"'([^']*[\u0600-\u06FF][^']*)'")


def needs_library(detail: str):
    """The library an example is missing, when the error names one of its words."""
    words = vocabulary()
    for candidate in WORD_IN_ERROR.findall(detail):
        if candidate in words:
            return words[candidate]
    return None


def first_problem_line(text: str) -> str:
    for line in text.splitlines():
        line = line.strip().replace("\u202b", "").replace("\u202c", "")
        if line.startswith("APL-") or line.startswith("خطأ") or "Error" in line:
            return line[:160]
    return (text.strip().splitlines() or [""])[0][:160]


def run_interpreter(path: Path, timeout: float):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", APL_NO_CACHE="1")
    check = subprocess.run([sys.executable, str(APL), "فحص", str(path)],
                           capture_output=True, text=True, encoding="utf-8",
                           env=env, timeout=timeout + 30)
    if check.returncode != 0:
        text = check.stderr or check.stdout
        return {"ok": False, "stage": "check",
                "detail": first_problem_line(text), "raw": text}
    try:
        run = subprocess.run([sys.executable, str(APL), "شغل", str(path)],
                             capture_output=True, text=True, encoding="utf-8",
                             env=env, timeout=timeout, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return {"ok": False, "stage": "run", "detail": f"عدّى {timeout:.0f} ثانية من غير ما يخلص"}
    if run.returncode != 0:
        text = run.stderr or run.stdout
        return {"ok": False, "stage": "run",
                "detail": first_problem_line(text), "raw": text}
    return {"ok": True, "output": run.stdout}


def run_playground(path: Path, work: Path, timeout: float):
    """Run one example through the playground's own bootstrap."""
    if NEEDS_STDIN.search(path.read_text(encoding="utf-8")):
        return {"ok": False, "stage": "playground", "detail": "بيستنى إدخال (ادخل) — بيتعلّق في المتصفح"}
    source = work / "program.py"
    runner = work / "runner.py"
    runner.write_text(PLAYGROUND_RUNNER.format(
        root=str(work / "apl"), bootstrap=bootstrap(), source=str(path)), encoding="utf-8")
    try:
        result = subprocess.run([sys.executable, str(runner)], capture_output=True,
                                text=True, encoding="utf-8", timeout=timeout,
                                stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return {"ok": False, "stage": "playground", "detail": f"عدّى {timeout:.0f} ثانية في بيئة المتصفح"}
    if result.returncode != 0:
        return {"ok": False, "stage": "playground", "detail": first_problem_line(result.stderr)}
    try:
        payload = json.loads((result.stdout.strip().splitlines() or ["{}"])[-1])
    except ValueError:
        return {"ok": False, "stage": "playground", "detail": "المخرجات مش JSON: " + result.stdout[:120]}
    text = payload.get("output") or ""
    if "APL-" in text or "خطأ" in text:
        return {"ok": False, "stage": "playground", "detail": first_problem_line(text)}
    return {"ok": True, "output": text}


def wanted(name: str, only) -> bool:
    if not only:
        return True
    number = re.match(r"(\d+)", name)
    start = int(number.group(1)) if number else -1
    return start >= only


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dir", default=str(ROOT / "examples"))
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--only", type=int, default=None, help="start at this example number")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--no-playground", action="store_true")
    args = parser.parse_args(argv)

    folder = Path(args.dir)
    programs = sorted(folder.glob("*.apl"))
    if not programs:
        print(f"مفيش أمثلة في {folder}")
        return 1

    work = Path(tempfile.mkdtemp(prefix="apl-verify-"))
    try:
        if not args.no_playground:
            shutil.copytree(ROOT / "core", work / "apl" / "core",
                            ignore=shutil.ignore_patterns("__pycache__"))
        results = []
        for program in programs:
            if not wanted(program.name, args.only):
                continue
            if args.limit is not None and len(results) >= args.limit:
                break
            record = {"example": program.name}
            interpreter = run_interpreter(program, args.timeout)
            record["interpreter"] = interpreter
            if not interpreter["ok"]:
                library = needs_library(interpreter.get("raw") or interpreter["detail"])
                if library:
                    interpreter["needs_library"] = library
            if not args.no_playground:
                record["playground"] = run_playground(program, work, args.timeout)
            results.append(record)
            if not args.json:
                marks = "ok " if interpreter["ok"] else "FAIL"
                print(f"{marks} {program.name}")
                for stage in ("interpreter", "playground"):
                    outcome = record.get(stage)
                    if outcome and not outcome["ok"]:
                        print(f"     {stage}/{outcome['stage']}: {outcome['detail']}")
                        if outcome.get("needs_library"):
                            print(f"     محتاج مكتبة: apl-{outcome['needs_library']}")
    finally:
        shutil.rmtree(work, ignore_errors=True)

    broken = [r for r in results if not r["interpreter"]["ok"]
              or (r.get("playground") and not r["playground"]["ok"])]
    if args.json:
        print(json.dumps({"total": len(results), "broken": broken}, ensure_ascii=False, indent=2))
    else:
        print()
        print(f"{len(results) - len(broken)}/{len(results)} سليم")
        if broken:
            print("محتاج إصلاح: " + "، ".join(r["example"] for r in broken[:40])
                  + (" …" if len(broken) > 40 else ""))
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())

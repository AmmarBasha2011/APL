#!/usr/bin/env python3
# APL - Ammar Programming Language
# Converts Arabic code to Python

import sys, os, re, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.platform == "win32":
    import ctypes
    try:
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleOutputCP(65001)
        kernel32.SetConsoleCP(65001)
    except Exception:
        pass

TYPE_ALIASES = {
    "صحيح": "int", "نص": "str", "عشري": "float", "منطق": "bool",
    "قائمة": "list", "مجموعة": "tuple", "مصفوفة": "set",
    "قاموس": "dict", "بايت": "bytes",
}
_TYPE_PATTERN = re.compile("(" + "|".join(TYPE_ALIASES.keys()) + r")\s*\(")

_INLINE_FUNCS = {"نطاق": "range", "طول": "len"}
_INLINE_FUNC_PATTERN = re.compile("(" + "|".join(_INLINE_FUNCS.keys()) + r")\s*\(")

_MATH_FUNCS = {
    "مطلق": "abs", "قوة": "pow", "جذر": "math.sqrt",
    "أكبر": "max", "أصغر": "min", "مقرب": "round",
    "مجموع": "sum", "مفرز": "sorted",
}
_MATH_PATTERN = re.compile("(" + "|".join(_MATH_FUNCS.keys()) + r")\s*\(")

_METHOD_ALIASES = {
    "تقسيم": "split", "أضف": "append", "ضم": "join",
    "عكس": "reverse", "فرز": "sort", "حذف": "pop",
    "نسخ": "copy", "عد": "count", "بحث": "index",
    "أزل": "remove", "وسع": "extend", "أدخل": "insert",
    "استبدال": "replace", "علوي": "upper", "سفلي": "lower",
    "بداية": "startswith", "نهاية": "endswith", "تقليم": "strip",
    "اتحاد": "union", "تقاطع": "intersection", "فرق": "difference",
}
_METHOD_PATTERN = re.compile(r"\." + "(" + "|".join(_METHOD_ALIASES.keys()) + r")\s*\(")

_TYPE_NAMES = {
    "صحيح": "int", "نص": "str", "عشري": "float", "منطق": "bool",
    "قائمة": "list", "مجموعة": "tuple", "مصفوفة": "set",
    "قاموس": "dict", "بايت": "bytes",
}

_EXTRA_FUNCS = {
    "جسون_تحويل": "json.dumps",
    "جسون": "json.loads",
    "الساعة": "datetime.datetime.now",
    "التاريخ": "datetime.date.today",
    "فتح": "open",
    "كل": "all",
    "أي": "any",
    "خريطة": "map",
    "فلترة": "filter",
    "تجميع": "zip",
    "عشوائي": "random.choice",
    "نوع": "type",
    "عدد": "enumerate",
    "انتظر": "time.sleep",
    "وقت": "time.time",
    "تمثيل": "repr",
    "ثنائي": "bin",
    "سداسي": "hex",
    "ترتيب": "ord",
    "رمز": "chr",
    "اخرج": "exit",
    "حجم_ملف": "os.path.getsize",
    "قائمة_ملفات": "os.listdir",
}
_EXTRA_PATTERN = re.compile("(" + "|".join(_EXTRA_FUNCS.keys()) + r")\s*\(")

_CONSTANTS = {
    "صواب": "True", "خطأ": "False", "لا_شيء": "None",
    "ط": "math.pi", "ه": "math.e",
}
_CONSTANT_PATTERN = re.compile(r"(?<!\w)(" + "|".join(_CONSTANTS.keys()) + r")(?!\w)")

_LOGICAL_PATTERNS = [
    (re.compile(r"(?<!\w)و(?!\w)"), "and"),
    (re.compile(r"(?<!\w)أو(?!\w)"), "or"),
    (re.compile(r"(?<!\w)ليس(?!\w)"), "not"),
    (re.compile(r"(?<!\w)مثل(?!\w)"), "as"),
    (re.compile(r"(?<!\w)في(?!\w)"), "in"),
]

_KW_ALIASES = {
    "ترميز": "encoding",
    "تأكد_من_ascii": "ensure_ascii",
    "مسافة_بادئة": "indent",
}

_IO_ALIASES = {
    "اقرأ": "_apl_read",
    "اكتب": "_apl_write",
    "اغلق": "_apl_close",
    "طلب": "_apl_fetch",
}
_IO_PATTERN = re.compile("(" + "|".join(_IO_ALIASES.keys()) + r")\s*\(")


def _replace_type_names(text: str) -> str:
    for arabic, english in _TYPE_NAMES.items():
        text = re.sub(rf"(?<!\w){arabic}(?!\w)", english, text)
    return text

def _inline_replace(text: str) -> str:
    strings = {}
    def _save(m):
        idx = len(strings)
        strings[idx] = m.group(0)
        return f"\x00APL{idx}\x00"
    text = re.sub(r'"[^"]*"', _save, text)
    text = re.sub(r"'[^']*'", _save, text)

    text = re.sub(r"ادخل\s*\(", "input(", text)
    text = _TYPE_PATTERN.sub(lambda m: f"{TYPE_ALIASES[m.group(1)]}(", text)
    text = _INLINE_FUNC_PATTERN.sub(lambda m: f"{_INLINE_FUNCS[m.group(1)]}(", text)
    text = _METHOD_PATTERN.sub(lambda m: f".{_METHOD_ALIASES[m.group(1)]}(", text)
    text = _MATH_PATTERN.sub(lambda m: f"{_MATH_FUNCS[m.group(1)]}(", text)
    text = _EXTRA_PATTERN.sub(lambda m: f"{_EXTRA_FUNCS[m.group(1)]}(", text)
    text = _IO_PATTERN.sub(lambda m: f"{_IO_ALIASES[m.group(1)]}(", text)
    text = re.sub(r"من\s*\(([^()]+)\)", lambda m: f"isinstance({_replace_type_names(m.group(1))})", text)
    text = _CONSTANT_PATTERN.sub(lambda m: _CONSTANTS[m.group(1)], text)
    for pat, repl in _LOGICAL_PATTERNS:
        text = pat.sub(repl, text)

    for ar, en in _KW_ALIASES.items():
        text = re.sub(rf"(?<!\w){ar}(?=\s*=)", en, text)

    text = re.sub(r"(?<!\w)سهم\s+(.+?):\s*(.+)", lambda m: f"lambda {m.group(1)}: {m.group(2)}", text)
    text = re.sub(r"(.+?)\sإذا\s(.+?)\sوالا\s(.+)", r"\1 if \2 else \3", text)

    for idx in sorted(strings.keys(), reverse=True):
        text = text.replace(f"\x00APL{idx}\x00", strings[idx])
    return text


def transpile_line(line: str) -> str:
    indent = line[: len(line) - len(line.lstrip())]
    stripped = line.strip()

    if not stripped or stripped.startswith("#"):
        return line

    if stripped.startswith("اطبع_بدون"):
        rest = _inline_replace(stripped[len('اطبع_بدون'):].strip())
        return f"{indent}print({rest[1:-1] if rest.startswith('(') else rest}, end='')"

    if stripped.startswith("اطبع"):
        rest = _inline_replace(stripped[4:].strip())
        return f"{indent}print({rest[1:-1] if rest.startswith('(') else rest})"

    if stripped.startswith("الا لو"):
        return f"{indent}elif {_inline_replace(stripped[6:].strip())}"
    if stripped.startswith("الا"):
        rest = _inline_replace(stripped[3:].strip())
        return f"{indent}else{rest}"

    if stripped.startswith("لو"):
        return f"{indent}if {_inline_replace(stripped[2:].strip())}"
    if stripped.startswith("طالما"):
        return f"{indent}while {_inline_replace(stripped[6:].strip())}"

    if stripped.startswith("لكل"):
        rest = stripped[4:].strip()
        if "في" in rest:
            parts = rest.split("في", 1)
            return f"{indent}for {parts[0].strip()} in {_inline_replace(parts[1].strip().lstrip(':').strip())}"
        return f"{indent}for {rest}"

    if stripped.startswith("خاصية"):
        rest = stripped[len('خاصية'):].strip()
        return f"{indent}@property" if not rest else f"{indent}@property {rest}"
    if stripped.startswith("محدد_حذف"):
        rest = stripped[len('محدد_حذف'):].strip()
        return f"{indent}@{rest}.deleter" if rest else f"{indent}@deleter"
    if stripped.startswith("محدد"):
        rest = stripped[len('محدد'):].strip()
        return f"{indent}@{rest}.setter" if rest else f"{indent}@setter"

    if stripped.startswith("دالة"):
        return f"{indent}def {stripped[4:].strip()}"
    if stripped.startswith("ارجع"):
        rest = stripped[4:].strip()
        return f"{indent}return {_inline_replace(rest)}" if rest else f"{indent}return"

    if stripped.startswith("توقف"):
        return f"{indent}break"
    if stripped.startswith("اكمل"):
        return f"{indent}continue"

    if stripped.startswith("حاول"):
        return f"{indent}try:{stripped[5:]}"
    if stripped.startswith("إمسك"):
        rest = _inline_replace(stripped[4:].strip())
        return f"{indent}except {rest}" if rest and rest != ":" else f"{indent}except:"
    if stripped.startswith("امسك"):
        rest = _inline_replace(stripped[4:].strip())
        return f"{indent}except {rest}" if rest and rest != ":" else f"{indent}except:"

    if stripped.startswith("استورد"):
        return f"{indent}import {stripped[7:].strip()}"
    if stripped.startswith("من") and "استورد" in stripped:
        parts = stripped.split("استورد", 1)
        return f"{indent}from {parts[0][2:].strip()} import {parts[1].strip()}"

    if stripped.startswith("تأكد"):
        rest = _inline_replace(stripped[len('تأكد'):].strip())
        if len(rest) >= 2 and rest.startswith("(") and rest.endswith(")"):
            rest = rest[1:-1]
        return f"{indent}assert {rest}"

    if stripped == "اخرج":
        return f"{indent}exit()"
    if stripped.startswith("اخرج") and not stripped.startswith("اخرج(") and stripped[4:5] == " ":
        rest = _inline_replace(stripped[5:].strip())
        return f"{indent}exit({rest})"

    if stripped.startswith("حالة"):
        return f"{indent}match {stripped[len('حالة'):].strip()}"
    if stripped.startswith("قيمة"):
        rest = _inline_replace(stripped[5:].strip())
        if not rest or rest == ":":
            return f"{indent}case:"
        return f"{indent}case {rest}"
    if stripped.startswith("افتراضي"):
        return f"{indent}case _:{stripped[9:]}"

    if stripped.startswith("مع") and "مثل" in stripped:
        parts = stripped[3:].strip().split("مثل", 1)
        left = _inline_replace(parts[0].strip())
        right = parts[1].strip().rstrip(":")
        return f"{indent}with {left} as {right}:"

    if stripped.startswith("المتغير"):
        rest = stripped[7:].strip()
        if "=" in rest:
            parts = rest.split("=", 1)
            return f"{indent}{parts[0].strip()} = {_inline_replace(parts[1].strip())}"
        raise SyntaxError(f"'=' expected after المتغير")

    if stripped.startswith("قاعدة") or stripped.startswith("صنف"):
        return f"{indent}class {stripped[6:].strip() if stripped.startswith('قاعدة') else stripped[4:].strip()}"
    if stripped.startswith("تمرير"):
        return f"{indent}pass"

    if stripped.startswith("خاص المتغير"):
        inner = stripped[11:].strip()
        if "=" in inner:
            parts = inner.split("=", 1)
            return f"{indent}__{parts[0].strip()} = {_inline_replace(parts[1].strip())}"
    if stripped.startswith("خاص دالة"):
        return f"{indent}def __{stripped[len('خاص دالة'):].strip()}"
    if stripped.startswith("عام المتغير"):
        inner = stripped[11:].strip()
        if "=" in inner:
            parts = inner.split("=", 1)
            return f"{indent}{parts[0].strip()} = {_inline_replace(parts[1].strip())}"
    if stripped.startswith("عام دالة"):
        return f"{indent}def {stripped[len('عام دالة'):].strip()}"

    if stripped.startswith("مولد"):
        rest = stripped[4:].strip()
        return f"{indent}yield {_inline_replace(rest)}" if rest else f"{indent}yield"
    if stripped == "حذف" or stripped.startswith("حذف ") or stripped.startswith("حذف\t"):
        return f"{indent}del {stripped[3:].strip()}"
    if stripped.startswith("أبدا"):
        return f"{indent}while True:{stripped[5:]}"

    if stripped.startswith("نسخ ملف"):
        rest = _inline_replace(stripped[len('نسخ ملف'):].strip())
        if "إلى" in rest:
            parts = rest.split("إلى", 1)
            return f"{indent}shutil.copy({parts[0].strip()}, {parts[1].strip()})"
    if stripped.startswith("نقل ملف"):
        rest = _inline_replace(stripped[len('نقل ملف'):].strip())
        if "إلى" in rest:
            parts = rest.split("إلى", 1)
            return f"{indent}shutil.move({parts[0].strip()}, {parts[1].strip()})"
    if stripped.startswith("احذف ملف"):
        return f"{indent}os.remove({stripped[9:].strip()})"
    if stripped.startswith("انشئ مجلد"):
        return f"{indent}os.mkdir({stripped[9:].strip()})"

    return f"{indent}{_inline_replace(stripped)}"


def transpile(source: str) -> str:
    lines = source.split("\n")
    result = []
    for line in lines:
        try:
            result.append(transpile_line(line))
        except SyntaxError as e:
            result.append(f"# ERROR: {e}")
    code = "\n".join(result)

    needs = []
    if "math." in code and "import math" not in code:
        needs.append("import math")
    if "json." in code and "import json" not in code:
        needs.append("import json")
    if "os." in code and "import os" not in code:
        needs.append("import os")
    if "datetime." in code and "import datetime" not in code:
        needs.append("import datetime")
    if "_apl_fetch" in code and "import urllib.request" not in code:
        needs.append("import urllib.request")
    if "random." in code and "import random" not in code:
        needs.append("import random")
    if "time." in code and "import time" not in code:
        needs.append("import time")
    if "shutil." in code and "import shutil" not in code:
        needs.append("import shutil")

    if needs:
        code = "\n".join(needs) + "\n\n" + code
    return code


_RUNTIME = """
import sys
import builtins

_apl_orig_print = builtins.print

def _apl_has_arabic(v):
    return any('\\u0600' <= c <= '\\u06FF' or '\\u0750' <= c <= '\\u07FF' or '\\u08A0' <= c <= '\\u08FF' or '\\uFB50' <= c <= '\\uFDFF' for c in str(v))

def _apl_print(*args, **kwargs):
    if any(_apl_has_arabic(a) for a in args):
        _apl_orig_print('\\u202B', *args, '\\u202C', **kwargs)
    else:
        _apl_orig_print(*args, **kwargs)

builtins.print = _apl_print

_ERROR_AR = {
    "SyntaxError": "خطأ في الصياغة",
    "NameError": "خطأ: متغير غير معروف",
    "TypeError": "خطأ في نوع البيانات",
    "ValueError": "خطأ في القيمة",
    "IndexError": "خطأ: الفهرس خارج النطاق",
    "KeyError": "خطأ: المفتاح غير موجود",
    "ZeroDivisionError": "خطأ: القسمة على صفر",
    "FileNotFoundError": "خطأ: الملف غير موجود",
    "ImportError": "خطأ: استيراد فاشل",
    "AttributeError": "خطأ: الخاصية غير موجودة",
    "EOFError": "خطأ: لا توجد بيانات إدخال",
    "IndentationError": "خطأ: مشكلة في المسافات",
    "StopIteration": "تم التوقف",
    "RuntimeError": "خطأ في التشغيل",
    "PermissionError": "خطأ: صلاحية مرفوضة",
    "TimeoutError": "خطأ: انتهاء الوقت",
    "ConnectionError": "خطأ: فشل الاتصال",
    "OSError": "خطأ: نظام التشغيل",
    "OverflowError": "خطأ: تجاوز السعة",
    "RecursionError": "خطأ: استدعاء متكرر عميق",
    "ModuleNotFoundError": "خطأ: الوحدة غير موجودة",
    "AssertionError": "خطأ: التأكيد فشل",
    "KeyboardInterrupt": "توقف بواسطة المستخدم",
}

_old_excepthook = sys.excepthook
def _apl_excepthook(typ, val, tb):
    name = _ERROR_AR.get(typ.__name__, typ.__name__)
    import traceback
    traceback.print_exception(typ, val, tb)
    sys.stderr.write(f"\\u202B{name}: {val}\\u202C\\n")
sys.excepthook = _apl_excepthook

def _apl_read(f):
    return f.read()

def _apl_write(f, s):
    return f.write(s)

def _apl_close(f):
    f.close()

def _apl_fetch(url):
    return urllib.request.urlopen(url).read().decode("utf-8")
"""


def run_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
    python_code = _RUNTIME + "\n" + transpile(source)
    try:
        exec(python_code, {})
    except Exception as e:
        msg = _get_error_ar(e)
        print(f"\u202B{msg}\u202C", file=sys.stderr)


def _get_error_ar(e: Exception) -> str:
    name = type(e).__name__
    ar_name = {
        "SyntaxError": "خطأ في الصياغة",
        "NameError": "خطأ: متغير غير معروف",
        "TypeError": "خطأ في نوع البيانات",
        "ValueError": "خطأ في القيمة",
        "IndexError": "خطأ: الفهرس خارج النطاق",
        "KeyError": "خطأ: المفتاح غير موجود",
        "ZeroDivisionError": "خطأ: القسمة على صفر",
        "FileNotFoundError": "خطأ: الملف غير موجود",
        "ImportError": "خطأ: استيراد فاشل",
        "AttributeError": "خطأ: الخاصية غير موجودة",
        "EOFError": "خطأ: لا توجد بيانات إدخال",
        "IndentationError": "خطأ: مشكلة في المسافات",
        "RuntimeError": "خطأ في التشغيل",
        "PermissionError": "خطأ: صلاحية مرفوضة",
        "OSError": "خطأ: نظام التشغيل",
        "ConnectionError": "خطأ: فشل الاتصال",
        "ModuleNotFoundError": "خطأ: الوحدة غير موجودة",
        "OverflowError": "خطأ: تجاوز السعة",
    }.get(name, name)
    return f"{ar_name}: {e}"


def transpile_to_code(source: str) -> str:
    return transpile(source)


def main():
    if len(sys.argv) < 2:
        print("APL - Ammar Programming Language")
        print("Usage: apl <file.apl>")
        print()
        print("Commands:")
        for cmd in [
            "المتغير x = y       - متغير",
            "اطبع / اطبع_بدون     - طباعة",
            "ادخل(...)            - إدخال",
            "لو / الا لو / الا    - شرط",
            "سإذا شرط والا ص     - شرط ثلاثي",
            "طالما شرط:           - while",
            "لكل x في y:          - for",
            "دالة / ارجع          - function / return",
            "سهم x, y: expr       - lambda",
            "مولد / توقف / اكمل   - yield / break / continue",
            "حاول / إمسك          - try / except",
            "تأكد(شرط)            - assert",
            "خاصية / محدد / محدد_حذف - property/setter/deleter",
            "صنف/قاعدة / تمرير    - class / pass",
            "خاص / عام            - private / public",
            "حالة / قيمة / افتراضي - match / case",
            "مع .. مثل            - with .. as",
            "حذف / أبدا           - del / while True",
            "اخرج(0)              - exit",
            "نسخ ملف / نقل ملف    - shutil.copy/move",
            "حجم ملف / قائمة ملفات - os.path.getsize/listdir",
            "احذف ملف / انشئ مجلد - os.remove/mkdir",
            "استورد / من..استورد   - import",
            "فتح / اقرأ / اكتب / اغلق - ملفات",
            "طلب(url)             - HTTP",
            "جسون / جسون_تحويل    - JSON",
            "الساعة / التاريخ     - وقت/تاريخ",
            "كل / أي / خريطة / فلترة / تجميع - all/any/map/filter/zip",
            "عشوائي / نوع / عدد   - random.choice/type/enumerate",
            "انتظر(ثوان) / وقت()  - time.sleep/time.time",
            "تمثيل / ثنائي / سداسي / ترتيب / رمز - repr/bin/hex/ord/chr",
            "من(س, نوع)           - isinstance",
            "صحيح/نص/عشري/منطق   - int/str/float/bool",
            "قائمة/مجموعة/مصفوفة/قاموس - list/tuple/set/dict",
            "نطاق/طول / عدد      - range/len/enumerate",
            "مطلق/قوة/جذر        - abs/pow/sqrt",
            "أكبر/أصغر/مقرب      - max/min/round",
            "مجموع/مفرز          - sum/sorted",
            ".تقسيم/.أضف/.ضم     - .split/.append/.join",
            ".علوي/.سفلي/.تقليم  - .upper/.lower/.strip",
            ".استبدال/.بداية/.نهاية - .replace/.startswith/.endswith",
            ".اتحاد/.تقاطع/.فرق   - .union/.intersection/.difference",
            "و / أو / ليس / مثل / في - and/or/not/as/in",
            "ط / ه                - math.pi / math.e",
            "صواب / خطأ / لا_شيء  - True / False / None",
        ]:
            print(f"  {cmd}")
        return

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Error: file '{filepath}' not found")
        sys.exit(1)

    run_file(filepath)


if __name__ == "__main__":
    main()

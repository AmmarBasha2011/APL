"""
APL - Transpile Dispatch
"""

import re
from core.apl_runner.patterns import _TYPE_NAMES, _UDF_NAMES
from core.apl_runner.inline_replacer import _inline_replace

# Arabic decorator names -> Python decorators
# Bare "@اسم" (no call parens) on a function is a pass-through decorator.
_APL_IDENTITY = "_apl_passthrough_decorator"

# Decorators that require a function argument, so a bare @اسم cannot use them
_NEEDS_FUNC_ARG = {"functools.wraps", "functools.total_ordering",
                   "functools.singledispatch", "functools.cached_property"}


_DECORATOR_ALIASES = {
    "يلتف": "functools.wraps",
    "تغليف_دالة": "functools.wraps",
    "كاش_دالة": "functools.cache",
    "كاش_مؤقت_دالة": "functools.lru_cache",
    "ترتيب_كامل": "functools.total_ordering",
    "توزيع_فردي": "functools.singledispatch",
    "خاصية_مخزنة_دالة": "functools.cached_property",
    "فئة_بيانات": "dataclass",
    "dataclass": "dataclass",
}


def transpile_line(line: str) -> str:
    """Translate a single line of APL code to Python"""
    indent = line[: len(line) - len(line.lstrip())]
    stripped = line.strip()

    if not stripped or stripped.startswith("#"):
        return line

    # Handle context managers FIRST (before any library patterns)
    if stripped.startswith(("مع ", "with ", "ضمنياً ", "ضمني ")):
        match = re.match(r'(?:مع|with|ضمنياً|ضمني)\s+(.+?)\s+(?:مثل|as|كـ|يساوي)\s+(\w+)\s*:', stripped)
        if match:
            expr = _inline_replace(match.group(1).strip())
            var = _inline_replace(match.group(2).strip())
            return f"{indent}with {expr} as {var}:"
    
    # Handle generators (yield/yield from)
    if stripped.startswith(("ولد ", "ولّد ", "yield ")):
        rest = stripped.split(" ", 1)[1] if " " in stripped else "None"
        return f"{indent}yield {_inline_replace(rest)}"
    if stripped.startswith(("ولد_من ", "yield_from ", "ولّد_من ")):
        rest = stripped.split(" ", 1)[1] if " " in stripped else ""
        return f"{indent}yield from {_inline_replace(rest)}"
    
    # Handle semicolons - split multiple statements on one line
    if ";" in stripped and not stripped.startswith(("اطبع", "#", "'''", '"""')):
        parts = stripped.split(";")
        results = []
        for part in parts:
            if part.strip():
                # Recursively transpile each part
                results.append(transpile_line(part))
        return "\n".join(results)

    # Remove trailing semicolon if present
    if stripped.endswith(";"):
        stripped = stripped[:-1].strip()

    if stripped.startswith("اطبع_بدون"):
        rest = _inline_replace(stripped[len('اطبع_بدون'):].strip())
        args = rest
        if args.startswith("(") and args.endswith(")"):
            args = args[1:-1]
        return f"{indent}print({args}, end='')"

    if stripped.startswith("اطبع"):
        rest = _inline_replace(stripped[4:].strip())
        if rest.startswith("(") and rest.endswith(")"):
            rest = rest[1:-1]
        return f"{indent}print({rest})"

    if stripped.startswith("الا لو"):
        return f"{indent}elif {_inline_replace(stripped[6:].strip())}"
    if stripped.startswith("الا"):
        rest = _inline_replace(stripped[3:].strip())
        return f"{indent}else{rest}"

    # Class methods: "اسم(self, ...):" -> "def اسم(self, ...):"
    m = re.match(r"^(\w+)\s*\((self|\s*self)\s*(.*)\)\s*:\s*$", stripped)
    if m and not stripped.startswith((" def", "def", "if", "for", "while", "return", "print")):
        name, params, rest = m.group(1), m.group(2), m.group(3)
        rest = re.sub(r"\bself\b", "self", rest)
        return f"{indent}def {name}({params}{rest}):"

    # Block-level conditional keywords (before generic inline substitution)
    # else / else-if (block level)
    if stripped == "والا" or stripped.startswith("والا:") or stripped.startswith("والا "):
        rest = stripped[4:].strip()
        return f"{indent}else{':' if not rest or rest == ':' else rest}"
    if stripped.startswith("والا_لو") or stripped.startswith("والا لو"):
        cond = stripped.split("لو", 1)[1].strip()
        return f"{indent}else:\n{indent}    if {_inline_replace(cond)}"

    if stripped.startswith("س إذا"):
        rest = stripped.split("شرط", 1)[1].strip() if "شرط" in stripped else stripped[4:].strip()
        return f"{indent}elif {_inline_replace(rest)}"
    if stripped.startswith("سإذا"):
        rest = stripped.split("شرط", 1)[1].strip() if "شرط" in stripped else stripped[4:].strip()
        return f"{indent}elif {_inline_replace(rest)}"
    if stripped.startswith("إذا"):
        rest = stripped[3:].strip()
        return f"{indent}if {_inline_replace(rest)}"
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

    # Decorators: @اسم  ->  @python_name
    if stripped.startswith("@"):
        name = stripped[1:].strip()
        if "(" in name:
            head, _, tail = name.partition("(")
            mapped = _DECORATOR_ALIASES.get(head, head)
            return f"{indent}@{mapped}({tail.rstrip(')')})"
        if name in _DECORATOR_ALIASES:
            mapped = _DECORATOR_ALIASES[name]
            if mapped in _NEEDS_FUNC_ARG:
                return f"{indent}@{_APL_IDENTITY}"
            return f"{indent}@{mapped}"
        # user-defined decorator: the @اسم refers to their own function
        return f"{indent}@_APL_UDF_{name}"

    if stripped.startswith("خاصية"):
        rest = stripped[len('خاصية'):].strip()
        return f"{indent}@property" if not rest else f"{indent}@property {rest}"
    if stripped.startswith("محدد_حذف"):
        rest = stripped[len('محدد_حذف'):].strip()
        return f"{indent}@{rest}.deleter" if rest else f"{indent}@deleter"
    if stripped.startswith("محدد"):
        rest = stripped[len('محدد'):].strip()
        return f"{indent}@{rest}.setter" if rest else f"{indent}@setter"

    if ((stripped.startswith("دالة_") or stripped.startswith("_apl_udf_دالة_"))
            and "(" in stripped) or stripped.startswith("دالة ") \
            or (stripped.startswith("دالة(") and False):
        # "دالة_اسم(...)" / "_apl_udf_دالة_اسم(...)" keep the full identifier;
        # "دالة اسم(...)" strips the keyword.
        if stripped.startswith("دالة "):
            rest = stripped[4:].strip()
        elif stripped.startswith("دالة_"):
            rest = stripped
        else:
            rest = stripped
        mname = re.match(r"^([^\s(]+)", rest)
        if not rest or rest.startswith("("):
            # nameless "دالة(...)" is not a valid definition
            return f"{indent}pass"
        # constructor:  دالة_إنشاء(ذات, ...)  ->  def __init__(self, ...)
        if rest.startswith("دالة_إنشاء(") or rest.startswith("دالة إنشاء("):
            body = rest[rest.index("(") + 1:rest.rindex(")")]
            params = body.strip()
            if not params.startswith("ذات") and not params.startswith("self"):
                params = ("ذات, " + params) if params else "ذات"
            return f"{indent}def __init__({params}):"
        # Translate type hints in function signature
        for arabic_type, english_type in _TYPE_NAMES.items():
            rest = re.sub(rf':\s*{arabic_type}(?=[^\w])', f': {english_type}', rest)
            rest = re.sub(rf'->\s*{arabic_type}(?=[^\w])', f'-> {english_type}', rest)
        return f"{indent}def {rest}"
    if stripped.startswith("ارجع"):
        rest = stripped[4:].strip()
        return f"{indent}return {_inline_replace(rest)}" if rest else f"{indent}return"

    if stripped.startswith("توقف"):
        return f"{indent}break"
    if stripped.startswith("اكمل"):
        return f"{indent}continue"

    if stripped.startswith("حاول"):
        return f"{indent}try:{stripped[5:]}"
    if stripped.startswith("أخيراً") or stripped.startswith("أخيرا") or stripped.startswith("في_الاخير"):
        rest = stripped.split(":", 1)[1] if ":" in stripped else ""
        return f"{indent}finally:{rest}"
    if stripped.startswith("خطأ_في") or stripped.startswith("استثناء"):
        rest = stripped.split(":", 1)[1] if ":" in stripped else ""
        return f"{indent}except{rest}"
    for _kw in ("إمسك", "امسك", "خطأ_في"):
        if stripped.startswith(_kw):
            rest = _inline_replace(stripped[len(_kw):].strip())
            if not rest or rest == ":":
                return f"{indent}except:"
            # "إمسك مثل خطأ:" -> "except ... خطأ:"  (Arabic exception variable)
            m = re.match(r"^(?:مثل|كـ|اسـ|as)\s+([\w\u0600-\u06FF]+)\s*:?$", rest)
            if m:
                return f"{indent}except Exception as {m.group(1)}:"
            return f"{indent}except {rest}"

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
    # match/case: "قيمة <pattern>:"  -- must be followed by space/colon, never "="
    _apl_case = re.match(r"^قيمة(?:\s+(.*))?\s*:\s*$", stripped)
    if _apl_case or stripped.rstrip() == "قيمة:":
        rest = _inline_replace((_apl_case.group(1) if _apl_case else "").strip())
        if not rest:
            return f"{indent}case _:"
        # Support guard clauses: "قيمة ن لو ن > 0:" → "case ن if ن > 0:"
        if "لو" in rest:
            parts = rest.split("لو", 1)
            pattern = parts[0].strip()
            guard = parts[1].strip().rstrip(":")
            return f"{indent}case {pattern} if {guard}:"
        return f"{indent}case {rest}:"
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

    # class definitions: "صنف اسم:" or "قاعدة اسم:" (a class database helper)
    _m = re.match(r"^(صنف|قاعدة)\s+([^\s:(]+(?:\([^)]*\))?)\s*:\s*$", stripped)
    if _m:
        return f"{indent}class {_m.group(2)}:"
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

"""
APL - Transpile Dispatch
"""

import re
from core.apl_runner.patterns import _TYPE_NAMES
from core.apl_runner.inline_replacer import _inline_replace


def transpile_line(line: str) -> str:
    """Translate a single line of APL code to Python"""
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
        rest = stripped[4:].strip()
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
        # Support guard clauses: "قيمة ن لو ن > 0:" → "case ن if ن > 0:"
        if "لو" in rest:
            parts = rest.split("لو", 1)
            pattern = parts[0].strip()
            guard = parts[1].strip().rstrip(":")
            return f"{indent}case {pattern} if {guard}:"
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

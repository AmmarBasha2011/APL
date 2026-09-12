"""
APL - Patterns & Constants
All regex patterns, type aliases, and transpilation mappings
"""

import re

# Type aliases - أنواع البيانات
TYPE_ALIASES = {
    "صحيح": "int", "نص": "str", "عشري": "float", "منطق": "bool",
    "قائمة": "list", "مجموعة": "tuple", "مصفوفة": "set",
    "قاموس": "dict", "بايت": "bytes",
}
_TYPE_PATTERN = re.compile("(" + "|".join(TYPE_ALIASES.keys()) + r")\s*\(")

# Inline functions - الدوال المضمنة
_INLINE_FUNCS = {"نطاق": "range", "طول": "len"}
_INLINE_FUNC_PATTERN = re.compile("(" + "|".join(_INLINE_FUNCS.keys()) + r")\s*\(")

# Method aliases - أسماء الدوال البديلة
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

# Type names for isinstance()
_TYPE_NAMES = {
    "صحيح": "int", "نص": "str", "عشري": "float", "منطق": "bool",
    "قائمة": "list", "مجموعة": "tuple", "مصفوفة": "set",
    "قاموس": "dict", "بايت": "bytes",
}

# Constants - الثوابت
_CONSTANTS = {
    "صواب": "True", "خطأ": "False", "لا_شيء": "None",
    "ط": "math.pi", "ه": "math.e",
    "تاو": "math.tau", "لانهائي_موجب": "math.inf",
}
_CONSTANT_PATTERN = re.compile(r"(?<!\w)(" + "|".join(_CONSTANTS.keys()) + r")(?!\w)")

# Logical patterns - العوامل المنطقية
_LOGICAL_PATTERNS = [
    (re.compile(r"(?<!\w)و(?!\w)"), "and"),
    (re.compile(r"(?<!\w)أو(?!\w)"), "or"),
    (re.compile(r"(?<!\w)ليس(?!\w)"), "not"),
    (re.compile(r"(?<!\w)مثل(?!\w)"), "as"),
    (re.compile(r"(?<!\w)في(?!\w)"), "in"),
]

# Keyword arguments - حجج الكلمات المفتاحية
_KW_ALIASES = {
    "ترميز": "encoding",
    "تأكد_من_ascii": "ensure_ascii",
    "مسافة_بادئة": "indent",
}

# I/O aliases - إدخال/إخراج
_IO_ALIASES = {
    "اقرأ": "_apl_read",
    "اكتب": "_apl_write",
    "اغلق": "_apl_close",
    "طلب": "_apl_fetch",
}
_IO_PATTERN = re.compile("(" + "|".join(_IO_ALIASES.keys()) + r")\s*\(")

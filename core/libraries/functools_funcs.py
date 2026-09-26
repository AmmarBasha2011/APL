"""
APL - functools Library Functions
Transpiles Arabic keywords to Python functools module
"""

FUNCTOOLS_FUNCS = {
    "@تغليف_دالة": "functools.wraps",
    "تغليف_دالة": "functools.wraps",
    "جزئي_دالة": "functools.partial",
    "كاش_مؤقت_دالة": "functools.lru_cache",
    "كاش_بلا_حد": "functools.cache",
    "مقارن_بالعكس": "functools.cmp_to_key",
    "اختصر_دالة": "functools.reduce",
    "تعيين_ترتيب": "functools.total_ordering",
    "أقوى_قيمة": "functools.reduce",
}

FUNCTOOLS_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(FUNCTOOLS_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
FUNCTOOLS_HELP = [
    "# functools - أدوات الدوال",
    "تغليف_دالة(دالة)               - wraps للـ decorators",
    "جزئي_دالة(دالة, ...)           - partial لتثبيت وسائط",
    "كاش_مؤقت_دالة(عدد=128)         - lru_cache للتخزين المؤقت",
    "كاش_بلا_حد(دالة)                - cache بدون حد",
    "مقارن_بالعكس(دالة)             - cmp_to_key للترتيب",
]

# Import detection
IMPORT_NAME = "functools"
IMPORT_CHECK = r"functools\."
IMPORT_STATEMENT = "import functools"

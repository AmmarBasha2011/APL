"""
APL - Itertools Library Functions
Transpiles Arabic itertools keywords to Python itertools module calls
"""

ITERTOOLS_FUNCS = {
    # مكررات لا نهائية (Infinite Iterators)
    "عد_لا نهائي": "itertools.count",
    "تكرار_لا نهائي": "itertools.cycle",
    "كرر_لا نهائي": "itertools.repeat",
    "مدى_لا نهائي": "itertools.count",
    
    # مكررات منتهية (Finite Iterators)
    "تجميع": "itertools.chain",
    "تجميع_من_قوائم": "itertools.chain.from_iterable",
    "ضغط": "itertools.compress",
    "فلترة_خاطئة": "itertools.filterfalse",
    "قطّع": "itertools.islice",
    "اقطع": "itertools.islice",
    
    # توليفات (Combinatoric)
    "توافيق_مع_إرجاع": "itertools.combinations_with_replacement",
    "ناتج_ديكارتي": "itertools.product",
    "تباديل_مع_إرجاع": "itertools.product",
    
    # تجميع (Grouping)
    "اجمع_مفتاح": "itertools.groupby",
    
    # مساعدة (Helpers)
    "تراكم": "itertools.accumulate",
    "زوجي": "itertools.zip_longest",
    "سلسلة": "itertools.chain",
    "فلتر": "filter",
    "خريطة": "map",
}

ITERTOOLS_PATTERN = r"(?<!\w)(" + "|".join(sorted(ITERTOOLS_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
ITERTOOLS_HELP = [
    "# مكررات لا نهائية (Infinite Iterators)",
    "عد_لا نهائي(بداية, خطوة) - عد لا نهائي",
    "تكرار_لا نهائي(تسلسل)    - تكرار لا نهائي",
    "كرر_لا نهائي(قيمة, مرة) - تكرار قيمة",
    "# مكررات منتهية (Finite Iterators)",
    "تجميع(ت1, ت2, ...)      - تجميع المكررات",
    "تجميع_من_قوائم(قوائم)    - تجميع قوائم",
    "ضغط(بيانات, أقنعة)      - ضغط",
    "فلترة_خاطئة(د, بيانات)  - فلترة خاطئة",
    "قطّع(مكرر, بداية, نهاية) - قطعة",
    "# توليفات (Combinatoric)",
    "ناتج_ديكارتي(ت1, ت2)   - ناتج ديكارتي",
    "توافيق_مع_إرجاع(ت, ر)  - توافيق مع إرجاع",
    "تباديل_مع_إرجاع(ت1, ت2) - تباديل مع إرجاع",
    "# مساعدة (Helpers)",
    "تراكم(مكرر)             - تراكمي",
    "زوجي(ت1, ت2, حشو)      - زوجي",
    "اجمع_مفتاح(مكرر, مفتاح)  - تجميع بمفتاح",
    "# دوال مضمنة بديلة (Alternative Built-ins)",
    "فلتر(د, تسلسل)         - فلتر",
    "خريطة(د, تسلسل)         - خريطة",
    "سلسلة(ت1, ت2, ...)      - سلسلة",
]

# Import detection
IMPORT_NAME = "itertools"
IMPORT_CHECK = "itertools\."
IMPORT_STATEMENT = "import itertools"

"""
APL - decimal Library Functions
Transpiles Arabic keywords to Python decimal module
"""

DECIMAL_FUNCS = {
    "عشري_دقيق": "decimal.Decimal",
    "من_نص_عشري": "decimal.Decimal",
    "من_كسر_عشري": "decimal.Decimal",
    "من_عدد_عشري": "decimal.Decimal",
    "سياق_العشري": "decimal.getcontext",
    "سياق_محلي": "decimal.localcontext",
    "اجمع_عشري": "_apl_decimal_add",
    "اطرح_عشري": "_apl_decimal_sub",
    "اضرب_عشري": "_apl_decimal_mul",
    "اقسم_عشري": "_apl_decimal_div",
    "اقسم_باقي_عشري": "_apl_decimal_mod",
    "اس_عشري": "_apl_decimal_pow",
    "جذر_عشري": "_apl_decimal_sqrt",
    "مقارنة_عشري": "_apl_decimal_cmp",
    "نسخ_عشري": "_apl_decimal_copy",
    "قرّب_عشري": "_apl_decimal_quantize",
    "بدقة_عشري": "_apl_decimal_fma",
}

DECIMAL_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(DECIMAL_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

DECIMAL_CONSTANTS = {
    "نقطة_عشرية": "decimal.getcontext().prec",
    "اقرب_لأسفل": "decimal.ROUND_DOWN",
    "اقرب_لأعلى": "decimal.ROUND_UP",
    "اقرب_منتصف": "decimal.ROUND_HALF_UP",
    "اقرب_سقف": "decimal.ROUND_CEILING",
    "اقرب_أرض": "decimal.ROUND_FLOOR",
    "أقصى_دقة": "decimal.MAX_PREC",
}

DECIMAL_CONSTANT_PATTERN = r"(?<![\w.\u0600-\u06FF])(" + "|".join(sorted(DECIMAL_CONSTANTS.keys(), key=len, reverse=True)) + r")(?![\w\u0600-\u06FF])"

# Help text for CLI
DECIMAL_HELP = [
    "# decimal - الحساب العشري الدقيق (بدون أخطاء تقريب)",
    "عشري_دقيق(نص)        - تحويل نص إلى رقم عشري دقيق",
    "من_نص_عشري('3.14')   - نص -> Decimal",
    "اجمع_عشري(أ, ب)       - جمع دقيق",
    "اقسم_عشري(أ, ب, دقة)  - قسمة بتحديد الخانات",
    "مقارنة_عشري(أ, ب)    - نتيجة المقارنة",
    "# ثوابت: تقريب_لأسفل, تقريب_لأعلى, تقريب_منتصف, أقصى_دقة",
]

# Import detection
IMPORT_NAME = "decimal"
IMPORT_CHECK = r"decimal\."
IMPORT_STATEMENT = "import decimal"

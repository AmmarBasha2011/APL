"""
APL - fractions Library Functions
Transpiles Arabic keywords to Python fractions module
"""

FRACTIONS_FUNCS = {
    "كسر": "fractions.Fraction",
    "من_عددين": "fractions.Fraction",
    "من_نص_كسر": "fractions.Fraction",
    "قيمة_كسر": "_apl_fraction_value",
    "مقلوب_كسر": "_apl_fraction_recip",
}

FRACTIONS_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(FRACTIONS_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

FRACTIONS_METHODS = {
    "حد_المقام": "limit_denominator",
}

FRACTIONS_METHOD_PATTERN = r"\.(" + "|".join(sorted(FRACTIONS_METHODS.keys(), key=len, reverse=True)) + r")\s*\("

FRACTIONS_PROPS = {
    "بسط_كسر": "numerator",
    "مقام_كسر": "denominator",
}

FRACTIONS_PROP_PATTERN = r"\.(" + "|".join(sorted(FRACTIONS_PROPS.keys(), key=len, reverse=True)) + r")(?=\b)"

# Help text for CLI
FRACTIONS_HELP = [
    "# fractions - الكسور الرياضية الدقيقة",
    "كسر(1, 3)             - كسر 1/3",
    "من_عددين(3, 6)        - يبسّط إلى 1/2",
    "كسر.بسط_كسر           - البسط",
    "كسر.مقام_كسر          - المقام",
    "قيمة_كسر(كسر)        - تحويل إلى float",
]

# Import detection
IMPORT_NAME = "fractions"
IMPORT_CHECK = r"fractions\."
IMPORT_STATEMENT = "import fractions"

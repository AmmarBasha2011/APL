"""
APL - pprint Library Functions
Transpiles Arabic keywords to Python pprint module
"""

PPRINT_FUNCS = {
    "طباعة_جميلة": "pprint.pprint",
    "طباعة_نص_جميل": "pprint.pformat",
}

PPRINT_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(PPRINT_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
PPRINT_HELP = [
    "# pprint - طباعة القواميس والقوائم بشكل مقروء",
    "طباعة_جميلة(قاموس)  - طباعة منسّقة",
    "طباعة_نص_جميل(قائمة) - إرجاع النص المنسّق كسلسلة",
]

# Import detection
IMPORT_NAME = "pprint"
IMPORT_CHECK = r"pprint\."
IMPORT_STATEMENT = "import pprint"

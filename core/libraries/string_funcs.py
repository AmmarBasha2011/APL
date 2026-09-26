"""
APL - string Library Functions
Transpiles Arabic keywords to Python string module
"""

STRING_FUNCS = {
    "أحرف_كبيرة_أول_كل_كلمة": "string.capwords",
    "قالب_نص": "string.Template",
}

STRING_CONSTANTS = {
    "حروف_انجليزية": "string.ascii_letters",
    "حروف_صغيرة_ثابتة": "string.ascii_lowercase",
    "حروف_كبيرة_ثابتة": "string.ascii_uppercase",
    "أرقام_ثابتة": "string.digits",
    "رموز_خاصة": "string.punctuation",
    "حروف_سداسية": "string.hexdigits",
    "حروف_قابلة_للطباعة": "string.printable",
    "مسافات_بيضاء": "string.whitespace",
}

STRING_CONSTANT_PATTERN = r"(?<![\w.\u0600-\u06FF])(" + "|".join(sorted(STRING_CONSTANTS.keys(), key=len, reverse=True)) + r")(?![\w\u0600-\u06FF])"

STRING_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(STRING_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
STRING_HELP = [
    "# string - مجموعات الأحرف الثابتة",
    "حروف_انجليزية         - a-zA-Z",
    "أرقام_ثابتة          - 0-9",
    "رموز_خاصة            - علامات الترقيم",
    "أحرف_كبيرة_أول_كل_كلمة(نص) - Capitalize Each Word",
    "قالب_نص(نص)          - قالب بdollar replacements",
]

# Import detection
IMPORT_NAME = "string"
IMPORT_CHECK = r"string\."
IMPORT_STATEMENT = "import string"

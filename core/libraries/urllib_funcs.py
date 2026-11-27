"""
APL - urllib Library Functions
Transpiles Arabic keywords to Python urllib module
"""

URLLIB_FUNCS = {
    "فك_ترميز_الرابط_كامل": "urllib.parse.unquote_plus",
}

URLLIB_PATTERN = r"(?<![\w.\u0600-\u06FF])(" + "|".join(sorted(URLLIB_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
URLLIB_HELP = [
    "# urllib - التعامل مع الروابط (parse + request)",
    "ترميز_الرابط(نص)                - encode للنص",
    "فك_ترميز_الرابط(نص)             - decode",
    "تحليل_الرابط(رابط)              - urlparse (مخطط/نطاق/مسار)",
    "نطاق_الرابط(رابط)               - نفس الدالة (اسم بديل)",
    "بناء_الرابط(قاموس)               - urlencode",
    "تحليل_استعلام('a=1&b=2')        - parse_qs",
    "حمّل_الرابط(رابط)                - فتح الرابط",
]

# Import detection
IMPORT_NAME = "urllib"
IMPORT_CHECK = r"urllib\."
IMPORT_STATEMENT = "import urllib.parse, urllib.request"

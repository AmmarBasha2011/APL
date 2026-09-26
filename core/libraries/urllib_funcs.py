"""
APL - urllib Library Functions
Transpiles Arabic keywords to Python urllib module
"""

URLLIB_FUNCS = {
    "ترميز_الرابط": "urllib.parse.quote",
    "فك_ترميز_الرابط": "urllib.parse.unquote",
    "ترميز_الرابط_كامل": "urllib.parse.quote_plus",
    "فك_ترميز_الرابط_كامل": "urllib.parse.unquote_plus",
    "تحليل_الرابط": "urllib.parse.urlparse",
    "نطاق_الرابط": "urllib.parse.urlparse",
    "بناء_الرابط": "urllib.parse.urlencode",
    "بناء_الرابط_من_قاموس": "urllib.parse.urlencode",
    "تحليل_استعلام": "urllib.parse.parse_qs",
    "تحليل_استعلام_نص": "urllib.parse.parse_qsl",
    "حمّل_الرابط": "urllib.request.urlopen",
    "استخدم_وكيل": "urllib.request.Request",
    "وكيل_المتصفح": "urllib.request.Request",
}

URLLIB_PATTERN = r"(?<!\w)(" + "|".join(sorted(URLLIB_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

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

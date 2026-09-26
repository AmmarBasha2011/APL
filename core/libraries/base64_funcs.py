"""
APL - base64 Library Functions
Transpiles Arabic keywords to Python base64 module
"""

BASE64_FUNCS = {
    "ترميز_قاعد64": "base64.b64encode",
    "فك_ترميز_قاعد64": "base64.b64decode",
    "ترميز_آمن_للروابط": "base64.urlsafe_b64encode",
    "فك_ترميز_آمن": "base64.urlsafe_b64decode",
    "ترميز_أسطر": "base64.encodebytes",
    "فك_ترميز_أسطر": "base64.decodebytes",
    "ترميز_سداسي": "base64.b16encode",
    "فك_ترميز_سداسي": "base64.b16decode",
    "ترميز_أساس_32": "base64.b32encode",
    "فك_ترميز_أساس_32": "base64.b32decode",
}

BASE64_PATTERN = r"(?<!\w)(" + "|".join(sorted(BASE64_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
BASE64_HELP = [
    "# base64 - الترميز وفك الترميز (تتطلب bytes وليس str)",
    "ترميز_قاعد64(نص.encode('utf-8'))  - ترميز base64",
    "فك_ترميز_قاعد64(بيانات)           - فك الترميز",
    "ترميز_آمن_للروابط(بيانات)         - ترميز آمن للروابط URL",
    "ترميز_سداسي(بيانات)               - ترميز Base16",
]

# Import detection
IMPORT_NAME = "base64"
IMPORT_CHECK = r"base64\."
IMPORT_STATEMENT = "import base64"

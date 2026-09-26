"""
APL - getpass Library Functions
Transpiles Arabic keywords to Python getpass module
"""

GETPASS_FUNCS = {
    "كلمة_سر_مخفية": "getpass.getpass",
    "اسم_المستخدم_الحالي": "getpass.getuser",
}

GETPASS_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(GETPASS_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
GETPASS_HELP = [
    "# getpass - إدخال كلمات السر دون إظهارها",
    "كلمة_سر_مخفية('كلمة السر: ')  - إدخال مخفي",
    "اسم_المستخدم_الحالي()       - اسم مستخدم النظام",
]

# Import detection
IMPORT_NAME = "getpass"
IMPORT_CHECK = r"getpass\."
IMPORT_STATEMENT = "import getpass"

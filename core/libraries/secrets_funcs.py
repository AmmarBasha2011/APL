"""
APL - secrets Library Functions
Transpiles Arabic keywords to Python secrets module
"""

SECRETS_FUNCS = {
    "سر_سداسي": "secrets.token_hex",
    "سر_آمن_لرابط": "secrets.token_urlsafe",
    "سر_بايتات": "secrets.token_bytes",
      "سر_حددي": "secrets.token_int",
    "سر_في_مجال": "_apl_secret_int",
    "اختر_عشوائي": "secrets.choice",
    "مقارنة_آمنة": "secrets.compare_digest",
    "مصدر_عشوائي_آمن": "secrets.SystemRandom",
}

SECRETS_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(SECRETS_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
SECRETS_HELP = [
    "# secrets - توليد قيم عشوائية آمنة (cryptographically secure)",
    "سر_سداسي(16)          - 16 بايت عشوائية كـ hex",
    "سر_آمن_لرابط(32)      - token آمن للروابط",
    "اختر_عشوائي(قائمة)     - عنصر عشوائي من قائمة",
    "مقارنة_آمنة(أ, ب)     - مقارنة بزمن ثابت",
]

# Import detection
IMPORT_NAME = "secrets"
IMPORT_CHECK = r"secrets\."
IMPORT_STATEMENT = "import secrets"

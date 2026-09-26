"""
APL - uuid Library Functions
Transpiles Arabic keywords to Python uuid module
"""

UUID_FUNCS = {
    "معرف_فريد": "uuid.uuid4",
    "معرف_نص": "str",
    "معرف_عشوائي": "uuid.uuid4",
    "معرف_زمني": "uuid.uuid1",
    "معرف_بالاسم": "uuid.uuid3",
    "معرف_من_نص": "uuid.UUID",
    "معرف_فارغ": "uuid.UUID",
}

UUID_PATTERN = r"(?<!\w)(" + "|".join(sorted(UUID_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

UUID_CONSTANTS = {
    "نطاق_دنس": "uuid.NAMESPACE_DNS",
    "نطاق_رابط": "uuid.NAMESPACE_URL",
    "نطاق_معرف": "uuid.NAMESPACE_OID",
    "نطاق_شهادة": "uuid.NAMESPACE_X500",
}

UUID_CONSTANT_PATTERN = r"(?<![\w.\u0600-\u06FF])(" + "|".join(sorted(UUID_CONSTANTS.keys(), key=len, reverse=True)) + r")(?![\w\u0600-\u06FF])"

UUID_PROPS = {
    "نسخة_المعرف": "version",
    "معرف_النسخة": "version",
}

UUID_PROP_PATTERN = r"\.(" + "|".join(sorted(UUID_PROPS.keys(), key=len, reverse=True)) + r")(?=\b)"

# Help text for CLI
UUID_HELP = [
    "# uuid - المعرفات الفريدة (UUID)",
    "معرف_فريد()                    - معرف UUID v4 عشوائي",
    "معرف_نص()                      - نفس الدالة (اسم بديل)",
    "معرف_زمني()                    - معرف v1 مبني على الوقت",
    "معرف_بالاسم(نطاق_دن��, اسم)     - معرف ثابت v3 مشتق من نص",
    "معرف_من_نص('...')              - تحويل نص إلى كائن UUID",
    "# خاصية: كائن.نسخة_المعرف",
]

# Import detection
IMPORT_NAME = "uuid"
IMPORT_CHECK = r"uuid\."
IMPORT_STATEMENT = "import uuid"

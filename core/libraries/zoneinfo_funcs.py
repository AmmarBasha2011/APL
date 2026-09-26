"""
APL - zoneinfo Library Functions
Transpiles Arabic keywords to Python zoneinfo module
"""

ZONEINFO_FUNCS = {
    "منطقة_زمنية": "zoneinfo.ZoneInfo",
    "كل_المناطق_الزمنية": "zoneinfo.available_timezones",
    "من_النص_إلى_منطقة": "_apl_zone_from_key",
    "إعادة_ضبط_مسار_المناطق": "zoneinfo.reset_tzpath",
      "منطقة_من_النص": "zoneinfo.ZoneInfo",
}

ZONEINFO_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(ZONEINFO_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

ZONEINFO_CONSTANTS = {
    "مسار_المناطق": "zoneinfo.TZPATH",
    "منطقة_utc": "datetime.timezone.utc",
}

ZONEINFO_CONSTANT_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(ZONEINFO_CONSTANTS.keys(), key=len, reverse=True)) + r")(?![\w\u0600-\u06FF])"

ZONEINFO_PROPS = {
    "مفتاح_المنطقة": "key",
}

ZONEINFO_PROP_PATTERN = r"\.(" + "|".join(sorted(ZONEINFO_PROPS.keys(), key=len, reverse=True)) + r")(?=\b)"

# Help text for CLI
ZONEINFO_HELP = [
    "# zoneinfo - المناطق الزمنية (IANA)",
    "منطقة_زمنية('Africa/Cairo')  - كائن منطقة زمنية",
    "كل_المناطق_ الزمنية()       - قائمة بكل المناطق",
    "منطقة_من_النص('Asia/Riyadh') - من نص",
    "مسار_المناطق                - مسارات البحث عن المناطق",
]

# Import detection
IMPORT_NAME = "zoneinfo"
IMPORT_CHECK = r"zoneinfo\."
IMPORT_STATEMENT = "import zoneinfo"

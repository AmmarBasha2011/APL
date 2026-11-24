"""
APL - datetime Library Functions
Transpiles Arabic keywords to Python datetime module
"""

DATETIME_KWARGS = {
    "أيام": "days",
    "ساعات": "hours",
    "دقائق": "minutes",
    "ثوان": "seconds",
    "ميكروثاني": "microseconds",
    "أسابيع": "weeks",
}

DATETIME_FUNCS = {
    "التاريخ_اليوم": "datetime.date.today",
    "التاريخ_الآن": "datetime.datetime.now",
    "الوقت_عالمي_الآن": "datetime.datetime.utcnow",
    "حوّل_نص_لتاريخ": "datetime.date.fromisoformat",
    "التاريخ_من_رقم": "datetime.date.fromordinal",
}

DATETIME_PATTERN = r"(?<![\w.\u0600-\u06FF])(" + "|".join(sorted(DATETIME_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

DATETIME_CONSTANTS = {
}

DATETIME_CONSTANT_PATTERN = r"(?<![\w.\u0600-\u06FF])(" + ("|".join(sorted(DATETIME_CONSTANTS.keys(), key=len, reverse=True)) or "(?!)") + r")(?![\w\u0600-\u06FF])"

DATETIME_PROPS = {
    "رقم_السنة": "year",
    "رقم_الشهر": "month",
    "رقم_اليوم": "day",
    "رقم_الساعة": "hour",
    "رقم_الدقيقة": "minute",
    "رقم_الثانية": "second",
    "رقم_الميكروثانية": "microsecond",
    "أيام_الفرق": "days",
}

DATETIME_PROP_PATTERN = r"\.(" + "|".join(sorted(DATETIME_PROPS.keys(), key=len, reverse=True)) + r")(?=\b)"

# Help text for CLI
DATETIME_HELP = [
    "# datetime - التعامل مع التاريخ والوقت",
    "التاريخ_اليوم()                  - تاريخ اليوم",
    "التاريخ_الآن()                   - تاريخ ووقت الآن",
    "حوّل_نص_لتاريخ('2026-01-01')     - نص ISO -> date",
    "حوّل_نص_لوقت(نص)                 - نص ISO -> datetime",
    "التاريخ_إلى_نص(كائن)              - date -> نص ISO",
    "نسق_الوقت(كائن, '%Y/%m/%d')       - تنسيق بـ strftime",
    "فك_الوقت(نص, '%Y-%m-%d')          - تحليل بـ strptime",
    "فرق_الوقت(أيام=3)                 - timedelta (أيام/ساعات/دقائق/ثوان)",
    "أيام_من_التاريخ(تاريخ)            - رقم اليوم التراكمي",
    "# خصائص الكائن: كائن.رقم_السنة، كائن.رقم_الشهر، كائن.رقم_يوم_الأسبوع",
    "# ثوابت: الحد_الأدنى، الحد_الأقصى، منطقة_ع_ي_تي",
]

# Import detection
IMPORT_NAME = "datetime"
IMPORT_CHECK = r"datetime\."
IMPORT_STATEMENT = "import datetime"

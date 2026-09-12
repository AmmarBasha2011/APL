"""
APL - Time & DateTime Library Functions
Transpiles Arabic time/datetime keywords to Python time/datetime module calls
"""

TIME_FUNCS = {
    # time module - وقت
    "وقت": "time.time",
    "وقت_نومي": "time.sleep",
    "وقت_نص": "time.ctime",
    "وقت_عالمي": "time.gmtime",
    "وقت_محلي": "time.localtime",
    "مؤشر_أداء": "time.perf_counter",
    "وقت_عملية": "time.process_time",
    "وقت_رتيب": "time.monotonic",
    
    # datetime module - تاريخ ووقت
    "الآن": "datetime.datetime.now",
    "اليوم": "datetime.date.today",
    "تاريخ_ووقت": "datetime.datetime",
    "تاريخ": "datetime.date",
    "وقت_فقط": "datetime.time",
    "مدة": "datetime.timedelta",
    "من_نص_وقت": "datetime.datetime.strptime",
    "لتنسيق_وقت": "datetime.datetime.strftime",
    
    # time formatting - تنسيق الوقت
    "تنسيق_وقت": "time.strftime",
    "تحليل_وقت": "time.strptime",
}

# Properties - no parentheses needed
TIME_PROPS = {
    "سنة_الآن": "datetime.datetime.now().year",
    "شهر_الآن": "datetime.datetime.now().month",
    "يوم_الآن": "datetime.datetime.now().day",
    "ساعة_الآن": "datetime.datetime.now().hour",
    "دقيقة_الآن": "datetime.datetime.now().minute",
    "ثانية_الآن": "datetime.datetime.now().second",
    "يوم_أسبوع_الآن": "datetime.datetime.now().weekday()",
}

# Combined pattern for functions (with parens)
TIME_PATTERN = "(" + "|".join(sorted(TIME_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Pattern for properties (word boundary, no parens)
TIME_PROP_PATTERN = r"(?<!\w)(" + "|".join(sorted(TIME_PROPS.keys(), key=len, reverse=True)) + r")(?!\s*\()(?!\w)"

# Help text for CLI
TIME_HELP = [
    "# وقت (time)",
    "وقت()              - الوقت بالثواني منذ epoch",
    "وقت_نومي(ث)        - انتظار (ثواني)",
    "وقت_نص()           - وقت كنص",
    "وقت_عالمي()        - وقت UTC",
    "وقت_محلي()         - وقت محلي",
    "مؤشر_أداء()        - مؤشر أداء عالي الدقة",
    "وقت_عملية()        - وقت المعالج",
    "وقت_رتيب()         - وقت رتيب (لقياس الفترات)",
    "# تاريخ ووقت (datetime)",
    "الآن()             - الوقت والتاريخ الحالي",
    "اليوم()            - التاريخ الحالي",
    "تاريخ_ووقت(س,ش,ي,...)  - كائن تاريخ ووقت",
    "تاريخ(س,ش,ي)       - كائن تاريخ",
    "وقت_فقط(س,د,ث)     - كائن وقت",
    "مدة(أيام, ثواني, ...)  - كائن مدة",
    "# مكونات التاريخ (خصائص)",
    "سنة_الآن()         - السنة الحالية",
    "شهر_الآن()         - الشهر الحالي",
    "يوم_الآن()         - اليوم الحالي",
    "ساعة_الآن()        - الساعة الحالية",
    "دقيقة_الآن()       - الدقيقة الحالية",
    "ثانية_الآن()       - الثانية الحالية",
    "# تنسيق",
    "تنسيق_وقت(ن, ت)    - تنسيق الوقت",
    "تحليل_وقت(ن, ت)    - تحليل نص وقت",
]

# Import detection
IMPORT_NAME = "time"
IMPORT_CHECK = "(time\.|datetime\.)"
IMPORT_STATEMENT = "import time, datetime"

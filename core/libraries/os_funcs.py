"""
APL - OS & Path Library Functions
Transpiles Arabic OS/path keywords to Python os/pathlib module calls
"""

OS_FUNCS = {
    # مسارات (Path operations)
    "مسار_مطلق": "os.path.abspath",
    "مسار_نسبي": "os.path.relpath",
    "اسم_ملف": "os.path.basename",
    "اسم_مجلد": "os.path.dirname",
    "امتداد": "os.path.splitext",
    "دمج_مسار": "os.path.join",
    "فصل_مسار": "os.path.split",
    # مجلدات (Directory operations)
    "مجلد_حالي": "os.getcwd",
    "غير_مجلد": "os.chdir",
    "انشئ_مجلد": "os.mkdir",
    "انشئ_مجلدات": "os.makedirs",
    "احذف_مجلد": "os.rmdir",
    "احذف_مجلدات": "os.removedirs",
    "قائمة_ملفات": "os.listdir",
    # ملفات (File operations)
    "احذف_ملف": "os.remove",
    "اعد_تسمية": "os.rename",
    "نسخ_ملف": "shutil.copy",
    "نقل_ملف": "shutil.move",
    "حجم_ملف": "os.path.getsize",
    "وقت_تعديل": "os.path.getmtime",
    # فحص (Inspection)
    "موجود": "os.path.exists",
    "هو_ملف": "os.path.isfile",
    "هو_مجلد": "os.path.isdir",
    "هو_رابط_مطلق": "os.path.isabs",
    # بيئة (Environment)
    "متغير_بيئة": "os.environ.get",
    "معرف_عملية": "os.getpid",
    "مجلد_منزل": "os.path.expanduser",
}

# Properties - no parentheses
OS_PROPS = {
    "فاصل_مسار": "os.sep",
    "فاصل_سطر": "os.linesep",
    "مسار_بحث": "sys.path",
}

OS_PATTERN = r"(?<!\w)(" + "|".join(sorted(OS_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("
OS_PROP_PATTERN = r"(?<!\w)(" + "|".join(sorted(OS_PROPS.keys(), key=len, reverse=True)) + r")(?!\w)"

OS_HELP = [
    "# مسارات (Path)",
    "مسار_مطلق(مسار)       - المسار المطلق",
    "اسم_ملف(مسار)         - اسم الملف من المسار",
    "اسم_مجلد(مسار)        - اسم المجلد",
    "امتداد(مسار)          - امتداد الملف",
    "دمج_مسار(أ, ب)        - دمج مسارين",
    "فصل_مسار(مسار)        - (مجلد, ملف)",
    "# مجلدات (Directory)",
    "مجلد_حالي()           - المجلد الحالي",
    "غير_مجلد(مسار)        - تغيير المجلد",
    "انشئ_مجلد(مسار)       - إنشاء مجلد",
    "انشئ_مجلدات(مسار)     - إنشاء مجلدات متداخلة",
    "احذف_مجلد(مسار)       - حذف مجلد فارغ",
    "قائمة_ملفات(مسار)     - قائمة الملفات",
    "# ملفات (File)",
    "احذف_ملف(مسار)        - حذف ملف",
    "اعد_تسمية(ق, ج)       - إعادة تسمية",
    "نسخ_ملف(م, هـ)        - نسخ ملف",
    "نقل_ملف(م, هـ)        - نقل ملف",
    "حجم_ملف(مسار)         - حجم الملف",
    "وقت_تعديل(مسار)       - وقت آخر تعديل",
    "# فحص (Inspection)",
    "موجود(مسار)           - هل المسار موجود",
    "هو_ملف(مسار)          - هل هو ملف",
    "هو_مجلد(مسار)         - هل هو مجلد",
    "هو_رابط_مطلق(مسار)    - هل المسار مطلق",
    "# بيئة (Environment)",
    "متغير_بيئة(اسم)       - متغير بيئة",
    "معرف_عملية()          - معرف العملية",
    "مجلد_منزل(مسار='~')   - مجلد المستخدم",
    "فاصل_مسار()           - فاصل المسارات",
]

IMPORT_NAME = "os"
IMPORT_CHECK = "(os\.|shutil\.)"
IMPORT_STATEMENT = "import os, shutil"

"""
APL - shutil Library Functions
Transpiles Arabic keywords to Python shutil module
"""

SHUTIL_FUNCS = {
    "انسخ_ملف": "shutil.copy",
    "انسخ_ملف_كامل": "shutil.copy2",
    "انسخ_شجرة": "shutil.copytree",
    "انقل_ملف": "shutil.move",
    "احذف_شجرة": "shutil.rmtree",
    "نسخ_محتوى": "shutil.copyfile",
    "الحجم_البشري": "shutil.disk_usage",
    "ابحث_في_المسار": "shutil.which",
    "أمر_النظام": "shutil.which",
    "انسخ_الصلاحيات": "shutil.copymode",
    "انسخ_البيانات": "shutil.copyfileobj",
    "تجاهل_الملفات": "shutil.ignore_patterns",
}

SHUTIL_PATTERN = r"(?<!\w)(" + "|".join(sorted(SHUTIL_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
SHUTIL_HELP = [
    "# shutil - نسخ ونقل وحذف الملفات والمجلدات",
    "انسخ_ملف(من, إلى)              - نسخ ملف",
    "انسخ_ملف_كامل(من, إلى)        - نسخ مع الأذونات والأوقات",
    "انسخ_شجرة(من, إلى)             - نسخ مجلد كامل بمحتوياته",
    "انقل_ملف(من, إلى)              - نقل أو إعادة تسمية",
    "احذف_شجرة(مجلد)                - حذف مجلد ومحتوياته",
    "الحجم_البشري(مسار)             - مساحة القرص",
    "ابحث_في_المسار('python')       - أين يوجد البرنامج؟",
]

# Import detection
IMPORT_NAME = "shutil"
IMPORT_CHECK = r"shutil\."
IMPORT_STATEMENT = "import shutil"

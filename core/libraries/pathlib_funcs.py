"""
APL - pathlib Library Functions
Transpiles Arabic keywords to Python pathlib module
"""

PATHLIB_KWARGS = {
    "آباء": "parents",
    "موجود_سلفا": "exist_ok",
}

PATHLIB_FUNCS = {
    "مسار_جديد": "pathlib.Path",
    "المسار_الحالي": "pathlib.Path.cwd",
    "مسار_موجود": "_apl_path_exists",
    "مسار_اقرأ": "pathlib.Path.read_text",
    "مسار_اكتب": "pathlib.Path.write_text",
    "مسار_ابحث": "pathlib.Path.glob",
    "مسار_محتويات": "pathlib.Path.iterdir",
    "أنشئ_مجلد_مسار": "pathlib.Path.mkdir",
    "مسار_احذف": "pathlib.Path.unlink",
}

PATHLIB_PATTERN = r"(?<![\w.\u0600-\u06FF])(" + "|".join(sorted(PATHLIB_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

PATHLIB_METHODS = {
    "ادمج": "joinpath",
    "نص_له": "as_posix",
    "مطلق_له": "resolve",
    "نسبي_له": "absolute",
    "موجود_له": "exists",
    "هو_مجلد_له": "is_dir",
    "هو_ملف_له": "is_file",
    "اقرأ_له": "read_text",
    "اكتب_له": "write_text",
    "افتح_له": "open",
    "لمس_له": "touch",
    "ابحث_له": "glob",
    "محتويات_له": "iterdir",
    "أعد_تسمية_له": "rename",
    "استبدل_له": "replace",
    "إحصاء_له": "stat",
    "اسم_له": "name",
    "امتداد_له": "suffix",
    "بدون_امتداد_له": "stem",
    "أبوين_له": "parent",
    "أجزاء_له": "parts",
}

PATHLIB_METHOD_PATTERN = r"\.(" + "|".join(sorted(PATHLIB_METHODS.keys(), key=len, reverse=True)) + r")\s*\("

PATHLIB_PROPS = {
    "مسار_اسم": "name",
    "مسار_بدون_امتداد": "stem",
    "مسار_امتداد": "suffix",
    "مسار_امتدادات": "suffixes",
    "مسار_أبوين": "parent",
    "مسار_أصول": "parents",
    "مسار_أجزاء": "parts",
}

PATHLIB_PROP_PATTERN = r"\.(" + "|".join(sorted(PATHLIB_PROPS.keys(), key=len, reverse=True)) + r")(?=\b)"

# Help text for CLI
PATHLIB_HELP = [
    "# pathlib - التعامل مع المسارات ككائنات",
    "مسار_جديد('مجلد/ملف.txt')      - إنشاء كائن مسار",
    "المسار_الحالي()                - مجلد العمل الحالي",
    "المسار_المنزل()                - مجلد المنزل",
    "مسار_ادمج(مسار, 'مجلد')        - دمج أجزاء المسار",
    "مسار_موجود(مسار)               - هل المسار موجود؟",
    "مسار_اقرأ(مسار)                - قراءة نص الملف",
    "مسار_اكتب(مسار, 'محتوى')       - كتابة نص",
    "مسار_ابحث(مسار, '*.py')        - بحث بنمط",
    "# خصائص: كائن.مسار_اسم، كائن.مسار_امتداد، كائن.مسار_بدون_امتداد، كائن.مسار_أبوين",
]

# Import detection
IMPORT_NAME = "pathlib"
IMPORT_CHECK = r"pathlib\."
IMPORT_STATEMENT = "import pathlib"

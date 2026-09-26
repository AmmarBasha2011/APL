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
    "درب": "pathlib.Path",
    "أنشئ_مسار": "pathlib.Path",
    "المسار_الحالي": "pathlib.Path.cwd",
    "المسار_المنزل": "pathlib.Path.home",
    "مسار_ادمج": "pathlib.Path.joinpath",
    "مسار_نص": "pathlib.Path.as_posix",
    "مسار_مطلق_كامل": "pathlib.Path.resolve",
    "مسار_نسبي_كامل": "pathlib.Path.absolute",
    "مسار_موجود": "_apl_path_exists",
    "مسار_هو_مجلد": "pathlib.Path.is_dir",
    "مسار_هو_ملف": "pathlib.Path.is_file",
    "مسار_رابط_رمزي": "pathlib.Path.is_symlink",
    "مسار_إحصاء": "pathlib.Path.stat",
    "مسار_لمس": "pathlib.Path.touch",
    "مسار_فتح": "pathlib.Path.open",
    "مسار_اقرأ": "pathlib.Path.read_text",
    "مسار_اكتب": "pathlib.Path.write_text",
    "مسار_اقرأ_ثنائي": "pathlib.Path.read_bytes",
    "مسار_اكتب_ثنائي": "pathlib.Path.write_bytes",
    "مسار_ابحث": "pathlib.Path.glob",
    "مسار_ابحث_الكل": "pathlib.Path.rglob",
    "مسار_إعادة_تسمية": "pathlib.Path.rename",
    "مسار_استبدال": "pathlib.Path.replace",
    "مسار_محتويات": "pathlib.Path.iterdir",
    "مسار_أنشئ_مجلد": "pathlib.Path.mkdir",
    "أنشئ_مجلد_مسار": "pathlib.Path.mkdir",
    "مسار_احذف": "pathlib.Path.unlink",
    "مسار_احذف_مجلد": "pathlib.Path.rmdir",
    "مسار_نفسه": "pathlib.Path.samefile",
    "مسار_أنشئ_رابط": "pathlib.Path.symlink_to",
}

PATHLIB_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(PATHLIB_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

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

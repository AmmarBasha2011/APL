"""
APL - SQLite3 Database Library
Full SQLite3 wrapper with Arabic keywords
"""

SQLITE3_FUNCS = {
    # الاتصال بقاعدة البيانات
    "افتح_قاعدة": "sqlite3.connect",
    "افتح_قاعدة_بيانات": "sqlite3.connect",
    "اتصل_قاعدة": "sqlite3.connect",
    "قاعدة": "sqlite3.connect",
    
    # المؤشر (Cursor)
    "مؤشر": "cursor",
    "أنشئ_مؤشر": "connection.cursor",
    
    # تنفيذ الاستعلامات

    
    # جلب النتائج

    
    # التأكيد والتراجع

    
    # الإغلاق

    
    # خصائص الاتصال
    "صف_مصنع": "connection.row_factory",
    "نص_مصنع": "connection.text_factory",
    "عزل_مستوى": "connection.isolation_level",
    
    # الدوال المساعدة
    "نسخ_احتياطي": "sqlite3.connect",
}

SQLITE3_METHODS = {
    "نفذ": "execute",
    "نفذ_استعلام": "execute",
    "نفذ_كثير": "executemany",
    "نفذ_سكريبت": "executescript",
    "جلب_واحد": "fetchone",
    "جلب_الكل": "fetchall",
    "جلب_عدد": "fetchmany",
    "أغلق_مؤشر": "close",
    "تأكد": "commit",
    "احفظ": "commit",
    "تراجع": "rollback",
    "أغلق_قاعدة": "close",
    "أغلق_اتصال": "close",
}

SQLITE3_METHOD_PATTERN = r"\.(" + "|".join(sorted(SQLITE3_METHODS.keys(), key=len, reverse=True)) + r")\s*\("

SQLITE3_PATTERN = r"(?<!\w)(" + "|".join(sorted(SQLITE3_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

SQLITE3_HELP = [
    "# === الاتصال ===",
    "افتح_قاعدة('ملف.db')  - فتح قاعدة بيانات",
    "اتصل_قاعدة('ملف.db')   - اتصال بقاعدة",
    "# === المؤشر ===",
    "مؤشر()                 - إنشاء مؤشر",
    "أنشئ_مؤشر()           - إنشاء مؤشر",
    "# === التنفيذ ===",
    "نفذ('استعلام')        - تنفيذ استعلام",
    "نفذ_استعلام('استعلام') - تنفيذ استعلام",
    "نفذ_كثير('استعلام', بيانات) - تنفيذ كثير",
    "# === الجلب ===",
    "جلب_واحد()            - جلب صف واحد",
    "جلب_الكل()            - جلب كل الصفوف",
    "جلب_عدد(ن)            - جلب ن صفوف",
    "# === التأكيد ===",
    "تأكد()                - تأكيد التغييرات",
    "احفظ()                 - حفظ التغييرات",
    "تراجع()               - تراجع عن التغييرات",
    "# === الإغلاق ===",
    "أغلق()                - إغلاق الاتصال",
    "أغلق_قاعدة()          - إغلاق قاعدة البيانات",
]

IMPORT_NAME = "sqlite3"
IMPORT_CHECK = "sqlite3\."
IMPORT_STATEMENT = "import sqlite3"

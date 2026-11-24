"""
APL - Logging Library
Full logging wrapper with Arabic keywords
"""

LOGGING_FUNCS = {
    # الإنشاء والتكوين
    
    # مستويات السجل
    "مستوى": "setLevel",
    "ضع_مستوى": "setLevel",
    
    # تنسيق السجل
    "شكل": "logging.Formatter",
    "ضع_شكل": "handler.setFormatter",
    "صيغة": "fmt",
    "تاريخ_صيغة": "datefmt",
    
    # المعالجات (Handlers)
    "معالج": "logging.Handler",
    "معالج_ملف": "logging.FileHandler",
    "أضف_معالج": "logger.addHandler",
    "أزل_معالج": "logger.removeHandler",
    
    # المسجل الجذر
    "جذر_تسجيل": "logging.root",
    "سجل_جذر": "logging.root",
    "سجل_أساسي": "logging",
    
    # الدوال المختصرة
    
    # التسجيل
    "تسجيل": "logging.log",
    "تصحيح": "debug",
    "معلومات": "info",
    "تحذير": "warning",
    "خطأ_تسجيل": "error",
    "حرج": "critical",
    "استثناء_سجل": "exception",
    
    # الفلاتر (Filters)
    "أضف_فلتر": "logger.addFilter",
    "أزل_فلتر": "logger.removeFilter",
    "اسم_فلتر": "filter.name",
    
    # البيانات الوصفية
    "اسم_المسجل": "logger.name",
    "أب": "logger.parent",
    "منتشر": "logger.propagate",
    "مكّن": "logger.disabled",
    "فعّل": "logger.enable",
    "عطّل": "logger.disable",
    "مستوى_فعّال": "logger.getEffectiveLevel",
    "مُعَطَّل": "logger.disabled",
    
    # البيانات السياقية
    "محول_سجل": "logging.LoggerAdapter",
    "بيانات_إضافية": "logger.extra",
    
    # إغلاق
    "أغلق": "logging.shutdown",
    
    # مكتبات المعالجات
    "معالجات": "logging.handlers",
    "دوار": "logging.handlers.RotatingFileHandler",
    "مؤقت_دوار": "logging.handlers.TimedRotatingFileHandler",
    "معالج_tcp": "logging.handlers.SocketHandler",
    "معالج_udp": "logging.handlers.DatagramHandler",
    "معالج_syslog": "logging.handlers.SysLogHandler",
    "معجل_nt": "logging.handlers.NTEventLogHandler",
    "معالج_http": "logging.handlers.HTTPHandler",
    
    # الطوابير (Queues)
    "طابور_سجل": "logging.handlers.QueueHandler",
    "مستمع_سجل": "logging.handlers.QueueListener",
    
    # القفل
    "قفل_سجل": "logging._lock",
    
    # المتغيرات العامة
    "تحذير_مرة": "logging._warnings",
    "تحذيرات_مرة": "logging.captureWarnings",
    "كتالوجات": "logging.Logger.manager.loggerDict",
    "كل_المسجلات": "logging.Logger.manager",
}

LOGGING_VERBS = {
    "سجل_تصحيح": "logging.debug",
    "سجل_معلومات": "logging.info",
    "سجل_تحذير": "logging.warning",
    "سجل_خطأ": "logging.error",
    "سجل_حرج": "logging.critical",
    "سجل_استثناء": "logging.exception",
    "سجل_تهيئة": "logging.basicConfig",
}

LOGGING_PATTERN = r"(?<![\w.\u0600-\u06FF])(" + "|".join(sorted(LOGGING_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

LOGGING_HELP = [
    "# === الإنشاء ===",
    "مسجّل(اسم_المسجل)               - إنشاء مسجل",
    "أنشئ_مسجل(اسم_المسجل)         - إنشاء مسجل",
    "مسجل(اسم_المسجل)              - مسجل (مختصر)",
    "جذر_تسجيل()                   - المسجل الجذر",
    "# === التكوين ===",
    "تكوين_تسجيل()                - تكوين_تسجيل أساسي",
    "أساسي()                - تكوين_تسجيل أساسي",
    "ضع_مستوى(مستوى)        - تعيين المستوى",
    "# === المستويات ===",
    "مستوى_تصحيح()          - DEBUG",
    "مستوى_معلومات()        - INFO",
    "مستوى_تحذير()          - WARNING",
    "مستوى_خطأ()            - ERROR",
    "level_حرج()            - CRITICAL",
    "# === المعالجات ===",
    "معالج_ملف(ملف)         - معالج ملف",
    "معالج_شاشة()           - معالج شاشة",
    "أضف_معالج(معالج)       - إضافة معالج",
    "أزل_معالج(معالج)       - إزالة معالج",
    "# === التنسيق ===",
    "شكل(تنسيق)             - منسق النصوص",
    "ضع_شكل(شكل)            - تعيين المنسق",
    "أضف_فلتر(فلتر_تسجيل)         - إضافة فلتر_تسجيل",
    "# === التسجيل ===",
    "تصحيح(رسالة)           - تصحيح",
    "معلومات(رسالة)        - معلومات",
    "تحذير(رسالة)           - تحذير",
    "خطأ_تسجيل(رسالة)             - خطأ_تسجيل",
    "حرج(رسالة)             - حرج",
    "استثناء_تسجيل(رسالة)         - استثناء_تسجيل",
    "# === البيانات الإضافية ===",
    "سجل_إضافي(مسجل, بيانات) - محول مسجّل",
    "محول_سجل(مسجل, بيانات) - محول مسجّل",
    "# === الإغلاق ===",
    "أغلق()                 - إغلاق كل المسجلات",
    "تنظيف()                - تنظيف المسجلات",
]

IMPORT_NAME = "logging"
IMPORT_CHECK = "logging\."
IMPORT_STATEMENT = "import logging"

# مستويات التسجيل كقيم ثابتة (تُستعمل وحدها بلا أقواس)
LOGGING_CONSTANTS = {
    "مستوى_تصحيح": "logging.DEBUG",
    "مستوى_معلومات": "logging.INFO",
    "مستوى_تحذير": "logging.WARNING",
    "مستوى_خطأ": "logging.ERROR",
    "مستوى_حرج": "logging.CRITICAL",
}

LOGGING_CONSTANT_PATTERN = (
    r"(?<![\w.\u0600-\u06FF])("
    + "|".join(sorted(LOGGING_CONSTANTS.keys(), key=len, reverse=True))
    + r")(?![\w\u0600-\u06FF])"
)

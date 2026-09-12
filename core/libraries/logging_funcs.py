"""
APL - Logging Library
Full logging wrapper with Arabic keywords
"""

LOGGING_FUNCS = {
    # الإنشاء والتكوين
    "سجل": "logging.getLogger",
    "أنشئ_مسجل": "logging.getLogger",
    "مسجل": "logging.getLogger",
    "تكوين": "logging.basicConfig",
    "أساسي": "logging.basicConfig",
    
    # مستويات السجل
    "مستوى_تصحيح": "logging.DEBUG",
    "مستوى_معلومات": "logging.INFO",
    "مستوى_تحذير": "logging.WARNING",
    "مستوى_خطأ": "logging.ERROR",
    "level_حرج": "logging.CRITICAL",
    "مستوى": "setLevel",
    "ضع_مستوى": "setLevel",
    
    # تنسيق السجل
    "تنسيق": "logging.Formatter",
    "شكل": "logging.Formatter",
    "شكل_جديد": "logging.Formatter",
    "شكل_افتراضي": "logging.Formatter",
    "ضع_شكل": "handler.setFormatter",
    "صيغة": "fmt",
    "تاريخ_صيغة": "datefmt",
    
    # المعالجات (Handlers)
    "معالج": "logging.Handler",
    "معالج_ملف": "logging.FileHandler",
    "معالج_شاشة": "logging.StreamHandler",
    "معالج_دوار": "logging.handlers.RotatingFileHandler",
    "معجل_مؤقت": "logging.handlers.TimedRotatingFileHandler",
    "أنشئ_معالج": "logging.Handler",
    "أضف_معالج": "logger.addHandler",
    "أزل_معالج": "logger.removeHandler",
    
    # المسجل الجذر
    "جذر": "logging.root",
    "سجل_جذر": "logging.root",
    "سجل_أساسي": "logging",
    
    # الدوال المختصرة
    "اطبع_تصحيح": "logging.debug",
    "اطبع_معلومات": "logging.info",
    "اطبع_تحذير": "logging.warning",
    "اطبع_خطأ": "logging.error",
    "اطبع_حرج": "logging.critical",
    "استثناء": "logging.exception",
    
    # التسجيل
    "تسجيل": "logging.log",
    "تصحيح": "debug",
    "معلومات": "info",
    "تحذير": "warning",
    "خطأ": "error",
    "حرج": "critical",
    "استثناء_سجل": "exception",
    
    # الفلاتر (Filters)
    "فلتر": "logging.Filter",
    "أنشئ_فلتر": "logging.Filter",
    "أضف_فلتر": "logger.addFilter",
    "أزل_فلتر": "logger.removeFilter",
    "اسم_فلتر": "filter.name",
    
    # البيانات الوصفية
    "اسم": "logger.name",
    "أب": "logger.parent",
    "منتشر": "logger.propagate",
    "مكّن": "logger.disabled",
    "فعّل": "logger.enable",
    "عطّل": "logger.disable",
    "مستوى_فعّال": "logger.getEffectiveLevel",
    "مُعَطَّل": "logger.disabled",
    
    # البيانات السياقية
    "سجل_إضافي": "logging.LoggerAdapter",
    "محول_سجل": "logging.LoggerAdapter",
    "بيانات_إضافية": "logger.extra",
    
    # إغلاق
    "أغلق": "logging.shutdown",
    "تنظيف": "logging.shutdown",
    
    # مكتبات المعالجات
    "معالجات": "logging.handlers",
    "دوار": "logging.handlers.RotatingFileHandler",
    "مؤقت_دوار": "logging.handlers.TimedRotatingFileHandler",
    "معالج_tcp": "logging.handlers.SocketHandler",
    "معالج_udp": "logging.handlers.DatagramHandler",
    "معالج_بريد": "logging.handlers.SMTPHandler",
    "معالج_syslog": "logging.handlers.SysLogHandler",
    "معجل_nt": "logging.handlers.NTEventLogHandler",
    "معالج_http": "logging.handlers.HTTPHandler",
    "معالج_ذاكرة": "logging.handlers.MemoryHandler",
    "معالج_queue": "logging.handlers.QueueHandler",
    
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

LOGGING_PATTERN = r"(?<!\w)(" + "|".join(sorted(LOGGING_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

LOGGING_HELP = [
    "# === الإنشاء ===",
    "سجل(اسم)               - إنشاء مسجل",
    "أنشئ_مسجل(اسم)         - إنشاء مسجل",
    "مسجل(اسم)              - مسجل (مختصر)",
    "جذر()                   - المسجل الجذر",
    "# === التكوين ===",
    "تكوين()                - تكوين أساسي",
    "أساسي()                - تكوين أساسي",
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
    "أضف_فلتر(فلتر)         - إضافة فلتر",
    "# === التسجيل ===",
    "تصحيح(رسالة)           - تصحيح",
    "معلومات(رسالة)        - معلومات",
    "تحذير(رسالة)           - تحذير",
    "خطأ(رسالة)             - خطأ",
    "حرج(رسالة)             - حرج",
    "استثناء(رسالة)         - استثناء",
    "# === البيانات الإضافية ===",
    "سجل_إضافي(مسجل, بيانات) - محول سجل",
    "محول_سجل(مسجل, بيانات) - محول سجل",
    "# === الإغلاق ===",
    "أغلق()                 - إغلاق كل المسجلات",
    "تنظيف()                - تنظيف المسجلات",
]

IMPORT_NAME = "logging"
IMPORT_CHECK = "logging\."
IMPORT_STATEMENT = "import logging"

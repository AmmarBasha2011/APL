"""
APL - ConfigParser Library
Full configparser wrapper with Arabic keywords
"""

CONFIGPARSER_FUNCS = {
    # الإنشاء
    "أنشئ_مُكوِّن": "configparser.ConfigParser",
    "مُكوِّن": "configparser.ConfigParser",
    "مُكوِّن_إعدادات": "configparser.ConfigParser",
    "إعدادات": "configparser.ConfigParser",
    
    # التنسيقات
    "افتراضي": "configparser.DEFAULTSECT",
    "تكوين_افتراضي": "configparser.DEFAULTSECT",
    
    # القراءة
    "اقرأ": "config.read",
    "اقرأ_ملف": "config.read_file",
    "اقرأ_سلسلة": "config.read_string",
    "اقرأ_قاموس": "config.read_dict",
    
    # الكتابة
    "اكتب": "config.write",
    "اكتب_ملف": "config.write",
    
    # الأقسام
    "أضف_قسم": "config.add_section",
    "أزل_قسم": "config.remove_section",
    "يوجد_قسم": "config.has_section",
    "الأقسام": "config.sections",
    
    # الخيارات
    "ضع": "config.set",
    "احصل": "config.get",
    "أزل_خيار": "config.remove_option",
    "يوجد_خيار": "config.has_option",
    "الخيارات": "config.options",
    
    # أنواع البيانات
    "احصل_عدد_صحيح": "config.getint",
    "احصل_عدد_عشري": "config.getfloat",
    "احصل_منطقي": "config.getboolean",
    
    # التعيينات
    "items": "config.items",
    "احصل_كل": "config.items",
    
    # الاستيفاء
    "BasicInterpolation": "configparser.BasicInterpolation",
    "ExtendedInterpolation": "configparser.ExtendedInterpolation",
    "RawInterpolation": "configparser.RawInterpolation",
    
    # التكوين المُنظّم
    "RawConfigParser": "configparser.RawConfigParser",
    "SafeConfigParser": "configparser.SafeConfigParser",
    
    # الخصائص
    "افتراضي": "config.defaults",
    "مفاتيح_افتراضية": "config.defaults",
    
    # التعليقات
    "بادئة_تعليق": "config._comment_prefixes",
    
    # القسم الافتراضي
    "DEFAULT": "configparser.DEFAULTSECT",
    "الافتراضي": "configparser.DEFAULTSECT",
}

CONFIGPARSER_PATTERN = r"(?<!\w)(" + "|".join(sorted(CONFIGPARSER_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

CONFIGPARSER_HELP = [
    "# === الإنشاء ===",
    "أنشئ_مُكوِّن()             - إنشاء مُكوِّن",
    "مُكوِّن()                  - مُكوِّن (مختصر)",
    "مُكوِّن_إعدادات()          - مُكوِّن إعدادات",
    "إعدادات()                 - إعدادات (مختصر)",
    "# === القراءة ===",
    "اقرأ(ملف)                - قراءة ملف إعدادات",
    "اقرأ_ملف(ملف)            - قراءة ملف إعدادات",
    "اقرأ_سلسلة(نص)          - قراءة سلسلة إعدادات",
    "اقرأ_قاموس(قاموس)        - قراءة قاموس إعدادات",
    "# === الكتابة ===",
    "اكتب(ملف)                - كتابة ملف إعدادات",
    "اكتب_ملف(ملف)            - كتابة ملف إعدادات",
    "# === الأقسام ===",
    "أضف_قسم(قسم)            - إضافة قسم",
    "أزل_قسم(قسم)            - إزالة قسم",
    "يوجد_قسم(قسم)           - هل القسم موجود",
    "الأقسام()                - قائمة الأقسام",
    "# === الخيارات ===",
    "ضع(قسم, خيار, قيمة)      - تعيين خيار",
    "احصل(قسم, خيار)          - الحصول على خيار",
    "أزل_خيار(قسم, خيار)      - إزالة خيار",
    "يوجد_خيار(قسم, خيار)     - هل الخيار موجود",
    "الخيارات(قسم)            - قائمة الخيارات",
    "# === أنواع البيانات ===",
    "احصل_عدد_صحيح(قسم, خيار) - الحصول على عدد صحيح",
    "احصل_عدد_عشري(قسم, خيار) - الحصول على عدد عشري",
    "احصل_منطقي(قسم, خيار)    - الحصول على قيمة منطقية",
    "# === التعيينات ===",
    "items(قسم)               - جميع الخيارات",
    "احصل_كل(قسم)             - جميع الخيارات",
]

IMPORT_NAME = "configparser"
IMPORT_CHECK = "configparser\."
IMPORT_STATEMENT = "import configparser"

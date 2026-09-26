"""
APL - Argparse Library
Full argparse wrapper with Arabic keywords
"""

ARGPARSE_FUNCS = {
    # الإنشاء
    "أنشئ_محلل": "argparse.ArgumentParser",
    "محلل": "argparse.ArgumentParser",
    "محلل_وسائط": "argparse.ArgumentParser",
    
    # الخصائص
    "اسم": "parser.prog",
    "وصف": "parser.description",
    "تلميح_استخدام": "parser.usage",
    "نهاية_مساعدة": "parser.formatter_class",
    "خاتمة_مساعدة": "parser.epilog",
    "بادئة_حجة": "parser.prefix_chars",
    "من_ملف_وسائط": "parser.fromfile_prefix_chars",
    "أب": "parser.parents",
    "مُنسَق": "parser.formatter_class",
    "إضافة_مساعدة": "parser.add_help",
    "السماح_الاختصارات": "parser.allow_abbrev",
    
    # المجموعات
    "أضف_مجموعة": "parser.add_argument_group",
    "مجموعة_متنافية": "parser.add_mutually_exclusive_group",
    "مجموعة_حجة": "parser.add_argument_group",
    "مجموعة_حجج": "parser.add_argument_group",
    
    # الحجج الموضعية
    "أضف_حجة": "parser.add_argument",
    "حجة": "parser.add_argument",
    "أضف_حجة_وضعية": "parser.add_argument",
    "حجة_وضعية": "parser.add_argument",
    
    # الحجج الاختيارية
    "أضف_خيار": "parser.add_argument",
    "خيار": "parser.add_argument",
    "أضف_علم": "parser.add_argument",
    "علم": "parser.add_argument",
    
    # خصائص الحجة
    "اسم_حجة": "name",
    "وجهة": "dest",
    "نوع": "type",
    "افتراضي": "default",
    "مطلوب": "required",
    "تلميح": "help",
    "الإجراء": "action",
    "ثابت": "const",
    "خيارات": "choices",
    " nargs": "nargs",
    " metavar": "metavar",
    
    # الإجراءات
    "خزن": "store",
    "خزن_ثابت": "store_const",
    "خزن_صحيح": "store_true",
    "خزن_خطأ": "store_false",
    "أضف_قيمة": "append",
    "عد_مرات": "count",
    "أضف_وسيط": "append",
    "أضف_ثابت": "append_const",
    "عد_وسيط": "count",
    "مساعدة": "help",
    "إصدار": "version",
    
    # التحليل
    "حلل": "parser.parse_args",
    "حلل_وسائط": "parser.parse_args",
    "حلل_معروف": "parser.parse_known_args",
    "حلل_من_سلسلة": "parser.parse_args",
    "وسائط": "parser.parse_args",
    "حلل_وسائط_من_ملف": "parser.parse_args",
    
    # الإصدار
    "إصدار_المحلل": "parser.version",
    
    # الرسائل
    "خطأ": "parser.error",
    "خروج": "parser.exit",
    "استخدم_بعد_التحليل": "parser.exit",
    "اطبع_مساعدة": "parser.print_help",
    "اطبع_استخدام": "parser.print_usage",
    "مساعدة_كاملة": "parser.format_help",
    "استخدام_كامل": "parser.format_usage",
    
    # المساعد التلقائي
    "مساعدة_تلقائية": "ArgumentDefaultsHelpFormatter",
    "مساعدة_نصية": "RawDescriptionHelpFormatter",
    "مساعدة_نصية_فقط": "RawTextHelpFormatter",
    "مساعدة_Metavar": "MetavarTypeHelpFormatter",
    
    # ملفات الوسائط
    "من_ملف": "parser.parse_args",
    "إلى_ملف": "parser.parse_args",
    
    # مساعد للحجج (prefixed to avoid shadowing core types صحيح/خطأ)
    "قيمة_صحيح": "True",
    "قيمة_خطأ": "False",
    "قيمة_لا_شيء": "None",
    
    # المكتبة الفرعية
    "فرعي": "subparsers",
    "أضف_فرعي": "parser.add_subparsers",
    "أضف_محلل_فرعي": "subparsers.add_parser",
    "محلل_فرعي": "subparsers.add_parser",
    
    # الأنواع (prefixed to avoid shadowing core types نص/صحيح/قائمة/قاموس)
    "نوع_نص": "str",
    "نوع_عدد_صحيح": "int",
    "نوع_عدد_عشري": "float",
    "نوع_منطقي": "bool",
    "نوع_قائمة": "list",
    "نوع_صف": "tuple",
    "نوع_مجموعة": "set",
    "نوع_قاموس": "dict",
    "ملف": "argparse.FileType",
    
    # القيم الخاصة
    "واحد": "1",
    "صفر": "0",
    "الكل": "*",
    "واحد_أو_أكثر": "+",
    "اختياري": "?",
    
    # المخرجات
    "Namespace": "argparse.Namespace",
    "FILE": "argparse.FileType",
}

# Standalone helpers: take the parser as the first argument
ARGPARSE_STANDALONE = {
    "محلل_أضف_حجة": "_apl_ap_add_argument",
    "محلل_أضف_قيمة": "_apl_ap_add_argument",
    "محلل_أضف_مجموعة": "_apl_ap_add_argument_group",
    "محلل_حلل": "_apl_ap_parse_args",
    "محلل_حلل_معروف": "_apl_ap_parse_known_args",
    "محلل_مساعدة": "_apl_ap_format_help",
    "محلل_اطبع_مساعدة": "_apl_ap_print_help",
    "محلل_نسخ": "_apl_ap_parser_copy",
}

ARGPARSE_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(ARGPARSE_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

ARGPARSE_HELP = [
    "# === الإنشاء ===",
    "أنشئ_محلل()             - إنشاء محلل",
    "محلل()                  - محلل (مختصر)",
    "محلل_وسائط()            - محلل وسائط",
    "# === الخصائص ===",
    "وصف(نص)                - وصف البرنامج",
    "تلميح_استخدام(نص)      - تلميح الاستخدام",
    "خاتمة_مساعدة(نص)        - خاتمة المساعدة",
    "# === المجموعات ===",
    "أضف_مجموعة(عنوان)      - إضافة مجموعة",
    "مجموعة_متنافية()       - مجموعة متنافية",
    "# === الحجج ===",
    "أضف_حجة(اسم)           - إضافة حجة",
    "حجة(اسم)               - حجة (مختصر)",
    "أضف_خيار(اسم)          - إضافة خيار",
    "خيار(اسم)              - خيار (مختصر)",
    "# === خصائص الحجة ===",
    "وجهة(اسم)              - اسم الوجهة",
    "نوع(نوع)               - نوع الحجة",
    "افتراضي(قيمة)          - القيمة الافتراضية",
    "مطلوب(صحيح)            - هل الحجة مطلوبة",
    "تلميح(نص)              - نص المساعدة",
    "الإجراء(فعل)            - فعل الحجة",
    "خيارات(قائمة)          - خيارات الحجة",
    "# === الإجراءات ===",
    "خزن(قيمة)              - خزن القيمة",
    "خزن_ثابت(قيمة)         - خزن ثابت",
    "خزن_صحيح()             - خزن True",
    "خزن_خطأ()             - خزن False",
    "أضف(قيمة)              - إضافة لقائمة",
    "عد()                    - عدد المرات",
    "مساعدة()                - عرض المساعدة",
    "إصدار(نص)              - عرض الإصدار",
    "# === التحليل ===",
    "حلل()                   - تحليل الوسائط",
    "حلل_وسائط()            - تحليل الوسائط",
    "حلل_معروف()            - تحليل معروف",
    "# === الرسائل ===",
    "خطأ(رسالة)             - إظهار خطأ",
    "خروج(حالة)             - خروج من البرنامج",
    "اطبع_مساعدة()           - طباعة المساعدة",
    "اطبع_استخدام()          - طباعة الاستخدام",
    "# === المساعدات ===",
    "مساعدة_تلقائية()       - مساعدة مع افتراضيات",
    "مساعدة_نصية()           - مساعدة نصية",
    "# === المخرجات ===",
    "وسائط.حجة              - الوصول للحجة",
]

IMPORT_NAME = "argparse"
IMPORT_CHECK = "argparse\."
IMPORT_STATEMENT = "import argparse"

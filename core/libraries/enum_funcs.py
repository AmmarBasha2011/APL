"""
APL - enum Library Functions
Transpiles Arabic keywords to the Python enum module.

    المتغير حالة = نوع_تعداد("حالة", "نشط، معطل، pending")
    اطبع حالة.نشط.name      #  "نشط"
    اطبع حالة.نشط.value     #  1

NOTE: "تعداد" is already mapped to enum.Enum by the dataclasses library, so the
constructor here uses the distinct "نوع_تعداد". Member attribute access uses the
plain Python `.name` / `.value` (ENUM_METHODS is intentionally absent — mapping
"اسم"/"قيمة" as properties would hijack those words everywhere).
"""

ENUM_FUNCS = {
    "نوع_تعداد": "_apl_enum",
    "كل_الأسماء": "_apl_enum_all_names",
    "كل_القيم": "_apl_enum_all_values",
    "تحقق_من_القيمة": "_apl_enum_has_value",
    "قيمة_من_اسم": "_apl_enum_value",
    "قيمة_من": "_apl_enum_value",
    "أسماء_التعداد": "_apl_enum_all_names",
}

ENUM_PATTERN = (
    r"(?<![\w\u0600-\u06FF])("
    + "|".join(sorted(ENUM_FUNCS.keys(), key=len, reverse=True))
    + r")\s*\("
)

ENUM_HELP = [
    "# enum - أنواع معدودة (Enums)",
    'نوع_تعداد(اسم, "أ، ب، ج") - إنشاء نوع معدود من أسماء مفصولة بفاصلة',
    "  النوع.اسم               - اسم العنصر",
    "  النوع.قيمة              - قيمة العنصر (ترقيم من 1)",
    "كل_الأسماء(النوع)         - قائمة بكل الأسماء",
    "كل_القيم(النوع)           - قائمة بكل القيم",
    "تحقق_من_القيمة(النوع, رقم) - هل القيمة موجودة؟",
    "قيمة_من_اسم(النوع, \"أ\")  - القيمة من الاسم",
    "مثال:",
    '  المتغير حالة = نوع_تعداد("حالة", "نشط، معطل، pending")',
    "  اطبع حالة.نشط.name",
]

IMPORT_NAME = "enum"
IMPORT_CHECK = r"enum\."
IMPORT_STATEMENT = "import enum"

"""
APL - Math Library Functions
Transpiles Arabic math keywords to Python math module calls
"""

MATH_FUNCS = {
    # أساسي
    "مطلق": "abs", "قوة": "pow", "جذر": "math.sqrt",
    "أكبر": "max", "أصغر": "min", "مقرب": "round",
    "مجموع": "sum", "مفرز": "sorted",
    # مثلثات
    "جتا": "math.cos", "جب": "math.sin", "ظا": "math.tan",
    "م_جتا": "math.acos", "م_جب": "math.asin", "م_ظا": "math.atan", "م_ظا2": "math.atan2",
    # زائدي
    "جتا_زائدي": "math.cosh", "جب_زائدي": "math.sinh", "ظا_زائدي": "math.tanh",
    "م_جتا_زائدي": "math.acosh", "م_جب_زائدي": "math.asinh", "م_ظا_زائدي": "math.atanh",
    # لوغاريتمات وأس
    "لوغاريتم": "math.log", "لوغاريتم_2": "math.log2", "لوغاريتم_10": "math.log10",
    "لوغاريتم_زائد_واحد": "math.log1p", "أس": "math.exp", "أس_ناقص_واحد": "math.expm1",
    # قوة وجذور
    "جذر_صحيح": "math.isqrt",
    # تقريب
    "سقف": "math.ceil", "أرضي": "math.floor", "اقتطاع": "math.trunc",
    # نظرية الأعداد
    "مضروب": "math.factorial", "توافيق": "math.comb", "تباديل": "math.perm",
    "قاسم_مشترك": "math.gcd", "مضاعف_مشترك": "math.lcm", "جداء": "math.prod",
    # عوائم
    "مطلق_عشري": "math.fabs", "باقي_قسمة": "math.fmod", "كسر_صحيح": "math.modf",
    "تفكيك": "math.frexp", "ضرب_أس": "math.ldexp", "نسخ_الإشارة": "math.copysign",
    "التالي": "math.nextafter", "وحدة_الدقة": "math.ulp", "مجموع_دقيق": "math.fsum",
    "باقي": "math.remainder",
    # مقارنة
    "قريب_من": "math.isclose", "محدود": "math.isfinite", "لا_نهائي": "math.isinf", "ليس_رقم": "math.isnan",
    # هندسة
    "مسافة": "math.dist", "وتر": "math.hypot",
    # تحويل زوايا
    "درجات": "math.degrees", "راديان": "math.radians",
    # دوال خاصة
    "دالة_الخطأ": "math.erf", "دالة_الخطأ_المكملة": "math.erfc",
    "جاما": "math.gamma", "لوغاريتم_جاما": "math.lgamma",
}

MATH_PATTERN = r"(?<!\w)(" + "|".join(sorted(MATH_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
MATH_HELP = [
    "# مثلثات",
    "جتا/جب/ظا           - cos/sin/tan",
    "م_جتا/م_جب/م_ظا     - acos/asin/atan",
    "م_ظا2               - atan2",
    "# زائدي",
    "جتا_زائدي/جب_زائدي/ظا_زائدي     - cosh/sinh/tanh",
    "م_جتا_زائدي/م_جب_زائدي/م_ظا_زائدي - acosh/asinh/atanh",
    "# لوغاريتمات وأس",
    "لوغاريتم            - log",
    "لوغاريتم_2          - log2",
    "لوغاريتم_10         - log10",
    "لوغاريتم_زائد_واحد  - log1p",
    "أس                  - exp",
    "أس_ناقص_واحد       - expm1",
    "# جذور",
    "جذر_صحيح            - isqrt",
    "# تقريب",
    "سقف/أرضي/اقتطاع     - ceil/floor/trunc",
    "# نظرية الأعداد",
    "مضروب              - factorial",
    "توافيق              - comb",
    "تباديل              - perm",
    "قاسم_مشترك         - gcd",
    "مضاعف_مشترك        - lcm",
    "جداء                - prod",
    "# عوائم",
    "مطلق_عشري          - fabs",
    "باقي_قسمة          - fmod",
    "كسر_صحيح           - modf",
    "تفكيك              - frexp",
    "ضرب_أس              - ldexp",
    "نسخ_الإشارة        - copysign",
    "التالي              - nextafter",
    "وحدة_الدقة          - ulp",
    "مجموع_دقيق          - fsum",
    "باقي                - remainder",
    "# مقارنة",
    "قريب_من             - isclose",
    "محدود              - isfinite",
    "لا_نهائي            - isinf",
    "ليس_رقم            - isnan",
    "# هندسة",
    "مسافة               - dist",
    "وتر                - hypot",
    "# تحويل زوايا",
    "درجات/راديان        - degrees/radians",
    "# دوال خاصة",
    "دالة_الخطأ          - erf",
    "دالة_الخطأ_المكملة  - erfc",
    "جاما                - gamma",
    "لوغاريتم_جاما       - lgamma",
]

# Import detection
IMPORT_NAME = "math"
IMPORT_CHECK = "math\."
IMPORT_STATEMENT = "import math"

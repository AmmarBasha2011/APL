"""
APL - operator Library Functions
Transpiles Arabic keywords to Python operator module
"""

OPERATOR_FUNCS = {
    "عامل_جمع": "operator.add",
    "عامل_طرح": "operator.sub",
    "عامل_ضرب": "operator.mul",
    "عامل_قسمة": "operator.truediv",
    "عامل_قسمة_أرضية": "operator.floordiv",
    "عامل_باقي": "operator.mod",
    "عامل_أس": "operator.pow",
    "عامل_سالب": "operator.neg",
    "عامل_مطلق": "operator.abs",
    "مساواة_عامل": "operator.eq",
    "اختلاف_عامل": "operator.ne",
    "أصغر_عامل": "operator.lt",
    "أصغر_أو_يساوي_عامل": "operator.le",
    "أكبر_عامل": "operator.gt",
    "أكبر_أو_يساوي_عامل": "operator.ge",
    "عامل_نفي": "operator.not_",
    "عامل_و": "operator.and_",
    "عامل_أو": "operator.or_",
    "عامل_أو_حصري": "operator.xor",
    "جالب_عنصر": "operator.itemgetter",
    "جالب_خاصية": "operator.attrgetter",
    "حجم_تقريبي": "operator.length_hint",
    "بانتظار_الكل": "_apl_operator_all",
    "أي_من_الكل": "_apl_operator_any",
    "مقلوب_القيمة": "_apl_operator_invert",
    "قوة_مركبة": "_apl_operator_pow",
}

OPERATOR_PATTERN = r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(OPERATOR_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
OPERATOR_HELP = [
    "# operator - دوال المشغّلات كدوال",
    "عامل_جمع(2, 3)              - بديل عن lambda",
    "عامل_مطلق(-5)               - القيمة المطلقة",
    "جالب_عنصر(1)(['a','b','c'])  - استدعاء الدالة مباشرة",
    "عامل_أس(2, 10)              - 2**10",
]

# Import detection
IMPORT_NAME = "operator"
IMPORT_CHECK = r"operator\."
IMPORT_STATEMENT = "import operator"

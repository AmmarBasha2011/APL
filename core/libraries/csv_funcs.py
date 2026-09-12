"""
APL - CSV Library
Full CSV wrapper with Arabic keywords
"""

CSV_FUNCS = {
    # قراءة
    "اقرأ_csv": "csv.reader",
    "اقرأ_قاموس": "csv.DictReader",
    "اقرأ_ملف_csv": "open",
    
    # كتابة
    "اكتب_csv": "csv.writer",
    "اكتب_قاموس": "csv.DictWriter",
    "اكتب_ملف_csv": "open",
    
    # خصائص
    "فاصل": "delimiter",
    "اقتباس": "quotechar",
    "هروب": "escapechar",
    "سطر_جديد": "lineterminator",
    "اقتباس_نمط": "quoting",
    "تخطي_مسافات": "skipinitialspace",
    "صارم": "strict",
}

CSV_PATTERN = r"(?<!\w)(" + "|".join(sorted(CSV_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

CSV_HELP = [
    "# === القراءة ===",
    "اقرأ_csv(ملف)           - قراءة ملف CSV",
    "اقرأ_قاموس(ملف)         - قراءة كقاموس",
    "# === الكتابة ===",
    "اكتب_csv(ملف)           - كتابة ملف CSV",
    "اكتب_قاموس(ملف, حقول)   - كتابة قاموس",
    "# === الخصائص ===",
    "فاصل                   - الفاصل (عادةً , أو ;)",
    "اقتباس                  - حرف الاقتباس",
    "هروب                    - حرف الهروب",
]

IMPORT_NAME = "csv"
IMPORT_CHECK = "csv\."
IMPORT_STATEMENT = "import csv"

"""
APL - Statistics Library Functions
Transpiles Arabic statistics keywords to Python statistics module calls
"""

STATISTICS_FUNCS = {
    # نزعة مركزية (Central Tendency)
    "متوسط": "statistics.mean",
    "متوسط_حسابي": "statistics.mean",
    "وسيط": "statistics.median",
    "منوال": "statistics.mode",
    "متوسط_توافقي": "statistics.harmonic_mean",
    "متوسط_هندسي": "statistics.geometric_mean",
    "وسيط_منخفض": "statistics.median_low",
    "وسيط_مرتفع": "statistics.median_high",
    "وسيط_مجمع": "statistics.median_grouped",
    
    # تشتت (Dispersion)
    "تباين": "statistics.variance",
    "تباين_مجتمع": "statistics.pvariance",
    "انحراف_معياري": "statistics.stdev",
    "انحراف_معياري_مجتمع": "statistics.pstdev",
    "نطاق": "range",
    
    # ارتباط (Correlation) - for sequences
    "ارتباط": "statistics.correlation",
    "ميل": "statistics.linear_regression",
}

STATISTICS_PATTERN = "(" + "|".join(sorted(STATISTICS_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
STATISTICS_HELP = [
    "# نزعة مركزية (Central Tendency)",
    "متوسط(قائمة)           - المتوسط الحسابي",
    "متوسط_حسابي(قائمة)     - المتوسط الحسابي",
    "وسيط(قائمة)            - الوسيط",
    "منوال(قائمة)           - المنوال (أكثر قيمة تكراراً)",
    "متوسط_توافقي(قائمة)    - المتوسط التوافقي",
    "متوسط_هندسي(قائمة)     - المتوسط الهندسي",
    "وسيط_منخفض(قائمة)      - الوسيط المنخفض",
    "وسيط_مرتفع(قائمة)      - الوسيط المرتفع",
    "# تشتت (Dispersion)",
    "تباين(قائمة)           - التباين (عينة)",
    "تباين_مجتمع(قائمة)     - التباين (المجتمع)",
    "انحراف_معياري(قائمة)   - الانحراف المعياري (عينة)",
    "انحراف_معياري_مجتمع(قائمة) - الانحراف المعياري (المجتمع)",
    "# ارتباط (Correlation)",
    "ارتباط(س1, س2)         - معامل الارتباط",
    "ميل(س1, س2)            - الانحدار الخطي",
]

# Import detection
IMPORT_NAME = "statistics"
IMPORT_CHECK = "statistics\."
IMPORT_STATEMENT = "import statistics"

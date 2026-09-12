"""
APL - JSON Library Functions
Transpiles Arabic JSON keywords to Python json module calls
"""

JSON_FUNCS = {
    # مختصرات القراءة (Reading Shortcuts)
    "جسون": "json.loads",
    
    # مختصرات الكتابة (Writing Shortcuts)
    "جسون_تحويل": "json.dumps",
    
    # قراءة (Reading)
    "اقرأ_جسون": "json.loads",
    "من_جسون": "json.loads",
    
    # كتابة (Writing)
    "اكتب_جسون": "json.dumps",
    "ل_جسون": "json.dumps",
    
    # ملفات (Files)
    "من_ملف_جسون": "json.load",
    "لملف_جسون": "json.dump",
}

JSON_PATTERN = r"(?<!\w)(" + "|".join(sorted(JSON_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
JSON_HELP = [
    "# مختصرات (Shortcuts)",
    "جسون(نص)              - قراءة JSON من نص (مختصر)",
    "جسون_تحويل(بيانات)     - كتابة JSON لنص (مختصر)",
    "# قراءة (Reading)",
    "اقرأ_جسون(نص)         - قراءة JSON من نص",
    "من_جسون(نص)            - قراءة JSON من نص",
    "# كتابة (Writing)",
    "اكتب_جسون(بيانات)      - كتابة JSON لنص",
    "ل_جسون(بيانات)         - كتابة JSON لنص",
    "# ملفات (Files)",
    "من_ملف_جسون(ملف)       - قراءة من ملف JSON",
    "لملف_جسون(بيانات, ملف) - كتابة لملف JSON",
]

# Import detection
IMPORT_NAME = "json"
IMPORT_CHECK = "json\."
IMPORT_STATEMENT = "import json"

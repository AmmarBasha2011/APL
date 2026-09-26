"""
APL - Regular Expression Library Functions
Transpiles Arabic regex keywords to Python re module calls
"""

RE_FUNCS = {
    # بحث (Searching)
    "بحث_نمطي": "re.search",
    "بحث_كامل": "re.match",
    "بحث_شامل": "re.findall",
    "بحث_مكرر": "re.finditer",
    
    # استبدال (Substitution)
    "استبدل": "re.sub",
    "استبدل_عدد": "re.subn",
    
    # تقسيم (Splitting)
    "قسم_نمطي": "re.split",
    
    # تجميع (Groups)
    "مجموعة_نمطية": "re.group",
    "مجموعات_نمطية": "re.groups",
    
    # مطابقة (Matching)
    "مطابقة": "re.fullmatch",
    
    # تجميع النمط (Pattern compilation)
    "جمع_نمط": "re.compile",
    
    # هروب (Escaping)
    "هرب": "re.escape",
}

RE_PATTERN = r"(?<!\w)(" + "|".join(sorted(RE_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
RE_HELP = [
    "# بحث (Searching)",
    "بحث_نمطي(نمط, نص)     - بحث عن النمط في النص",
    "بحث_كامل(نمط, نص)     - مطابقة من البداية",
    "بحث_شامل(نمط, نص)     - كل التطابقات",
    "بحث_مكرر(نمط, نص)     - مكرر للتطابقات",
    "# استبدال (Substitution)",
    "استبدل(نمط, بديل, نص) - استبدال التطابقات",
    "استبدل_عدد(نمط, بديل, نص) - استبدال مع العدد",
    "# تقسيم (Splitting)",
    "قسم_نمطي(نمط, نص)     - تقسيم بالنمط",
    "# تجميع (Groups)",
    "مجموعة_نمطية(رقم)     - مجموعة محددة",
    "مجموعات_نمطية()       - كل المجموعات",
    "# مطابقة (Matching)",
    "مطابقة(نمط, نص)       - مطابقة كاملة",
    "# أخرى",
    "جمع_نمط(نمط)          - تجميع النمط (للأداء)",
    "هرب(نص)               - هروب الأحرف الخاصة",
]

# Common regex patterns (constants)
RE_CONSTANTS = {
    "نمط_رقم": "r'\\d'",
    "نمط_أرقام": "r'\\d+'",
    "نمط_حرف": "r'\\w'",
    "نمط_حروف": "r'\\w+'",
    "نمط_مسافة": "r'\\s'",
    "نمط_مسافات": "r'\\s+'",
    "نمط_أي_حرف": "r'.'",
    "نمط_بداية": "r'^'",
    "نمط_نهاية": "r'$'",
    "نمط_نقطة": "r'\\.'",
    "نمط_نجمة": "r'\\*'",
    "نمط_زائد": "r'\\+'",
    "نمط_علامة_استفهام": "r'\\?'",
}

RE_CONSTANT_PATTERN = r"(?<!\w)(" + "|".join(sorted(RE_CONSTANTS.keys(), key=len, reverse=True)) + r")(?!\s*\()(?!\w)"

# Import detection
IMPORT_NAME = "re"
IMPORT_CHECK = "re\."
IMPORT_STATEMENT = "import re"

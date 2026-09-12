"""
APL - Collections Library Functions
Transpiles Arabic collections keywords to Python collections module calls
"""

COLLECTIONS_FUNCS = {
    # أنواع خاصة (Specialized Types)
    "عداد": "collections.Counter",
    "قاموس_افتراضي": "collections.defaultdict",
    "قائمة_مزدوجة": "collections.deque",
    "صف_مسمى": "collections.namedtuple",
    "سلسلة_مرتبة": "collections.OrderedDict",
    
    # دوال (Functions)
    "عد_عناصر": "collections.Counter",
    "عنصر_أكثر": "collections.Counter.most_common",
    
    # فئات (Classes)
    "صف_انتظار": "collections.deque",
    "صف_انتظار_محدود": "collections.deque",
}

COLLECTIONS_PATTERN = r"(?<!\w)(" + "|".join(sorted(COLLECTIONS_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
COLLECTIONS_HELP = [
    "# أنواع خاصة (Specialized Types)",
    "عداد(تسلسل)           - عداد للعناصر (Counter)",
    "قاموس_افتراضي(نوع)    - قاموس بقيمة افتراضية",
    "قائمة_مزدوجة(تسلسل)   - قائمة مزدوجة الطرفين (deque)",
    "صف_مسمى(اسم, حقول)    - صف مسمى (namedtuple)",
    "سلسلة_مرتبة(قاموس)    - قاموس مرتب (OrderedDict)",
    "# دوال (Functions)",
    "عد_عناصر(تسلسل)       - عد العناصر (Counter)",
    "عنصر_أكثر(تسلسل, ن)  - أكثر العناصر تكراراً",
    "# فئات (Classes)",
    "صف_انتظار(تسلسل)      - صف انتظار (deque)",
    "صف_انتظار_محدود(تسلسل, حد) - صف محدود",
]

# Import detection
IMPORT_NAME = "collections"
IMPORT_CHECK = "collections\."
IMPORT_STATEMENT = "import collections"

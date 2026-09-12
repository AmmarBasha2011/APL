"""
APL - Advanced Python Features Library
Covers: Decorators, Metaclasses, Packages, Data Structures, Concurrency, Types, Descriptors
"""

ADVANCED_FUNCS = {
    # === Advanced Decorators ===
    "@wraps_دالة": "functools.wraps",
    "@يلتف": "functools.wraps",
    "@كاش_دالة": "functools.cache",
    "@خاصية_مخزنة_دالة": "functools.cached_property",
    "@توزيع_فردي": "functools.singledispatch",
    "@ترتيب_كامل": "functools.total_ordering",
    
    # === Metaclasses ===
    "ميتا_فئة": "type",
    "فئة_فوقية": "type",
    "Meta_فئة": "type",
    "ميتا": "metaclass",
    
    # === Package/Module System ===
    "init_حزمة": "__init__",
    "كل_الصادرات": "__all__",
    "رئيسي_ملف": "__main__",
    "حزمة": "__init__",
    "كل": "__all__",
    "رئيسي": "__main__",
    "مسار_بحث_حزم": "sys.path",
    
    # === Data Structures ===
    "كومة_دفعة": "heapq.heappush",
    "كومة_سحب": "heapq.heappop",
    "كومة_دفعة_وسحب": "heapq.heappushpop",
    "كومة_استبدال": "heapq.heapreplace",
    "كومة_بناء": "heapq.heapify",
    "كومة_دمج": "heapq.merge",
    "كومة_أكبر": "heapq.nlargest",
    "كومة_أصغر": "heapq.nsmallest",
    "بحث_ثنائي_إدراج": "bisect.insort",
    "بحث_ثنائي_يسار": "bisect.bisect_left",
    "بحث_ثنائي_يمين": "bisect.bisect_right",
    "مرجع_ضعيف_جديد": "weakref.ref",
    "مرجع_ضعيف_وكيل": "weakref.proxy",
    "مرجع_ضعيف_نهائي": "weakref.finalize",
    
    # === Concurrency ===
    "متعدد_المعالجات": "multiprocessing",
    "عملية_جديدة": "multiprocessing.Process",
    "Pool_عمليات": "multiprocessing.Pool",
    "مدير_عمليات": "multiprocessing.Manager",
    "أنبوب_عمليات": "multiprocessing.Pipe",
    "قيمة_مشتركة": "multiprocessing.Value",
    "ذاكرة_مشتركة": "multiprocessing.shared_memory",
    "مجموعة_ثريدات": "concurrent.futures.ThreadPoolExecutor",
    "مجموعة_عمليات_نظام": "concurrent.futures.ProcessPoolExecutor",
    "مستقبل_عملية": "concurrent.futures.Future",
    "عند_اكتمال": "concurrent.futures.as_completed",
    "عند_اكتمال_أي": "concurrent.futures.wait",
    "مستقبل_عند_اكتمال": "future.result",
    "مستقبل_استثناء": "future.exception",
    "مستقبل_ألغى": "future.cancel",
    "مستقبل_انتهى": "future.done",
    
    # === Type System ===
    "متغير_نوع_عام": "TypeVar",
    "بروتوكول_نوع": "Protocol",
    "عام_نوع": "Generic",
    "اختياري_نوع": "Optional",
    "اتحاد_نوع": "Union",
    "قائمة_نوع_عام": "List",
    "قاموس_نوع_عام": "Dict",
    "صف_نوع_عام": "Tuple",
    "مجموعة_نوع_عام": "Set",
    "قابل_للنداء_عام": "Callable",
    "أي_نوع_عام": "Any",
    "صف_مسمى_عام": "NamedTuple",
    "قاموس_مهيكل_عام": "TypedDict",
    "نوع_نوع": "Type",
    
    # === Descriptors ===
    "حصل_واصف_دالة": "__get__",
    "وضع_واصف_دالة": "__set__",
    "حذف_واصف_دالة": "__delete__",
    "وضع_اسم_دالة": "__set_name__",
    "فتحات_فئة": "__slots__",
    "خاصية_واصف": "property",
    "دالة_فئة_واصف": "classmethod",
    "دالة_ثابتة_واصف": "staticmethod",
    "خاصية_مخزنة_مؤقتا_دالة": "cached_property",
}

ADVANCED_PATTERN = r"(?<!\w)(" + "|".join(sorted(ADVANCED_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

ADVANCED_HELP = [
    "# === Advanced Decorators ===",
    "@wraps_دالة(دالة)       - الحفاظ على البيانات الوصفية",
    "@يلتف(دالة)             - يلتف (عربي)",
    "@كاش_دالة               - cache",
    "@خاصية_مخزنة_دالة       - cached_property",
    "@ترتيب_كامل            - total_ordering",
    "# === Metaclasses ===",
    "ميتا_فئة                  - type",
    "فئة_فوقية               - type",
    "# === Package/Module System ===",
    "init_حزمة               - __init__",
    "كل_الصادرات              - __all__",
    "رئيسي_ملف               - __main__",
    "# === Data Structures ===",
    "كومة_دفعة(كومة, عنصر)   - heappush",
    "كومة_سحب(كومة)          - heappop",
    "كومة_بناء(قائمة)        - heapify",
    "بحث_ثنائي_إدراج(قائمة, عنصر) - insort",
    "مرجع_ضعيف_جديد(كائن)    - weakref.ref",
    "# === Concurrency ===",
    "متعدد_المعالجات          - multiprocessing",
    "عملية_جديدة(هدف)        - multiprocessing.Process",
    "Pool_عمليات             - multiprocessing.Pool",
    "مجموعة_ثريدات           - ThreadPoolExecutor",
    "مجموعة_عمليات_نظام      - ProcessPoolExecutor",
    "عند_اكتمال(مستقبلات)    - as_completed",
    "# === Type System ===",
    "متغير_نوع_عام(اسم)      - TypeVar",
    "بروتوكول_نوع            - Protocol",
    "عام_نوع                - Generic",
    "اتحاد_نوع(نوع1, نوع2)  - Union",
    "قاموس_مهيكل_عام        - TypedDict",
    "# === Descriptors ===",
    "حصل_واصف_دالة(ذات, كائن, نوع) - __get__",
    "وضع_واصف_دالة(ذات, كائن, قيمة) - __set__",
    "فتحات_فئة = (...)        - __slots__",
]

IMPORT_NAME = "advanced"
IMPORT_CHECK = "(functools|multiprocessing|concurrent|typing|heapq|bisect|weakref)"
IMPORT_STATEMENT = "import functools, multiprocessing, concurrent.futures, typing, heapq, bisect, weakref"

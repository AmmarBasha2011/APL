"""
APL - Threading Library
Full threading wrapper with Arabic keywords
"""

THREADING_FUNCS = {
    # إنشاء ثريد
    "ثريد": "threading.Thread",
    "أنشئ_ثريد": "threading.Thread",
    "مهمة": "threading.Thread",
    "أنشئ_مهمة": "threading.Thread",
    "عامل": "threading.Thread",
    
    # التحكم في الثريد
    "ابدأ": "thread.start",
    "انتظر": "thread.join",
    "ألغى": "thread.cancel",
    
    # حالة الثريد
    "نشط": "thread.is_alive",
    "اسم": "thread.name",
    "دايمون": "thread.daemon",
    
    # القفل (Lock)
    "قفل": "threading.Lock",
    "أنشئ_قفل": "threading.Lock",
    "امتلك": "lock.acquire",
    "أطلق": "lock.release",
    
    # الإشارات (Semaphore)
    "إشارة": "threading.Semaphore",
    "أنشئ_إشارة": "threading.Semaphore",
    
    # الأحداث (Event)
    "حدث": "threading.Event",
    "أنشئ_حدث": "threading.Event",
    "انتظر_حدث": "event.wait",
    "أطلق_حدث": "event.set",
    "امسح_حدث": "event.clear",
    
    # المؤقت (Timer)
    "مؤقت": "threading.Timer",
    "أنشئ_مؤقت": "threading.Timer",
    
    # الثريد الحالي
    "ثريد_حالي": "threading.current_thread",
    "الثريد_الحالي": "threading.current_thread",
    
    # عداد الثريدات
    "عداد_ثريدات": "threading.active_count",
    
    # النوم
    "نوم": "time.sleep",
    "انتظر_ثانية": "time.sleep",
}

THREADING_PATTERN = r"(?<!\w)(" + "|".join(sorted(THREADING_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

THREADING_HELP = [
    "# === إنشاء ثريد ===",
    "ثريد(هدف=دالة)        - إنشاء ثريد",
    "مهمة(هدف=دالة)         - إنشاء مهمة",
    "أنشئ_ثريد(هدف=دالة)   - إنشاء ثريد",
    "# === التحكم ===",
    "ابدأ()                 - بدء الثريد",
    "انتظر()                - انتظار انتهاء الثريد",
    "نشط()                  - هل الثريد نشط",
    "# === القفل ===",
    "قفل()                   - إنشاء قفل",
    "امتلك()                - امتلاك القفل",
    "أطلق()                - إطلاق القفل",
    "# === الحدث ===",
    "حدث()                   - إنشاء حدث",
    "انتظر_حدث()            - انتظار الحدث",
    "أطلق_حدث()            - إطلاق الحدث",
    "# === المؤقت ===",
    "مؤقت(ثوان, دالة)      - مؤقت",
    "نوم(ثوان)              - نوم لثواني",
]

IMPORT_NAME = "threading"
IMPORT_CHECK = "threading\."
IMPORT_STATEMENT = "import threading"

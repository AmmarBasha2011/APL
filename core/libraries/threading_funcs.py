"""
APL - Threading Library
Full threading wrapper with Arabic keywords
"""

THREADING_FUNCS = {
    # إنشاء ثريد
    "ثريد": "threading.Thread",
    "أنشئ_ثريد": "threading.Thread",
    "مهمة_خيوط": "threading.Thread",
    "أنشئ_مهمة_خيوط": "threading.Thread",
    "عامل": "threading.Thread",
    
    # التحكم في الثريد
    "ابدأ_خيوط": "thread.start",
    "انتظر_خيوط": "thread.join",
    "ألغى_خيوط": "thread.cancel",
    
    # حالة الثريد
    "نشط": "thread.is_alive",
    "اسم": "thread.name",
    "دايمون": "thread.daemon",
    
    # القفل (Lock)
    "قفل_خيوط": "threading.Lock",
    "أنشئ_قفل": "threading.Lock",
    "امتلك_خيوط": "lock.acquire",
    "أطلق_خيوط": "lock.release",
    
    # الإشارات (Semaphore)
    "إشارة_خيوط": "threading.Semaphore",
    "أنشئ_إشارة": "threading.Semaphore",
    
    # الأحداث (Event)
    "حدث_خيوط": "threading.Event",
    "أنشئ_حدث": "threading.Event",
    "انتظر_حدث_خيوط": "event.wait",
    "أطلق_حدث_خيوط": "event.set",
    "امسح_حدث_خيوط": "event.clear",
    
    # المؤقت (Timer)
    "مؤقت_خيوط": "threading.Timer",
    "أنشئ_مؤقت_خيوط": "threading.Timer",
    
    # الثريد الحالي
    "ثريد_حالي": "threading.current_thread",
    "الثريد_الحالي": "threading.current_thread",
    
    # عداد الثريدات
    "عداد_ثريدات": "threading.active_count",
    
    # النوم
    "نوم_خيوط": "time.sleep",
    "انتظر_ثانية": "time.sleep",
}

THREADING_PATTERN = r"(?<![\w.\u0600-\u06FF])(" + "|".join(sorted(THREADING_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

THREADING_HELP = [
    "# === إنشاء ثريد ===",
    "ثريد(هدف=دالة)        - إنشاء ثريد",
    "مهمة_خيوط(هدف=دالة)         - إنشاء مهمة_خيوط",
    "أنشئ_ثريد(هدف=دالة)   - إنشاء ثريد",
    "# === التحكم ===",
    "ابدأ_خيوط()                 - بدء الثريد",
    "انتظر_خيوط()                - انتظار انتهاء الثريد",
    "نشط()                  - هل الثريد نشط",
    "# === القفل ===",
    "قفل_خيوط()                   - إنشاء قفل_خيوط",
    "امتلك_خيوط()                - امتلاك القفل",
    "أطلق_خيوط()                - إطلاق القفل",
    "# === الحدث ===",
    "حدث_خيوط()                   - إنشاء حدث_خيوط",
    "انتظر_حدث_خيوط()            - انتظار الحدث",
    "أطلق_حدث_خيوط()            - إطلاق الحدث",
    "# === المؤقت ===",
    "مؤقت_خيوط(ثوان, دالة)      - مؤقت_خيوط",
    "نوم_خيوط(ثوان)              - نوم_خيوط لثواني",
]

IMPORT_NAME = "threading"
IMPORT_CHECK = "threading\."
IMPORT_STATEMENT = "import threading"

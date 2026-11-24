# 83 · التسجيل — logging
# Structured logging with the logging library
#
# Run:  python apl.py examples/83-syslib-logging.apl

اطبع "=== التسجيل ==="
سجل_تهيئة(level="INFO")
المتغير س = احصل_على_مسجّل("apl.demo")
س.مسجّل_معلومات("رسالة معلومات من APL")
س.مسجّل_تحذير("رسالة تحذير")
س.مسجّل_خطأ("رسالة خطأ")
س.مسجّل_تصحيح("لا تظهر عند مستوى INFO")

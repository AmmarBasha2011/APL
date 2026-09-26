# مثال 35 — إعداد السجلات
# Logging Setup
# Demonstrates: logging library, log levels, formatted messages
#
# Run:  python apl.py examples/35-logging-setup.apl

سجل_تهيئة(level="INFO", format="%(levelname)s: %(message)s")

سجل_معلومات("سجل معلومات عادي")
سجل_تحذير("هذا تحذير")
سجل_خطأ("هذا خطأ")
سجل_حرج("هذه رسالة حرجة")

اطبع ""
سجل_معلومات("رسالة مخصصة: %s", "تطبيقي")
سجل_معلومات("رقم: %d و نسبة: %.2f", 42, 3.14159)

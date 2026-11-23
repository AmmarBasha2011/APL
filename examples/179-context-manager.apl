# مثال 179 — مدير السياق مع الملفات
# Context managers with files
# Demonstrates: مع ... مثل، فتح
#
# Run:  python apl.py examples/179-context-manager.apl

المتغير مسار = "/tmp/apl_179.txt"

مع فتح(مسار, "w") مثل ملف:
    ملف.write("السطر الأول\n")
    ملف.write("السطر الثاني\n")

مع فتح(مسار, "r") مثل ملف:
    المتغير محتوى = ملف.read()

اطبع "المحتوى:", محتوى.تقليم()
اطبع "عدد الأسطر:", طول(محتوى.splitlines())

احذف_ملف(مسار)

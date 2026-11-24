# مثال 363 — عكس نص بالعودية
# Recursive string reverse
# Demonstrates: تقسيم المشكلة
#
# Run:  python apl.py examples/363-reverse-string-rec.apl

دالة اعكس(نص_الدخل):
    لو طول(نص_الدخل) <= 1:
        ارجع نص_الدخل
    ارجع اعكس(نص_الدخل[1:]) + نص_الدخل[0]

اطبع اعكس("مرحبا")
اطبع اعكس("APL")

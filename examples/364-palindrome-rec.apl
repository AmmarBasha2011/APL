# مثال 364 — فحص التناظر بالعودية
# Recursive palindrome check
# Demonstrates: مقارنة الطرفين
#
# Run:  python apl.py examples/364-palindrome-rec.apl

دالة متناظر(نص_الدخل):
    لو طول(نص_الدخل) <= 1:
        ارجع صواب
    لو نص_الدخل[0] != نص_الدخل[-1]:
        ارجع خطأ
    ارجع متناظر(نص_الدخل[1:طول(نص_الدخل) - 1])

اطبع "level:", متناظر("level")
اطبع "abcba:", متناظر("abcba")
اطبع "hello:", متناظر("hello")

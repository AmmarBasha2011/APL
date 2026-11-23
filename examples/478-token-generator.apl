# مثال 478 — مولد رموز الجلسات
# Session token generator
# Demonstrates: رموز عشوائية طويلة
#
# Run:  python apl.py examples/478-token-generator.apl

بذرة(21)
المتغير أحرف = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

دالة رمز_جلسة(طول_مطلوب):
    المتغير ناتج = ""
    لكل _ في نطاق(طول_مطلوب):
        ناتج = ناتج + أحرف[عشوائي_عدد(0, طول(أحرف) - 1)]
    ارجع ناتج

اطبع رمز_جلسة(16)
اطبع رمز_جلسة(32)

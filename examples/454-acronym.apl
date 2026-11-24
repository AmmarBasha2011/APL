# مثال 454 — مولد الاختصارات
# Acronym maker
# Demonstrates: أول حرف من كل كلمة
#
# Run:  python apl.py examples/454-acronym.apl

دالة اختصار(عبارة):
    المتغير ناتج = ""
    لكل كلمة في عبارة.تقسيم(" "):
        لو طول(كلمة) > 0:
            ناتج = ناتج + كلمة[0].علوي()
    ارجع ناتج

اطبع اختصار("as soon as possible")
اطبع اختصار("for your information")

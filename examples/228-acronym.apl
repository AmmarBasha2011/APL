# مثال 228 — توليد الاختصارات
# Acronym generator
# Demonstrates: أول حرف من كل كلمة
#
# Run:  python apl.py examples/228-acronym.apl

دالة اختصار(عبارة):
    المتغير حروف = []
    لكل كلمة في عبارة.تقسيم(" "):
        لو طول(كلمة) > 0:
            حروف.أضف(كلمة[0])
    ارجع "".ضم(حروف).علوي()

اطبع "as soon as possible ->", اختصار("as soon as possible")
اطبع "for your information ->", اختصار("for your information")
اطبع "arabic programming language ->", اختصار("arabic programming language")

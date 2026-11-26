# مثال 2133 — عناوين مع إبقاء الكلمات الصغيرة
# Title case with small words
# Demonstrates: نصوص
#
# Run:  python apl.py examples/2133-title-case-keep-small-words-lower.apl

# # القائمة a وan وthe وof وand وin وon
# # أول كلمة تكبر دائما

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة عنوان(س):
  صغيرة = ["a", "an", "the", "of", "and", "in", "on"]
  خرج = []
  لكل ك في نطاق(طول(س.split())):
    ك_ = س.split()[ك]
    لو ك > 0 و (ك_ في صغيرة):
      خرج = خرج + [ك_]
    والا:
      خرج = خرج + [ك_.capitalize()]
  ارجع " ".join(خرج)

تأكد_يساوي(عنوان("the lord of the rings"), "The Lord of the Rings", "ثلاثة")
تأكد_يساوي(عنوان("war and peace"), "War and Peace", "اثنان")
تأكد_يساوي(عنوان("a tale of two cities"), "A Tale of Two Cities", "أربعة")

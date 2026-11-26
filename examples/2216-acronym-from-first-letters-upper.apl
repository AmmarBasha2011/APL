# مثال 2216 — اختصار من الأحرف الأولى
# Acronym from first letters
# Demonstrates: نصوص
#
# Run:  python apl.py examples/2216-acronym-from-first-letters-upper.apl

# # ندخل النص
# # ونقارن النتيجة

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ن):
  ر = ""
  لكل و2 في ن.split():
    ر = ر + chr(ord(و2[0]) - 32)
  ارجع ر

تأكد_يساوي(ف("portable network graphics"), "PNG", "حالة 1")
تأكد_يساوي(ف("as soon as possible"), "ASAP", "حالة 2")
تأكد_يساوي(ف("a b c"), "ABC", "حالة 3")

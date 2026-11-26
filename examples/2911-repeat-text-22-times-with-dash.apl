# مثال 2911 — تكرار النص 22 مرات بشرطة
# Repeat text 22 times
# Demonstrates: نصوص
#
# Run:  python apl.py examples/2911-repeat-text-22-times-with-dash.apl

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
  ر = []
  لكل ي في نطاق(22):
    ر = ر + [ن]
  ارجع "-".join(ر)

تأكد_يساوي(ف("a"), "a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a", "حالة 1")
تأكد_يساوي(ف("ab"), "ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab", "حالة 2")
تأكد_يساوي(ف("xyz"), "xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz", "حالة 3")

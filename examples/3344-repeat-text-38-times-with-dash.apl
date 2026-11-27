# مثال 3344 — تكرار النص 38 مرات بشرطة
# Repeat text 38 times
# Demonstrates: نصوص
#
# Run:  python apl.py examples/3344-repeat-text-38-times-with-dash.apl

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
  لكل ي في نطاق(38):
    ر = ر + [ن]
  ارجع "-".join(ر)

تأكد_يساوي(ف("a"), "a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a-a", "حالة 1")
تأكد_يساوي(ف("ab"), "ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab-ab", "حالة 2")
تأكد_يساوي(ف("xyz"), "xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz-xyz", "حالة 3")

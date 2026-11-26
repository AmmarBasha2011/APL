# مثال 2314 — عكس ترتيب الكلمات
# Reverse word order
# Demonstrates: نصوص
#
# Run:  python apl.py examples/2314-reverse-word-order-in-text.apl

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
  ك = ن.split()
  ك.reverse()
  ارجع " ".join(ك)

تأكد_يساوي(ف("hello world"), "world hello", "حالة 1")
تأكد_يساوي(ف("abc"), "abc", "حالة 2")
تأكد_يساوي(ف("a b c"), "c b a", "حالة 3")
تأكد_يساوي(ف("one two three four"), "four three two one", "حالة 4")

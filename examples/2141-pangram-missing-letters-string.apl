# مثال 2141 — الأحرف الناقصة لتصبح الجملة بانجرام
# Pangram missing letters
# Demonstrates: نصوص
#
# Run:  python apl.py examples/2141-pangram-missing-letters-string.apl

# # نمر على الأبجدية
# # ونفحص وجود كل حرف

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ناقصة(س):
  س = س.lower()
  خرج = ""
  لكل ح في "abcdefghijklmnopqrstuvwxyz":
    لو (ح في س) == خطأ:
      خرج = خرج + ح
  ارجع خرج

تأكد_يساوي(ناقصة("the quick brown fox"), "adgjlmpsvyz", "ناقصة")
تأكد_يساوي(ناقصة("The quick brown fox jumps over the lazy dog"), "", "كاملة")

# مثال 1242 — عدد إلى إنجليزية
# Integer to English words
# Demonstrates: تقسيم لثلاثيات
#
# Run:  python apl.py examples/1242-integer-to-english.apl

# نقسم العدد إلى مجموعات من ثلاثة أرقام
# ونضيف Thousand وMillion وBillion

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ثلاثة(ن):
  احاد = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
  عشرات = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
  اجزاء = []
  لو ن >= 100:
    اجزاء.ألحق(احاد[ن // 100])
    اجزاء.ألحق("Hundred")
    ن = ن % 100
  لو ن >= 20:
    اجزاء.ألحق(عشرات[ن // 10])
    ن = ن % 10
  لو ن > 0:
    اجزاء.ألحق(احاد[ن])
  ارجع " ".join(اجزاء)

دالة بالكلمات(ن):
  لو ن == 0:
    ارجع "Zero"
  اسماء = ["", "Thousand", "Million", "Billion"]
  اجزاء = []
  ع = 0
  طالما ن > 0:
    ب = ن % 1000
    لو ب > 0:
      ق = ثلاثة(ب)
      لو اسماء[ع] != "":
        ق = ق + " " + اسماء[ع]
      اجزاء.insert(0, ق)
    ن = ن // 1000
    ع = ع + 1
  ارجع " ".join(اجزاء)

تأكد_يساوي(بالكلمات(123), "One Hundred Twenty Three", "مئة وثلاثة وعشرون")
تأكد_يساوي(بالكلمات(12345), "Twelve Thousand Three Hundred Forty Five", "آلاف")
تأكد_يساوي(بالكلمات(1000000), "One Million", "مليون")
تأكد_يساوي(بالكلمات(0), "Zero", "صفر")
تأكد_يساوي(بالكلمات(1000010), "One Million Ten", "مليون وعشرة")

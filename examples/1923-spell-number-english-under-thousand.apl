# مثال 1923 — كتابة عدد بالكلمات الإنجليزية
# Number to English words
# Demonstrates: نصوص
#
# Run:  python apl.py examples/1923-spell-number-english-under-thousand.apl

# جدول للأعداد حتى ١٩
# جدول للعشرات

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة كلمات(ن):
  صغير = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
  عشرات = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
  لو ن < 20:
    ارجع صغير[ن]
  لو ن < 100:
    لو ن % 10 == 0:
      ارجع عشرات[ن // 10]
    ارجع عشرات[ن // 10] + "-" + صغير[ن % 10]
  لو ن % 100 == 0:
    ارجع صغير[ن // 100] + " hundred"
  ارجع صغير[ن // 100] + " hundred " + كلمات(ن % 100)

تأكد_يساوي(كلمات(7), "seven", "آحاد")
تأكد_يساوي(كلمات(42), "forty-two", "عشرات")
تأكد_يساوي(كلمات(300), "three hundred", "مئات")
تأكد_يساوي(كلمات(115), "one hundred fifteen", "مختلط")

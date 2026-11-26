# مثال 1793 — العدد بالكلمات الإنجليزية
# Number to English words under 100
# Demonstrates: ترميز
#
# Run:  python apl.py examples/1793-number-to-english-words-small.apl

# جداول للآحاد والعشرات
# نربط العشرة بالوحدة

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة بالكلمات(ن):
  آحاد = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  عشرات = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  لو ن < 20:
    ارجع آحاد[ن]
  لو ن % 10 == 0:
    ارجع عشرات[ن // 10]
  ارجع عشرات[ن // 10] + "-" + آحاد[ن % 10]

تأكد_يساوي(بالكلمات(7), "seven", "سبعة")
تأكد_يساوي(بالكلمات(40), "forty", "أربعون")
تأكد_يساوي(بالكلمات(99), "ninety-nine", "تسعة وتسعون")
تأكد_يساوي(بالكلمات(15), "fifteen", "خمسة عشر")

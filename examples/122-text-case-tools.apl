# مثال 122 — أدوات الحالة والفحص في النصوص
# Case and inspection string tools
# Demonstrates: علوي، سفلي، بداية، نهاية، تقليم، استبدال
#
# Run:  python apl.py examples/122-text-case-tools.apl

المتغير نص = "  Ammar Programming Language  "
اطبع "الأصل: [", نص, "]"
اطبع "مقلم: [", نص.تقليم(), "]"
اطبع "علوي:", نص.علوي()
اطبع "سفلي:", نص.سفلي()
اطبع "يبدأ بـ Ammar؟", نص.تقليم().بداية("Ammar")
اطبع "ينتهي بـ Language؟", نص.تقليم().نهاية("Language")
اطبع "استبدال:", نص.تقليم().استبدال("Programming", "Coding")
اطبع "عدد حرف a:", نص.عد("a")

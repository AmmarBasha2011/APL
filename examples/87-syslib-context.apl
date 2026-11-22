# 87 · السياق والنصوص — contextvars وshlex وfilecmp وtypes
# Context copies, shell-style parsing, file comparison and simple namespaces
#
# Run:  python apl.py examples/87-syslib-context.apl

اطبع "=== السياق ==="
المتغير س = انسخ_السياق()
اطبع "السياق موجود؟", س != لا_شيء

اطبع "=== تحليل سطر أوامر ==="
اطبع "الحجج:", حلل_سطراً("apl.py --طباعة ملف.txt")
اطبع "اقتباس:", اقتبس_حجة("ملف به مسافة")

اطبع "=== النطاق ==="
المتغير ن = نطاق_اسم_بسيط(اسم="APL", عدد=4)
اطبع "النطاق:", ن.اسم, ن.عدد

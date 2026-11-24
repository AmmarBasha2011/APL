# 510 · الأدوات العميقة — utildeep
# dateutil / pytz / psutil
#
# Run:  python apl.py examples/510-utildeep.apl

اطبع "=== تحليل ISO ==="
اطبع أدوات_isoparse("2026-01-15T10:30:00")

اطبع "=== فروق نسبية ==="
المتغير ف = أدوات_ريلاتيفيديلتا(months=2)
اطبع "الشهور:", ف.months

# مثال 33 — القوائم فهم comprehensions
# List Comprehensions
# Demonstrates: list comprehensions, filtering, conditions inline
#
# Run:  python apl.py examples/33-comprehension-examples.apl

المتغير الأرقام = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

اطبع "=== قوائم الفهم (Comprehensions) ==="
اطبع ""
اطبع "الأصلية: " + نص(الأرقام)
اطبع "مضروبة في 2: " + نص([x * 2 for x in الأرقام])
اطبع "الأعداد الفردية: " + نص([x for x in الأرقام if x % 2 == 1])
اطبع "الأعداد الكبيرة (>{5}): " + نص([x for x in الأرقام if x > 5])
اطبع "مربعات الزوجية: " + نص([x * x for x in الأرقام if x % 2 == 0])
اطبع ""
اطبع "--- مع النصوص ---"
المتغير الكلمات = ["apple", "banana", "cherry", "date"]
اطبع "بالحروف الكبيرة: " + نص([w.upper() for w in الكلمات])
اطبع "الطويلة فقط (>5): " + نص([w for w in الكلمات if len(w) > 5])

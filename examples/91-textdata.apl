# 91 · النصوص والبيانات — textdata
# pathspec / attrs / frozenlist / starlette / PIL
#
# Run:  python apl.py examples/91-textdata.apl

اطبع "=== القوائم المجمّدة ==="
المتغير ق = مجمّد_قائمة_2()
ق.أضف_ذيلياً(1)
ق.أضف_ذيلياً(2)
اطبع "العناصر:", ق

اطبع "=== العدّ ==="
اطبع "الطول:", طول(ق)

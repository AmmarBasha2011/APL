# 504 · التخزين العميق — storedeep
# redis-py
#
# Run:  python apl.py examples/504-storedeep.apl

اطبع "=== تحليل روابط redis ==="
المتغير م = مخزن_اتصال_حلل_رابط_2("redis://localhost:6379/0")
اطبع "المضيف:", م["host"]
اطبع "المنفذ:", م["port"]
اطبع "قاعدة البيانات:", م["db"]

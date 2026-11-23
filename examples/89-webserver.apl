# 89 · الخوادم — webserver
# uvicorn / click / anyio / h11 / httpx
#
# Run:  python apl.py examples/89-webserver.apl

اطبع "=== الخادم ==="
المتغير إ = إعداد_2("app:app", port=8000)
اطبع "رقم المنفذ:", إ.port

اطبع "=== المهام ==="
اطبع "مصنع المهام:", إنشاء_مهمة_مجموعة != لا_شيء

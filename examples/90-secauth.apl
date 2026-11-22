# 90 · الأمان والمصادقة — secauth
# cryptography / jinja2 / jsonschema / jwt / cffi
#
# Run:  python apl.py examples/90-secauth.apl

اطبع "=== التحقق من المخطط ==="
اطبع جيسون_مخطط_تحقق({"a": 1}, {"type": "object"})

اطبع "=== القوالب ==="
المتغير ب = جينجا_بيئة()
اطبع "البيئة جاهزة؟", ب != لا_شيء

# 507 · النماذج والتحقق العميق — datadeep
# pydantic / jsonschema
#
# Run:  python apl.py examples/507-datadeep.apl

اطبع "=== pydantic ==="
المتغير م = نوع_مكيّف(int)
اطبع "تحويل نص لعدد:", م.validate_python("42")
اطبع "الإصدار:", نماذج_VERSION

اطبع "=== jsonschema ==="
المتغير ق = مسودة_7_متحقق({"type": "object"})
اطبع "كائن صالح؟", ق.is_valid({"a": 1})
اطبع "عدد صالح؟", ق.is_valid(5)

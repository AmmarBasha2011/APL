# 509 · الأمان العميق — secdeep
# cryptography / cffi / google
#
# Run:  python apl.py examples/509-secdeep.apl

اطبع "=== Fernet ==="
المتغير م = فيرنيت_توليد_مفتاح()
اطبع "طول المفتاح:", طول(م)

اطبع "=== cffi ==="
المتغير ف = أمان_FFI()
اطبع أمان_FFI_من_2(ف, "int")

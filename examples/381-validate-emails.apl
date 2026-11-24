# مثال 381 — التحقق من قائمة بريدات
# Validate email list
# Demonstrates: نمط بريد كامل التطابق
#
# Run:  python apl.py examples/381-validate-emails.apl

دالة بريد_صالح(بريد):
    المتغير م = بحث_نمطي("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.][A-Za-z][A-Za-z]+$", بريد)
    ارجع م != لا_شيء

المتغير قائمة = ["ahmed@example.com", "خطأ@بلا", "sara@company.org", "no-at.com", "x@y.z"]
لكل ب in قائمة:
    لو بريد_صالح(ب):
        اطبع "صالح:", ب
    الا:
        اطبع "مرفوض:", ب

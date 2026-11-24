# مثال 379 — تجميع نتائج متنوعة
# Gather mixed results
# Demonstrates: اجمع مع مهام مختلفة
#
# Run:  python apl.py examples/379-async-gather-mixed.apl

async def جلب_مستخدم():
    await نوم(0.01)
    return {"اسم": "أحمد"}

async def جلب_طلبات():
    await نوم(0.02)
    return [1, 2, 3]

async def جلب_إشعارات():
    await نوم(0.005)
    return ["رسالة", "تنبيه"]

async def الرئيسية():
    المتغير نتائج = await اجمع(جلب_مستخدم(), جلب_طلبات(), جلب_إشعارات())
    اطبع "المستخدم:", نتائج[0]
    اطبع "الطلبات:", نتائج[1]
    اطبع "الإشعارات:", نتائج[2]

شغل_تزامن(الرئيسية())

# مثال 172 — تشغيل مهام متوازية وتجميع نتائجها
# Parallel tasks with gather
# Demonstrates: اجمع، شغل_تزامن، أنشئ_مهمة
#
# Run:  python apl.py examples/172-asyncio-gather.apl

async def جلب(رقم):
    await نوم(0.01)
    return رقم * رقم

async def الرئيسية():
    المتغير نتائج = await اجمع(جلب(1), جلب(2), جلب(3), جلب(4))
    اطبع "المربعات:", نتائج

شغل_تزامن(الرئيسية())

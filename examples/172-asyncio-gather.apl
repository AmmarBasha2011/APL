# مثال 172 — تشغيل مهام متوازية وتجميع نتائجها
# Parallel tasks with gather
# Demonstrates: اجمع، شغل_تزامن، أنشئ_مهمة
#
# Run:  python apl.py examples/172-asyncio-gather.apl

async def get(رقم):
    await نوم(0.01)
    return رقم * رقم

async def الرئيسية():
    المتغير نتائج = await اجمع(get(1), get(2), get(3), get(4))
    اطبع "المربعات:", نتائج

شغل_تزامن(الرئيسية())

# مثال 372 — قائمة مهام بأسماء
# Named async tasks
# Demonstrates: أنشئ_مهمة، تتبع النتائج
#
# Run:  python apl.py examples/372-async-tasks-list.apl

async def عامل(رقم):
    await نوم(0.01)
    return "عامل " + نص(رقم) + " أنهى"

async def الرئيسية():
    المتغير مهام = []
    لكل ي في نطاق(3):
        مهام.أضف(أنشئ_مهمة(عامل(ي + 1)))
    لكل م in مهام:
        اطبع await م

شغل_تزامن(الرئيسية())

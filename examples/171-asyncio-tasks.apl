# مثال 171 — مهام غير متزامنة
# Async tasks
# Demonstrates: شغل_تزامن، نوم، async def، await
#
# Run:  python apl.py examples/171-asyncio-tasks.apl

async def مهمة(اسم, ثوان):
    اطبع "بدأت:", اسم
    await نوم(ثوان)
    اطبع "انتهت:", اسم
    return اسم

شغل_تزامن(مهمة("تنزيل", 0.05))
شغل_تزامن(مهمة("معالجة", 0.01))

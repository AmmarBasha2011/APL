# مثال 376 — مؤقت خيط
# Thread timer
# Demonstrates: تأجيل تنفيذ
#
# Run:  python apl.py examples/376-thread-timer.apl

دالة رن():
    اطبع "رن المنبه!"

المتغير مؤقت = أنشئ_مؤقت_خيوط(0.05, رن)
مؤقت.start()
اطبع "المنبه مضبوط..."
مؤقت.join()
اطبع "انتهى البرنامج."

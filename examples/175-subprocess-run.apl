# مثال 175 — تشغيل أوامر النظام
# Running system commands
# Demonstrates: أنشئ_عملية_أوامر
#
# Run:  python apl.py examples/175-subprocess-run.apl

المتغير ن = أنشئ_عملية_أوامر(["echo", "مرحبا من APL"], capture_output=True, text=True)
اطبع "رمز الخروج:", ن.returncode
اطبع "المخرجات:", ن.stdout.تقليم()

المتغير م = أنشئ_عملية_أوامر(["echo", "1 + 1 = 2"], capture_output=True, text=True)
اطبع "حساب:", م.stdout.تقليم()

# مثال 148 — صف انتظار مهام الطباعة
# Printer job queue with deque
# Demonstrates: قائمة_مزدوجة، append، popleft، appendleft
#
# Run:  python apl.py examples/148-deque-printer.apl

المتغير صف = قائمة_مزدوجة()
صف.append("مهمة 1: تقرير")
صف.append("مهمة 2: صور")
صف.append("مهمة 3: عقد")
صف.appendleft("مهمة عاجلة: تأشيرة")

اطبع "عدد المهام:", طول(صف)
طالما طول(صف) > 0:
    اطبع "تُطبع الآن:", صف.popleft()

اطبع "الصف فارغ؟", طول(صف) == 0

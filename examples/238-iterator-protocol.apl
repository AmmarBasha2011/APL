# مثال 238 — مكرر مخصص (عداد تنازلي)
# Custom iterator (countdown)
# Demonstrates: صنف يعمل كمكرر في لكل
#
# Run:  python apl.py examples/238-iterator-protocol.apl

صنف عد_تنازلي:
    دالة_إنشاء(ذات, من):
        ذات.حالي = من

    دالة __iter__(ذات):
        ارجع ذات

    دالة __next__(ذات):
        لو ذات.حالي <= 0:
            raise StopIteration
        ذات.حالي = ذات.حالي - 1
        ارجع ذات.حالي + 1

لكل ن في عد_تنازلي(5):
    اطبع ن
اطبع "انطلاق!"

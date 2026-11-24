# مثال 412 — ترميز URL يدويا
# Manual URL encoding
# Demonstrates: تحويل الأحرف الخاصة
#
# Run:  python apl.py examples/412-url-encode.apl

المتغير آمنة = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~"

دالة سداسي(عدد):
    المتغير أرقام = "0123456789ABCDEF"
    ارجع أرقام[عدد // 16] + أرقام[عدد % 16]

دالة رمز_رابط(نص_الدخل):
    المتغير ناتج = ""
    لكل حرف in نص_الدخل:
        لو آمنة.find(حرف) >= 0:
            ناتج = ناتج + حرف
        الا لو حرف == " ":
            ناتج = ناتج + "%20"
        الا:
            ناتج = ناتج + "%" + سداسي(ترميز_حرف(حرف) % 256)
    ارجع ناتج

اطبع رمز_رابط("hello world!")

المتغير آمنة = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~"

# 508 · الصور والنصوص العميقة — mediadeep
# PIL / markdown-it / jinja2
#
# Run:  python apl.py examples/508-mediadeep.apl

اطبع "=== الصور ==="
المتغير ص = صورة_جديد("RGB", (10, 20))
اطبع "الحجم:", ص.size

اطبع "=== ماركداون ==="
اطبع رئيسي_ماركداون_IT().render("# عنوان")

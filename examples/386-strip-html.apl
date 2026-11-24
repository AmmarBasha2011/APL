# مثال 386 — إزالة وسوم HTML
# Strip HTML tags
# Demonstrates: استبدال نمطي للوسوم
#
# Run:  python apl.py examples/386-strip-html.apl

المتغير صفحة = "<h1>عنوان</h1><p>فقرة <b>مهمة</b> هنا</p>"
المتغير نظيف = استبدل_عدد("<[^>]+>", "", صفحة)
اطبع "بعد إزالة الوسوم:", نظيف

المتغير روابط = بحث_شامل("href=.([^\"']+)", '<a href="https://example.com">رابط</a> <a href="https://apl.dev">APL</a>')
اطبع "الروابط:", روابط

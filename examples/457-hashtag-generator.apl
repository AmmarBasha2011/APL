# مثال 457 — مولد هاشتاجات
# Hashtag generator
# Demonstrates: دمج كلمات بحالة الجمل
#
# Run:  python apl.py examples/457-hashtag-generator.apl

دالة هاشتاج(عبارة):
    المتغير ناتج = "#"
    لكل كلمة في عبارة.تقسيم(" "):
        لو طول(كلمة) > 0:
            ناتج = ناتج + كلمة[0].علوي() + كلمة[1:]
    ارجع ناتج

اطبع هاشتاج("arabic programming language")
اطبع هاشتاج("open source community")

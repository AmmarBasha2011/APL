# مثال 152 — التخزين المؤقت للدوال
# Function caching with lru_cache
# Demonstrates: @كاش_مؤقت_دالة، recursion
#
# Run:  python apl.py examples/152-functools-cache.apl

@كاش_مؤقت_دالة
دالة فيب(ن):
    لو ن < 2:
        ارجع ن
    ارجع فيب(ن - 1) + فيب(ن - 2)

اطبع "فيب(10) =", فيب(10)
اطبع "فيب(50) =", فيب(50)
اطبع "فيب(90) =", فيب(90)
اطبع "معلومات الكاش:", فيب.cache_info().hits > 0

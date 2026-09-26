# مكتبة أدوات الدوال — `functools`

أدوات لتثبيت الوسائط والتخزين المؤقت وتغليف الدوال.

**9 عنصر** (9 دالة، 0 خاصية).

## الدوال

| العربي | Python | الوصف |
|--------|--------|-------|
| `@تغليف_دالة(...)` | `functools.wraps` |  |
| `تغليف_دالة(...)` | `functools.wraps` | functools.wraps للـ decorators |
| `جزئي_دالة(...)` | `functools.partial` | partial لتثبيت وسائط |
| `كاش_مؤقت_دالة(...)` | `functools.lru_cache` | lru_cache للتخزين المؤقت |
| `كاش_بلا_حد(...)` | `functools.cache` | cache بدون حد |
| `مقارن_بالعكس(...)` | `functools.cmp_to_key` | cmp_to_key للترتيب |
| `اختصر_دالة(...)` | `functools.reduce` | reduce |
| `تعيين_ترتيب(...)` | `functools.total_ordering` | total_ordering |
| `أقوى_قيمة(...)` | `functools.reduce` | reduce |

## أمثلة

```apl
دالة مربع(س):
    ارجع س * س

# partial: تثبيت وسائط
المتغير جزئي = جزئي_دالة(مربع, 5)
اطبع "مربع 5:", جزئي()

# lru_cache: تخزين مؤقت
اطبع "مع التخزين:", كاش_مؤقت_دالة(مربع)(6)
```

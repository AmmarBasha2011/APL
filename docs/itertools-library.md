# مكتبة أدوات التكرار — `itertools`

كل الدوال من مكتبة `itertools` في Python، مترجمة بالكامل:

**19 عنصراً عربياً** (الدوال: 19).

## الدوال (19)

| العربي | Python |
|--------|--------|
| `عد_لا نهائي` | `itertools.count` |
| `تكرار_لا نهائي` | `itertools.cycle` |
| `كرر_لا نهائي` | `itertools.repeat` |
| `مدى_لا نهائي` | `itertools.count` |
| `تجميع` | `itertools.chain` |
| `تجميع_من_قوائم` | `itertools.chain.from_iterable` |
| `ضغط` | `itertools.compress` |
| `فلترة_خاطئة` | `itertools.filterfalse` |
| `قطّع` | `itertools.islice` |
| `اقطع` | `itertools.islice` |
| `توافيق_مع_إرجاع` | `itertools.combinations_with_replacement` |
| `ناتج_ديكارتي` | `itertools.product` |
| `تباديل_مع_إرجاع` | `itertools.product` |
| `اجمع_مفتاح` | `itertools.groupby` |
| `تراكم` | `itertools.accumulate` |
| `زوجي` | `itertools.zip_longest` |
| `سلسلة` | `itertools.chain` |
| `فلتر` | `filter` |
| `خريطة` | `map` |

## مثال

```apl
# chain
print("chain:", قائمة(تجميع([1,2,3], [4,5,6])))

# accumulate
print("accumulate:", قائمة(تراكم([1,2,3,4,5])))

# product
print("product:", قائمة(ناتج_ديكارتي([1,2], ['a','b'])))

# combinations
print("combinations:", قائمة(توافيق_مع_إرجاع([1,2,3], 2)))

# compress
print("compress:", قائمة(ضغط(['a','b','c','d'], [1,0,1,0])))

# count
print("count:", قائمة(اقطع(عد_لا نهائي(10), 5)))

# cycle
print("cycle:", قائمة(اقطع(تكرار_لا نهائي([1,2,3]), 7)))

# repeat
print("repeat:", قائمة(كرر_لا نهائي(5, 3)))
```

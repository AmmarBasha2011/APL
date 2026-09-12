# المكتبات المخصصة — `collections`

كل الدوال من مكتبة `collections` في Python، مترجمة بالكامل:

## أنواع خاصة (Specialized Types)

| العربي | Python | الوصف |
|--------|--------|-------|
| `عداد(تسلسل)` | `collections.Counter(تسلسل)` | عداد للعناصر (Counter) |
| `قاموس_افتراضي(نوع)` | `collections.defaultdict(نوع)` | قاموس بقيمة افتراضية |
| `قائمة_مزدوجة(تسلسل)` | `collections.deque(تسلسل)` | قائمة مزدوجة الطرفين (deque) |
| `صف_مسمى(اسم, حقول)` | `collections.namedtuple(اسم, حقول)` | صف مسمى (namedtuple) |
| `سلسلة_مرتبة(قاموس)` | `collections.OrderedDict(قاموس)` | قاموس مرتب (OrderedDict) |

## دوال (Functions)

| العربي | Python | الوصف |
|--------|--------|-------|
| `عد_عناصر(تسلسل)` | `collections.Counter(تسلسل)` | عد العناصر (Counter) |
| `عنصر_أكثر(تسلسل, ن)` | `collections.Counter.most_common(ن)` | أكثر العناصر تكراراً |

## مثال

```apl
# Counter
المتغير عداد = عداد(["a", "b", "c", "a", "b", "a"])
print("عداد:", عداد)
print("أكثر تكرارا:", عنصر_أكثر(عداد, 3))

# deque
المتغير صف = قائمة_مزدوجة([1, 2, 3])
صف.appendleft(0)
صف.append(4)
print("صف:", صف)

# OrderedDict
المتغير سلسلة = سلسلة_مرتبة([("c", 3), ("a", 1), ("b", 2)])
print("سلسلة:", سلسلة)
```

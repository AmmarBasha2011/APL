# المكتبات المخصصة — `collections`

كل الدوال من مكتبة `collections` في Python، مترجمة بالكامل:

**9 عنصراً عربياً** (الدوال: 9).

## الدوال (9)

| العربي | Python |
|--------|--------|
| `عداد` | `collections.Counter` |
| `قاموس_افتراضي` | `collections.defaultdict` |
| `قائمة_مزدوجة` | `collections.deque` |
| `صف_مسمى` | `collections.namedtuple` |
| `سلسلة_مرتبة` | `collections.OrderedDict` |
| `عد_عناصر` | `collections.Counter` |
| `عنصر_أكثر` | `collections.Counter.most_common` |
| `صف_انتظار` | `collections.deque` |
| `صف_انتظار_محدود` | `collections.deque` |

## مثال

```apl
# Counter
المتغير تكرارات = عداد(["a", "b", "c", "a", "b", "a"])
print("عداد:", تكرارات)
print("أكثر تكرارا:", عنصر_أكثر(تكرارات, 3))

# deque
المتغير صف = قائمة_مزدوجة([1, 2, 3])
صف.appendleft(0)
صف.append(4)
print("صف:", صف)

# OrderedDict
المتغير سلسلة = سلسلة_مرتبة([("c", 3), ("a", 1), ("b", 2)])
print("سلسلة:", سلسلة)
```

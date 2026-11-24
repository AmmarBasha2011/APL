# مكتبة الإحصاء — `statistics`

كل الدوال من مكتبة `statistics` في Python، مترجمة بالكامل:

**15 عنصراً عربياً** (الدوال: 16).

## الدوال (15)

| العربي | Python |
|--------|--------|
| `متوسط` | `statistics.mean` |
| `وسيط` | `statistics.median` |
| `منوال` | `statistics.mode` |
| `متوسط_توافقي` | `statistics.harmonic_mean` |
| `متوسط_هندسي` | `statistics.geometric_mean` |
| `وسيط_منخفض` | `statistics.median_low` |
| `وسيط_مرتفع` | `statistics.median_high` |
| `وسيط_مجمع` | `statistics.median_grouped` |
| `تباين` | `statistics.variance` |
| `تباين_مجتمع` | `statistics.pvariance` |
| `انحراف_معياري` | `statistics.stdev` |
| `انحراف_معياري_مجتمع` | `statistics.pstdev` |
| `نطاق_إحصاء` | `range` |
| `ارتباط` | `statistics.correlation` |
| `ميل` | `statistics.linear_regression` |

## مثال

```apl
المتغير قائمة = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

اطبع "المتوسط:", متوسط(قائمة)
اطبع "الوسيط:", وسيط(قائمة)
اطبع "المنوال:", منوال([1, 2, 2, 3, 3, 3, 4])
اطبع "التباين:", تباين(قائمة)
اطبع "الانحراف المعياري:", انحراف_معياري(قائمة)
```

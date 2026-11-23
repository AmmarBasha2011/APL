# مكتبة العشوائية — `random`

كل الدوال من مكتبة `random` في Python، مترجمة بالكامل:

**20 عنصراً عربياً** (الدوال: 20).

## الدوال (20)

| العربي | Python |
|--------|--------|
| `عشوائي_كسر` | `random.random` |
| `عشوائي_عائم` | `random.uniform` |
| `عشوائي_عدد` | `random.randint` |
| `عشوائي_خطوة` | `random.randrange` |
| `عشوائي` | `random.choice` |
| `عشوائي_أوزان` | `random.choices` |
| `عشوائي_عينة` | `random.sample` |
| `خلط` | `random.shuffle` |
| `عشوائي_طبيعي` | `random.gauss` |
| `عشوائي_متماثل` | `random.normalvariate` |
| `عشوائي_لوغ` | `random.lognormvariate` |
| `عشوائي_أسي` | `random.expovariate` |
| `عشوائي_فونميس` | `random.vonmisesvariate` |
| `عشوائي_جاما` | `random.gammavariate` |
| `عشوائي_بيتا` | `random.betavariate` |
| `عشوائي_باريتو` | `random.paretovariate` |
| `عشوائي_ويبول` | `random.weibullvariate` |
| `بذرة` | `random.seed` |
| `حالة_عشوائي` | `random.getstate` |
| `تعيين_حالة` | `random.setstate` |

## مثال

```apl
بذرة(42)
اطبع "كسر عشوائي:", عشوائي_كسر()
اطبع "عدد عشوائي [1,100]:", عشوائي_عدد(1, 100)
اطبع "اختيار عشوائي:", عشوائي(["تفاح", "موز", "برتقال"])

المتغير قائمة = [1, 2, 3, 4, 5]
خلط(قائمة)
اطبع "بعد الخلط:", قائمة
```

# مكتبة العشوائية — `random`

كل الدوال من مكتبة `random` في Python، مترجمة بالكامل:

## أساسي (Basic)

| العربي | Python | الوصف |
|--------|--------|-------|
| `عشوائي_كسر()` | `random.random()` | كسر عشوائي [0.0, 1.0) |
| `عشوائي_عائم(a, b)` | `random.uniform(a, b)` | كسر عشوائي في النطاق [a, b] |
| `عشوائي_عدد(a, b)` | `random.randint(a, b)` | عدد صحيح عشوائي [a, b] |
| `عشوائي_خطوة(start, stop, step)` | `random.randrange(start, stop, step)` | عدد صحيح بخطوة |
| `عشوائي(seq)` | `random.choice(seq)` | عنصر عشوائي من تسلسل |
| `عشوائي_أوزان(seq, k=n)` | `random.choices(seq, k=n)` | عينة مع إرجاع |
| `عشوائي_عينة(seq, k)` | `random.sample(seq, k)` | عينة بدون إرجاع |
| `خلط(list)` | `random.shuffle(list)` | خلط القائمة في مكانها |

## توزيعات (Distributions)

| العربي | Python | الوصف |
|--------|--------|-------|
| `عشوائي_طبيعي(mu, sigma)` | `random.gauss(mu, sigma)` | التوزيع الطبيعي |
| `عشوائي_متماثل(mu, sigma)` | `random.normalvariate(mu, sigma)` | طبيعي متماثل |
| `عشوائي_لوغ(mu, sigma)` | `random.lognormvariate(mu, sigma)` | لوغاريتمي طبيعي |
| `عشوائي_أسي(lambd)` | `random.expovariate(lambd)` | توزيع أسي |
| `عشوائي_فونميس(mu, kappa)` | `random.vonmisesvariate(mu, kappa)` | فون ميسيس |
| `عشوائي_جاما(alpha, beta)` | `random.gammavariate(alpha, beta)` | توزيع جاما |
| `عشوائي_بيتا(alpha, beta)` | `random.betavariate(alpha, beta)` | توزيع بيتا |
| `عشوائي_باريتو(alpha)` | `random.paretovariate(alpha)` | باريتو |
| `عشوائي_ويبول(alpha, beta)` | `random.weibullvariate(alpha, beta)` | ويبول |

## حالة (State)

| العربي | Python | الوصف |
|--------|--------|-------|
| `بذرة(n)` | `random.seed(n)` | تهيئة المولد (لل reproducibility) |
| `حالة_عشوائي()` | `random.getstate()` | الحصول على الحالة الحالية |
| `تعيين_حالة(state)` | `random.setstate(state)` | تعيين الحالة |

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

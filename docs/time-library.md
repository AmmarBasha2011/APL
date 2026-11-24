# مكتبة الوقت والتاريخ — `time` + `datetime`

كل الدوال من مكتبتين `time` و `datetime` في Python، مترجمة بالكامل:

**18 عنصراً عربياً** (الدوال: 18، الخصائص: 7).

## الدوال (11)

| العربي | Python |
|--------|--------|
| `وقت` | `time.time` |
| `وقت_نص` | `time.ctime` |
| `وقت_عالمي` | `time.gmtime` |
| `وقت_محلي` | `time.localtime` |
| `مؤشر_أداء` | `time.perf_counter` |
| `تاريخ` | `datetime.date` |
| `مدة` | `datetime.timedelta` |
| `من_نص_وقت` | `datetime.datetime.strptime` |
| `لتنسيق_وقت` | `datetime.datetime.strftime` |
| `تنسيق_وقت` | `time.strftime` |
| `تحليل_وقت` | `time.strptime` |

## الخصائص (7) — `TIME_PROPS`

| العربي | Python |
|--------|--------|
| `سنة_الآن` | `datetime.datetime.now().year` |
| `شهر_الآن` | `datetime.datetime.now().month` |
| `يوم_الآن` | `datetime.datetime.now().day` |
| `ساعة_الآن` | `datetime.datetime.now().hour` |
| `دقيقة_الآن` | `datetime.datetime.now().minute` |
| `ثانية_الآن` | `datetime.datetime.now().second` |
| `يوم_أسبوع_الآن` | `datetime.datetime.now().weekday()` |

## مثال

```apl
# الوقت الحالي
اطبع "الآن:", الآن()
اطبع "اليوم:", اليوم()

# مكونات التاريخ (بدون أقواس)
اطبع "السنة:", سنة_الآن
اطبع "الشهر:", شهر_الآن
اطبع "الساعة:", ساعة_الآن

# الانتظار
وقت_نومي(1)  # انتظر ثانية
```

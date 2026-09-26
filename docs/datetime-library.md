# مكتبة التاريخ والوقت — `datetime`

دوال التاريخ والوقت والتحويل بينها، مع خصائص كائن التاريخ والثوابت.

**45 عنصر** (25 دالة، 11 خاصية، 3 ثابت، 6 معامل).

## الحالية

| العربي | Python | الوصف |
|--------|--------|-------|
| `التاريخ_اليوم(...)` | `datetime.date.today` | تاريخ اليوم |
| `التاريخ_الآن(...)` | `datetime.datetime.now` | تاريخ ووقت الآن |
| `تاريخ_و_وقت_الآن(...)` | `datetime.datetime.now` | تاريخ ووقت الآن |
| `الوقت_الآن_فقط(...)` | `datetime.datetime.today` | datetime.today |
| `الوقت_عالمي_الآن(...)` | `datetime.datetime.utcnow` | الوقت بتوقيت UTC |

## التحويل بين الصيغ

| العربي | Python | الوصف |
|--------|--------|-------|
| `حوّل_نص_لتاريخ(...)` | `datetime.date.fromisoformat` | نص ISO -> date |
| `حوّل_نص_لوقت(...)` | `datetime.datetime.fromisoformat` | نص ISO -> datetime |
| `التاريخ_إلى_نص(...)` | `datetime.date.isoformat` | date -> نص ISO |
| `الوقت_إلى_نص(...)` | `datetime.datetime.isoformat` | datetime -> نص ISO |
| `الوقت_إلى_طابع(...)` | `datetime.datetime.timestamp` | تحويل إلى timestamp |
| `من_طابع(...)` | `datetime.datetime.fromtimestamp` | timestamp -> datetime |
| `أيام_من_التاريخ(...)` | `datetime.date.toordinal` | رقم اليوم التراكمي |
| `التاريخ_من_رقم(...)` | `datetime.date.fromordinal` | عكس أيام_من_التاريخ |

## التنسيق والتحليل

| العربي | Python | الوصف |
|--------|--------|-------|
| `نسق_الوقت(...)` | `datetime.datetime.strftime` | تنسيق بـ strftime |
| `فك_الوقت(...)` | `datetime.datetime.strptime` | تحليل بـ strptime |
| `تنسيق_تقويمي(...)` | `datetime.datetime.isocalendar` | isocalendar |
| `رقم_يوم_الأسبوع(...)` | `datetime.date.weekday` | 0=الاثنين .. 6=الأحد |
| `رقم_الأسبوع(...)` | `datetime.date.isoweekday` | 1=الاثنين .. 7=الأحد |
| `ثواني_الفرق(...)` | `datetime.timedelta.total_seconds` | إجمالي الثواني |

## فرق الوقت (timedelta)

| العربي | Python | الوصف |
|--------|--------|-------|
| `فرق_الوقت(...)` | `datetime.timedelta` | إنشاء timedelta |
| `أضف_أيام(...)` | `datetime.timedelta` | مرادف لفرق_الوقت |

## أخرى

| العربي | Python | الوصف |
|--------|--------|-------|
| `منطقة_الوقت(...)` | `datetime.timezone` | إنشاء timezone |
| `تعويض_ساعات(...)` | `datetime.timezone` | تعويض ساعات |
| `استبدل_في_الوقت(...)` | `datetime.datetime.replace` | replace |
| `اجمع_تاريخ_و_وقت(...)` | `datetime.datetime.combine` | دمج تاريخ ووقت |

## خصائص الكائن (Properties)

تُستخدم بعد النقطة: `كائن.رقم_السنة`

| العربي | Python | الوصف |
|--------|--------|-------|
| `رقم_السنة` | `year` |  |
| `رقم_الشهر` | `month` |  |
| `رقم_اليوم` | `day` |  |
| `رقم_الساعة` | `hour` |  |
| `رقم_الدقيقة` | `minute` |  |
| `رقم_الثانية` | `second` |  |
| `رقم_الميكروثانية` | `microsecond` |  |
| `أيام_الفرق` | `days` |  |
| `الحد_الأدنى` | `datetime.datetime.min` | أصغر datetime ممكن |
| `الحد_الأقصى` | `datetime.datetime.max` | أكبر datetime ممكن |
| `منطقة_ع_ي_تي` | `datetime.timezone.utc` | منطقة التوقيت UTC |

## ثوابت (Constants)

| العربي | Python | الوصف |
|--------|--------|-------|
| `الحد_الأدنى` | `datetime.datetime.min` | أصغر datetime ممكن |
| `الحد_الأقصى` | `datetime.datetime.max` | أكبر datetime ممكن |
| `منطقة_ع_ي_تي` | `datetime.timezone.utc` | منطقة التوقيت UTC |

## معاملات عربية (Keyword Arguments)

تُستخدم في `فرق_الوقت` وغيرها:

| العربي | Python |
|--------|--------|
| `أيام=` | `days=` |
| `ساعات=` | `hours=` |
| `دقائق=` | `minutes=` |
| `ثوان=` | `seconds=` |
| `ميكروثاني=` | `microseconds=` |
| `أسابيع=` | `weeks=` |

## أمثلة

```apl
المتغير حال = التاريخ_الآن()
اطبع "السنة:", حال.رقم_السنة
اطبع "التاريخ:", نسق_الوقت(حال, "%Y-%m-%d %H:%M")
اطبع "نص:", التاريخ_إلى_نص(التاريخ_اليوم())

# فرق بين تاريخين
المتغير ف = فرق_الوقت(أيام=5, ساعات=3)
اطبع "أيام:", ف.أيام_الفرق
اطبع "إجمالي الثواني:", ثواني_الفرق(ف)
```

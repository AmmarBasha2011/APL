# مكتبة التاريخ والوقت — `datetime`

دوال التاريخ والوقت والتحويل بينها، مع خصائص كائن التاريخ والثوابت.

**45 عنصراً عربياً** (الدوال: 25، الخصائص: 11، الثوابت: 3، المعاملات المسماة: 6).

## الدوال (25)

| العربي | Python |
|--------|--------|
| `التاريخ_اليوم` | `datetime.date.today` |
| `التاريخ_الآن` | `datetime.datetime.now` |
| `تاريخ_و_وقت_الآن` | `datetime.datetime.now` |
| `الوقت_عالمي_الآن` | `datetime.datetime.utcnow` |
| `الوقت_الآن_فقط` | `datetime.datetime.today` |
| `حوّل_نص_لتاريخ` | `datetime.date.fromisoformat` |
| `حوّل_نص_لوقت` | `datetime.datetime.fromisoformat` |
| `التاريخ_إلى_نص` | `datetime.date.isoformat` |
| `الوقت_إلى_نص` | `datetime.datetime.isoformat` |
| `الوقت_إلى_طابع` | `datetime.datetime.timestamp` |
| `من_طابع` | `datetime.datetime.fromtimestamp` |
| `نسق_الوقت` | `datetime.datetime.strftime` |
| `فك_الوقت` | `datetime.datetime.strptime` |
| `فرق_الوقت` | `datetime.timedelta` |
| `أضف_أيام` | `datetime.timedelta` |
| `أيام_من_التاريخ` | `datetime.date.toordinal` |
| `التاريخ_من_رقم` | `datetime.date.fromordinal` |
| `منطقة_الوقت` | `datetime.timezone` |
| `تعويض_ساعات` | `datetime.timezone` |
| `استبدل_في_الوقت` | `datetime.datetime.replace` |
| `اجمع_تاريخ_و_وقت` | `datetime.datetime.combine` |
| `تنسيق_تقويمي` | `datetime.datetime.isocalendar` |
| `رقم_يوم_الأسبوع` | `datetime.date.weekday` |
| `رقم_الأسبوع` | `datetime.date.isoweekday` |
| `ثواني_الفرق` | `datetime.timedelta.total_seconds` |

## الخصائص (11) — `DATETIME_PROPS`

| العربي | Python |
|--------|--------|
| `رقم_السنة` | `year` |
| `رقم_الشهر` | `month` |
| `رقم_اليوم` | `day` |
| `رقم_الساعة` | `hour` |
| `رقم_الدقيقة` | `minute` |
| `رقم_الثانية` | `second` |
| `رقم_الميكروثانية` | `microsecond` |
| `أيام_الفرق` | `days` |
| `الحد_الأدنى` | `datetime.datetime.min` |
| `الحد_الأقصى` | `datetime.datetime.max` |
| `منطقة_ع_ي_تي` | `datetime.timezone.utc` |

## الثوابت (3) — `DATETIME_CONSTANTS`

| العربي | Python |
|--------|--------|
| `الحد_الأدنى` | `datetime.datetime.min` |
| `الحد_الأقصى` | `datetime.datetime.max` |
| `منطقة_ع_ي_تي` | `datetime.timezone.utc` |

## المعاملات المسماة (6) — `DATETIME_KWARGS`

| العربي | Python |
|--------|--------|
| `أيام` | `days` |
| `ساعات` | `hours` |
| `دقائق` | `minutes` |
| `ثوان` | `seconds` |
| `ميكروثاني` | `microseconds` |
| `أسابيع` | `weeks` |

## مثال

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

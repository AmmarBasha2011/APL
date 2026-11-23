# مكتبة الحساب العشري الدقيق — `decimal`

الحساب العشري الدقيق بدون أخطاء تقريب — كل عمليات الفاصلة العائمة بشكل دقيق.

**24 عنصراً عربياً** (الدوال: 17، الثوابت: 7).

## الدوال (17)

| العربي | Python |
|--------|--------|
| `عشري_دقيق` | `decimal.Decimal` |
| `من_نص_عشري` | `decimal.Decimal` |
| `من_كسر_عشري` | `decimal.Decimal` |
| `من_عدد_عشري` | `decimal.Decimal` |
| `سياق_العشري` | `decimal.getcontext` |
| `سياق_محلي` | `decimal.localcontext` |
| `اجمع_عشري` | `_apl_decimal_add` |
| `اطرح_عشري` | `_apl_decimal_sub` |
| `اضرب_عشري` | `_apl_decimal_mul` |
| `اقسم_عشري` | `_apl_decimal_div` |
| `اقسم_باقي_عشري` | `_apl_decimal_mod` |
| `اس_عشري` | `_apl_decimal_pow` |
| `جذر_عشري` | `_apl_decimal_sqrt` |
| `مقارنة_عشري` | `_apl_decimal_cmp` |
| `نسخ_عشري` | `_apl_decimal_copy` |
| `قرّب_عشري` | `_apl_decimal_quantize` |
| `بدقة_عشري` | `_apl_decimal_fma` |

## الثوابت (7) — `DECIMAL_CONSTANTS`

| العربي | Python |
|--------|--------|
| `نقطة_عشرية` | `decimal.getcontext().prec` |
| `اقرب_لأسفل` | `decimal.ROUND_DOWN` |
| `اقرب_لأعلى` | `decimal.ROUND_UP` |
| `اقرب_منتصف` | `decimal.ROUND_HALF_UP` |
| `اقرب_سقف` | `decimal.ROUND_CEILING` |
| `اقرب_أرض` | `decimal.ROUND_FLOOR` |
| `أقصى_دقة` | `decimal.MAX_PREC` |

## مثال

```apl
# أخطاء الفاصلة العائمة في Python:
#   0.1 + 0.2 == 0.30000000000000004   <-- خطأ
# مع decimal النتيجة دقيقة:
المتغير ن = عشري_دقيق("0.1") + عشري_دقيق("0.2")
اطبع "0.1 + 0.2 =", ن
اطبع "قسمة:", اقسم_عشري(عشري_دقيق("1"), عشري_دقيق("3"), 10)
اطبع "جذر 2:", جذر_عشري(عشري_دقيق("2"))
اطبع "تقريب:", قرّب_عشري(عشري_دقيق("3.14159"), 3)
```

# مكتبة الروابط — `urllib`

تحليل الروابط وبناؤها وترميزها، وفتح الروابط.

**13 عنصر** (13 دالة، 0 خاصية).

## تحليل الروابط

| العربي | Python | الوصف |
|--------|--------|-------|
| `تحليل_الرابط(...)` | `urllib.parse.urlparse` | urlparse |
| `نطاق_الرابط(...)` | `urllib.parse.urlparse` | اسم بديل |
| `تحليل_استعلام(...)` | `urllib.parse.parse_qs` | parse_qs |
| `تحليل_استعلام_نص(...)` | `urllib.parse.parse_qsl` | parse_qsl |

## الترميز

| العربي | Python | الوصف |
|--------|--------|-------|
| `ترميز_الرابط(...)` | `urllib.parse.quote` | quote |
| `فك_ترميز_الرابط(...)` | `urllib.parse.unquote` | unquote |
| `ترميز_الرابط_كامل(...)` | `urllib.parse.quote_plus` | quote_plus |
| `فك_ترميز_الرابط_كامل(...)` | `urllib.parse.unquote_plus` | unquote_plus |

## بناء الروابط

| العربي | Python | الوصف |
|--------|--------|-------|
| `بناء_الرابط(...)` | `urllib.parse.urlencode` | urlencode |
| `بناء_الرابط_من_قاموس(...)` | `urllib.parse.urlencode` | اسم بديل |

## فتح الروابط

| العربي | Python | الوصف |
|--------|--------|-------|
| `حمّل_الرابط(...)` | `urllib.request.urlopen` | فتح رابط |
| `استخدم_وكيل(...)` | `urllib.request.Request` | إنشاء Request |
| `وكيل_المتصفح(...)` | `urllib.request.Request` | اسم بديل |

## أمثلة

```apl
المتغير رابط = تحليل_الرابط("https://example.com/p?a=1")
اطبع "المخطط:", نطاق_الرابط("https://example.com").scheme
اطبع "الاستعلام:", رابط.query

اطبع "معاملات:", تحليل_استعلام("a=1&b=2")
اطبع "بناء:", بناء_الرابط({"a": "1", "b": "2"})
اطبع "ترميز:", ترميز_الرابط("سلام عالم")
```

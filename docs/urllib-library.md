# مكتبة الروابط — `urllib`

تحليل الروابط وبناؤها وترميزها، وفتح الروابط.

**13 عنصراً عربياً** (الدوال: 13).

## الدوال (13)

| العربي | Python |
|--------|--------|
| `ترميز_الرابط` | `urllib.parse.quote` |
| `فك_ترميز_الرابط` | `urllib.parse.unquote` |
| `ترميز_الرابط_كامل` | `urllib.parse.quote_plus` |
| `فك_ترميز_الرابط_كامل` | `urllib.parse.unquote_plus` |
| `تحليل_الرابط` | `urllib.parse.urlparse` |
| `نطاق_الرابط` | `urllib.parse.urlparse` |
| `بناء_الرابط` | `urllib.parse.urlencode` |
| `بناء_الرابط_من_قاموس` | `urllib.parse.urlencode` |
| `تحليل_استعلام` | `urllib.parse.parse_qs` |
| `تحليل_استعلام_نص` | `urllib.parse.parse_qsl` |
| `حمّل_الرابط` | `urllib.request.urlopen` |
| `استخدم_وكيل` | `urllib.request.Request` |
| `وكيل_المتصفح` | `urllib.request.Request` |

## مثال

```apl
المتغير رابط = تحليل_الرابط("https://example.com/p?a=1")
اطبع "المخطط:", نطاق_الرابط("https://example.com").scheme
اطبع "الاستعلام:", رابط.query

اطبع "معاملات:", تحليل_استعلام("a=1&b=2")
اطبع "بناء:", بناء_الرابط({"a": "1", "b": "2"})
اطبع "ترميز:", ترميز_الرابط("سلام عالم")
```

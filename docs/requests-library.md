# مكتبة Requests — HTTP Client بالعربي

مكتبة HTTP Client بالعربي، متوافقة مع Python requests:

## الطرق الأساسية

| العربي | Python | الوصف |
|--------|--------|-------|
| `احصل_على(رابط)` | `requests.get(رابط)` | GET request |
| `أرسل_إلى(رابط, بيانات)` | `requests.post(رابط, بيانات)` | POST request |
| `ضع_في(رابط, بيانات)` | `requests.put(رابط, بيانات)` | PUT request |
| `احذف(رابط)` | `requests.delete(رابط)` | DELETE request |
| `صحح(رابط, بيانات)` | `requests.patch(رابط, بيانات)` | PATCH request |
| `رأس(رابط)` | `requests.head(رابط)` | HEAD request |
| `خيارات(رابط)` | `requests.options(رابط)` | OPTIONS request |

## اختصارات

| العربي | Python |
|--------|--------|
| `get(رابط)` | GET |
| `post(رابط)` | POST |
| `put(رابط)` | PUT |
| `delete(رابط)` | DELETE |
| `جيت(رابط)` | GET |
| `بوست(رابط)` | POST |

## الاستجابة

| العربي | Python |
|--------|--------|
| `رابط_كامل` | response.url |
| `رابط_توجيهي` | response.headers.get('Location') |

## ملفات تعريف الارتباط

| العربي | Python |
|--------|--------|
| `كوكي` | response.cookies.get |
| `ضع_كوكي` | requests.cookies.set |
| `احذف_كوكي` | requests.cookies.clear |

## معاملات الطلب

| العربي | Python |
|--------|--------|
| `معاملات` | params |
| `بيانات` | data |
| `جسم` | json |
| `ملف` | files |

## رؤوس الطلب

| العربي | Python |
|--------|--------|
| `رؤوس_الطلب` | headers |
| `وكيل_المستخدم` | headers |
| `تفويض` | headers |

## المهلة

| العربي | Python |
|--------|--------|
| `مهلة` | timeout |
| `محاولة_جديدة` | retry |
| `عدد_المحاولات` | max_retries |

## التحقق

| العربي | Python |
|--------|--------|
| `تحقق` | verify |
| `اسمح_التوجيه` | allow_redirects |
| `بروكسي` | proxies |

## المصادقة

| العربي | Python |
|--------|--------|
| `مصادقة` | auth |
| `مصادقة_أساسية` | HTTPBasicAuth |
| `مصادقة_ملخصة` | HTTPDigestAuth |

## الجلسات

| العربي | Python |
|--------|--------|
| `جلسة` | requests.Session |
| `افتح_جلسة` | requests.Session |
| `أغلق_جلسة` | session.close |
| `جلسة_جيت` | session.get |
| `جلسة_بوست` | session.post |

## الأخطاء

| العربي | Python |
|--------|--------|
| `خطأ_http` | requests.exceptions.HTTPError |
| `خطأ_اتصال` | requests.exceptions.ConnectionError |
| `انتهت_مهلة` | requests.exceptions.Timeout |
| `توجيهات_كثيرة` | requests.exceptions.TooManyRedirects |

## التصفح

| العربي | Python |
|--------|--------|
| `تصفح` | params |
| `صفحة_تالية` | response.links.get('next') |
| `رقم_الصفحة` | params.get('page') |

## الفلترة

| العربي | Python |
|--------|--------|
| `فلتر` | params |
| `حيث` | params |
| `يساوي` | params |
| `أكبر_من` | params |

## الترتيب

| العربي | Python |
|--------|--------|
| `رتب_حسب` | params |
| `تصاعدي` | params |
| `تنازلي` | params |

## الحقول

| العربي | Python |
|--------|--------|
| `حقول` | params |
| `اختر` | params |
| `عدد` | params |
| `مجموع` | params |

## الأمان

| العربي | Python |
|--------|--------|
| `آمن` | verify=True |
| `تحقق_ssl` | verify |
| `استخدم_بروكسي` | proxies |

## الأداء

| العربي | Python |
|--------|--------|
| `مدة_الطلب` | response.elapsed.total_seconds |
| `سرعة_التنزيل` | calculated |

## مثال

```apl
# Simple GET
المتغير ر = جيت("https://httpbin.org/json")
print("نص:", r.text)
print("حالة:", r.status_code)

# POST with data
المتغير ر2 = بوست("https://httpbin.org/post", بيانات={"key": "value"})
print("نتيجة:", r2.json())

# Session
المتغير s = جلسة()
s.headers.update({"Authorization": "Bearer token"})
المتغير ر3 = s.get("https://api.example.com/data")
```

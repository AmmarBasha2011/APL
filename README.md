# APL - Ammar Programming Language

**لغة برمجة كاملة بالعربي.** اكتب كود بالعربي، يتحول تلقائياً لـ Python ويشتغل مباشرة.

```
المتغير اسم = ادخل("ما اسمك؟ ")
اطبع "أهلاً بك يا", اسم
```

## ابدأ الآن

```bash
git clone https://github.com/AmmarBasha2011/APL.git
cd APL
python apl.py examples/01-calculator.apl   # شغّل ملف
python apl.py -c "اطبع 'مرحباً'"  # تنفيذ كود مباشرة
python apl.py help             # عرض المساعدة
python apl.py repl # REPL تفاعلي
python apl.py examples/02-sales-report.apl # تشغيل مثال جاهز
```

## المميزات

- **كلمات مفتاحية عربية** — `اطبع`، `لو`، `دالة`، `صنف`، والمزيد
- **مكتبات بالعربي** — 40 مكتبة مترجمة بالكامل (من `math` و `requests` إلى `datetime` و `decimal` و `operator`)
- **رسائل أخطاء بالعربي** — كل أخطاء Python مترجمة للعربية
- **تحويل تلقائي للمستورداات** — يستورد المكتبات المطلوبة تلقائياً
- **بدون dependencies** — فقط Python 3.8+
- **فهم متقدم** — list comprehensions، type hints، f-strings، multi-line strings
- **تطابق أنماط متقدم** — pattern matching مع guard clauses
- **إدارة سياق** — `with` statement بالعربي
- **مولدات** — `yield` و `yield from` بالعربي
- **REPL تفاعلي** — جرب الكود سطر بسطر بـ `python apl.py repl`

## المكتبات المتاحة (40 مكتبة)

| المكتبة | عدد العناصر | الوصف |
|---------|------------:|-------|
| `fastapi` | 536 | إطار عمل ويب حديث |
| `requests` | 244 | HTTP Client كامل |
| `asyncio` | 118 | برمجة غير متزامنة |
| `argparse` | 91 | تحليل وسائط سطر الأوامر |
| `unittest` | 85 | اختبارات الوحدة |
| `logging` | 79 | تسجيل الأحداث |
| `flask` | 78 | إطار عمل ويب |
| `subprocess` | 74 | أوامر النظام |
| `advanced` | 70 | ميزات متقدمة (decorators, metaclasses, typing) |
| `dataclasses` | 68 | فئات بيانات، تعدادات، ABC |
| `pathlib` | 61 | التعامل مع المسارات ككائنات |
| `math` | 59 | مثلثات، لوغاريتمات، جذور، تقريب، هندسة |
| `datetime` | 45 | التاريخ والوقت والتحويل بينهما |
| `configparser` | 35 | ملفات الإعدادات |
| `os` | 30 | ملفات، مجلدات، مسارات، فحص |
| `threading` | 29 | تعدد المهام |
| `operator` | 26 | المشغّلات كدوال (add, mul, itemgetter) |
| `re` | 25 | تعابير نمطية، بحث، استبدال، تقسيم |
| `time` | 25 | وقت، تاريخ، تأخير، تنسيق |
| `decimal` | 24 | الحساب العشري الدقيق (بدون أخطاء تقريب) |
| `sqlite3` | 23 | قاعدة بيانات محلية |
| `random` | 20 | أرقام عشوائية، توزيعات، خلط |
| `itertools` | 19 | أدوات تكرار، توافيق، تباديل |
| `statistics` | 16 | متوسط، وسيط، منوال، تباين، انحراف معياري |
| `csv` | 13 | ملفات بيانات |
| `urllib` | 13 | تحليل وبناء الروابط وترميزها |
| `uuid` | 13 | المعرفات الفريدة (UUID) |
| `shutil` | 12 | نسخ ونقل وحذف الملفات والمجلدات |
| `base64` | 11 | الترميز وفك الترميز |
| `string` | 10 | مجموعات الأحرف والرموز الثابتة |
| `collections` | 9 | Counter, defaultdict, deque |
| `functools` | 9 | أدوات الدوال (partial, cache, wraps) |
| `textwrap` | 9 | تنسيق النصوص ولفّها |
| `fractions` | 8 | الكسور الرياضية الدقيقة |
| `json` | 8 | قراءة وكتابة JSON |
| `secrets` | 8 | توليد قيم عشوائية آمنة تشفيرياً |
| `zoneinfo` | 8 | المناطق الزمنية (IANA) |
| `hashlib` | 7 | تجزئة وتشفير |
| `getpass` | 2 | إدخال كلمات السر دون إظهارها |
| `pprint` | 2 | طباعة منسّقة للقواميس والقوائم |

**الإجمالي: 2022 عنصراً في 40 مكتبة** (1862 مفتاحاً فريداً بعد إزالة التكرار).

تشمل العناصر: الدوال، خصائص الكائنات، دوال الكائن المتسلسلة، الثوابت، والمعاملات العربية.
إضافة إلى **168** عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط، دوال مضمّنة)،
ما يجعل الإجمالي الكلي **2190** عنصراً عربياً في اللغة.

تشمل العناصر: الدوال، خصائص الكائنات، دوال الكائن المتسلسلة، الثوابت، والمعاملات العربية.
إضافة إلى **168** عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط، دوال مضمّنة)،
ما يجعل الإجمالي الكلي **2100** عنصراً عربياً في اللغة.

تشمل العناصر: الدوال، خصائص الكائنات، دوال الكائن المتسلسلة، الثوابت، والمعاملات العربية.
إضافة إلى **168** عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط، دوال مضمّنة)،
ما يجعل الإجمالي الكلي **2،089** عنصراً عربياً في اللغة.

إضافة إلى **167** عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط)، ما يجعل الإجمالي الكلي أكثر من **2,000** عنصر عربي في اللغة.

## الأمثلة

**جمع عددين:**
```apl
المتغير أ = صحيح(ادخل("الأول: "))
المتغير ب = صحيح(ادخل("الثاني: "))
اطبع "المجموع:", أ + ب
```

**عدد عشوائي:**
```apl
بذرة(42)
اطبع عشوائي_عدد(1, 100)
```

**مثلثات:**
```apl
المتغير زاوية = راديان(45)
اطبع جب(زاوية)
```

**طلب HTTP:**
```apl
المتغير ر = جيت("https://httpbin.org/json")
اطبع r.text
```

**API سريع:**
```apl
app = سريع()

سريع_جيت('/')
def رئيسية():
    جسونيا({"رسالة": "مرحباً"})

شغل(app, 8000)
```

**قاعدة بيانات SQLite:**
```apl
المتغير conn = افتح_قاعدة('test.db')
المتغير c = مؤشر()
نفذ('CREATE TABLE users (id INTEGER, name TEXT)')
نفذ('INSERT INTO users VALUES (1, ?)', ('عمار',))
تأكد()
أغلق()
```

**Context Manager:**
```apl
مع فتح('ملف.txt', 'r') مثل f:
    محتوى = f.read()
    اطبع محتوى
```

**Generator:**
```apl
دالة أرقام(نهاية):
    لكل i في نطاق(نهاية):
        ولد i  # yield i

لكل رقم في أرقام(10):
   اطبع رقم
```

## أمثلة جاهزة للتشغيل (Examples)

مجلد `examples/` يحتوي على **10 برامج حقيقية** مكتوبة بالكامل بالعربي، وجميعها مختبرة وتعمل:

| # | الملف | الوصف | يشرح |
|---|-------|-------|------|
| 1 | [`01-calculator.apl`](examples/01-calculator.apl) | آلة حاسبة تفاعلية | إدخال، شروط متداخلة، عمليات حسابية |
| 2 | [`02-sales-report.apl`](examples/02-sales-report.apl) | تقرير مبيعات وخصم | قوائم، حلقات، f-strings، حساب |
| 3 | [`03-task-manager.apl`](examples/03-task-manager.apl) | مدير المهام | قواميس، بحث، إحصاء، uuid |
| 4 | [`04-text-analyzer.apl`](examples/04-text-analyzer.apl) | محلل نصوص | مكتبة `re`، تقطيع، عدّ |
| 5 | [`05-report-writer.apl`](examples/05-report-writer.apl) | كاتب تقارير | مكتبة `textwrap`، تنسيق، ضم |
| 6 | [`06-search-sort.apl`](examples/06-search-sort.apl) | بحث وترتيب | دوال مخصصة، حلقات متداخلة |
| 7 | [`07-sqlite-tasks.apl`](examples/07-sqlite-tasks.apl) | قاعدة بيانات SQLite | CRUD كامل، معاملات، ملفات |
| 8 | [`08-word-frequency.apl`](examples/08-word-frequency.apl) | عدّاد تكرار الكلمات | قواميس، `تقسيم`، `تقليم` |
| 9 | [`09-encoding-hashing.apl`](examples/09-encoding-hashing.apl) | ترميز وتجزيع | `base64`، `hashlib`، `uuid` |
| 10 | [`10-file-manager.apl`](examples/10-file-manager.apl) | مدير ملفات | `pathlib`، `shutil`، `os` |

### تشغيل أي مثال

```bash
python apl.py examples/02-sales-report.apl
echo "1" | python apl.py examples/01-calculator.apl   # مثال يحتاج إدخال
```

### مثال كامل

```apl
# examples/06-search-sort.apl (مقتطف)
دالة فقاعة(المدخل):
    الناتج = المدخل.نسخ()
    n = طول(الناتج)
    i = 0
    طالما i < n:
        j = 0
        طالما j < n - 1 - i:
            إذا الناتج[j] > الناتج[j + 1]:
                مؤقت = الناتج[j]
                الناتج[j] = الناتج[j + 1]
                الناتج[j + 1] = مؤقت
            j = j + 1
        i = i + 1
    ارجع الناتج

المتغير البيانات = [64, 25, 12, 22, 11, 90, 33]
اطبع "مرتب: " + نص(فقاعة(البيانات))
```

**الناتج:** `مرتب: [11, 12, 22, 25, 33, 64, 90]`

## التوثيق الكامل

📚 **[فهرس التوثيق](docs/README.md)** — مرجع كامل لكل التفاصيل

## المتطلبات

- Python 3.8+
- بدون مكتبات خارجية

## الرخصة

Ammar Programming Language (APL) — Copyright © 2026 Ammar Al-Khateeb (عمار الخطيب)

This project is open source and free to use. All rights are reserved by the author.

PERMISSIONS (Free of Charge):
✅ You may use the Software for any personal, non-commercial purpose.
✅ You may study, learn from, and modify the Software for your own use.

RESTRICTIONS (Not Permitted WITHOUT Explicit Written Permission):
❌ Distribution — You may not distribute, share, sublicense, or make the Software available to third parties in any form.
❌ Commercial Use — You may not sell, rent, lease, sublicense, or otherwise monetize the Software.
❌ Public Hosting — You may not host the Software on any platform accessible to the public.

ATTRIBUTION:
"Ammar Programming Language (APL) — Created by Ammar Al-Khateeb (عمار الخطيب) — https://github.com/AmmarBasha2011/APL"

NO WARRANTY: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

For inquiries: Ammar Al-Khateeb — inex.own@gmail.com

## المؤلف

**عمار الخطيب** — [GitHub](https://github.com/AmmarBasha2011) | [LinkedIn](https://www.linkedin.com/in/ammar2011)

---

**الإصدار:** APL v1.8 — 2,190 عنصر عربي — 40 مكتبة

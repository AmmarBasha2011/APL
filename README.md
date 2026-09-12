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
python apl.py calculator.apl   # شغّل ملف
python apl.py help             # عرض المساعدة
python apl.py repl             # REPL تفاعلي
```

## المميزات

- **كلمات مفتاحية عربية** — `اطبع`، `لو`، `دالة`، `صنف`، والمزيد
- **مكتبات بالعربي** — كل دوال `math` و `random` و 23+ مكتبات أخرى مترجمة
- **رسائل أخطاء بالعربي** — كل أخطاء Python مترجمة للعربية
- **تحويل تلقائي للمستورداات** — يستورد المكتبات المطلوبة تلقائياً
- **بدون dependencies** — فقط Python 3.8+
- **فهم متقدم** — list comprehensions، type hints، f-strings، multi-line strings
- **تطابق أنماط متقدم** — pattern matching مع guard clauses
- **REPL تفاعلي** — جرب الكود سطر بسطر بـ `python apl.py repl`

## المكتبات المتاحة (25 مكتبة)

| المكتبة | عدد الدوال | الوصف |
|---------|-----------|-------|
| `math` | 50+ | مثلثات، لوغاريتمات، جذور، تقريب، هندسة |
| `random` | 20+ | أرقام عشوائية، توزيعات، خلط |
| `statistics` | 15+ | متوسط، وسيط، منوال، تباين، انحراف معياري |
| `time` + `datetime` | 20+ | وقت، تاريخ، تأخير، تنسيق |
| `os` + `pathlib` | 30+ | ملفات، مجلدات، مسارات، فحص |
| `re` | 10+ | تعابير نمطية، بحث، استبدال، تقسيم |
| `collections` | 10+ | Counter, defaultdict, deque |
| `itertools` | 20+ | أدوات تكرار، توافيق، تباديل |
| `json` | 4+ | قراءة وكتابة JSON |
| `hashlib` | 5+ | تجزئة وتشفير |
| `flask` | 50+ | إطار عمل ويب |
| `fastapi` | 100+ | إطار عمل ويب حديث |
| `requests` | 150+ | HTTP Client كامل |
| `sqlite3` | 20+ | قاعدة بيانات محلية |
| `asyncio` | 50+ | برمجة غير متزامنة |
| `threading` | 20+ | تعدد المهام |
| `unittest` | 40+ | اختبارات الوحدة |
| `csv` | 10+ | ملفات بيانات |
| `logging` | 30+ | تسجيل الأحداث |
| `argparse` | 30+ | تحليل وسائط سطر الأوامر |
| `subprocess` | 20+ | أوامر النظام |
| `configparser` | 20+ | ملفات الإعدادات |
| `dataclasses` | 30+ | فئات بيانات، تعدادات، ABC |

**إجمالي: ~674 دالة ومفتاح بالعربي**

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

**تسجيل الأحداث:**
```apl
تكوين(مستوى=مستوى_معلومات)
المتغير logger = جل_("تطبيقي")
معلومات("بدء التطبيق")
تحذير("هذا تحذير")
خطأ("حدث خطأ")
```

**تحليل الوسائط:**
```apl
المتغير parser = أنشئ_محلل()
أضف_حجة("اسم", تلم_hint="اسم المستخدم")
أضف_خيار("--عمر", نوع=عدد_صحيح, افتراضي=25)
المتغير args = حلل()
اطبع args.اسم, args.عمر
```

**أوامر النظام:**
```apl
المتغير r = نفذ(["ls", "-la"])
اطبع "رمز العودة:", r.returncode
اطبع "الخرج:", r.stdout
```

## التوثيق الكامل

📚 **[فهرس التوثيق](docs/index.md)** — مرجع كامل لكل التفاصيل

| الملف | المحتوى |
|-------|---------|
| [docs/language-reference.md](docs/language-reference.md) | مرجع اللغة الكامل |
| [docs/math-library.md](docs/math-library.md) | مكتبة `math` |
| [docs/random-library.md](docs/random-library.md) | مكتبة `random` |
| [docs/statistics-library.md](docs/statistics-library.md) | مكتبة `statistics` |
| [docs/time-library.md](docs/time-library.md) | مكتبة `time` + `datetime` |
| [docs/os-library.md](docs/os-library.md) | مكتبة `os` + `pathlib` |
| [docs/re-library.md](docs/re-library.md) | مكتبة `re` |
| [docs/collections-library.md](docs/collections-library.md) | مكتبة `collections` |
| [docs/itertools-library.md](docs/itertools-library.md) | مكتبة `itertools` |
| [docs/json-library.md](docs/json-library.md) | مكتبة `json` |
| [docs/hashlib-library.md](docs/hashlib-library.md) | مكتبة `hashlib` |
| [docs/flask-library.md](docs/flask-library.md) | مكتبة `flask` |
| [docs/fastapi-library.md](docs/fastapi-library.md) | مكتبة `fastapi` |
| [docs/requests-library.md](docs/requests-library.md) | مكتبة `requests` |
| [docs/sqlite3-library.md](docs/sqlite3-library.md) | مكتبة `sqlite3` |
| [docs/asyncio-library.md](docs/asyncio-library.md) | مكتبة `asyncio` |
| [docs/threading-library.md](docs/threading-library.md) | مكتبة `threading` |
| [docs/unittest-library.md](docs/unittest-library.md) | مكتبة `unittest` |
| [docs/csv-library.md](docs/csv-library.md) | مكتبة `csv` |
| [docs/logging-library.md](docs/logging-library.md) | مكتبة `logging` |
| [docs/argparse-library.md](docs/argparse-library.md) | مكتبة `argparse` |
| [docs/subprocess-library.md](docs/subprocess-library.md) | مكتبة `subprocess` |
| [docs/configparser-library.md](docs/configparser-library.md) | مكتبة `configparser` |
| [docs/dataclasses-library.md](docs/dataclasses-library.md) | مكتبة `dataclasses` |
| [docs/error-messages.md](docs/error-messages.md) | رسائل الأخطاء بالعربي |
| [docs/architecture.md](docs/architecture.md) | هيكل المشروع وطريقة العمل |

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

**الإصدار:** APL v1.6 — ~674 دالة بالعربي — 25 مكتبة

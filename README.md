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
python apl.py -c "اطبع 'مرحباً'"  # تنفيذ كود مباشرة
python apl.py help             # عرض المساعدة
python apl.py repl             # REPL تفاعلي
```

## المميزات

- **كلمات مفتاحية عربية** — `اطبع`، `لو`، `دالة`، `صنف`، والمزيد
- **مكتبات بالعربي** — كل دوال `math` و `random` و 24+ مكتبات أخرى مترجمة
- **رسائل أخطاء بالعربي** — كل أخطاء Python مترجمة للعربية
- **تحويل تلقائي للمستورداات** — يستورد المكتبات المطلوبة تلقائياً
- **بدون dependencies** — فقط Python 3.8+
- **فهم متقدم** — list comprehensions، type hints، f-strings، multi-line strings
- **تطابق أنماط متقدم** — pattern matching مع guard clauses
- **إدارة سياق** — `with` statement بالعربي
- **مولدات** — `yield` و `yield from` بالعربي
- **REPL تفاعلي** — جرب الكود سطر بسطر بـ `python apl.py repl`

## المكتبات المتاحة (26 مكتبة)

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
| `advanced` | 100+ | ميزات متقدمة |

**إجمالي: ~774 دالة ومفتاح بالعربي**

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

## التوثيق الكامل

📚 **[فهرس التوثيق](docs/index.md)** — مرجع كامل لكل التفاصيل

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

**الإصدار:** APL v1.7 — ~774 دالة بالعربي — 26 مكتبة

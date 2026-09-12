# التوثيق الكامل — APL v1.5

فهرس جميع ملفات التوثيق:

| # | الملف | الوصف |
|---|-------|-------|
| 1 | [architecture.md](architecture.md) | هيكل المشروع، كيفية العمل، التصميم |
| 2 | [language-reference.md](language-reference.md) | مرجع اللغة — كل الكلمات المفتاحية والتراكيب بما فيها التحسينات الجديدة |
| 3 | [math-library.md](math-library.md) | مكتبة `math` — 50+ دالة مثلثات، لوغاريتمات، جذور، هندسة |
| 4 | [random-library.md](random-library.md) | مكتبة `random` — 20+ دالة أرقام عشوائية وتوزيعات |
| 5 | [statistics-library.md](statistics-library.md) | مكتبة `statistics` — متوسط، وسيط، منوال، تباين، انحراف معياري |
| 6 | [time-library.md](time-library.md) | مكتبة `time` + `datetime` — وقت، تاريخ، تأخير، تنسيق |
| 7 | [os-library.md](os-library.md) | مكتبة `os` + `pathlib` — ملفات، مجلدات، مسارات، فحص |
| 8 | [re-library.md](re-library.md) | مكتبة `re` — تعابير نمطية، بحث، استبدال، تقسيم |
| 9 | [collections-library.md](collections-library.md) | مكتبة `collections` — Counter, defaultdict, deque |
| 10 | [itertools-library.md](itertools-library.md) | مكتبة `itertools` — أدوات تكرار، توافيق، تباديل |
| 11 | [json-library.md](json-library.md) | مكتبة `json` — قراءة وكتابة JSON |
| 12 | [hashlib-library.md](hashlib-library.md) | مكتبة `hashlib` — تجزئة وتشفير |
| 13 | [flask-library.md](flask-library.md) | مكتبة `flask` — إطار عمل ويب |
| 14 | [fastapi-library.md](fastapi-library.md) | مكتبة `fastapi` — إطار عمل ويب حديث |
| 15 | [requests-library.md](requests-library.md) | مكتبة `requests` — HTTP Client كامل |
| 16 | [sqlite3-library.md](sqlite3-library.md) | مكتبة `sqlite3` — قاعدة بيانات محلية |
| 17 | [asyncio-library.md](asyncio-library.md) | مكتبة `asyncio` — برمجة غير متزامنة |
| 18 | [threading-library.md](threading-library.md) | مكتبة `threading` — تعدد المهام |
| 19 | [unittest-library.md](unittest-library.md) | مكتبة `unittest` — اختبارات الوحدة |
| 20 | [csv-library.md](csv-library.md) | مكتبة `csv` — ملفات بيانات |
| 21 | [error-messages.md](error-messages.md) | رسائل الأخطاء — كل أخطاء Python مترجمة بالعربي |

---

## هيكل التوثيق

```
docs/
├── index.md               ← هذا الملف (الفهرس)
├── architecture.md        ← هيكل المشروع وطريقة العمل
├── language-reference.md  ← مرجع اللغة الكامل (مع التحسينات الجديدة)
├── math-library.md        ← مكتبة الرياضيات
├── random-library.md      ← مكتبة العشوائية
├── statistics-library.md  ← مكتبة الإحصاء
├── time-library.md        ← مكتبة الوقت والتاريخ
├── os-library.md          ← مكتبة نظام التشغيل
├── re-library.md          ← مكتبة التعابير النمطية
├── collections-library.md ← المكتبات المخصصة
├── itertools-library.md   ← أدوات التكرار
├── json-library.md        ← مكتبة JSON
├── hashlib-library.md     ← مكتبة التجزئة
├── flask-library.md       ← إطار عمل Flask
├── fastapi-library.md     ← إطار عمل FastAPI
├── requests-library.md    ← HTTP Client
├── sqlite3-library.md     ← قاعدة بيانات SQLite
├── asyncio-library.md     ← برمجة غير متزامنة
├── threading-library.md   ← تعدد المهام
├── unittest-library.md    ← اختبارات الوحدة
├── csv-library.md         ← ملفات CSV
└── error-messages.md      ← رسائل الأخطاء
```

## التحسينات الجديدة (v1.5)

- **sqlite3** — قاعدة بيانات محلية (أهم إضافة!)
- **asyncio** — برمجة غير متزامنة كاملة
- **threading** — تعدد المهام
- **unittest** — اختبارات وحدة مع تسميات عربية
- **csv** — قراءة وكتابة ملفات البيانات
- **تحسينات اللغة** — list comprehensions، type hints، f-strings، multi-line strings، walrus operator، match guards، decorators

## المكتبات المتاحة (20 مكتبة)

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

**إجمالي: ~574 دالة ومفتاح بالعربي**

## كيف تستخدم التوثيق

- **مبتدئ؟** ابدأ بـ [language-reference.md](language-reference.md)
- **محتاج دالة رياضية؟** راجع [math-library.md](math-library.md)
- **محتاج أرقام عشوائية؟** راجع [random-library.md](random-library.md)
- **محتاج إحصاء؟** راجع [statistics-library.md](statistics-library.md)
- **محتاج وقت وتاريخ؟** راجع [time-library.md](time-library.md)
- **محتاج ملفات ومجلدات؟** راجع [os-library.md](os-library.md)
- **محتاج تعابير نمطية؟** راجع [re-library.md](re-library.md)
- **محتاج مكتبات مخصصة؟** راجع [collections-library.md](collections-library.md)
- **محتاج أدوات تكرار؟** راجع [itertools-library.md](itertools-library.md)
- **محتاج JSON؟** راجع [json-library.md](json-library.md)
- **محتاج تجزئة؟** راجع [hashlib-library.md](hashlib-library.md)
- **محتاج ويب Flask؟** راجع [flask-library.md](flask-library.md)
- **محتاج ويب FastAPI؟** راجع [fastapi-library.md](fastapi-library.md)
- **محتاج HTTP Client؟** راجع [requests-library.md](requests-library.md)
- **محتاج قاعدة بيانات؟** راجع [sqlite3-library.md](sqlite3-library.md)
- **محتاج برمجة غير متزامنة؟** راجع [asyncio-library.md](asyncio-library.md)
- **محتاج تعدد مهام؟** راجع [threading-library.md](threading-library.md)
- **محتاج اختبارات؟** راجع [unittest-library.md](unittest-library.md)
- **محتاج CSV؟** راجع [csv-library.md](csv-library.md)
- **لقيت error؟** شوف [error-messages.md](error-messages.md)
- **عايز تفهم التصميم؟** اقرأ [architecture.md](architecture.md)

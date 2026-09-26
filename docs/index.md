# التوثيق الكامل — APL v1.7

فهرس جميع ملفات التوثيق:

| # | الملف | الوصف |
|---|-------|-------|
| 1 | [architecture.md](architecture.md) | هيكل المشروع، كيفية العمل، التصميم |
| 2 | [language-reference.md](language-reference.md) | مرجع اللغة — كل الكلمات المفتاحية والتراكيب بما فيها التحسينات الجديدة |
| 3 | [math-library.md](math-library.md) | مكتبة `math` — 59 دالة مثلثات، لوغاريتمات، جذور، هندسة |
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
| 14 | [fastapi-library.md](fastapi-library.md) | مكتبة `fastapi` — 532 دالة، إطار عمل ويب حديث |
| 15 | [requests-library.md](requests-library.md) | مكتبة `requests` — HTTP Client كامل |
| 16 | [sqlite3-library.md](sqlite3-library.md) | مكتبة `sqlite3` — قاعدة بيانات محلية |
| 17 | [asyncio-library.md](asyncio-library.md) | مكتبة `asyncio` — برمجة غير متزامنة |
| 18 | [threading-library.md](threading-library.md) | مكتبة `threading` — تعدد المهام |
| 19 | [unittest-library.md](unittest-library.md) | مكتبة `unittest` — اختبارات الوحدة |
| 20 | [csv-library.md](csv-library.md) | مكتبة `csv` — ملفات بيانات |
| 21 | [logging-library.md](logging-library.md) | مكتبة `logging` — تسجيل الأحداث |
| 22 | [argparse-library.md](argparse-library.md) | مكتبة `argparse` — تحليل وسائط سطر الأوامر |
| 23 | [subprocess-library.md](subprocess-library.md) | مكتبة `subprocess` — أوامر النظام |
| 24 | [configparser-library.md](configparser-library.md) | مكتبة `configparser` — ملفات الإعدادات |
| 25 | [dataclasses-library.md](dataclasses-library.md) | مكتبة `dataclasses` — فئات بيانات، تعدادات، ABC |
| 26 | [advanced-library.md](advanced-library.md) | المكتبة المتقدمة — Decorators, Metaclasses, Data Structures, Concurrency, Types, Descriptors |
| 27 | [error-messages.md](error-messages.md) رسائل الأخطاء — كل أخطاء Python مترجمة بالعربي |

---

## الميزات الجديدة (v1.7)

### Context Managers (إدارة السياق)
```apl
# استخدام with عربي
مع فتح("ملف.txt") مثل f:
    اطبع f.read()

# أو بالإنجليزي
with open("file.txt") as f:
    print(f.read())
```

### Generators (المولدات)
```apl
# yield عربي
دالة أرقام(نهاية):
    لكل i في نطاق(نهاية):
        ولد i  # yield i

# yield from عربي
دالة تسطيح(قائمة):
    لكل عنصر في قائمة:
        ولد_من عنصر  # yield from element
```

### Semicolons (الفواصل المنقوطة)
```apl
# يمكن استخدام ; لفصل الأوامر (اختياري)
المتغير س = 5; اطبع س

# أو بدون ;
المتغير س = 5
اطبع س
```

## المكتبات المتاحة (24 مكتبة)

| المكتبة | عدد الدوال | الوصف |
|---------|-----------:|-------|
| `fastapi` | 532 | إطار عمل ويب حديث |
| `requests` | 249 | HTTP Client كامل |
| `asyncio` | 116 | برمجة غير متزامنة |
| `argparse` | 87 | تحليل وسائط سطر الأوامر |
| `unittest` | 85 | اختبارات الوحدة |
| `logging` | 79 | تسجيل الأحداث |
| `flask` | 77 | إطار عمل ويب |
| `subprocess` | 74 | أوامر النظام |
| `advanced` | 70 | ميزات متقدمة |
| `dataclasses` | 66 | فئات بيانات، تعدادات، ABC |
| `math` | 59 | مثلثات، لوغاريتمات، جذور، تقريب، هندسة |
| `configparser` | 35 | ملفات الإعدادات |
| `os` | 30 | ملفات، مجلدات، مسارات، فحص |
| `threading` | 29 | تعدد المهام |
| `re` | 25 | تعابير نمطية، بحث، استبدال، تقسيم |
| `time` | 25 | وقت، تاريخ، تأخير، تنسيق |
| `sqlite3` | 22 | قاعدة بيانات محلية |
| `random` | 20 | أرقام عشوائية، توزيعات، خلط |
| `itertools` | 19 | أدوات تكرار، توافيق، تباديل |
| `statistics` | 16 | متوسط، وسيط، منوال، تباين، انحراف معياري |
| `csv` | 13 | ملفات بيانات |
| `collections` | 9 | Counter, defaultdict, deque |
| `json` | 8 | قراءة وكتابة JSON |
| `hashlib` | 7 | تجزئة وتشفير |

**إجمالي المكتبات: 1,752 مفتاح في 24 مكتبة (1,579 فريد بعد إزالة التكرار)**

**إجمالي المشروع: ~1,746 دالة ومفتاح بالعربي** — 1,752 من المكتبات + 167 عنصراً في اللغة الأساسية (`core/apl_runner/patterns.py`: كلمات مفتاحية، أنواع، ثوابت، أنماط) − 173 مفتاحاً مكرراً بين المكتبات.

# التوثيق الكامل — APL v1.8

فهرس جميع ملفات التوثيق ومجلد الأمثلة الجاهزة:

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
| 27 | [datetime-library.md](datetime-library.md) | مكتبة `datetime` — التاريخ والوقت والتحويل بينهما، مع الخصائص والثوابت |
| 28 | [pathlib-library.md](pathlib-library.md) | مكتبة `pathlib` — التعامل مع المسارات ككائنات |
| 29 | [shutil-library.md](shutil-library.md) | مكتبة `shutil` — نسخ ونقل وحذف الملفات والمجلدات |
| 30 | [textwrap-library.md](textwrap-library.md) | مكتبة `textwrap` — تنسيق النصوص ولفّها |
| 31 | [uuid-library.md](uuid-library.md) | مكتبة `uuid` — المعرفات الفريدة (UUID) |
| 32 | [base64-library.md](base64-library.md) | مكتبة `base64` — الترميز وفك الترميز |
| 33 | [urllib-library.md](urllib-library.md) | مكتبة `urllib` — تحليل وبناء الروابط وترميزها |
| 34 | [functools-library.md](functools-library.md) | مكتبة `functools` — أدوات الدوال (partial, cache, wraps) |
| 35 | [error-messages.md](error-messages.md) | رسائل الأخطاء — كل أخطاء Python مترجمة بالعربي |

---

## الأمثلة الجاهزة (`examples/`)

10 برامج حقيقية مكتوبة بالكامل بالعربي، وجميعها مختبرة وتعمل بلا أخطاء:

| # | الملف | الوصف | المكتبات المستخدمة |
|---|-------|-------|-------------------|
| 1 | [01-calculator.apl](../examples/01-calculator.apl) | آلة حاسبة تفاعلية | `math`، شروط |
| 2 | [02-sales-report.apl](../examples/02-sales-report.apl) | تقرير مبيعات وخصم | `random`، `math` |
| 3 | [03-task-manager.apl](../examples/03-task-manager.apl) | مدير المهام | `uuid`، قواميس |
| 4 | [04-text-analyzer.apl](../examples/04-text-analyzer.apl) | محلل نصوص | `re` |
| 5 | [05-report-writer.apl](../examples/05-report-writer.apl) | كاتب تقارير | `textwrap` |
| 6 | [06-search-sort.apl](../examples/06-search-sort.apl) | بحث وترتيب (bubble sort) | خوارزميات |
| 7 | [07-sqlite-tasks.apl](../examples/07-sqlite-tasks.apl) | قاعدة بيانات مهام | `sqlite3`، `os` |
| 8 | [08-word-frequency.apl](../examples/08-word-frequency.apl) | عدّاد تكرار الكلمات | `re`، قواميس |
| 9 | [09-encoding-hashing.apl](../examples/09-encoding-hashing.apl) | ترميز وتجزيع | `base64`، `hashlib`، `uuid` |
| 10 | [10-file-manager.apl](../examples/10-file-manager.apl) | مدير ملفات | `pathlib`، `shutil`، `os` |

**التشغيل:**
```bash
python apl.py examples/01-calculator.apl
```

---

## الميزات الجديدة (v1.8)

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

## المكتبات المتاحة (32 مكتبة)

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
| `re` | 25 | تعابير نمطية، بحث، استبدال، تقسيم |
| `time` | 25 | وقت، تاريخ، تأخير، تنسيق |
| `sqlite3` | 22 | قاعدة بيانات محلية |
| `random` | 20 | أرقام عشوائية، توزيعات، خلط |
| `itertools` | 19 | أدوات تكرار، توافيق، تباديل |
| `statistics` | 16 | متوسط، وسيط، منوال، تباين، انحراف معياري |
| `csv` | 13 | ملفات بيانات |
| `urllib` | 13 | تحليل وبناء الروابط وترميزها |
| `uuid` | 13 | المعرفات الفريدة (UUID) |
| `shutil` | 12 | نسخ ونقل وحذف الملفات والمجلدات |
| `base64` | 10 | الترميز وفك الترميز |
| `collections` | 9 | Counter, defaultdict, deque |
| `functools` | 9 | أدوات الدوال (partial, cache, wraps) |
| `textwrap` | 9 | تنسيق النصوص ولفّها |
| `json` | 8 | قراءة وكتابة JSON |
| `hashlib` | 7 | تجزئة وتشفير |

**الإجمالي: 1932 عنصراً في 32 مكتبة** (1763 مفتاحاً فريداً بعد إزالة التكرار).

تشمل العناصر: الدوال، خصائص الكائنات، دوال الكائن المتسلسلة، الثوابت، والمعاملات العربية.
إضافة إلى **168** عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط، دوال مضمّنة)،
ما يجعل الإجمالي الكلي **2100** عنصراً عربياً في اللغة.

تشمل العناصر: الدوال، خصائص الكائنات، دوال الكائن المتسلسلة، الثوابت، والمعاملات العربية.
إضافة إلى **168** عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط، دوال مضمّنة)،
ما يجعل الإجمالي الكلي **2،089** عنصراً عربياً في اللغة.

إضافة إلى **167** عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط)، ما يجعل الإجمالي الكلي أكثر من **2,000** عنصر عربي في اللغة.

**إجمالي المشروع: أكثر من 2,000 عنصر عربي** — 1,921 عنصراً في 32 مكتبة (دوال، خصائص، ثوابت، معاملات عربية) + 167 عنصراً في اللغة الأساسية (`core/apl_runner/patterns.py`: كلمات مفتاحية، أنواع، ثوابت، أنماط).

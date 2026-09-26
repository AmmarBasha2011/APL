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
- **مكتبات بالعربي** — 41 مكتبة مترجمة بالكامل (من `math` و `requests` إلى `datetime` و `decimal` و `operator`)
- **50 مثالاً جاهزاً** — في `examples/`، كلها مختبرة وتعمل
- **رسائل أخطاء بالعربي** — كل أخطاء Python مترجمة للعربية
- **تحويل تلقائي للمستورداات** — يستورد المكتبات المطلوبة تلقائياً
- **بدون dependencies** — فقط Python 3.8+
- **أداء سريع** — تحميل كسول للمكتبات + ذاكرة ترجمة + طيّ ثوابت (4.6× أسرع في الترجمة)
- **فهم متقدم** — list comprehensions، type hints، f-strings، multi-line strings
- **تطابق أنماط متقدم** — `حالة` / `قيمة` مع guards و alternatives
- **معالجة أخطاء حقيقية** — `حاول` / `إمسك مثل متغير` / `أخيراً`
- **دوال مختصرة (lambda)** — `(س) => س * س`赋 Jedi في أي مكان
- **وراثة الأصناف** — `صنف ب(أ):` مع `دالة_إنشاء` للـ constructor
- **أنواع معدودة (Enum)** — قيم مسمّاة بدل الأرقام السحرية
- **إدارة سياق** — `with` statement بالعربي
- **مولدات** — `yield` و `yield from` بالعربي
- **REPL تفاعلي** — جرب الكود سطر بسطر بـ `python apl.py repl`

## المكتبات المتاحة (41 مكتبة)

| المكتبة | عدد العناصر | الوصف |
|---------|------------:|-------|
| `fastapi` | 536 | إطار عمل ويب حديث |
| `requests` | 244 | HTTP Client كامل |
| `advanced` | 135 | ميزات متقدمة (decorators, metaclasses, typing) |
| `asyncio` | 118 | برمجة غير متزامنة |
| `argparse` | 91 | تحليل وسائط سطر الأوامر |
| `unittest` | 85 | اختبارات الوحدة |
| `logging` | 79 | تسجيل الأحداث |
| `flask` | 78 | إطار عمل ويب |
| `subprocess` | 74 | أوامر النظام |
| `dataclasses` | 68 | فئات بيانات، تعدادات، ABC |
| `math` | 63 | مثلثات، لوغاريتمات، جذور، تقريب، هندسة |
| `pathlib` | 61 | التعامل مع المسارات ككائنات |
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
| `json` | 10 | قراءة وكتابة JSON |
| `string` | 10 | مجموعات الأحرف والرموز الثابتة |
| `collections` | 9 | Counter, defaultdict, deque |
| `functools` | 9 | أدوات الدوال (partial, cache, wraps) |
| `textwrap` | 9 | تنسيق النصوص ولفّها |
| `fractions` | 8 | الكسور الرياضية الدقيقة |
| `secrets` | 8 | توليد قيم عشوائية آمنة تشفيرياً |
| `zoneinfo` | 8 | المناطق الزمنية (IANA) |
| `hashlib` | 7 | تجزئة وتشفير |
| `getpass` | 2 | إدخال كلمات السر دون إظهارها |
| `pprint` | 2 | طباعة منسّقة للقواميس والقوائم |
| `enum` | 7 | أنواع معدودة (Enums) — قيم مسمّاة بدل الأرقام السحرية |

**الإجمالي: 2116 عنصراً في 41 مكتبة** (1956 مفتاحاً فريداً بعد إزالة التكرار).

تشمل العناصر: الدوال، خصائص الكائنات، دوال الكائن المتسلسلة، الثوابت، والمعاملات العربية.
إضافة إلى **168** عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط، دوال مضمّنة)،
ما يجعل الإجمالي الكلي **2261** عنصراً عربياً في اللغة.

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

## الأمثلة الجاهزة (50 مثالاً)

مجلد `examples/` يحتوي على **50 برنامجاً حقيقياً** مكتوباً بالكامل بالعربي، وجميعها مختبرة وتعمل بلا أخطاء.

| # | الملف | الوصف |
|--:|-------|-------|
| 1 | [`01-calculator.apl`](examples/01-calculator.apl) | آلة حاسبة تفاعلية |
| 2 | [`02-sales-report.apl`](examples/02-sales-report.apl) | تقرير مبيعات وتقدير الإجمالي |
| 3 | [`03-task-manager.apl`](examples/03-task-manager.apl) | مدير المهام (Lists + Dictionary + Search) |
| 4 | [`04-text-analyzer.apl`](examples/04-text-analyzer.apl) | تحليل نص ومطابقة الأنماط |
| 5 | [`05-report-writer.apl`](examples/05-report-writer.apl) | كاتب التقارير |
| 6 | [`06-search-sort.apl`](examples/06-search-sort.apl) | خوارزميات البحث والترتيب |
| 7 | [`07-sqlite-tasks.apl`](examples/07-sqlite-tasks.apl) | قاعدة بيانات المهام (SQLite) |
| 8 | [`08-word-frequency.apl`](examples/08-word-frequency.apl) | عدّاد الكلمات الم unique مع itertools |
| 9 | [`09-encoding-hashing.apl`](examples/09-encoding-hashing.apl) | تشفير وفك تشفير البيانات (base64 + hashlib) |
| 10 | [`10-file-manager.apl`](examples/10-file-manager.apl) | مدير الملفات والمجلدات |
| 11 | [`11-fibonacci.apl`](examples/11-fibonacci.apl) | مثال تطبيقي |
| 12 | [`12-prime-check.apl`](examples/12-prime-check.apl) | فحص الأعداد الأولية |
| 13 | [`13-matrix-ops.apl`](examples/13-matrix-ops.apl) | عمليات المصفوفات |
| 14 | [`14-statistics-report.apl`](examples/14-statistics-report.apl) | تقرير إحصائي للدرجات |
| 15 | [`15-string-processing.apl`](examples/15-string-processing.apl) | معالجة النصوص |
| 16 | [`16-hash-passwords.apl`](examples/16-hash-passwords.apl) | بصمات كلمات السر |
| 17 | [`17-bank-account.apl`](examples/17-bank-account.apl) | نظام حساب بنكي مبسّط |
| 18 | [`18-linked-list.apl`](examples/18-linked-list.apl) | قائمة مرتبطة |
| 19 | [`19-inventory-system.apl`](examples/19-inventory-system.apl) | نظام إدارة مخزون |
| 20 | [`20-json-config.apl`](examples/20-json-config.apl) | قراءة وكتابة إعدادات JSON |
| 21 | [`21-calculator-class.apl`](examples/21-calculator-class.apl) | آلة حاسبة كصنف |
| 22 | [`22-temperature-converter.apl`](examples/22-temperature-converter.apl) | محول درجات الحرارة |
| 23 | [`23-palindrome-check.apl`](examples/23-palindrome-check.apl) | فحص الكلمات المتناظرة |
| 24 | [`24-roman-numerals.apl`](examples/24-roman-numerals.apl) | تحويل إلى أرقام رومانية |
| 25 | [`25-caesar-cipher.apl`](examples/25-caesar-cipher.apl) | شيفرة قيصر |
| 26 | [`26-queue-stack.apl`](examples/26-queue-stack.apl) | طابور ومكدّس |
| 27 | [`27-expense-tracker.apl`](examples/27-expense-tracker.apl) | متتبع المصروفات |
| 28 | [`28-binary-search.apl`](examples/28-binary-search.apl) | البحث الثنائي |
| 29 | [`29-coin-change.apl`](examples/29-coin-change.apl) | مشكلة تغيير العملات |
| 30 | [`30-lru-cache-decorator.apl`](examples/30-lru-cache-decorator.apl) | كاش LRU مع functools |
| 31 | [`31-decorator-timer.apl`](examples/31-decorator-timer.apl) | مزخرف قياس الأداء |
| 32 | [`32-generator-pipeline.apl`](examples/32-generator-pipeline.apl) | خط أنابيب بالمولدات |
| 33 | [`33-comprehension-examples.apl`](examples/33-comprehension-examples.apl) | القوائم فهم comprehensions |
| 34 | [`34-args-parser-cli.apl`](examples/34-args-parser-cli.apl) | محلل وسائط سطر الأوامر |
| 35 | [`35-logging-setup.apl`](examples/35-logging-setup.apl) | إعداد السجلات |
| 36 | [`36-threading-tasks.apl`](examples/36-threading-tasks.apl) | تنفيذ مهام متوازية |
| 37 | [`37-csv-report.apl`](examples/37-csv-report.apl) | قراءة وكتابة ملفات CSV |
| 38 | [`38-hashlib-integrity.apl`](examples/38-hashlib-integrity.apl) | التحقق من سلامة البيانات |
| 39 | [`39-uuid-tokens.apl`](examples/39-uuid-tokens.apl) | توليد معرفات فريدة |
| 40 | [`40-latin-converter.apl`](examples/40-latin-converter.apl) | تحويل بين الأرقام العربية والهندية |
| 41 | [`41-word-frequency-top.apl`](examples/41-word-frequency-top.apl) | أكثر الكلمات تكراراً |
| 42 | [`42-geometry-shapes.apl`](examples/42-geometry-shapes.apl) | أشكال هندسية |
| 43 | [`43-parallel-processing.apl`](examples/43-parallel-processing.apl) | المعالجة عبر map و filter |
| 44 | [`44-tic-tac-toe.apl`](examples/44-tic-tac-toe.apl) | لعبة tic-tac-toe |
| 45 | [`45-simple-lexer.apl`](examples/45-simple-lexer.apl) | محلّل نصوص بسيط |
| 46 | [`46-simple-interpreter.apl`](examples/46-simple-interpreter.apl) | مفسّر حسابات مبسّط |
| 47 | [`47-simple-cache.apl`](examples/47-simple-cache.apl) | كاش بسيط من الصفر |
| 48 | [`48-text-analyzer-advanced.apl`](examples/48-text-analyzer-advanced.apl) | تحليل نص متقدم |
| 49 | [`49-validate-input.apl`](examples/49-validate-input.apl) | التحقق من صحة المدخلات |
| 50 | [`50-final-showcase.apl`](examples/50-final-showcase.apl) | العرض النهائي (شامل) |

### تشغيل أي مثال

```bash
python apl.py examples/02-sales-report.apl
echo "1" | python apl.py examples/01-calculator.apl   # مثال يحتاج إدخال
```

### اختبار الأمثلة

```bash
python test_examples.py     # يشغّل كل الأمثلة ويفحص النتائج
```

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

**الإصدار:** APL v1.8 — 2,284 عنصر عربي — 41 مكتبة — 50 مثالاً

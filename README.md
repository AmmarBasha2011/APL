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
- **مكتبات بالعربي** — 46 مكتبة مترجمة بالكامل (من `math` و `requests` إلى `datetime` و `decimal` و `xml` و `archive` و `net`)
- **73 مثالاً جاهزاً** — في `examples/`، كلها مختبرة وتعمل
- **رسائل أخطاء بالعربي** — كل أخطاء Python مترجمة للعربية
- **تحويل تلقائي للمستورداات** — يستورد المكتبات المطلوبة تلقائياً
- **بدون dependencies** — فقط Python 3.14+
- **أداء سريع** — تحميل كسول للمكتبات + ذاكرة ترجمة + طيّ ثوابت (4.6× أسرع في الترجمة)
- **فهم متقدم** — list comprehensions، type hints، f-strings، multi-line strings
- **أدوات مطوّر بالعربي** — فحص الكائنات وتوقيعات الدوال، شجرة بناء الجملة، تفكيك البايتكود، المصحّح، القياس والتحليل (1123 عنصراً)
- **الويب والبريد بالعربي** — العناوين وHTTP والبريد وصناديقه والكوكيز وHTML وWSGI وXML-RPC (2761 عنصراً)
- **تطابق أنماط متقدم** — `حالة` / `قيمة` مع guards و alternatives
- **معالجة أخطاء حقيقية** — `حاول` / `إمسك مثل متغير` / `أخيراً`
- **دوال مختصرة (lambda)** — `(س) => س * س` في أي موضع
- **وراثة الأصناف** — `صنف ب(أ):` مع `دالة_إنشاء` للـ constructor
- **أنواع معدودة (Enum)** — قيم مسمّاة بدل الأرقام السحرية
- **إدارة سياق** — `with` statement بالعربي
- **مولدات** — `yield` و `yield from` بالعربي
- **REPL تفاعلي** — جرب الكود سطر بسطر بـ `python apl.py repl`

## المكتبات المتاحة (46 مكتبة)

| المكتبة | عدد العناصر | الوصف |
|---------|------------:|-------|
| `devtools` | 1123 | أدوات المطوّر: فحص، تصحيح، قياس أداء، ترجمة (inspect / ast / dis / pdb / doctest / timeit / profile / tracemalloc) |
| `web` | 2761 | الويب والبريد: عناوين، HTTP، بريد، صناديق، كوكيز، HTML، WSGI، XML-RPC (http / urllib / email / mailbox / html / wsgiref / xmlrpc) |
| `net` | 1006 | الشبكة: socket و ssl و http و email و SMTP/IMAP/FTP |
| `fastapi` | 536 | إطار عمل ويب حديث |
| `requests` | 244 | HTTP Client كامل |
| `advanced` | 135 | ميزات متقدمة (decorators, metaclasses, typing) |
| `asyncio` | 118 | برمجة غير متزامنة |
| `argparse` | 109 | تحليل وسائط سطر الأوامر |
| `xml` | 109 | قراءة وبناء وتعديل ملفات XML (ElementTree) |
| `archive` | 106 | أرشيف ZIP و TAR وضغط gzip / bz2 / xz |
| `logging` | 87 | تسجيل الأحداث |
| `unittest` | 84 | اختبارات الوحدة |
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
| `time` | 25 | وقت، تاريخ، تأخير، تنسيق |
| `re` | 25 | تعابير نمطية، بحث، استبدال، تقسيم |
| `sqlite3` | 24 | قاعدة بيانات محلية |
| `decimal` | 24 | الحساب العشري الدقيق (بدون أخطاء تقريب) |
| `random` | 20 | أرقام عشوائية، توزيعات، خلط |
| `itertools` | 19 | أدوات تكرار، توافيق، تباديل |
| `statistics` | 16 | متوسط، وسيط، منوال، تباين، انحراف معياري |
| `csv` | 13 | ملفات بيانات |
| `uuid` | 13 | المعرفات الفريدة (UUID) |
| `urllib` | 13 | تحليل وبناء الروابط وترميزها |
| `shutil` | 12 | نسخ ونقل وحذف الملفات والمجلدات |
| `base64` | 11 | الترميز وفك الترميز |
| `json` | 10 | قراءة وكتابة JSON |
| `string` | 10 | مجموعات الأحرف والرموز الثابتة |
| `collections` | 9 | Counter, defaultdict, deque |
| `textwrap` | 9 | تنسيق النصوص ولفّها |
| `functools` | 9 | أدوات الدوال (partial, cache, wraps) |
| `fractions` | 8 | الكسور الرياضية الدقيقة |
| `secrets` | 8 | توليد قيم عشوائية آمنة تشفيرياً |
| `zoneinfo` | 8 | المناطق الزمنية (IANA) |
| `hashlib` | 7 | تجزئة وتشفير |
| `enum` | 7 | أنواع معدودة (Enums) — قيم مسمّاة بدل الأرقام السحرية |
| `getpass` | 2 | إدخال كلمات السر دون إظهارها |
| `pprint` | 2 | طباعة منسّقة للقواميس والقوائم |

**الإجمالي: 7,231 عنصراً في 46 مكتبة** (7,213 مفتاحاً فريداً بعد إزالة التكرار).

تشمل العناصر: الدوال، خصائص الكائنات، دوال الكائن المتسلسلة، الثوابت، والمعاملات العربية.
إضافة إلى 231 عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط، دوال مضمّنة)
في `core/apl_runner/patterns.py`، فيصبح عدد العناصر العربية الفريدة في اللغة **7,444 عنصراً**.

## الأمثلة

**جمع عددين:**
```apl
المتغير أ = 7
المتغير ب = 5
اطبع "المجموع:", أ + ب

# للقراءة من لوحة المفاتيح استعمل:
# المتغير أ = صحيح(ادخل("الأول: "))
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
# طلب HTTP عبر مكتبة requests (يحتاج اتصالاً بالشبكة)
حاول:
    المتغير ر = جيت("https://api.github.com/zen")
    اطبع "الحالة:", ر.status_code
    اطبع "الرد:", ر.text.strip()
إمسك:
    اطبع "تعذّر الوصول إلى الشبكة الآن - الكود نفسه صحيح"
```

**API سريع:**
```apl
المتغير app = فاست_أبي()

@مسار_جيت("/")
دالة_رئيسية():
    ارجع {"رسالة": "مرحباً"}

@مسار_جيت("/عناصر/{معرف}")
دالة_عنصر(معرف: صحيح):
    ارجع {"معرف": معرف}

اطبع [مسار.path for مسار in app.routes]
```

**قاعدة بيانات SQLite:**
```apl
المتغير اتصال = افتح_قاعدة("_تجربة.db")
المتغير مؤشر_ج = اتصال.cursor()
مؤشر_ج.نفذ("CREATE TABLE users (id INTEGER, name TEXT)")
مؤشر_ج.نفذ("INSERT INTO users VALUES (1, ?)", ("عمار",))
اتصال.تأكد()
مؤشر_ج.نفذ("SELECT * FROM users")
اطبع مؤشر_ج.جلب_الكل()
اتصال.أغلق_قاعدة()
احذف_ملف("_تجربة.db")
```

**XML — قراءة مستند:**
```apl
المتغير مستند = "<مكتبة><كتاب نوع='علمي'><العنوان>الفيزياء</العنوان></كتاب></مكتبة>"
المتغير الجذر = إكس_إم_إل_من_نص(مستند)

لكل كتاب في الجذر.كرر("كتاب"):
    اطبع كتاب.ابحث_نص("العنوان") + " — " + كتاب.اقرأ_خاصية("نوع")
```

**XML — بناء وحفظ:**
```apl
المتغير الجذر = عنصر_جديد("مكتبة")
المتغير كتاب = عنصر_فرعي_جديد(الجذر, "كتاب", {"نوع": "علمي"})
غذِّ_نص_العنصر(كتاب, "الفيزياء الحديثة")
احفظ_إكس_إم_إل(الجذر, "مكتبة.xml")
اطبع إكس_إم_إل_إلى_نص(الجذر)
```

**أرشيف وضغط — نسخة احتياطية:**
```apl
# المقتطف مستقل: ينشئ مجلده وينظّفه
انشئ_مجلدات("المشروع")
اكتب("المشروع/README.md", "# مشروع\n")

أنشئ_أرشيف("نسخة.zip", ["المشروع"])      # كل الملفات والمجلدات
عرض_الأرشيف("نسخة.zip")                   # جدول الأعضاء والأحجام
استخرج_الأرشيف("نسخة.zip", "مستخرج")     # استخراج آمن

المتغير مضغوط = ضغط_فائق("نص طويل جداً " * 100)
اطبع حجم_بشري(طول(مضغوط))

احذف_ملف("نسخة.zip")
احذف_شجرة("مستخرج")
احذف_شجرة("المشروع")
```

**Context Manager:**
```apl
# المقتطف مستقل: ينشئ ملفه وينظّفه
اكتب("ملف.txt", "سطر من الملف\n")

مع فتح('ملف.txt', 'r') مثل f:
    محتوى = f.read()
    اطبع محتوى

احذف_ملف("ملف.txt")
```

**Generator:**
```apl
دالة أرقام(نهاية):
    لكل i في نطاق(نهاية):
        ولد i  # yield i

لكل رقم في أرقام(10):
   اطبع رقم
```

## الأمثلة الجاهزة (73 مثالاً)

مجلد `examples/` يحتوي على **66 برنامجاً حقيقياً** مكتوباً بالكامل بالعربي، وجميعها مختبرة وتعمل بلا أخطاء.

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
| 51 | [`51-xml-read.apl`](examples/51-xml-read.apl) | قراءة مستند XML وتحليله |
| 52 | [`52-xml-build.apl`](examples/52-xml-build.apl) | بناء ملف XML وتعديله وحفظه |
| 53 | [`53-xml-namespaces.apl`](examples/53-xml-namespaces.apl) | مساحات الأسماء والتحليل التدريجي والباني |
| 54 | [`54-archive-zip.apl`](examples/54-archive-zip.apl) | أرشيف ZIP: إنشاء، قراءة، تعديل، استخراج |
| 55 | [`55-archive-compress.apl`](examples/55-archive-compress.apl) | الضغط: gzip و bz2 و xz وأرشيف TAR |
| 56 | [`56-archive-backup.apl`](examples/56-archive-backup.apl) | أداة نسخ احتياطي حقيقية بالأرشيف |
| 57 | [`57-net-tcp.apl`](examples/57-net-tcp.apl) | مقابس TCP و UDP: خادم وعميل على نفس الجهاز |
| 58 | [`58-net-http.apl`](examples/58-net-http.apl) | خادم HTTP محلي وعميله حتى تحليل JSON |
| 59 | [`59-net-email.apl`](examples/59-net-email.apl) | بناء رسالة بريد ومرفق وحفظها `.eml` ثم قراءتها |
| 60 | [`60-net-tools.apl`](examples/60-net-tools.apl) | أدوات بلا اتصال: IP و struct و ترميزات و MIME |
| 61 | [`61-devtools-inspect.apl`](examples/61-devtools-inspect.apl) | فحص الكائنات: التوقيع، النوع، الأعضاء، شجرة الأصناف (devtools) |
| 62 | [`62-devtools-ast.apl`](examples/62-devtools-ast.apl) | شجرة بناء الجملة: تحليل المصدر وتجوال العقد (devtools/ast) |
| 63 | [`63-devtools-dis.apl`](examples/63-devtools-dis.apl) | تفكيك الشيفرة وتقطيع الرموز وجداول الرموز (devtools/dis) |
| 64 | [`64-devtools-traceback.apl`](examples/64-devtools-traceback.apl) | تنسيق تتبع الأخطاء واختبارات الوثائق (devtools/traceback) |
| 65 | [`65-devtools-profile.apl`](examples/65-devtools-profile.apl) | قياس الزمن وتحليل الأداء والذاكرة (devtools/timeit) |
| 66 | [`66-devtools-import.apl`](examples/66-devtools-import.apl) | الاستيراد الديناميكي والتحذيرات وذاكرة الأسطر (devtools/importlib) |
| 67 | [`67-web-http-status.apl`](examples/67-web-http-status.apl) | ثوابت حالات HTTP (web/http) |
| 68 | [`68-web-url-parse.apl`](examples/68-web-url-parse.apl) | تحليل العناوين وترميزها وربطها (web/urllib.parse) |
| 69 | [`69-web-email-build.apl`](examples/69-web-email-build.apl) | بناء رسائل البريد وإخراجها (web/email) |
| 70 | [`70-web-mailbox-mime.apl`](examples/70-web-mailbox-mime.apl) | صناديق البريد وأنواع MIME (web/mailbox) |
| 71 | [`71-web-html-cookies.apl`](examples/71-web-html-cookies.apl) | تهريب HTML وملفات تعريف الارتباط (web/html) |
| 72 | [`72-web-xmlrpc-wsgi.apl`](examples/72-web-xmlrpc-wsgi.apl) | نداءات XML-RPC ورؤوس WSGI (web/xmlrpc) |
| 73 | [`73-web-robots-maildir.apl`](examples/73-web-robots-maildir.apl) | تحليل robots.txt وصناديق Maildir (web/urllib) |

### تشغيل أي مثال

```bash
python apl.py examples/02-sales-report.apl
echo "1" | python apl.py examples/01-calculator.apl   # مثال يحتاج إدخال
```

### اختبار الأمثلة

```bash
python test_examples.py     # يشغّل كل الأمثلة ويفحص النتائج
```

## التحقق المستمر

كل الفحوص دي بتشتغل في أمر واحد:

```bash
./scripts/check.sh            # نفس اللي بتشتغل في CI
./scripts/check.sh --quiet    # من غير التفاصيل
```

وبتتفصّل كده:

| الأمر | ماذا يفحص |
|-------|-----------|
| `python scripts/check_libraries.py` | كل عنصر في كل مكتبة يُترجم فعلاً لهدفه + حلّ المسارات + مفيش تكرار ولا تصادم |
| `python scripts/check_repo.py` | `compileall` + اتساق النسخة والأرقام في التوثيق + التحميل الكسول + بلوكات `README` |
| `python test_examples.py` | يشغّل كل الأمثلة الـ 66 ويفحص **مخرجاتها** مش بس عدم الخطأ |

أي خطأ تشغيل في `apl.py` بيطلع **كود 1**، فالفحوص بتقدر تعتمد على الكود مش على نص الخطأ.

### المشاكل المعروفة (baseline)

`scripts/baselines/library_issues.txt` بيسجّل مشاكل قديمة في مكتبات موجودة قبل وقت طويل
(أسماء اتشالت من Python مثل `ssl.match_hostname` و`configparser.SafeConfigParser`،
ومفاتيح بتتصادم مع كلمات النواة). الفحص بيفشل فقط على **الجديد**:

```bash
python scripts/check_libraries.py --strict            # يعرض القديم كمان
python scripts/check_libraries.py --update-baseline   # يحدّث الـ baseline
```

### GitHub Actions

- **[CI](.github/workflows/ci.yml)** — كل push على `main` وكل PR: المكتبات + الريبو + الأمثلة،
  بالإضافة إلى job **غير حاجب** على أحدث نسخة (3.15) يبلّغ عن الانحراف قبل ما يطلع.
- **[Stdlib drift](.github/workflows/stdlib-drift.yml)** — كل إثنين 04:23 UTC + كل PR + يدوياً؛
  أي فشل بيفتح **issue تلقائياً** (بدون تكرار)، ولما الفحص يرجع أخضر **بيقفلها تلقائياً**.

## مقارنة الأداء: APL مقابل Python

تجد اختباراً قابلاً لإعادة التشغيل لقياس حلقة حسابية متطابقة في `benchmarks/`، مع **مليون دورة في كل عينة و100 عينة افتراضياً**. يقيس الاختبار التنفيذ بعد الترجمة، وكلفة ترجمة APL، وتشغيل الملف كاملاً مع ذاكرة الترجمة وبدونها، ويتأكد من تطابق الناتج.

```bash
python benchmarks/run_benchmark.py
python benchmarks/run_benchmark.py --iterations 100000 --runs 10 --setup-runs 5 --process-runs 3 --output benchmarks/latest-results.json
```

افتح [`benchmark.html`](benchmark.html) لعرض التقرير العربي، أو حمّل إليه ملف JSON الناتج من الاختبار. الصفحة مكتفية ذاتياً ولا تحتاج إلى اتصال بالإنترنت.

> APL في هذا المشروع يحوّل الشيفرة العربية إلى Python؛ لذلك يستخدم قياس التنفيذ الصافي CPython في اللغتين، بينما يُظهر قياس تشغيل الملف كلفة بدء محرك APL والترجمة وذاكرتها المؤقتة.

## التوثيق الكامل

📚 **[فهرس التوثيق](docs/README.md)** — مرجع كامل لكل التفاصيل

## المتطلبات

- Python 3.14+
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

**الإصدار:** APL v1.11 — 7,444 عنصراً عربياً — 46 مكتبة — 73 مثالاً

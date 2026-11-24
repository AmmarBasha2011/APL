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
- **مكتبات بالعربي** — 63 مكتبة مترجمة بالكامل (من `math` و `requests` إلى `datetime` و `decimal` و `xml` و `archive` و `net`)
- **500 مثال جاهز** — في `examples/`، كلها مختبرة وتعمل
- **رسائل أخطاء بالعربي** — كل أخطاء Python مترجمة للعربية
- **تحويل تلقائي للمستورداات** — يستورد المكتبات المطلوبة تلقائياً
- **بدون dependencies** — فقط Python 3.14+
- **أداء سريع** — تحميل كسول للمكتبات + ذاكرة ترجمة + طيّ ثوابت (4.6× أسرع في الترجمة)
- **فهم متقدم** — list comprehensions، type hints، f-strings، multi-line strings
- **أدوات مطوّر بالعربي** — فحص الكائنات وتوقيعات الدوال، شجرة بناء الجملة، تفكيك البايتكود، المصحّح، القياس والتحليل (1123 عنصراً)
- **الويب والبريد بالعربي** — العناوين وHTTP والبريد وصناديقه والكوكيز وHTML وWSGI وXML-RPC (2757 عنصراً)
- **البيانات والملفات بالعربي** — مسارات وضغط وأرشيف وتسلسل وهياكل بيانات وXML ويونيكود (2631 عنصراً)
- **تطابق أنماط متقدم** — `حالة` / `قيمة` مع guards و alternatives
- **معالجة أخطاء حقيقية** — `حاول` / `إمسك مثل متغير` / `أخيراً`
- **دوال مختصرة (lambda)** — `(س) => س * س` في أي موضع
- **وراثة الأصناف** — `صنف ب(أ):` مع `دالة_إنشاء` للـ constructor
- **أنواع معدودة (Enum)** — قيم مسمّاة بدل الأرقام السحرية
- **إدارة سياق** — `with` statement بالعربي
- **مولدات** — `yield` و `yield from` بالعربي
- **REPL تفاعلي** — جرب الكود سطر بسطر بـ `python apl.py repl`

## المكتبات المتاحة (63 مكتبة)

| المكتبة | عدد العناصر | الوصف |
|---------|------------:|-------|
| `devtools` | 1123 | أدوات المطوّر: فحص، تصحيح، قياس أداء، ترجمة (inspect / ast / dis / pdb / doctest / timeit / profile / tracemalloc) |
| `datafiles` | 2631 | البيانات والملفات: مسارات، ضغط، أرشيف، تسلسل، هياكل بيانات، XML، يونيكود (io / zipfile / tarfile / pickle / shelve / array / struct / xml.dom / xml.etree / unicodedata) |
| `syslib` | 3973 | النظام والتشغيل والتشخيص: منصة، إشارات، موارد، تسجيل، اختبارات، عمليات متعددة، ctypes، سياق (platform / signal / resource / logging / unittest / multiprocessing / concurrent.futures / ctypes / termios) |
| `weblibs` | 5496 | الويب والنصوص: بث متدفق، قوالب، ماركداون، تورنيدو، سطر الأوامر، تلوين الشيفرة (websockets / jinja2 / markdown / tornado / click / pygments) |
| `webserver` | 5492 | الخوادم والشبكات: خوادم ASGI/WSGI، عملاء HTTP غير متزامنين، HTTP/1.1 (starlette / uvicorn / httpx / httpcore / h11 / anyio) |
| `secauth` | 5495 | الأمان والمصادقة: تشفير وشهادات، قوالب معزولة، تحقق من المخططات، JWT (cryptography / jinja2 / jsonschema / jwt / cffi) |
| `textdata` | 5492 | النصوص والبيانات: مطابقة الأنماط، أصناف الخصائص، الصور، النماذج الأولية (pathspec / attrs / PIL / markdown / proto) |
| `utiltools` | 5494 | الأدوات المساعدة: الإصدارات والتواريخ، أشرطة التقدم، مراقبة العمليات (packaging / dateutil / tqdm / psutil / websockets) |
| `idlelib` | 11138 | بيئة التطوير المدمجة: محرر، إكمال تلقائي، مصحح، إعدادات (idlelib) |
| `cdp_use` | 10569 | بروتوكول أدوات تطوير كروم CDP (cdp_use) |
| `acp` | 11180 | بروتوكول العميل-الوكيل ACP (acp) |
| `aiohttp` | 15592 | عميل وخادم HTTP غير متزامنين (aiohttp) |
| `stdlib_ext` | 12950 | توسعة المكتبة القياسية (encodings / inspect / doctest / pdb / tracemalloc) |
| `numpy` | 5937 | الحساب العددي: مصفوفات، جبر خطي، تحويلات فورييه، عشوائيات (numpy) |
| `scipy` | 8396 | الحساب العلمي: تكامل، تحسين، استيفاء، إحصاء، مصفوفات متناثرة (scipy) |
| `telegram` | 6429 | بوتات تيليجرام: رسائل، محادثات، مستخدمون، لوحات مفاتيح (python-telegram-bot) |
| `redis` | 6500 | تخزين المفاتيح والقيم والجلسات والمهام الموزعة (redis-py) |
| `celery` | 6350 | طوابير المهام الموزعة والجدولة الزمنية (celery) |
| `web` | 2757 | الويب والبريد: عناوين، HTTP، بريد، صناديق، كوكيز، HTML، WSGI، XML-RPC (http / urllib / email / mailbox / html / wsgiref / xmlrpc) |
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

**الإجمالي: 136,341 عنصراً في 63 مكتبة** (136,323 مفتاحاً فريداً بعد إزالة التكرار).

تشمل العناصر: الدوال، خصائص الكائنات، دوال الكائن المتسلسلة، الثوابت، والمعاملات العربية.
إضافة إلى 231 عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط، دوال مضمّنة)
في `core/apl_runner/patterns.py`، فيصبح عدد العناصر العربية الفريدة في اللغة **136,554 عنصراً**.

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

## الأمثلة الجاهزة (500 مثال)

مجلد `examples/` يحتوي على **500 برنامج حقيقي** مكتوباً بالكامل بالعربي، وجميعها مختبرة وتعمل بلا أخطاء.

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
| 58 | [`47-simple-cache.apl`](examples/47-simple-cache.apl) | كاش بسيط من الصفر |
| 58 | [`48-text-analyzer-advanced.apl`](examples/48-text-analyzer-advanced.apl) | تحليل نص متقدم |
| 49 | [`49-validate-input.apl`](examples/49-validate-input.apl) | التحقق من صحة المدخلات |
| 50 | [`50-final-showcase.apl`](examples/50-final-showcase.apl) | العرض النهائي (شامل) |
| 51 | [`51-xml-read.apl`](examples/51-xml-read.apl) | قراءة مستند XML وتحليله |
| 52 | [`52-xml-build.apl`](examples/52-xml-build.apl) | بناء ملف XML وتعديله وحفظه |
| 58 | [`53-xml-namespaces.apl`](examples/53-xml-namespaces.apl) | مساحات الأسماء والتحليل التدريجي والباني |
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
| 74 | [`74-df-paths.apl`](examples/74-df-paths.apl) | المسارات والبحث النمطي (datafiles/os.path) |
| 75 | [`75-df-archive.apl`](examples/75-df-archive.apl) | ضغط zip وgzip وbz2 (datafiles/zipfile) |
| 76 | [`76-df-serialize.apl`](examples/76-df-serialize.apl) | تسلسل البيانات (datafiles/pickle) |
| 77 | [`77-df-structures.apl`](examples/77-df-structures.apl) | هياكل البيانات (datafiles/array) |
| 78 | [`78-df-xml.apl`](examples/78-df-xml.apl) | بناء XML وتحليله (datafiles/xml) |
| 79 | [`79-df-text.apl`](examples/79-df-text.apl) | يونيكود والترميز (datafiles/unicodedata) |
| 80 | [`80-df-refs.apl`](examples/80-df-refs.apl) | المراجع والسياق والفروق (datafiles/weakref) |
| 81 | [`81-syslib-system.apl`](examples/81-syslib-system.apl) | معلومات النظام (syslib/platform) |
| 82 | [`82-syslib-signals.apl`](examples/82-syslib-signals.apl) | الإشارات وحدود الموارد (syslib/signal) |
| 83 | [`83-syslib-logging.apl`](examples/83-syslib-logging.apl) | التسجيل (syslib/logging) |
| 84 | [`84-syslib-docs.apl`](examples/84-syslib-docs.apl) | التوثيق ويونيكود والفروق (syslib/pydoc) |
| 85 | [`85-syslib-processes.apl`](examples/85-syslib-processes.apl) | العمليات المتعددة (syslib/multiprocessing) |
| 86 | [`86-syslib-ctypes.apl`](examples/86-syslib-ctypes.apl) | ctypes والأنواع (syslib/ctypes) |
| 87 | [`87-syslib-context.apl`](examples/87-syslib-context.apl) | السياق وتحليل الأوامر (syslib/contextvars) |
| 88 | [`88-weblibs.apl`](examples/88-weblibs.apl) | الويب والنصوص (weblibs/markdown) |
| 89 | [`89-webserver.apl`](examples/89-webserver.apl) | الخوادم (webserver/uvicorn) |
| 90 | [`90-secauth.apl`](examples/90-secauth.apl) | الأمان والمصادقة (secauth/jinja2) |
| 91 | [`91-textdata.apl`](examples/91-textdata.apl) | النصوص والبيانات (textdata/pathspec) |
| 92 | [`92-utiltools.apl`](examples/92-utiltools.apl) | الأدوات (utiltools/dateutil) |
| 93 | [`93-idlelib.apl`](examples/93-idlelib.apl) | بيئة التطوير (idlelib) |
| 94 | [`94-cdp-use.apl`](examples/94-cdp-use.apl) | المتصفح (cdp_use) |
| 95 | [`95-acp.apl`](examples/95-acp.apl) | الوكلاء (acp) |
| 96 | [`96-aiohttp2.apl`](examples/96-aiohttp2.apl) | الويب غير المتزامن (aiohttp) |
| 97 | [`97-stdlib-ext.apl`](examples/97-stdlib-ext.apl) | المكتبة الموسّعة (stdlib_ext) |
| 98 | [`98-numpy.apl`](examples/98-numpy.apl) | الحساب العددي (numpy) |
| 99 | [`99-scipy.apl`](examples/99-scipy.apl) | الحساب العلمي (scipy) |
| 100 | [`100-telegram.apl`](examples/100-telegram.apl) | بوتات تيليجرام (telegram) |
| 101 | [`101-redis.apl`](examples/101-redis.apl) | تخزين ريديس (redis) |
| 102 | [`102-celery.apl`](examples/102-celery.apl) | طوابير المهام (celery) |
| 103 | [`103-gcd-lcm.apl`](examples/103-gcd-lcm.apl) | القاسم المشترك والمضاعف المشترك ونظرية الأعداد |
| 104 | [`104-trig-table.apl`](examples/104-trig-table.apl) | جدول الدوال المثلثية |
| 105 | [`105-log-exp.apl`](examples/105-log-exp.apl) | اللوغاريتمات والأسس والجذور |
| 106 | [`106-rounding.apl`](examples/106-rounding.apl) | التقريب بكل أنواعه |
| 107 | [`107-special-funcs.apl`](examples/107-special-funcs.apl) | الدوال الخاصة: جاما ودالة الخطأ |
| 108 | [`108-decimal-money.apl`](examples/108-decimal-money.apl) | حساب الأموال بدقة بلا أخطاء عشرية |
| 109 | [`109-fractions-ops.apl`](examples/109-fractions-ops.apl) | الكسور الدقيقة والعمليات عليها |
| 110 | [`110-statistics-data.apl`](examples/110-statistics-data.apl) | تقرير إحصائي لدرجات طلاب |
| 111 | [`111-random-dice.apl`](examples/111-random-dice.apl) | محاكاة رمي نرد |
| 112 | [`112-montecarlo-pi.apl`](examples/112-montecarlo-pi.apl) | تقدير ط بطريقة مونت كارلو |
| 113 | [`113-string-constants.apl`](examples/113-string-constants.apl) | ثوابت النصوص وتصنيف الحروف |
| 114 | [`114-string-template.apl`](examples/114-string-template.apl) | قوالب النصوص |
| 115 | [`115-textwrap-report.apl`](examples/115-textwrap-report.apl) | تنسيق التقارير النصية |
| 116 | [`116-re-emails.apl`](examples/116-re-emails.apl) | استخراج البريد الإلكتروني والأرقام من نص |
| 117 | [`117-re-arabic-words.apl`](examples/117-re-arabic-words.apl) | البحث عن الكلمات العربية في نص |
| 118 | [`118-re-substitutions.apl`](examples/118-re-substitutions.apl) | الاستبدال والتقسيم بالأنماط |
| 119 | [`119-text-palindromes.apl`](examples/119-text-palindromes.apl) | كشف النصوص المتناظرة |
| 120 | [`120-text-slug.apl`](examples/120-text-slug.apl) | توليد روابط صديقة من العناوين |
| 121 | [`121-text-wordcount.apl`](examples/121-text-wordcount.apl) | تكرار الكلمات في نص عربي |
| 122 | [`122-text-case-tools.apl`](examples/122-text-case-tools.apl) | أدوات الحالة والفحص في النصوص |
| 123 | [`123-text-split-join.apl`](examples/123-text-split-join.apl) | التقسيم والدمج |
| 124 | [`124-text-validate.apl`](examples/124-text-validate.apl) | التحقق من المدخلات بالأنماط |
| 125 | [`125-datetime-arithmetic.apl`](examples/125-datetime-arithmetic.apl) | حسابات التواريخ والمدد |
| 126 | [`126-datetime-format.apl`](examples/126-datetime-format.apl) | تنسيق وتحليل التواريخ |
| 127 | [`127-datetime-age.apl`](examples/127-datetime-age.apl) | حساب العمر بالتفصيل |
| 128 | [`128-zoneinfo-meeting.apl`](examples/128-zoneinfo-meeting.apl) | تحويل اجتماع بين المناطق الزمنية |
| 129 | [`129-time-stopwatch.apl`](examples/129-time-stopwatch.apl) | ساعة إيقاف لقياس الأداء |
| 130 | [`130-datetime-weekday.apl`](examples/130-datetime-weekday.apl) | أيام الأسبوع وعطلات نهاية الأسبوع |
| 131 | [`131-month-calendar.apl`](examples/131-month-calendar.apl) | طباعة تقويم شهر |
| 132 | [`132-pathlib-ops.apl`](examples/132-pathlib-ops.apl) | المسارات ككائنات |
| 133 | [`133-file-search-ext.apl`](examples/133-file-search-ext.apl) | البحث عن ملفات بامتداد معين |
| 134 | [`134-file-dedup-hash.apl`](examples/134-file-dedup-hash.apl) | كشف الملفات المكررة بالتجزئة |
| 135 | [`135-dir-size-report.apl`](examples/135-dir-size-report.apl) | تقرير أحجام المجلدات |
| 136 | [`136-shutil-backup.apl`](examples/136-shutil-backup.apl) | نسخ احتياطي لمجلد كامل |
| 137 | [`137-file-rename-batch.apl`](examples/137-file-rename-batch.apl) | إعادة تسمية مجموعة ملفات |
| 138 | [`138-os-env.apl`](examples/138-os-env.apl) | معلومات النظام والبيئة |
| 139 | [`139-file-read-write.apl`](examples/139-file-read-write.apl) | القراءة والكتابة الأساسية للملفات |
| 140 | [`140-json-nested.apl`](examples/140-json-nested.apl) | JSON متداخل: بناء وقراءة |
| 141 | [`141-json-files.apl`](examples/141-json-files.apl) | حفظ وقراءة JSON من ملف |
| 142 | [`142-json-merge.apl`](examples/142-json-merge.apl) | دمج وتحديث قواميس JSON |
| 143 | [`143-csv-write-read.apl`](examples/143-csv-write-read.apl) | كتابة وقراءة CSV |
| 144 | [`144-csv-stats.apl`](examples/144-csv-stats.apl) | إحصاءات على عمود CSV |
| 145 | [`145-configparser-settings.apl`](examples/145-configparser-settings.apl) | ملفات الإعدادات |
| 146 | [`146-json-to-csv.apl`](examples/146-json-to-csv.apl) | تحويل JSON إلى CSV |
| 147 | [`147-counter-advanced.apl`](examples/147-counter-advanced.apl) | العداد المتقدم |
| 148 | [`148-deque-printer.apl`](examples/148-deque-printer.apl) | صف انتظار مهام الطباعة |
| 149 | [`149-itertools-combos.apl`](examples/149-itertools-combos.apl) | التوافيق والناتج الديكارتي |
| 150 | [`150-itertools-slicing.apl`](examples/150-itertools-slicing.apl) | تقطيع المكررات وتجميعها |
| 151 | [`151-functools-reduce.apl`](examples/151-functools-reduce.apl) | الاختزال بدوال العوامل |
| 152 | [`152-functools-cache.apl`](examples/152-functools-cache.apl) | التخزين المؤقت للدوال |
| 153 | [`153-operator-sorting.apl`](examples/153-operator-sorting.apl) | الترتيب بجالب العناصر |
| 154 | [`154-enum-states.apl`](examples/154-enum-states.apl) | حالات الطلب بالتعداد |
| 155 | [`155-dataclass-inventory.apl`](examples/155-dataclass-inventory.apl) | جرد المنتجات بفئات البيانات |
| 156 | [`156-sqlite-notes.apl`](examples/156-sqlite-notes.apl) | دفتر ملاحظات بقاعدة بيانات |
| 157 | [`157-sqlite-grades.apl`](examples/157-sqlite-grades.apl) | تقرير درجات باستعلامات تجميعية |
| 158 | [`158-sqlite-transactions.apl`](examples/158-sqlite-transactions.apl) | المعاملات والتراجع |
| 159 | [`159-hash-integrity.apl`](examples/159-hash-integrity.apl) | التحقق من سلامة الملفات |
| 160 | [`160-hash-pbkdf2.apl`](examples/160-hash-pbkdf2.apl) | اشتقاق مفاتيح كلمات السر |
| 161 | [`161-base64-codec.apl`](examples/161-base64-codec.apl) | الترميز وفكه بقاعدة 64 |
| 162 | [`162-secrets-tokens.apl`](examples/162-secrets-tokens.apl) | توليد الرموز الآمنة |
| 163 | [`163-uuid-generate.apl`](examples/163-uuid-generate.apl) | المعرفات الفريدة |
| 164 | [`164-hash-file.apl`](examples/164-hash-file.apl) | تجزئة ملف قبل وبعد النسخ |
| 165 | [`165-xml-parse.apl`](examples/165-xml-parse.apl) | قراءة بيانات من XML |
| 166 | [`166-xml-build.apl`](examples/166-xml-build.apl) | بناء مستند XML من الصفر |
| 167 | [`167-xml-modify.apl`](examples/167-xml-modify.apl) | تعديل مستند XML |
| 168 | [`168-archive-tar.apl`](examples/168-archive-tar.apl) | أرشيف TAR كامل |
| 169 | [`169-archive-compress.apl`](examples/169-archive-compress.apl) | ضغط النصوص بثلاث خوارزميات |
| 170 | [`170-archive-zip-info.apl`](examples/170-archive-zip-info.apl) | فحص أرشيف ZIP وإحصاءاته |
| 171 | [`171-asyncio-tasks.apl`](examples/171-asyncio-tasks.apl) | مهام غير متزامنة |
| 172 | [`172-asyncio-gather.apl`](examples/172-asyncio-gather.apl) | تشغيل مهام متوازية وتجميع نتائجها |
| 173 | [`173-threading-lock.apl`](examples/173-threading-lock.apl) | عداد مشترك بقفل بين الخيوط |
| 174 | [`174-threading-event.apl`](examples/174-threading-event.apl) | إشارة بين خيطين |
| 175 | [`175-subprocess-run.apl`](examples/175-subprocess-run.apl) | تشغيل أوامر النظام |
| 176 | [`176-logging-levels.apl`](examples/176-logging-levels.apl) | تسجيل الأحداث بمستويات |
| 177 | [`177-match-case.apl`](examples/177-match-case.apl) | التطابق بالحالات (match/case) |
| 178 | [`178-decorators-property.apl`](examples/178-decorators-property.apl) | الخواص المحسوبة والمحددات |
| 179 | [`179-context-manager.apl`](examples/179-context-manager.apl) | مدير السياق مع الملفات |
| 180 | [`180-generator-pipeline.apl`](examples/180-generator-pipeline.apl) | خط معالجة متسلسل |
| 181 | [`181-inheritance.apl`](examples/181-inheritance.apl) | الوراثة وتعدد الأشكال |
| 182 | [`182-error-handling.apl`](examples/182-error-handling.apl) | معالجة الأخطاء |
| 183 | [`183-lambda-hof.apl`](examples/183-lambda-hof.apl) | الدوال المجردة ودوال الرتبة العليا |
| 184 | [`184-comprehensions.apl`](examples/184-comprehensions.apl) | التوليدات الشاملة المتقدمة |
| 185 | [`185-bubble-sort.apl`](examples/185-bubble-sort.apl) | الترتيب الفقاعي |
| 186 | [`186-merge-sort.apl`](examples/186-merge-sort.apl) | ترتيب الدمج |
| 187 | [`187-quick-sort.apl`](examples/187-quick-sort.apl) | الترتيب السريع |
| 188 | [`188-binary-search.apl`](examples/188-binary-search.apl) | البحث الثنائي بالعودية |
| 189 | [`189-balanced-brackets.apl`](examples/189-balanced-brackets.apl) | فحص توازن الأقواس |
| 190 | [`190-two-sum.apl`](examples/190-two-sum.apl) | مجموع العددين |
| 191 | [`191-anagrams.apl`](examples/191-anagrams.apl) | كشف الجناس الناقص |
| 192 | [`192-collatz.apl`](examples/192-collatz.apl) | متتالية كولاتز |
| 193 | [`193-fizzbuzz.apl`](examples/193-fizzbuzz.apl) | فيزباز |
| 194 | [`194-sieve-primes.apl`](examples/194-sieve-primes.apl) | غربال إراتوستينس |
| 195 | [`195-matrix-multiply.apl`](examples/195-matrix-multiply.apl) | ضرب المصفوفات |
| 196 | [`196-number-to-words.apl`](examples/196-number-to-words.apl) | تحويل الأرقام إلى كلمات عربية |
| 197 | [`197-temperature-stats.apl`](examples/197-temperature-stats.apl) | إحصاءات درجات الحرارة |
| 198 | [`198-todo-json.apl`](examples/198-todo-json.apl) | قائمة مهام محفوظة في ملف JSON |
| 199 | [`199-banking-oop.apl`](examples/199-banking-oop.apl) | نظام بنكي بسيط بالكائنات |
| 200 | [`200-final-showcase-2.apl`](examples/200-final-showcase-2.apl) | لوحة نتائج الطلاب |
| 201 | [`201-insertion-sort.apl`](examples/201-insertion-sort.apl) | الترتيب بالإدراج |
| 202 | [`202-selection-sort.apl`](examples/202-selection-sort.apl) | ترتيب الاختيار |
| 203 | [`203-counting-sort.apl`](examples/203-counting-sort.apl) | الترتيب بالعد |
| 204 | [`204-radix-sort.apl`](examples/204-radix-sort.apl) | الترتيب الجذري |
| 205 | [`205-heap-sort.apl`](examples/205-heap-sort.apl) | ترتيب الكومة |
| 206 | [`206-linear-search.apl`](examples/206-linear-search.apl) | البحث الخطي وكل المواضع |
| 207 | [`207-jump-search.apl`](examples/207-jump-search.apl) | البحث بالقفز |
| 208 | [`208-fibonacci-memo.apl`](examples/208-fibonacci-memo.apl) | فيبوناتشي بالتخزين |
| 209 | [`209-climbing-stairs.apl`](examples/209-climbing-stairs.apl) | طرق صعود السلم (برمجة ديناميكية) |
| 210 | [`210-coin-change.apl`](examples/210-coin-change.apl) | أقل عدد عملات (برمجة ديناميكية) |
| 211 | [`211-stack-class.apl`](examples/211-stack-class.apl) | المكدس كصنف |
| 212 | [`212-queue-class.apl`](examples/212-queue-class.apl) | الطابور كصنف |
| 213 | [`213-linked-list.apl`](examples/213-linked-list.apl) | القائمة المترابطة |
| 214 | [`214-binary-tree.apl`](examples/214-binary-tree.apl) | الشجرة الثنائية وجولاتها |
| 215 | [`215-bst.apl`](examples/215-bst.apl) | شجرة البحث الثنائية |
| 216 | [`216-trie.apl`](examples/216-trie.apl) | شجرة البادئات (Trie) |
| 217 | [`217-graph-bfs.apl`](examples/217-graph-bfs.apl) | المسح بالعرض للرسم البياني |
| 218 | [`218-graph-dfs.apl`](examples/218-graph-dfs.apl) | المسح بالعمق وإيجاد مسار |
| 219 | [`219-priority-queue.apl`](examples/219-priority-queue.apl) | طابور الأولوية اليدوي |
| 220 | [`220-doubly-linked.apl`](examples/220-doubly-linked.apl) | القائمة المترابطة المزدوجة |
| 221 | [`221-caesar-cipher.apl`](examples/221-caesar-cipher.apl) | شيفرة قيصر |
| 222 | [`222-vigenere.apl`](examples/222-vigenere.apl) | شيفرة فيجنير |
| 223 | [`223-rot13.apl`](examples/223-rot13.apl) | ROT13 |
| 224 | [`224-morse.apl`](examples/224-morse.apl) | شيفرة مورس |
| 225 | [`225-run-length.apl`](examples/225-run-length.apl) | ضغط طول التكرار |
| 226 | [`226-pig-latin.apl`](examples/226-pig-latin.apl) | لغة الخنزير اللاتينية |
| 227 | [`227-leet-speak.apl`](examples/227-leet-speak.apl) | لغة الليت (1337) |
| 228 | [`228-acronym.apl`](examples/228-acronym.apl) | توليد الاختصارات |
| 229 | [`229-word-reverser.apl`](examples/229-word-reverser.apl) | عكس الكلمات والجمل |
| 230 | [`230-title-case.apl`](examples/230-title-case.apl) | تنسيق العناوين الإنجليزية |
| 231 | [`231-factory-pattern.apl`](examples/231-factory-pattern.apl) | نمط المصنع |
| 232 | [`232-singleton.apl`](examples/232-singleton.apl) | نمط المفرد |
| 233 | [`233-observer.apl`](examples/233-observer.apl) | نمط المراقب |
| 234 | [`234-strategy.apl`](examples/234-strategy.apl) | نمط الاستراتيجية |
| 235 | [`235-builder.apl`](examples/235-builder.apl) | نمط البنّاء |
| 236 | [`236-adapter.apl`](examples/236-adapter.apl) | نمط المحوّل |
| 237 | [`237-state-machine.apl`](examples/237-state-machine.apl) | آلة الحالات (إشارة مرور) |
| 238 | [`238-iterator-protocol.apl`](examples/238-iterator-protocol.apl) | مكرر مخصص (عداد تنازلي) |
| 239 | [`239-template-method.apl`](examples/239-template-method.apl) | نمط القالب |
| 240 | [`240-composite.apl`](examples/240-composite.apl) | نمط المركّب (نظام ملفات) |
| 241 | [`241-tic-tac-toe.apl`](examples/241-tic-tac-toe.apl) | لعبة إكس أو (منطق) |
| 242 | [`242-guess-number.apl`](examples/242-guess-number.apl) | تخمين الرقم (محاكاة آلية) |
| 243 | [`243-rock-paper-scissors.apl`](examples/243-rock-paper-scissors.apl) | حجر ورقة مقص |
| 244 | [`244-dice-stats.apl`](examples/244-dice-stats.apl) | إحصاءات رمي النرد |
| 245 | [`245-card-deck.apl`](examples/245-card-deck.apl) | مجموعة أوراق لعب |
| 246 | [`246-blackjack.apl`](examples/246-blackjack.apl) | بلاك جاك مبسط |
| 247 | [`247-slot-machine.apl`](examples/247-slot-machine.apl) | ماكينة الحظ |
| 248 | [`248-lottery.apl`](examples/248-lottery.apl) | محاكاة يانصيب |
| 249 | [`249-bingo-card.apl`](examples/249-bingo-card.apl) | بطاقة بنغو |
| 250 | [`250-hangman-logic.apl`](examples/250-hangman-logic.apl) | منطق لعبة الرجل المشنوق |
| 251 | [`251-bmi.apl`](examples/251-bmi.apl) | حاسبة كتلة الجسم |
| 252 | [`252-compound-interest.apl`](examples/252-compound-interest.apl) | الفائدة المركبة |
| 253 | [`253-loan-amortization.apl`](examples/253-loan-amortization.apl) | جدول سداد قرض |
| 254 | [`254-tip-split.apl`](examples/254-tip-split.apl) | تقسيم الالحساب والإكرامية |
| 255 | [`255-leap-years.apl`](examples/255-leap-years.apl) | السنوات الكبيسة |
| 256 | [`256-zeller-weekday.apl`](examples/256-zeller-weekday.apl) | يوم الأسبوع بمعادلة زيلر |
| 257 | [`257-savings-goal.apl`](examples/257-savings-goal.apl) | هدف الادخار |
| 258 | [`258-age-days.apl`](examples/258-age-days.apl) | العمر بالأيام |
| 259 | [`259-countdown.apl`](examples/259-countdown.apl) | عداد تنازلي لتاريخ |
| 260 | [`260-currency-static.apl`](examples/260-currency-static.apl) | محول عملات بأسعار ثابتة |
| 261 | [`261-math-quiz.apl`](examples/261-math-quiz.apl) | اختبار حساب آلي |
| 262 | [`262-password-strength.apl`](examples/262-password-strength.apl) | قياس قوة كلمة المرور |
| 263 | [`263-atm.apl`](examples/263-atm.apl) | صراف آلي مبسط |
| 264 | [`264-voting.apl`](examples/264-voting.apl) | نظام تصويت |
| 265 | [`265-library-books.apl`](examples/265-library-books.apl) | مكتبة كتب بسيطة |
| 266 | [`266-shopping-cart.apl`](examples/266-shopping-cart.apl) | سلة تسوق |
| 267 | [`267-expense-categories.apl`](examples/267-expense-categories.apl) | مصروفات بالفئات |
| 268 | [`268-grade-book.apl`](examples/268-grade-book.apl) | سجل درجات فصل |
| 269 | [`269-parking.apl`](examples/269-parking.apl) | موقف سيارات |
| 270 | [`270-flashcards.apl`](examples/270-flashcards.apl) | بطاقات مراجعة |
| 271 | [`271-kadane.apl`](examples/271-kadane.apl) | أكبر مجموع متتالي (كادان) |
| 272 | [`272-majority.apl`](examples/272-majority.apl) | العنصر الأغلبي (بوير-مور) |
| 273 | [`273-dutch-flag.apl`](examples/273-dutch-flag.apl) | مسألة العلم الهولندي |
| 274 | [`274-rotate-array.apl`](examples/274-rotate-array.apl) | تدوير المصفوفة |
| 275 | [`275-merge-intervals.apl`](examples/275-merge-intervals.apl) | دمج الفترات المتداخلة |
| 276 | [`276-product-except-self.apl`](examples/276-product-except-self.apl) | حاصل ضرب ما عدا الذات |
| 277 | [`277-lis.apl`](examples/277-lis.apl) | أطول متتالية متزايدة |
| 278 | [`278-lcs.apl`](examples/278-lcs.apl) | أطول متتالية مشتركة |
| 279 | [`279-edit-distance.apl`](examples/279-edit-distance.apl) | مسافة التحرير |
| 280 | [`280-knapsack.apl`](examples/280-knapsack.apl) | حقيبة الظهر 0/1 |
| 281 | [`281-subsets.apl`](examples/281-subsets.apl) | كل المجموعات الفرعية |
| 282 | [`282-permutations-manual.apl`](examples/282-permutations-manual.apl) | التبديلات يدويا |
| 283 | [`283-generate-parentheses.apl`](examples/283-generate-parentheses.apl) | توليد الأقواس المتوازنة |
| 284 | [`284-combination-sum.apl`](examples/284-combination-sum.apl) | مجموعات بمبلغ مستهدف |
| 285 | [`285-n-queens.apl`](examples/285-n-queens.apl) | ملكات الشطرنج (عد الحلول) |
| 286 | [`286-rat-maze.apl`](examples/286-rat-maze.apl) | فأر في متاهة |
| 287 | [`287-word-search.apl`](examples/287-word-search.apl) | البحث عن كلمة في شبكة |
| 288 | [`288-phone-letters.apl`](examples/288-phone-letters.apl) | حروف لوحة الهاتف |
| 289 | [`289-sudoku-mini.apl`](examples/289-sudoku-mini.apl) | سودوكو مصغر 4x4 |
| 290 | [`290-hanoi.apl`](examples/290-hanoi.apl) | أبراج هانوي |
| 291 | [`291-string-search-count.apl`](examples/291-string-search-count.apl) | عد تكرارات نموذج في نص |
| 292 | [`292-longest-palindrome-sub.apl`](examples/292-longest-palindrome-sub.apl) | أطول مقطع متناظر |
| 293 | [`293-roman-to-int.apl`](examples/293-roman-to-int.apl) | من أرقام رومانية إلى عشرية |
| 294 | [`294-int-to-roman.apl`](examples/294-int-to-roman.apl) | من أرقام عشرية إلى رومانية |
| 295 | [`295-longest-common-prefix.apl`](examples/295-longest-common-prefix.apl) | أطول مقدمة مشتركة |
| 296 | [`296-count-and-say.apl`](examples/296-count-and-say.apl) | عد وقل |
| 297 | [`297-excel-column.apl`](examples/297-excel-column.apl) | عنوان عمود إكسل |
| 298 | [`298-zigzag.apl`](examples/298-zigzag.apl) | تحويل متعرج |
| 299 | [`299-valid-palindrome2.apl`](examples/299-valid-palindrome2.apl) | متناظر بحذف حرف واحد |
| 300 | [`300-string-to-int.apl`](examples/300-string-to-int.apl) | تحويل نص إلى عدد (atoi) |
| 301 | [`301-armstrong.apl`](examples/301-armstrong.apl) | أعداد أرمسترونج |
| 302 | [`302-perfect-numbers.apl`](examples/302-perfect-numbers.apl) | الأعداد الكاملة |
| 303 | [`303-happy-number.apl`](examples/303-happy-number.apl) | الأعداد السعيدة |
| 304 | [`304-harshad.apl`](examples/304-harshad.apl) | أعداد هارشاد |
| 305 | [`305-palindrome-number.apl`](examples/305-palindrome-number.apl) | الأعداد المتناظرة |
| 306 | [`306-digital-root.apl`](examples/306-digital-root.apl) | الجذر الرقمي |
| 307 | [`307-factorial.apl`](examples/307-factorial.apl) | العاملي (مضروب العدد) |
| 308 | [`308-fast-power.apl`](examples/308-fast-power.apl) | القوة السريعة |
| 309 | [`309-prime-factors.apl`](examples/309-prime-factors.apl) | العوامل الأولية |
| 310 | [`310-totient.apl`](examples/310-totient.apl) | دالة أويلر (مؤشر القواسم المشتركة) |
| 311 | [`311-tribonacci.apl`](examples/311-tribonacci.apl) | متتالية تريبوناتشي |
| 312 | [`312-catalan.apl`](examples/312-catalan.apl) | أعداد كاتالان |
| 313 | [`313-pascal.apl`](examples/313-pascal.apl) | مثلث باسكال |
| 314 | [`314-look-and-say.apl`](examples/314-look-and-say.apl) | متتالية انظر وقل |
| 315 | [`315-arithmetic-sequence.apl`](examples/315-arithmetic-sequence.apl) | المتتالية الحسابية |
| 316 | [`316-geometric-sequence.apl`](examples/316-geometric-sequence.apl) | المتتالية الهندسية |
| 317 | [`317-divisors.apl`](examples/317-divisors.apl) | قواسم العدد |
| 318 | [`318-lcm-list.apl`](examples/318-lcm-list.apl) | المضاعف المشترك الأصغر لقائمة |
| 319 | [`319-modular-inverse.apl`](examples/319-modular-inverse.apl) | المعكوس الضربي التراكبي |
| 320 | [`320-sieve-count.apl`](examples/320-sieve-count.apl) | عد الأولية وقائمتها حتى ن |
| 321 | [`321-chunk-list.apl`](examples/321-chunk-list.apl) | تقسيم قائمة إلى قطع |
| 322 | [`322-flatten-nested.apl`](examples/322-flatten-nested.apl) | تسطيح قائمة متداخلة (عودي) |
| 323 | [`323-pairwise.apl`](examples/323-pairwise.apl) | أزواج متتالية |
| 324 | [`324-interleave.apl`](examples/324-interleave.apl) | تداخل قائمتين |
| 325 | [`325-sliding-window.apl`](examples/325-sliding-window.apl) | النافذة المنزلقة |
| 326 | [`326-dedupe-consecutive.apl`](examples/326-dedupe-consecutive.apl) | إزالة التكرار المتتالي |
| 327 | [`327-unique-preserve.apl`](examples/327-unique-preserve.apl) | فريد مع الحفاظ على الترتيب |
| 328 | [`328-zip-manual.apl`](examples/328-zip-manual.apl) | دمج قائمتين يدويا (zip) |
| 329 | [`329-group-parity.apl`](examples/329-group-parity.apl) | تجميع زوجي وفردي |
| 330 | [`330-running-total.apl`](examples/330-running-total.apl) | المجموع التراكمي |
| 331 | [`331-next-birthday.apl`](examples/331-next-birthday.apl) | العد التنازلي لعيد الميلاد |
| 332 | [`332-working-days.apl`](examples/332-working-days.apl) | أيام العمل بين تاريخين |
| 333 | [`333-day-of-year.apl`](examples/333-day-of-year.apl) | رقم اليوم في السنة |
| 334 | [`334-weeks-between.apl`](examples/334-weeks-between.apl) | أسابيع بين تاريخين |
| 335 | [`335-month-start-end.apl`](examples/335-month-start-end.apl) | أول وآخر يوم في الشهر |
| 336 | [`336-age-calculator.apl`](examples/336-age-calculator.apl) | حاسبة العمر الدقيقة |
| 337 | [`337-quarter.apl`](examples/337-quarter.apl) | الربع السنوي والفصل |
| 338 | [`338-first-weekdays.apl`](examples/338-first-weekdays.apl) | أول اثنين من كل شهر |
| 339 | [`339-days-until-weekend.apl`](examples/339-days-until-weekend.apl) | كم باقي على العطلة |
| 340 | [`340-date-list.apl`](examples/340-date-list.apl) | قائمة تواريخ شهر |
| 341 | [`341-contacts-json.apl`](examples/341-contacts-json.apl) | دليل جهات اتصال بملف JSON |
| 342 | [`342-notes-tags.apl`](examples/342-notes-tags.apl) | ملاحظات بوسوم |
| 343 | [`343-inventory.apl`](examples/343-inventory.apl) | مخزون منتجات |
| 344 | [`344-log-analyzer.apl`](examples/344-log-analyzer.apl) | محلل سجلات |
| 345 | [`345-config-editor.apl`](examples/345-config-editor.apl) | محرر إعدادات بسيط |
| 346 | [`346-duplicate-finder.apl`](examples/346-duplicate-finder.apl) | كاشف المحتوى المكرر |
| 347 | [`347-backup-names.apl`](examples/347-backup-names.apl) | مولد أسماء نسخ احتياطية |
| 348 | [`348-csv-manual.apl`](examples/348-csv-manual.apl) | قراءة CSV يدويا |
| 349 | [`349-word-frequency-file.apl`](examples/349-word-frequency-file.apl) | تكرار كلمات ملف |
| 350 | [`350-mini-database.apl`](examples/350-mini-database.apl) | قاعدة بيانات JSON مصغرة |
| 351 | [`351-vector2d.apl`](examples/351-vector2d.apl) | متجه ثنائي الأبعاد |
| 352 | [`352-complex-manual.apl`](examples/352-complex-manual.apl) | أعداد مركبة يدويا |
| 353 | [`353-matrix-class.apl`](examples/353-matrix-class.apl) | صنف مصفوفة |
| 354 | [`354-rational.apl`](examples/354-rational.apl) | كسر اعتيادي يدوي |
| 355 | [`355-employee-payroll.apl`](examples/355-employee-payroll.apl) | رواتب الموظفين |
| 356 | [`356-shapes-area.apl`](examples/356-shapes-area.apl) | مساحات الأشكال |
| 357 | [`357-bank-accounts.apl`](examples/357-bank-accounts.apl) | حسابات بنكية متعددة |
| 358 | [`358-school.apl`](examples/358-school.apl) | مدرسة وطلاب ومواد |
| 359 | [`359-animals-farm.apl`](examples/359-animals-farm.apl) | مزرعة حيوانات |
| 360 | [`360-temperature-class.apl`](examples/360-temperature-class.apl) | صنف درجة حرارة |
| 361 | [`361-recursion-basics.apl`](examples/361-recursion-basics.apl) | أساسيات العودية |
| 362 | [`362-gcd-euclid.apl`](examples/362-gcd-euclid.apl) | القاسم المشترك بإقليدس العودي |
| 363 | [`363-reverse-string-rec.apl`](examples/363-reverse-string-rec.apl) | عكس نص بالعودية |
| 364 | [`364-palindrome-rec.apl`](examples/364-palindrome-rec.apl) | فحص التناظر بالعودية |
| 365 | [`365-sum-digits-rec.apl`](examples/365-sum-digits-rec.apl) | مجموع الأرقام بالعودية |
| 366 | [`366-binary-rec.apl`](examples/366-binary-rec.apl) | التحويل لثنائي بالعودية |
| 367 | [`367-flatten-rec.apl`](examples/367-flatten-rec.apl) | عد عناصر متداخلة بالعودية |
| 368 | [`368-power-rec.apl`](examples/368-power-rec.apl) | القوة بالعودية |
| 369 | [`369-tree-sum.apl`](examples/369-tree-sum.apl) | مجموع شجرة بالعودية |
| 370 | [`370-fib-tree-count.apl`](examples/370-fib-tree-count.apl) | عد استدعاءات فيبوناتشي |
| 371 | [`371-async-timeout.apl`](examples/371-async-timeout.apl) | مهلة على مهمة غير متزامنة |
| 372 | [`372-async-tasks-list.apl`](examples/372-async-tasks-list.apl) | قائمة مهام بأسماء |
| 373 | [`373-async-counter.apl`](examples/373-async-counter.apl) | عداد متزامن مشترك |
| 374 | [`374-async-pipeline.apl`](examples/374-async-pipeline.apl) | خط إنتاج واستهلاك مبسط |
| 375 | [`375-thread-semaphore.apl`](examples/375-thread-semaphore.apl) | إشارة حد التزامن بين الخيوط |
| 376 | [`376-thread-timer.apl`](examples/376-thread-timer.apl) | مؤقت خيط |
| 377 | [`377-thread-pool-manual.apl`](examples/377-thread-pool-manual.apl) | مجمع خيوط يدوي |
| 378 | [`378-thread-name-id.apl`](examples/378-thread-name-id.apl) | أسماء الخيوط |
| 379 | [`379-async-gather-mixed.apl`](examples/379-async-gather-mixed.apl) | تجميع نتائج متنوعة |
| 380 | [`380-async-retry.apl`](examples/380-async-retry.apl) | إعادة المحاولة غير المتزامنة |
| 381 | [`381-validate-emails.apl`](examples/381-validate-emails.apl) | التحقق من قائمة بريدات |
| 382 | [`382-extract-numbers.apl`](examples/382-extract-numbers.apl) | استخراج الأرقام والعمليات |
| 383 | [`383-parse-dates.apl`](examples/383-parse-dates.apl) | استخراج التواريخ من نص |
| 384 | [`384-egypt-phones.apl`](examples/384-egypt-phones.apl) | أرقام الهواتف المصرية |
| 385 | [`385-log-parser.apl`](examples/385-log-parser.apl) | محلل سجل بالأنماط |
| 386 | [`386-strip-html.apl`](examples/386-strip-html.apl) | إزالة وسوم HTML |
| 387 | [`387-camel-snake.apl`](examples/387-camel-snake.apl) | تحويل camelCase إلى snake_case |
| 388 | [`388-markdown-headings.apl`](examples/388-markdown-headings.apl) | فهرس عناوين ماركداون |
| 389 | [`389-find-arabic-numbers.apl`](examples/389-find-arabic-numbers.apl) | الأرقام العربية المشرقية في نص |
| 390 | [`390-password-regex.apl`](examples/390-password-regex.apl) | تحقق كلمة المرور بالأنماط |
| 391 | [`391-descriptive-stats.apl`](examples/391-descriptive-stats.apl) | إحصاءات وصفية |
| 392 | [`392-variance-std.apl`](examples/392-variance-std.apl) | التباين والانحراف المعياري |
| 393 | [`393-weighted-average.apl`](examples/393-weighted-average.apl) | المتوسط المرجح |
| 394 | [`394-moving-average.apl`](examples/394-moving-average.apl) | المتوسط المتحرك |
| 395 | [`395-percentiles.apl`](examples/395-percentiles.apl) | المئينيات |
| 396 | [`396-correlation.apl`](examples/396-correlation.apl) | معامل الارتباط |
| 397 | [`397-normalize-data.apl`](examples/397-normalize-data.apl) | تطبيع البيانات |
| 398 | [`398-frequency-table.apl`](examples/398-frequency-table.apl) | جدول التكرار |
| 399 | [`399-linear-regression.apl`](examples/399-linear-regression.apl) | الانحدار الخطي |
| 400 | [`400-chi-square.apl`](examples/400-chi-square.apl) | احتمالات بسيطة |
| 401 | [`401-hangman-game.apl`](examples/401-hangman-game.apl) | لعبة الجلاد |
| 402 | [`402-rps-tournament.apl`](examples/402-rps-tournament.apl) | بطولة حجر ورقة مقص |
| 403 | [`403-pig-dice.apl`](examples/403-pig-dice.apl) | لعبة نرد الخنزير |
| 404 | [`404-higher-lower.apl`](examples/404-higher-lower.apl) | أعلى أم أدنى |
| 405 | [`405-word-scramble.apl`](examples/405-word-scramble.apl) | خلط الكلمات |
| 406 | [`406-typing-test.apl`](examples/406-typing-test.apl) | اختبار سرعة الكتابة |
| 407 | [`407-simon-memory.apl`](examples/407-simon-memory.apl) | لعبة ذاكرة الألوان |
| 408 | [`408-battleship-mini.apl`](examples/408-battleship-mini.apl) | حرب السفن المصغرة |
| 409 | [`409-connect-four.apl`](examples/409-connect-four.apl) | منطق أربعة تربح |
| 410 | [`410-slot-machine.apl`](examples/410-slot-machine.apl) | ماكينة الحظ |
| 411 | [`411-base64-manual.apl`](examples/411-base64-manual.apl) | ترميز Base64 يدويا |
| 412 | [`412-url-encode.apl`](examples/412-url-encode.apl) | ترميز URL يدويا |
| 413 | [`413-unicode-explorer.apl`](examples/413-unicode-explorer.apl) | مستكشف يونيكود |
| 414 | [`414-morse-code.apl`](examples/414-morse-code.apl) | شيفرة مورس |
| 415 | [`415-run-length.apl`](examples/415-run-length.apl) | ترميز طول التسلسل |
| 416 | [`416-hex-binary.apl`](examples/416-hex-binary.apl) | تحويلات عددية |
| 417 | [`417-html-entities.apl`](examples/417-html-entities.apl) | كيانات HTML |
| 418 | [`418-checksum.apl`](examples/418-checksum.apl) | مجاميع تحقق |
| 419 | [`419-delta-encoding.apl`](examples/419-delta-encoding.apl) | ترميز الفروقات |
| 420 | [`420-hamming-distance.apl`](examples/420-hamming-distance.apl) | مسافة هامنج ورمز التصحيح |
| 421 | [`421-graph-coloring.apl`](examples/421-graph-coloring.apl) | تلوين الرسم البياني |
| 422 | [`422-graph-components.apl`](examples/422-graph-components.apl) | المكونات المتصلة |
| 423 | [`423-graph-bipartite.apl`](examples/423-graph-bipartite.apl) | فحص الرسم الثنائي |
| 424 | [`424-topo-sort.apl`](examples/424-topo-sort.apl) | الترتيب الطوبولوجي |
| 425 | [`425-kruskal-mst.apl`](examples/425-kruskal-mst.apl) | شجرة كروسكال الممتدة |
| 426 | [`426-bellman-ford.apl`](examples/426-bellman-ford.apl) | بيلمان فورد |
| 427 | [`427-floyd-warshall.apl`](examples/427-floyd-warshall.apl) | فلويد وارشال |
| 428 | [`428-trie-autocomplete.apl`](examples/428-trie-autocomplete.apl) | إكمال تلقائي بشجرة البادئات |
| 429 | [`429-union-find.apl`](examples/429-union-find.apl) | مجموعات منفصلة |
| 430 | [`430-graph-diameter.apl`](examples/430-graph-diameter.apl) | قطر الشجرة |
| 431 | [`431-table-formatter.apl`](examples/431-table-formatter.apl) | منسق جداول نصية |
| 432 | [`432-progress-bar.apl`](examples/432-progress-bar.apl) | شريط تقدم نصي |
| 433 | [`433-column-align.apl`](examples/433-column-align.apl) | محاذاة النصوص |
| 434 | [`434-number-format.apl`](examples/434-number-format.apl) | تنسيق الأرقام الكبيرة |
| 435 | [`435-duration-format.apl`](examples/435-duration-format.apl) | تنسيق المدد الزمنية |
| 436 | [`436-byte-format.apl`](examples/436-byte-format.apl) | تنسيق أحجام الملفات |
| 437 | [`437-sort-benchmark.apl`](examples/437-sort-benchmark.apl) | مقارنة خوارزميات الترتيب |
| 438 | [`438-text-wrap.apl`](examples/438-text-wrap.apl) | التفاف النص |
| 439 | [`439-pad-center.apl`](examples/439-pad-center.apl) | توسيط وتعبئة النصوص |
| 440 | [`440-markdown-table.apl`](examples/440-markdown-table.apl) | مولد جداول ماركداون |
| 441 | [`441-point-distance.apl`](examples/441-point-distance.apl) | المسافة بين نقطتين |
| 442 | [`442-polygon-area.apl`](examples/442-polygon-area.apl) | مساحة مضلع |
| 443 | [`443-circle-line.apl`](examples/443-circle-line.apl) | حسابات الدائرة والخط |
| 444 | [`444-triangle-check.apl`](examples/444-triangle-check.apl) | صحة المثلث ونوعه |
| 445 | [`445-angles.apl`](examples/445-angles.apl) | تحويل الزوايا |
| 446 | [`446-vector-ops.apl`](examples/446-vector-ops.apl) | عمليات المتجهات |
| 447 | [`447-quadratic.apl`](examples/447-quadratic.apl) | حل المعادلة التربيعية |
| 448 | [`448-matrix-determinant.apl`](examples/448-matrix-determinant.apl) | محدد المصفوفة |
| 449 | [`449-fractions-math.apl`](examples/449-fractions-math.apl) | كسور رياضية |
| 450 | [`450-complex-manual.apl`](examples/450-complex-manual.apl) | أعداد مركبة يدويا |
| 451 | [`451-arabic-lorem.apl`](examples/451-arabic-lorem.apl) | مولد نص عشوائي عربي |
| 452 | [`452-name-generator.apl`](examples/452-name-generator.apl) | مولد أسماء مستعارة |
| 453 | [`453-pronounceable-password.apl`](examples/453-pronounceable-password.apl) | كلمة مرور قابلة للنطق |
| 454 | [`454-acronym.apl`](examples/454-acronym.apl) | مولد الاختصارات |
| 455 | [`455-title-case.apl`](examples/455-title-case.apl) | تنسيق العناوين الإنجليزية |
| 456 | [`456-slug-generator.apl`](examples/456-slug-generator.apl) | مولد روابط Slug |
| 457 | [`457-hashtag-generator.apl`](examples/457-hashtag-generator.apl) | مولد هاشتاجات |
| 458 | [`458-markov-lite.apl`](examples/458-markov-lite.apl) | توليد جمل بسلاسل بسيطة |
| 459 | [`459-mad-libs.apl`](examples/459-mad-libs.apl) | قصة بقوالب |
| 460 | [`460-palindrome-maker.apl`](examples/460-palindrome-maker.apl) | مولد متناقضات لفظية |
| 461 | [`461-json-to-csv.apl`](examples/461-json-to-csv.apl) | تحويل JSON إلى CSV |
| 462 | [`462-csv-to-json.apl`](examples/462-csv-to-json.apl) | تحويل CSV إلى JSON |
| 463 | [`463-flatten-dict.apl`](examples/463-flatten-dict.apl) | تسطيح القواميس المتداخلة |
| 464 | [`464-list-to-tree.apl`](examples/464-list-to-tree.apl) | بناء شجرة من قائمة مسطحة |
| 465 | [`465-ini-parser.apl`](examples/465-ini-parser.apl) | قارئ ملفات INI |
| 466 | [`466-yaml-lite.apl`](examples/466-yaml-lite.apl) | قارئ YAML مبسط |
| 467 | [`467-env-parser.apl`](examples/467-env-parser.apl) | قارئ ملفات البيئة |
| 468 | [`468-xml-lite.apl`](examples/468-xml-lite.apl) | قارئ وسوم مبسط |
| 469 | [`469-html-table.apl`](examples/469-html-table.apl) | سجلات إلى جدول HTML |
| 470 | [`470-properties-convert.apl`](examples/470-properties-convert.apl) | تحويل خصائص إلى JSON |
| 471 | [`471-password-strength.apl`](examples/471-password-strength.apl) | مقياس قوة كلمة المرور |
| 472 | [`472-login-limiter.apl`](examples/472-login-limiter.apl) | محدد محاولات الدخول |
| 473 | [`473-pin-bruteforce.apl`](examples/473-pin-bruteforce.apl) | تجربة كسر رمز PIN |
| 474 | [`474-otp-generator.apl`](examples/474-otp-generator.apl) | مولد رموز تحقق |
| 475 | [`475-rbac.apl`](examples/475-rbac.apl) | التحكم بالصلاحيات |
| 476 | [`476-fnv-hash.apl`](examples/476-fnv-hash.apl) | دالة تجزية يدوية |
| 477 | [`477-salted-password.apl`](examples/477-salted-password.apl) | تجزئة كلمة مرور بملح |
| 478 | [`478-token-generator.apl`](examples/478-token-generator.apl) | مولد رموز الجلسات |
| 479 | [`479-firewall-sim.apl`](examples/479-firewall-sim.apl) | محاكي جدار ناري |
| 480 | [`480-log-anomaly.apl`](examples/480-log-anomaly.apl) | كاشف شذوذ السجلات |
| 481 | [`481-inventory-system.apl`](examples/481-inventory-system.apl) | نظام مخزون |
| 482 | [`482-library-system.apl`](examples/482-library-system.apl) | نظام مكتبة |
| 483 | [`483-grades-system.apl`](examples/483-grades-system.apl) | نظام درجات مدرسي |
| 484 | [`484-clinic-queue.apl`](examples/484-clinic-queue.apl) | طابور عيادة |
| 485 | [`485-parking-system.apl`](examples/485-parking-system.apl) | نظام مواقف سيارات |
| 486 | [`486-expense-splitter.apl`](examples/486-expense-splitter.apl) | مقسم المصاريف |
| 487 | [`487-survey-analyzer.apl`](examples/487-survey-analyzer.apl) | محلل استبيان |
| 488 | [`488-tournament-bracket.apl`](examples/488-tournament-bracket.apl) | شجرة بطولة |
| 489 | [`489-quiz-engine.apl`](examples/489-quiz-engine.apl) | محرك اختبارات من ملف |
| 490 | [`490-chat-analyzer.apl`](examples/490-chat-analyzer.apl) | محلل سجل محادثة |
| 491 | [`491-payroll-system.apl`](examples/491-payroll-system.apl) | نظام رواتب |
| 492 | [`492-bus-booking.apl`](examples/492-bus-booking.apl) | حجز مقاعد حافلة |
| 493 | [`493-recipe-manager.apl`](examples/493-recipe-manager.apl) | مدير وصفات الطعام |
| 494 | [`494-habit-tracker.apl`](examples/494-habit-tracker.apl) | متتبع العادات |
| 495 | [`495-flashcards.apl`](examples/495-flashcards.apl) | بطاقات استذكار |
| 496 | [`496-invoice-generator.apl`](examples/496-invoice-generator.apl) | مولد فواتير لملف |
| 497 | [`497-contact-search.apl`](examples/497-contact-search.apl) | محرك بحث جهات اتصال |
| 498 | [`498-blog-engine.apl`](examples/498-blog-engine.apl) | مولد مدونة ثابتة |
| 499 | [`499-event-planner.apl`](examples/499-event-planner.apl) | مخطط فعاليات |
| 500 | [`500-task-manager-suite.apl`](examples/500-task-manager-suite.apl) | نظام إدارة مهام متكامل |

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
| `python test_examples.py` | يشغّل كل الأمثلة الـ 500 ويفحص **مخرجاتها** مش بس عدم الخطأ |

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

**الإصدار:** APL v1.13 — 136,554 عنصراً عربياً — 63 مكتبة — 500 مثال

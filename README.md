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
- **مكتبات بالعربي** — 106 مكتبة مترجمة بالكامل (من `math` و `requests` إلى `datetime` و `decimal` و `xml` و `archive` و `net`)
- **3448 مثال جاهزاً** — في `examples/`، كلها مختبرة وتعمل
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

## المكتبات المتاحة (106 مكتبة)

| المكتبة | عدد العناصر | الوصف |
|---------|------------:|-------|
| `devtools` | 969 | أدوات المطوّر: فحص، تصحيح، قياس أداء، ترجمة (inspect / ast / dis / pdb / doctest / timeit / profile / tracemalloc) |
| `datafiles` | 2514 | البيانات والملفات: مسارات، ضغط، أرشيف، تسلسل، هياكل بيانات، XML، يونيكود (io / zipfile / tarfile / pickle / shelve / array / struct / xml.dom / xml.etree / unicodedata) |
| `syslib` | 3712 | النظام والتشغيل والتشخيص: منصة، إشارات، موارد، تسجيل، اختبارات، عمليات متعددة، ctypes، سياق (platform / signal / resource / logging / unittest / multiprocessing / concurrent.futures / ctypes / termios) |
| `weblibs` | 1431 | الويب والنصوص: بث متدفق، قوالب، ماركداون، تورنيدو، سطر الأوامر، تلوين الشيفرة (websockets / jinja2 / markdown / tornado / click / pygments) |
| `webserver` | 1925 | الخوادم والشبكات: خوادم ASGI/WSGI، عملاء HTTP غير متزامنين، HTTP/1.1 (starlette / uvicorn / httpx / httpcore / h11 / anyio) |
| `secauth` | 1730 | الأمان والمصادقة: تشفير وشهادات، قوالب معزولة، تحقق من المخططات، JWT (cryptography / jinja2 / jsonschema / jwt / cffi) |
| `textdata` | 1571 | النصوص والبيانات: مطابقة الأنماط، أصناف الخصائص، الصور، النماذج الأولية (pathspec / attrs / PIL / markdown / proto) |
| `utiltools` | 1401 | الأدوات المساعدة: الإصدارات والتواريخ، أشرطة التقدم، مراقبة العمليات (packaging / dateutil / tqdm / psutil / websockets) |
| `idlelib` | 720 | بيئة التطوير المدمجة: محرر، إكمال تلقائي، مصحح، إعدادات (idlelib) |
| `cdp_use` | 1164 | بروتوكول أدوات تطوير كروم CDP (cdp_use) |
| `acp` | 403 | بروتوكول العميل-الوكيل ACP (acp) |
| `aiohttp` | 1310 | عميل وخادم HTTP غير متزامنين (aiohttp) |
| `stdlib_ext` | 6607 | توسعة المكتبة القياسية (encodings / inspect / doctest / pdb / tracemalloc) |
| `numpy` | 2124 | الحساب العددي: مصفوفات، جبر خطي، تحويلات فورييه، عشوائيات (numpy) |
| `scipy` | 3913 | الحساب العلمي: تكامل، تحسين، استيفاء، إحصاء، مصفوفات متناثرة (scipy) |
| `telegram` | 3572 | بوتات تيليجرام: رسائل، محادثات، مستخدمون، لوحات مفاتيح (python-telegram-bot) |
| `redis` | 2106 | تخزين المفاتيح والقيم والجلسات والمهام الموزعة (redis-py) |
| `celery` | 2652 | طوابير المهام الموزعة والجدولة الزمنية (celery) |
| `numdeep` | 936 | الحساب العددي والعلمي العميق: مصفوفات وجبر خطي وإحصاء وتكامل (numpy / scipy) |
| `botdeep` | 925 | بوتات تيليجرام العميقة: كل أنواع الرسائل والتحديثات واللوحات (python-telegram-bot) |
| `taskdeep` | 3449 | المهام الموزعة العميقة: طوابير ورسائل وجدولة ونتائج (celery / kombu / billiard / amqp) |
| `storedeep` | 1501 | التخزين العميق: كل أوامر وأنواع redis (redis-py) |
| `pygdeep` | 9078 | تلوين الشيفرة العميق: كل المُحلّلات والمُنسّقات والأنماط (pygments) |
| `sympy_ext` | 20217 | توسعة حزمة sympy: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `plotly_ext` | 11595 | توسعة حزمة plotly: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `sqlalchemy_ext` | 8440 | توسعة حزمة sqlalchemy: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `twisted_ext` | 8144 | توسعة حزمة twisted: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `astropy_ext` | 6591 | توسعة حزمة astropy: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `statsmodels_ext` | 5180 | توسعة حزمة statsmodels: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `bokeh_ext` | 4955 | توسعة حزمة bokeh: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `sphinx_ext` | 4645 | توسعة حزمة sphinx: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `nltk_ext` | 4603 | توسعة حزمة nltk: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `openpyxl_ext` | 4404 | توسعة حزمة openpyxl: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `pandas_ext` | 4312 | توسعة حزمة pandas: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `crypto_ext` | 740 | توسعة حزمة Crypto: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `matplotlib_ext` | 4035 | توسعة حزمة matplotlib: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `docutils_ext` | 3520 | توسعة حزمة docutils: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `cv2_ext` | 3298 | توسعة حزمة cv2: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى |
| `pkgs_ext1` | 20830 | حزم متنوعة موسّعة (selenium / dask / xarray / pyarrow / sklearn / gevent / cdp_use / mpmath / networkx / botocore / jedi / aiohttp / telegram / markdown_it) |
| `pkgs_ext2` | 19295 | حزم متنوعة موسّعة (scrapy / prompt_toolkit / lxml / hypothesis / peewee / arrow / alembic / rich / trio / paramiko / h5py / cryptography / pyasn1 / skimage / yaml / seaborn / pyparsing / bs4 / shapely / babel / redis / pendulum / mako / nacl / typer / google / PIL / kombu / marshmallow / requests / sqlparse / celery / packaging / six / httpx / jinja2 / acp / regex / uvicorn / websockets / markdown / tornado / anyio / httplib2 / pygments / cffi / click / fastapi / httpcore / googleapiclient / tqdm / starlette / dateutil / pydantic / attr / jsonschema / multidict / numpy / scipy) |
| `webdeep` | 1778 | الويب العميق: أطر وخوادم وبروتوكولات (fastapi / starlette / tornado / websockets) |
| `datadeep` | 2435 | النماذج والتحقق العميق: مخططات وأنواع وتحقق (pydantic / jsonschema) |
| `mediadeep` | 3406 | الصور والنصوص العميقة: صور وماركداون وقوالب وسطر أوامر (PIL / markdown / jinja2) |
| `secdeep` | 2546 | الأمان وسحابة جوجل العميقة: تشفير وتوكنات وواجهات API (cryptography / google) |
| `utildeep` | 478 | الأدوات العميقة: تواريخ ومناطق ومراقبة وحزم مساعدة (dateutil / pytz / psutil) |
| `stdfull` | 4326 | المكتبة القياسية الشاملة: كل ما تبقى من وحدات Python القياسية |
| `web` | 2640 | الويب والبريد: عناوين، HTTP، بريد، صناديق، كوكيز، HTML، WSGI، XML-RPC (http / urllib / email / mailbox / html / wsgiref / xmlrpc) |
| `net` | 879 | الشبكة: socket و ssl و http و email و SMTP/IMAP/FTP |
| `fastapi` | 531 | إطار عمل ويب حديث |
| `requests` | 185 | HTTP Client كامل |
| `advanced` | 114 | ميزات متقدمة (decorators, metaclasses, typing) |
| `asyncio` | 101 | برمجة غير متزامنة |
| `argparse` | 106 | تحليل وسائط سطر الأوامر |
| `xml` | 109 | قراءة وبناء وتعديل ملفات XML (ElementTree) |
| `archive` | 106 | أرشيف ZIP و TAR وضغط gzip / bz2 / xz |
| `logging` | 61 | تسجيل الأحداث |
| `unittest` | 81 | اختبارات الوحدة |
| `flask` | 78 | إطار عمل ويب |
| `subprocess` | 67 | أوامر النظام |
| `dataclasses` | 51 | فئات بيانات، تعدادات، ABC |
| `math` | 63 | مثلثات، لوغاريتمات، جذور، تقريب، هندسة |
| `pathlib` | 39 | التعامل مع المسارات ككائنات |
| `datetime` | 19 | التاريخ والوقت والتحويل بينهما |
| `configparser` | 32 | ملفات الإعدادات |
| `os` | 20 | ملفات، مجلدات، مسارات، فحص |
| `threading` | 19 | تعدد المهام |
| `operator` | 20 | المشغّلات كدوال (add, mul, itemgetter) |
| `time` | 18 | وقت، تاريخ، تأخير، تنسيق |
| `re` | 24 | تعابير نمطية، بحث، استبدال، تقسيم |
| `sqlite3` | 20 | قاعدة بيانات محلية |
| `decimal` | 21 | الحساب العشري الدقيق (بدون أخطاء تقريب) |
| `random` | 20 | أرقام عشوائية، توزيعات، خلط |
| `itertools` | 12 | أدوات تكرار، توافيق، تباديل |
| `statistics` | 15 | متوسط، وسيط، منوال، تباين، انحراف معياري |
| `csv` | 12 | ملفات بيانات |
| `uuid` | 10 | المعرفات الفريدة (UUID) |
| `urllib` | 1 | تحليل وبناء الروابط وترميزها |
| `shutil` | 8 | نسخ ونقل وحذف الملفات والمجلدات |
| `base64` | 11 | الترميز وفك الترميز |
| `json` | 5 | قراءة وكتابة JSON |
| `string` | 10 | مجموعات الأحرف والرموز الثابتة |
| `collections` | 3 | Counter, defaultdict, deque |
| `textwrap` | 5 | تنسيق النصوص ولفّها |
| `functools` | 2 | أدوات الدوال (partial, cache, wraps) |
| `fractions` | 6 | الكسور الرياضية الدقيقة |
| `secrets` | 7 | توليد قيم عشوائية آمنة تشفيرياً |
| `zoneinfo` | 6 | المناطق الزمنية (IANA) |
| `hashlib` | 4 | تجزئة وتشفير |
| `enum` | 7 | أنواع معدودة (Enums) — قيم مسمّاة بدل الأرقام السحرية |
| `getpass` | 2 | إدخال كلمات السر دون إظهارها |
| `pprint` | 2 | طباعة منسّقة للقواميس والقوائم |
| `more_itertools` | 188 | أدوات التكرار الإضافية من حزمة more_itertools |
| `humanize` | 25 | تحويل الأرقام والأزمنة والأحجام لصيغة مقروءة من حزمة humanize |
| `tenacity` | 72 | إعادة المحاولة بسياسات إيقاف وانتظار من حزمة tenacity |
| `cachetools` | 38 | ذواكر مؤقتة بسياسات إخلاء متعددة من حزمة cachetools |
| `sortedcontainers` | 70 | قوائم وقواميس ومجموعات مرتبة من حزمة sortedcontainers |
| `mypy` | 5859 | فاحص الأنواع الساكنة من حزمة mypy |
| `polars` | 1750 | إطارات البيانات السريعة من حزمة polars |
| `faker` | 2276 | توليد البيانات الوهمية من حزمة faker |
| `openai` | 5298 | واجهة أوبن أي البرمجية من حزمة openai |
| `black` | 365 | منسّق شيفرة بايثون من حزمة black |
| `spacy` | 2986 | معالجة اللغات الطبيعية من حزمة spacy |
| `textual` | 1290 | واجهات طرفية تفاعلية من حزمة textual |
| `xgboost` | 227 | التعزيز التدرجي للأشجار من حزمة xgboost |
| `lightgbm` | 148 | التعزيز التدرجي الخفيف من حزمة lightgbm |
| `optuna` | 113 | تحسين المعلمات الفائقة من حزمة optuna |

**الإجمالي: 231,743 عنصراً في 106 مكتبة** (231,728 مفتاحاً فريداً بعد إزالة التكرار).

تشمل العناصر: الدوال، خصائص الكائنات، دوال الكائن المتسلسلة، الثوابت، والمعاملات العربية.
إضافة إلى 231 عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط، دوال مضمّنة)
في `core/apl_runner/patterns.py`، فيصبح عدد العناصر العربية الفريدة في اللغة **231,959 عنصراً**.

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

## الأمثلة الجاهزة (3448 مثال)

مجلد `examples/` يحتوي على **3448 برنامج حقيقياً** مكتوباً بالكامل بالعربي، وجميعها مختبرة وتعمل بلا أخطاء.

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
| 501 | [`501-numdeep.apl`](examples/501-numdeep.apl) | الحساب العلمي العميق (numdeep/numpy) |
| 502 | [`502-botdeep.apl`](examples/502-botdeep.apl) | بوتات تيليجرام العميقة (botdeep/telegram) |
| 503 | [`503-taskdeep.apl`](examples/503-taskdeep.apl) | المهام الموزعة العميقة (taskdeep/kombu) |
| 504 | [`504-storedeep.apl`](examples/504-storedeep.apl) | التخزين العميق (storedeep/redis) |
| 505 | [`505-pygdeep.apl`](examples/505-pygdeep.apl) | تلوين الشيفرة العميق (pygdeep/pygments) |
| 506 | [`506-webdeep.apl`](examples/506-webdeep.apl) | الويب العميق (webdeep/fastapi) |
| 507 | [`507-datadeep.apl`](examples/507-datadeep.apl) | النماذج والتحقق العميق (datadeep/pydantic) |
| 508 | [`508-mediadeep.apl`](examples/508-mediadeep.apl) | الصور والنصوص العميقة (mediadeep/PIL) |
| 509 | [`509-secdeep.apl`](examples/509-secdeep.apl) | الأمان العميق (secdeep/cryptography) |
| 510 | [`510-utildeep.apl`](examples/510-utildeep.apl) | الأدوات العميقة (utildeep/dateutil) |
| 511 | [`511-stdfull.apl`](examples/511-stdfull.apl) | المكتبة القياسية الشاملة (stdfull) |
| 512 | [`512-dijkstra.apl`](examples/512-dijkstra.apl) | خوارزمية ديكسترا لأقصر مسار في رسم موزون |
| 513 | [`513-kmp-search.apl`](examples/513-kmp-search.apl) | بحث كنوث-موريس-برات عن نمط في نص |
| 514 | [`514-shell-sort.apl`](examples/514-shell-sort.apl) | فرز شل بفجوات متناقصة |
| 515 | [`515-bucket-sort.apl`](examples/515-bucket-sort.apl) | فرز الحاويات لأعداد كسرية |
| 516 | [`516-interpolation-search.apl`](examples/516-interpolation-search.apl) | بحث بالاستكمال في قائمة متجانسة |
| 517 | [`517-ternary-search.apl`](examples/517-ternary-search.apl) | بحث ثلاثي في قائمة مفرزة |
| 518 | [`518-segment-tree.apl`](examples/518-segment-tree.apl) | شجرة المقاطع لمجاميع المجالات مع تحديث |
| 519 | [`519-fenwick-tree.apl`](examples/519-fenwick-tree.apl) | شجرة فينويك للمجاميع البادئة |
| 520 | [`520-bloom-filter.apl`](examples/520-bloom-filter.apl) | مرشح بلوم للعضوية التقريبية |
| 521 | [`521-chinese-remainder.apl`](examples/521-chinese-remainder.apl) | مبرهنة الباقي الصينية |
| 522 | [`522-fib-doubling.apl`](examples/522-fib-doubling.apl) | فيبوناتشي بالمضاعفة السريعة O(log n) |
| 523 | [`523-house-robber.apl`](examples/523-house-robber.apl) | لص المنازل (برمجة ديناميكية) |
| 524 | [`524-word-break.apl`](examples/524-word-break.apl) | تقطيع نص إلى كلمات قاموس (برمجة ديناميكية) |
| 525 | [`525-flood-fill-islands.apl`](examples/525-flood-fill-islands.apl) | عدّ الجزر بملء غامر على شبكة |
| 526 | [`526-line-diff.apl`](examples/526-line-diff.apl) | مقارنة نصين سطرياً بأطول تتابع مشترك |
| 527 | [`527-token-bucket.apl`](examples/527-token-bucket.apl) | دلو الرموز لتحديد معدل الطلبات |
| 528 | [`528-luhn-check.apl`](examples/528-luhn-check.apl) | تحقق لون لأرقام البطاقات |
| 529 | [`529-isbn13-check.apl`](examples/529-isbn13-check.apl) | تحقق من ردمك ISBN-13 |
| 530 | [`530-hijri-convert.apl`](examples/530-hijri-convert.apl) | تحويل ميلادي إلى هجري (الخوارزمية الكويتية) |
| 531 | [`531-arabic-indic-digits.apl`](examples/531-arabic-indic-digits.apl) | تحويل الأرقام بين العربية الغربية والمشرقية |
| 532 | [`532-egypt-national-id.apl`](examples/532-egypt-national-id.apl) | قراءة الرقم القومي المصري: الميلاد والمحافظة والنوع |
| 533 | [`533-zakat-calc.apl`](examples/533-zakat-calc.apl) | حساب زكاة المال فوق النصاب |
| 534 | [`534-electricity-bill.apl`](examples/534-electricity-bill.apl) | فاتورة كهرباء منزلية بشرائح تقريبية |
| 535 | [`535-vat-invoice.apl`](examples/535-vat-invoice.apl) | فاتورة بضريبة قيمة مضافة 14% |
| 536 | [`536-prim-mst.apl`](examples/536-prim-mst.apl) | شجرة بريم الممتدة الصغرى |
| 537 | [`537-a-star.apl`](examples/537-a-star.apl) | بحث A* على شبكة بعوائق مع إعادة بناء المسار |
| 538 | [`538-topological-lex.apl`](examples/538-topological-lex.apl) | ترتيب طوبولوجي بأصغر تسمية أولاً (خوارزمية كان) |
| 539 | [`539-rabin-karp.apl`](examples/539-rabin-karp.apl) | بحث رابين-كارب بالتجزئة الدوارة |
| 540 | [`540-z-algorithm.apl`](examples/540-z-algorithm.apl) | مصفوفة Z للبحث عن نمط |
| 541 | [`541-aho-corasick.apl`](examples/541-aho-corasick.apl) | أتمتة أهو-كوراسيك للبحث بعدة أنماط معاً |
| 542 | [`542-huffman-coding.apl`](examples/542-huffman-coding.apl) | ترميز هافمان: شجرة أكواد متغيرة الطول |
| 543 | [`543-burrows-wheeler.apl`](examples/543-burrows-wheeler.apl) | تحويل بوروز-ويلر وعكسه |
| 544 | [`544-word-ladder.apl`](examples/544-word-ladder.apl) | سلم الكلمات: أقصر تحويل بحرف واحد (BFS) |
| 545 | [`545-quickselect.apl`](examples/545-quickselect.apl) | اختيار سريع: ك-أصغر عنصر دون فرز كامل |
| 546 | [`546-sliding-window-max.apl`](examples/546-sliding-window-max.apl) | أقصى نافذة منزلقة بقائمة رتيبة |
| 547 | [`547-next-greater-element.apl`](examples/547-next-greater-element.apl) | العنصر الأكبر التالي بمكدس رتيب |
| 548 | [`548-largest-rectangle.apl`](examples/548-largest-rectangle.apl) | أكبر مستطيل في هيستوجرام بمكدس |
| 549 | [`549-trapping-rain-water.apl`](examples/549-trapping-rain-water.apl) | حصر مياه الأمطار بين الحواجز بمؤشرين |
| 550 | [`550-count-inversions.apl`](examples/550-count-inversions.apl) | عدّ المعكوسات بفرز الدمج |
| 551 | [`551-matrix-chain-dp.apl`](examples/551-matrix-chain-dp.apl) | ترتيب ضرب المصفوفات بأقل كلفة (برمجة ديناميكية) |
| 552 | [`552-egg-drop-dp.apl`](examples/552-egg-drop-dp.apl) | لغز البيض: أقل محاولات مضمونة (برمجة ديناميكية) |
| 553 | [`553-miller-rabin.apl`](examples/553-miller-rabin.apl) | اختبار ميلر-رابين للأولية بقواعد حتمية |
| 554 | [`554-segmented-sieve.apl`](examples/554-segmented-sieve.apl) | الغربال المقطعي: أوليات مجال بعيد |
| 555 | [`555-egyptian-fractions.apl`](examples/555-egyptian-fractions.apl) | الكسور المصرية: تمثيل كسر بمجموع كسور وحدة |
| 556 | [`556-newton-sqrt.apl`](examples/556-newton-sqrt.apl) | الجذر التربيعي بطريقة نيوتن-رافسون |
| 557 | [`557-josephus.apl`](examples/557-josephus.apl) | مسألة جوزيفوس: الناجي من حلقة الإقصاء |
| 558 | [`558-gaussian-elimination.apl`](examples/558-gaussian-elimination.apl) | حذف جاوس لحل نظام معادلات خطية |
| 559 | [`559-derangements.apl`](examples/559-derangements.apl) | التباديل المُخلّة: لا عنصر في موضعه |
| 560 | [`560-continued-fractions.apl`](examples/560-continued-fractions.apl) | الكسر المستمر لجذر غير نسبي |
| 561 | [`561-egypt-carriers.apl`](examples/561-egypt-carriers.apl) | معرفة شركة المحمول المصرية من مقدمة الرقم |
| 562 | [`562-currency-change.apl`](examples/562-currency-change.apl) | فك مبلغ إلى فئات الجنيه المصري (بالقروش) |
| 563 | [`563-gpa-calc.apl`](examples/563-gpa-calc.apl) | المعدل التراكمي بالساعات المعتمدة |
| 564 | [`564-iban-check.apl`](examples/564-iban-check.apl) | تحقق IBAN بمعيار mod-97 وتوليد رقم تحقق |
| 565 | [`565-base62-codec.apl`](examples/565-base62-codec.apl) | ترميز base62 لروابط قصيرة |
| 566 | [`566-circuit-breaker.apl`](examples/566-circuit-breaker.apl) | قاطع الدائرة: حماية من تكرار الفشل |
| 567 | [`567-semver-compare.apl`](examples/567-semver-compare.apl) | مقارنة إصدارات دلالية semver |
| 568 | [`568-template-mini.apl`](examples/568-template-mini.apl) | محرك قوالب مصغر بمتغيرات {{اسم}} |
| 569 | [`569-game-2048.apl`](examples/569-game-2048.apl) | منطق دمج 2048: انزلاق ودمج صف |
| 570 | [`570-wordle-feedback.apl`](examples/570-wordle-feedback.apl) | تقييم ووردل: أخضر/أصفر/رمادي بمرورين |
| 571 | [`571-mastermind-score.apl`](examples/571-mastermind-score.apl) | تقييم ماسترمايند: دقيق ولون فقط |
| 572 | [`572-median-stream.apl`](examples/572-median-stream.apl) | وسيط تدفق بكوميتين (أدنى وأقصى) |
| 573 | [`573-tarjan-scc.apl`](examples/573-tarjan-scc.apl) | خوارزمية تارجان للمكونات القوية في رسم موجه |
| 574 | [`574-maze-bfs.apl`](examples/574-maze-bfs.apl) | أقصر طريق في متاهة نصية مع جدران |
| 575 | [`575-suffix-array.apl`](examples/575-suffix-array.apl) | مصفوفة السوابق والبحث فيها |
| 576 | [`576-longest-common-substring.apl`](examples/576-longest-common-substring.apl) | أطول سلسلة فرعية مشتركة بين نصين |
| 577 | [`577-min-window-substring.apl`](examples/577-min-window-substring.apl) | أصغر نافذة تحوي كل أحرف نمط |
| 578 | [`578-group-anagrams.apl`](examples/578-group-anagrams.apl) | تجميع الكلمات المتناقضة الأحرف |
| 579 | [`579-jaro-winkler.apl`](examples/579-jaro-winkler.apl) | مقياس تشابه الأسماء جارو-وينكلر |
| 580 | [`580-k-way-merge.apl`](examples/580-k-way-merge.apl) | دمج عدة قوائم مرتبة بكومة |
| 581 | [`581-spiral-matrix.apl`](examples/581-spiral-matrix.apl) | قراءة مصفوفة بالترتيب الحلزوني |
| 582 | [`582-rotate-matrix.apl`](examples/582-rotate-matrix.apl) | تدوير مصفوفة 90 درجة |
| 583 | [`583-partition-subset-dp.apl`](examples/583-partition-subset-dp.apl) | تقسيم مجموعة إلى نصفين متساويين |
| 584 | [`584-unbounded-knapsack.apl`](examples/584-unbounded-knapsack.apl) | حقيبة الظهر غير المحدودة العناصر |
| 585 | [`585-bitmask-tsp.apl`](examples/585-bitmask-tsp.apl) | أقصر جولة تزور كل المدن بأقنعة البتات |
| 586 | [`586-sqrt-decomposition.apl`](examples/586-sqrt-decomposition.apl) | مجاميع المدى بتحليل الجذر التربيعي |
| 587 | [`587-circular-buffer.apl`](examples/587-circular-buffer.apl) | مخزن دائري يكتب فوق الأقدم |
| 588 | [`588-lfu-cache.apl`](examples/588-lfu-cache.apl) | ذاكرة مؤقتة تطرد الأقل استخداما |
| 589 | [`589-pollard-rho.apl`](examples/589-pollard-rho.apl) | تحليل عدد إلى عوامل بطريقة بولارد-رو |
| 590 | [`590-linear-diophantine.apl`](examples/590-linear-diophantine.apl) | حل معادلة ديوفانتية خطية بإقليدس الموسعة |
| 591 | [`591-stirling-digits.apl`](examples/591-stirling-digits.apl) | عدد أرقام المضروب باللوغاريتمات دون حسابه |
| 592 | [`592-matrix-exponentiation.apl`](examples/592-matrix-exponentiation.apl) | تريبوناتشي برفع مصفوفة لقوة |
| 593 | [`593-qibla-bearing.apl`](examples/593-qibla-bearing.apl) | اتجاه القبلة من القاهرة بحساب كروي |
| 594 | [`594-cairo-metro-fare.apl`](examples/594-cairo-metro-fare.apl) | تذكرة مترو القاهرة بعدد المحطات (تعريفة مبسطة) |
| 595 | [`595-egypt-income-tax.apl`](examples/595-egypt-income-tax.apl) | ضريبة الدخل المصرية بشرائح تصاعدية تقريبية |
| 596 | [`596-consistent-hashing.apl`](examples/596-consistent-hashing.apl) | توزيع مفاتيح مستقر على عقد متغيرة |
| 597 | [`597-bridges-articulation.apl`](examples/597-bridges-articulation.apl) | كشف الحواف والعقد الحرجة في رسم غير موجه |
| 598 | [`598-euler-path.apl`](examples/598-euler-path.apl) | مسار يعبر كل حافة مرة واحدة |
| 599 | [`599-manacher.apl`](examples/599-manacher.apl) | أطول سلسلة متناظرة بخوارزمية ماناكر |
| 600 | [`600-lz77-lite.apl`](examples/600-lz77-lite.apl) | ضغط LZ77 المبسط وفك الضغط |
| 601 | [`601-avl-tree.apl`](examples/601-avl-tree.apl) | شجرة بحث ذاتية الاتزان بالتدويرات |
| 602 | [`602-sparse-table.apl`](examples/602-sparse-table.apl) | أدنى مدى بزمن ثابت بعد تجهيز |
| 603 | [`603-xor-trie.apl`](examples/603-xor-trie.apl) | أقصى أو-حصري لزوج بشجرة بتات |
| 604 | [`604-knight-tour.apl`](examples/604-knight-tour.apl) | جولة الحصان بقاعدة وارنسدورف |
| 605 | [`605-minesweeper-reveal.apl`](examples/605-minesweeper-reveal.apl) | كشف متتال للخلايا الفارغة |
| 606 | [`606-minimax-ab.apl`](examples/606-minimax-ab.apl) | لعب مثالي في إكس-أو بتقليم ألفا-بيتا |
| 607 | [`607-othello-flips.apl`](examples/607-othello-flips.apl) | قانونية النقلة وقلب الأقراص |
| 608 | [`608-puzzle-15.apl`](examples/608-puzzle-15.apl) | هل وضع لغز الخمسة عشر قابل للحل |
| 609 | [`609-card-war.apl`](examples/609-card-war.apl) | محاكاة لعبة الحرب بالورق |
| 610 | [`610-snake-step.apl`](examples/610-snake-step.apl) | حركة ونمو واصطدام الثعبان |
| 611 | [`611-sliding-log-limiter.apl`](examples/611-sliding-log-limiter.apl) | تحديد المعدل بسجل طوابع منزلق |
| 612 | [`612-ttl-cache.apl`](examples/612-ttl-cache.apl) | ذاكرة مؤقتة بمدة صلاحية |
| 613 | [`613-undo-stack.apl`](examples/613-undo-stack.apl) | محرر بسجل تراجع وإعادة |
| 614 | [`614-event-bus.apl`](examples/614-event-bus.apl) | نشر واشتراك بين مكونات منفصلة |
| 615 | [`615-cron-parser.apl`](examples/615-cron-parser.apl) | موعد الرنة التالية لجدول كرون |
| 616 | [`616-prayer-times-lite.apl`](examples/616-prayer-times-lite.apl) | مواقيت الصلاة التقريبية للقاهرة بحساب شمسي |
| 617 | [`617-hijri-calendar-print.apl`](examples/617-hijri-calendar-print.apl) | طباعة شهر هجري كشبكة أسابيع |
| 618 | [`618-ramadan-countdown.apl`](examples/618-ramadan-countdown.apl) | أيام متبقية لرمضان بالتقويم الاصطلاحي |
| 619 | [`619-tafqeet.apl`](examples/619-tafqeet.apl) | تحويل المبلغ إلى كلمات عربية |
| 620 | [`620-skip-list.apl`](examples/620-skip-list.apl) | بحث سريع في قائمة مرتبة بمستويات |
| 621 | [`621-convex-hull-graham.apl`](examples/621-convex-hull-graham.apl) | أصغر مضلع محدب يحوي النقاط |
| 622 | [`622-closest-pair.apl`](examples/622-closest-pair.apl) | أقرب زوج نقاط بالفرز والفحص |
| 623 | [`623-point-in-polygon.apl`](examples/623-point-in-polygon.apl) | هل النقطة داخل المضلع بقذف شعاع |
| 624 | [`624-line-intersection.apl`](examples/624-line-intersection.apl) | تقاطع القطع المستقيمة باختبارات الاتجاه |
| 625 | [`625-karatsuba.apl`](examples/625-karatsuba.apl) | ضرب الأعداد الكبيرة بتقسيم أسرع |
| 626 | [`626-crc32.apl`](examples/626-crc32.apl) | مجموع CRC32 الاختباري بت بت |
| 627 | [`627-hamming-ecc.apl`](examples/627-hamming-ecc.apl) | شفرة هامنغ (7,4) لتصحيح خطأ أحادي البت |
| 628 | [`628-glob-match.apl`](examples/628-glob-match.apl) | مطابقة أنماط glob النجمة والاستفهام |
| 629 | [`629-regex-nfa-lite.apl`](examples/629-regex-nfa-lite.apl) | محرك نمطية مصغر بحرف ونقطة ونجمة |
| 630 | [`630-json-parser.apl`](examples/630-json-parser.apl) | محلل JSON مصغر من الصفر |
| 631 | [`631-bytecode-vm.apl`](examples/631-bytecode-vm.apl) | آلة افتراضية كومة مصغرة |
| 632 | [`632-allocator-first-fit.apl`](examples/632-allocator-first-fit.apl) | محاكي تخصيص ذاكرة بأول ملائم ودمج |
| 633 | [`633-merkle-tree.apl`](examples/633-merkle-tree.apl) | إثبات سلامة البيانات بشجرة تجزئة |
| 634 | [`634-leader-election-bully.apl`](examples/634-leader-election-bully.apl) | انتخاب قائد بخوارزمية التنمر |
| 635 | [`635-vector-clock.apl`](examples/635-vector-clock.apl) | ترتيب الأحداث الموزعة بالساعات المتجهة |
| 636 | [`636-banker-algorithm.apl`](examples/636-banker-algorithm.apl) | كشف الحالة الآمنة من الجمود |
| 637 | [`637-page-replacement.apl`](examples/637-page-replacement.apl) | إحلال الصفحات FIFO والأمثل |
| 638 | [`638-disk-scan.apl`](examples/638-disk-scan.apl) | جدولة القرص بخوارزمية المصعد |
| 639 | [`639-round-robin.apl`](examples/639-round-robin.apl) | جدولة المعالج بالتناوب الدائري |
| 640 | [`640-dining-philosophers.apl`](examples/640-dining-philosophers.apl) | تجنب الجمود بترتيب الموارد |
| 641 | [`641-faraid-lite.apl`](examples/641-faraid-lite.apl) | الأنصبة الشرعية الثابتة المبسطة |
| 642 | [`642-arabic-light-stemmer.apl`](examples/642-arabic-light-stemmer.apl) | تجذيع عربي خفيف بقص السوابق واللواحق |
| 643 | [`643-cairo-taxi-fare.apl`](examples/643-cairo-taxi-fare.apl) | عداد التاكسي الأبيض بالقاهرة (تقريبي) |
| 644 | [`644-electricity-bill-egypt.apl`](examples/644-electricity-bill-egypt.apl) | فاتورة كهرباء منزلية بشرائح (تقريبية) |
| 645 | [`645-b-tree-insert.apl`](examples/645-b-tree-insert.apl) | إدخال في شجرة ب مع انقسام العقد الممتلئة |
| 646 | [`646-treap.apl`](examples/646-treap.apl) | شجرة بحث متوازنة بأولويات كومة مشتقة |
| 647 | [`647-lca-binary-lifting.apl`](examples/647-lca-binary-lifting.apl) | أدنى سلف مشترك بجداول قوى اثنين |
| 648 | [`648-mo-algorithm.apl`](examples/648-mo-algorithm.apl) | إجابة استعلامات المدى بإعادة ترتيبها |
| 649 | [`649-meet-in-middle.apl`](examples/649-meet-in-middle.apl) | عد المجموعات الجزئية باللقاء في المنتصف |
| 650 | [`650-gray-code.apl`](examples/650-gray-code.apl) | تتابع ثنائي يختلف في بت واحد |
| 651 | [`651-bit-tricks.apl`](examples/651-bit-tricks.apl) | حيل البتات الشائعة بالإزاحات والأقنعة |
| 652 | [`652-reservoir-sampling.apl`](examples/652-reservoir-sampling.apl) | عينة عادلة ثابتة الحجم من تيار |
| 653 | [`653-weighted-random.apl`](examples/653-weighted-random.apl) | اختيار عشوائي باحتمال يتناسب مع الوزن |
| 654 | [`654-count-min-sketch.apl`](examples/654-count-min-sketch.apl) | تقدير تكرارات بذاكرة ثابتة |
| 655 | [`655-bresenham-line.apl`](examples/655-bresenham-line.apl) | رسم خط مستقيم على شبكة بلا فاصلة عائمة |
| 656 | [`656-iterative-deepening.apl`](examples/656-iterative-deepening.apl) | بحث يجد أضحل حل بذاكرة البحث العميق |
| 657 | [`657-suffix-automaton.apl`](examples/657-suffix-automaton.apl) | بنية مدمجة لكل النصوص الفرعية |
| 658 | [`658-damerau-levenshtein.apl`](examples/658-damerau-levenshtein.apl) | مسافة تحرير مع تبديل الحروف المتجاورة |
| 659 | [`659-arabic-number-parse.apl`](examples/659-arabic-number-parse.apl) | قراءة الأرقام المشرقية ٠١٢٣ كأعداد |
| 660 | [`660-arabic-sort-collation.apl`](examples/660-arabic-sort-collation.apl) | ترتيب الأسماء بالهجائية العربية |
| 661 | [`661-coptic-calendar.apl`](examples/661-coptic-calendar.apl) | تحويل التواريخ من وإلى التقويم القبطي |
| 662 | [`662-kalman-lite.apl`](examples/662-kalman-lite.apl) | دمج قياسات مزعجة في تقدير مستقر |
| 663 | [`663-pid-controller.apl`](examples/663-pid-controller.apl) | متحكم نسبي تكاملي تفاضلي على نظام محاكى |
| 664 | [`664-shamir-secret.apl`](examples/664-shamir-secret.apl) | تقسيم سر على حصص لا تكفي بعضها وحدها |
| 665 | [`665-bidirectional-bfs.apl`](examples/665-bidirectional-bfs.apl) | أقصر طريق بجبهتين متعاكستين |
| 666 | [`666-zero-one-bfs.apl`](examples/666-zero-one-bfs.apl) | أقصر تكلفة بأوزان صفر وواحد |
| 667 | [`667-mcts-lite.apl`](examples/667-mcts-lite.apl) | معادلة الاختيار التي تقود بحث مونت كارلو |
| 668 | [`668-simulated-annealing-tsp.apl`](examples/668-simulated-annealing-tsp.apl) | تحسين جولة مندوب السفر بالتلدين المحاكى |
| 669 | [`669-max-flow-ford-fulkerson.apl`](examples/669-max-flow-ford-fulkerson.apl) | أقصى تدفق في شبكة بمسارات معززة |
| 670 | [`670-hungarian-lite.apl`](examples/670-hungarian-lite.apl) | إسناد عامل لمهمة بأقل كلفة إجمالية |
| 671 | [`671-hyperloglog-lite.apl`](examples/671-hyperloglog-lite.apl) | تقدير عدد العناصر المميزة بذاكرة ثابتة |
| 672 | [`672-lz78.apl`](examples/672-lz78.apl) | ضغط وفك بقاموس عبارات متنام |
| 673 | [`673-arithmetic-coding-lite.apl`](examples/673-arithmetic-coding-lite.apl) | ترميز رسالة ككسر في مدى احتمالي |
| 674 | [`674-rsa-toy.apl`](examples/674-rsa-toy.apl) | توليد مفاتيح وتشفير RSA بأعداد صغيرة |
| 675 | [`675-diffie-hellman-toy.apl`](examples/675-diffie-hellman-toy.apl) | اشتقاق سر مشترك عبر قناة علنية |
| 676 | [`676-chacha-quarter-round.apl`](examples/676-chacha-quarter-round.apl) | العملية الأساسية في تشفير تشاتشا |
| 677 | [`677-easter-computus.apl`](examples/677-easter-computus.apl) | تاريخ عيد الفصح الغربي لأي سنة |
| 678 | [`678-hebrew-calendar-lite.apl`](examples/678-hebrew-calendar-lite.apl) | تحويل تقريبي من وإلى التقويم العبري |
| 679 | [`679-smith-waterman.apl`](examples/679-smith-waterman.apl) | أقوى تشابه جزئي بين تسلسلي DNA |
| 680 | [`680-moon-phase-lite.apl`](examples/680-moon-phase-lite.apl) | هل الليلة محاق أم بدر من التاريخ وحده |
| 681 | [`681-game-of-life.apl`](examples/681-game-of-life.apl) | مذبذب ونمط ساكن بقواعد كونواي |
| 682 | [`682-langton-ant.apl`](examples/682-langton-ant.apl) | فوضى تتحول إلى طريق سريع دوري |
| 683 | [`683-rule-110.apl`](examples/683-rule-110.apl) | أتمتة خلوية أولية كاملة حسابيا |
| 684 | [`684-sprague-grundy.apl`](examples/684-sprague-grundy.apl) | تحليل الألعاب المحايدة بأرقام غروندي |
| 685 | [`685-poker-hand-eval-lite.apl`](examples/685-poker-hand-eval-lite.apl) | تصنيف يد من خمس ورقات |
| 686 | [`686-fen-parse.apl`](examples/686-fen-parse.apl) | قراءة موقف شطرنج بترميز فورسيث-إدواردز |
| 687 | [`687-verhoeff-checksum.apl`](examples/687-verhoeff-checksum.apl) | رقم تحقق يكشف تبديل الخانات المتجاورة |
| 688 | [`688-brainfuck-interp.apl`](examples/688-brainfuck-interp.apl) | مفسر كامل للغة براين فك المصغرة |
| 689 | [`689-lisp-eval-lite.apl`](examples/689-lisp-eval-lite.apl) | حساب تعابير البادئة المتداخلة |
| 690 | [`690-toml-lite.apl`](examples/690-toml-lite.apl) | قراءة ملفات إعداد بصيغة TOML |
| 691 | [`691-ical-rrule-lite.apl`](examples/691-ical-rrule-lite.apl) | توليد مواعيد متكررة يوميا وأسبوعيا وشهريا |
| 692 | [`692-mandelbrot-ascii.apl`](examples/692-mandelbrot-ascii.apl) | رسم مجموعة ماندلبروت بالأحرف |
| 693 | [`693-perlin-noise-1d.apl`](examples/693-perlin-noise-1d.apl) | ضوضاء ناعمة بلا مولد عشوائي |
| 694 | [`694-bezier-curve.apl`](examples/694-bezier-curve.apl) | تقييم منحنيات بيزييه التربيعية والتكعيبية |
| 695 | [`695-catmull-rom.apl`](examples/695-catmull-rom.apl) | منحنى يمر بكل نقاط التحكم |
| 696 | [`696-shoelace-area.apl`](examples/696-shoelace-area.apl) | مساحة ومحيط مضلع من رؤوسه |
| 697 | [`697-circle-circle-intersection.apl`](examples/697-circle-circle-intersection.apl) | نقاط تلاقي دائرتين وحالاتها الخاصة |
| 698 | [`698-kmeans-1d.apl`](examples/698-kmeans-1d.apl) | تجميع نقاط على الخط في عنقودين |
| 699 | [`699-gradient-descent-1d.apl`](examples/699-gradient-descent-1d.apl) | إيجاد أدنى دالة تربيعية بالنزول |
| 700 | [`700-perceptron-lite.apl`](examples/700-perceptron-lite.apl) | أبسط عصبون يتعلم بوابة منطقية |
| 701 | [`701-julian-day-number.apl`](examples/701-julian-day-number.apl) | حسابات التواريخ بالأرقام المطلقة |
| 702 | [`702-wav-header-parse.apl`](examples/702-wav-header-parse.apl) | قراءة حقول ملف صوتي من بايتاته |
| 703 | [`703-bmp-ascii-render.apl`](examples/703-bmp-ascii-render.apl) | تحويل بكسلات نقطية إلى فن نصي |
| 704 | [`704-maze-wilson.apl`](examples/704-maze-wilson.apl) | متاهة مثالية بتوزيع منتظم |
| 705 | [`705-datalog-lite.apl`](examples/705-datalog-lite.apl) | استنتاج علاقات السلف بالإغلاق المتعدي |
| 706 | [`706-prolog-unify-lite.apl`](examples/706-prolog-unify-lite.apl) | مطابقة الحدود بالتوحيد |
| 707 | [`707-dpll-sat-lite.apl`](examples/707-dpll-sat-lite.apl) | إشباع صيغ منطقية بالتقسيم |
| 708 | [`708-expectimax-lite.apl`](examples/708-expectimax-lite.apl) | قرارات مثلى تحت عدم اليقين |
| 709 | [`709-pagerank-lite.apl`](examples/709-pagerank-lite.apl) | ترتيب صفحات ويب بأهميتها |
| 710 | [`710-astar-grid.apl`](examples/710-astar-grid.apl) | أقصر طريق حول العوائق |
| 711 | [`711-tf-idf-lite.apl`](examples/711-tf-idf-lite.apl) | أهم كلمات مستند ضمن مجموعة |
| 712 | [`712-tashkeel-strip.apl`](examples/712-tashkeel-strip.apl) | تنظيف النص العربي من الحركات |
| 713 | [`713-stopword-filter-ar.apl`](examples/713-stopword-filter-ar.apl) | حذف الكلمات الشائعة قبل البحث |
| 714 | [`714-sentence-split-ar.apl`](examples/714-sentence-split-ar.apl) | تقطيع النص إلى جمل بقواعد |
| 715 | [`715-soundex-en.apl`](examples/715-soundex-en.apl) | رمز صوتي للأسماء الإنجليزية |
| 716 | [`716-iso-week-date.apl`](examples/716-iso-week-date.apl) | سنة الأسبوع ورقمه ويومه |
| 717 | [`717-murmur-lite.apl`](examples/717-murmur-lite.apl) | هاش 32-بت غير تشفيري للسلاسل |
| 718 | [`718-pearson-hash.apl`](examples/718-pearson-hash.apl) | هاش 8-بت بجدول تبديل ثابت |
| 719 | [`719-adler32.apl`](examples/719-adler32.apl) | مجموع فحص سريع للبيانات |
| 720 | [`720-fletcher16.apl`](examples/720-fletcher16.apl) | كشف أخطاء بمجموعين متعاقبين |
| 721 | [`721-crc16-modbus.apl`](examples/721-crc16-modbus.apl) | فحص دوري لبروتوكول مودباس |
| 722 | [`722-base58-codec.apl`](examples/722-base58-codec.apl) | ترميز بيتكوين النصي وفكه |
| 723 | [`723-varint-protobuf.apl`](examples/723-varint-protobuf.apl) | أعداد صحيحة متغيرة الطول |
| 724 | [`724-zigzag-encoding.apl`](examples/724-zigzag-encoding.apl) | سالب وموجب بأعداد موجبة صغيرة |
| 725 | [`725-utf8-decode-manual.apl`](examples/725-utf8-decode-manual.apl) | قراءة حروف يونيكود من بايتاتها |
| 726 | [`726-utf16-surrogates.apl`](examples/726-utf16-surrogates.apl) | حروف فوق U+FFFF بوحدتين |
| 727 | [`727-punycode-lite.apl`](examples/727-punycode-lite.apl) | أسماء نطاقات دولية بأحرف ASCII |
| 728 | [`728-phone-t9.apl`](examples/728-phone-t9.apl) | كتابة نص بلوحة هاتف قديمة |
| 729 | [`729-braille-lite.apl`](examples/729-braille-lite.apl) | تحويل نص إلى خلايا برايل |
| 730 | [`730-resistor-color-code.apl`](examples/730-resistor-color-code.apl) | قراءة قيم مقاومة من ألوانها |
| 731 | [`731-dna-transcribe.apl`](examples/731-dna-transcribe.apl) | تحويل تسلسل جيني ومكمله العكسي |
| 732 | [`732-gc-content.apl`](examples/732-gc-content.apl) | قياس غنى قواعد DNA |
| 733 | [`733-fasta-parse.apl`](examples/733-fasta-parse.apl) | قراءة ملفات تسلسل جينية |
| 734 | [`734-protein-mass.apl`](examples/734-protein-mass.apl) | كتلة بروتين من أحماضه الأمينية |
| 735 | [`735-hebrew-numerals.apl`](examples/735-hebrew-numerals.apl) | كتابة الأعداد بالحروف العبرية |
| 736 | [`736-chinese-numerals.apl`](examples/736-chinese-numerals.apl) | كتابة الأعداد بالحروف الصينية |
| 737 | [`737-babylonian-numerals.apl`](examples/737-babylonian-numerals.apl) | النظام الستيني للأعداد |
| 738 | [`738-simpson-integrate.apl`](examples/738-simpson-integrate.apl) | تكامل عددي دقيق للدوال |
| 739 | [`739-horner-eval.apl`](examples/739-horner-eval.apl) | تقييم كثيرات الحدود ومشتقاتها |
| 740 | [`740-golomb-coding.apl`](examples/740-golomb-coding.apl) | ضغط الأعداد الصحيحة الموجبة |
| 741 | [`741-hmac-manual.apl`](examples/741-hmac-manual.apl) | بناء HMAC من تجزئة SHA-256 (RFC 2104) |
| 742 | [`742-hkdf-lite.apl`](examples/742-hkdf-lite.apl) | اشتقاق مفاتيح من مادة أولية (RFC 5869) |
| 743 | [`743-otp-hotp-lite.apl`](examples/743-otp-hotp-lite.apl) | رموز HOTP من مفتاح وعداد |
| 744 | [`744-aes-sbox-lite.apl`](examples/744-aes-sbox-lite.apl) | اشتقاق جدول S-Box رياضياً |
| 745 | [`745-xor-cipher-break.apl`](examples/745-xor-cipher-break.apl) | كسر تشفير XOR بتحليل التكرار |
| 746 | [`746-vigenere-break.apl`](examples/746-vigenere-break.apl) | كسر فيجنير بطول مفتاح معلوم |
| 747 | [`747-playfair-lite.apl`](examples/747-playfair-lite.apl) | تشفير ثنائي الحروف التاريخي |
| 748 | [`748-enigma-lite.apl`](examples/748-enigma-lite.apl) | محاكاة إنجما I التاريخية |
| 749 | [`749-rail-fence.apl`](examples/749-rail-fence.apl) | تبديل مواضع بقضبان متعرجة |
| 750 | [`750-greek-numerals.apl`](examples/750-greek-numerals.apl) | النظام الأيوني للأرقام |
| 751 | [`751-mayan-numerals.apl`](examples/751-mayan-numerals.apl) | النظام العشريني بالنقاط والأصابع |
| 752 | [`752-emoji-grapheme-split.apl`](examples/752-emoji-grapheme-split.apl) | تقسيم نص لوحدات مرئية صحيحة |
| 753 | [`753-arabic-reshaper-lite.apl`](examples/753-arabic-reshaper-lite.apl) | حروف عربية بأشكال العرض الأربعة |
| 754 | [`754-json-path-lite.apl`](examples/754-json-path-lite.apl) | استعلام $.a.b[0] عن بنى متداخلة |
| 755 | [`755-tokenizer-ar-lite.apl`](examples/755-tokenizer-ar-lite.apl) | كلمات وأرقام وعلامات من نص عربي |
| 756 | [`756-keyboard-dvorak-lite.apl`](examples/756-keyboard-dvorak-lite.apl) | تحويل QWERTY ودفوراك وكفاءتهما |
| 757 | [`757-quaternion-rotate.apl`](examples/757-quaternion-rotate.apl) | تدوير متجهات ثلاثية الأبعاد |
| 758 | [`758-sun-position-lite.apl`](examples/758-sun-position-lite.apl) | ارتفاع الشمس من اليوم وخط العرض |
| 759 | [`759-fastq-parse.apl`](examples/759-fastq-parse.apl) | تسلسلات مع درجات جودة |
| 760 | [`760-newick-parse.apl`](examples/760-newick-parse.apl) | أشجار تطور نصية |
| 761 | [`761-codon-table.apl`](examples/761-codon-table.apl) | ترجمة DNA إلى بروتين |
| 762 | [`762-upgma-tree.apl`](examples/762-upgma-tree.apl) | شجرة تطور من مصفوفة مسافات |
| 763 | [`763-boggle-solver.apl`](examples/763-boggle-solver.apl) | كلمات من شبكة حروف متجاورة |
| 764 | [`764-fft-butterfly-lite.apl`](examples/764-fft-butterfly-lite.apl) | تحويل فورييه السريع يدوياً |
| 765 | [`765-rc4-cipher.apl`](examples/765-rc4-cipher.apl) | تشفير تدفقي بجدول تبديل 256 بايت |
| 766 | [`766-tea-cipher.apl`](examples/766-tea-cipher.apl) | شبكة فيستل صغيرة بمفتاح 128-بت |
| 767 | [`767-affine-cipher.apl`](examples/767-affine-cipher.apl) | شفرة أحادية الأبجدية الخطية |
| 768 | [`768-hill-cipher.apl`](examples/768-hill-cipher.apl) | تشفير أزواج الحروف بمصفوفة |
| 769 | [`769-sha1-manual.apl`](examples/769-sha1-manual.apl) | بناء SHA-1 من المواصفة |
| 770 | [`770-poly1305-lite.apl`](examples/770-poly1305-lite.apl) | مصادقة رسائل (RFC 8439) |
| 771 | [`771-bech32-lite.apl`](examples/771-bech32-lite.apl) | ترميز BIP 173 مع مجموع تحقق |
| 772 | [`772-fibonacci-coding.apl`](examples/772-fibonacci-coding.apl) | شفرة أعداد ذاتية الفصل |
| 773 | [`773-elias-gamma.apl`](examples/773-elias-gamma.apl) | شفرة عالمية للأعداد الصحيحة |
| 774 | [`774-natural-sort.apl`](examples/774-natural-sort.apl) | img2 يأتي قبل img10 |
| 775 | [`775-fuzzy-search.apl`](examples/775-fuzzy-search.apl) | ترتيب مرشحين بأسلوب fzf |
| 776 | [`776-bm25-lite.apl`](examples/776-bm25-lite.apl) | ترتيب مستندات لاستعلام بحث |
| 777 | [`777-plural-ar.apl`](examples/777-plural-ar.apl) | صيغ العدد: مفرد ومثنى وجمع |
| 778 | [`778-needleman-wunsch.apl`](examples/778-needleman-wunsch.apl) | محاذاة تسلسلين من الطرف للطرف |
| 779 | [`779-forth-lite.apl`](examples/779-forth-lite.apl) | مفسر لغة مكدسية مصغر |
| 780 | [`780-turing-machine.apl`](examples/780-turing-machine.apl) | محاكاة آلة تورينغ: جمع أحادي |
| 781 | [`781-l-system.apl`](examples/781-l-system.apl) | توليد نصوص الطحالب وكوخ |
| 782 | [`782-magic-square.apl`](examples/782-magic-square.apl) | مربعات سحرية فردية الرتبة |
| 783 | [`783-dragon-curve.apl`](examples/783-dragon-curve.apl) | متتالية منحنى التنين |
| 784 | [`784-z-order-curve.apl`](examples/784-z-order-curve.apl) | ترميز مورتون للإحداثيات |
| 785 | [`785-turtle-graphics.apl`](examples/785-turtle-graphics.apl) | رسم بأوامر F وR وL |
| 786 | [`786-business-days.apl`](examples/786-business-days.apl) | حساب أيام العمل مع العطلات |
| 787 | [`787-ipv4-cidr.apl`](examples/787-ipv4-cidr.apl) | تحليل عناوين وشبكات فرعية |
| 788 | [`788-genetic-algorithm.apl`](examples/788-genetic-algorithm.apl) | حل Ones-Max بالتطور الصناعي |
| 789 | [`789-lfsr-prng.apl`](examples/789-lfsr-prng.apl) | مسجل إزاحة بخطي راجع 16-بت |
| 790 | [`790-blum-blum-shub.apl`](examples/790-blum-blum-shub.apl) | مولد عشوائي آمن نظرياً |
| 791 | [`791-xxhash-lite.apl`](examples/791-xxhash-lite.apl) | تجزية غير تشفيرية سريعة |
| 792 | [`792-polybius-square.apl`](examples/792-polybius-square.apl) | شفرة الإحداثيات اليونانية |
| 793 | [`793-nihilist-cipher.apl`](examples/793-nihilist-cipher.apl) | شفرة بوليبيوس بمفتاح دوري |
| 794 | [`794-dct-lite.apl`](examples/794-dct-lite.apl) | تحويل JPEG الترددي مباشرة |
| 795 | [`795-elgamal-toy.apl`](examples/795-elgamal-toy.apl) | تشفير بمفتاح عام تعليمي |
| 796 | [`796-reed-solomon.apl`](examples/796-reed-solomon.apl) | تصحيح أخطاء بحذف وإتلاف |
| 797 | [`797-quoted-printable.apl`](examples/797-quoted-printable.apl) | ترميز بريد RFC 2045 |
| 798 | [`798-base85-codec.apl`](examples/798-base85-codec.apl) | ترميز ثنائي-نصي كثيف |
| 799 | [`799-justify-text.apl`](examples/799-justify-text.apl) | ضبط كامل بعرض ثابت |
| 800 | [`800-hex-dump.apl`](examples/800-hex-dump.apl) | عارض بايتات بأسلوب hexdump |
| 801 | [`801-printf-format.apl`](examples/801-printf-format.apl) | تنسيق نصوص بأسلوب C |
| 802 | [`802-shunting-yard.apl`](examples/802-shunting-yard.apl) | من infix إلى postfix وتقييم |
| 803 | [`803-knn-classifier.apl`](examples/803-knn-classifier.apl) | تصنيف بأقرب k جيران |
| 804 | [`804-naive-bayes.apl`](examples/804-naive-bayes.apl) | تصنيف نصوص احتمالي |
| 805 | [`805-id3-tree.apl`](examples/805-id3-tree.apl) | تعلم شجرة قرار من بيانات |
| 806 | [`806-discrete-log-bsgs.apl`](examples/806-discrete-log-bsgs.apl) | حل اللوغاريتم بجذر تربيعي |
| 807 | [`807-integer-partitions.apl`](examples/807-integer-partitions.apl) | عد p(n) وتعديد التقسيمات |
| 808 | [`808-barcode-code39.apl`](examples/808-barcode-code39.apl) | توليد باركود مع خانة تحقق |
| 809 | [`809-pbm-image.apl`](examples/809-pbm-image.apl) | صور نقطية بصيغة netpbm |
| 810 | [`810-ansi-color.apl`](examples/810-ansi-color.apl) | تنسيق طرفية بالتسلسلات |
| 811 | [`811-hex-color.apl`](examples/811-hex-color.apl) | نسبة تباين WCAG من hex |
| 812 | [`812-nim-game.apl`](examples/812-nim-game.apl) | استراتيجية نيم المثلى |
| 813 | [`813-md5-manual.apl`](examples/813-md5-manual.apl) | بناء MD5 من المواصفة |
| 814 | [`814-adfgvx.apl`](examples/814-adfgvx.apl) | شفرة ألمانيا في الحرب الأولى |
| 815 | [`815-columnar-transposition.apl`](examples/815-columnar-transposition.apl) | شفرة نقل كلاسيكية |
| 816 | [`816-robin-hood-hashing.apl`](examples/816-robin-hood-hashing.apl) | جدول تجزئة بتباين منخفض |
| 817 | [`817-baudot-code.apl`](examples/817-baudot-code.apl) | ترميز التليكس التاريخي |
| 818 | [`818-bifid-cipher.apl`](examples/818-bifid-cipher.apl) | شفرة تجزيئة بدون مفتاح |
| 819 | [`819-djb2-hash.apl`](examples/819-djb2-hash.apl) | تجزية نصوص شهيرة |
| 820 | [`820-xorshift.apl`](examples/820-xorshift.apl) | عشوائية سريعة بدون ضرب |
| 821 | [`821-splitmix.apl`](examples/821-splitmix.apl) | مولد بذور عالي الجودة |
| 822 | [`822-pcg-lite.apl`](examples/822-pcg-lite.apl) | عشوائية مبسطة عالية الجودة |
| 823 | [`823-zobrist-hashing.apl`](examples/823-zobrist-hashing.apl) | تجزئة وضعيات اللعب |
| 824 | [`824-cuckoo-filter.apl`](examples/824-cuckoo-filter.apl) | عضوية تقريبية قابلة للحذف |
| 825 | [`825-quasi-random-halton.apl`](examples/825-quasi-random-halton.apl) | توليد شبه عشوائي متجانس |
| 826 | [`826-kosaraju.apl`](examples/826-kosaraju.apl) | مكونات قوية الاتصال |
| 827 | [`827-gale-shapley.apl`](examples/827-gale-shapley.apl) | مطابقة مستقرة مضمونة |
| 828 | [`828-bipartite-matching.apl`](examples/828-bipartite-matching.apl) | أقصى تطابق بخوارزمية كون |
| 829 | [`829-hill-climbing.apl`](examples/829-hill-climbing.apl) | تحسين محلي بسيط |
| 830 | [`830-tabu-search.apl`](examples/830-tabu-search.apl) | هروب من الحلول المحلية |
| 831 | [`831-ant-colony-lite.apl`](examples/831-ant-colony-lite.apl) | أقصر جولة بالاستعارة النملية |
| 832 | [`832-particle-swarm-lite.apl`](examples/832-particle-swarm-lite.apl) | تحسين جماعي مستمر |
| 833 | [`833-runge-kutta.apl`](examples/833-runge-kutta.apl) | تكامل ODE بدقة رابعة |
| 834 | [`834-bisection-method.apl`](examples/834-bisection-method.apl) | إيجاد جذور الدوال |
| 835 | [`835-kolmogorov-smirnov.apl`](examples/835-kolmogorov-smirnov.apl) | اختبار مطابقة التوزيع |
| 836 | [`836-splay-tree.apl`](examples/836-splay-tree.apl) | شجرة ذاتية التعديل |
| 837 | [`837-lu-decomposition.apl`](examples/837-lu-decomposition.apl) | تحليل المصفوفة لحل الأنظمة |
| 838 | [`838-cholesky-decomposition.apl`](examples/838-cholesky-decomposition.apl) | تحليل متماثل أسرع من LU |
| 839 | [`839-gram-schmidt.apl`](examples/839-gram-schmidt.apl) | بناء قاعدة متعامدة معيارية |
| 840 | [`840-gauss-jordan.apl`](examples/840-gauss-jordan.apl) | حل أنظمة المعادلات الخطية |
| 841 | [`841-thomas-tridiagonal.apl`](examples/841-thomas-tridiagonal.apl) | حل ثلاثي القطر في زمن خطي |
| 842 | [`842-sieve-of-atkin.apl`](examples/842-sieve-of-atkin.apl) | غربال أولي حديث نظرياً |
| 843 | [`843-wheel-factorization.apl`](examples/843-wheel-factorization.apl) | قسمة تجريبية مسرعة |
| 844 | [`844-twin-primes.apl`](examples/844-twin-primes.apl) | حدسية غير مثبتة حتى اليوم |
| 845 | [`845-sophie-germain.apl`](examples/845-sophie-germain.apl) | استخدمت في برهان فيرما |
| 846 | [`846-emirp.apl`](examples/846-emirp.apl) | أولية مقلوبة غير متناظرة |
| 847 | [`847-semiprime.apl`](examples/847-semiprime.apl) | أساس أمن RSA |
| 848 | [`848-amicable-numbers.apl`](examples/848-amicable-numbers.apl) | 220 و284 منذ فيثاغورس |
| 849 | [`849-kaprekar-number.apl`](examples/849-kaprekar-number.apl) | كل رباعي يصل إلى 6174 |
| 850 | [`850-vampire-number.apl`](examples/850-vampire-number.apl) | 1260 = 21 في 60 |
| 851 | [`851-taxicab-number.apl`](examples/851-taxicab-number.apl) | 1729 وحوار رامانوجان |
| 852 | [`852-abundant-numbers.apl`](examples/852-abundant-numbers.apl) | أول وفيرة فردية هي 945 |
| 853 | [`853-trailing-zeros-factorial.apl`](examples/853-trailing-zeros-factorial.apl) | أسرع من حساب المضروب |
| 854 | [`854-primorial.apl`](examples/854-primorial.apl) | مضروب الأولية وبرهان إقليدس |
| 855 | [`855-gregory-pi.apl`](examples/855-gregory-pi.apl) | أبسط متسلسلة لط |
| 856 | [`856-nilakantha-pi.apl`](examples/856-nilakantha-pi.apl) | مئة حد لخمس خانات |
| 857 | [`857-machin-pi.apl`](examples/857-machin-pi.apl) | حسبت ط لمئة خانة عام 1706 |
| 858 | [`858-aliquot-sequence.apl`](examples/858-aliquot-sequence.apl) | مصائر: واحد أو كامل أو متحاب |
| 859 | [`859-recaman-sequence.apl`](examples/859-recaman-sequence.apl) | متتابعة ذاتية المرجع |
| 860 | [`860-boyer-moore-search.apl`](examples/860-boyer-moore-search.apl) | بحث نصي بقفزات طويلة |
| 861 | [`861-lucas-numbers.apl`](examples/861-lucas-numbers.apl) | نظير فيبوناتشي بالنسبة الذهبية |
| 862 | [`862-pell-numbers.apl`](examples/862-pell-numbers.apl) | تقارب النسبة الفضية |
| 863 | [`863-jacobsthal-numbers.apl`](examples/863-jacobsthal-numbers.apl) | صيغة مغلقة بقوى اثنين |
| 864 | [`864-stirling-second.apl`](examples/864-stirling-second.apl) | تكرارية k*S+S |
| 865 | [`865-bell-numbers.apl`](examples/865-bell-numbers.apl) | عدد تقسيمات المجموعة |
| 866 | [`866-three-sum.apl`](examples/866-three-sum.apl) | ثلاثيات صفرية فريدة |
| 867 | [`867-integral-image.apl`](examples/867-integral-image.apl) | مجاميع مستطيلات في O(1) |
| 868 | [`868-difference-array.apl`](examples/868-difference-array.apl) | تراكم مؤجل واحد |
| 869 | [`869-stein-gcd.apl`](examples/869-stein-gcd.apl) | قاسم مشترك للعتاد |
| 870 | [`870-russian-peasant.apl`](examples/870-russian-peasant.apl) | ضرب بلا جدول ضرب |
| 871 | [`871-gauss-seidel.apl`](examples/871-gauss-seidel.apl) | حل تكراري للأنظمة |
| 872 | [`872-power-iteration.apl`](examples/872-power-iteration.apl) | أكبر قيمة ذاتية |
| 873 | [`873-euler-method.apl`](examples/873-euler-method.apl) | أبسط تكامل ODE |
| 874 | [`874-jarvis-march.apl`](examples/874-jarvis-march.apl) | غلاف محدب بسيط |
| 875 | [`875-monty-hall.apl`](examples/875-monty-hall.apl) | التبديل يفوز بثلثين |
| 876 | [`876-birthday-paradox.apl`](examples/876-birthday-paradox.apl) | 23 تكفي لخمسين بالمئة |
| 877 | [`877-coupon-collector.apl`](examples/877-coupon-collector.apl) | متوسط جمع الأنواع |
| 878 | [`878-farey-sequence.apl`](examples/878-farey-sequence.apl) | خاصية الجارين bc-ad=1 |
| 879 | [`879-stern-brocot.apl`](examples/879-stern-brocot.apl) | مسار L/R لكل كسر |
| 880 | [`880-lehmer-code.apl`](examples/880-lehmer-code.apl) | رتبة التبديل في n! |
| 881 | [`881-damm-algorithm.apl`](examples/881-damm-algorithm.apl) | يكشف الأخطاء والتبديلات |
| 882 | [`882-floyd-cycle.apl`](examples/882-floyd-cycle.apl) | دورة بذاكرة ثابتة |
| 883 | [`883-balanced-ternary.apl`](examples/883-balanced-ternary.apl) | تمثيل فريد للسالب والموجب |
| 884 | [`884-zeckendorf.apl`](examples/884-zeckendorf.apl) | جشع فريد لكل عدد |
| 885 | [`885-thue-morse.apl`](examples/885-thue-morse.apl) | خالية من التكرار الثلاثي |
| 886 | [`886-kolakoski.apl`](examples/886-kolakoski.apl) | متتابعة مولدة لنفسها |
| 887 | [`887-hofstadter-q.apl`](examples/887-hofstadter-q.apl) | تكرارية ميتافيبوناتشي |
| 888 | [`888-fusc-diatomic.apl`](examples/888-fusc-diatomic.apl) | تعد شجرة كوكينس |
| 889 | [`889-motzkin-numbers.apl`](examples/889-motzkin-numbers.apl) | تنعيم كاتالان بخطوة مستوية |
| 890 | [`890-schroder-numbers.apl`](examples/890-schroder-numbers.apl) | تقارب ضعفي مع كاتالان |
| 891 | [`891-delannoy-numbers.apl`](examples/891-delannoy-numbers.apl) | وسطاء المسارات القطرية |
| 892 | [`892-narayana-numbers.apl`](examples/892-narayana-numbers.apl) | تنعيم كاتالان بعدد القمم |
| 893 | [`893-eulerian-numbers.apl`](examples/893-eulerian-numbers.apl) | مجموع الصف مضروب ن |
| 894 | [`894-cantor-pairing.apl`](examples/894-cantor-pairing.apl) | فك ببحث مثلثي ثنائي |
| 895 | [`895-cantor-set.apl`](examples/895-cantor-set.apl) | عضوية في فراكتل |
| 896 | [`896-exponential-search.apl`](examples/896-exponential-search.apl) | بحث في مصفوفة غير محدودة |
| 897 | [`897-fibonacci-search.apl`](examples/897-fibonacci-search.apl) | لوصول غير متجانس الكلفة |
| 898 | [`898-move-to-front.apl`](examples/898-move-to-front.apl) | ضغط يستغل التكرار الموضعي |
| 899 | [`899-distinct-subsequences.apl`](examples/899-distinct-subsequences.apl) | عد بلا تكرار |
| 900 | [`900-lyndon-words.apl`](examples/900-lyndon-words.apl) | أدنى من كل تدويراتها |
| 901 | [`901-minimal-rotation.apl`](examples/901-minimal-rotation.apl) | مطابقة السلاسل الدائرية |
| 902 | [`902-shannon-entropy.apl`](examples/902-shannon-entropy.apl) | متوسط المعلومة بالبت |
| 903 | [`903-kl-divergence.apl`](examples/903-kl-divergence.apl) | بعد احتمالي غير متماثل |
| 904 | [`904-gini-coefficient.apl`](examples/904-gini-coefficient.apl) | قياس عدم المساواة |
| 905 | [`905-kendall-tau.apl`](examples/905-kendall-tau.apl) | ارتباط ترتيبي |
| 906 | [`906-skewness-kurtosis.apl`](examples/906-skewness-kurtosis.apl) | قياس شكل التوزيع |
| 907 | [`907-negabinary.apl`](examples/907-negabinary.apl) | سالب وموجب بلا بت إشارة |
| 908 | [`908-iqr-outliers.apl`](examples/908-iqr-outliers.apl) | فرز ووسائط وربيعيات |
| 909 | [`909-dutch-national-flag.apl`](examples/909-dutch-national-flag.apl) | فرز ثلاثي في مكانه |
| 910 | [`910-cycle-sort.apl`](examples/910-cycle-sort.apl) | أقل كتابات ممكنة |
| 911 | [`911-sliding-window-maximum.apl`](examples/911-sliding-window-maximum.apl) | كل عنصر يعالج مرة |
| 912 | [`912-longest-increasing-subsequence.apl`](examples/912-longest-increasing-subsequence.apl) | طول في n log n |
| 913 | [`913-lru-cache.apl`](examples/913-lru-cache.apl) | إخلاء الأقدم عند الامتلاء |
| 914 | [`914-hyperloglog.apl`](examples/914-hyperloglog.apl) | عد تقريبي بذاكرة ثابتة |
| 915 | [`915-bipartite-check.apl`](examples/915-bipartite-check.apl) | لا جارين بلون واحد |
| 916 | [`916-bridges.apl`](examples/916-bridges.apl) | أضلاع حذفها يفصل |
| 917 | [`917-matrix-chain.apl`](examples/917-matrix-chain.apl) | أقل عدد عمليات |
| 918 | [`918-recaman.apl`](examples/918-recaman.apl) | قفزات بحجم الموضع |
| 919 | [`919-van-eck.apl`](examples/919-van-eck.apl) | صفر للجديد |
| 920 | [`920-egyptian-fraction.apl`](examples/920-egyptian-fraction.apl) | تمثيل قديم للكسور |
| 921 | [`921-continued-fraction.apl`](examples/921-continued-fraction.apl) | أفضل تقريب كسري |
| 922 | [`922-kaprekar.apl`](examples/922-kaprekar.apl) | كل رباعي يبلغ 6174 |
| 923 | [`923-huffman.apl`](examples/923-huffman.apl) | شيفرات مثلى بلا بادئة |
| 924 | [`924-lz77.apl`](examples/924-lz77.apl) | أساس ZIP و gzip |
| 925 | [`925-base64.apl`](examples/925-base64.apl) | أبجدية 64 قابلة للطباعة |
| 926 | [`926-varint.apl`](examples/926-varint.apl) | أعداد صغيرة ببايتات أقل |
| 927 | [`927-kmeans.apl`](examples/927-kmeans.apl) | تقسيم نقاط لمجموعات |
| 928 | [`928-logistic-regression.apl`](examples/928-logistic-regression.apl) | تصنيف ثنائي احتمالي |
| 929 | [`929-median-of-medians.apl`](examples/929-median-of-medians.apl) | اختيار خطي بأسوأ حالة |
| 930 | [`930-golden-section.apl`](examples/930-golden-section.apl) | تقليل بلا مشتقات |
| 931 | [`931-soundex.apl`](examples/931-soundex.apl) | أسماء متشابهة الصوت |
| 932 | [`932-jaro-winkler.apl`](examples/932-jaro-winkler.apl) | قياس تقارب الأسماء |
| 933 | [`933-kmp.apl`](examples/933-kmp.apl) | بحث بلا رجوع في النص |
| 934 | [`934-longest-common-subsequence.apl`](examples/934-longest-common-subsequence.apl) | أساس diff الحيوي |
| 935 | [`935-regex-matcher.apl`](examples/935-regex-matcher.apl) | مطابقة نمط كامل |
| 936 | [`936-arithmetic-coding.apl`](examples/936-arithmetic-coding.apl) | سلسلة كاملة في كسر |
| 937 | [`937-lzw.apl`](examples/937-lzw.apl) | أساس GIF |
| 938 | [`938-bitonic-sort.apl`](examples/938-bitonic-sort.apl) | فرز قابل للتوازي |
| 939 | [`939-pancake-sort.apl`](examples/939-pancake-sort.apl) | قلبتان لكل عنصر |
| 940 | [`940-cholesky.apl`](examples/940-cholesky.apl) | للموجبة التعريف |
| 941 | [`941-simpson-rule.apl`](examples/941-simpson-rule.apl) | تكامل بقطع مكافئ |
| 942 | [`942-dft.apl`](examples/942-dft.apl) | من الزمن للتردد |
| 943 | [`943-haar-wavelet.apl`](examples/943-haar-wavelet.apl) | أبسط تحويل مويجي |
| 944 | [`944-kalman.apl`](examples/944-kalman.apl) | دمج قياسات مضججة |
| 945 | [`945-lucas-theorem.apl`](examples/945-lucas-theorem.apl) | C(n,k) مودولو أولي |
| 946 | [`946-primitive-root.apl`](examples/946-primitive-root.apl) | مولد مودولو أولي |
| 947 | [`947-shamir.apl`](examples/947-shamir.apl) | ك حصة تكفي وأقل لا |
| 948 | [`948-hamming-code.apl`](examples/948-hamming-code.apl) | تصحيح خطأ واحد |
| 949 | [`949-rule-30.apl`](examples/949-rule-30.apl) | فوضى من قاعدة بسيطة |
| 950 | [`950-maze-generation.apl`](examples/950-maze-generation.apl) | متاهة مثالية بشجرة |
| 951 | [`951-sudoku.apl`](examples/951-sudoku.apl) | صف وعمود وصندوق |
| 952 | [`952-interval-scheduling.apl`](examples/952-interval-scheduling.apl) | أكبر عدد مهام متوافقة |
| 953 | [`953-egg-drop.apl`](examples/953-egg-drop.apl) | محاولات مضمونة |
| 954 | [`954-tf-idf.apl`](examples/954-tf-idf.apl) | أهمية مصطلح لوثيقة |
| 955 | [`955-segment-intersection.apl`](examples/955-segment-intersection.apl) | جداء تبادلي بإشارات |
| 956 | [`956-lagrange.apl`](examples/956-lagrange.apl) | كثير حدود مار بنقاط |
| 957 | [`957-majority-vote.apl`](examples/957-majority-vote.apl) | أغلبية بذاكرة ثابتة |
| 958 | [`958-weighted-interval.apl`](examples/958-weighted-interval.apl) | أقصى ربح بلا تداخل |
| 959 | [`959-job-sequencing.apl`](examples/959-job-sequencing.apl) | أقصى ربح قبل الموعد |
| 960 | [`960-cryptarithmetic.apl`](examples/960-cryptarithmetic.apl) | SEND+MORE=MONEY |
| 961 | [`961-tree-diameter.apl`](examples/961-tree-diameter.apl) | أطول مسار بين عقدتين |
| 962 | [`962-viterbi.apl`](examples/962-viterbi.apl) | فك ملاحظات ماركوف |
| 963 | [`963-simhash.apl`](examples/963-simhash.apl) | تقارب وثائق بمسافة هامنغ |
| 964 | [`964-fisher-yates.apl`](examples/964-fisher-yates.apl) | خلط عادل بمرور واحد |
| 965 | [`965-bresenham.apl`](examples/965-bresenham.apl) | رسم خطوط بلا كسور |
| 966 | [`966-bezier.apl`](examples/966-bezier.apl) | أساس منحنيات الرسم |
| 967 | [`967-mortgage-amortization.apl`](examples/967-mortgage-amortization.apl) | فائدة تتناقص وأصل ينمو |
| 968 | [`968-rdp.apl`](examples/968-rdp.apl) | ضغط مسارات الخرائط |
| 969 | [`969-exponential-smoothing.apl`](examples/969-exponential-smoothing.apl) | سلسلة زمنية ملساء |
| 970 | [`970-pell-equation.apl`](examples/970-pell-equation.apl) | حلول ديوفانتية صحيحة |
| 971 | [`971-geohash.apl`](examples/971-geohash.apl) | عنوان نصي لإحداثيات |
| 972 | [`972-baby-step-giant-step.apl`](examples/972-baby-step-giant-step.apl) | لوغاريتم منفصل بجذر الزمن |
| 973 | [`973-fermat-factorization.apl`](examples/973-fermat-factorization.apl) | تحليل قريب من مربع |
| 974 | [`974-ear-clipping.apl`](examples/974-ear-clipping.apl) | مضلع إلى مثلثات |
| 975 | [`975-legendre-symbol.apl`](examples/975-legendre-symbol.apl) | باقٍ تربيعي أم لا |
| 976 | [`976-barnsley-fern.apl`](examples/976-barnsley-fern.apl) | فركتال نباتي واقعي |
| 977 | [`977-median-filter.apl`](examples/977-median-filter.apl) | إزالة الشوائب النبضية |
| 978 | [`978-hilbert.apl`](examples/978-hilbert.apl) | ملء فضاء يحفظ الجوار |
| 979 | [`979-k-nearest.apl`](examples/979-k-nearest.apl) | تصنيف بلا نموذج مدرب |
| 980 | [`980-zeller.apl`](examples/980-zeller.apl) | أي تاريخ إلى يوم أسبوع |
| 981 | [`981-cubic-spline.apl`](examples/981-cubic-spline.apl) | منحنى أملس مار بالنقاط |
| 982 | [`982-hamiltonian-path.apl`](examples/982-hamiltonian-path.apl) | زيارة كل عقدة مرة |
| 983 | [`983-two-sat.apl`](examples/983-two-sat.apl) | حل ومستحيل بتعيينات |
| 984 | [`984-optimal-bst.apl`](examples/984-optimal-bst.apl) | أدنى كلفة بحث متوقعة |
| 985 | [`985-carmichael.apl`](examples/985-carmichael.apl) | مركبة تنتحل الأولية |
| 986 | [`986-tonelli-shanks.apl`](examples/986-tonelli-shanks.apl) | أساس التوقيع الرقمي |
| 987 | [`987-strassen.apl`](examples/987-strassen.apl) | مصفوفات بلا حلقات |
| 988 | [`988-boruvka.apl`](examples/988-boruvka.apl) | أقدم خوارزمية امتداد |
| 989 | [`989-min-cost-flow.apl`](examples/989-min-cost-flow.apl) | نقل بأرخص الطرق |
| 990 | [`990-qr-decomposition.apl`](examples/990-qr-decomposition.apl) | أساس حل المربعات الصغرى |
| 991 | [`991-dbscan.apl`](examples/991-dbscan.apl) | عناقيد بلا عدد مسبق |
| 992 | [`992-apriori.apl`](examples/992-apriori.apl) | أصناف تُشترى معاً |
| 993 | [`993-rod-cutting.apl`](examples/993-rod-cutting.apl) | أقصى ثمن للتقطيع |
| 994 | [`994-lazy-segment-tree.apl`](examples/994-lazy-segment-tree.apl) | إضافة مدى واستعلام |
| 995 | [`995-ring-buffer.apl`](examples/995-ring-buffer.apl) | طابور بسعة ثابتة |
| 996 | [`996-bigint-multiply.apl`](examples/996-bigint-multiply.apl) | حساب بلا حد للطول |
| 997 | [`997-pi-spigot.apl`](examples/997-pi-spigot.apl) | ط بلا كسور عائمة |
| 998 | [`998-midi-freq.apl`](examples/998-midi-freq.apl) | من رقم النوتة للهرتز |
| 999 | [`999-floyd-steinberg.apl`](examples/999-floyd-steinberg.apl) | رمادي إلى ثنائي بسلاسة |
| 1000 | [`1000-convolution.apl`](examples/1000-convolution.apl) | أساس معالجة الإشارات |
| 1001 | [`1001-ugly-numbers.apl`](examples/1001-ugly-numbers.apl) | ترتيب أعداد عواملها 2 و3 و5 |
| 1002 | [`1002-container-water.apl`](examples/1002-container-water.apl) | أقصى مساحة بين عمودين |
| 1003 | [`1003-move-zeroes.apl`](examples/1003-move-zeroes.apl) | دفع الأصفار للنهاية مع حفظ الترتيب |
| 1004 | [`1004-missing-number.apl`](examples/1004-missing-number.apl) | إيجاد رقم ناقص من متتالية |
| 1005 | [`1005-single-number-xor.apl`](examples/1005-single-number-xor.apl) | العنصر الذي لا يتكرر |
| 1006 | [`1006-plus-one.apl`](examples/1006-plus-one.apl) | إضافة واحد لعدد مخزن أرقاماً |
| 1007 | [`1007-merge-sorted-arrays.apl`](examples/1007-merge-sorted-arrays.apl) | الدمج بالترتيب في مرور واحد |
| 1008 | [`1008-first-unique-char.apl`](examples/1008-first-unique-char.apl) | فهرس أول حرف يظهر مرة واحدة |
| 1009 | [`1009-isomorphic-strings.apl`](examples/1009-isomorphic-strings.apl) | تطابق نمط الحروف بين نصين |
| 1010 | [`1010-ransom-note.apl`](examples/1010-ransom-note.apl) | هل تكفي حروف المجلة للرسالة |
| 1011 | [`1011-best-time-stock.apl`](examples/1011-best-time-stock.apl) | أقصى ربح من صفقة واحدة |
| 1012 | [`1012-jump-game.apl`](examples/1012-jump-game.apl) | هل نصل للنهاية بخطوات محددة |
| 1013 | [`1013-gas-station.apl`](examples/1013-gas-station.apl) | نقطة بداية دورة كاملة |
| 1014 | [`1014-candy-distribution.apl`](examples/1014-candy-distribution.apl) | أقل حلوى تحقق شرط الجيران |
| 1015 | [`1015-partition-labels.apl`](examples/1015-partition-labels.apl) | أكبر عدد أجزاء لا يتكرر حرفها |
| 1016 | [`1016-daily-temperatures.apl`](examples/1016-daily-temperatures.apl) | عدد الأيام حتى يوم أدفأ |
| 1017 | [`1017-asteroid-collision.apl`](examples/1017-asteroid-collision.apl) | محاكاة تصادم كويكبات متقابلة |
| 1018 | [`1018-decode-ways.apl`](examples/1018-decode-ways.apl) | عدد طرق قراءة رقم كحروف |
| 1019 | [`1019-unique-paths.apl`](examples/1019-unique-paths.apl) | عدد مسارات يمين وأسفل في شبكة |
| 1020 | [`1020-min-path-sum.apl`](examples/1020-min-path-sum.apl) | أرخص طريق من الزاوية للزاوية |
| 1021 | [`1021-max-product-subarray.apl`](examples/1021-max-product-subarray.apl) | أكبر ضرب لعناصر متجاورة |
| 1022 | [`1022-house-robber-circular.apl`](examples/1022-house-robber-circular.apl) | أقصى سرقة في صف دائري |
| 1023 | [`1023-bin-packing-ffd.apl`](examples/1023-bin-packing-ffd.apl) | تقدير أقل عدد صناديق |
| 1024 | [`1024-pythagorean-triples.apl`](examples/1024-pythagorean-triples.apl) | كل ثلاثيات الأعداد حتى حد |
| 1025 | [`1025-binary-gap.apl`](examples/1025-binary-gap.apl) | أطول سلسلة أصفار بين واحدين |
| 1026 | [`1026-min-add-parens.apl`](examples/1026-min-add-parens.apl) | أقل إضافات لتوازن الأقواس |
| 1027 | [`1027-longest-valid-parens.apl`](examples/1027-longest-valid-parens.apl) | أطول جزء متوازن متصل |
| 1028 | [`1028-longest-consecutive.apl`](examples/1028-longest-consecutive.apl) | أطول أعداد متتابعة غير مرتبة |
| 1029 | [`1029-subarray-sum-k.apl`](examples/1029-subarray-sum-k.apl) | عدد الأجزاء المتصلة بمجموع معين |
| 1030 | [`1030-longest-no-repeat.apl`](examples/1030-longest-no-repeat.apl) | أطول جزء بحروف مختلفة |
| 1031 | [`1031-min-size-subarray.apl`](examples/1031-min-size-subarray.apl) | أقصر جزء مجموعه لا يقل عن هدف |
| 1032 | [`1032-rotate-string.apl`](examples/1032-rotate-string.apl) | هل نص دوران لنص آخر |
| 1033 | [`1033-reverse-words-spaces.apl`](examples/1033-reverse-words-spaces.apl) | عكس ترتيب الكلمات وحذف الفراغ الزائد |
| 1034 | [`1034-valid-mountain.apl`](examples/1034-valid-mountain.apl) | هل القائمة تصعد ثم تهبط |
| 1035 | [`1035-sorted-squares.apl`](examples/1035-sorted-squares.apl) | مربعات قائمة مرتبة بلا فرز جديد |
| 1036 | [`1036-sorted-intersection.apl`](examples/1036-sorted-intersection.apl) | العناصر المشتركة بلا تكرار |
| 1037 | [`1037-duplicate-within-k.apl`](examples/1037-duplicate-within-k.apl) | هل يتكرر عنصر خلال مسافة محددة |
| 1038 | [`1038-remove-element.apl`](examples/1038-remove-element.apl) | حذف كل ظهور لقيمة وإرجاع الطول الجديد |
| 1039 | [`1039-search-rotated.apl`](examples/1039-search-rotated.apl) | إيجاد قيمة في قائمة مرتبة مدورة |
| 1040 | [`1040-find-peak.apl`](examples/1040-find-peak.apl) | فهرس عنصر أكبر من جاريه |
| 1041 | [`1041-first-last-position.apl`](examples/1041-first-last-position.apl) | حدود ظهور قيمة في قائمة مرتبة |
| 1042 | [`1042-integer-sqrt.apl`](examples/1042-integer-sqrt.apl) | أكبر عدد مربعه لا يتجاوز العدد |
| 1043 | [`1043-power-of-three.apl`](examples/1043-power-of-three.apl) | هل العدد قوة للثلاثة |
| 1044 | [`1044-add-binary.apl`](examples/1044-add-binary.apl) | جمع عددين ثنائيين مكتوبين نصاً |
| 1045 | [`1045-multiply-strings.apl`](examples/1045-multiply-strings.apl) | ضرب عددين كبيرين مكتوبين نصاً |
| 1046 | [`1046-string-compress.apl`](examples/1046-string-compress.apl) | اختصار التكرار المتتالي |
| 1047 | [`1047-length-last-word.apl`](examples/1047-length-last-word.apl) | طول آخر كلمة في جملة |
| 1048 | [`1048-count-bits-table.apl`](examples/1048-count-bits-table.apl) | عدد الآحاد الثنائية لكل عدد حتى ن |
| 1049 | [`1049-first-missing-positive.apl`](examples/1049-first-missing-positive.apl) | أصغر عدد موجب غائب |
| 1050 | [`1050-h-index.apl`](examples/1050-h-index.apl) | أكبر ه بحيث ه أبحاث لكل منها ه استشهاداً |
| 1051 | [`1051-set-matrix-zeroes.apl`](examples/1051-set-matrix-zeroes.apl) | تصفير صف وعمود كل خانة صفرية |
| 1052 | [`1052-remove-dup-twice.apl`](examples/1052-remove-dup-twice.apl) | السماح بتكرارين لكل قيمة في قائمة مرتبة |
| 1053 | [`1053-pascal-row.apl`](examples/1053-pascal-row.apl) | بناء صف محدد من مثلث باسكال |
| 1054 | [`1054-word-pattern.apl`](examples/1054-word-pattern.apl) | هل تتبع الكلمات نمط الحروف |
| 1055 | [`1055-reverse-vowels.apl`](examples/1055-reverse-vowels.apl) | عكس مواضع حروف العلة فقط |
| 1056 | [`1056-find-substring.apl`](examples/1056-find-substring.apl) | فهرس أول ظهور لنص داخل نص |
| 1057 | [`1057-contiguous-array.apl`](examples/1057-contiguous-array.apl) | أطول جزء بأصفار وآحاد متساوية |
| 1058 | [`1058-coin-change-ways.apl`](examples/1058-coin-change-ways.apl) | عدد التراكيب التي تبلغ مبلغاً |
| 1059 | [`1059-perfect-squares-dp.apl`](examples/1059-perfect-squares-dp.apl) | أقل عدد مربعات مجموعها ن |
| 1060 | [`1060-target-sum-ways.apl`](examples/1060-target-sum-ways.apl) | عدد طرق وضع الإشارات للوصول لهدف |
| 1061 | [`1061-min-cuts-palindrome.apl`](examples/1061-min-cuts-palindrome.apl) | أقل قطع تجعل كل جزء متناظراً |
| 1062 | [`1062-longest-palindromic-subseq.apl`](examples/1062-longest-palindromic-subseq.apl) | أطول تتابع غير متصل يقرأ بالاتجاهين |
| 1063 | [`1063-interleaving-string.apl`](examples/1063-interleaving-string.apl) | هل نص مدموج من نصين بحفظ ترتيب كل منهما |
| 1064 | [`1064-falling-path-sum.apl`](examples/1064-falling-path-sum.apl) | أقل مجموع نزول بخطوة أو قطر |
| 1065 | [`1065-triangle-min-path.apl`](examples/1065-triangle-min-path.apl) | أقل مجموع من قمة المثلث لقاعدته |
| 1066 | [`1066-maximal-square.apl`](examples/1066-maximal-square.apl) | مساحة أكبر مربع كله آحاد |
| 1067 | [`1067-stock-cooldown.apl`](examples/1067-stock-cooldown.apl) | أقصى ربح مع يوم راحة بعد كل بيع |
| 1068 | [`1068-stock-two-transactions.apl`](examples/1068-stock-two-transactions.apl) | أقصى ربح بصفقتين على الأكثر |
| 1069 | [`1069-longest-palindrome-build.apl`](examples/1069-longest-palindrome-build.apl) | طول أطول متناظر من حروف نص |
| 1070 | [`1070-ones-with-flips.apl`](examples/1070-ones-with-flips.apl) | أطول جزء آحاد بعد قلب عدد محدود من الأصفار |
| 1071 | [`1071-anagram-indices.apl`](examples/1071-anagram-indices.apl) | كل مواضع بدء جناس نص داخل نص |
| 1072 | [`1072-shortest-unsorted.apl`](examples/1072-shortest-unsorted.apl) | طول أقصر جزء لو رتبناه رتبت القائمة |
| 1073 | [`1073-next-permutation.apl`](examples/1073-next-permutation.apl) | التبديل الأكبر التالي بالترتيب المعجمي |
| 1074 | [`1074-pivot-index.apl`](examples/1074-pivot-index.apl) | موضع مجموع ما قبله يساوي مجموع ما بعده |
| 1075 | [`1075-valid-triangle-count.apl`](examples/1075-valid-triangle-count.apl) | كم ثلاثية أضلاع تكوّن مثلثاً |
| 1076 | [`1076-digit-product-minus-sum.apl`](examples/1076-digit-product-minus-sum.apl) | ضرب خانات عدد ناقص جمعها |
| 1077 | [`1077-reverse-integer.apl`](examples/1077-reverse-integer.apl) | عكس خانات عدد مع حد 32 بت |
| 1078 | [`1078-add-without-plus.apl`](examples/1078-add-without-plus.apl) | الجمع بعمليات البتات فقط |
| 1079 | [`1079-number-complement.apl`](examples/1079-number-complement.apl) | قلب بتات العدد دون الأصفار الأمامية |
| 1080 | [`1080-nth-digit.apl`](examples/1080-nth-digit.apl) | الخانة ن في 123456789101112 |
| 1081 | [`1081-self-dividing.apl`](examples/1081-self-dividing.apl) | أعداد تقبل القسمة على كل خانة فيها |
| 1082 | [`1082-to-base-k.apl`](examples/1082-to-base-k.apl) | كتابة عدد في أساس من 2 إلى 16 |
| 1083 | [`1083-excel-title-number.apl`](examples/1083-excel-title-number.apl) | تحويل اسم العمود لرقمه |
| 1084 | [`1084-bulb-switcher.apl`](examples/1084-bulb-switcher.apl) | كم مصباح يبقى مضاء بعد ن جولة |
| 1085 | [`1085-water-jug.apl`](examples/1085-water-jug.apl) | هل نقيس كمية بإبريقين |
| 1086 | [`1086-valid-perfect-square.apl`](examples/1086-valid-perfect-square.apl) | هل العدد مربع كامل بلا جذر مضمن |
| 1087 | [`1087-arranging-coins.apl`](examples/1087-arranging-coins.apl) | عدد الصفوف الكاملة في سلم عملات |
| 1088 | [`1088-detect-capital.apl`](examples/1088-detect-capital.apl) | هل كتابة الكلمة بالأحرف الكبيرة صحيحة |
| 1089 | [`1089-repeated-substring.apl`](examples/1089-repeated-substring.apl) | هل النص تكرار لجزء منه |
| 1090 | [`1090-license-key-format.apl`](examples/1090-license-key-format.apl) | إعادة تجميع المفتاح بمجموعات متساوية |
| 1091 | [`1091-to-lower-manual.apl`](examples/1091-to-lower-manual.apl) | تحويل الأحرف اللاتينية الكبيرة لصغيرة |
| 1092 | [`1092-unique-emails.apl`](examples/1092-unique-emails.apl) | عدد العناوين المختلفة فعلاً |
| 1093 | [`1093-goat-latin.apl`](examples/1093-goat-latin.apl) | تحويل الجملة بقواعد لغة الماعز |
| 1094 | [`1094-defang-ip.apl`](examples/1094-defang-ip.apl) | كتابة النقاط بين أقواس |
| 1095 | [`1095-route-circle.apl`](examples/1095-route-circle.apl) | هل تعيد الحركات الروبوت لنقطة البداية |
| 1096 | [`1096-baseball-game.apl`](examples/1096-baseball-game.apl) | حساب النقاط بقواعد ملغاة ومضاعفة ومجموع |
| 1097 | [`1097-can-place-flowers.apl`](examples/1097-can-place-flowers.apl) | هل نزرع عدداً من الزهور دون تجاور |
| 1098 | [`1098-lemonade-change.apl`](examples/1098-lemonade-change.apl) | هل نعيد الباقي لكل زبون |
| 1099 | [`1099-height-checker.apl`](examples/1099-height-checker.apl) | عدد الطلاب الواقفين في غير موضعهم |
| 1100 | [`1100-check-pangram.apl`](examples/1100-check-pangram.apl) | هل تحوي الجملة كل حروف الأبجدية |
| 1101 | [`1101-max-69-number.apl`](examples/1101-max-69-number.apl) | أكبر عدد بتغيير خانة واحدة من 6 إلى 9 |
| 1102 | [`1102-min-stack.apl`](examples/1102-min-stack.apl) | مكدس يعرف أدنى قيمة فيه في زمن ثابت |
| 1103 | [`1103-queue-two-stacks.apl`](examples/1103-queue-two-stacks.apl) | طابور مبني من مكدسين |
| 1104 | [`1104-circular-deque.apl`](examples/1104-circular-deque.apl) | طابور بطرفين على مصفوفة ثابتة |
| 1105 | [`1105-hit-counter.apl`](examples/1105-hit-counter.apl) | عدد الزيارات في آخر 300 ثانية |
| 1106 | [`1106-moving-average.apl`](examples/1106-moving-average.apl) | متوسط آخر ك قيم في تدفق |
| 1107 | [`1107-logger-rate-limit.apl`](examples/1107-logger-rate-limit.apl) | منع تكرار رسالة قبل عشر ثوانٍ |
| 1108 | [`1108-phone-directory.apl`](examples/1108-phone-directory.apl) | إعطاء الأرقام وإعادتها |
| 1109 | [`1109-text-editor.apl`](examples/1109-text-editor.apl) | إضافة وحذف وتحريك مؤشر |
| 1110 | [`1110-browser-history.apl`](examples/1110-browser-history.apl) | زيارة ورجوع وتقدم |
| 1111 | [`1111-snapshot-array.apl`](examples/1111-snapshot-array.apl) | مصفوفة تحفظ لقطات من حالاتها |
| 1112 | [`1112-time-map.apl`](examples/1112-time-map.apl) | قراءة قيمة مفتاح كما كانت في وقت ما |
| 1113 | [`1113-randomized-set.apl`](examples/1113-randomized-set.apl) | إدخال وحذف في زمن ثابت |
| 1114 | [`1114-first-unique-stream.apl`](examples/1114-first-unique-stream.apl) | أول عنصر لم يتكرر حتى الآن |
| 1115 | [`1115-product-of-numbers.apl`](examples/1115-product-of-numbers.apl) | ضرب آخر ك عدداً من تدفق |
| 1116 | [`1116-bank-system.apl`](examples/1116-bank-system.apl) | إيداع وسحب وتحويل بين حسابات |
| 1117 | [`1117-stock-spanner.apl`](examples/1117-stock-spanner.apl) | عدد الأيام المتتالية بسعر لا يتجاوز اليوم |
| 1118 | [`1118-kth-largest-stream.apl`](examples/1118-kth-largest-stream.apl) | الترتيب ك من الأكبر مع كل إدخال |
| 1119 | [`1119-range-sum-query.apl`](examples/1119-range-sum-query.apl) | مجموع أي مدى في زمن ثابت |
| 1120 | [`1120-matrix-region-sum.apl`](examples/1120-matrix-region-sum.apl) | مجموع مستطيل في مصفوفة |
| 1121 | [`1121-peeking-iterator.apl`](examples/1121-peeking-iterator.apl) | مكرر يعرض التالي دون استهلاكه |
| 1122 | [`1122-flatten-nested.apl`](examples/1122-flatten-nested.apl) | مكرر يمر على أعداد داخل قوائم متعددة المستويات |
| 1123 | [`1123-zigzag-iterator.apl`](examples/1123-zigzag-iterator.apl) | أخذ عنصر من كل قائمة بالتناوب |
| 1124 | [`1124-underground-system.apl`](examples/1124-underground-system.apl) | متوسط زمن الرحلة بين محطتين |
| 1125 | [`1125-undo-redo-editor.apl`](examples/1125-undo-redo-editor.apl) | كتابة وتراجع وإعادة |
| 1126 | [`1126-vending-machine.apl`](examples/1126-vending-machine.apl) | إدخال نقود وصرف منتج وباقٍ |
| 1127 | [`1127-spiral-matrix.apl`](examples/1127-spiral-matrix.apl) | قراءة مصفوفة بشكل حلزوني |
| 1128 | [`1128-rotate-image.apl`](examples/1128-rotate-image.apl) | تدوير مصفوفة مربعة تسعين درجة |
| 1129 | [`1129-game-of-life.apl`](examples/1129-game-of-life.apl) | خطوة واحدة من لعبة الحياة |
| 1130 | [`1130-gray-code.apl`](examples/1130-gray-code.apl) | توليد تسلسل غراي |
| 1131 | [`1131-jump-game-two.apl`](examples/1131-jump-game-two.apl) | أقل عدد قفزات للوصول للنهاية |
| 1132 | [`1132-bulls-and-cows.apl`](examples/1132-bulls-and-cows.apl) | مقارنة تخمين برقم سري |
| 1133 | [`1133-partition-equal-subset.apl`](examples/1133-partition-equal-subset.apl) | هل نقسم القائمة إلى نصفين بمجموع واحد |
| 1134 | [`1134-unique-paths-obstacles.apl`](examples/1134-unique-paths-obstacles.apl) | عدد المسارات في شبكة فيها عوائق |
| 1135 | [`1135-meeting-rooms.apl`](examples/1135-meeting-rooms.apl) | أقل عدد قاعات لجدول اجتماعات |
| 1136 | [`1136-summary-ranges.apl`](examples/1136-summary-ranges.apl) | تلخيص أرقام متتالية بمجالات |
| 1137 | [`1137-missing-ranges.apl`](examples/1137-missing-ranges.apl) | إيجاد المجالات الناقصة بين حدين |
| 1138 | [`1138-remove-k-digits.apl`](examples/1138-remove-k-digits.apl) | أصغر عدد بعد حذف k رقماً |
| 1139 | [`1139-largest-number.apl`](examples/1139-largest-number.apl) | ترتيب أرقام لتكوين أكبر عدد |
| 1140 | [`1140-find-duplicate-floyd.apl`](examples/1140-find-duplicate-floyd.apl) | إيجاد الرقم المكرر دون تعديل القائمة |
| 1141 | [`1141-integer-break.apl`](examples/1141-integer-break.apl) | أكبر حاصل ضرب لأجزاء عدد |
| 1142 | [`1142-search-2d-matrix.apl`](examples/1142-search-2d-matrix.apl) | بحث عن قيمة في مصفوفة مرتبة |
| 1143 | [`1143-star-parentheses.apl`](examples/1143-star-parentheses.apl) | صحة أقواس فيها نجمة تعمل كأي شيء |
| 1144 | [`1144-max-circular-subarray.apl`](examples/1144-max-circular-subarray.apl) | أكبر مجموع لقائمة جزئية في قائمة دائرية |
| 1145 | [`1145-wiggle-sort.apl`](examples/1145-wiggle-sort.apl) | ترتيب يتناوب بين الأصغر والأكبر |
| 1146 | [`1146-candy-crush-1d.apl`](examples/1146-candy-crush-1d.apl) | إزالة ثلاثة متتالية فأكثر من نفس النوع |
| 1147 | [`1147-task-scheduler-cooldown.apl`](examples/1147-task-scheduler-cooldown.apl) | أقل وقت لتنفيذ مهام مع فترة تبريد |
| 1148 | [`1148-subarray-product-less.apl`](examples/1148-subarray-product-less.apl) | عدّ القوائم الجزئية بجداء أقل من k |
| 1149 | [`1149-sum-of-squares.apl`](examples/1149-sum-of-squares.apl) | هل العدد مجموع مربعين |
| 1150 | [`1150-longest-turbulent.apl`](examples/1150-longest-turbulent.apl) | أطول قائمة جزئية تتناوب فيها المقارنات |
| 1151 | [`1151-squares-of-digits-cycle.apl`](examples/1151-squares-of-digits-cycle.apl) | طول الدورة في مربعات أرقام العدد |
| 1152 | [`1152-kth-smallest-matrix.apl`](examples/1152-kth-smallest-matrix.apl) | العنصر ذو الترتيب k في مصفوفة مرتبة |
| 1153 | [`1153-two-sum-sorted.apl`](examples/1153-two-sum-sorted.apl) | زوج مجموعه هدف في قائمة مرتبة |
| 1154 | [`1154-three-sum.apl`](examples/1154-three-sum.apl) | ثلاثيات مجموعها صفر |
| 1155 | [`1155-four-sum-count.apl`](examples/1155-four-sum-count.apl) | عدد رباعيات مجموعها صفر من أربع قوائم |
| 1156 | [`1156-sort-by-frequency.apl`](examples/1156-sort-by-frequency.apl) | ترتيب الحروف حسب عدد تكرارها |
| 1157 | [`1157-top-k-frequent.apl`](examples/1157-top-k-frequent.apl) | أكثر k عناصر تكراراً |
| 1158 | [`1158-group-anagrams-key.apl`](examples/1158-group-anagrams-key.apl) | تجميع الكلمات التي لها نفس الحروف |
| 1159 | [`1159-isomorphic-groups.apl`](examples/1159-isomorphic-groups.apl) | توقيع يعرف نمط تكرار الحروف في الكلمة |
| 1160 | [`1160-longest-substring-k-distinct.apl`](examples/1160-longest-substring-k-distinct.apl) | أطول نص جزئي بحد أقصى k حرفاً مختلفاً |
| 1161 | [`1161-fruit-baskets.apl`](examples/1161-fruit-baskets.apl) | أطول مقطع بنوعين من الفاكهة |
| 1162 | [`1162-min-window-substring.apl`](examples/1162-min-window-substring.apl) | أصغر نص جزئي يحوي كل حروف نمط |
| 1163 | [`1163-valid-sudoku-board.apl`](examples/1163-valid-sudoku-board.apl) | التحقق من صحة لوحة سودوكو جزئية |
| 1164 | [`1164-longest-common-subarray.apl`](examples/1164-longest-common-subarray.apl) | أطول مقطع متصل مشترك بين قائمتين |
| 1165 | [`1165-distinct-subsequences.apl`](examples/1165-distinct-subsequences.apl) | عدد طرق تكوين نص هدف كمتتالية من نص |
| 1166 | [`1166-wildcard-matching.apl`](examples/1166-wildcard-matching.apl) | مطابقة نص بنمط فيه ? و * |
| 1167 | [`1167-regex-matching-dp.apl`](examples/1167-regex-matching-dp.apl) | مطابقة نص بنمط فيه . و * |
| 1168 | [`1168-burst-balloons.apl`](examples/1168-burst-balloons.apl) | أقصى عملات من تفجير البالونات |
| 1169 | [`1169-palindrome-pairs-count.apl`](examples/1169-palindrome-pairs-count.apl) | أزواج كلمات يكوّن لصقها كلمة متناظرة |
| 1170 | [`1170-shortest-palindrome.apl`](examples/1170-shortest-palindrome.apl) | إضافة أقل حروف في البداية لنص ليصير متناظراً |
| 1171 | [`1171-count-palindromic-substrings.apl`](examples/1171-count-palindromic-substrings.apl) | عدد النصوص الجزئية المتناظرة |
| 1172 | [`1172-longest-palindromic-substring-center.apl`](examples/1172-longest-palindromic-substring-center.apl) | أطول نص جزئي متناظر |
| 1173 | [`1173-sliding-window-median.apl`](examples/1173-sliding-window-median.apl) | وسيط كل نافذة بطول k |
| 1174 | [`1174-median-two-sorted.apl`](examples/1174-median-two-sorted.apl) | وسيط قائمتين مرتبتين |
| 1175 | [`1175-running-median-stream.apl`](examples/1175-running-median-stream.apl) | وسيط بعد كل رقم جديد |
| 1176 | [`1176-meeting-scheduler-slot.apl`](examples/1176-meeting-scheduler-slot.apl) | أول فترة مشتركة بين جدولين |
| 1177 | [`1177-interval-intersections.apl`](examples/1177-interval-intersections.apl) | تقاطع قائمتين من المجالات |
| 1178 | [`1178-insert-interval.apl`](examples/1178-insert-interval.apl) | إدراج مجال جديد ودمج ما يتداخل |
| 1179 | [`1179-non-overlapping-intervals.apl`](examples/1179-non-overlapping-intervals.apl) | أقل حذف لتصبح المجالات غير متداخلة |
| 1180 | [`1180-min-arrows-balloons.apl`](examples/1180-min-arrows-balloons.apl) | أقل سهام لتفجير بالونات |
| 1181 | [`1181-car-fleet.apl`](examples/1181-car-fleet.apl) | عدد الأساطيل التي تصل للهدف |
| 1182 | [`1182-asteroid-field-sim.apl`](examples/1182-asteroid-field-sim.apl) | محاكاة تصادم الكويكبات |
| 1183 | [`1183-decode-string-nested.apl`](examples/1183-decode-string-nested.apl) | فك صيغة k[نص] المتداخلة |
| 1184 | [`1184-basic-calculator.apl`](examples/1184-basic-calculator.apl) | تقييم عبارة فيها جمع وطرح وأقواس |
| 1185 | [`1185-basic-calculator-two.apl`](examples/1185-basic-calculator-two.apl) | تقييم عبارة فيها أربع عمليات |
| 1186 | [`1186-evaluate-rpn.apl`](examples/1186-evaluate-rpn.apl) | تقييم عبارة بصيغة البوستفيكس |
| 1187 | [`1187-infix-to-postfix.apl`](examples/1187-infix-to-postfix.apl) | تحويل عبارة وسطية إلى لاحقة |
| 1188 | [`1188-min-remove-valid-parens.apl`](examples/1188-min-remove-valid-parens.apl) | حذف أقل عدد أقواس لتصير العبارة صالحة |
| 1189 | [`1189-score-of-parentheses.apl`](examples/1189-score-of-parentheses.apl) | حساب درجة عبارة أقواس متوازنة |
| 1190 | [`1190-lfu-cache.apl`](examples/1190-lfu-cache.apl) | ذاكرة تطرد الأقل استخداماً |
| 1191 | [`1191-all-oone.apl`](examples/1191-all-oone.apl) | زيادة ونقصان مفاتيح مع أكبر وأصغر عدّاد |
| 1192 | [`1192-design-twitter.apl`](examples/1192-design-twitter.apl) | نشر ومتابعة وخلاصة أحدث عشر تغريدات |
| 1193 | [`1193-file-system-tree.apl`](examples/1193-file-system-tree.apl) | مجلدات وملفات في الذاكرة |
| 1194 | [`1194-shortest-path-binary-matrix.apl`](examples/1194-shortest-path-binary-matrix.apl) | أقصر مسار بثماني اتجاهات |
| 1195 | [`1195-rotting-oranges.apl`](examples/1195-rotting-oranges.apl) | دقائق لتعفن كل البرتقال |
| 1196 | [`1196-walls-and-gates.apl`](examples/1196-walls-and-gates.apl) | مسافة كل غرفة لأقرب بوابة |
| 1197 | [`1197-surrounded-regions.apl`](examples/1197-surrounded-regions.apl) | قلب الخانات المحاصرة بالجدران |
| 1198 | [`1198-pacific-atlantic.apl`](examples/1198-pacific-atlantic.apl) | خانات يصل ماؤها للمحيطين |
| 1199 | [`1199-clone-graph-copy.apl`](examples/1199-clone-graph-copy.apl) | نسخ رسم بياني مع التحقق من الاستقلال |
| 1200 | [`1200-course-schedule-order.apl`](examples/1200-course-schedule-order.apl) | ترتيب دراسة مقررات لها متطلبات |
| 1201 | [`1201-redundant-connection.apl`](examples/1201-redundant-connection.apl) | الحافة التي تكوّن حلقة في شجرة |
| 1202 | [`1202-number-of-provinces.apl`](examples/1202-number-of-provinces.apl) | عدد المجموعات المتصلة في مصفوفة صلات |
| 1203 | [`1203-accounts-merge.apl`](examples/1203-accounts-merge.apl) | دمج حسابات تشترك في بريد |
| 1204 | [`1204-tree-max-depth-list.apl`](examples/1204-tree-max-depth-list.apl) | عمق شجرة ثنائية ممثلة بقوائم |
| 1205 | [`1205-tree-level-order-list.apl`](examples/1205-tree-level-order-list.apl) | قراءة الشجرة مستوى مستوى |
| 1206 | [`1206-tree-zigzag-order.apl`](examples/1206-tree-zigzag-order.apl) | قراءة مستويات الشجرة بالتناوب |
| 1207 | [`1207-tree-path-sum.apl`](examples/1207-tree-path-sum.apl) | هل يوجد مسار من الجذر لورقة بمجموع معين |
| 1208 | [`1208-tree-all-paths.apl`](examples/1208-tree-all-paths.apl) | كل مسارات الجذر إلى الأوراق |
| 1209 | [`1209-tree-lca.apl`](examples/1209-tree-lca.apl) | أقرب سلف مشترك في شجرة بحث ثنائية |
| 1210 | [`1210-tree-symmetric.apl`](examples/1210-tree-symmetric.apl) | هل الشجرة صورة مرآة لنفسها |
| 1211 | [`1211-tree-invert.apl`](examples/1211-tree-invert.apl) | تبديل الفرعين الأيسر والأيمن في كل عقدة |
| 1212 | [`1212-tree-diameter-list.apl`](examples/1212-tree-diameter-list.apl) | أطول مسار بين أي عقدتين |
| 1213 | [`1213-tree-serialize.apl`](examples/1213-tree-serialize.apl) | تحويل شجرة إلى نص وإعادتها |
| 1214 | [`1214-build-tree-preorder-inorder.apl`](examples/1214-build-tree-preorder-inorder.apl) | إعادة بناء شجرة من القراءتين المسبقة والمتوسطة |
| 1215 | [`1215-sorted-list-to-bst.apl`](examples/1215-sorted-list-to-bst.apl) | بناء شجرة بحث متوازنة من قائمة مرتبة |
| 1216 | [`1216-bst-validate.apl`](examples/1216-bst-validate.apl) | هل الشجرة شجرة بحث صحيحة |
| 1217 | [`1217-bst-kth-smallest.apl`](examples/1217-bst-kth-smallest.apl) | العنصر ذو الترتيب k في شجرة بحث |
| 1218 | [`1218-bst-insert-delete.apl`](examples/1218-bst-insert-delete.apl) | إدراج وحذف في شجرة بحث ثنائية |
| 1219 | [`1219-single-number-two.apl`](examples/1219-single-number-two.apl) | الرقم الذي يظهر مرة بين أرقام تظهر ثلاثاً |
| 1220 | [`1220-single-number-three.apl`](examples/1220-single-number-three.apl) | الرقمان اللذان يظهران مرة بين أزواج |
| 1221 | [`1221-hamming-weight-table.apl`](examples/1221-hamming-weight-table.apl) | عدد البتات المضبوطة في عدد |
| 1222 | [`1222-reverse-bits.apl`](examples/1222-reverse-bits.apl) | عكس ترتيب بتات عدد من اثنين وثلاثين بتاً |
| 1223 | [`1223-power-of-two-check.apl`](examples/1223-power-of-two-check.apl) | التحقق من أن العدد قوة اثنين أو أربعة |
| 1224 | [`1224-subsets-bitmask.apl`](examples/1224-subsets-bitmask.apl) | توليد كل المجموعات الجزئية بقناع بتات |
| 1225 | [`1225-max-xor-pair.apl`](examples/1225-max-xor-pair.apl) | أكبر نتيجة xor بين زوج من القائمة |
| 1226 | [`1226-gcd-of-strings.apl`](examples/1226-gcd-of-strings.apl) | أكبر نص يقسم نصين بالتكرار |
| 1227 | [`1227-pow-mod-recursive.apl`](examples/1227-pow-mod-recursive.apl) | حساب a أس b بباقي m |
| 1228 | [`1228-count-primes-segment.apl`](examples/1228-count-primes-segment.apl) | عدد الأوليات أقل من n |
| 1229 | [`1229-ugly-number-two.apl`](examples/1229-ugly-number-two.apl) | العدد القبيح ذو الترتيب n |
| 1230 | [`1230-super-ugly.apl`](examples/1230-super-ugly.apl) | العدد القبيح بقائمة أوليات معطاة |
| 1231 | [`1231-kth-missing-positive.apl`](examples/1231-kth-missing-positive.apl) | الرقم الموجب المفقود ذو الترتيب k |
| 1232 | [`1232-split-array-largest-sum.apl`](examples/1232-split-array-largest-sum.apl) | تقسيم قائمة إلى m أجزاء بأصغر أكبر مجموع |
| 1233 | [`1233-koko-bananas.apl`](examples/1233-koko-bananas.apl) | أقل سرعة أكل لإنهاء الأكوام في h ساعة |
| 1234 | [`1234-ship-packages.apl`](examples/1234-ship-packages.apl) | أقل سعة سفينة لشحن الطرود خلال d يوماً |
| 1235 | [`1235-find-min-rotated-dup.apl`](examples/1235-find-min-rotated-dup.apl) | أصغر عنصر في قائمة مدورة فيها تكرار |
| 1236 | [`1236-search-insert-position.apl`](examples/1236-search-insert-position.apl) | موضع إدراج قيمة في قائمة مرتبة |
| 1237 | [`1237-longest-common-prefix-trie.apl`](examples/1237-longest-common-prefix-trie.apl) | أطول بادئة مشتركة بمقارنة الأول والأخير |
| 1238 | [`1238-valid-word-abbreviation.apl`](examples/1238-valid-word-abbreviation.apl) | هل الاختصار الرقمي يطابق الكلمة |
| 1239 | [`1239-compare-versions.apl`](examples/1239-compare-versions.apl) | مقارنة رقمي إصدارين |
| 1240 | [`1240-simplify-path.apl`](examples/1240-simplify-path.apl) | تبسيط مسار ملف فيه نقطة ونقطتان |
| 1241 | [`1241-longest-absolute-path.apl`](examples/1241-longest-absolute-path.apl) | أطول مسار لملف في نظام ملفات نصي |
| 1242 | [`1242-integer-to-english.apl`](examples/1242-integer-to-english.apl) | كتابة عدد بالكلمات الإنجليزية |
| 1243 | [`1243-count-and-say-iter.apl`](examples/1243-count-and-say-iter.apl) | تسلسل عد وقل الدوري |
| 1244 | [`1244-multiply-strings-big.apl`](examples/1244-multiply-strings-big.apl) | ضرب عددين كبيرين مخزنين كأرقام |
| 1245 | [`1245-add-two-digit-lists.apl`](examples/1245-add-two-digit-lists.apl) | جمع عددين مخزنين رقماً رقماً بترتيب معكوس |
| 1246 | [`1246-fraction-to-decimal.apl`](examples/1246-fraction-to-decimal.apl) | تحويل كسر إلى عدد عشري مع الدورة بين قوسين |
| 1247 | [`1247-ones-and-zeroes.apl`](examples/1247-ones-and-zeroes.apl) | أكبر مجموعة نصوص ضمن حد أصفار وآحاد |
| 1248 | [`1248-last-stone-weight.apl`](examples/1248-last-stone-weight.apl) | تحطيم أثقل حجرين حتى يبقى حجر |
| 1249 | [`1249-reorganize-string.apl`](examples/1249-reorganize-string.apl) | ترتيب الحروف بحيث لا يتجاور حرفان متماثلان |
| 1250 | [`1250-task-assign-workers.apl`](examples/1250-task-assign-workers.apl) | إسناد المهام الأثقل إلى الأقدر |
| 1251 | [`1251-boats-to-save.apl`](examples/1251-boats-to-save.apl) | أقل عدد قوارب بحد حمولة |
| 1252 | [`1252-assign-cookies.apl`](examples/1252-assign-cookies.apl) | أكبر عدد أطفال يرضون بالكعك |
| 1253 | [`1253-queue-reconstruction.apl`](examples/1253-queue-reconstruction.apl) | إعادة ترتيب أشخاص بحسب الطول وعدد الأطول أمامهم |
| 1254 | [`1254-minimum-cost-sticks.apl`](examples/1254-minimum-cost-sticks.apl) | وصل عصي بأقل كلفة |
| 1255 | [`1255-min-cost-climbing.apl`](examples/1255-min-cost-climbing.apl) | أقل كلفة لبلوغ قمة السلم |
| 1256 | [`1256-paint-house.apl`](examples/1256-paint-house.apl) | أقل كلفة لطلاء صف بيوت بلا لونين متجاورين |
| 1257 | [`1257-delete-and-earn.apl`](examples/1257-delete-and-earn.apl) | أقصى نقاط بحذف رقم وجيرانه |
| 1258 | [`1258-maximal-rectangle-binary.apl`](examples/1258-maximal-rectangle-binary.apl) | أكبر مستطيل من الآحاد في مصفوفة |
| 1259 | [`1259-rate-limiter-window.apl`](examples/1259-rate-limiter-window.apl) | السماح بعدد طلبات في نافذة زمنية |
| 1260 | [`1260-parking-lot-slots.apl`](examples/1260-parking-lot-slots.apl) | موقف بأحجام متعددة |
| 1261 | [`1261-elevator-sim.apl`](examples/1261-elevator-sim.apl) | مصعد يخدم طلبات بالترتيب |
| 1262 | [`1262-bank-transfer-ledger.apl`](examples/1262-bank-transfer-ledger.apl) | تحويلات بين حسابات مع التراجع عند الفشل |
| 1263 | [`1263-shopping-offers.apl`](examples/1263-shopping-offers.apl) | أقل سعر لقائمة مشتريات مع عروض حزم |
| 1264 | [`1264-candy-split-sim.apl`](examples/1264-candy-split-sim.apl) | توزيع حلوى بزيادة تدريجية |
| 1265 | [`1265-josephus-list.apl`](examples/1265-josephus-list.apl) | ترتيب إقصاء دائري |
| 1266 | [`1266-tic-tac-toe-winner.apl`](examples/1266-tic-tac-toe-winner.apl) | تحديد الفائز في لوحة إكس أو |
| 1267 | [`1267-minesweeper-count.apl`](examples/1267-minesweeper-count.apl) | عدد الألغام المجاورة لكل خانة |
| 1268 | [`1268-spiral-matrix-two.apl`](examples/1268-spiral-matrix-two.apl) | ملء مصفوفة بأرقام متتالية بشكل حلزوني |
| 1269 | [`1269-diagonal-traverse.apl`](examples/1269-diagonal-traverse.apl) | قراءة المصفوفة بالأقطار المتناوبة |
| 1270 | [`1270-prefix-sum-2d.apl`](examples/1270-prefix-sum-2d.apl) | مجموع منطقة في مصفوفة بزمن ثابت |
| 1271 | [`1271-difference-array.apl`](examples/1271-difference-array.apl) | تطبيق زيادات على مجالات بمسح واحد |
| 1272 | [`1272-corporate-flight-bookings.apl`](examples/1272-corporate-flight-bookings.apl) | عدد المقاعد المحجوزة لكل رحلة |
| 1273 | [`1273-car-pooling.apl`](examples/1273-car-pooling.apl) | هل تكفي سعة السيارة لكل الرحلات |
| 1274 | [`1274-range-addition-sorted.apl`](examples/1274-range-addition-sorted.apl) | أقصى تداخل بين مجالات |
| 1275 | [`1275-skyline-heights.apl`](examples/1275-skyline-heights.apl) | خط الأفق لمجموعة مباني |
| 1276 | [`1276-merge-sorted-streams.apl`](examples/1276-merge-sorted-streams.apl) | دمج عدة قوائم مرتبة |
| 1277 | [`1277-smallest-range-k-lists.apl`](examples/1277-smallest-range-k-lists.apl) | أصغر مدى يحوي رقماً من كل قائمة |
| 1278 | [`1278-kth-largest-quickselect.apl`](examples/1278-kth-largest-quickselect.apl) | العنصر ذو الترتيب k من الأكبر |
| 1279 | [`1279-sort-colors-three-way.apl`](examples/1279-sort-colors-three-way.apl) | فرز قيم من ثلاثة أنواع بمسح واحد |
| 1280 | [`1280-merge-intervals-count.apl`](examples/1280-merge-intervals-count.apl) | عدد المجالات الناتجة من دمج المتداخلة |
| 1281 | [`1281-longest-increasing-triplet.apl`](examples/1281-longest-increasing-triplet.apl) | هل توجد ثلاثة عناصر متزايدة بالترتيب |
| 1282 | [`1282-russian-doll.apl`](examples/1282-russian-doll.apl) | أكبر عدد مظاريف متداخلة |
| 1283 | [`1283-lis-count.apl`](examples/1283-lis-count.apl) | عدد المتتاليات المتزايدة الأطول |
| 1284 | [`1284-max-sum-increasing.apl`](examples/1284-max-sum-increasing.apl) | أكبر مجموع لمتتالية متزايدة |
| 1285 | [`1285-bitonic-subsequence.apl`](examples/1285-bitonic-subsequence.apl) | أطول متتالية تزداد ثم تنقص |
| 1286 | [`1286-longest-chain-pairs.apl`](examples/1286-longest-chain-pairs.apl) | أطول سلسلة أزواج متتابعة |
| 1287 | [`1287-min-deletions-sorted.apl`](examples/1287-min-deletions-sorted.apl) | أقل حذف لتصبح القائمة متزايدة |
| 1288 | [`1288-shortest-supersequence.apl`](examples/1288-shortest-supersequence.apl) | طول أقصر نص يحوي نصين كمتتاليتين |
| 1289 | [`1289-min-ascii-delete-sum.apl`](examples/1289-min-ascii-delete-sum.apl) | أقل مجموع رموز محذوفة لتساوي نصين |
| 1290 | [`1290-palindrome-removal.apl`](examples/1290-palindrome-removal.apl) | أقل حذف لتصبح السلسلة متناظرة |
| 1291 | [`1291-restore-ip-addresses.apl`](examples/1291-restore-ip-addresses.apl) | كل العناوين الصالحة من سلسلة أرقام |
| 1292 | [`1292-hash-map-design.apl`](examples/1292-hash-map-design.apl) | تنفيذ خريطة بسلاسل داخل سطول |
| 1293 | [`1293-hash-set-design.apl`](examples/1293-hash-set-design.apl) | تنفيذ مجموعة تضيف وتحذف وتفحص |
| 1294 | [`1294-my-calendar.apl`](examples/1294-my-calendar.apl) | حجز مواعيد بلا تداخل |
| 1295 | [`1295-my-calendar-two.apl`](examples/1295-my-calendar-two.apl) | السماح بحجز مزدوج ومنع الثلاثي |
| 1296 | [`1296-data-stream-first-bad.apl`](examples/1296-data-stream-first-bad.apl) | أول إصدار سيئ بأقل عدد استدعاءات |
| 1297 | [`1297-guess-higher-lower.apl`](examples/1297-guess-higher-lower.apl) | تخمين رقم بإرشادات أعلى وأقل |
| 1298 | [`1298-random-pick-weight.apl`](examples/1298-random-pick-weight.apl) | اختيار فهرس بحسب أوزانه |
| 1299 | [`1299-shuffle-array-lcg.apl`](examples/1299-shuffle-array-lcg.apl) | خلط قائمة بمولد أرقام يمكن إعادة إنتاجه |
| 1300 | [`1300-reservoir-sampling-fixed.apl`](examples/1300-reservoir-sampling-fixed.apl) | اختيار عنصر من تدفق بلا معرفة طوله |
| 1301 | [`1301-linked-list-cycle-array.apl`](examples/1301-linked-list-cycle-array.apl) | كشف حلقة في قائمة مترابطة مخزنة بمصفوفة تالي |
| 1302 | [`1302-linked-list-middle-array.apl`](examples/1302-linked-list-middle-array.apl) | عقدة المنتصف بمؤشر سريع وبطيء |
| 1303 | [`1303-reverse-linked-list-arrays.apl`](examples/1303-reverse-linked-list-arrays.apl) | عكس قائمة مخزنة بمصفوفة التالي |
| 1304 | [`1304-palindrome-linked-list.apl`](examples/1304-palindrome-linked-list.apl) | هل قائمة مترابطة متناظرة |
| 1305 | [`1305-remove-nth-from-end.apl`](examples/1305-remove-nth-from-end.apl) | حذف العنصر ذي الترتيب n من النهاية |
| 1306 | [`1306-odd-even-list.apl`](examples/1306-odd-even-list.apl) | جمع المواضع الفردية ثم الزوجية |
| 1307 | [`1307-rotate-list-right.apl`](examples/1307-rotate-list-right.apl) | تدوير قائمة k خطوة لليمين |
| 1308 | [`1308-letter-combinations-count.apl`](examples/1308-letter-combinations-count.apl) | عدد وتركيبات حروف أرقام الهاتف |
| 1309 | [`1309-permutations-unique.apl`](examples/1309-permutations-unique.apl) | التباديل المختلفة لقائمة فيها تكرار |
| 1310 | [`1310-subsets-unique.apl`](examples/1310-subsets-unique.apl) | المجموعات الجزئية المختلفة لقائمة فيها تكرار |
| 1311 | [`1311-combination-sum-two.apl`](examples/1311-combination-sum-two.apl) | تركيبات مجموعها هدف دون إعادة استخدام |
| 1312 | [`1312-combinations-k.apl`](examples/1312-combinations-k.apl) | كل اختيارات k عنصراً من n |
| 1313 | [`1313-gray-subsets-order.apl`](examples/1313-gray-subsets-order.apl) | ترتيب المجموعات بحيث يختلف كل جاران بعنصر |
| 1314 | [`1314-beautiful-arrangement.apl`](examples/1314-beautiful-arrangement.apl) | عدد الترتيبات التي يقسم فيها العدد موضعه أو العكس |
| 1315 | [`1315-matchsticks-square.apl`](examples/1315-matchsticks-square.apl) | هل تكوّن العيدان مربعاً |
| 1316 | [`1316-partition-k-subsets.apl`](examples/1316-partition-k-subsets.apl) | هل تقسم القائمة إلى k مجموعات متساوية |
| 1317 | [`1317-sudoku-solver-mini.apl`](examples/1317-sudoku-solver-mini.apl) | حل سودوكو ٤ في ٤ |
| 1318 | [`1318-target-sum-combos.apl`](examples/1318-target-sum-combos.apl) | عدد طرق وضع الإشارات لبلوغ هدف |
| 1319 | [`1319-expression-add-operators.apl`](examples/1319-expression-add-operators.apl) | وضع عمليات بين الأرقام لبلوغ هدف |
| 1320 | [`1320-rotate-matrix-in-place.apl`](examples/1320-rotate-matrix-in-place.apl) | تدوير مصفوفة بنقلها ثم عكس الصفوف |
| 1321 | [`1321-transpose-matrix.apl`](examples/1321-transpose-matrix.apl) | تبديل الصفوف والأعمدة في مصفوفة مستطيلة |
| 1322 | [`1322-toeplitz-check.apl`](examples/1322-toeplitz-check.apl) | هل كل قطر في المصفوفة ثابت |
| 1323 | [`1323-lonely-pixel.apl`](examples/1323-lonely-pixel.apl) | عدد البكسلات السوداء الوحيدة في صفها وعمودها |
| 1324 | [`1324-island-perimeter.apl`](examples/1324-island-perimeter.apl) | محيط جزيرة في شبكة |
| 1325 | [`1325-max-area-island.apl`](examples/1325-max-area-island.apl) | أكبر جزيرة في شبكة |
| 1326 | [`1326-number-of-distinct-islands.apl`](examples/1326-number-of-distinct-islands.apl) | عدد أشكال الجزر المختلفة |
| 1327 | [`1327-shortest-bridge.apl`](examples/1327-shortest-bridge.apl) | أقل عدد خانات ماء لربط جزيرتين |
| 1328 | [`1328-minimum-knight-moves.apl`](examples/1328-minimum-knight-moves.apl) | أقل عدد حركات حصان بين خانتين |
| 1329 | [`1329-open-the-lock.apl`](examples/1329-open-the-lock.apl) | أقل عدد لفات لفتح قفل رقمي |
| 1330 | [`1330-dungeon-game.apl`](examples/1330-dungeon-game.apl) | أقل صحة ابتدائية للوصول إلى الأميرة |
| 1331 | [`1331-last-stone-weight-two.apl`](examples/1331-last-stone-weight-two.apl) | أقل وزن متبق بتحطيم الأحجار |
| 1332 | [`1332-stone-game.apl`](examples/1332-stone-game.apl) | أفضل فارق نقاط للاعب الأول في لعبة أكوام |
| 1333 | [`1333-predict-the-winner.apl`](examples/1333-predict-the-winner.apl) | هل ينتهي اللاعب الأول بمجموع لا يقل عن الثاني |
| 1334 | [`1334-largest-divisible-subset.apl`](examples/1334-largest-divisible-subset.apl) | أكبر مجموعة كل زوج فيها يقبل أحدهما القسمة على الآخر |
| 1335 | [`1335-sum-subarray-minimums.apl`](examples/1335-sum-subarray-minimums.apl) | مجموع أصغر عنصر في كل مصفوفة جزئية |
| 1336 | [`1336-jump-game-three.apl`](examples/1336-jump-game-three.apl) | هل نصل إلى قيمة صفر بقفز يميناً أو يساراً |
| 1337 | [`1337-cheapest-flights-k-stops.apl`](examples/1337-cheapest-flights-k-stops.apl) | أرخص سعر بعدد محدود من التوقفات |
| 1338 | [`1338-network-delay-time.apl`](examples/1338-network-delay-time.apl) | زمن وصول إشارة من عقدة إلى كل العقد |
| 1339 | [`1339-path-min-effort.apl`](examples/1339-path-min-effort.apl) | مسار في شبكة ارتفاعات بأقل فارق أقصى بين خطوتين |
| 1340 | [`1340-longest-increasing-path-matrix.apl`](examples/1340-longest-increasing-path-matrix.apl) | أطول مسار تزداد قيمه في مصفوفة |
| 1341 | [`1341-count-sorted-vowels.apl`](examples/1341-count-sorted-vowels.apl) | عدد نصوص من حروف العلة مرتبة أبجدياً بطول معين |
| 1342 | [`1342-paint-fence.apl`](examples/1342-paint-fence.apl) | عدد طرق طلاء سور بلا ثلاثة ألواح متتالية بنفس اللون |
| 1343 | [`1343-min-refueling-stops.apl`](examples/1343-min-refueling-stops.apl) | أقل عدد محطات وقود للوصول إلى الهدف |
| 1344 | [`1344-evaluate-division.apl`](examples/1344-evaluate-division.apl) | حساب نسب بين متغيرات من معادلات معروفة |
| 1345 | [`1345-reverse-pairs-count.apl`](examples/1345-reverse-pairs-count.apl) | عدد أزواج i<j حيث العنصر الأول أكبر من ضعف الثاني |
| 1346 | [`1346-alien-dictionary-order.apl`](examples/1346-alien-dictionary-order.apl) | استنتاج ترتيب الحروف من كلمات مرتبة |
| 1347 | [`1347-possible-bipartition.apl`](examples/1347-possible-bipartition.apl) | تقسيم أشخاص إلى مجموعتين لا يتنافر أعضاء كل منهما |
| 1348 | [`1348-reconstruct-itinerary.apl`](examples/1348-reconstruct-itinerary.apl) | ترتيب تذاكر طيران في رحلة واحدة بأصغر ترتيب أبجدي |
| 1349 | [`1349-eventual-safe-states.apl`](examples/1349-eventual-safe-states.apl) | العقد التي كل مساراتها تنتهي بعقدة طرفية |
| 1350 | [`1350-swim-rising-water.apl`](examples/1350-swim-rising-water.apl) | أقل زمن للوصول من الزاوية إلى الزاوية |
| 1351 | [`1351-word-break-sentences.apl`](examples/1351-word-break-sentences.apl) | كل الجمل الممكنة بتقسيم نص إلى كلمات من قاموس |
| 1352 | [`1352-count-smaller-after-self.apl`](examples/1352-count-smaller-after-self.apl) | لكل عنصر عدد العناصر الأصغر منه على يمينه |
| 1353 | [`1353-k-closest-points.apl`](examples/1353-k-closest-points.apl) | أقرب ك نقطة إلى نقطة الأصل |
| 1354 | [`1354-min-height-trees.apl`](examples/1354-min-height-trees.apl) | جذور تعطي أقل ارتفاع لشجرة غير موجهة |
| 1355 | [`1355-prison-cells-days.apl`](examples/1355-prison-cells-days.apl) | حالة ثماني زنازين بعد عدد كبير من الأيام |
| 1356 | [`1356-champagne-tower.apl`](examples/1356-champagne-tower.apl) | كمية السائل في كأس معين في برج كؤوس |
| 1357 | [`1357-rabbits-in-forest.apl`](examples/1357-rabbits-in-forest.apl) | أقل عدد ممكن للأرانب من إجابات عددها حولها |
| 1358 | [`1358-sliding-puzzle.apl`](examples/1358-sliding-puzzle.apl) | أقل حركات لحل لغز انزلاق بثلاثة في اثنين |
| 1359 | [`1359-smallest-string-with-swaps.apl`](examples/1359-smallest-string-with-swaps.apl) | أصغر نص بتبديل أي حرفين ضمن أزواج مسموحة |
| 1360 | [`1360-number-of-islands.apl`](examples/1360-number-of-islands.apl) | عدد الجزر المتصلة أفقياً ورأسياً في شبكة |
| 1361 | [`1361-max-consecutive-ones-three.apl`](examples/1361-max-consecutive-ones-three.apl) | أطول سلسلة آحاد بقلب عدد محدود من الأصفار |
| 1362 | [`1362-subarrays-k-different.apl`](examples/1362-subarrays-k-different.apl) | عدد المصفوفات الجزئية التي فيها ك قيمة مختلفة بالضبط |
| 1363 | [`1363-permutation-in-string.apl`](examples/1363-permutation-in-string.apl) | هل يحتوي نص على تبديل لنص آخر |
| 1364 | [`1364-longest-repeating-replacement.apl`](examples/1364-longest-repeating-replacement.apl) | أطول نص متماثل الحروف بعد ك استبدال |
| 1365 | [`1365-partition-stable.apl`](examples/1365-partition-stable.apl) | نقل العناصر الأصغر من محور للأمام مع حفظ الترتيب |
| 1366 | [`1366-remove-duplicate-letters.apl`](examples/1366-remove-duplicate-letters.apl) | أصغر نص بترتيب أبجدي بعد حذف تكرار الحروف |
| 1367 | [`1367-pattern-one-three-two.apl`](examples/1367-pattern-one-three-two.apl) | هل توجد ثلاثة عناصر بنمط أصغر ثم أكبر ثم وسط |
| 1368 | [`1368-bus-routes-min.apl`](examples/1368-bus-routes-min.apl) | أقل عدد حافلات للوصول من محطة إلى أخرى |
| 1369 | [`1369-jump-game-four.apl`](examples/1369-jump-game-four.apl) | أقل قفزات للوصول لآخر موضع مع القفز بين القيم المتساوية |
| 1370 | [`1370-guess-number-cost.apl`](examples/1370-guess-number-cost.apl) | أقل مال يضمن الفوز في لعبة التخمين |
| 1371 | [`1371-can-i-win.apl`](examples/1371-can-i-win.apl) | لعبة اختيار أرقام بدون تكرار للوصول إلى مجموع |
| 1372 | [`1372-rectangle-area-union.apl`](examples/1372-rectangle-area-union.apl) | مساحة اتحاد مستطيلين متوازيي الأضلاع مع المحاور |
| 1373 | [`1373-poor-pigs.apl`](examples/1373-poor-pigs.apl) | أقل عدد خنازير لإيجاد الدلو المسموم |
| 1374 | [`1374-stone-game-two.apl`](examples/1374-stone-game-two.apl) | أقصى حجارة للاعب الأول عندما يأخذ حتى ضعف م أكوام |
| 1375 | [`1375-flip-game-moves.apl`](examples/1375-flip-game-moves.apl) | كل الحالات التالية بقلب علامتين متجاورتين |
| 1376 | [`1376-subarray-sums-divisible.apl`](examples/1376-subarray-sums-divisible.apl) | عدد المصفوفات الجزئية التي يقبل مجموعها القسمة على ك |
| 1377 | [`1377-max-stack-ops.apl`](examples/1377-max-stack-ops.apl) | مكدس يدعم أعلى وأقصى وحذف الأقصى |
| 1378 | [`1378-paint-house-k-colors.apl`](examples/1378-paint-house-k-colors.apl) | أقل تكلفة لطلاء صف بيوت بلا لونين متجاورين متماثلين |
| 1379 | [`1379-min-cost-tickets.apl`](examples/1379-min-cost-tickets.apl) | أقل تكلفة لتذاكر يوم وأسبوع وشهر تغطي أيام سفر |
| 1380 | [`1380-longest-arithmetic-subsequence.apl`](examples/1380-longest-arithmetic-subsequence.apl) | أطول متتالية جزئية بفارق ثابت |
| 1381 | [`1381-arithmetic-slices-count.apl`](examples/1381-arithmetic-slices-count.apl) | عدد المصفوفات الجزئية الحسابية بطول ثلاثة فأكثر |
| 1382 | [`1382-wiggle-subsequence-length.apl`](examples/1382-wiggle-subsequence-length.apl) | أطول متتالية جزئية فروقها تتناوب بين موجب وسالب |
| 1383 | [`1383-best-sightseeing-pair.apl`](examples/1383-best-sightseeing-pair.apl) | أكبر قيمة لزوج بحسب قيمتيهما والمسافة بينهما |
| 1384 | [`1384-maximum-gap-sorted.apl`](examples/1384-maximum-gap-sorted.apl) | أكبر فرق بين عنصرين متجاورين بعد الفرز |
| 1385 | [`1385-good-triplets-count.apl`](examples/1385-good-triplets-count.apl) | عدد الثلاثيات التي فروقها ضمن حدود معينة |
| 1386 | [`1386-harmonic-fraction.apl`](examples/1386-harmonic-fraction.apl) | مجموع مقلوبات الأعداد حتى ن ككسر مختزل |
| 1387 | [`1387-digit-factorials.apl`](examples/1387-digit-factorials.apl) | أعداد تساوي مجموع مضروبات أرقامها |
| 1388 | [`1388-spiral-diagonals-sum.apl`](examples/1388-spiral-diagonals-sum.apl) | مجموع قطري لولب أعداد بحجم فردي |
| 1389 | [`1389-lattice-paths-count.apl`](examples/1389-lattice-paths-count.apl) | عدد مسارات يمين وأسفل في شبكة مربعة |
| 1390 | [`1390-sum-of-multiples-below.apl`](examples/1390-sum-of-multiples-below.apl) | مجموع مضاعفات 3 و5 تحت حد معين |
| 1391 | [`1391-even-fibonacci-sum.apl`](examples/1391-even-fibonacci-sum.apl) | مجموع حدود فيبوناتشي الزوجية حتى حد |
| 1392 | [`1392-pandigital-check.apl`](examples/1392-pandigital-check.apl) | هل يحتوي عدد كل الأرقام من 1 إلى ن مرة واحدة |
| 1393 | [`1393-truncatable-primes.apl`](examples/1393-truncatable-primes.apl) | أعداد أولية تبقى أولية عند بتر أرقامها من الجهتين |
| 1394 | [`1394-circular-primes.apl`](examples/1394-circular-primes.apl) | أعداد أولية تبقى أولية بتدوير أرقامها |
| 1395 | [`1395-power-digit-sum.apl`](examples/1395-power-digit-sum.apl) | مجموع أرقام العدد 2 مرفوعاً لقوة |
| 1396 | [`1396-factorial-digit-sum.apl`](examples/1396-factorial-digit-sum.apl) | مجموع أرقام مضروب عدد |
| 1397 | [`1397-palindromic-product.apl`](examples/1397-palindromic-product.apl) | أكبر عدد متماثل يساوي حاصل ضرب عددين بعدد أرقام معين |
| 1398 | [`1398-smallest-multiple-lcm.apl`](examples/1398-smallest-multiple-lcm.apl) | أصغر عدد يقبل القسمة على كل الأعداد من 1 إلى ن |
| 1399 | [`1399-sum-square-difference.apl`](examples/1399-sum-square-difference.apl) | الفرق بين مربع المجموع ومجموع المربعات |
| 1400 | [`1400-triangle-number-divisors.apl`](examples/1400-triangle-number-divisors.apl) | أول عدد مثلثي له أكثر من عدد معين من القواسم |
| 1401 | [`1401-pentagonal-numbers.apl`](examples/1401-pentagonal-numbers.apl) | توليد الأعداد الخماسية واختبار الانتماء |
| 1402 | [`1402-goldbach-other-conjecture.apl`](examples/1402-goldbach-other-conjecture.apl) | أول عدد فردي مركب لا يساوي أولياً زائد ضعف مربع |
| 1403 | [`1403-longest-collatz-start.apl`](examples/1403-longest-collatz-start.apl) | العدد البادئ الذي يعطي أطول سلسلة كولاتز تحت حد |
| 1404 | [`1404-polygonal-numbers.apl`](examples/1404-polygonal-numbers.apl) | الحد ن من الأعداد المضلعة لعدد أضلاع ك |
| 1405 | [`1405-smallest-repunit-divisor.apl`](examples/1405-smallest-repunit-divisor.apl) | أقل طول لعدد كله آحاد يقبل القسمة على ك |
| 1406 | [`1406-multiplicative-persistence.apl`](examples/1406-multiplicative-persistence.apl) | عدد المرات لضرب الأرقام حتى يبقى رقم واحد |
| 1407 | [`1407-sum-of-divisors-sigma.apl`](examples/1407-sum-of-divisors-sigma.apl) | مجموع كل قواسم عدد بما فيها نفسه |
| 1408 | [`1408-champernowne-digit.apl`](examples/1408-champernowne-digit.apl) | الرقم ذو الترتيب ن في تسلسل الأعداد الصحيحة المتتالية |
| 1409 | [`1409-longest-uncommon-subsequence.apl`](examples/1409-longest-uncommon-subsequence.apl) | أطول متتالية جزئية موجودة في نص واحد فقط |
| 1410 | [`1410-reverse-each-word.apl`](examples/1410-reverse-each-word.apl) | عكس حروف كل كلمة مع بقاء ترتيب الكلمات |
| 1411 | [`1411-buddy-strings.apl`](examples/1411-buddy-strings.apl) | هل يتساوى النصان بتبديل حرفين في أحدهما |
| 1412 | [`1412-backspace-compare.apl`](examples/1412-backspace-compare.apl) | مقارنة نصين حيث العلامة # تمسح الحرف السابق |
| 1413 | [`1413-keyboard-row-words.apl`](examples/1413-keyboard-row-words.apl) | كلمات تكتب كلها من صف واحد في لوحة المفاتيح |
| 1414 | [`1414-reverse-string-k-groups.apl`](examples/1414-reverse-string-k-groups.apl) | عكس أول ك حرف من كل 2ك حرف |
| 1415 | [`1415-student-attendance-record.apl`](examples/1415-student-attendance-record.apl) | هل يستحق الطالب الجائزة بحسب غيابه وتأخره |
| 1416 | [`1416-long-pressed-name.apl`](examples/1416-long-pressed-name.apl) | هل نص مكتوب هو الاسم مع ضغط بعض الحروف طويلاً |
| 1417 | [`1417-di-string-match.apl`](examples/1417-di-string-match.apl) | تبديل يوافق نمط الزيادة والنقصان |
| 1418 | [`1418-shortest-completing-word.apl`](examples/1418-shortest-completing-word.apl) | أقصر كلمة تحوي كل حروف لوحة الترخيص |
| 1419 | [`1419-camelcase-matching.apl`](examples/1419-camelcase-matching.apl) | هل يطابق كل استعلام نمط الأحرف الكبيرة |
| 1420 | [`1420-number-of-segments.apl`](examples/1420-number-of-segments.apl) | عدد الكلمات المفصولة بمسافات في نص |
| 1421 | [`1421-count-binary-substrings.apl`](examples/1421-count-binary-substrings.apl) | عدد المقاطع التي فيها أصفار وآحاد متتالية بعدد متساو |
| 1422 | [`1422-repeated-dna-sequences.apl`](examples/1422-repeated-dna-sequences.apl) | كل مقطع من عشرة حروف يظهر أكثر من مرة |
| 1423 | [`1423-base-seven.apl`](examples/1423-base-seven.apl) | تحويل عدد صحيح إلى النظام السباعي |
| 1424 | [`1424-add-large-strings.apl`](examples/1424-add-large-strings.apl) | جمع عددين كبيرين مكتوبين كنصين بدون تحويل |
| 1425 | [`1425-repeated-string-match.apl`](examples/1425-repeated-string-match.apl) | أقل تكرار لنص أول ليحتوي نصاً ثانياً |
| 1426 | [`1426-next-closest-time.apl`](examples/1426-next-closest-time.apl) | أقرب وقت لاحق يستخدم نفس أرقام الوقت المعطى |
| 1427 | [`1427-sentence-similarity-pairs.apl`](examples/1427-sentence-similarity-pairs.apl) | هل جملتان متشابهتان بحسب أزواج كلمات متشابهة |
| 1428 | [`1428-sort-vowels-in-string.apl`](examples/1428-sort-vowels-in-string.apl) | فرز حروف العلة في مواضعها وإبقاء الباقي |
| 1429 | [`1429-max-nesting-depth.apl`](examples/1429-max-nesting-depth.apl) | أقصى عمق لتداخل الأقواس في تعبير |
| 1430 | [`1430-remove-outer-parentheses.apl`](examples/1430-remove-outer-parentheses.apl) | حذف أقواس المستوى الأول من كل جزء أولي |
| 1431 | [`1431-heron-area.apl`](examples/1431-heron-area.apl) | مساحة مثلث من أطوال أضلاعه الثلاثة |
| 1432 | [`1432-rectangle-overlap.apl`](examples/1432-rectangle-overlap.apl) | هل يتداخل مستطيلان بمساحة موجبة |
| 1433 | [`1433-polygon-centroid.apl`](examples/1433-polygon-centroid.apl) | مركز ثقل مضلع بصيغة الحذاء |
| 1434 | [`1434-angle-type-vectors.apl`](examples/1434-angle-type-vectors.apl) | هل الزاوية بين متجهين حادة أم قائمة أم منفرجة |
| 1435 | [`1435-rotate-point-quarter.apl`](examples/1435-rotate-point-quarter.apl) | تدوير نقطة حول الأصل بمضاعفات تسعين درجة |
| 1436 | [`1436-reflect-point.apl`](examples/1436-reflect-point.apl) | انعكاس نقطة حول المحور السيني أو الصادي أو القطر |
| 1437 | [`1437-collinear-three-points.apl`](examples/1437-collinear-three-points.apl) | هل تقع ثلاث نقاط على خط مستقيم |
| 1438 | [`1438-max-points-on-line.apl`](examples/1438-max-points-on-line.apl) | أكبر عدد نقاط تقع على خط واحد |
| 1439 | [`1439-valid-square-points.apl`](examples/1439-valid-square-points.apl) | هل تشكل أربع نقاط مربعاً |
| 1440 | [`1440-convex-polygon-check.apl`](examples/1440-convex-polygon-check.apl) | هل مضلع محدب |
| 1441 | [`1441-min-area-rectangle.apl`](examples/1441-min-area-rectangle.apl) | أصغر مساحة لمستطيل أضلاعه موازية للمحاور من نقاط |
| 1442 | [`1442-largest-triangle-area.apl`](examples/1442-largest-triangle-area.apl) | أكبر مساحة لمثلث رؤوسه من مجموعة نقاط |
| 1443 | [`1443-boomerang-points.apl`](examples/1443-boomerang-points.apl) | هل ثلاث نقاط متمايزة وغير مستقيمة |
| 1444 | [`1444-manhattan-chebyshev.apl`](examples/1444-manhattan-chebyshev.apl) | مسافتان بين نقطتين على شبكة |
| 1445 | [`1445-line-slope-reduced.apl`](examples/1445-line-slope-reduced.apl) | ميل خط يمر بنقطتين ككسر مختزل |
| 1446 | [`1446-point-line-side.apl`](examples/1446-point-line-side.apl) | هل تقع نقطة يسار خط موجه أو يمينه أو عليه |
| 1447 | [`1447-lattice-points-on-segment.apl`](examples/1447-lattice-points-on-segment.apl) | عدد النقاط الصحيحة على قطعة مستقيمة بين نقطتين |
| 1448 | [`1448-pick-theorem-interior.apl`](examples/1448-pick-theorem-interior.apl) | عدد النقاط الشبكية داخل مضلع شبكي |
| 1449 | [`1449-bounding-box-points.apl`](examples/1449-bounding-box-points.apl) | أصغر مستطيل يحيط بمجموعة نقاط |
| 1450 | [`1450-ulam-spiral-position.apl`](examples/1450-ulam-spiral-position.apl) | إحداثيات العدد ن في لولب مربع يبدأ من الأصل |
| 1451 | [`1451-single-server-queue.apl`](examples/1451-single-server-queue.apl) | متوسط انتظار العملاء أمام شباك واحد |
| 1452 | [`1452-robot-bounded-circle.apl`](examples/1452-robot-bounded-circle.apl) | هل يبقى الروبوت في مسار محدود إذا كرر التعليمات |
| 1453 | [`1453-dice-sum-distribution.apl`](examples/1453-dice-sum-distribution.apl) | عدد طرق كل مجموع عند رمي نردين |
| 1454 | [`1454-english-ordinal-suffix.apl`](examples/1454-english-ordinal-suffix.apl) | إضافة st أو nd أو rd أو th للرقم |
| 1455 | [`1455-fibonacci-word-build.apl`](examples/1455-fibonacci-word-build.apl) | كلمة تبنى بدمج الكلمتين السابقتين |
| 1456 | [`1456-bit-count-kernighan.apl`](examples/1456-bit-count-kernighan.apl) | عدد الآحاد في التمثيل الثنائي |
| 1457 | [`1457-swap-with-xor.apl`](examples/1457-swap-with-xor.apl) | تبديل بلا متغير ثالث |
| 1458 | [`1458-csv-line-split.apl`](examples/1458-csv-line-split.apl) | فصل الحقول مع احترام علامات الاقتباس |
| 1459 | [`1459-thermostat-hysteresis.apl`](examples/1459-thermostat-hysteresis.apl) | تشغيل وإيقاف المكيف دون تذبذب |
| 1460 | [`1460-tiered-discount.apl`](examples/1460-tiered-discount.apl) | سعر الوحدة يقل كلما زادت الكمية |
| 1461 | [`1461-income-tax-brackets.apl`](examples/1461-income-tax-brackets.apl) | الضريبة تتصاعد بحسب شريحة كل جزء من الدخل |
| 1462 | [`1462-clock-hands-angle.apl`](examples/1462-clock-hands-angle.apl) | أصغر زاوية بين عقرب الساعات والدقائق |
| 1463 | [`1463-seconds-to-clock.apl`](examples/1463-seconds-to-clock.apl) | تحويل عدد الثواني إلى صيغة ساعة |
| 1464 | [`1464-age-in-days.apl`](examples/1464-age-in-days.apl) | عدد الأيام بين تاريخين بلا مكتبات |
| 1465 | [`1465-next-calendar-day.apl`](examples/1465-next-calendar-day.apl) | حساب التاريخ بعد يوم واحد |
| 1466 | [`1466-score-ranking-ties.apl`](examples/1466-score-ranking-ties.apl) | اللاعبون بنفس النتيجة يأخذون نفس المركز |
| 1467 | [`1467-league-points-table.apl`](examples/1467-league-points-table.apl) | نقاط الفوز ثلاث والتعادل واحدة |
| 1468 | [`1468-knockout-bracket-rounds.apl`](examples/1468-knockout-bracket-rounds.apl) | عدد المباريات والجولات لعدد فرق معين |
| 1469 | [`1469-next-bus-arrival.apl`](examples/1469-next-bus-arrival.apl) | أقرب حافلة بعد وقت الوصول |
| 1470 | [`1470-greedy-word-wrap.apl`](examples/1470-greedy-word-wrap.apl) | توزيع كلمات على أسطر بعرض أقصى |
| 1471 | [`1471-center-text-padding.apl`](examples/1471-center-text-padding.apl) | وضع النص في منتصف عرض معين |
| 1472 | [`1472-camel-to-snake-case.apl`](examples/1472-camel-to-snake-case.apl) | تحويل أسماء المتغيرات بين الأنماط |
| 1473 | [`1473-title-to-slug.apl`](examples/1473-title-to-slug.apl) | تحويل عنوان إلى رابط بحروف صغيرة وشرطات |
| 1474 | [`1474-number-to-english-words.apl`](examples/1474-number-to-english-words.apl) | كتابة الأعداد حتى الآلاف بالإنجليزية |
| 1475 | [`1475-unit-conversion-chain.apl`](examples/1475-unit-conversion-chain.apl) | كل وحدة تُحول إلى المتر أولاً |
| 1476 | [`1476-anti-diagonal-sum.apl`](examples/1476-anti-diagonal-sum.apl) | مجموع القطر الرئيسي والثانوي دون عد المركز مرتين |
| 1477 | [`1477-matrix-trace-value.apl`](examples/1477-matrix-trace-value.apl) | مجموع عناصر القطر الرئيسي |
| 1478 | [`1478-identity-matrix-check.apl`](examples/1478-identity-matrix-check.apl) | القطر آحاد وما عداه أصفار |
| 1479 | [`1479-matrix-saddle-point.apl`](examples/1479-matrix-saddle-point.apl) | عنصر أصغر ما في صفه وأكبر ما في عموده |
| 1480 | [`1480-row-and-column-sums.apl`](examples/1480-row-and-column-sums.apl) | جمع كل صف وكل عمود في مرور واحد |
| 1481 | [`1481-pascal-triangle-row.apl`](examples/1481-pascal-triangle-row.apl) | الصف رقم ن بدون بناء كل المثلث |
| 1482 | [`1482-wave-sort-array.apl`](examples/1482-wave-sort-array.apl) | مصفوفة تتبادل فيها القمم والقيعان |
| 1483 | [`1483-gnome-sort-steps.apl`](examples/1483-gnome-sort-steps.apl) | فرز ببساطة: تقدم إن صح الترتيب وإلا بدل وارجع |
| 1484 | [`1484-cocktail-shaker-sort.apl`](examples/1484-cocktail-shaker-sort.apl) | فقاعات تذهب وتعود في الاتجاهين |
| 1485 | [`1485-comb-sort-gap.apl`](examples/1485-comb-sort-gap.apl) | فرز بفجوة تتقلص تدريجياً |
| 1486 | [`1486-stooge-sort-recursive.apl`](examples/1486-stooge-sort-recursive.apl) | فرز تراجعي بطيء لكنه يعمل |
| 1487 | [`1487-is-sorted-check.apl`](examples/1487-is-sorted-check.apl) | فحص الترتيب التصاعدي أو التنازلي |
| 1488 | [`1488-partition-around-pivot.apl`](examples/1488-partition-around-pivot.apl) | الأصغر يسار والأكبر يمين |
| 1489 | [`1489-ackermann-function.apl`](examples/1489-ackermann-function.apl) | دالة تراجعية تنمو بسرعة هائلة |
| 1490 | [`1490-even-odd-mutual.apl`](examples/1490-even-odd-mutual.apl) | دالتان تستدعي كل منهما الأخرى |
| 1491 | [`1491-nested-list-depth.apl`](examples/1491-nested-list-depth.apl) | أقصى مستوى تداخل في قائمة |
| 1492 | [`1492-query-string-parse.apl`](examples/1492-query-string-parse.apl) | تحويل a=1&b=2 إلى قاموس |
| 1493 | [`1493-time-string-parse.apl`](examples/1493-time-string-parse.apl) | تحويل 14:30 إلى دقائق مع التحقق |
| 1494 | [`1494-ipv4-address-valid.apl`](examples/1494-ipv4-address-valid.apl) | أربعة أجزاء كل منها من 0 إلى 255 |
| 1495 | [`1495-mac-address-valid.apl`](examples/1495-mac-address-valid.apl) | ستة أزواج سداسية عشرية |
| 1496 | [`1496-phone-number-format.apl`](examples/1496-phone-number-format.apl) | تجميع الأرقام في أجزاء مقروءة |
| 1497 | [`1497-lucky-numbers-matrix.apl`](examples/1497-lucky-numbers-matrix.apl) | أصغر في صفه وأكبر في عموده |
| 1498 | [`1498-subset-sum-count.apl`](examples/1498-subset-sum-count.apl) | كم مجموعة جزئية مجموعها قيمة معينة |
| 1499 | [`1499-blackjack-hand-score.apl`](examples/1499-blackjack-hand-score.apl) | حساب قيمة اليد مع احتساب الآص بأحد أو أحد عشر |
| 1500 | [`1500-tennis-game-score.apl`](examples/1500-tennis-game-score.apl) | من عدد نقاط كل لاعب إلى النتيجة المعلنة |
| 1501 | [`1501-fisher-yates-lcg.apl`](examples/1501-fisher-yates-lcg.apl) | خلط يمكن إعادته لأن المولد محدد البذرة |
| 1502 | [`1502-longest-coin-streak.apl`](examples/1502-longest-coin-streak.apl) | أطول تتابع لنفس الوجه |
| 1503 | [`1503-queen-attack-check.apl`](examples/1503-queen-attack-check.apl) | هل يهاجم الوزير خانة معينة |
| 1504 | [`1504-king-moves-count.apl`](examples/1504-king-moves-count.apl) | كم خانة يستطيع الملك الوصول إليها |
| 1505 | [`1505-atbash-cipher-text.apl`](examples/1505-atbash-cipher-text.apl) | قلب الأبجدية: الأول يصبح الأخير |
| 1506 | [`1506-a1z26-cipher.apl`](examples/1506-a1z26-cipher.apl) | كل حرف يمثله ترتيبه في الأبجدية |
| 1507 | [`1507-integer-to-binary-string.apl`](examples/1507-integer-to-binary-string.apl) | كتابة عدد بالنظام الثنائي بالقسمة المتكررة |
| 1508 | [`1508-hex-digits-encode.apl`](examples/1508-hex-digits-encode.apl) | تحويل عدد إلى نظام 16 بأرقامه وحروفه |
| 1509 | [`1509-delta-encode-list.apl`](examples/1509-delta-encode-list.apl) | تخزين الفرق بين كل عنصرين متتاليين |
| 1510 | [`1510-run-length-decode-string.apl`](examples/1510-run-length-decode-string.apl) | من 3a2b إلى aaabb |
| 1511 | [`1511-simple-interest-total.apl`](examples/1511-simple-interest-total.apl) | المبلغ بعد فترة بنسبة ثابتة على الأصل |
| 1512 | [`1512-net-present-value.apl`](examples/1512-net-present-value.apl) | قيمة تدفقات مستقبلية اليوم |
| 1513 | [`1513-straight-line-depreciation.apl`](examples/1513-straight-line-depreciation.apl) | قيمة الأصل بعد سنوات بإهلاك ثابت |
| 1514 | [`1514-break-even-units.apl`](examples/1514-break-even-units.apl) | كم وحدة يجب بيعها لتغطية التكاليف |
| 1515 | [`1515-markup-vs-margin.apl`](examples/1515-markup-vs-margin.apl) | الفرق بين نسبة الزيادة ونسبة الربح من البيع |
| 1516 | [`1516-atm-notes-dispense.apl`](examples/1516-atm-notes-dispense.apl) | أقل عدد أوراق لمبلغ معين |
| 1517 | [`1517-invoice-total-with-vat.apl`](examples/1517-invoice-total-with-vat.apl) | مجموع البنود ثم ضريبة القيمة المضافة |
| 1518 | [`1518-late-fee-days.apl`](examples/1518-late-fee-days.apl) | فترة سماح ثم غرامة يومية بحد أقصى |
| 1519 | [`1519-arabic-letter-count.apl`](examples/1519-arabic-letter-count.apl) | نتجاهل المسافات وعلامات الترقيم |
| 1520 | [`1520-abjad-numeral-value.apl`](examples/1520-abjad-numeral-value.apl) | كل حرف عربي له قيمة عددية في حساب الجمل |
| 1521 | [`1521-vowel-consonant-split.apl`](examples/1521-vowel-consonant-split.apl) | فصل حروف العلة عن بقية الحروف |
| 1522 | [`1522-population-std-dev.apl`](examples/1522-population-std-dev.apl) | جذر متوسط مربعات الانحراف عن المتوسط |
| 1523 | [`1523-mode-of-list.apl`](examples/1523-mode-of-list.apl) | القيمة الأكثر تكراراً وأصغرها عند التعادل |
| 1524 | [`1524-mean-absolute-deviation.apl`](examples/1524-mean-absolute-deviation.apl) | متوسط بعد كل قيمة عن المتوسط |
| 1525 | [`1525-geometric-mean-pair.apl`](examples/1525-geometric-mean-pair.apl) | جذر حاصل ضرب القيم |
| 1526 | [`1526-z-score-of-value.apl`](examples/1526-z-score-of-value.apl) | كم انحرافاً معيارياً تبعد القيمة عن المتوسط |
| 1527 | [`1527-min-max-normalize.apl`](examples/1527-min-max-normalize.apl) | إعادة قياس القيم إلى المجال من 0 إلى 1 |
| 1528 | [`1528-histogram-buckets.apl`](examples/1528-histogram-buckets.apl) | عد القيم في مجالات متساوية العرض |
| 1529 | [`1529-running-total-list.apl`](examples/1529-running-total-list.apl) | كل عنصر مجموع ما قبله ونفسه |
| 1530 | [`1530-prefix-xor-array.apl`](examples/1530-prefix-xor-array.apl) | نتيجة XOR لكل عناصر البداية حتى كل موضع |
| 1531 | [`1531-trailing-zero-bits.apl`](examples/1531-trailing-zero-bits.apl) | عدد الأصفار على يمين آخر واحد |
| 1532 | [`1532-highest-set-bit-position.apl`](examples/1532-highest-set-bit-position.apl) | رتبة أعلى واحد في العدد |
| 1533 | [`1533-isolate-lowest-bit.apl`](examples/1533-isolate-lowest-bit.apl) | إبقاء أدنى واحد وتصفير الباقي |
| 1534 | [`1534-power-of-four-check.apl`](examples/1534-power-of-four-check.apl) | قوة اثنين موضع بتها زوجي |
| 1535 | [`1535-set-clear-toggle-bit.apl`](examples/1535-set-clear-toggle-bit.apl) | ثلاث عمليات أساسية على بت واحد |
| 1536 | [`1536-reverse-byte-bits.apl`](examples/1536-reverse-byte-bits.apl) | قلب ترتيب ثمانية بتات |
| 1537 | [`1537-range-bitwise-and.apl`](examples/1537-range-bitwise-and.apl) | نتيجة AND لكل الأعداد من م إلى ن |
| 1538 | [`1538-frequency-counter-dict.apl`](examples/1538-frequency-counter-dict.apl) | كم مرة ظهر كل عنصر |
| 1539 | [`1539-group-words-by-length.apl`](examples/1539-group-words-by-length.apl) | قاموس طول الكلمة إلى قائمة كلماتها |
| 1540 | [`1540-invert-dictionary.apl`](examples/1540-invert-dictionary.apl) | المفاتيح قيماً والقيم مفاتيح |
| 1541 | [`1541-merge-dicts-sum.apl`](examples/1541-merge-dicts-sum.apl) | المفاتيح المشتركة تُجمع قيمها |
| 1542 | [`1542-nested-dict-path-get.apl`](examples/1542-nested-dict-path-get.apl) | الوصول لقيمة عميقة بقائمة مفاتيح |
| 1543 | [`1543-deep-copy-nested-list.apl`](examples/1543-deep-copy-nested-list.apl) | نسخة لا تتأثر بتعديل الأصل |
| 1544 | [`1544-quartile-bounds.apl`](examples/1544-quartile-bounds.apl) | الربيع الأول والثالث بطريقة الوسيط |
| 1545 | [`1545-range-of-list.apl`](examples/1545-range-of-list.apl) | الفرق بين أكبر وأصغر قيمة |
| 1546 | [`1546-dot-product-3d.apl`](examples/1546-dot-product-3d.apl) | مجموع حاصل ضرب المركبات المتناظرة |
| 1547 | [`1547-cross-product-3d.apl`](examples/1547-cross-product-3d.apl) | متجه عمودي على المتجهين |
| 1548 | [`1548-vector-length-3d.apl`](examples/1548-vector-length-3d.apl) | جذر مجموع مربعات المركبات |
| 1549 | [`1549-distance-between-3d-points.apl`](examples/1549-distance-between-3d-points.apl) | جذر مجموع مربعات فروق الإحداثيات |
| 1550 | [`1550-cube-space-diagonal.apl`](examples/1550-cube-space-diagonal.apl) | القطر الذي يعبر المكعب من ركن لركن |
| 1551 | [`1551-square-pyramid-volume.apl`](examples/1551-square-pyramid-volume.apl) | ثلث مساحة القاعدة في الارتفاع |
| 1552 | [`1552-triangular-prism-volume.apl`](examples/1552-triangular-prism-volume.apl) | مساحة المثلث في طول المنشور |
| 1553 | [`1553-box-surface-area.apl`](examples/1553-box-surface-area.apl) | ستة أوجه في ثلاثة أزواج |
| 1554 | [`1554-midpoint-3d-points.apl`](examples/1554-midpoint-3d-points.apl) | متوسط كل إحداثي |
| 1555 | [`1555-centroid-of-3d-points.apl`](examples/1555-centroid-of-3d-points.apl) | متوسط إحداثيات عدة نقاط |
| 1556 | [`1556-trapezoid-area-value.apl`](examples/1556-trapezoid-area-value.apl) | نصف مجموع القاعدتين في الارتفاع |
| 1557 | [`1557-rhombus-area-diagonals.apl`](examples/1557-rhombus-area-diagonals.apl) | نصف حاصل ضرب القطرين |
| 1558 | [`1558-point-to-line-distance.apl`](examples/1558-point-to-line-distance.apl) | أقصر مسافة بين نقطة ومستقيم يمر بنقطتين |
| 1559 | [`1559-perpendicular-vectors-check.apl`](examples/1559-perpendicular-vectors-check.apl) | الجداء النقطي صفر |
| 1560 | [`1560-day-of-year-number.apl`](examples/1560-day-of-year-number.apl) | كم يوماً مضى من بداية السنة |
| 1561 | [`1561-quarter-of-year.apl`](examples/1561-quarter-of-year.apl) | أي ربع مالي يقع فيه الشهر |
| 1562 | [`1562-leap-years-between.apl`](examples/1562-leap-years-between.apl) | من غير المرور على كل سنة |
| 1563 | [`1563-month-number-to-name.apl`](examples/1563-month-number-to-name.apl) | الشهور الميلادية بأسمائها العربية |
| 1564 | [`1564-count-words-in-text.apl`](examples/1564-count-words-in-text.apl) | كلمات تفصل بينها مسافات متعددة |
| 1565 | [`1565-capitalize-each-word.apl`](examples/1565-capitalize-each-word.apl) | أول حرف من كل كلمة كبير والباقي صغير |
| 1566 | [`1566-remove-vowels-text.apl`](examples/1566-remove-vowels-text.apl) | إبقاء بقية الحروف بترتيبها |
| 1567 | [`1567-longest-word-in-text.apl`](examples/1567-longest-word-in-text.apl) | أول كلمة بأكبر طول |
| 1568 | [`1568-sum-digits-in-text.apl`](examples/1568-sum-digits-in-text.apl) | نجمع الأرقام المبعثرة في نص |
| 1569 | [`1569-swap-letter-case.apl`](examples/1569-swap-letter-case.apl) | الكبير يصير صغيراً والعكس |
| 1570 | [`1570-remove-adjacent-duplicates-stack.apl`](examples/1570-remove-adjacent-duplicates-stack.apl) | حذف زوج الحرفين المتساويين المتجاورين تكراراً |
| 1571 | [`1571-boats-to-save-people.apl`](examples/1571-boats-to-save-people.apl) | أقل عدد قوارب يحمل كل منها شخصين بحد وزن |
| 1572 | [`1572-minimum-platforms-needed.apl`](examples/1572-minimum-platforms-needed.apl) | أقصى عدد قطارات في المحطة معاً |
| 1573 | [`1573-activity-selection-count.apl`](examples/1573-activity-selection-count.apl) | أنشطة لا تتداخل بأكبر عدد ممكن |
| 1574 | [`1574-fractional-knapsack-value.apl`](examples/1574-fractional-knapsack-value.apl) | نأخذ الأعلى قيمة لكل وزن ويجوز التجزئة |
| 1575 | [`1575-hand-of-straights-check.apl`](examples/1575-hand-of-straights-check.apl) | تقسيم أرقام إلى مجموعات متتالية بحجم ثابت |
| 1576 | [`1576-monotonic-array-check.apl`](examples/1576-monotonic-array-check.apl) | تصاعدية أو تنازلية بالكامل |
| 1577 | [`1577-sliding-window-maximum-naive.apl`](examples/1577-sliding-window-maximum-naive.apl) | أكبر عنصر لكل نافذة بطول ثابت |
| 1578 | [`1578-sort-stack-with-temp.apl`](examples/1578-sort-stack-with-temp.apl) | نرتب مكدساً بمكدس إضافي واحد فقط |
| 1579 | [`1579-tiny-stack-vm.apl`](examples/1579-tiny-stack-vm.apl) | تنفيذ تعليمات push وadd وmul |
| 1580 | [`1580-bank-ledger-balance.apl`](examples/1580-bank-ledger-balance.apl) | إيداع وسحب مع رفض السحب الزائد |
| 1581 | [`1581-inventory-restock-alerts.apl`](examples/1581-inventory-restock-alerts.apl) | أصناف نزل مخزونها تحت الحد |
| 1582 | [`1582-door-state-machine.apl`](examples/1582-door-state-machine.apl) | باب يفتح ويغلق ويقفل وفق جدول انتقالات |
| 1583 | [`1583-library-overdue-fine.apl`](examples/1583-library-overdue-fine.apl) | غرامة تتضاعف بعد أسبوع |
| 1584 | [`1584-majority-element-vote.apl`](examples/1584-majority-element-vote.apl) | عنصر يظهر أكثر من نصف المرات |
| 1585 | [`1585-pair-sum-two-pointers.apl`](examples/1585-pair-sum-two-pointers.apl) | قائمة مرتبة وهدف: هل يوجد زوج مجموعه الهدف |
| 1586 | [`1586-pairs-with-given-difference.apl`](examples/1586-pairs-with-given-difference.apl) | عدد الأزواج التي فرقها قيمة محددة |
| 1587 | [`1587-intersection-of-sorted-lists.apl`](examples/1587-intersection-of-sorted-lists.apl) | العناصر المشتركة بمرور واحد |
| 1588 | [`1588-remove-duplicates-sorted-list.apl`](examples/1588-remove-duplicates-sorted-list.apl) | نبقي نسخة واحدة من كل قيمة |
| 1589 | [`1589-rotate-left-by-k.apl`](examples/1589-rotate-left-by-k.apl) | نقل أول ك عناصر إلى النهاية |
| 1590 | [`1590-contains-duplicate-set.apl`](examples/1590-contains-duplicate-set.apl) | نكتشف أول تكرار بقاموس |
| 1591 | [`1591-valid-anagram-counts.apl`](examples/1591-valid-anagram-counts.apl) | نفس الحروف بنفس التكرار |
| 1592 | [`1592-sorted-squares-two-pointers.apl`](examples/1592-sorted-squares-two-pointers.apl) | مربعات قائمة مرتبة بالأعداد السالبة |
| 1593 | [`1593-peak-element-index.apl`](examples/1593-peak-element-index.apl) | عنصر أكبر من جاريه |
| 1594 | [`1594-binary-tree-height.apl`](examples/1594-binary-tree-height.apl) | أطول مسار من الجذر إلى ورقة |
| 1595 | [`1595-tree-node-count.apl`](examples/1595-tree-node-count.apl) | العقدة الجذر مع كل عقد الفرعين |
| 1596 | [`1596-tree-leaf-count.apl`](examples/1596-tree-leaf-count.apl) | العقد التي بلا أبناء |
| 1597 | [`1597-tree-values-sum.apl`](examples/1597-tree-values-sum.apl) | نجمع قيمة كل عقدة |
| 1598 | [`1598-invert-binary-tree.apl`](examples/1598-invert-binary-tree.apl) | تبديل الابن الأيسر بالأيمن في كل عقدة |
| 1599 | [`1599-symmetric-tree-check.apl`](examples/1599-symmetric-tree-check.apl) | الشجرة صورة مرآة لنفسها |
| 1600 | [`1600-valid-bst-check.apl`](examples/1600-valid-bst-check.apl) | كل عقدة بين حدين |
| 1601 | [`1601-bst-search-value.apl`](examples/1601-bst-search-value.apl) | ننزل يساراً أو يميناً بحسب المقارنة |
| 1602 | [`1602-kth-smallest-in-bst.apl`](examples/1602-kth-smallest-in-bst.apl) | الترتيب المتوسط يعطي القيم مرتبة |
| 1603 | [`1603-lca-in-bst.apl`](examples/1603-lca-in-bst.apl) | نفترق عند أول عقدة تقع بين القيمتين |
| 1604 | [`1604-same-tree-check.apl`](examples/1604-same-tree-check.apl) | نفس الشكل ونفس القيم |
| 1605 | [`1605-tree-minimum-depth.apl`](examples/1605-tree-minimum-depth.apl) | أقصر مسار إلى ورقة |
| 1606 | [`1606-tree-from-sorted-array.apl`](examples/1606-tree-from-sorted-array.apl) | الوسط جذراً والنصفان فرعان |
| 1607 | [`1607-tree-level-order-lists.apl`](examples/1607-tree-level-order-lists.apl) | قائمة لكل مستوى بالترتيب من الأعلى |
| 1608 | [`1608-tree-right-side-view.apl`](examples/1608-tree-right-side-view.apl) | آخر عقدة في كل مستوى |
| 1609 | [`1609-tree-root-to-leaf-paths.apl`](examples/1609-tree-root-to-leaf-paths.apl) | كل المسارات الكاملة من الجذر |
| 1610 | [`1610-count-good-nodes-tree.apl`](examples/1610-count-good-nodes-tree.apl) | عقدة لا يوجد في طريقها أكبر منها |
| 1611 | [`1611-graph-node-degrees.apl`](examples/1611-graph-node-degrees.apl) | عدد الأضلاع المتصلة بكل رأس |
| 1612 | [`1612-adjacency-matrix-from-edges.apl`](examples/1612-adjacency-matrix-from-edges.apl) | 1 إذا اتصل رأسان و0 غير ذلك |
| 1613 | [`1613-connected-components-count.apl`](examples/1613-connected-components-count.apl) | كم مجموعة منفصلة من الرؤوس المتصلة |
| 1614 | [`1614-undirected-graph-has-cycle.apl`](examples/1614-undirected-graph-has-cycle.apl) | هل يحتوي الرسم على دورة |
| 1615 | [`1615-island-count-grid.apl`](examples/1615-island-count-grid.apl) | مجموعات الواحدات المتجاورة أفقياً ورأسياً |
| 1616 | [`1616-digit-lists-addition-carry.apl`](examples/1616-digit-lists-addition-carry.apl) | الأرقام معكوسة والمرحّل يمتد |
| 1617 | [`1617-merge-k-sorted-lists.apl`](examples/1617-merge-k-sorted-lists.apl) | قائمة واحدة مرتبة من عدة قوائم |
| 1618 | [`1618-binary-search-first-occurrence.apl`](examples/1618-binary-search-first-occurrence.apl) | موضع أول نسخة من قيمة مكررة في قائمة مرتبة |
| 1619 | [`1619-binary-search-last-occurrence.apl`](examples/1619-binary-search-last-occurrence.apl) | موضع آخر نسخة من قيمة مكررة |
| 1620 | [`1620-sorted-lower-bound.apl`](examples/1620-sorted-lower-bound.apl) | أول موضع قيمته لا تقل عن الهدف |
| 1621 | [`1621-sorted-upper-bound.apl`](examples/1621-sorted-upper-bound.apl) | أول موضع قيمته أكبر من الهدف |
| 1622 | [`1622-integer-square-root-binary.apl`](examples/1622-integer-square-root-binary.apl) | أكبر عدد صحيح مربعه لا يتجاوز العدد |
| 1623 | [`1623-count-occurrences-sorted.apl`](examples/1623-count-occurrences-sorted.apl) | الفرق بين الحد الأعلى والأدنى |
| 1624 | [`1624-floor-and-ceiling-sorted.apl`](examples/1624-floor-and-ceiling-sorted.apl) | أكبر عنصر لا يزيد وأصغر عنصر لا ينقص |
| 1625 | [`1625-koko-eating-bananas.apl`](examples/1625-koko-eating-bananas.apl) | أقل سرعة تنهي بها الأكوام قبل مرور الساعات |
| 1626 | [`1626-mountain-array-peak.apl`](examples/1626-mountain-array-peak.apl) | تصعد ثم تهبط: نجد موضع القمة |
| 1627 | [`1627-sorted-matrix-staircase-search.apl`](examples/1627-sorted-matrix-staircase-search.apl) | صفوف وأعمدة مرتبة: نبدأ من الركن العلوي الأيمن |
| 1628 | [`1628-rotation-count-sorted.apl`](examples/1628-rotation-count-sorted.apl) | موضع أصغر عنصر هو عدد الدورات |
| 1629 | [`1629-cyclic-sort-one-to-n.apl`](examples/1629-cyclic-sort-one-to-n.apl) | كل رقم يوضع في خانته مباشرة |
| 1630 | [`1630-set-mismatch-find.apl`](examples/1630-set-mismatch-find.apl) | مجموعة 1 إلى ن فيها رقم مكرر وآخر مفقود |
| 1631 | [`1631-three-sum-closest-target.apl`](examples/1631-three-sum-closest-target.apl) | ثلاثة أعداد مجموعها الأقرب إلى الهدف |
| 1632 | [`1632-minimum-meeting-rooms.apl`](examples/1632-minimum-meeting-rooms.apl) | أقصى عدد اجتماعات متزامنة |
| 1633 | [`1633-moving-average-from-stream.apl`](examples/1633-moving-average-from-stream.apl) | متوسط آخر ك قيمة عند كل وصول |
| 1634 | [`1634-smallest-letter-greater-than.apl`](examples/1634-smallest-letter-greater-than.apl) | في قائمة حروف مرتبة مع الالتفاف |
| 1635 | [`1635-k-closest-elements-sorted.apl`](examples/1635-k-closest-elements-sorted.apl) | العناصر الأقرب إلى قيمة معينة |
| 1636 | [`1636-kth-missing-positive-number.apl`](examples/1636-kth-missing-positive-number.apl) | الأرقام الغائبة من قائمة مرتبة |
| 1637 | [`1637-perfect-square-binary-check.apl`](examples/1637-perfect-square-binary-check.apl) | بلا استخدام الجذر |
| 1638 | [`1638-arranging-coins-staircase.apl`](examples/1638-arranging-coins-staircase.apl) | كم صفاً كاملاً يمكن بناؤه |
| 1639 | [`1639-minimum-days-for-bouquets.apl`](examples/1639-minimum-days-for-bouquets.apl) | نبحث عن أول يوم تكتمل فيه الباقات |
| 1640 | [`1640-nth-root-binary-search.apl`](examples/1640-nth-root-binary-search.apl) | أكبر عدد صحيح قوته ن لا تتجاوز العدد |
| 1641 | [`1641-gcd-of-number-list.apl`](examples/1641-gcd-of-number-list.apl) | نطبق خوارزمية إقليدس على القائمة كلها |
| 1642 | [`1642-lcm-of-number-list.apl`](examples/1642-lcm-of-number-list.apl) | نحسب المضاعف عنصراً بعنصر |
| 1643 | [`1643-count-coprime-below.apl`](examples/1643-count-coprime-below.apl) | كم عدداً أصغر من ن لا يشاركه قاسماً |
| 1644 | [`1644-sum-of-proper-divisors.apl`](examples/1644-sum-of-proper-divisors.apl) | كل قواسم العدد عدا نفسه |
| 1645 | [`1645-deficient-number-check.apl`](examples/1645-deficient-number-check.apl) | مجموع قواسمه الفعلية أقل منه |
| 1646 | [`1646-sum-of-digit-squares.apl`](examples/1646-sum-of-digit-squares.apl) | نربع كل رقم ونجمع |
| 1647 | [`1647-pronic-number-check.apl`](examples/1647-pronic-number-check.apl) | حاصل ضرب عددين متتاليين |
| 1648 | [`1648-triangular-number-check.apl`](examples/1648-triangular-number-check.apl) | مجموع الأعداد من 1 إلى ك |
| 1649 | [`1649-hexagonal-number-nth.apl`](examples/1649-hexagonal-number-nth.apl) | القانون ن×(2ن-1) |
| 1650 | [`1650-fibonacci-membership-check.apl`](examples/1650-fibonacci-membership-check.apl) | نولد المتتالية حتى نصل العدد |
| 1651 | [`1651-padovan-sequence-nth.apl`](examples/1651-padovan-sequence-nth.apl) | كل حد مجموع حدين قبل ثلاثة وقبل اثنين |
| 1652 | [`1652-integer-partition-count.apl`](examples/1652-integer-partition-count.apl) | بكم طريقة يُكتب العدد كمجموع أعداد موجبة |
| 1653 | [`1653-mobius-function-value.apl`](examples/1653-mobius-function-value.apl) | صفر إذا قبل القسمة على مربع وإلا حسب عدد العوامل |
| 1654 | [`1654-extended-euclid-coefficients.apl`](examples/1654-extended-euclid-coefficients.apl) | نجد س وص بحيث أ س + ب ص = القاسم |
| 1655 | [`1655-convert-to-any-base.apl`](examples/1655-convert-to-any-base.apl) | كتابة عدد بأساس بين 2 و16 |
| 1656 | [`1656-product-of-digits.apl`](examples/1656-product-of-digits.apl) | نضرب كل رقم في الآخر |
| 1657 | [`1657-smallest-prime-factor-table.apl`](examples/1657-smallest-prime-factor-table.apl) | غربال يسجل أصغر عامل لكل عدد |
| 1658 | [`1658-perfect-power-check.apl`](examples/1658-perfect-power-check.apl) | يساوي أساساً مرفوعاً لأس أكبر من واحد |
| 1659 | [`1659-radical-of-number.apl`](examples/1659-radical-of-number.apl) | حاصل ضرب عوامله الأولية المختلفة |
| 1660 | [`1660-automorphic-number-check.apl`](examples/1660-automorphic-number-check.apl) | مربعه ينتهي بنفسه |
| 1661 | [`1661-palindromic-prime-check.apl`](examples/1661-palindromic-prime-check.apl) | أولي يقرأ من اليسار كاليمين |
| 1662 | [`1662-distinct-prime-factor-count.apl`](examples/1662-distinct-prime-factor-count.apl) | كم عاملاً أولياً مختلفاً في تحليل العدد |
| 1663 | [`1663-square-free-check.apl`](examples/1663-square-free-check.apl) | لا يقبل القسمة على مربع أكبر من واحد |
| 1664 | [`1664-consecutive-sum-ways.apl`](examples/1664-consecutive-sum-ways.apl) | بكم طريقة يساوي العدد مجموع أعداد موجبة متتالية |
| 1665 | [`1665-trailing-zeros-of-factorial.apl`](examples/1665-trailing-zeros-of-factorial.apl) | عدد الأصفار في نهاية ن! |
| 1666 | [`1666-intervals-total-covered-length.apl`](examples/1666-intervals-total-covered-length.apl) | ندمج الفترات المتداخلة ونجمع أطوالها |
| 1667 | [`1667-intervals-any-overlap-check.apl`](examples/1667-intervals-any-overlap-check.apl) | نرتب ونقارن كل فترة بسابقتها |
| 1668 | [`1668-set-union-of-lists.apl`](examples/1668-set-union-of-lists.apl) | كل عنصر يظهر مرة واحدة |
| 1669 | [`1669-set-intersection-of-lists.apl`](examples/1669-set-intersection-of-lists.apl) | العناصر المشتركة دون تكرار |
| 1670 | [`1670-set-symmetric-difference-lists.apl`](examples/1670-set-symmetric-difference-lists.apl) | عناصر في إحداهما فقط |
| 1671 | [`1671-array-rotate-left-by-k.apl`](examples/1671-array-rotate-left-by-k.apl) | نقل أول ك عناصر إلى النهاية |
| 1672 | [`1672-count-inversions-pairs.apl`](examples/1672-count-inversions-pairs.apl) | أزواج مرتبة بعكس الترتيب الصاعد |
| 1673 | [`1673-subset-sum-reachable.apl`](examples/1673-subset-sum-reachable.apl) | هل نصل الهدف بجمع بعض العناصر |
| 1674 | [`1674-binary-strings-of-length-n.apl`](examples/1674-binary-strings-of-length-n.apl) | نولدها بالترتيب |
| 1675 | [`1675-balanced-parentheses-count.apl`](examples/1675-balanced-parentheses-count.apl) | عدد الأنماط الصحيحة لـ ن زوج |
| 1676 | [`1676-squared-distance-two-points.apl`](examples/1676-squared-distance-two-points.apl) | نتجنب الجذر بالأعداد الصحيحة |
| 1677 | [`1677-dot-product-of-vectors.apl`](examples/1677-dot-product-of-vectors.apl) | مجموع حاصل ضرب المركبات المتقابلة |
| 1678 | [`1678-cross-product-sign-turn.apl`](examples/1678-cross-product-sign-turn.apl) | الجداء الاتجاهي يحدد اليمين أو اليسار |
| 1679 | [`1679-bounding-box-of-points.apl`](examples/1679-bounding-box-of-points.apl) | أصغر وأكبر إحداثي في كل بعد |
| 1680 | [`1680-integer-polygon-perimeter-squares.apl`](examples/1680-integer-polygon-perimeter-squares.apl) | نمر على الأضلاع بإغلاق المضلع |
| 1681 | [`1681-min-heap-manual-push-pop.apl`](examples/1681-min-heap-manual-push-pop.apl) | نبني الكومة بإصلاح الموضع |
| 1682 | [`1682-sliding-window-max-simple.apl`](examples/1682-sliding-window-max-simple.apl) | نأخذ أكبر عنصر في كل نافذة بطول ك |
| 1683 | [`1683-linked-list-array-pairs-reverse.apl`](examples/1683-linked-list-array-pairs-reverse.apl) | نمثل الروابط بمصفوفة المؤشرات |
| 1684 | [`1684-permutations-of-three-lists.apl`](examples/1684-permutations-of-three-lists.apl) | نولد كل الترتيبات بالتراجع |
| 1685 | [`1685-subsets-with-target-sum-count.apl`](examples/1685-subsets-with-target-sum-count.apl) | نعد الطرق بجدول |
| 1686 | [`1686-grid-path-count-obstacles.apl`](examples/1686-grid-path-count-obstacles.apl) | نعد المسارات يميناً وأسفل |
| 1687 | [`1687-edit-distance-two-words.apl`](examples/1687-edit-distance-two-words.apl) | أقل عمليات إدراج وحذف واستبدال |
| 1688 | [`1688-longest-common-subsequence-length.apl`](examples/1688-longest-common-subsequence-length.apl) | طول أطول متتالية مشتركة بين نصين |
| 1689 | [`1689-count-set-bits-in-range.apl`](examples/1689-count-set-bits-in-range.apl) | نجمع عدد الآحاد الثنائية لكل عدد |
| 1690 | [`1690-is-power-of-two-bit.apl`](examples/1690-is-power-of-two-bit.apl) | ن & (ن-1) تساوي صفراً |
| 1691 | [`1691-gray-code-sequence.apl`](examples/1691-gray-code-sequence.apl) | كل رقمين متتاليين يختلفان ببت واحد |
| 1692 | [`1692-day-of-year-from-date.apl`](examples/1692-day-of-year-from-date.apl) | نجمع أيام الشهور السابقة |
| 1693 | [`1693-matrix-main-diagonal-sum.apl`](examples/1693-matrix-main-diagonal-sum.apl) | القطر الرئيسي والثانوي دون عد المركز مرتين |
| 1694 | [`1694-matrix-spiral-order-list.apl`](examples/1694-matrix-spiral-order-list.apl) | نقرأ الحواف من الخارج للداخل |
| 1695 | [`1695-queue-via-two-stacks.apl`](examples/1695-queue-via-two-stacks.apl) | نقلب المكدس عند الحاجة |
| 1696 | [`1696-thousands-separator-format.apl`](examples/1696-thousands-separator-format.apl) | نضع فاصلة كل ثلاثة أرقام |
| 1697 | [`1697-roman-numeral-to-integer.apl`](examples/1697-roman-numeral-to-integer.apl) | نطرح الرمز الأصغر قبل الأكبر |
| 1698 | [`1698-integer-to-roman-numeral.apl`](examples/1698-integer-to-roman-numeral.apl) | نطرح أكبر قيمة ممكنة مراراً |
| 1699 | [`1699-longest-palindromic-substring-length.apl`](examples/1699-longest-palindromic-substring-length.apl) | نوسع من كل مركز |
| 1700 | [`1700-coin-change-min-coins.apl`](examples/1700-coin-change-min-coins.apl) | نبني الحل لكل مبلغ أصغر |
| 1701 | [`1701-house-robber-max-sum.apl`](examples/1701-house-robber-max-sum.apl) | لا نأخذ عنصرين متجاورين |
| 1702 | [`1702-max-subarray-kadane.apl`](examples/1702-max-subarray-kadane.apl) | خوارزمية كادان |
| 1703 | [`1703-product-except-self-list.apl`](examples/1703-product-except-self-list.apl) | ضرب البادئة في اللاحقة |
| 1704 | [`1704-two-sum-indices-pair.apl`](examples/1704-two-sum-indices-pair.apl) | نبحث عن المكمل بقاموس |
| 1705 | [`1705-jump-game-reachable.apl`](examples/1705-jump-game-reachable.apl) | أبعد موضع يمكن بلوغه |
| 1706 | [`1706-min-jumps-to-end.apl`](examples/1706-min-jumps-to-end.apl) | نوسع مدى كل قفزة |
| 1707 | [`1707-grid-shortest-path-bfs-steps.apl`](examples/1707-grid-shortest-path-bfs-steps.apl) | نستكشف الجيران طبقة طبقة |
| 1708 | [`1708-flood-fill-region-size.apl`](examples/1708-flood-fill-region-size.apl) | نملأ الخلايا المتجاورة المتشابهة |
| 1709 | [`1709-count-islands-grid.apl`](examples/1709-count-islands-grid.apl) | كل مجموعة من الآحاد المتصلة جزيرة |
| 1710 | [`1710-topological-order-kahn.apl`](examples/1710-topological-order-kahn.apl) | نأخذ العقد بلا اعتماديات أولاً |
| 1711 | [`1711-graph-bipartite-check.apl`](examples/1711-graph-bipartite-check.apl) | نلون العقد بلونين |
| 1712 | [`1712-graph-components-dfs-total.apl`](examples/1712-graph-components-dfs-total.apl) | نستكشف كل عقدة لم تزر |
| 1713 | [`1713-tree-depth-from-pairs.apl`](examples/1713-tree-depth-from-pairs.apl) | نتتبع الآباء حتى الجذر |
| 1714 | [`1714-tree-leaf-count-nested.apl`](examples/1714-tree-leaf-count-nested.apl) | القوائم فروع والأرقام أوراق |
| 1715 | [`1715-nested-list-flatten-depth.apl`](examples/1715-nested-list-flatten-depth.apl) | كم مستوى من القوائم داخل بعض |
| 1716 | [`1716-recursive-digit-root.apl`](examples/1716-recursive-digit-root.apl) | نجمع الأرقام حتى يبقى رقم واحد |
| 1717 | [`1717-tower-of-hanoi-move-count.apl`](examples/1717-tower-of-hanoi-move-count.apl) | نحسب النقلات بالاستدعاء الذاتي |
| 1718 | [`1718-string-run-length-decode.apl`](examples/1718-string-run-length-decode.apl) | نعيد بناء النص من الحرف والعدد |
| 1719 | [`1719-string-word-frequency-top.apl`](examples/1719-string-word-frequency-top.apl) | نعد الكلمات ونأخذ الأكثر |
| 1720 | [`1720-bank-account-balance-simulation.apl`](examples/1720-bank-account-balance-simulation.apl) | نطبق الإيداع والسحب ونرفض الزائد |
| 1721 | [`1721-inventory-restock-needed.apl`](examples/1721-inventory-restock-needed.apl) | نقارن الكمية بحد الطلب |
| 1722 | [`1722-elevator-floor-travel-sum.apl`](examples/1722-elevator-floor-travel-sum.apl) | نجمع الفروق بين الطوابق المتتالية |
| 1723 | [`1723-parking-lot-fee-calculator.apl`](examples/1723-parking-lot-fee-calculator.apl) | الساعة الأولى بسعر والباقي بسعر أقل |
| 1724 | [`1724-counting-sort-small-range.apl`](examples/1724-counting-sort-small-range.apl) | نعد تكرار كل قيمة ثم نعيد كتابتها |
| 1725 | [`1725-selection-sort-swap-count.apl`](examples/1725-selection-sort-swap-count.apl) | نعد التبديلات الفعلية |
| 1726 | [`1726-merge-two-sorted-lists.apl`](examples/1726-merge-two-sorted-lists.apl) | نأخذ الأصغر من الرأسين |
| 1727 | [`1727-sort-by-frequency-then-value.apl`](examples/1727-sort-by-frequency-then-value.apl) | الأكثر تكراراً أولاً وعند التعادل الأصغر |
| 1728 | [`1728-majority-boyer-moore-candidate.apl`](examples/1728-majority-boyer-moore-candidate.apl) | نلغي كل عنصرين مختلفين |
| 1729 | [`1729-remove-duplicates-sorted-count.apl`](examples/1729-remove-duplicates-sorted-count.apl) | نقارن كل عنصر بسابقه |
| 1730 | [`1730-missing-number-in-range.apl`](examples/1730-missing-number-in-range.apl) | الفرق بين المجموع المتوقع والفعلي |
| 1731 | [`1731-first-unique-character-index.apl`](examples/1731-first-unique-character-index.apl) | نعد الحروف ثم نبحث عن أول عدد واحد |
| 1732 | [`1732-anagram-pair-check-sorted.apl`](examples/1732-anagram-pair-check-sorted.apl) | كلمتان جناس إذا تطابقت حروفهما مرتبة |
| 1733 | [`1733-string-compress-char-counts.apl`](examples/1733-string-compress-char-counts.apl) | نكتب الحرف وبعده عدد تكراره المتتالي |
| 1734 | [`1734-caesar-shift-lowercase-only.apl`](examples/1734-caesar-shift-lowercase-only.apl) | نزيح الحروف الصغيرة فقط |
| 1735 | [`1735-vowel-consonant-count-pair.apl`](examples/1735-vowel-consonant-count-pair.apl) | نصنف كل حرف لاتيني |
| 1736 | [`1736-capitalize-each-word-simple.apl`](examples/1736-capitalize-each-word-simple.apl) | نكبر الحرف الأول من كل كلمة |
| 1737 | [`1737-fizz-buzz-count-range.apl`](examples/1737-fizz-buzz-count-range.apl) | نعد كل فئة في المدى |
| 1738 | [`1738-meeting-rooms-needed-count.apl`](examples/1738-meeting-rooms-needed-count.apl) | أقصى عدد اجتماعات متزامنة |
| 1739 | [`1739-job-scheduling-earliest-deadline.apl`](examples/1739-job-scheduling-earliest-deadline.apl) | نرتب بالموعد ونحسب أقصى تأخير |
| 1740 | [`1740-round-robin-turnaround-time.apl`](examples/1740-round-robin-turnaround-time.apl) | كل مهمة تأخذ حصة زمنية بالدور |
| 1741 | [`1741-two-pointer-container-water.apl`](examples/1741-two-pointer-container-water.apl) | نتحرك من الجدار الأقصر |
| 1742 | [`1742-trapping-rain-water-total.apl`](examples/1742-trapping-rain-water-total.apl) | الماء فوق كل عمود بحسب الجدارين |
| 1743 | [`1743-best-time-buy-sell-once.apl`](examples/1743-best-time-buy-sell-once.apl) | نتتبع أقل سعر ورأس الربح |
| 1744 | [`1744-stock-profit-many-trades.apl`](examples/1744-stock-profit-many-trades.apl) | نجمع كل صعود |
| 1745 | [`1745-gas-station-start-index.apl`](examples/1745-gas-station-start-index.apl) | من أين نبدأ لنكمل الدائرة |
| 1746 | [`1746-candy-distribution-min-total.apl`](examples/1746-candy-distribution-min-total.apl) | كل طفل أكثر تقييماً من جاره يأخذ أكثر |
| 1747 | [`1747-matrix-transpose-rectangular.apl`](examples/1747-matrix-transpose-rectangular.apl) | الصف يصبح عموداً |
| 1748 | [`1748-matrix-multiply-small.apl`](examples/1748-matrix-multiply-small.apl) | صف في عمود |
| 1749 | [`1749-matrix-rotate-quarter-turn.apl`](examples/1749-matrix-rotate-quarter-turn.apl) | نقلب ثم نعكس الصفوف |
| 1750 | [`1750-matrix-row-column-max-sums.apl`](examples/1750-matrix-row-column-max-sums.apl) | نقارن مجاميع الصفوف والأعمدة |
| 1751 | [`1751-pascal-triangle-row-nth.apl`](examples/1751-pascal-triangle-row-nth.apl) | كل عنصر مجموع الفوقيين |
| 1752 | [`1752-n-choose-k-iterative.apl`](examples/1752-n-choose-k-iterative.apl) | نضرب ونقسم تدريجياً |
| 1753 | [`1753-combinations-of-size-two.apl`](examples/1753-combinations-of-size-two.apl) | نختار كل زوجين مختلفين |
| 1754 | [`1754-subsets-of-list-bitmask.apl`](examples/1754-subsets-of-list-bitmask.apl) | كل رقم ثنائي يمثل مجموعة |
| 1755 | [`1755-generate-parentheses-all.apl`](examples/1755-generate-parentheses-all.apl) | نضيف قوساً مفتوحاً أو مغلقاً بشرط |
| 1756 | [`1756-word-break-possible.apl`](examples/1756-word-break-possible.apl) | هل نغطي النص بكلمات القاموس |
| 1757 | [`1757-climbing-stairs-ways-count.apl`](examples/1757-climbing-stairs-ways-count.apl) | خطوة أو خطوتان في كل مرة |
| 1758 | [`1758-longest-increasing-subsequence-len.apl`](examples/1758-longest-increasing-subsequence-len.apl) | نحسب لكل عنصر أطول متتالية تنتهي به |
| 1759 | [`1759-knapsack-zero-one-value.apl`](examples/1759-knapsack-zero-one-value.apl) | أقصى قيمة ضمن سعة محدودة |
| 1760 | [`1760-unique-paths-grid-count.apl`](examples/1760-unique-paths-grid-count.apl) | يمين وأسفل فقط |
| 1761 | [`1761-min-path-sum-triangle.apl`](examples/1761-min-path-sum-triangle.apl) | ننزل من القمة للقاعدة |
| 1762 | [`1762-decode-ways-digit-string.apl`](examples/1762-decode-ways-digit-string.apl) | الأرقام من 1 إلى 26 حروف |
| 1763 | [`1763-perfect-squares-min-count.apl`](examples/1763-perfect-squares-min-count.apl) | كم مربعاً يكفي لتكوين العدد |
| 1764 | [`1764-linked-list-middle-node-index.apl`](examples/1764-linked-list-middle-node-index.apl) | مؤشر سريع وآخر بطيء |
| 1765 | [`1765-linked-list-cycle-detect-floyd.apl`](examples/1765-linked-list-cycle-detect-floyd.apl) | سرعتان تلتقيان داخل الدورة |
| 1766 | [`1766-linked-list-remove-nth-from-end.apl`](examples/1766-linked-list-remove-nth-from-end.apl) | نحسب الطول ثم نعيد الربط |
| 1767 | [`1767-date-days-between-years-simple.apl`](examples/1767-date-days-between-years-simple.apl) | نجمع أطوال السنوات مع الكبيسة |
| 1768 | [`1768-weekday-from-date-zeller.apl`](examples/1768-weekday-from-date-zeller.apl) | معادلة تحسب اليوم من التاريخ |
| 1769 | [`1769-clock-angle-between-hands.apl`](examples/1769-clock-angle-between-hands.apl) | نحسب موضع كل عقرب بالدرجات |
| 1770 | [`1770-next-greater-element-stack.apl`](examples/1770-next-greater-element-stack.apl) | لكل عنصر أول عنصر أكبر منه على يمينه |
| 1771 | [`1771-daily-temperatures-wait-days.apl`](examples/1771-daily-temperatures-wait-days.apl) | كم يوماً حتى ترتفع الحرارة |
| 1772 | [`1772-largest-rectangle-histogram.apl`](examples/1772-largest-rectangle-histogram.apl) | مكدس يحفظ أعمدة صاعدة |
| 1773 | [`1773-valid-brackets-three-kinds.apl`](examples/1773-valid-brackets-three-kinds.apl) | كل قوس يغلق بنظيره |
| 1774 | [`1774-min-add-parentheses-fix.apl`](examples/1774-min-add-parentheses-fix.apl) | نعد الأقواس غير المتزنة |
| 1775 | [`1775-postfix-expression-evaluate.apl`](examples/1775-postfix-expression-evaluate.apl) | الأعداد تدخل المكدس والعمليات تأخذ آخر عددين |
| 1776 | [`1776-infix-to-postfix-simple.apl`](examples/1776-infix-to-postfix-simple.apl) | نرتب العمليات بأولوياتها |
| 1777 | [`1777-simplify-unix-path.apl`](examples/1777-simplify-unix-path.apl) | نعالج النقطتين والنقطة |
| 1778 | [`1778-decode-nested-repeat-string.apl`](examples/1778-decode-nested-repeat-string.apl) | 3[ab] تعني ababab |
| 1779 | [`1779-longest-substring-no-repeat.apl`](examples/1779-longest-substring-no-repeat.apl) | نافذة تتمدد وتنكمش |
| 1780 | [`1780-min-window-sum-at-least.apl`](examples/1780-min-window-sum-at-least.apl) | نافذة متحركة على أعداد موجبة |
| 1781 | [`1781-subarray-sum-equals-target-count.apl`](examples/1781-subarray-sum-equals-target-count.apl) | مجاميع تراكمية وقاموس |
| 1782 | [`1782-longest-consecutive-run-set.apl`](examples/1782-longest-consecutive-run-set.apl) | نبدأ من بدايات المتتاليات فقط |
| 1783 | [`1783-pair-count-with-difference-k.apl`](examples/1783-pair-count-with-difference-k.apl) | نبحث عن العدد زائد الفرق |
| 1784 | [`1784-happy-number-check-loop.apl`](examples/1784-happy-number-check-loop.apl) | مجموع مربعات الأرقام يصل إلى واحد |
| 1785 | [`1785-ugly-number-nth.apl`](examples/1785-ugly-number-nth.apl) | عوامله الأولية 2 و3 و5 فقط |
| 1786 | [`1786-kaprekar-routine-steps.apl`](examples/1786-kaprekar-routine-steps.apl) | فرق الترتيب التنازلي والتصاعدي |
| 1787 | [`1787-collatz-longest-under-limit.apl`](examples/1787-collatz-longest-under-limit.apl) | نختبر كل بداية تحت الحد |
| 1788 | [`1788-sum-multiples-three-five-limit.apl`](examples/1788-sum-multiples-three-five-limit.apl) | مضاعفات 3 أو 5 |
| 1789 | [`1789-largest-prime-factor-of.apl`](examples/1789-largest-prime-factor-of.apl) | نقسم على أصغر عامل مراراً |
| 1790 | [`1790-count-digit-occurrences-range.apl`](examples/1790-count-digit-occurrences-range.apl) | نعد رقماً في كل الأعداد من 1 إلى ن |
| 1791 | [`1791-reverse-integer-digits.apl`](examples/1791-reverse-integer-digits.apl) | نبني العدد المعكوس رقماً رقماً |
| 1792 | [`1792-armstrong-numbers-below.apl`](examples/1792-armstrong-numbers-below.apl) | مجموع الأرقام مرفوعة لعددها |
| 1793 | [`1793-number-to-english-words-small.apl`](examples/1793-number-to-english-words-small.apl) | نحول أعداداً أقل من مئة إلى كلمات |
| 1794 | [`1794-excel-column-title-number.apl`](examples/1794-excel-column-title-number.apl) | نظام عد بالأحرف يبدأ من واحد |
| 1795 | [`1795-excel-column-number-from-title.apl`](examples/1795-excel-column-number-from-title.apl) | عكس الترقيم بالأحرف |
| 1796 | [`1796-binary-add-two-strings.apl`](examples/1796-binary-add-two-strings.apl) | جمع بالحمل من اليمين |
| 1797 | [`1797-single-number-xor-trick.apl`](examples/1797-single-number-xor-trick.apl) | كل مكرر يلغي نفسه |
| 1798 | [`1798-hamming-distance-two-numbers.apl`](examples/1798-hamming-distance-two-numbers.apl) | عدد البتات المختلفة |
| 1799 | [`1799-reverse-bits-eight.apl`](examples/1799-reverse-bits-eight.apl) | البت الأخير يصبح الأول |
| 1800 | [`1800-lowest-set-bit-isolate.apl`](examples/1800-lowest-set-bit-isolate.apl) | ن & (-ن) يعطي أدنى بت |
| 1801 | [`1801-swap-without-temp-xor.apl`](examples/1801-swap-without-temp-xor.apl) | ثلاث عمليات XOR تكفي |
| 1802 | [`1802-point-on-segment-check.apl`](examples/1802-point-on-segment-check.apl) | استقامة ثم داخل الحدود |
| 1803 | [`1803-rectangles-intersect-area.apl`](examples/1803-rectangles-intersect-area.apl) | نحسب التداخل في كل محور |
| 1804 | [`1804-manhattan-closest-pair-brute.apl`](examples/1804-manhattan-closest-pair-brute.apl) | نقارن كل زوج |
| 1805 | [`1805-shoelace-polygon-twice-area.apl`](examples/1805-shoelace-polygon-twice-area.apl) | نجمع الجداءات المتقاطعة |
| 1806 | [`1806-circle-lattice-points-count.apl`](examples/1806-circle-lattice-points-count.apl) | نعد النقاط ذات الإحداثيات الصحيحة |
| 1807 | [`1807-group-words-by-length-dict.apl`](examples/1807-group-words-by-length-dict.apl) | قاموس يربط الطول بقائمة كلمات |
| 1808 | [`1808-invert-dictionary-values.apl`](examples/1808-invert-dictionary-values.apl) | القيم تصبح مفاتيح |
| 1809 | [`1809-merge-two-dicts-sum.apl`](examples/1809-merge-two-dicts-sum.apl) | المفاتيح المشتركة تجمع قيمها |
| 1810 | [`1810-most-common-character-count.apl`](examples/1810-most-common-character-count.apl) | نعد الحروف ونختار الأعلى |
| 1811 | [`1811-isomorphic-strings-check.apl`](examples/1811-isomorphic-strings-check.apl) | كل حرف يقابل حرفاً واحداً |
| 1812 | [`1812-word-pattern-match-check.apl`](examples/1812-word-pattern-match-check.apl) | حرف النمط يقابل كلمة واحدة |
| 1813 | [`1813-common-prefix-of-words.apl`](examples/1813-common-prefix-of-words.apl) | نقارن الحروف بالموضع |
| 1814 | [`1814-count-and-say-sequence.apl`](examples/1814-count-and-say-sequence.apl) | كل حد يصف الحد السابق |
| 1815 | [`1815-reverse-words-in-sentence.apl`](examples/1815-reverse-words-in-sentence.apl) | الكلمات بترتيب معكوس |
| 1816 | [`1816-title-case-length-check.apl`](examples/1816-title-case-length-check.apl) | كم كلمة تبدأ بحرف كبير |
| 1817 | [`1817-string-rotation-check.apl`](examples/1817-string-rotation-check.apl) | النص الثاني داخل مضاعف الأول |
| 1818 | [`1818-balanced-binary-split-count.apl`](examples/1818-balanced-binary-split-count.apl) | أجزاء فيها عدد الأصفار يساوي الآحاد |
| 1819 | [`1819-alternating-bits-check.apl`](examples/1819-alternating-bits-check.apl) | كل بتين متجاورين مختلفان |
| 1820 | [`1820-complement-of-binary-number.apl`](examples/1820-complement-of-binary-number.apl) | نقلب كل بتات العدد دون الأصفار البادئة |
| 1821 | [`1821-binary-gap-longest-zeros.apl`](examples/1821-binary-gap-longest-zeros.apl) | أصفار بين واحدين |
| 1822 | [`1822-counting-bits-up-to-n.apl`](examples/1822-counting-bits-up-to-n.apl) | نبني الجدول من النصف |
| 1823 | [`1823-fraction-add-lowest-terms.apl`](examples/1823-fraction-add-lowest-terms.apl) | نوحد المقامات ثم نختصر |
| 1824 | [`1824-repeating-decimal-cycle-length.apl`](examples/1824-repeating-decimal-cycle-length.apl) | نتتبع البواقي حتى تتكرر |
| 1825 | [`1825-running-average-window-list.apl`](examples/1825-running-average-window-list.apl) | متوسط كل نافذة من ك عناصر |
| 1826 | [`1826-max-consecutive-ones-run.apl`](examples/1826-max-consecutive-ones-run.apl) | نعد الآحاد المتتالية |
| 1827 | [`1827-move-zeros-to-end-stable.apl`](examples/1827-move-zeros-to-end-stable.apl) | نحافظ على ترتيب غير الأصفار |
| 1828 | [`1828-sort-colors-dutch-flag.apl`](examples/1828-sort-colors-dutch-flag.apl) | ثلاثة مؤشرات تكفي |
| 1829 | [`1829-power-set-size-recursive.apl`](examples/1829-power-set-size-recursive.apl) | نعد المجموعات الجزئية بالتكرار |
| 1830 | [`1830-recursive-binary-search-index.apl`](examples/1830-recursive-binary-search-index.apl) | نقسم المدى بالاستدعاء الذاتي |
| 1831 | [`1831-search-rotated-sorted-array.apl`](examples/1831-search-rotated-sorted-array.apl) | نحدد النصف المرتب أولاً |
| 1832 | [`1832-find-minimum-rotated-array.apl`](examples/1832-find-minimum-rotated-array.apl) | نقارن المنتصف بالنهاية |
| 1833 | [`1833-first-last-position-sorted.apl`](examples/1833-first-last-position-sorted.apl) | حدان بحث ثنائي |
| 1834 | [`1834-integer-sqrt-binary-search.apl`](examples/1834-integer-sqrt-binary-search.apl) | أكبر عدد مربعه لا يتجاوز ن |
| 1835 | [`1835-peak-element-binary-search.apl`](examples/1835-peak-element-binary-search.apl) | نتبع الاتجاه الصاعد |
| 1836 | [`1836-koko-eating-bananas-speed.apl`](examples/1836-koko-eating-bananas-speed.apl) | بحث ثنائي على الإجابة |
| 1837 | [`1837-ship-packages-capacity-days.apl`](examples/1837-ship-packages-capacity-days.apl) | بحث ثنائي على السعة |
| 1838 | [`1838-search-insert-position-sorted.apl`](examples/1838-search-insert-position-sorted.apl) | أول موضع لا يقل عن الهدف |
| 1839 | [`1839-matrix-search-sorted-rows.apl`](examples/1839-matrix-search-sorted-rows.apl) | نبدأ من الزاوية العلوية اليمنى |
| 1840 | [`1840-kth-smallest-in-matrix-sorted.apl`](examples/1840-kth-smallest-in-matrix-sorted.apl) | نجمع ونرتب |
| 1841 | [`1841-insertion-sort-shift-count.apl`](examples/1841-insertion-sort-shift-count.apl) | نعد حركات العناصر |
| 1842 | [`1842-bubble-sort-pass-count.apl`](examples/1842-bubble-sort-pass-count.apl) | نتوقف حين لا يحدث تبديل |
| 1843 | [`1843-quick-select-kth-element.apl`](examples/1843-quick-select-kth-element.apl) | نقسم حول محور |
| 1844 | [`1844-sort-by-absolute-value-stable.apl`](examples/1844-sort-by-absolute-value-stable.apl) | نرتب الأزواج بالمطلق ثم الأصلي |
| 1845 | [`1845-squares-sorted-from-both-ends.apl`](examples/1845-squares-sorted-from-both-ends.apl) | نملأ من الأكبر |
| 1846 | [`1846-three-sum-zero-count.apl`](examples/1846-three-sum-zero-count.apl) | نثبت عنصراً ونبحث بمؤشرين |
| 1847 | [`1847-remove-element-in-place-count.apl`](examples/1847-remove-element-in-place-count.apl) | نكتب غير المحذوف في المقدمة |
| 1848 | [`1848-valid-palindrome-ignore-nonalnum.apl`](examples/1848-valid-palindrome-ignore-nonalnum.apl) | نتجاوز غير الحروف والأرقام |
| 1849 | [`1849-days-in-month-with-leap.apl`](examples/1849-days-in-month-with-leap.apl) | فبراير يتغير حسب السنة |
| 1850 | [`1850-add-days-to-date-simple.apl`](examples/1850-add-days-to-date-simple.apl) | نتحرك يوماً يوماً عبر الأشهر |
| 1851 | [`1851-time-add-minutes-clock.apl`](examples/1851-time-add-minutes-clock.apl) | ساعة ودقيقة بنظام أربع وعشرين |
| 1852 | [`1852-seconds-to-hms-format.apl`](examples/1852-seconds-to-hms-format.apl) | نقسم على 3600 ثم 60 |
| 1853 | [`1853-overlap-minutes-between-ranges.apl`](examples/1853-overlap-minutes-between-ranges.apl) | نحسب تقاطع فترتين زمنيتين |
| 1854 | [`1854-weekday-index-after-days.apl`](examples/1854-weekday-index-after-days.apl) | نحرك اليوم بمقياس سبعة |
| 1855 | [`1855-age-in-years-from-dates.apl`](examples/1855-age-in-years-from-dates.apl) | نطرح السنوات ونصحح قبل عيد الميلاد |
| 1856 | [`1856-leap-years-count-in-range.apl`](examples/1856-leap-years-count-in-range.apl) | نعد من سنة إلى أخرى |
| 1857 | [`1857-sum-of-two-largest-distinct.apl`](examples/1857-sum-of-two-largest-distinct.apl) | نتتبع أكبر قيمتين مختلفتين |
| 1858 | [`1858-second-smallest-distinct-value.apl`](examples/1858-second-smallest-distinct-value.apl) | نتتبع أصغر قيمتين |
| 1859 | [`1859-array-equilibrium-index-find.apl`](examples/1859-array-equilibrium-index-find.apl) | مجموع اليسار يساوي مجموع اليمين |
| 1860 | [`1860-array-leaders-from-right.apl`](examples/1860-array-leaders-from-right.apl) | عناصر أكبر من كل ما على يمينها |
| 1861 | [`1861-array-chunk-split-size.apl`](examples/1861-array-chunk-split-size.apl) | كل جزء بحجم ثابت |
| 1862 | [`1862-interleave-two-lists-alternate.apl`](examples/1862-interleave-two-lists-alternate.apl) | عنصر من كل قائمة بالدور |
| 1863 | [`1863-histogram-text-bars.apl`](examples/1863-histogram-text-bars.apl) | نرسم كل عدد بنجوم |
| 1864 | [`1864-pyramid-rows-star-count.apl`](examples/1864-pyramid-rows-star-count.apl) | الصف ك فيه 2ك-1 نجمة |
| 1865 | [`1865-multiplication-table-row-list.apl`](examples/1865-multiplication-table-row-list.apl) | مضاعفات عدد حتى عشرة |
| 1866 | [`1866-celsius-fahrenheit-integer-table.apl`](examples/1866-celsius-fahrenheit-integer-table.apl) | تحويل بأعداد صحيحة عند مضاعفات الخمسة |
| 1867 | [`1867-sum-arithmetic-progression-terms.apl`](examples/1867-sum-arithmetic-progression-terms.apl) | نستخدم صيغة المجموع |
| 1868 | [`1868-compound-interest-integer-years.apl`](examples/1868-compound-interest-integer-years.apl) | نضيف نسبة مئوية كل سنة |
| 1869 | [`1869-loan-payoff-months-count.apl`](examples/1869-loan-payoff-months-count.apl) | قسط ثابت وفائدة شهرية |
| 1870 | [`1870-discount-tier-price-calc.apl`](examples/1870-discount-tier-price-calc.apl) | الخصم يزيد مع الكمية |
| 1871 | [`1871-heap-array-is-valid-min.apl`](examples/1871-heap-array-is-valid-min.apl) | كل أب أصغر من ابنيه |
| 1872 | [`1872-heapify-build-min-heap.apl`](examples/1872-heapify-build-min-heap.apl) | ننزل كل أب غير فرعي |
| 1873 | [`1873-top-k-largest-by-sort.apl`](examples/1873-top-k-largest-by-sort.apl) | نرتب ونأخذ آخر ك |
| 1874 | [`1874-running-median-small-list.apl`](examples/1874-running-median-small-list.apl) | نحافظ على قائمة مرتبة |
| 1875 | [`1875-mode-of-list-smallest.apl`](examples/1875-mode-of-list-smallest.apl) | القيمة الأكثر تكراراً |
| 1876 | [`1876-range-and-spread-of-list.apl`](examples/1876-range-and-spread-of-list.apl) | الفرق بين الأكبر والأصغر |
| 1877 | [`1877-variance-integer-scaled.apl`](examples/1877-variance-integer-scaled.apl) | ن×مجموع المربعات - مربع المجموع |
| 1878 | [`1878-prefix-sum-range-queries.apl`](examples/1878-prefix-sum-range-queries.apl) | مجاميع تراكمية |
| 1879 | [`1879-difference-array-range-add.apl`](examples/1879-difference-array-range-add.apl) | نضيف على مدى بعمليتين |
| 1880 | [`1880-rectangle-sum-prefix-2d.apl`](examples/1880-rectangle-sum-prefix-2d.apl) | نبني جدولاً تراكمياً ثنائي |
| 1881 | [`1881-tree-heights-from-parent-list.apl`](examples/1881-tree-heights-from-parent-list.apl) | أطول سلسلة من الجذر |
| 1882 | [`1882-lowest-common-ancestor-parents.apl`](examples/1882-lowest-common-ancestor-parents.apl) | نصعد من العقدتين حتى نلتقي |
| 1883 | [`1883-tree-diameter-parents-path.apl`](examples/1883-tree-diameter-parents-path.apl) | أطول مسار بين عقدتين |
| 1884 | [`1884-dijkstra-small-graph-distance.apl`](examples/1884-dijkstra-small-graph-distance.apl) | نختار أقرب عقدة غير مزارة |
| 1885 | [`1885-floyd-warshall-all-pairs-small.apl`](examples/1885-floyd-warshall-all-pairs-small.apl) | نجرب كل عقدة وسيطة |
| 1886 | [`1886-union-find-count-groups.apl`](examples/1886-union-find-count-groups.apl) | ندمج المجموعات ونعد الجذور |
| 1887 | [`1887-redundant-edge-cycle-detect.apl`](examples/1887-redundant-edge-cycle-detect.apl) | أول حافة تصل عنصرين متصلين أصلاً |
| 1888 | [`1888-minimum-spanning-tree-kruskal.apl`](examples/1888-minimum-spanning-tree-kruskal.apl) | نضيف أرخص حافة لا تكون دورة |
| 1889 | [`1889-caesar-shift-lowercase-text.apl`](examples/1889-caesar-shift-lowercase-text.apl) | نزيح كل حرف بعدد ثابت |
| 1890 | [`1890-atbash-lowercase-text.apl`](examples/1890-atbash-lowercase-text.apl) | كل حرف يقابل حرفه المعكوس |
| 1891 | [`1891-rot13-lowercase-text.apl`](examples/1891-rot13-lowercase-text.apl) | إزاحة ثابتة قدرها ١٣ |
| 1892 | [`1892-vigenere-lowercase-encode.apl`](examples/1892-vigenere-lowercase-encode.apl) | مفتاح كلمة يحدد الإزاحة لكل حرف |
| 1893 | [`1893-count-subsets-with-target-sum.apl`](examples/1893-count-subsets-with-target-sum.apl) | نختار العنصر أو نتركه |
| 1894 | [`1894-n-queens-count-solutions.apl`](examples/1894-n-queens-count-solutions.apl) | نضع ملكة في كل صف بلا تهديد |
| 1895 | [`1895-count-derangements-backtracking.apl`](examples/1895-count-derangements-backtracking.apl) | لا يبقى عنصر في مكانه |
| 1896 | [`1896-list-combinations-n-choose-k.apl`](examples/1896-list-combinations-n-choose-k.apl) | نبني توافيق بحجم ثابت |
| 1897 | [`1897-count-palindrome-partitions.apl`](examples/1897-count-palindrome-partitions.apl) | نقطع النص إلى أجزاء متماثلة |
| 1898 | [`1898-text-center-with-padding.apl`](examples/1898-text-center-with-padding.apl) | نضيف حشوا على الجانبين |
| 1899 | [`1899-word-wrap-line-count.apl`](examples/1899-word-wrap-line-count.apl) | نلف الكلمات على عرض محدد |
| 1900 | [`1900-format-thousands-separator.apl`](examples/1900-format-thousands-separator.apl) | نضع فاصلة كل ثلاث خانات |
| 1901 | [`1901-month-length-leap-aware.apl`](examples/1901-month-length-leap-aware.apl) | فبراير يتغير في السنة الكبيسة |
| 1902 | [`1902-ordinal-day-of-year-calc.apl`](examples/1902-ordinal-day-of-year-calc.apl) | نجمع أيام الشهور السابقة |
| 1903 | [`1903-weekday-from-date-sakamoto.apl`](examples/1903-weekday-from-date-sakamoto.apl) | خوارزمية ساكاموتو |
| 1904 | [`1904-linked-list-reverse-by-arrays.apl`](examples/1904-linked-list-reverse-by-arrays.apl) | نغير اتجاه المؤشرات |
| 1905 | [`1905-linked-list-middle-node-fast-slow.apl`](examples/1905-linked-list-middle-node-fast-slow.apl) | مؤشر سريع وآخر بطيء |
| 1906 | [`1906-linked-list-detect-cycle-floyd.apl`](examples/1906-linked-list-detect-cycle-floyd.apl) | السريع يلحق البطيء عند وجود دورة |
| 1907 | [`1907-merge-two-sorted-linked-lists.apl`](examples/1907-merge-two-sorted-linked-lists.apl) | نأخذ الأصغر من الرأسين |
| 1908 | [`1908-roman-numeral-to-integer-parse.apl`](examples/1908-roman-numeral-to-integer-parse.apl) | الرمز الأصغر قبل الأكبر يطرح |
| 1909 | [`1909-integer-to-roman-numeral-build.apl`](examples/1909-integer-to-roman-numeral-build.apl) | نطرح أكبر قيمة ممكنة مرارا |
| 1910 | [`1910-decimal-to-any-base-string.apl`](examples/1910-decimal-to-any-base-string.apl) | نقسم على الأساس ونجمع البواقي |
| 1911 | [`1911-parse-string-in-any-base.apl`](examples/1911-parse-string-in-any-base.apl) | نضرب الناتج بالأساس ونضيف الخانة |
| 1912 | [`1912-josephus-queue-simulation.apl`](examples/1912-josephus-queue-simulation.apl) | نحذف كل شخص ك في الدائرة |
| 1913 | [`1913-hot-potato-queue-last-player.apl`](examples/1913-hot-potato-queue-last-player.apl) | نمرر الكرة ثم نخرج اللاعب |
| 1914 | [`1914-bit-dp-count-hamiltonian-paths.apl`](examples/1914-bit-dp-count-hamiltonian-paths.apl) | القناع يمثل العقد المزارة |
| 1915 | [`1915-bit-dp-min-cost-assignment.apl`](examples/1915-bit-dp-min-cost-assignment.apl) | القناع يمثل المهام المسندة |
| 1916 | [`1916-tic-tac-toe-winner-check.apl`](examples/1916-tic-tac-toe-winner-check.apl) | نفحص الصفوف والأعمدة والقطرين |
| 1917 | [`1917-nim-game-winning-position.apl`](examples/1917-nim-game-winning-position.apl) | الموقف رابح إن كان مجموع xor غير صفر |
| 1918 | [`1918-stone-game-subtract-dp.apl`](examples/1918-stone-game-subtract-dp.apl) | الموقف خاسر إن كانت كل الحركات تؤدي لموقف رابح |
| 1919 | [`1919-matrix-spiral-order-traverse.apl`](examples/1919-matrix-spiral-order-traverse.apl) | أربع حدود تضيق تدريجيا |
| 1920 | [`1920-matrix-rotate-ninety-degrees.apl`](examples/1920-matrix-rotate-ninety-degrees.apl) | الصف الأخير يصبح العمود الأول |
| 1921 | [`1921-pascal-triangle-row-build.apl`](examples/1921-pascal-triangle-row-build.apl) | كل عنصر مجموع العنصرين فوقه |
| 1922 | [`1922-ticket-queue-wait-time.apl`](examples/1922-ticket-queue-wait-time.apl) | كل شخص يشتري تذكرة في ثانية |
| 1923 | [`1923-spell-number-english-under-thousand.apl`](examples/1923-spell-number-english-under-thousand.apl) | نقسم العدد لمئات وعشرات وآحاد |
| 1924 | [`1924-gray-code-sequence-generate.apl`](examples/1924-gray-code-sequence-generate.apl) | كل رقمين متتاليين يختلفان ببت واحد |
| 1925 | [`1925-lcs-length-two-strings-table.apl`](examples/1925-lcs-length-two-strings-table.apl) | جدول يقارن بادئات النصين |
| 1926 | [`1926-levenshtein-edit-distance-table.apl`](examples/1926-levenshtein-edit-distance-table.apl) | أقل عدد إدراج وحذف واستبدال |
| 1927 | [`1927-longest-palindrome-expand-center.apl`](examples/1927-longest-palindrome-expand-center.apl) | نوسع حول كل مركز |
| 1928 | [`1928-count-distinct-subsequence-matches.apl`](examples/1928-count-distinct-subsequence-matches.apl) | كم طريقة نكون بها النص الهدف |
| 1929 | [`1929-sudoku-four-by-four-validator.apl`](examples/1929-sudoku-four-by-four-validator.apl) | كل صف وعمود ومربع فيه ١ إلى ٤ |
| 1930 | [`1930-symmetric-difference-of-lists.apl`](examples/1930-symmetric-difference-of-lists.apl) | العناصر الموجودة في قائمة واحدة فقط |
| 1931 | [`1931-is-subset-of-list-check.apl`](examples/1931-is-subset-of-list-check.apl) | كل عنصر يجب أن يوجد في الأكبر |
| 1932 | [`1932-run-length-encode-plain-text.apl`](examples/1932-run-length-encode-plain-text.apl) | نكتب الحرف وعدد تكراره |
| 1933 | [`1933-run-length-decode-single-digit.apl`](examples/1933-run-length-decode-single-digit.apl) | نكرر كل حرف حسب العدد بعده |
| 1934 | [`1934-longest-common-prefix-of-words.apl`](examples/1934-longest-common-prefix-of-words.apl) | نقارن الحروف عمودا بعمود |
| 1935 | [`1935-pad-right-fixed-width-column.apl`](examples/1935-pad-right-fixed-width-column.apl) | نكمل بحرف حتى العرض المطلوب |
| 1936 | [`1936-count-vowels-in-english-text.apl`](examples/1936-count-vowels-in-english-text.apl) | نعد a e i o u |
| 1937 | [`1937-affine-cipher-lowercase-encode.apl`](examples/1937-affine-cipher-lowercase-encode.apl) | نضرب الموقع ثم نجمع |
| 1938 | [`1938-rail-fence-cipher-encode.apl`](examples/1938-rail-fence-cipher-encode.apl) | نكتب الحروف متعرجة على صفوف |
| 1939 | [`1939-bank-single-teller-total-wait.apl`](examples/1939-bank-single-teller-total-wait.apl) | العميل ينتظر حتى يفرغ الصراف |
| 1940 | [`1940-round-robin-finish-times.apl`](examples/1940-round-robin-finish-times.apl) | كل عملية تأخذ حصة زمنية ثم تعود للطابور |
| 1941 | [`1941-longest-valid-parentheses-length.apl`](examples/1941-longest-valid-parentheses-length.apl) | نخزن مواضع الأقواس في مكدس |
| 1942 | [`1942-parking-fee-first-hour-then-hourly.apl`](examples/1942-parking-fee-first-hour-then-hourly.apl) | أول ساعة بسعر ثابت ثم سعر أقل لكل ساعة بسقف يومي |
| 1943 | [`1943-library-fine-days-late.apl`](examples/1943-library-fine-days-late.apl) | أيام سماح ثم غرامة يومية بسقف لكل كتاب |
| 1944 | [`1944-disk-scheduling-sstf-total-movement.apl`](examples/1944-disk-scheduling-sstf-total-movement.apl) | نخدم الطلب الأقرب لرأس القرص ونجمع المسافات |
| 1945 | [`1945-disk-scheduling-scan-elevator-order.apl`](examples/1945-disk-scheduling-scan-elevator-order.apl) | نتحرك لأعلى نخدم الطلبات ثم نعود ونخدم الباقي |
| 1946 | [`1946-fifo-page-replacement-fault-count.apl`](examples/1946-fifo-page-replacement-fault-count.apl) | نطرد أقدم صفحة عند امتلاء الإطارات ونعد الأخطاء |
| 1947 | [`1947-lru-page-replacement-fault-count.apl`](examples/1947-lru-page-replacement-fault-count.apl) | نطرد الصفحة الأقدم استخداما ونعد الأخطاء |
| 1948 | [`1948-bank-overdraft-ledger-fees.apl`](examples/1948-bank-overdraft-ledger-fees.apl) | نطبق العمليات ونخصم رسما عند نزول الرصيد تحت الصفر |
| 1949 | [`1949-weighted-grade-book-average.apl`](examples/1949-weighted-grade-book-average.apl) | نضرب كل درجة بوزنها ونقسم على مجموع الأوزان |
| 1950 | [`1950-longest-warm-streak-days.apl`](examples/1950-longest-warm-streak-days.apl) | نعد الأيام المتتالية التي تتجاوز حدا معينا |
| 1951 | [`1951-word-ladder-shortest-length-bfs.apl`](examples/1951-word-ladder-shortest-length-bfs.apl) | بحث بالعرض عبر كلمات تختلف بحرف واحد |
| 1952 | [`1952-excel-column-title-from-number.apl`](examples/1952-excel-column-title-from-number.apl) | نحول رقم العمود إلى حروف على أساس 26 بدون صفر |
| 1953 | [`1953-excel-column-letters-to-index.apl`](examples/1953-excel-column-letters-to-index.apl) | نعامل الاسم كعدد بأساس 26 من 1 إلى 26 |
| 1954 | [`1954-collatz-longest-chain-start-below.apl`](examples/1954-collatz-longest-chain-start-below.apl) | نخزن أطوال السلاسل لتفادي إعادة الحساب |
| 1955 | [`1955-happy-number-cycle-detection-set.apl`](examples/1955-happy-number-cycle-detection-set.apl) | نكرر مجموع مربعات الأرقام حتى نصل 1 أو ندخل دورة |
| 1956 | [`1956-look-and-say-nth-term.apl`](examples/1956-look-and-say-nth-term.apl) | كل حد يصف الحد السابق بعد مجموعات الأرقام المتكررة |
| 1957 | [`1957-hamming-distance-sum-all-pairs.apl`](examples/1957-hamming-distance-sum-all-pairs.apl) | نعد لكل بت كم عددا فيه واحد وكم فيه صفر |
| 1958 | [`1958-luhn-card-number-validator.apl`](examples/1958-luhn-card-number-validator.apl) | نضاعف كل رقم ثان من اليمين ونتحقق من قابلية المجموع للقسمة على 10 |
| 1959 | [`1959-isbn-ten-checksum-validate.apl`](examples/1959-isbn-ten-checksum-validate.apl) | مجموع الأرقام مضروبة بأوزان من 10 إلى 1 يقبل القسمة على 11 |
| 1960 | [`1960-time-add-minutes-wrap-clock.apl`](examples/1960-time-add-minutes-wrap-clock.apl) | نحول الوقت إلى دقائق ونعيد الباقي على 1440 |
| 1961 | [`1961-day-of-year-with-leap-rule.apl`](examples/1961-day-of-year-with-leap-rule.apl) | نجمع أيام الأشهر السابقة ونراعي السنة الكبيسة |
| 1962 | [`1962-matrix-diagonal-difference-abs.apl`](examples/1962-matrix-diagonal-difference-abs.apl) | مجموع القطر الرئيسي ناقص مجموع القطر الثانوي |
| 1963 | [`1963-bulls-and-cows-score-guess.apl`](examples/1963-bulls-and-cows-score-guess.apl) | ثور لرقم صحيح في مكانه وبقرة لرقم صحيح في مكان خاطئ |
| 1964 | [`1964-merge-row-left-2048-rule.apl`](examples/1964-merge-row-left-2048-rule.apl) | نزيح الأرقام لليسار وندمج المتساوين المتجاورين مرة واحدة |
| 1965 | [`1965-minesweeper-neighbor-count-board.apl`](examples/1965-minesweeper-neighbor-count-board.apl) | لكل خلية خالية نعد الألغام في الخلايا الثماني المجاورة |
| 1966 | [`1966-bracket-min-insertions-balance.apl`](examples/1966-bracket-min-insertions-balance.apl) | نعد الإغلاقات الزائدة والفتحات غير المغلقة |
| 1967 | [`1967-run-length-encode-pairs-list.apl`](examples/1967-run-length-encode-pairs-list.apl) | نحول النص إلى قائمة أزواج حرف وعدد |
| 1968 | [`1968-pascal-triangle-row-sum-powers.apl`](examples/1968-pascal-triangle-row-sum-powers.apl) | مجموع الصف ن يساوي 2 أس ن |
| 1969 | [`1969-tennis-game-score-from-points.apl`](examples/1969-tennis-game-score-from-points.apl) | نحول النقاط إلى 15 و30 و40 مع التعادل والأفضلية |
| 1970 | [`1970-bowling-score-ten-frames.apl`](examples/1970-bowling-score-ten-frames.apl) | الضربة القاضية والضربة الاحتياطية تضيفان نقاط الرميات التالية |
| 1971 | [`1971-stair-climb-ways-one-two-three.apl`](examples/1971-stair-climb-ways-one-two-three.apl) | عدد الطرق للدرجة ن مجموع الطرق للثلاث درجات قبلها |
| 1972 | [`1972-longest-run-in-coin-flips.apl`](examples/1972-longest-run-in-coin-flips.apl) | نعد أطول سلسلة متطابقة من H أو T |
| 1973 | [`1973-snake-case-to-title-words.apl`](examples/1973-snake-case-to-title-words.apl) | نقسم عند الشرطة السفلية ونكبر أول حرف في كل جزء |
| 1974 | [`1974-phone-keypad-combination-count.apl`](examples/1974-phone-keypad-combination-count.apl) | نضرب عدد الأحرف على كل زر |
| 1975 | [`1975-t9-word-to-digit-sequence.apl`](examples/1975-t9-word-to-digit-sequence.apl) | كل حرف يقابل الزر الذي يحمله |
| 1976 | [`1976-seven-segment-lit-segments-total.apl`](examples/1976-seven-segment-lit-segments-total.apl) | كل رقم يضيء عددا ثابتا من القطع |
| 1977 | [`1977-binary-nibble-grouped-string.apl`](examples/1977-binary-nibble-grouped-string.apl) | نملأ بأصفار حتى مضاعف الأربعة ونفصل بشرطة سفلية |
| 1978 | [`1978-ipv4-address-format-validate.apl`](examples/1978-ipv4-address-format-validate.apl) | أربعة أجزاء رقمية بين 0 و255 بلا أصفار بادئة |
| 1979 | [`1979-ipv4-to-integer-and-back.apl`](examples/1979-ipv4-to-integer-and-back.apl) | العنوان أربع خانات بأساس 256 |
| 1980 | [`1980-cidr-usable-host-count.apl`](examples/1980-cidr-usable-host-count.apl) | عدد العناوين اثنان أس 32 ناقص البادئة ناقص عنوانين محجوزين |
| 1981 | [`1981-hex-color-to-rgb-triple.apl`](examples/1981-hex-color-to-rgb-triple.apl) | نقرأ كل زوج حروف كعدد بأساس 16 |
| 1982 | [`1982-rgb-to-gray-luma-integer.apl`](examples/1982-rgb-to-gray-luma-integer.apl) | مجموع موزون بأوزان 299 و587 و114 على 1000 |
| 1983 | [`1983-mac-address-normalize-format.apl`](examples/1983-mac-address-normalize-format.apl) | نزيل الفواصل المختلفة ونكتب بحروف صغيرة مع نقطتين |
| 1984 | [`1984-semantic-version-compare-three-parts.apl`](examples/1984-semantic-version-compare-three-parts.apl) | نقارن الأجزاء رقميا ونكمل الناقص بأصفار |
| 1985 | [`1985-file-size-human-readable-units.apl`](examples/1985-file-size-human-readable-units.apl) | نقسم على 1024 حتى نصل لوحدة مناسبة |
| 1986 | [`1986-seconds-to-hours-minutes-seconds-text.apl`](examples/1986-seconds-to-hours-minutes-seconds-text.apl) | نقسم على 3600 ثم 60 ونملأ الصفر البادئ |
| 1987 | [`1987-pluralize-count-with-noun-rules.apl`](examples/1987-pluralize-count-with-noun-rules.apl) | نضيف s أو es أو نبدل y بـ ies حسب آخر الاسم |
| 1988 | [`1988-balanced-ternary-digits-from-int.apl`](examples/1988-balanced-ternary-digits-from-int.apl) | الخانات 1 و0 وT حيث T تساوي ناقص واحد |
| 1989 | [`1989-negabinary-digits-from-int.apl`](examples/1989-negabinary-digits-from-int.apl) | الأساس ناقص اثنين يمثل كل الأعداد بلا إشارة |
| 1990 | [`1990-factorial-trailing-zeros-count-fives.apl`](examples/1990-factorial-trailing-zeros-count-fives.apl) | عدد الأصفار يساوي عدد الخماسات في العوامل |
| 1991 | [`1991-count-digit-occurrences-up-to-n.apl`](examples/1991-count-digit-occurrences-up-to-n.apl) | نمر على كل عدد من 1 إلى ن ونعد الرقم المطلوب |
| 1992 | [`1992-abundant-deficient-perfect-classify.apl`](examples/1992-abundant-deficient-perfect-classify.apl) | نقارن مجموع القواسم الحقيقية بالعدد نفسه |
| 1993 | [`1993-text-pyramid-rows-centered.apl`](examples/1993-text-pyramid-rows-centered.apl) | كل صف يضيف نجمتين مع مسافات بادئة |
| 1994 | [`1994-matrix-zigzag-diagonal-traverse.apl`](examples/1994-matrix-zigzag-diagonal-traverse.apl) | نجمع خلايا كل قطر ونعكس الاتجاه بالتناوب |
| 1995 | [`1995-count-pairs-with-given-difference.apl`](examples/1995-count-pairs-with-given-difference.apl) | نبحث عن القيمة زائد الفارق في مجموعة القيم الفريدة |
| 1996 | [`1996-reverse-first-k-elements-of-list.apl`](examples/1996-reverse-first-k-elements-of-list.apl) | نقتطع البداية ونعكسها ثم نلصق الباقي |
| 1997 | [`1997-rotate-list-left-by-k-steps.apl`](examples/1997-rotate-list-left-by-k-steps.apl) | نأخذ ك باقي القسمة على الطول ونبدل الجزءين |
| 1998 | [`1998-missing-number-xor-trick.apl`](examples/1998-missing-number-xor-trick.apl) | نجري XOR على كل الفهارس وكل القيم فيبقى العدد الناقص |
| 1999 | [`1999-single-number-among-pairs-xor.apl`](examples/1999-single-number-among-pairs-xor.apl) | XOR لكل القيم يلغي الأزواج |
| 2000 | [`2000-two-sum-sorted-two-pointers.apl`](examples/2000-two-sum-sorted-two-pointers.apl) | مؤشر من كل طرف نقربهما حسب المجموع |
| 2001 | [`2001-three-sum-zero-unique-triplet-count.apl`](examples/2001-three-sum-zero-unique-triplet-count.apl) | نرتب ونثبت عنصرا ونبحث عن الباقي بمؤشرين |
| 2002 | [`2002-container-with-most-water-area.apl`](examples/2002-container-with-most-water-area.apl) | المساحة تحددها الأقصر من الجدارين والمسافة بينهما |
| 2003 | [`2003-remove-value-from-list-new-copy.apl`](examples/2003-remove-value-from-list-new-copy.apl) | نبني قائمة بكل العناصر المختلفة عن القيمة |
| 2004 | [`2004-move-zeroes-to-end-stable.apl`](examples/2004-move-zeroes-to-end-stable.apl) | نحافظ على ترتيب غير الأصفار |
| 2005 | [`2005-majority-element-boyer-moore-vote.apl`](examples/2005-majority-element-boyer-moore-vote.apl) | مرشح وعداد يلغي الأصوات المتعارضة |
| 2006 | [`2006-max-consecutive-ones-with-k-flips.apl`](examples/2006-max-consecutive-ones-with-k-flips.apl) | نافذة متحركة تسمح بعدد محدود من الأصفار |
| 2007 | [`2007-subarray-sum-equals-k-prefix-map.apl`](examples/2007-subarray-sum-equals-k-prefix-map.apl) | مجموع البادئات وقاموس تكرارها |
| 2008 | [`2008-longest-consecutive-run-hash-set.apl`](examples/2008-longest-consecutive-run-hash-set.apl) | نبدأ العد من الأعداد التي لا يسبقها عدد في المجموعة |
| 2009 | [`2009-valid-mountain-array-check.apl`](examples/2009-valid-mountain-array-check.apl) | تصعد بشدة ثم تنزل بشدة بقمة داخلية |
| 2010 | [`2010-find-peak-element-binary-search.apl`](examples/2010-find-peak-element-binary-search.apl) | نتحرك نحو الجار الأكبر |
| 2011 | [`2011-search-in-rotated-sorted-list.apl`](examples/2011-search-in-rotated-sorted-list.apl) | نحدد النصف المرتب في كل خطوة |
| 2012 | [`2012-first-last-position-sorted-target.apl`](examples/2012-first-last-position-sorted-target.apl) | حد أدنى للقيمة وحد أدنى للقيمة التالية |
| 2013 | [`2013-integer-sqrt-newton-iteration.apl`](examples/2013-integer-sqrt-newton-iteration.apl) | نكرر المتوسط حتى لا ينقص التقدير |
| 2014 | [`2014-modular-power-square-and-multiply.apl`](examples/2014-modular-power-square-and-multiply.apl) | نربع الأساس ونضرب عند البت الواحد في الأس |
| 2015 | [`2015-nth-ugly-number-three-pointers.apl`](examples/2015-nth-ugly-number-three-pointers.apl) | أعداد عواملها الأولية 2 و3 و5 فقط |
| 2016 | [`2016-goldbach-smallest-prime-pair.apl`](examples/2016-goldbach-smallest-prime-pair.apl) | نجد أصغر أولي يكمل العدد الزوجي إلى أولي |
| 2017 | [`2017-twin-primes-pairs-up-to-limit.apl`](examples/2017-twin-primes-pairs-up-to-limit.apl) | أوليان يفصل بينهما عدد زوجي واحد |
| 2018 | [`2018-prime-factorization-exponent-pairs.apl`](examples/2018-prime-factorization-exponent-pairs.apl) | نرجع قائمة أزواج العامل والأس |
| 2019 | [`2019-euler-totient-from-prime-factors.apl`](examples/2019-euler-totient-from-prime-factors.apl) | لكل عامل أولي نضرب في واحد ناقص مقلوبه |
| 2020 | [`2020-modular-inverse-brute-force-search.apl`](examples/2020-modular-inverse-brute-force-search.apl) | نبحث عن x يجعل a*x يساوي 1 بالباقي m |
| 2021 | [`2021-chinese-remainder-two-moduli-search.apl`](examples/2021-chinese-remainder-two-moduli-search.apl) | نبحث في مضاعفات حاصل ضرب المقياسين |
| 2022 | [`2022-fraction-add-reduced-lowest-terms.apl`](examples/2022-fraction-add-reduced-lowest-terms.apl) | نوحد المقامات ونقسم على القاسم المشترك الأكبر |
| 2023 | [`2023-continued-fraction-of-rational-number.apl`](examples/2023-continued-fraction-of-rational-number.apl) | نكرر القسمة الصحيحة كخوارزمية إقليدس |
| 2024 | [`2024-egyptian-fraction-greedy-expansion.apl`](examples/2024-egyptian-fraction-greedy-expansion.apl) | نطرح أكبر كسر وحدة ممكن في كل خطوة |
| 2025 | [`2025-farey-sequence-term-count.apl`](examples/2025-farey-sequence-term-count.apl) | نولد الحد التالي من الحدين السابقين بصيغة مباشرة |
| 2026 | [`2026-reverse-word-order-collapse-spaces.apl`](examples/2026-reverse-word-order-collapse-spaces.apl) | نقسم عند المسافات ونعكس القائمة ونجمعها بمسافة واحدة |
| 2027 | [`2027-is-subsequence-two-pointer-scan.apl`](examples/2027-is-subsequence-two-pointer-scan.apl) | نمشي على النص الثاني ونطابق حروف الأول بالترتيب |
| 2028 | [`2028-common-prefix-shrink-until-match.apl`](examples/2028-common-prefix-shrink-until-match.apl) | نقص البادئة حتى تبدأ بها كل كلمة |
| 2029 | [`2029-compress-repeats-only-if-shorter.apl`](examples/2029-compress-repeats-only-if-shorter.apl) | نكتب الحرف وعدده ونرجع الأصل إن لم يقصر |
| 2030 | [`2030-one-edit-distance-string-check.apl`](examples/2030-one-edit-distance-string-check.apl) | إدراج أو حذف أو استبدال حرف واحد |
| 2031 | [`2031-isomorphic-strings-two-way-map.apl`](examples/2031-isomorphic-strings-two-way-map.apl) | كل حرف يقابل حرفا واحدا في الاتجاهين |
| 2032 | [`2032-word-pattern-bijection-check.apl`](examples/2032-word-pattern-bijection-check.apl) | كل حرف يقابل كلمة واحدة والعكس |
| 2033 | [`2033-first-unique-character-position.apl`](examples/2033-first-unique-character-position.apl) | نعد التكرارات ثم نبحث عن أول عدد يساوي واحد |
| 2034 | [`2034-ransom-note-letter-budget.apl`](examples/2034-ransom-note-letter-budget.apl) | نخصم حروف الرسالة من رصيد حروف المجلة |
| 2035 | [`2035-string-rotation-doubled-search.apl`](examples/2035-string-rotation-doubled-search.apl) | نبحث عن الأول داخل الثاني مكررا مرتين |
| 2036 | [`2036-substring-count-overlapping-matches.apl`](examples/2036-substring-count-overlapping-matches.apl) | نفحص كل موضع بداية ممكن |
| 2037 | [`2037-characters-sorted-by-frequency-desc.apl`](examples/2037-characters-sorted-by-frequency-desc.apl) | الأكثر تكرارا أولا والتعادل بالترتيب الأبجدي |
| 2038 | [`2038-palindrome-allow-one-deletion.apl`](examples/2038-palindrome-allow-one-deletion.apl) | عند أول اختلاف نجرب حذف أحد الحرفين |
| 2039 | [`2039-longest-unique-substring-last-seen.apl`](examples/2039-longest-unique-substring-last-seen.apl) | نخزن آخر موضع لكل حرف ونحرك بداية النافذة |
| 2040 | [`2040-reverse-integer-with-32-bit-guard.apl`](examples/2040-reverse-integer-with-32-bit-guard.apl) | نرجع صفرا إن تجاوز المعكوس حد 32 بت |
| 2041 | [`2041-palindrome-number-reverse-half.apl`](examples/2041-palindrome-number-reverse-half.apl) | نعكس نصف الأرقام فقط ونقارن |
| 2042 | [`2042-add-binary-strings-with-carry.apl`](examples/2042-add-binary-strings-with-carry.apl) | نجمع من اليمين مع الحمل |
| 2043 | [`2043-add-decimal-strings-manual-carry.apl`](examples/2043-add-decimal-strings-manual-carry.apl) | جمع خانة بخانة مع حمل |
| 2044 | [`2044-plus-one-digit-list-carry.apl`](examples/2044-plus-one-digit-list-carry.apl) | نمشي من اليمين ونحمل عند التسعة |
| 2045 | [`2045-count-set-bits-for-zero-to-n.apl`](examples/2045-count-set-bits-for-zero-to-n.apl) | عدد بتات i يساوي عدد بتات i/2 زائد آخر بت |
| 2046 | [`2046-power-of-base-check-by-division.apl`](examples/2046-power-of-base-check-by-division.apl) | نقسم على الأساس طالما يقبل القسمة |
| 2047 | [`2047-reverse-bits-of-32-bit-integer.apl`](examples/2047-reverse-bits-of-32-bit-integer.apl) | نأخذ آخر بت ونضعه في بداية الناتج 32 مرة |
| 2048 | [`2048-hamming-weight-kernighan-loop.apl`](examples/2048-hamming-weight-kernighan-loop.apl) | كل خطوة تمسح أقل بت واحد |
| 2049 | [`2049-number-complement-flip-all-bits.apl`](examples/2049-number-complement-flip-all-bits.apl) | نصنع قناعا من آحاد بطول العدد ونطبق XOR |
| 2050 | [`2050-bitwise-and-of-number-range-prefix.apl`](examples/2050-bitwise-and-of-number-range-prefix.apl) | النتيجة هي البادئة الثنائية المشتركة بين الطرفين |
| 2051 | [`2051-add-two-integers-with-xor-and-carry.apl`](examples/2051-add-two-integers-with-xor-and-carry.apl) | XOR يعطي المجموع بلا حمل وAND مزاحا يعطي الحمل |
| 2052 | [`2052-maximum-xor-of-any-pair-brute.apl`](examples/2052-maximum-xor-of-any-pair-brute.apl) | نجرب كل الأزواج ونحتفظ بالأكبر |
| 2053 | [`2053-gray-code-binary-conversion-both-ways.apl`](examples/2053-gray-code-binary-conversion-both-ways.apl) | غراي يساوي n XOR n>>1 والعكس بطي الإزاحات |
| 2054 | [`2054-parity-of-bits-xor-fold.apl`](examples/2054-parity-of-bits-xor-fold.apl) | نطوي العدد على نفسه بإزاحات متناقصة |
| 2055 | [`2055-insertion-sort-count-shifts.apl`](examples/2055-insertion-sort-count-shifts.apl) | كل إزاحة تعني عنصرا أكبر تجاوزناه |
| 2056 | [`2056-bubble-sort-swap-count-passes.apl`](examples/2056-bubble-sort-swap-count-passes.apl) | نبدل الجارين غير المرتبين ونعد التبديلات |
| 2057 | [`2057-selection-sort-compare-count.apl`](examples/2057-selection-sort-compare-count.apl) | عدد المقارنات ثابت مهما كان الترتيب |
| 2058 | [`2058-counting-sort-small-integer-range.apl`](examples/2058-counting-sort-small-integer-range.apl) | نعد كل قيمة ثم نكتبها بالترتيب |
| 2059 | [`2059-radix-sort-least-significant-digit.apl`](examples/2059-radix-sort-least-significant-digit.apl) | نوزع الأعداد على سلال حسب كل خانة |
| 2060 | [`2060-bucket-sort-by-tens-group.apl`](examples/2060-bucket-sort-by-tens-group.apl) | نوزع الأعداد من 0 إلى 99 على عشر سلال |
| 2061 | [`2061-merge-sorted-lists-drop-duplicates.apl`](examples/2061-merge-sorted-lists-drop-duplicates.apl) | نأخذ الأصغر ونتجاهل القيمة إن كررت الأخيرة |
| 2062 | [`2062-kth-largest-quickselect-partition.apl`](examples/2062-kth-largest-quickselect-partition.apl) | نقسم حول محور ونتابع في الجزء المناسب |
| 2063 | [`2063-order-numbers-by-count-then-size.apl`](examples/2063-order-numbers-by-count-then-size.apl) | الأقل تكرارا أولا وعند التعادل الأصغر قيمة |
| 2064 | [`2064-sort-colors-dutch-flag-three-way.apl`](examples/2064-sort-colors-dutch-flag-three-way.apl) | ثلاثة مؤشرات تفرز 0 و1 و2 بمرور واحد |
| 2065 | [`2065-wiggle-sort-adjacent-swaps.apl`](examples/2065-wiggle-sort-adjacent-swaps.apl) | نجعل القائمة صعودا ونزولا بالتناوب |
| 2066 | [`2066-transpose-rectangular-matrix.apl`](examples/2066-transpose-rectangular-matrix.apl) | العنصر i,j يصبح j,i |
| 2067 | [`2067-matrix-row-sums-and-column-sums.apl`](examples/2067-matrix-row-sums-and-column-sums.apl) | نرجع قائمتين من المجاميع |
| 2068 | [`2068-matrix-saddle-point-row-min-column-max.apl`](examples/2068-matrix-saddle-point-row-min-column-max.apl) | أصغر قيمة في صفها وأكبر قيمة في عمودها |
| 2069 | [`2069-matrix-symmetric-check-transpose-equal.apl`](examples/2069-matrix-symmetric-check-transpose-equal.apl) | العنصر i,j يساوي j,i لكل الأزواج |
| 2070 | [`2070-pascal-matrix-lower-triangular-build.apl`](examples/2070-pascal-matrix-lower-triangular-build.apl) | كل عنصر مجموع العنصر فوقه والذي قبله |
| 2071 | [`2071-matrix-trace-and-identity-build.apl`](examples/2071-matrix-trace-and-identity-build.apl) | الأثر مجموع القطر الرئيسي |
| 2072 | [`2072-fibonacci-by-2x2-matrix-power.apl`](examples/2072-fibonacci-by-2x2-matrix-power.apl) | نرفع مصفوفة فيبوناتشي إلى الأس ن بالتربيع |
| 2073 | [`2073-spiral-matrix-fill-n-by-n.apl`](examples/2073-spiral-matrix-fill-n-by-n.apl) | نكتب الأرقام من 1 حلزونيا |
| 2074 | [`2074-flood-fill-image-paint-bucket-stack.apl`](examples/2074-flood-fill-image-paint-bucket-stack.apl) | نلون كل الخلايا المتصلة بنفس اللون |
| 2075 | [`2075-game-of-life-blinker-oscillation.apl`](examples/2075-game-of-life-blinker-oscillation.apl) | النمط الوامض يعود لحاله بعد خطوتين |
| 2076 | [`2076-rotate-matrix-counterclockwise-ninety.apl`](examples/2076-rotate-matrix-counterclockwise-ninety.apl) | العمود الأخير يصبح الصف الأول |
| 2077 | [`2077-checkerboard-text-pattern-rows.apl`](examples/2077-checkerboard-text-pattern-rows.apl) | علامتان متناوبتان في كل صف |
| 2078 | [`2078-right-aligned-staircase-text.apl`](examples/2078-right-aligned-staircase-text.apl) | كل صف يزيد علامة ويقل مسافة |
| 2079 | [`2079-diamond-text-pattern-odd-width.apl`](examples/2079-diamond-text-pattern-odd-width.apl) | هرم ثم هرم مقلوب |
| 2080 | [`2080-simple-interest-and-final-amount.apl`](examples/2080-simple-interest-and-final-amount.apl) | الفائدة = الأصل × النسبة × المدة على 100 |
| 2081 | [`2081-percentage-change-rounded-one-decimal.apl`](examples/2081-percentage-change-rounded-one-decimal.apl) | الفرق على القيمة الأصلية مضروبا في 100 |
| 2082 | [`2082-chained-discounts-final-price.apl`](examples/2082-chained-discounts-final-price.apl) | كل خصم يطبق على السعر الناتج من الذي قبله |
| 2083 | [`2083-bill-split-with-tip-ceiling-cents.apl`](examples/2083-bill-split-with-tip-ceiling-cents.apl) | نقرب نصيب كل شخص لأعلى |
| 2084 | [`2084-change-making-greedy-coin-counts.apl`](examples/2084-change-making-greedy-coin-counts.apl) | نأخذ أكبر فئة ممكنة أولا |
| 2085 | [`2085-round-cents-to-nearest-five.apl`](examples/2085-round-cents-to-nearest-five.apl) | نضيف 2 ونقسم على 5 ونضرب |
| 2086 | [`2086-weekday-sakamoto-method.apl`](examples/2086-weekday-sakamoto-method.apl) | صيغة قصيرة تعطي 0 للأحد |
| 2087 | [`2087-days-between-dates-julian-day-number.apl`](examples/2087-days-between-dates-julian-day-number.apl) | نحول كل تاريخ إلى رقم يوم ونطرح |
| 2088 | [`2088-century-number-from-year.apl`](examples/2088-century-number-from-year.apl) | السنة 100 آخر القرن الأول |
| 2089 | [`2089-fizzbuzz-generalized-rule-list.apl`](examples/2089-fizzbuzz-generalized-rule-list.apl) | كل قاعدة قاسم وكلمة |
| 2090 | [`2090-clock-hands-smaller-angle.apl`](examples/2090-clock-hands-smaller-angle.apl) | عقرب الساعة 30 درجة للساعة و0.5 للدقيقة والدقائق 6 درجات |
| 2091 | [`2091-first-of-month-sundays-count-century.apl`](examples/2091-first-of-month-sundays-count-century.apl) | نعد أول الأشهر التي كانت أحدا بين 1901 و2000 |
| 2092 | [`2092-friday-thirteenth-count-in-year.apl`](examples/2092-friday-thirteenth-count-in-year.apl) | نفحص يوم 13 من كل شهر |
| 2093 | [`2093-tower-of-hanoi-move-list-recursive.apl`](examples/2093-tower-of-hanoi-move-list-recursive.apl) | ننقل ن-1 ثم القرص الأكبر ثم ن-1 مرة أخرى |
| 2094 | [`2094-ackermann-function-small-inputs.apl`](examples/2094-ackermann-function-small-inputs.apl) | دالة تنمو بسرعة هائلة |
| 2095 | [`2095-catalan-numbers-dp-convolution.apl`](examples/2095-catalan-numbers-dp-convolution.apl) | كل حد مجموع حاصل ضرب الحدود المتقابلة |
| 2096 | [`2096-bell-numbers-triangle-method.apl`](examples/2096-bell-numbers-triangle-method.apl) | أول عنصر في كل صف هو عدد بيل |
| 2097 | [`2097-stirling-second-kind-recurrence.apl`](examples/2097-stirling-second-kind-recurrence.apl) | عدد طرق تقسيم ن عنصرا إلى ك مجموعات |
| 2098 | [`2098-derangement-count-recurrence.apl`](examples/2098-derangement-count-recurrence.apl) | تبديلات لا يبقى فيها عنصر في مكانه |
| 2099 | [`2099-integer-partition-count-dp.apl`](examples/2099-integer-partition-count-dp.apl) | طرق كتابة العدد كمجموع أعداد موجبة |
| 2100 | [`2100-binomial-coefficient-multiplicative-loop.apl`](examples/2100-binomial-coefficient-multiplicative-loop.apl) | نضرب ونقسم تباعا لنتجنب المضروب الكبير |
| 2101 | [`2101-lucas-numbers-first-terms.apl`](examples/2101-lucas-numbers-first-terms.apl) | تبدأ بـ 2 و1 وكل حد مجموع السابقين |
| 2102 | [`2102-tribonacci-nth-iterative.apl`](examples/2102-tribonacci-nth-iterative.apl) | كل حد مجموع ثلاثة حدود سابقة |
| 2103 | [`2103-padovan-sequence-terms-list.apl`](examples/2103-padovan-sequence-terms-list.apl) | كل حد مجموع الحدين قبل الأخير بخطوة وخطوتين |
| 2104 | [`2104-digit-sum-repeat-until-one-digit.apl`](examples/2104-digit-sum-repeat-until-one-digit.apl) | نكرر جمع الأرقام حتى يبقى رقم واحد |
| 2105 | [`2105-narcissistic-numbers-three-digits-list.apl`](examples/2105-narcissistic-numbers-three-digits-list.apl) | العدد يساوي مجموع مكعبات أرقامه |
| 2106 | [`2106-automorphic-number-square-ends-with.apl`](examples/2106-automorphic-number-square-ends-with.apl) | مربعه ينتهي بنفسه |
| 2107 | [`2107-kaprekar-number-split-square-check.apl`](examples/2107-kaprekar-number-split-square-check.apl) | نقسم المربع إلى جزأين مجموعهما العدد |
| 2108 | [`2108-perfect-power-base-exponent-test.apl`](examples/2108-perfect-power-base-exponent-test.apl) | نجرب كل أساس ونرفعه حتى نبلغ العدد |
| 2109 | [`2109-sum-of-two-squares-representable.apl`](examples/2109-sum-of-two-squares-representable.apl) | نجرب كل زوج أول لا يتجاوز الجذر |
| 2110 | [`2110-pythagorean-triples-hypotenuse-limit-count.apl`](examples/2110-pythagorean-triples-hypotenuse-limit-count.apl) | نعد الثلاثيات a<b<c بوتر لا يتجاوز الحد |
| 2111 | [`2111-gcd-of-fibonacci-numbers-property.apl`](examples/2111-gcd-of-fibonacci-numbers-property.apl) | gcd(F(m),F(n)) = F(gcd(m,n)) |
| 2112 | [`2112-sum-of-primes-below-limit-trial.apl`](examples/2112-sum-of-primes-below-limit-trial.apl) | نجمع كل أولي أصغر من الحد |
| 2113 | [`2113-nth-prime-by-counting-primes.apl`](examples/2113-nth-prime-by-counting-primes.apl) | نعد الأوليات حتى نبلغ الترتيب المطلوب |
| 2114 | [`2114-largest-prime-gap-below-limit.apl`](examples/2114-largest-prime-gap-below-limit.apl) | نتتبع الفرق بين كل أولي والسابق |
| 2115 | [`2115-emirp-prime-whose-reverse-is-prime.apl`](examples/2115-emirp-prime-whose-reverse-is-prime.apl) | أولي ومعكوس أرقامه أولي مختلف عنه |
| 2116 | [`2116-circular-prime-all-rotations-prime.apl`](examples/2116-circular-prime-all-rotations-prime.apl) | كل دوران لأرقامه أولي |
| 2117 | [`2117-sophie-germain-prime-double-plus-one.apl`](examples/2117-sophie-germain-prime-double-plus-one.apl) | p أولي و2p+1 أولي أيضا |
| 2118 | [`2118-mersenne-primes-for-small-exponents.apl`](examples/2118-mersenne-primes-for-small-exponents.apl) | نختبر 2 أس p ناقص 1 للأسس الأولية |
| 2119 | [`2119-perfect-numbers-from-mersenne-primes.apl`](examples/2119-perfect-numbers-from-mersenne-primes.apl) | العدد التام يساوي 2^(p-1) × (2^p-1) |
| 2120 | [`2120-factorion-digit-factorial-sum-check.apl`](examples/2120-factorion-digit-factorial-sum-check.apl) | 145 يساوي 1!+4!+5! |
| 2121 | [`2121-reverse-and-add-steps-to-palindrome.apl`](examples/2121-reverse-and-add-steps-to-palindrome.apl) | نجمع العدد مع معكوسه حتى يصير متماثلا |
| 2122 | [`2122-harmonic-number-partial-sum-rounded.apl`](examples/2122-harmonic-number-partial-sum-rounded.apl) | H(n) مجموع مقلوبات 1 إلى n |
| 2123 | [`2123-geometric-series-sum-closed-form.apl`](examples/2123-geometric-series-sum-closed-form.apl) | a(r^n - 1)/(r - 1) عندما r لا يساوي 1 |
| 2124 | [`2124-arithmetic-series-term-and-sum.apl`](examples/2124-arithmetic-series-term-and-sum.apl) | الحد n = a + (n-1)d |
| 2125 | [`2125-triangular-number-index-or-minus-one.apl`](examples/2125-triangular-number-index-or-minus-one.apl) | نجد k الذي يحقق k(k+1)/2 = n |
| 2126 | [`2126-ways-to-write-as-consecutive-sum.apl`](examples/2126-ways-to-write-as-consecutive-sum.apl) | نبدأ من كل عدد ونجمع حتى نبلغ العدد |
| 2127 | [`2127-pentagonal-numbers-first-terms.apl`](examples/2127-pentagonal-numbers-first-terms.apl) | الحد n يساوي n(3n-1)/2 |
| 2128 | [`2128-hexagonal-number-membership-test.apl`](examples/2128-hexagonal-number-membership-test.apl) | الحد n يساوي n(2n-1) |
| 2129 | [`2129-centered-hexagonal-numbers-list.apl`](examples/2129-centered-hexagonal-numbers-list.apl) | الحد n يساوي 3n(n-1)+1 |
| 2130 | [`2130-ulam-numbers-first-terms.apl`](examples/2130-ulam-numbers-first-terms.apl) | كل حد له تمثيل وحيد كمجموع حدين مختلفين سابقين |
| 2131 | [`2131-kaprekar-routine-steps-to-6174.apl`](examples/2131-kaprekar-routine-steps-to-6174.apl) | نطرح الأصغر من الأكبر لأرقام العدد حتى 6174 |
| 2132 | [`2132-vowel-count-for-each-word.apl`](examples/2132-vowel-count-for-each-word.apl) | نرجع قائمة بعدد العلل لكل كلمة |
| 2133 | [`2133-title-case-keep-small-words-lower.apl`](examples/2133-title-case-keep-small-words-lower.apl) | الكلمات الصغيرة تبقى صغيرة إلا في أول العنوان |
| 2134 | [`2134-acronym-from-phrase-initials.apl`](examples/2134-acronym-from-phrase-initials.apl) | نأخذ أول حرف من كل كلمة ونكبره |
| 2135 | [`2135-syllable-estimate-by-vowel-groups.apl`](examples/2135-syllable-estimate-by-vowel-groups.apl) | كل مجموعة علل متتالية مقطع واحد |
| 2136 | [`2136-longest-character-run-with-its-char.apl`](examples/2136-longest-character-run-with-its-char.apl) | نرجع الحرف وطول أطول مجموعة |
| 2137 | [`2137-caesar-shift-between-two-words.apl`](examples/2137-caesar-shift-between-two-words.apl) | نحدد الإزاحة الثابتة التي تحول الأولى للثانية |
| 2138 | [`2138-hamming-distance-between-two-strings.apl`](examples/2138-hamming-distance-between-two-strings.apl) | عدد المواضع المختلفة بين نصين بنفس الطول |
| 2139 | [`2139-swap-letter-case-with-ascii-codes.apl`](examples/2139-swap-letter-case-with-ascii-codes.apl) | نضيف 32 للكبيرة ونطرحها من الصغيرة |
| 2140 | [`2140-count-upper-lower-digit-characters.apl`](examples/2140-count-upper-lower-digit-characters.apl) | ثلاثة عدادات في مرور واحد |
| 2141 | [`2141-pangram-missing-letters-string.apl`](examples/2141-pangram-missing-letters-string.apl) | نرجع الأحرف التي لم تظهر |
| 2142 | [`2142-longest-common-substring-dp-table.apl`](examples/2142-longest-common-substring-dp-table.apl) | جدول يمتد قطريا عند تطابق الحرفين |
| 2143 | [`2143-count-distinct-substrings-small-string.apl`](examples/2143-count-distinct-substrings-small-string.apl) | نجمع كل الشرائح في قاموس |
| 2144 | [`2144-lexicographically-smallest-string-rotation.apl`](examples/2144-lexicographically-smallest-string-rotation.apl) | نقارن كل الدورانات |
| 2145 | [`2145-generate-all-balanced-parentheses.apl`](examples/2145-generate-all-balanced-parentheses.apl) | نضيف فتحة إن بقي منها وإغلاقا إن زاد عدد الفتحات |
| 2146 | [`2146-binary-strings-without-adjacent-ones-count.apl`](examples/2146-binary-strings-without-adjacent-ones-count.apl) | يتبع فيبوناتشي |
| 2147 | [`2147-permutation-lexicographic-rank-factorial.apl`](examples/2147-permutation-lexicographic-rank-factorial.apl) | نعد الحروف الأصغر المتبقية ونضرب بالمضروب |
| 2148 | [`2148-nth-permutation-of-string-factoradic.apl`](examples/2148-nth-permutation-of-string-factoradic.apl) | نختار الحرف بقسمة الرتبة على المضروب |
| 2149 | [`2149-min-stack-class-constant-time-minimum.apl`](examples/2149-min-stack-class-constant-time-minimum.apl) | مكدس ثان يتتبع الأصغر |
| 2150 | [`2150-counter-class-step-and-reset.apl`](examples/2150-counter-class-step-and-reset.apl) | قيمة تزيد بخطوة محددة |
| 2151 | [`2151-bank-account-class-no-overdraft.apl`](examples/2151-bank-account-class-no-overdraft.apl) | السحب يفشل إن زاد عن الرصيد |
| 2152 | [`2152-rectangle-class-area-perimeter-square.apl`](examples/2152-rectangle-class-area-perimeter-square.apl) | المساحة والمحيط وهل هو مربع |
| 2153 | [`2153-fraction-class-add-and-reduce.apl`](examples/2153-fraction-class-add-and-reduce.apl) | الجمع يرجع كسرا مختصرا |
| 2154 | [`2154-vector-two-d-class-add-dot.apl`](examples/2154-vector-two-d-class-add-dot.apl) | الجمع والضرب النقطي والطول المربع |
| 2155 | [`2155-playlist-class-next-previous-wrap.apl`](examples/2155-playlist-class-next-previous-wrap.apl) | التنقل يلتف بين البداية والنهاية |
| 2156 | [`2156-inventory-class-add-remove-stock.apl`](examples/2156-inventory-class-add-remove-stock.apl) | الكميات في قاموس والسحب لا يتجاوز المتاح |
| 2157 | [`2157-todo-list-class-complete-and-remaining.apl`](examples/2157-todo-list-class-complete-and-remaining.apl) | نضيف المهام وننجزها ونعد المتبقي |
| 2158 | [`2158-shopping-cart-class-total-with-discount.apl`](examples/2158-shopping-cart-class-total-with-discount.apl) | المجموع بعد خصم نسبة مئوية |
| 2159 | [`2159-sum-multiples-of-seven-below-limit.apl`](examples/2159-sum-multiples-of-seven-below-limit.apl) | نجمع مضاعفات 7 الأصغر من ن |
| 2160 | [`2160-count-digits-equal-to-three-in-range.apl`](examples/2160-count-digits-equal-to-three-in-range.apl) | نعد الأعداد من 1 إلى ن التي فيها 3 |
| 2161 | [`2161-sum-of-squares-of-digits-total.apl`](examples/2161-sum-of-squares-of-digits-total.apl) | نربع كل رقم ونجمع |
| 2162 | [`2162-product-of-digits-nonzero-only.apl`](examples/2162-product-of-digits-nonzero-only.apl) | نتجاهل الأصفار في الضرب |
| 2163 | [`2163-count-even-digits-in-number.apl`](examples/2163-count-even-digits-in-number.apl) | نعد الأرقام الزوجية |
| 2164 | [`2164-largest-digit-of-number.apl`](examples/2164-largest-digit-of-number.apl) | نبحث عن أكبر رقم |
| 2165 | [`2165-smallest-digit-of-number.apl`](examples/2165-smallest-digit-of-number.apl) | نبحث عن أصغر رقم |
| 2166 | [`2166-reverse-digits-as-number.apl`](examples/2166-reverse-digits-as-number.apl) | نعكس النص ونحوله لعدد |
| 2167 | [`2167-is-number-palindrome-digits.apl`](examples/2167-is-number-palindrome-digits.apl) | نقارن العدد بمعكوسه |
| 2168 | [`2168-count-trailing-zeros-of-number.apl`](examples/2168-count-trailing-zeros-of-number.apl) | نقسم على 10 ما دام ممكنا |
| 2169 | [`2169-factorial-trailing-zeros-count.apl`](examples/2169-factorial-trailing-zeros-count.apl) | نجمع ن//5 ثم ن//25 وهكذا |
| 2170 | [`2170-triangular-number-formula-check.apl`](examples/2170-triangular-number-formula-check.apl) | ن(ن+1)/2 |
| 2171 | [`2171-pentagonal-number-formula.apl`](examples/2171-pentagonal-number-formula.apl) | ن(3ن-1)/2 |
| 2172 | [`2172-hexagonal-number-formula.apl`](examples/2172-hexagonal-number-formula.apl) | ن(2ن-1) |
| 2173 | [`2173-centered-square-number-formula.apl`](examples/2173-centered-square-number-formula.apl) | ن²+(ن-1)² |
| 2174 | [`2174-pronic-number-product-of-consecutive.apl`](examples/2174-pronic-number-product-of-consecutive.apl) | ن(ن+1) |
| 2175 | [`2175-sum-of-cubes-first-n-loop.apl`](examples/2175-sum-of-cubes-first-n-loop.apl) | نجمع ي³ بحلقة |
| 2176 | [`2176-sum-of-odd-numbers-first-n.apl`](examples/2176-sum-of-odd-numbers-first-n.apl) | يساوي ن² |
| 2177 | [`2177-count-divisors-by-trial.apl`](examples/2177-count-divisors-by-trial.apl) | نجرب كل عدد |
| 2178 | [`2178-sum-proper-divisors-total.apl`](examples/2178-sum-proper-divisors-total.apl) | نستثني العدد نفسه |
| 2179 | [`2179-is-perfect-number-by-divisors.apl`](examples/2179-is-perfect-number-by-divisors.apl) | مجموع القواسم الفعلية يساوي العدد |
| 2180 | [`2180-is-abundant-number-check.apl`](examples/2180-is-abundant-number-check.apl) | مجموع قواسمه أكبر منه |
| 2181 | [`2181-is-deficient-number-check.apl`](examples/2181-is-deficient-number-check.apl) | مجموع قواسمه أقل منه |
| 2182 | [`2182-largest-prime-factor-simple.apl`](examples/2182-largest-prime-factor-simple.apl) | نقسم على العوامل تباعا |
| 2183 | [`2183-count-distinct-prime-factors.apl`](examples/2183-count-distinct-prime-factors.apl) | نعد كل عامل مرة |
| 2184 | [`2184-euler-totient-by-gcd-count.apl`](examples/2184-euler-totient-by-gcd-count.apl) | نعد الأعداد الأولية نسبيا |
| 2185 | [`2185-collatz-steps-to-one-count.apl`](examples/2185-collatz-steps-to-one-count.apl) | نطبق القاعدة حتى 1 |
| 2186 | [`2186-binary-ones-count-loop.apl`](examples/2186-binary-ones-count-loop.apl) | نقسم على 2 |
| 2187 | [`2187-binary-length-of-number.apl`](examples/2187-binary-length-of-number.apl) | عدد الخانات الثنائية |
| 2188 | [`2188-is-power-of-two-bit-trick.apl`](examples/2188-is-power-of-two-bit-trick.apl) | ن & (ن-1) يساوي صفر |
| 2189 | [`2189-next-power-of-two-at-least.apl`](examples/2189-next-power-of-two-at-least.apl) | نضاعف حتى نصل |
| 2190 | [`2190-xor-of-range-one-to-n.apl`](examples/2190-xor-of-range-one-to-n.apl) | نطبق XOR تراكميا |
| 2191 | [`2191-gray-code-of-number.apl`](examples/2191-gray-code-of-number.apl) | ن ^ (ن >> 1) |
| 2192 | [`2192-fibonacci-mod-ten-last-digit.apl`](examples/2192-fibonacci-mod-ten-last-digit.apl) | نحتفظ بالباقي |
| 2193 | [`2193-tribonacci-nth-term-loop.apl`](examples/2193-tribonacci-nth-term-loop.apl) | مجموع ثلاثة سابقة |
| 2194 | [`2194-lucas-number-nth-loop.apl`](examples/2194-lucas-number-nth-loop.apl) | يبدأ 2 و1 |
| 2195 | [`2195-catalan-number-by-recurrence.apl`](examples/2195-catalan-number-by-recurrence.apl) | ك(ن+1)=ك(ن)*2(2ن+1)/(ن+2) |
| 2196 | [`2196-central-binomial-coefficient.apl`](examples/2196-central-binomial-coefficient.apl) | (2ن اختر ن) |
| 2197 | [`2197-stirling-triangle-row-sum-bell.apl`](examples/2197-stirling-triangle-row-sum-bell.apl) | مثلث بيل |
| 2198 | [`2198-digital-root-formula-mod-nine.apl`](examples/2198-digital-root-formula-mod-nine.apl) | 1+(ن-1)%9 |
| 2199 | [`2199-harshad-number-divisible-by-digit-sum.apl`](examples/2199-harshad-number-divisible-by-digit-sum.apl) | يقبل القسمة على مجموع أرقامه |
| 2200 | [`2200-happy-number-cycle-detect.apl`](examples/2200-happy-number-cycle-detect.apl) | نكرر مجموع مربعات الأرقام |
| 2201 | [`2201-smith-like-digit-sum-equals-factor-sum.apl`](examples/2201-smith-like-digit-sum-equals-factor-sum.apl) | مجموع أرقامه يساوي مجموع أرقام عوامله |
| 2202 | [`2202-count-vowels-latin-letters.apl`](examples/2202-count-vowels-latin-letters.apl) | نعد aeiou |
| 2203 | [`2203-count-uppercase-letters-in-text.apl`](examples/2203-count-uppercase-letters-in-text.apl) | نعد الأحرف الكبيرة |
| 2204 | [`2204-count-digits-in-text.apl`](examples/2204-count-digits-in-text.apl) | نعد الأرقام |
| 2205 | [`2205-swap-case-by-ord-offset.apl`](examples/2205-swap-case-by-ord-offset.apl) | نستخدم ord وchr |
| 2206 | [`2206-caesar-shift-three-lowercase.apl`](examples/2206-caesar-shift-three-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2207 | [`2207-alphabet-position-sum-of-word.apl`](examples/2207-alphabet-position-sum-of-word.apl) | a=1 ... z=26 |
| 2208 | [`2208-is-isogram-no-repeated-letters.apl`](examples/2208-is-isogram-no-repeated-letters.apl) | لا يتكرر حرف |
| 2209 | [`2209-is-pangram-all-letters-present.apl`](examples/2209-is-pangram-all-letters-present.apl) | كل حروف a-z |
| 2210 | [`2210-first-repeated-character-in-text.apl`](examples/2210-first-repeated-character-in-text.apl) | أول حرف يظهر ثانية |
| 2211 | [`2211-run-length-encode-compact-string.apl`](examples/2211-run-length-encode-compact-string.apl) | نكتب الحرف وعدده |
| 2212 | [`2212-longest-run-of-same-character.apl`](examples/2212-longest-run-of-same-character.apl) | أكبر تكرار متتال |
| 2213 | [`2213-remove-adjacent-duplicate-letters.apl`](examples/2213-remove-adjacent-duplicate-letters.apl) | نبقي حرفا واحدا للشوط |
| 2214 | [`2214-count-words-split-spaces.apl`](examples/2214-count-words-split-spaces.apl) | نقسم على المسافات |
| 2215 | [`2215-title-case-first-letters.apl`](examples/2215-title-case-first-letters.apl) | نكبر أول حرف |
| 2216 | [`2216-acronym-from-first-letters-upper.apl`](examples/2216-acronym-from-first-letters-upper.apl) | نأخذ أول حرف |
| 2217 | [`2217-hamming-weight-of-text-bits.apl`](examples/2217-hamming-weight-of-text-bits.apl) | نعد الآحاد لكل رمز |
| 2218 | [`2218-vowel-consonant-difference-text.apl`](examples/2218-vowel-consonant-difference-text.apl) | نطرح الصامتة من الصوتية |
| 2219 | [`2219-list-sum-of-evens-only.apl`](examples/2219-list-sum-of-evens-only.apl) | نجمع الزوجية فقط |
| 2220 | [`2220-list-count-of-positive-items.apl`](examples/2220-list-count-of-positive-items.apl) | نعد القيم الأكبر من صفر |
| 2221 | [`2221-list-max-minus-min-range.apl`](examples/2221-list-max-minus-min-range.apl) | أكبر ناقص أصغر |
| 2222 | [`2222-list-second-largest-distinct.apl`](examples/2222-list-second-largest-distinct.apl) | نرتب ونتجاهل المكرر |
| 2223 | [`2223-list-index-of-maximum-first.apl`](examples/2223-list-index-of-maximum-first.apl) | أول موضع للقيمة الكبرى |
| 2224 | [`2224-list-prefix-sums-running-total.apl`](examples/2224-list-prefix-sums-running-total.apl) | مجموع حتى كل موضع |
| 2225 | [`2225-list-differences-adjacent-pairs.apl`](examples/2225-list-differences-adjacent-pairs.apl) | ق[ي+1]-ق[ي] |
| 2226 | [`2226-list-is-sorted-ascending-check.apl`](examples/2226-list-is-sorted-ascending-check.apl) | نقارن كل زوج |
| 2227 | [`2227-list-remove-duplicates-keep-order.apl`](examples/2227-list-remove-duplicates-keep-order.apl) | نبقي أول ظهور |
| 2228 | [`2228-list-rotate-left-by-one.apl`](examples/2228-list-rotate-left-by-one.apl) | أول عنصر للنهاية |
| 2229 | [`2229-list-rotate-right-by-one.apl`](examples/2229-list-rotate-right-by-one.apl) | آخر عنصر للبداية |
| 2230 | [`2230-list-every-second-element-slice.apl`](examples/2230-list-every-second-element-slice.apl) | شريحة بخطوة 2 |
| 2231 | [`2231-list-square-each-element.apl`](examples/2231-list-square-each-element.apl) | نبني قائمة جديدة |
| 2232 | [`2232-list-keep-values-above-average.apl`](examples/2232-list-keep-values-above-average.apl) | نقارن بالمتوسط |
| 2233 | [`2233-list-count-inversions-pairs.apl`](examples/2233-list-count-inversions-pairs.apl) | أزواج ي<ك وق[ي]>ق[ك] |
| 2234 | [`2234-list-pair-sum-count-equals-ten.apl`](examples/2234-list-pair-sum-count-equals-ten.apl) | نعد الأزواج |
| 2235 | [`2235-list-most-frequent-smallest-tie.apl`](examples/2235-list-most-frequent-smallest-tie.apl) | عند التعادل الأصغر |
| 2236 | [`2236-list-alternating-sum-signs.apl`](examples/2236-list-alternating-sum-signs.apl) | +ثم- بالتناوب |
| 2237 | [`2237-list-dot-product-with-itself.apl`](examples/2237-list-dot-product-with-itself.apl) | مجموع المربعات |
| 2238 | [`2238-list-median-sorted-middle.apl`](examples/2238-list-median-sorted-middle.apl) | للمنتصف بعد الترتيب |
| 2239 | [`2239-list-product-of-all-items.apl`](examples/2239-list-product-of-all-items.apl) | نضرب الكل |
| 2240 | [`2240-list-max-subarray-kadane-sum.apl`](examples/2240-list-max-subarray-kadane-sum.apl) | خوارزمية كادان |
| 2241 | [`2241-list-longest-increasing-run-length.apl`](examples/2241-list-longest-increasing-run-length.apl) | نعد التزايد المتتالي |
| 2242 | [`2242-list-flatten-pairs-sum-first-second.apl`](examples/2242-list-flatten-pairs-sum-first-second.apl) | ق[ي]+ق[ي+1] |
| 2243 | [`2243-list-merge-two-halves-interleave.apl`](examples/2243-list-merge-two-halves-interleave.apl) | النصف الأول مع الثاني |
| 2244 | [`2244-list-binary-search-position-of-seven.apl`](examples/2244-list-binary-search-position-of-seven.apl) | في قائمة مرتبة |
| 2245 | [`2245-list-count-zero-crossings-sign-change.apl`](examples/2245-list-count-zero-crossings-sign-change.apl) | نعد عبور الصفر |
| 2246 | [`2246-list-min-gap-between-sorted-values.apl`](examples/2246-list-min-gap-between-sorted-values.apl) | نرتب ونقارن المتجاورات |
| 2247 | [`2247-list-equilibrium-index-left-right.apl`](examples/2247-list-equilibrium-index-left-right.apl) | مجموع اليسار يساوي اليمين |
| 2248 | [`2248-list-majority-element-over-half.apl`](examples/2248-list-majority-element-over-half.apl) | يظهر أكثر من النصف |
| 2249 | [`2249-list-two-sum-indices-target-nine.apl`](examples/2249-list-two-sum-indices-target-nine.apl) | أول زوج مجموعه 9 |
| 2250 | [`2250-list-count-subarrays-sum-equals-six.apl`](examples/2250-list-count-subarrays-sum-equals-six.apl) | نجرب كل مقطع |
| 2251 | [`2251-list-move-zeros-to-end.apl`](examples/2251-list-move-zeros-to-end.apl) | نحافظ على ترتيب الباقي |
| 2252 | [`2252-list-partition-evens-before-odds.apl`](examples/2252-list-partition-evens-before-odds.apl) | نفصل ونجمع |
| 2253 | [`2253-list-intersection-with-fixed-set.apl`](examples/2253-list-intersection-with-fixed-set.apl) | القيم الموجودة في 2 و4 و6 |
| 2254 | [`2254-list-histogram-counts-of-small-values.apl`](examples/2254-list-histogram-counts-of-small-values.apl) | نعد كل قيمة من 0 إلى 4 |
| 2255 | [`2255-list-sum-of-digits-of-all-items.apl`](examples/2255-list-sum-of-digits-of-all-items.apl) | نجمع أرقام كل عدد |
| 2256 | [`2256-list-build-multiplication-row.apl`](examples/2256-list-build-multiplication-row.apl) | نضرب كل عنصر في 3 |
| 2257 | [`2257-list-count-elements-greater-than-previous.apl`](examples/2257-list-count-elements-greater-than-previous.apl) | نقارن بالسابق |
| 2258 | [`2258-list-first-missing-positive-small.apl`](examples/2258-list-first-missing-positive-small.apl) | أصغر موجب غائب |
| 2259 | [`2259-list-sum-of-corner-and-center-items.apl`](examples/2259-list-sum-of-corner-and-center-items.apl) | ق[0]+ق[-1]+ق[ن//2] |
| 2260 | [`2260-list-reverse-in-place-swap-ends.apl`](examples/2260-list-reverse-in-place-swap-ends.apl) | نبدل الأطراف |
| 2261 | [`2261-list-bubble-sort-pass-count-swaps.apl`](examples/2261-list-bubble-sort-pass-count-swaps.apl) | نعد التبديلات |
| 2262 | [`2262-list-selection-sort-result-copy.apl`](examples/2262-list-selection-sort-result-copy.apl) | نختار الأصغر |
| 2263 | [`2263-list-insertion-sort-result-copy.apl`](examples/2263-list-insertion-sort-result-copy.apl) | ندرج كل عنصر |
| 2264 | [`2264-count-primes-below-limit-sieve-list.apl`](examples/2264-count-primes-below-limit-sieve-list.apl) | غربال إراتوستينس |
| 2265 | [`2265-sum-primes-up-to-sieve.apl`](examples/2265-sum-primes-up-to-sieve.apl) | نجمع الأولية حتى ن |
| 2266 | [`2266-nth-prime-by-counting-loop.apl`](examples/2266-nth-prime-by-counting-loop.apl) | نعد حتى الوصول |
| 2267 | [`2267-twin-prime-pairs-count-below.apl`](examples/2267-twin-prime-pairs-count-below.apl) | أولي وأولي+2 |
| 2268 | [`2268-goldbach-first-pair-smaller-prime.apl`](examples/2268-goldbach-first-pair-smaller-prime.apl) | أصغر أولي ن-ب أولي |
| 2269 | [`2269-sum-of-two-squares-representation-count.apl`](examples/2269-sum-of-two-squares-representation-count.apl) | أزواج أ<=ب |
| 2270 | [`2270-integer-square-root-binary-search.apl`](examples/2270-integer-square-root-binary-search.apl) | بحث ثنائي |
| 2271 | [`2271-is-perfect-square-via-root-loop.apl`](examples/2271-is-perfect-square-via-root-loop.apl) | نجرب الجذر |
| 2272 | [`2272-sum-of-integers-divisible-by-three-or-five.apl`](examples/2272-sum-of-integers-divisible-by-three-or-five.apl) | تحت الحد ن |
| 2273 | [`2273-fizzbuzz-count-of-both-multiples.apl`](examples/2273-fizzbuzz-count-of-both-multiples.apl) | نعد حتى ن |
| 2274 | [`2274-number-of-ways-climb-stairs-steps-one-two.apl`](examples/2274-number-of-ways-climb-stairs-steps-one-two.apl) | خطوة أو خطوتان |
| 2275 | [`2275-coin-change-ways-one-five-ten.apl`](examples/2275-coin-change-ways-one-five-ten.apl) | برمجة ديناميكية |
| 2276 | [`2276-min-coins-greedy-twentyfive-ten-five-one.apl`](examples/2276-min-coins-greedy-twentyfive-ten-five-one.apl) | عملات أمريكية |
| 2277 | [`2277-number-to-roman-numerals-small.apl`](examples/2277-number-to-roman-numerals-small.apl) | حتى 3999 |
| 2278 | [`2278-number-to-binary-string-manual.apl`](examples/2278-number-to-binary-string-manual.apl) | قسمة متكررة |
| 2279 | [`2279-number-to-hex-string-manual.apl`](examples/2279-number-to-hex-string-manual.apl) | قسمة على 16 |
| 2280 | [`2280-number-to-base-three-string.apl`](examples/2280-number-to-base-three-string.apl) | قسمة على 3 |
| 2281 | [`2281-days-to-weeks-and-days-text.apl`](examples/2281-days-to-weeks-and-days-text.apl) | نقسم على 7 |
| 2282 | [`2282-seconds-to-clock-text-hh-mm-ss.apl`](examples/2282-seconds-to-clock-text-hh-mm-ss.apl) | نملأ بالأصفار |
| 2283 | [`2283-leap-year-gregorian-rule-check.apl`](examples/2283-leap-year-gregorian-rule-check.apl) | قاعدة 4 و100 و400 |
| 2284 | [`2284-celsius-to-fahrenheit-integer.apl`](examples/2284-celsius-to-fahrenheit-integer.apl) | ف=س*9/5+32 |
| 2285 | [`2285-matrix-trace-main-diagonal-sum.apl`](examples/2285-matrix-trace-main-diagonal-sum.apl) | مجموع القطر |
| 2286 | [`2286-matrix-anti-diagonal-sum.apl`](examples/2286-matrix-anti-diagonal-sum.apl) | م[ي][ن-1-ي] |
| 2287 | [`2287-matrix-transpose-square-build.apl`](examples/2287-matrix-transpose-square-build.apl) | نبدل الصفوف والأعمدة |
| 2288 | [`2288-matrix-sum-of-all-cells.apl`](examples/2288-matrix-sum-of-all-cells.apl) | نمر على الصفوف |
| 2289 | [`2289-matrix-row-sums-list.apl`](examples/2289-matrix-row-sums-list.apl) | مجموع كل صف |
| 2290 | [`2290-matrix-column-sums-list.apl`](examples/2290-matrix-column-sums-list.apl) | مجموع كل عمود |
| 2291 | [`2291-matrix-max-cell-value.apl`](examples/2291-matrix-max-cell-value.apl) | أكبر قيمة |
| 2292 | [`2292-matrix-is-symmetric-check.apl`](examples/2292-matrix-is-symmetric-check.apl) | م = منقولها |
| 2293 | [`2293-matrix-is-identity-check.apl`](examples/2293-matrix-is-identity-check.apl) | قطر 1 وغيره 0 |
| 2294 | [`2294-matrix-scale-rows-doubled.apl`](examples/2294-matrix-scale-rows-doubled.apl) | نبني الصفوف |
| 2295 | [`2295-matrix-flip-rows-vertical.apl`](examples/2295-matrix-flip-rows-vertical.apl) | ترتيب الصفوف عكسا |
| 2296 | [`2296-matrix-flip-each-row-horizontal.apl`](examples/2296-matrix-flip-each-row-horizontal.apl) | نعكس كل صف |
| 2297 | [`2297-matrix-rotate-clockwise-square.apl`](examples/2297-matrix-rotate-clockwise-square.apl) | منقول ثم عكس الصفوف |
| 2298 | [`2298-matrix-spiral-order-walk.apl`](examples/2298-matrix-spiral-order-walk.apl) | نقشر الطبقات |
| 2299 | [`2299-matrix-determinant-two-by-two-or-three.apl`](examples/2299-matrix-determinant-two-by-two-or-three.apl) | نفك على الصف الأول |
| 2300 | [`2300-matrix-count-zero-cells.apl`](examples/2300-matrix-count-zero-cells.apl) | نعد الأصفار |
| 2301 | [`2301-matrix-border-sum-cells.apl`](examples/2301-matrix-border-sum-cells.apl) | الصف الأول والأخير والأعمدة |
| 2302 | [`2302-matrix-multiply-by-itself-trace.apl`](examples/2302-matrix-multiply-by-itself-trace.apl) | نضرب ونجمع القطر |
| 2303 | [`2303-matrix-row-with-largest-sum-index.apl`](examples/2303-matrix-row-with-largest-sum-index.apl) | نقارن المجاميع |
| 2304 | [`2304-matrix-count-negative-cells.apl`](examples/2304-matrix-count-negative-cells.apl) | نعد السالب |
| 2305 | [`2305-palindrome-ignoring-spaces-lowercase.apl`](examples/2305-palindrome-ignoring-spaces-lowercase.apl) | نحذف المسافات |
| 2306 | [`2306-count-substring-ab-overlapping.apl`](examples/2306-count-substring-ab-overlapping.apl) | نمر على المواضع |
| 2307 | [`2307-string-compress-length-after-rle.apl`](examples/2307-string-compress-length-after-rle.apl) | نحسب طول الترميز |
| 2308 | [`2308-anagram-key-sorted-letters.apl`](examples/2308-anagram-key-sorted-letters.apl) | الحروف مرتبة |
| 2309 | [`2309-replace-spaces-with-dashes-lower.apl`](examples/2309-replace-spaces-with-dashes-lower.apl) | slug بسيط |
| 2310 | [`2310-count-each-letter-a-b-c.apl`](examples/2310-count-each-letter-a-b-c.apl) | نعد ثلاثة حروف |
| 2311 | [`2311-last-word-length-of-text.apl`](examples/2311-last-word-length-of-text.apl) | نقسم ونأخذ الأخيرة |
| 2312 | [`2312-longest-word-length-in-text.apl`](examples/2312-longest-word-length-in-text.apl) | نقارن الأطوال |
| 2313 | [`2313-reverse-each-word-in-place.apl`](examples/2313-reverse-each-word-in-place.apl) | نبقي ترتيب الكلمات |
| 2314 | [`2314-reverse-word-order-in-text.apl`](examples/2314-reverse-word-order-in-text.apl) | نعكس القائمة |
| 2315 | [`2315-is-string-all-digits-check.apl`](examples/2315-is-string-all-digits-check.apl) | نتحقق من كل رمز |
| 2316 | [`2316-digits-to-sum-from-text-mixed.apl`](examples/2316-digits-to-sum-from-text-mixed.apl) | نتجاهل الحروف |
| 2317 | [`2317-balanced-brackets-round-only.apl`](examples/2317-balanced-brackets-round-only.apl) | نعد العمق |
| 2318 | [`2318-max-nesting-depth-parentheses.apl`](examples/2318-max-nesting-depth-parentheses.apl) | أعلى عداد |
| 2319 | [`2319-first-once-only-letter-position.apl`](examples/2319-first-once-only-letter-position.apl) | يظهر مرة واحدة |
| 2320 | [`2320-common-prefix-length-with-hello.apl`](examples/2320-common-prefix-length-with-hello.apl) | نقارن حرفا بحرف |
| 2321 | [`2321-count-words-longer-than-three.apl`](examples/2321-count-words-longer-than-three.apl) | نفحص الطول |
| 2322 | [`2322-remove-vowels-from-latin-text.apl`](examples/2322-remove-vowels-from-latin-text.apl) | نبقي الصامتة |
| 2323 | [`2323-char-frequency-max-count.apl`](examples/2323-char-frequency-max-count.apl) | أعلى عدد |
| 2324 | [`2324-binary-string-to-decimal-manual.apl`](examples/2324-binary-string-to-decimal-manual.apl) | نضاعف ونضيف |
| 2325 | [`2325-hex-string-to-decimal-manual.apl`](examples/2325-hex-string-to-decimal-manual.apl) | نستخدم الموضع في الأرقام |
| 2326 | [`2326-roman-numeral-to-integer-simple.apl`](examples/2326-roman-numeral-to-integer-simple.apl) | نطرح عند الأصغر قبل الأكبر |
| 2327 | [`2327-vowel-start-word-count.apl`](examples/2327-vowel-start-word-count.apl) | أول حرف |
| 2328 | [`2328-string-sorted-letters-descending.apl`](examples/2328-string-sorted-letters-descending.apl) | فرز عكسي |
| 2329 | [`2329-is-sorted-string-letters.apl`](examples/2329-is-sorted-string-letters.apl) | نقارن المتجاورات |
| 2330 | [`2330-hamming-distance-to-abcde.apl`](examples/2330-hamming-distance-to-abcde.apl) | نعد الاختلافات |
| 2331 | [`2331-word-lengths-list-of-text.apl`](examples/2331-word-lengths-list-of-text.apl) | قائمة بأطوال الكلمات |
| 2332 | [`2332-first-letters-joined-string.apl`](examples/2332-first-letters-joined-string.apl) | أول حرف لكل كلمة |
| 2333 | [`2333-pad-number-string-with-zeros-five.apl`](examples/2333-pad-number-string-with-zeros-five.apl) | zfill |
| 2334 | [`2334-count-spaces-in-text.apl`](examples/2334-count-spaces-in-text.apl) | نعد " " |
| 2335 | [`2335-list-sum-of-squares-of-odd-items.apl`](examples/2335-list-sum-of-squares-of-odd-items.apl) | نربع الفردي فقط |
| 2336 | [`2336-list-count-items-equal-to-first.apl`](examples/2336-list-count-items-equal-to-first.apl) | نقارن بالعنصر الأول |
| 2337 | [`2337-list-last-minus-first-difference.apl`](examples/2337-list-last-minus-first-difference.apl) | فرق الطرفين |
| 2338 | [`2338-list-take-first-three-items.apl`](examples/2338-list-take-first-three-items.apl) | شريحة |
| 2339 | [`2339-list-drop-first-two-items.apl`](examples/2339-list-drop-first-two-items.apl) | شريحة من 2 |
| 2340 | [`2340-list-take-last-two-items.apl`](examples/2340-list-take-last-two-items.apl) | شريحة سالبة |
| 2341 | [`2341-list-chunk-sum-of-pairs-nonoverlap.apl`](examples/2341-list-chunk-sum-of-pairs-nonoverlap.apl) | نقفز بخطوتين |
| 2342 | [`2342-list-replace-negatives-with-zero.apl`](examples/2342-list-replace-negatives-with-zero.apl) | نبني قائمة |
| 2343 | [`2343-list-absolute-values-each.apl`](examples/2343-list-absolute-values-each.apl) | abs لكل عنصر |
| 2344 | [`2344-list-cumulative-max-running.apl`](examples/2344-list-cumulative-max-running.apl) | أكبر قيمة حتى الآن |
| 2345 | [`2345-list-cumulative-min-running.apl`](examples/2345-list-cumulative-min-running.apl) | أصغر قيمة حتى الآن |
| 2346 | [`2346-list-range-of-indices-where-even.apl`](examples/2346-list-range-of-indices-where-even.apl) | فهارس الزوجي |
| 2347 | [`2347-list-count-local-peaks-strict.apl`](examples/2347-list-count-local-peaks-strict.apl) | أكبر من الجارين |
| 2348 | [`2348-list-count-local-valleys-strict.apl`](examples/2348-list-count-local-valleys-strict.apl) | أصغر من الجارين |
| 2349 | [`2349-list-sum-between-min-and-max-positions.apl`](examples/2349-list-sum-between-min-and-max-positions.apl) | المواضع الأولى |
| 2350 | [`2350-list-score-grades-count-passing.apl`](examples/2350-list-score-grades-count-passing.apl) | 50 فأكثر |
| 2351 | [`2351-list-average-rounded-two-places.apl`](examples/2351-list-average-rounded-two-places.apl) | round(...,2) |
| 2352 | [`2352-list-weighted-sum-by-position.apl`](examples/2352-list-weighted-sum-by-position.apl) | ق[ي]*(ي+1) |
| 2353 | [`2353-list-is-arithmetic-progression.apl`](examples/2353-list-is-arithmetic-progression.apl) | فرق ثابت |
| 2354 | [`2354-list-is-geometric-progression-int.apl`](examples/2354-list-is-geometric-progression-int.apl) | نسبة ثابتة |
| 2355 | [`2355-list-count-palindromic-numbers.apl`](examples/2355-list-count-palindromic-numbers.apl) | نقارن النص بمعكوسه |
| 2356 | [`2356-list-gcd-of-all-items.apl`](examples/2356-list-gcd-of-all-items.apl) | نطبق إقليدس تباعا |
| 2357 | [`2357-list-lcm-of-all-items.apl`](examples/2357-list-lcm-of-all-items.apl) | نطبق على الأزواج |
| 2358 | [`2358-list-bits-or-of-all-items.apl`](examples/2358-list-bits-or-of-all-items.apl) | نجمع بـ | |
| 2359 | [`2359-list-bits-and-of-all-items.apl`](examples/2359-list-bits-and-of-all-items.apl) | نطبق & |
| 2360 | [`2360-list-single-number-xor-unique.apl`](examples/2360-list-single-number-xor-unique.apl) | المكرر يلغي نفسه |
| 2361 | [`2361-sum-of-first-n-fibonacci-numbers.apl`](examples/2361-sum-of-first-n-fibonacci-numbers.apl) | نجمع الحدود |
| 2362 | [`2362-count-fibonacci-numbers-below-limit.apl`](examples/2362-count-fibonacci-numbers-below-limit.apl) | نولد حتى الحد |
| 2363 | [`2363-number-of-digits-by-division-loop.apl`](examples/2363-number-of-digits-by-division-loop.apl) | نقسم على 10 |
| 2364 | [`2364-sum-of-digits-recursive-style-loop.apl`](examples/2364-sum-of-digits-recursive-style-loop.apl) | ن % 10 |
| 2365 | [`2365-alternating-digit-sum-from-right.apl`](examples/2365-alternating-digit-sum-from-right.apl) | نبدأ من اليمين بإشارة + |
| 2366 | [`2366-divisible-by-eleven-via-alternating-sum.apl`](examples/2366-divisible-by-eleven-via-alternating-sum.apl) | المجموع المتناوب يقبل 11 |
| 2367 | [`2367-sum-of-multiples-of-n-up-to-hundred.apl`](examples/2367-sum-of-multiples-of-n-up-to-hundred.apl) | نقفز بخطوة ن |
| 2368 | [`2368-count-lattice-points-in-circle-radius.apl`](examples/2368-count-lattice-points-in-circle-radius.apl) | س²+ص² ≤ نق² |
| 2369 | [`2369-pythagorean-triples-count-up-to.apl`](examples/2369-pythagorean-triples-count-up-to.apl) | أ<ب<ج<=ن |
| 2370 | [`2370-sum-of-squares-minus-square-of-sum.apl`](examples/2370-sum-of-squares-minus-square-of-sum.apl) | مسألة أويلر |
| 2371 | [`2371-nth-triangular-number-with-most-divisors-small.apl`](examples/2371-nth-triangular-number-with-most-divisors-small.apl) | نعد قواسم ن(ن+1)/2 |
| 2372 | [`2372-digit-factorial-sum-of-number.apl`](examples/2372-digit-factorial-sum-of-number.apl) | لكل رقم مضروبه |
| 2373 | [`2373-persistence-multiplicative-steps.apl`](examples/2373-persistence-multiplicative-steps.apl) | نضرب الأرقام حتى رقم واحد |
| 2374 | [`2374-additive-persistence-steps.apl`](examples/2374-additive-persistence-steps.apl) | نجمع الأرقام حتى رقم واحد |
| 2375 | [`2375-reverse-and-add-palindrome-steps.apl`](examples/2375-reverse-and-add-palindrome-steps.apl) | خطوات الوصول لعدد متناظر |
| 2376 | [`2376-ugly-number-check-two-three-five.apl`](examples/2376-ugly-number-check-two-three-five.apl) | عوامله 2 و3 و5 فقط |
| 2377 | [`2377-count-bits-to-flip-between-n-and-forty-two.apl`](examples/2377-count-bits-to-flip-between-n-and-forty-two.apl) | XOR مع 42 ثم عد الآحاد |
| 2378 | [`2378-reverse-bits-of-byte-value.apl`](examples/2378-reverse-bits-of-byte-value.apl) | 8 بتات |
| 2379 | [`2379-isolate-lowest-set-bit-value.apl`](examples/2379-isolate-lowest-set-bit-value.apl) | ن & (-ن) |
| 2380 | [`2380-clear-lowest-set-bit-value.apl`](examples/2380-clear-lowest-set-bit-value.apl) | ن & (ن-1) |
| 2381 | [`2381-swap-adjacent-bit-pairs-byte.apl`](examples/2381-swap-adjacent-bit-pairs-byte.apl) | أقنعة 0xAA و0x55 |
| 2382 | [`2382-triangular-root-check-is-triangular.apl`](examples/2382-triangular-root-check-is-triangular.apl) | نجمع حتى التجاوز |
| 2383 | [`2383-sum-of-first-n-primes-loop.apl`](examples/2383-sum-of-first-n-primes-loop.apl) | نعد الأولية |
| 2384 | [`2384-power-mod-fast-exponent-seven.apl`](examples/2384-power-mod-fast-exponent-seven.apl) | سبعة أس ن مقياس 13 |
| 2385 | [`2385-digits-of-pi-style-sum-reciprocal-int.apl`](examples/2385-digits-of-pi-style-sum-reciprocal-int.apl) | نضرب بألف ونجمع |
| 2386 | [`2386-class-counter-increment-reset.apl`](examples/2386-class-counter-increment-reset.apl) | عداد بسيط |
| 2387 | [`2387-class-stack-push-pop-size.apl`](examples/2387-class-stack-push-pop-size.apl) | دفع وسحب |
| 2388 | [`2388-class-queue-enqueue-dequeue-front.apl`](examples/2388-class-queue-enqueue-dequeue-front.apl) | أول داخل أول خارج |
| 2389 | [`2389-class-rectangle-area-perimeter-square-check.apl`](examples/2389-class-rectangle-area-perimeter-square-check.apl) | مساحة ومحيط |
| 2390 | [`2390-class-bank-account-deposit-withdraw-limit.apl`](examples/2390-class-bank-account-deposit-withdraw-limit.apl) | لا يسحب أكثر من الرصيد |
| 2391 | [`2391-class-temperature-converter-two-units.apl`](examples/2391-class-temperature-converter-two-units.apl) | سلسيوس وفهرنهايت |
| 2392 | [`2392-class-point-distance-squared-and-move.apl`](examples/2392-class-point-distance-squared-and-move.apl) | نقطة تتحرك |
| 2393 | [`2393-class-vector-add-dot-length-squared.apl`](examples/2393-class-vector-add-dot-length-squared.apl) | جمع وجداء |
| 2394 | [`2394-class-student-grades-average-best.apl`](examples/2394-class-student-grades-average-best.apl) | متوسط وأعلى درجة |
| 2395 | [`2395-class-inventory-add-remove-count.apl`](examples/2395-class-inventory-add-remove-count.apl) | أصناف وكميات |
| 2396 | [`2396-class-toggle-switch-state-flips.apl`](examples/2396-class-toggle-switch-state-flips.apl) | يقلب الحالة |
| 2397 | [`2397-class-accumulator-history-list.apl`](examples/2397-class-accumulator-history-list.apl) | يحفظ القيم |
| 2398 | [`2398-class-parking-lot-capacity-park-leave.apl`](examples/2398-class-parking-lot-capacity-park-leave.apl) | سعة محدودة |
| 2399 | [`2399-sum-multiples-of-2-below-limit-v2.apl`](examples/2399-sum-multiples-of-2-below-limit-v2.apl) | نجمع مضاعفات 2 الأصغر من ن |
| 2400 | [`2400-sum-multiples-of-4-below-limit-v2.apl`](examples/2400-sum-multiples-of-4-below-limit-v2.apl) | نجمع مضاعفات 4 الأصغر من ن |
| 2401 | [`2401-sum-multiples-of-5-below-limit-v2.apl`](examples/2401-sum-multiples-of-5-below-limit-v2.apl) | نجمع مضاعفات 5 الأصغر من ن |
| 2402 | [`2402-count-multiples-of-2-up-to-limit.apl`](examples/2402-count-multiples-of-2-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2403 | [`2403-count-multiples-of-4-up-to-limit.apl`](examples/2403-count-multiples-of-4-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2404 | [`2404-count-multiples-of-5-up-to-limit.apl`](examples/2404-count-multiples-of-5-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2405 | [`2405-list-multiply-each-by-2.apl`](examples/2405-list-multiply-each-by-2.apl) | نبني قائمة جديدة |
| 2406 | [`2406-list-multiply-each-by-4.apl`](examples/2406-list-multiply-each-by-4.apl) | نبني قائمة جديدة |
| 2407 | [`2407-list-multiply-each-by-5.apl`](examples/2407-list-multiply-each-by-5.apl) | نبني قائمة جديدة |
| 2408 | [`2408-list-add-2-to-each-item.apl`](examples/2408-list-add-2-to-each-item.apl) | نزيد كل عنصر |
| 2409 | [`2409-list-add-4-to-each-item.apl`](examples/2409-list-add-4-to-each-item.apl) | نزيد كل عنصر |
| 2410 | [`2410-list-add-5-to-each-item.apl`](examples/2410-list-add-5-to-each-item.apl) | نزيد كل عنصر |
| 2411 | [`2411-list-count-greater-than-2.apl`](examples/2411-list-count-greater-than-2.apl) | نعد الأكبر |
| 2412 | [`2412-list-count-greater-than-4.apl`](examples/2412-list-count-greater-than-4.apl) | نعد الأكبر |
| 2413 | [`2413-list-count-greater-than-5.apl`](examples/2413-list-count-greater-than-5.apl) | نعد الأكبر |
| 2414 | [`2414-list-keep-divisible-by-2.apl`](examples/2414-list-keep-divisible-by-2.apl) | نصفي القائمة |
| 2415 | [`2415-list-keep-divisible-by-4.apl`](examples/2415-list-keep-divisible-by-4.apl) | نصفي القائمة |
| 2416 | [`2416-list-keep-divisible-by-5.apl`](examples/2416-list-keep-divisible-by-5.apl) | نصفي القائمة |
| 2417 | [`2417-digit-sum-of-2-to-the-power-n.apl`](examples/2417-digit-sum-of-2-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2418 | [`2418-digit-sum-of-4-to-the-power-n.apl`](examples/2418-digit-sum-of-4-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2419 | [`2419-digit-sum-of-5-to-the-power-n.apl`](examples/2419-digit-sum-of-5-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2420 | [`2420-sum-of-remainders-mod-2-up-to-n.apl`](examples/2420-sum-of-remainders-mod-2-up-to-n.apl) | نجمع ي % 2 |
| 2421 | [`2421-sum-of-remainders-mod-4-up-to-n.apl`](examples/2421-sum-of-remainders-mod-4-up-to-n.apl) | نجمع ي % 4 |
| 2422 | [`2422-sum-of-remainders-mod-5-up-to-n.apl`](examples/2422-sum-of-remainders-mod-5-up-to-n.apl) | نجمع ي % 5 |
| 2423 | [`2423-number-to-base-2-string-v2.apl`](examples/2423-number-to-base-2-string-v2.apl) | قسمة متكررة |
| 2424 | [`2424-number-to-base-4-string-v2.apl`](examples/2424-number-to-base-4-string-v2.apl) | قسمة متكررة |
| 2425 | [`2425-number-to-base-5-string-v2.apl`](examples/2425-number-to-base-5-string-v2.apl) | قسمة متكررة |
| 2426 | [`2426-count-numbers-below-hundred-with-digit-sum-2.apl`](examples/2426-count-numbers-below-hundred-with-digit-sum-2.apl) | نعد الأعداد |
| 2427 | [`2427-count-numbers-below-hundred-with-digit-sum-4.apl`](examples/2427-count-numbers-below-hundred-with-digit-sum-4.apl) | نعد الأعداد |
| 2428 | [`2428-count-numbers-below-hundred-with-digit-sum-5.apl`](examples/2428-count-numbers-below-hundred-with-digit-sum-5.apl) | نعد الأعداد |
| 2429 | [`2429-list-take-every-2th-item.apl`](examples/2429-list-take-every-2th-item.apl) | شريحة بخطوة |
| 2430 | [`2430-list-take-every-3th-item.apl`](examples/2430-list-take-every-3th-item.apl) | شريحة بخطوة |
| 2431 | [`2431-list-take-every-4th-item.apl`](examples/2431-list-take-every-4th-item.apl) | شريحة بخطوة |
| 2432 | [`2432-list-rotate-left-by-1.apl`](examples/2432-list-rotate-left-by-1.apl) | نقص ونلصق |
| 2433 | [`2433-list-rotate-left-by-2.apl`](examples/2433-list-rotate-left-by-2.apl) | نقص ونلصق |
| 2434 | [`2434-list-rotate-left-by-3.apl`](examples/2434-list-rotate-left-by-3.apl) | نقص ونلصق |
| 2435 | [`2435-nth-term-arithmetic-sequence-step-2.apl`](examples/2435-nth-term-arithmetic-sequence-step-2.apl) | أ + (ن-1)*2 |
| 2436 | [`2436-nth-term-arithmetic-sequence-step-4.apl`](examples/2436-nth-term-arithmetic-sequence-step-4.apl) | أ + (ن-1)*4 |
| 2437 | [`2437-nth-term-arithmetic-sequence-step-5.apl`](examples/2437-nth-term-arithmetic-sequence-step-5.apl) | أ + (ن-1)*5 |
| 2438 | [`2438-sum-of-powers-of-2-up-to-n.apl`](examples/2438-sum-of-powers-of-2-up-to-n.apl) | نجمع 2^ي |
| 2439 | [`2439-sum-of-powers-of-4-up-to-n.apl`](examples/2439-sum-of-powers-of-4-up-to-n.apl) | نجمع 4^ي |
| 2440 | [`2440-sum-of-powers-of-5-up-to-n.apl`](examples/2440-sum-of-powers-of-5-up-to-n.apl) | نجمع 5^ي |
| 2441 | [`2441-clamp-list-values-to-max-2.apl`](examples/2441-clamp-list-values-to-max-2.apl) | نقص ما يزيد |
| 2442 | [`2442-clamp-list-values-to-max-4.apl`](examples/2442-clamp-list-values-to-max-4.apl) | نقص ما يزيد |
| 2443 | [`2443-clamp-list-values-to-max-5.apl`](examples/2443-clamp-list-values-to-max-5.apl) | نقص ما يزيد |
| 2444 | [`2444-caesar-shift-by-1-lowercase.apl`](examples/2444-caesar-shift-by-1-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2445 | [`2445-caesar-shift-by-5-lowercase.apl`](examples/2445-caesar-shift-by-5-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2446 | [`2446-caesar-shift-by-13-lowercase.apl`](examples/2446-caesar-shift-by-13-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2447 | [`2447-repeat-text-2-times-with-dash.apl`](examples/2447-repeat-text-2-times-with-dash.apl) | نكرر ونفصل |
| 2448 | [`2448-repeat-text-4-times-with-dash.apl`](examples/2448-repeat-text-4-times-with-dash.apl) | نكرر ونفصل |
| 2449 | [`2449-repeat-text-5-times-with-dash.apl`](examples/2449-repeat-text-5-times-with-dash.apl) | نكرر ونفصل |
| 2450 | [`2450-pad-number-with-zeros-to-width-3.apl`](examples/2450-pad-number-with-zeros-to-width-3.apl) | zfill |
| 2451 | [`2451-pad-number-with-zeros-to-width-8.apl`](examples/2451-pad-number-with-zeros-to-width-8.apl) | zfill |
| 2452 | [`2452-pad-number-with-zeros-to-width-10.apl`](examples/2452-pad-number-with-zeros-to-width-10.apl) | zfill |
| 2453 | [`2453-truncate-text-to-first-3-chars.apl`](examples/2453-truncate-text-to-first-3-chars.apl) | شريحة |
| 2454 | [`2454-truncate-text-to-first-5-chars.apl`](examples/2454-truncate-text-to-first-5-chars.apl) | شريحة |
| 2455 | [`2455-truncate-text-to-first-8-chars.apl`](examples/2455-truncate-text-to-first-8-chars.apl) | شريحة |
| 2456 | [`2456-count-triples-sum-to-6-small.apl`](examples/2456-count-triples-sum-to-6-small.apl) | أ<=ب<=ج موجبة |
| 2457 | [`2457-count-triples-sum-to-9-small.apl`](examples/2457-count-triples-sum-to-9-small.apl) | أ<=ب<=ج موجبة |
| 2458 | [`2458-count-triples-sum-to-12-small.apl`](examples/2458-count-triples-sum-to-12-small.apl) | أ<=ب<=ج موجبة |
| 2459 | [`2459-sum-multiples-of-3-below-limit-v2.apl`](examples/2459-sum-multiples-of-3-below-limit-v2.apl) | نجمع مضاعفات 3 الأصغر من ن |
| 2460 | [`2460-sum-multiples-of-6-below-limit-v2.apl`](examples/2460-sum-multiples-of-6-below-limit-v2.apl) | نجمع مضاعفات 6 الأصغر من ن |
| 2461 | [`2461-sum-multiples-of-7-below-limit-v2.apl`](examples/2461-sum-multiples-of-7-below-limit-v2.apl) | نجمع مضاعفات 7 الأصغر من ن |
| 2462 | [`2462-sum-multiples-of-8-below-limit-v2.apl`](examples/2462-sum-multiples-of-8-below-limit-v2.apl) | نجمع مضاعفات 8 الأصغر من ن |
| 2463 | [`2463-sum-multiples-of-9-below-limit-v2.apl`](examples/2463-sum-multiples-of-9-below-limit-v2.apl) | نجمع مضاعفات 9 الأصغر من ن |
| 2464 | [`2464-count-multiples-of-3-up-to-limit.apl`](examples/2464-count-multiples-of-3-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2465 | [`2465-count-multiples-of-6-up-to-limit.apl`](examples/2465-count-multiples-of-6-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2466 | [`2466-count-multiples-of-7-up-to-limit.apl`](examples/2466-count-multiples-of-7-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2467 | [`2467-count-multiples-of-8-up-to-limit.apl`](examples/2467-count-multiples-of-8-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2468 | [`2468-count-multiples-of-9-up-to-limit.apl`](examples/2468-count-multiples-of-9-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2469 | [`2469-list-multiply-each-by-3.apl`](examples/2469-list-multiply-each-by-3.apl) | نبني قائمة جديدة |
| 2470 | [`2470-list-multiply-each-by-6.apl`](examples/2470-list-multiply-each-by-6.apl) | نبني قائمة جديدة |
| 2471 | [`2471-list-multiply-each-by-7.apl`](examples/2471-list-multiply-each-by-7.apl) | نبني قائمة جديدة |
| 2472 | [`2472-list-multiply-each-by-8.apl`](examples/2472-list-multiply-each-by-8.apl) | نبني قائمة جديدة |
| 2473 | [`2473-list-multiply-each-by-9.apl`](examples/2473-list-multiply-each-by-9.apl) | نبني قائمة جديدة |
| 2474 | [`2474-list-add-3-to-each-item.apl`](examples/2474-list-add-3-to-each-item.apl) | نزيد كل عنصر |
| 2475 | [`2475-list-add-6-to-each-item.apl`](examples/2475-list-add-6-to-each-item.apl) | نزيد كل عنصر |
| 2476 | [`2476-list-add-7-to-each-item.apl`](examples/2476-list-add-7-to-each-item.apl) | نزيد كل عنصر |
| 2477 | [`2477-list-add-8-to-each-item.apl`](examples/2477-list-add-8-to-each-item.apl) | نزيد كل عنصر |
| 2478 | [`2478-list-add-9-to-each-item.apl`](examples/2478-list-add-9-to-each-item.apl) | نزيد كل عنصر |
| 2479 | [`2479-list-count-greater-than-3.apl`](examples/2479-list-count-greater-than-3.apl) | نعد الأكبر |
| 2480 | [`2480-list-count-greater-than-6.apl`](examples/2480-list-count-greater-than-6.apl) | نعد الأكبر |
| 2481 | [`2481-list-count-greater-than-7.apl`](examples/2481-list-count-greater-than-7.apl) | نعد الأكبر |
| 2482 | [`2482-list-count-greater-than-8.apl`](examples/2482-list-count-greater-than-8.apl) | نعد الأكبر |
| 2483 | [`2483-list-count-greater-than-9.apl`](examples/2483-list-count-greater-than-9.apl) | نعد الأكبر |
| 2484 | [`2484-list-keep-divisible-by-3.apl`](examples/2484-list-keep-divisible-by-3.apl) | نصفي القائمة |
| 2485 | [`2485-list-keep-divisible-by-6.apl`](examples/2485-list-keep-divisible-by-6.apl) | نصفي القائمة |
| 2486 | [`2486-list-keep-divisible-by-7.apl`](examples/2486-list-keep-divisible-by-7.apl) | نصفي القائمة |
| 2487 | [`2487-list-keep-divisible-by-8.apl`](examples/2487-list-keep-divisible-by-8.apl) | نصفي القائمة |
| 2488 | [`2488-list-keep-divisible-by-9.apl`](examples/2488-list-keep-divisible-by-9.apl) | نصفي القائمة |
| 2489 | [`2489-digit-sum-of-3-to-the-power-n.apl`](examples/2489-digit-sum-of-3-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2490 | [`2490-digit-sum-of-6-to-the-power-n.apl`](examples/2490-digit-sum-of-6-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2491 | [`2491-digit-sum-of-7-to-the-power-n.apl`](examples/2491-digit-sum-of-7-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2492 | [`2492-digit-sum-of-8-to-the-power-n.apl`](examples/2492-digit-sum-of-8-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2493 | [`2493-digit-sum-of-9-to-the-power-n.apl`](examples/2493-digit-sum-of-9-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2494 | [`2494-sum-of-remainders-mod-3-up-to-n.apl`](examples/2494-sum-of-remainders-mod-3-up-to-n.apl) | نجمع ي % 3 |
| 2495 | [`2495-sum-of-remainders-mod-6-up-to-n.apl`](examples/2495-sum-of-remainders-mod-6-up-to-n.apl) | نجمع ي % 6 |
| 2496 | [`2496-sum-of-remainders-mod-7-up-to-n.apl`](examples/2496-sum-of-remainders-mod-7-up-to-n.apl) | نجمع ي % 7 |
| 2497 | [`2497-sum-of-remainders-mod-8-up-to-n.apl`](examples/2497-sum-of-remainders-mod-8-up-to-n.apl) | نجمع ي % 8 |
| 2498 | [`2498-sum-of-remainders-mod-9-up-to-n.apl`](examples/2498-sum-of-remainders-mod-9-up-to-n.apl) | نجمع ي % 9 |
| 2499 | [`2499-number-to-base-3-string-v2.apl`](examples/2499-number-to-base-3-string-v2.apl) | قسمة متكررة |
| 2500 | [`2500-number-to-base-6-string-v2.apl`](examples/2500-number-to-base-6-string-v2.apl) | قسمة متكررة |
| 2501 | [`2501-number-to-base-7-string-v2.apl`](examples/2501-number-to-base-7-string-v2.apl) | قسمة متكررة |
| 2502 | [`2502-number-to-base-8-string-v2.apl`](examples/2502-number-to-base-8-string-v2.apl) | قسمة متكررة |
| 2503 | [`2503-number-to-base-9-string-v2.apl`](examples/2503-number-to-base-9-string-v2.apl) | قسمة متكررة |
| 2504 | [`2504-count-numbers-below-hundred-with-digit-sum-3.apl`](examples/2504-count-numbers-below-hundred-with-digit-sum-3.apl) | نعد الأعداد |
| 2505 | [`2505-count-numbers-below-hundred-with-digit-sum-6.apl`](examples/2505-count-numbers-below-hundred-with-digit-sum-6.apl) | نعد الأعداد |
| 2506 | [`2506-count-numbers-below-hundred-with-digit-sum-7.apl`](examples/2506-count-numbers-below-hundred-with-digit-sum-7.apl) | نعد الأعداد |
| 2507 | [`2507-count-numbers-below-hundred-with-digit-sum-8.apl`](examples/2507-count-numbers-below-hundred-with-digit-sum-8.apl) | نعد الأعداد |
| 2508 | [`2508-count-numbers-below-hundred-with-digit-sum-9.apl`](examples/2508-count-numbers-below-hundred-with-digit-sum-9.apl) | نعد الأعداد |
| 2509 | [`2509-list-take-every-5th-item.apl`](examples/2509-list-take-every-5th-item.apl) | شريحة بخطوة |
| 2510 | [`2510-list-take-every-6th-item.apl`](examples/2510-list-take-every-6th-item.apl) | شريحة بخطوة |
| 2511 | [`2511-list-take-every-7th-item.apl`](examples/2511-list-take-every-7th-item.apl) | شريحة بخطوة |
| 2512 | [`2512-list-take-every-8th-item.apl`](examples/2512-list-take-every-8th-item.apl) | شريحة بخطوة |
| 2513 | [`2513-list-take-every-9th-item.apl`](examples/2513-list-take-every-9th-item.apl) | شريحة بخطوة |
| 2514 | [`2514-list-rotate-left-by-4.apl`](examples/2514-list-rotate-left-by-4.apl) | نقص ونلصق |
| 2515 | [`2515-list-rotate-left-by-5.apl`](examples/2515-list-rotate-left-by-5.apl) | نقص ونلصق |
| 2516 | [`2516-list-rotate-left-by-6.apl`](examples/2516-list-rotate-left-by-6.apl) | نقص ونلصق |
| 2517 | [`2517-list-rotate-left-by-7.apl`](examples/2517-list-rotate-left-by-7.apl) | نقص ونلصق |
| 2518 | [`2518-list-rotate-left-by-8.apl`](examples/2518-list-rotate-left-by-8.apl) | نقص ونلصق |
| 2519 | [`2519-nth-term-arithmetic-sequence-step-3.apl`](examples/2519-nth-term-arithmetic-sequence-step-3.apl) | أ + (ن-1)*3 |
| 2520 | [`2520-nth-term-arithmetic-sequence-step-6.apl`](examples/2520-nth-term-arithmetic-sequence-step-6.apl) | أ + (ن-1)*6 |
| 2521 | [`2521-nth-term-arithmetic-sequence-step-7.apl`](examples/2521-nth-term-arithmetic-sequence-step-7.apl) | أ + (ن-1)*7 |
| 2522 | [`2522-nth-term-arithmetic-sequence-step-8.apl`](examples/2522-nth-term-arithmetic-sequence-step-8.apl) | أ + (ن-1)*8 |
| 2523 | [`2523-nth-term-arithmetic-sequence-step-9.apl`](examples/2523-nth-term-arithmetic-sequence-step-9.apl) | أ + (ن-1)*9 |
| 2524 | [`2524-sum-of-powers-of-3-up-to-n.apl`](examples/2524-sum-of-powers-of-3-up-to-n.apl) | نجمع 3^ي |
| 2525 | [`2525-sum-of-powers-of-6-up-to-n.apl`](examples/2525-sum-of-powers-of-6-up-to-n.apl) | نجمع 6^ي |
| 2526 | [`2526-sum-of-powers-of-7-up-to-n.apl`](examples/2526-sum-of-powers-of-7-up-to-n.apl) | نجمع 7^ي |
| 2527 | [`2527-sum-of-powers-of-8-up-to-n.apl`](examples/2527-sum-of-powers-of-8-up-to-n.apl) | نجمع 8^ي |
| 2528 | [`2528-sum-of-powers-of-9-up-to-n.apl`](examples/2528-sum-of-powers-of-9-up-to-n.apl) | نجمع 9^ي |
| 2529 | [`2529-clamp-list-values-to-max-3.apl`](examples/2529-clamp-list-values-to-max-3.apl) | نقص ما يزيد |
| 2530 | [`2530-clamp-list-values-to-max-6.apl`](examples/2530-clamp-list-values-to-max-6.apl) | نقص ما يزيد |
| 2531 | [`2531-clamp-list-values-to-max-7.apl`](examples/2531-clamp-list-values-to-max-7.apl) | نقص ما يزيد |
| 2532 | [`2532-clamp-list-values-to-max-8.apl`](examples/2532-clamp-list-values-to-max-8.apl) | نقص ما يزيد |
| 2533 | [`2533-clamp-list-values-to-max-9.apl`](examples/2533-clamp-list-values-to-max-9.apl) | نقص ما يزيد |
| 2534 | [`2534-caesar-shift-by-2-lowercase.apl`](examples/2534-caesar-shift-by-2-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2535 | [`2535-caesar-shift-by-3-lowercase.apl`](examples/2535-caesar-shift-by-3-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2536 | [`2536-caesar-shift-by-4-lowercase.apl`](examples/2536-caesar-shift-by-4-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2537 | [`2537-caesar-shift-by-6-lowercase.apl`](examples/2537-caesar-shift-by-6-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2538 | [`2538-caesar-shift-by-7-lowercase.apl`](examples/2538-caesar-shift-by-7-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2539 | [`2539-repeat-text-3-times-with-dash.apl`](examples/2539-repeat-text-3-times-with-dash.apl) | نكرر ونفصل |
| 2540 | [`2540-repeat-text-6-times-with-dash.apl`](examples/2540-repeat-text-6-times-with-dash.apl) | نكرر ونفصل |
| 2541 | [`2541-repeat-text-7-times-with-dash.apl`](examples/2541-repeat-text-7-times-with-dash.apl) | نكرر ونفصل |
| 2542 | [`2542-repeat-text-8-times-with-dash.apl`](examples/2542-repeat-text-8-times-with-dash.apl) | نكرر ونفصل |
| 2543 | [`2543-repeat-text-9-times-with-dash.apl`](examples/2543-repeat-text-9-times-with-dash.apl) | نكرر ونفصل |
| 2544 | [`2544-pad-number-with-zeros-to-width-2.apl`](examples/2544-pad-number-with-zeros-to-width-2.apl) | zfill |
| 2545 | [`2545-pad-number-with-zeros-to-width-4.apl`](examples/2545-pad-number-with-zeros-to-width-4.apl) | zfill |
| 2546 | [`2546-pad-number-with-zeros-to-width-5.apl`](examples/2546-pad-number-with-zeros-to-width-5.apl) | zfill |
| 2547 | [`2547-pad-number-with-zeros-to-width-6.apl`](examples/2547-pad-number-with-zeros-to-width-6.apl) | zfill |
| 2548 | [`2548-pad-number-with-zeros-to-width-7.apl`](examples/2548-pad-number-with-zeros-to-width-7.apl) | zfill |
| 2549 | [`2549-truncate-text-to-first-1-chars.apl`](examples/2549-truncate-text-to-first-1-chars.apl) | شريحة |
| 2550 | [`2550-truncate-text-to-first-2-chars.apl`](examples/2550-truncate-text-to-first-2-chars.apl) | شريحة |
| 2551 | [`2551-truncate-text-to-first-4-chars.apl`](examples/2551-truncate-text-to-first-4-chars.apl) | شريحة |
| 2552 | [`2552-truncate-text-to-first-6-chars.apl`](examples/2552-truncate-text-to-first-6-chars.apl) | شريحة |
| 2553 | [`2553-truncate-text-to-first-7-chars.apl`](examples/2553-truncate-text-to-first-7-chars.apl) | شريحة |
| 2554 | [`2554-count-triples-sum-to-7-small.apl`](examples/2554-count-triples-sum-to-7-small.apl) | أ<=ب<=ج موجبة |
| 2555 | [`2555-count-triples-sum-to-8-small.apl`](examples/2555-count-triples-sum-to-8-small.apl) | أ<=ب<=ج موجبة |
| 2556 | [`2556-count-triples-sum-to-10-small.apl`](examples/2556-count-triples-sum-to-10-small.apl) | أ<=ب<=ج موجبة |
| 2557 | [`2557-count-triples-sum-to-11-small.apl`](examples/2557-count-triples-sum-to-11-small.apl) | أ<=ب<=ج موجبة |
| 2558 | [`2558-count-triples-sum-to-13-small.apl`](examples/2558-count-triples-sum-to-13-small.apl) | أ<=ب<=ج موجبة |
| 2559 | [`2559-sum-multiples-of-10-below-limit-v2.apl`](examples/2559-sum-multiples-of-10-below-limit-v2.apl) | نجمع مضاعفات 10 الأصغر من ن |
| 2560 | [`2560-sum-multiples-of-11-below-limit-v2.apl`](examples/2560-sum-multiples-of-11-below-limit-v2.apl) | نجمع مضاعفات 11 الأصغر من ن |
| 2561 | [`2561-sum-multiples-of-12-below-limit-v2.apl`](examples/2561-sum-multiples-of-12-below-limit-v2.apl) | نجمع مضاعفات 12 الأصغر من ن |
| 2562 | [`2562-sum-multiples-of-13-below-limit-v2.apl`](examples/2562-sum-multiples-of-13-below-limit-v2.apl) | نجمع مضاعفات 13 الأصغر من ن |
| 2563 | [`2563-sum-multiples-of-14-below-limit-v2.apl`](examples/2563-sum-multiples-of-14-below-limit-v2.apl) | نجمع مضاعفات 14 الأصغر من ن |
| 2564 | [`2564-count-multiples-of-10-up-to-limit.apl`](examples/2564-count-multiples-of-10-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2565 | [`2565-count-multiples-of-11-up-to-limit.apl`](examples/2565-count-multiples-of-11-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2566 | [`2566-count-multiples-of-12-up-to-limit.apl`](examples/2566-count-multiples-of-12-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2567 | [`2567-count-multiples-of-13-up-to-limit.apl`](examples/2567-count-multiples-of-13-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2568 | [`2568-count-multiples-of-14-up-to-limit.apl`](examples/2568-count-multiples-of-14-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2569 | [`2569-list-multiply-each-by-10.apl`](examples/2569-list-multiply-each-by-10.apl) | نبني قائمة جديدة |
| 2570 | [`2570-list-multiply-each-by-11.apl`](examples/2570-list-multiply-each-by-11.apl) | نبني قائمة جديدة |
| 2571 | [`2571-list-multiply-each-by-12.apl`](examples/2571-list-multiply-each-by-12.apl) | نبني قائمة جديدة |
| 2572 | [`2572-list-multiply-each-by-13.apl`](examples/2572-list-multiply-each-by-13.apl) | نبني قائمة جديدة |
| 2573 | [`2573-list-multiply-each-by-14.apl`](examples/2573-list-multiply-each-by-14.apl) | نبني قائمة جديدة |
| 2574 | [`2574-list-add-10-to-each-item.apl`](examples/2574-list-add-10-to-each-item.apl) | نزيد كل عنصر |
| 2575 | [`2575-list-add-11-to-each-item.apl`](examples/2575-list-add-11-to-each-item.apl) | نزيد كل عنصر |
| 2576 | [`2576-list-add-12-to-each-item.apl`](examples/2576-list-add-12-to-each-item.apl) | نزيد كل عنصر |
| 2577 | [`2577-list-add-13-to-each-item.apl`](examples/2577-list-add-13-to-each-item.apl) | نزيد كل عنصر |
| 2578 | [`2578-list-add-14-to-each-item.apl`](examples/2578-list-add-14-to-each-item.apl) | نزيد كل عنصر |
| 2579 | [`2579-list-count-greater-than-10.apl`](examples/2579-list-count-greater-than-10.apl) | نعد الأكبر |
| 2580 | [`2580-list-count-greater-than-11.apl`](examples/2580-list-count-greater-than-11.apl) | نعد الأكبر |
| 2581 | [`2581-list-count-greater-than-12.apl`](examples/2581-list-count-greater-than-12.apl) | نعد الأكبر |
| 2582 | [`2582-list-count-greater-than-13.apl`](examples/2582-list-count-greater-than-13.apl) | نعد الأكبر |
| 2583 | [`2583-list-count-greater-than-14.apl`](examples/2583-list-count-greater-than-14.apl) | نعد الأكبر |
| 2584 | [`2584-list-keep-divisible-by-10.apl`](examples/2584-list-keep-divisible-by-10.apl) | نصفي القائمة |
| 2585 | [`2585-list-keep-divisible-by-11.apl`](examples/2585-list-keep-divisible-by-11.apl) | نصفي القائمة |
| 2586 | [`2586-list-keep-divisible-by-12.apl`](examples/2586-list-keep-divisible-by-12.apl) | نصفي القائمة |
| 2587 | [`2587-list-keep-divisible-by-13.apl`](examples/2587-list-keep-divisible-by-13.apl) | نصفي القائمة |
| 2588 | [`2588-list-keep-divisible-by-14.apl`](examples/2588-list-keep-divisible-by-14.apl) | نصفي القائمة |
| 2589 | [`2589-digit-sum-of-10-to-the-power-n.apl`](examples/2589-digit-sum-of-10-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2590 | [`2590-digit-sum-of-11-to-the-power-n.apl`](examples/2590-digit-sum-of-11-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2591 | [`2591-digit-sum-of-12-to-the-power-n.apl`](examples/2591-digit-sum-of-12-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2592 | [`2592-digit-sum-of-13-to-the-power-n.apl`](examples/2592-digit-sum-of-13-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2593 | [`2593-digit-sum-of-14-to-the-power-n.apl`](examples/2593-digit-sum-of-14-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2594 | [`2594-sum-of-remainders-mod-10-up-to-n.apl`](examples/2594-sum-of-remainders-mod-10-up-to-n.apl) | نجمع ي % 10 |
| 2595 | [`2595-sum-of-remainders-mod-11-up-to-n.apl`](examples/2595-sum-of-remainders-mod-11-up-to-n.apl) | نجمع ي % 11 |
| 2596 | [`2596-sum-of-remainders-mod-12-up-to-n.apl`](examples/2596-sum-of-remainders-mod-12-up-to-n.apl) | نجمع ي % 12 |
| 2597 | [`2597-sum-of-remainders-mod-13-up-to-n.apl`](examples/2597-sum-of-remainders-mod-13-up-to-n.apl) | نجمع ي % 13 |
| 2598 | [`2598-sum-of-remainders-mod-14-up-to-n.apl`](examples/2598-sum-of-remainders-mod-14-up-to-n.apl) | نجمع ي % 14 |
| 2599 | [`2599-number-to-base-10-string-v2.apl`](examples/2599-number-to-base-10-string-v2.apl) | قسمة متكررة |
| 2600 | [`2600-number-to-base-11-string-v2.apl`](examples/2600-number-to-base-11-string-v2.apl) | قسمة متكررة |
| 2601 | [`2601-number-to-base-12-string-v2.apl`](examples/2601-number-to-base-12-string-v2.apl) | قسمة متكررة |
| 2602 | [`2602-number-to-base-13-string-v2.apl`](examples/2602-number-to-base-13-string-v2.apl) | قسمة متكررة |
| 2603 | [`2603-number-to-base-14-string-v2.apl`](examples/2603-number-to-base-14-string-v2.apl) | قسمة متكررة |
| 2604 | [`2604-count-numbers-below-hundred-with-digit-sum-10.apl`](examples/2604-count-numbers-below-hundred-with-digit-sum-10.apl) | نعد الأعداد |
| 2605 | [`2605-count-numbers-below-hundred-with-digit-sum-11.apl`](examples/2605-count-numbers-below-hundred-with-digit-sum-11.apl) | نعد الأعداد |
| 2606 | [`2606-count-numbers-below-hundred-with-digit-sum-12.apl`](examples/2606-count-numbers-below-hundred-with-digit-sum-12.apl) | نعد الأعداد |
| 2607 | [`2607-count-numbers-below-hundred-with-digit-sum-13.apl`](examples/2607-count-numbers-below-hundred-with-digit-sum-13.apl) | نعد الأعداد |
| 2608 | [`2608-count-numbers-below-hundred-with-digit-sum-14.apl`](examples/2608-count-numbers-below-hundred-with-digit-sum-14.apl) | نعد الأعداد |
| 2609 | [`2609-list-take-every-10th-item.apl`](examples/2609-list-take-every-10th-item.apl) | شريحة بخطوة |
| 2610 | [`2610-list-take-every-11th-item.apl`](examples/2610-list-take-every-11th-item.apl) | شريحة بخطوة |
| 2611 | [`2611-list-take-every-12th-item.apl`](examples/2611-list-take-every-12th-item.apl) | شريحة بخطوة |
| 2612 | [`2612-list-take-every-13th-item.apl`](examples/2612-list-take-every-13th-item.apl) | شريحة بخطوة |
| 2613 | [`2613-list-take-every-14th-item.apl`](examples/2613-list-take-every-14th-item.apl) | شريحة بخطوة |
| 2614 | [`2614-list-rotate-left-by-9.apl`](examples/2614-list-rotate-left-by-9.apl) | نقص ونلصق |
| 2615 | [`2615-list-rotate-left-by-10.apl`](examples/2615-list-rotate-left-by-10.apl) | نقص ونلصق |
| 2616 | [`2616-list-rotate-left-by-11.apl`](examples/2616-list-rotate-left-by-11.apl) | نقص ونلصق |
| 2617 | [`2617-list-rotate-left-by-12.apl`](examples/2617-list-rotate-left-by-12.apl) | نقص ونلصق |
| 2618 | [`2618-list-rotate-left-by-13.apl`](examples/2618-list-rotate-left-by-13.apl) | نقص ونلصق |
| 2619 | [`2619-nth-term-arithmetic-sequence-step-10.apl`](examples/2619-nth-term-arithmetic-sequence-step-10.apl) | أ + (ن-1)*10 |
| 2620 | [`2620-nth-term-arithmetic-sequence-step-11.apl`](examples/2620-nth-term-arithmetic-sequence-step-11.apl) | أ + (ن-1)*11 |
| 2621 | [`2621-nth-term-arithmetic-sequence-step-12.apl`](examples/2621-nth-term-arithmetic-sequence-step-12.apl) | أ + (ن-1)*12 |
| 2622 | [`2622-nth-term-arithmetic-sequence-step-13.apl`](examples/2622-nth-term-arithmetic-sequence-step-13.apl) | أ + (ن-1)*13 |
| 2623 | [`2623-nth-term-arithmetic-sequence-step-14.apl`](examples/2623-nth-term-arithmetic-sequence-step-14.apl) | أ + (ن-1)*14 |
| 2624 | [`2624-sum-of-powers-of-10-up-to-n.apl`](examples/2624-sum-of-powers-of-10-up-to-n.apl) | نجمع 10^ي |
| 2625 | [`2625-sum-of-powers-of-11-up-to-n.apl`](examples/2625-sum-of-powers-of-11-up-to-n.apl) | نجمع 11^ي |
| 2626 | [`2626-sum-of-powers-of-12-up-to-n.apl`](examples/2626-sum-of-powers-of-12-up-to-n.apl) | نجمع 12^ي |
| 2627 | [`2627-sum-of-powers-of-13-up-to-n.apl`](examples/2627-sum-of-powers-of-13-up-to-n.apl) | نجمع 13^ي |
| 2628 | [`2628-sum-of-powers-of-14-up-to-n.apl`](examples/2628-sum-of-powers-of-14-up-to-n.apl) | نجمع 14^ي |
| 2629 | [`2629-clamp-list-values-to-max-10.apl`](examples/2629-clamp-list-values-to-max-10.apl) | نقص ما يزيد |
| 2630 | [`2630-clamp-list-values-to-max-11.apl`](examples/2630-clamp-list-values-to-max-11.apl) | نقص ما يزيد |
| 2631 | [`2631-clamp-list-values-to-max-12.apl`](examples/2631-clamp-list-values-to-max-12.apl) | نقص ما يزيد |
| 2632 | [`2632-clamp-list-values-to-max-13.apl`](examples/2632-clamp-list-values-to-max-13.apl) | نقص ما يزيد |
| 2633 | [`2633-clamp-list-values-to-max-14.apl`](examples/2633-clamp-list-values-to-max-14.apl) | نقص ما يزيد |
| 2634 | [`2634-caesar-shift-by-8-lowercase.apl`](examples/2634-caesar-shift-by-8-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2635 | [`2635-caesar-shift-by-9-lowercase.apl`](examples/2635-caesar-shift-by-9-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2636 | [`2636-caesar-shift-by-10-lowercase.apl`](examples/2636-caesar-shift-by-10-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2637 | [`2637-caesar-shift-by-11-lowercase.apl`](examples/2637-caesar-shift-by-11-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2638 | [`2638-caesar-shift-by-12-lowercase.apl`](examples/2638-caesar-shift-by-12-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2639 | [`2639-repeat-text-10-times-with-dash.apl`](examples/2639-repeat-text-10-times-with-dash.apl) | نكرر ونفصل |
| 2640 | [`2640-repeat-text-11-times-with-dash.apl`](examples/2640-repeat-text-11-times-with-dash.apl) | نكرر ونفصل |
| 2641 | [`2641-repeat-text-12-times-with-dash.apl`](examples/2641-repeat-text-12-times-with-dash.apl) | نكرر ونفصل |
| 2642 | [`2642-repeat-text-13-times-with-dash.apl`](examples/2642-repeat-text-13-times-with-dash.apl) | نكرر ونفصل |
| 2643 | [`2643-repeat-text-14-times-with-dash.apl`](examples/2643-repeat-text-14-times-with-dash.apl) | نكرر ونفصل |
| 2644 | [`2644-pad-number-with-zeros-to-width-9.apl`](examples/2644-pad-number-with-zeros-to-width-9.apl) | zfill |
| 2645 | [`2645-pad-number-with-zeros-to-width-11.apl`](examples/2645-pad-number-with-zeros-to-width-11.apl) | zfill |
| 2646 | [`2646-pad-number-with-zeros-to-width-12.apl`](examples/2646-pad-number-with-zeros-to-width-12.apl) | zfill |
| 2647 | [`2647-pad-number-with-zeros-to-width-13.apl`](examples/2647-pad-number-with-zeros-to-width-13.apl) | zfill |
| 2648 | [`2648-pad-number-with-zeros-to-width-14.apl`](examples/2648-pad-number-with-zeros-to-width-14.apl) | zfill |
| 2649 | [`2649-truncate-text-to-first-9-chars.apl`](examples/2649-truncate-text-to-first-9-chars.apl) | شريحة |
| 2650 | [`2650-truncate-text-to-first-10-chars.apl`](examples/2650-truncate-text-to-first-10-chars.apl) | شريحة |
| 2651 | [`2651-truncate-text-to-first-11-chars.apl`](examples/2651-truncate-text-to-first-11-chars.apl) | شريحة |
| 2652 | [`2652-truncate-text-to-first-12-chars.apl`](examples/2652-truncate-text-to-first-12-chars.apl) | شريحة |
| 2653 | [`2653-truncate-text-to-first-13-chars.apl`](examples/2653-truncate-text-to-first-13-chars.apl) | شريحة |
| 2654 | [`2654-count-triples-sum-to-14-small.apl`](examples/2654-count-triples-sum-to-14-small.apl) | أ<=ب<=ج موجبة |
| 2655 | [`2655-count-triples-sum-to-15-small.apl`](examples/2655-count-triples-sum-to-15-small.apl) | أ<=ب<=ج موجبة |
| 2656 | [`2656-count-triples-sum-to-16-small.apl`](examples/2656-count-triples-sum-to-16-small.apl) | أ<=ب<=ج موجبة |
| 2657 | [`2657-count-triples-sum-to-17-small.apl`](examples/2657-count-triples-sum-to-17-small.apl) | أ<=ب<=ج موجبة |
| 2658 | [`2658-count-triples-sum-to-18-small.apl`](examples/2658-count-triples-sum-to-18-small.apl) | أ<=ب<=ج موجبة |
| 2659 | [`2659-sum-of-integers-from-2-to-n.apl`](examples/2659-sum-of-integers-from-2-to-n.apl) | نجمع بحلقة |
| 2660 | [`2660-sum-of-integers-from-3-to-n.apl`](examples/2660-sum-of-integers-from-3-to-n.apl) | نجمع بحلقة |
| 2661 | [`2661-sum-of-integers-from-5-to-n.apl`](examples/2661-sum-of-integers-from-5-to-n.apl) | نجمع بحلقة |
| 2662 | [`2662-count-numbers-with-exactly-2-divisors-below-limit.apl`](examples/2662-count-numbers-with-exactly-2-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 2663 | [`2663-count-numbers-with-exactly-3-divisors-below-limit.apl`](examples/2663-count-numbers-with-exactly-3-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 2664 | [`2664-count-numbers-with-exactly-5-divisors-below-limit.apl`](examples/2664-count-numbers-with-exactly-5-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 2665 | [`2665-list-element-at-index-0-or-default.apl`](examples/2665-list-element-at-index-0-or-default.apl) | نتحقق من الطول |
| 2666 | [`2666-list-element-at-index-1-or-default.apl`](examples/2666-list-element-at-index-1-or-default.apl) | نتحقق من الطول |
| 2667 | [`2667-list-element-at-index-2-or-default.apl`](examples/2667-list-element-at-index-2-or-default.apl) | نتحقق من الطول |
| 2668 | [`2668-list-count-items-with-remainder-one-mod-2.apl`](examples/2668-list-count-items-with-remainder-one-mod-2.apl) | نعد |
| 2669 | [`2669-list-count-items-with-remainder-one-mod-3.apl`](examples/2669-list-count-items-with-remainder-one-mod-3.apl) | نعد |
| 2670 | [`2670-list-count-items-with-remainder-one-mod-5.apl`](examples/2670-list-count-items-with-remainder-one-mod-5.apl) | نعد |
| 2671 | [`2671-price-after-2-percent-discount-integer.apl`](examples/2671-price-after-2-percent-discount-integer.apl) | نطرح الخصم |
| 2672 | [`2672-price-after-3-percent-discount-integer.apl`](examples/2672-price-after-3-percent-discount-integer.apl) | نطرح الخصم |
| 2673 | [`2673-price-after-5-percent-discount-integer.apl`](examples/2673-price-after-5-percent-discount-integer.apl) | نطرح الخصم |
| 2674 | [`2674-price-with-2-percent-tax-integer.apl`](examples/2674-price-with-2-percent-tax-integer.apl) | نضيف الضريبة |
| 2675 | [`2675-price-with-3-percent-tax-integer.apl`](examples/2675-price-with-3-percent-tax-integer.apl) | نضيف الضريبة |
| 2676 | [`2676-price-with-5-percent-tax-integer.apl`](examples/2676-price-with-5-percent-tax-integer.apl) | نضيف الضريبة |
| 2677 | [`2677-split-bill-among-2-people-ceiling.apl`](examples/2677-split-bill-among-2-people-ceiling.apl) | نقرب لأعلى |
| 2678 | [`2678-split-bill-among-3-people-ceiling.apl`](examples/2678-split-bill-among-3-people-ceiling.apl) | نقرب لأعلى |
| 2679 | [`2679-split-bill-among-5-people-ceiling.apl`](examples/2679-split-bill-among-5-people-ceiling.apl) | نقرب لأعلى |
| 2680 | [`2680-minutes-to-hours-and-minutes-base-2.apl`](examples/2680-minutes-to-hours-and-minutes-base-2.apl) | نقسم على 2 |
| 2681 | [`2681-minutes-to-hours-and-minutes-base-3.apl`](examples/2681-minutes-to-hours-and-minutes-base-3.apl) | نقسم على 3 |
| 2682 | [`2682-minutes-to-hours-and-minutes-base-5.apl`](examples/2682-minutes-to-hours-and-minutes-base-5.apl) | نقسم على 5 |
| 2683 | [`2683-count-words-with-length-at-least-2.apl`](examples/2683-count-words-with-length-at-least-2.apl) | نعد الكلمات |
| 2684 | [`2684-count-words-with-length-at-least-3.apl`](examples/2684-count-words-with-length-at-least-3.apl) | نعد الكلمات |
| 2685 | [`2685-count-words-with-length-at-least-5.apl`](examples/2685-count-words-with-length-at-least-5.apl) | نعد الكلمات |
| 2686 | [`2686-count-letter-a-in-text-v0.apl`](examples/2686-count-letter-a-in-text-v0.apl) | نعد ظهور الحرف |
| 2687 | [`2687-count-letter-e-in-text-v1.apl`](examples/2687-count-letter-e-in-text-v1.apl) | نعد ظهور الحرف |
| 2688 | [`2688-count-letter-i-in-text-v2.apl`](examples/2688-count-letter-i-in-text-v2.apl) | نعد ظهور الحرف |
| 2689 | [`2689-count-letter-o-in-text-v3.apl`](examples/2689-count-letter-o-in-text-v3.apl) | نعد ظهور الحرف |
| 2690 | [`2690-count-letter-s-in-text-v4.apl`](examples/2690-count-letter-s-in-text-v4.apl) | نعد ظهور الحرف |
| 2691 | [`2691-sum-multiples-of-15-below-limit-v2.apl`](examples/2691-sum-multiples-of-15-below-limit-v2.apl) | نجمع مضاعفات 15 الأصغر من ن |
| 2692 | [`2692-sum-multiples-of-16-below-limit-v2.apl`](examples/2692-sum-multiples-of-16-below-limit-v2.apl) | نجمع مضاعفات 16 الأصغر من ن |
| 2693 | [`2693-sum-multiples-of-17-below-limit-v2.apl`](examples/2693-sum-multiples-of-17-below-limit-v2.apl) | نجمع مضاعفات 17 الأصغر من ن |
| 2694 | [`2694-sum-multiples-of-18-below-limit-v2.apl`](examples/2694-sum-multiples-of-18-below-limit-v2.apl) | نجمع مضاعفات 18 الأصغر من ن |
| 2695 | [`2695-sum-multiples-of-19-below-limit-v2.apl`](examples/2695-sum-multiples-of-19-below-limit-v2.apl) | نجمع مضاعفات 19 الأصغر من ن |
| 2696 | [`2696-count-multiples-of-15-up-to-limit.apl`](examples/2696-count-multiples-of-15-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2697 | [`2697-count-multiples-of-16-up-to-limit.apl`](examples/2697-count-multiples-of-16-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2698 | [`2698-count-multiples-of-17-up-to-limit.apl`](examples/2698-count-multiples-of-17-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2699 | [`2699-count-multiples-of-18-up-to-limit.apl`](examples/2699-count-multiples-of-18-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2700 | [`2700-count-multiples-of-19-up-to-limit.apl`](examples/2700-count-multiples-of-19-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2701 | [`2701-list-multiply-each-by-15.apl`](examples/2701-list-multiply-each-by-15.apl) | نبني قائمة جديدة |
| 2702 | [`2702-list-multiply-each-by-16.apl`](examples/2702-list-multiply-each-by-16.apl) | نبني قائمة جديدة |
| 2703 | [`2703-list-multiply-each-by-17.apl`](examples/2703-list-multiply-each-by-17.apl) | نبني قائمة جديدة |
| 2704 | [`2704-list-multiply-each-by-18.apl`](examples/2704-list-multiply-each-by-18.apl) | نبني قائمة جديدة |
| 2705 | [`2705-list-multiply-each-by-19.apl`](examples/2705-list-multiply-each-by-19.apl) | نبني قائمة جديدة |
| 2706 | [`2706-list-add-15-to-each-item.apl`](examples/2706-list-add-15-to-each-item.apl) | نزيد كل عنصر |
| 2707 | [`2707-list-add-16-to-each-item.apl`](examples/2707-list-add-16-to-each-item.apl) | نزيد كل عنصر |
| 2708 | [`2708-list-add-17-to-each-item.apl`](examples/2708-list-add-17-to-each-item.apl) | نزيد كل عنصر |
| 2709 | [`2709-list-add-18-to-each-item.apl`](examples/2709-list-add-18-to-each-item.apl) | نزيد كل عنصر |
| 2710 | [`2710-list-add-19-to-each-item.apl`](examples/2710-list-add-19-to-each-item.apl) | نزيد كل عنصر |
| 2711 | [`2711-list-count-greater-than-15.apl`](examples/2711-list-count-greater-than-15.apl) | نعد الأكبر |
| 2712 | [`2712-list-count-greater-than-16.apl`](examples/2712-list-count-greater-than-16.apl) | نعد الأكبر |
| 2713 | [`2713-list-count-greater-than-17.apl`](examples/2713-list-count-greater-than-17.apl) | نعد الأكبر |
| 2714 | [`2714-list-count-greater-than-18.apl`](examples/2714-list-count-greater-than-18.apl) | نعد الأكبر |
| 2715 | [`2715-list-count-greater-than-19.apl`](examples/2715-list-count-greater-than-19.apl) | نعد الأكبر |
| 2716 | [`2716-list-keep-divisible-by-15.apl`](examples/2716-list-keep-divisible-by-15.apl) | نصفي القائمة |
| 2717 | [`2717-list-keep-divisible-by-16.apl`](examples/2717-list-keep-divisible-by-16.apl) | نصفي القائمة |
| 2718 | [`2718-list-keep-divisible-by-17.apl`](examples/2718-list-keep-divisible-by-17.apl) | نصفي القائمة |
| 2719 | [`2719-list-keep-divisible-by-18.apl`](examples/2719-list-keep-divisible-by-18.apl) | نصفي القائمة |
| 2720 | [`2720-list-keep-divisible-by-19.apl`](examples/2720-list-keep-divisible-by-19.apl) | نصفي القائمة |
| 2721 | [`2721-digit-sum-of-15-to-the-power-n.apl`](examples/2721-digit-sum-of-15-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2722 | [`2722-digit-sum-of-16-to-the-power-n.apl`](examples/2722-digit-sum-of-16-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2723 | [`2723-digit-sum-of-17-to-the-power-n.apl`](examples/2723-digit-sum-of-17-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2724 | [`2724-digit-sum-of-18-to-the-power-n.apl`](examples/2724-digit-sum-of-18-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2725 | [`2725-digit-sum-of-19-to-the-power-n.apl`](examples/2725-digit-sum-of-19-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2726 | [`2726-sum-of-remainders-mod-15-up-to-n.apl`](examples/2726-sum-of-remainders-mod-15-up-to-n.apl) | نجمع ي % 15 |
| 2727 | [`2727-sum-of-remainders-mod-16-up-to-n.apl`](examples/2727-sum-of-remainders-mod-16-up-to-n.apl) | نجمع ي % 16 |
| 2728 | [`2728-sum-of-remainders-mod-17-up-to-n.apl`](examples/2728-sum-of-remainders-mod-17-up-to-n.apl) | نجمع ي % 17 |
| 2729 | [`2729-sum-of-remainders-mod-18-up-to-n.apl`](examples/2729-sum-of-remainders-mod-18-up-to-n.apl) | نجمع ي % 18 |
| 2730 | [`2730-sum-of-remainders-mod-19-up-to-n.apl`](examples/2730-sum-of-remainders-mod-19-up-to-n.apl) | نجمع ي % 19 |
| 2731 | [`2731-count-numbers-below-hundred-with-digit-sum-15.apl`](examples/2731-count-numbers-below-hundred-with-digit-sum-15.apl) | نعد الأعداد |
| 2732 | [`2732-count-numbers-below-hundred-with-digit-sum-16.apl`](examples/2732-count-numbers-below-hundred-with-digit-sum-16.apl) | نعد الأعداد |
| 2733 | [`2733-count-numbers-below-hundred-with-digit-sum-17.apl`](examples/2733-count-numbers-below-hundred-with-digit-sum-17.apl) | نعد الأعداد |
| 2734 | [`2734-count-numbers-below-hundred-with-digit-sum-18.apl`](examples/2734-count-numbers-below-hundred-with-digit-sum-18.apl) | نعد الأعداد |
| 2735 | [`2735-count-numbers-below-hundred-with-digit-sum-19.apl`](examples/2735-count-numbers-below-hundred-with-digit-sum-19.apl) | نعد الأعداد |
| 2736 | [`2736-list-take-every-15th-item.apl`](examples/2736-list-take-every-15th-item.apl) | شريحة بخطوة |
| 2737 | [`2737-list-take-every-16th-item.apl`](examples/2737-list-take-every-16th-item.apl) | شريحة بخطوة |
| 2738 | [`2738-list-take-every-17th-item.apl`](examples/2738-list-take-every-17th-item.apl) | شريحة بخطوة |
| 2739 | [`2739-list-take-every-18th-item.apl`](examples/2739-list-take-every-18th-item.apl) | شريحة بخطوة |
| 2740 | [`2740-list-take-every-19th-item.apl`](examples/2740-list-take-every-19th-item.apl) | شريحة بخطوة |
| 2741 | [`2741-list-rotate-left-by-14.apl`](examples/2741-list-rotate-left-by-14.apl) | نقص ونلصق |
| 2742 | [`2742-list-rotate-left-by-15.apl`](examples/2742-list-rotate-left-by-15.apl) | نقص ونلصق |
| 2743 | [`2743-list-rotate-left-by-16.apl`](examples/2743-list-rotate-left-by-16.apl) | نقص ونلصق |
| 2744 | [`2744-list-rotate-left-by-17.apl`](examples/2744-list-rotate-left-by-17.apl) | نقص ونلصق |
| 2745 | [`2745-list-rotate-left-by-18.apl`](examples/2745-list-rotate-left-by-18.apl) | نقص ونلصق |
| 2746 | [`2746-nth-term-arithmetic-sequence-step-15.apl`](examples/2746-nth-term-arithmetic-sequence-step-15.apl) | أ + (ن-1)*15 |
| 2747 | [`2747-nth-term-arithmetic-sequence-step-16.apl`](examples/2747-nth-term-arithmetic-sequence-step-16.apl) | أ + (ن-1)*16 |
| 2748 | [`2748-nth-term-arithmetic-sequence-step-17.apl`](examples/2748-nth-term-arithmetic-sequence-step-17.apl) | أ + (ن-1)*17 |
| 2749 | [`2749-nth-term-arithmetic-sequence-step-18.apl`](examples/2749-nth-term-arithmetic-sequence-step-18.apl) | أ + (ن-1)*18 |
| 2750 | [`2750-nth-term-arithmetic-sequence-step-19.apl`](examples/2750-nth-term-arithmetic-sequence-step-19.apl) | أ + (ن-1)*19 |
| 2751 | [`2751-sum-of-powers-of-15-up-to-n.apl`](examples/2751-sum-of-powers-of-15-up-to-n.apl) | نجمع 15^ي |
| 2752 | [`2752-sum-of-powers-of-16-up-to-n.apl`](examples/2752-sum-of-powers-of-16-up-to-n.apl) | نجمع 16^ي |
| 2753 | [`2753-sum-of-powers-of-17-up-to-n.apl`](examples/2753-sum-of-powers-of-17-up-to-n.apl) | نجمع 17^ي |
| 2754 | [`2754-sum-of-powers-of-18-up-to-n.apl`](examples/2754-sum-of-powers-of-18-up-to-n.apl) | نجمع 18^ي |
| 2755 | [`2755-sum-of-powers-of-19-up-to-n.apl`](examples/2755-sum-of-powers-of-19-up-to-n.apl) | نجمع 19^ي |
| 2756 | [`2756-clamp-list-values-to-max-15.apl`](examples/2756-clamp-list-values-to-max-15.apl) | نقص ما يزيد |
| 2757 | [`2757-clamp-list-values-to-max-16.apl`](examples/2757-clamp-list-values-to-max-16.apl) | نقص ما يزيد |
| 2758 | [`2758-clamp-list-values-to-max-17.apl`](examples/2758-clamp-list-values-to-max-17.apl) | نقص ما يزيد |
| 2759 | [`2759-clamp-list-values-to-max-18.apl`](examples/2759-clamp-list-values-to-max-18.apl) | نقص ما يزيد |
| 2760 | [`2760-clamp-list-values-to-max-19.apl`](examples/2760-clamp-list-values-to-max-19.apl) | نقص ما يزيد |
| 2761 | [`2761-caesar-shift-by-14-lowercase.apl`](examples/2761-caesar-shift-by-14-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2762 | [`2762-caesar-shift-by-15-lowercase.apl`](examples/2762-caesar-shift-by-15-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2763 | [`2763-caesar-shift-by-16-lowercase.apl`](examples/2763-caesar-shift-by-16-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2764 | [`2764-caesar-shift-by-17-lowercase.apl`](examples/2764-caesar-shift-by-17-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2765 | [`2765-caesar-shift-by-18-lowercase.apl`](examples/2765-caesar-shift-by-18-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2766 | [`2766-repeat-text-15-times-with-dash.apl`](examples/2766-repeat-text-15-times-with-dash.apl) | نكرر ونفصل |
| 2767 | [`2767-repeat-text-16-times-with-dash.apl`](examples/2767-repeat-text-16-times-with-dash.apl) | نكرر ونفصل |
| 2768 | [`2768-repeat-text-17-times-with-dash.apl`](examples/2768-repeat-text-17-times-with-dash.apl) | نكرر ونفصل |
| 2769 | [`2769-repeat-text-18-times-with-dash.apl`](examples/2769-repeat-text-18-times-with-dash.apl) | نكرر ونفصل |
| 2770 | [`2770-repeat-text-19-times-with-dash.apl`](examples/2770-repeat-text-19-times-with-dash.apl) | نكرر ونفصل |
| 2771 | [`2771-pad-number-with-zeros-to-width-15.apl`](examples/2771-pad-number-with-zeros-to-width-15.apl) | zfill |
| 2772 | [`2772-pad-number-with-zeros-to-width-16.apl`](examples/2772-pad-number-with-zeros-to-width-16.apl) | zfill |
| 2773 | [`2773-pad-number-with-zeros-to-width-17.apl`](examples/2773-pad-number-with-zeros-to-width-17.apl) | zfill |
| 2774 | [`2774-pad-number-with-zeros-to-width-18.apl`](examples/2774-pad-number-with-zeros-to-width-18.apl) | zfill |
| 2775 | [`2775-pad-number-with-zeros-to-width-19.apl`](examples/2775-pad-number-with-zeros-to-width-19.apl) | zfill |
| 2776 | [`2776-truncate-text-to-first-14-chars.apl`](examples/2776-truncate-text-to-first-14-chars.apl) | شريحة |
| 2777 | [`2777-truncate-text-to-first-15-chars.apl`](examples/2777-truncate-text-to-first-15-chars.apl) | شريحة |
| 2778 | [`2778-truncate-text-to-first-16-chars.apl`](examples/2778-truncate-text-to-first-16-chars.apl) | شريحة |
| 2779 | [`2779-truncate-text-to-first-17-chars.apl`](examples/2779-truncate-text-to-first-17-chars.apl) | شريحة |
| 2780 | [`2780-truncate-text-to-first-18-chars.apl`](examples/2780-truncate-text-to-first-18-chars.apl) | شريحة |
| 2781 | [`2781-count-triples-sum-to-19-small.apl`](examples/2781-count-triples-sum-to-19-small.apl) | أ<=ب<=ج موجبة |
| 2782 | [`2782-count-triples-sum-to-20-small.apl`](examples/2782-count-triples-sum-to-20-small.apl) | أ<=ب<=ج موجبة |
| 2783 | [`2783-count-triples-sum-to-21-small.apl`](examples/2783-count-triples-sum-to-21-small.apl) | أ<=ب<=ج موجبة |
| 2784 | [`2784-count-triples-sum-to-22-small.apl`](examples/2784-count-triples-sum-to-22-small.apl) | أ<=ب<=ج موجبة |
| 2785 | [`2785-count-triples-sum-to-23-small.apl`](examples/2785-count-triples-sum-to-23-small.apl) | أ<=ب<=ج موجبة |
| 2786 | [`2786-sum-of-integers-from-4-to-n.apl`](examples/2786-sum-of-integers-from-4-to-n.apl) | نجمع بحلقة |
| 2787 | [`2787-sum-of-integers-from-6-to-n.apl`](examples/2787-sum-of-integers-from-6-to-n.apl) | نجمع بحلقة |
| 2788 | [`2788-sum-of-integers-from-7-to-n.apl`](examples/2788-sum-of-integers-from-7-to-n.apl) | نجمع بحلقة |
| 2789 | [`2789-sum-of-integers-from-8-to-n.apl`](examples/2789-sum-of-integers-from-8-to-n.apl) | نجمع بحلقة |
| 2790 | [`2790-sum-of-integers-from-9-to-n.apl`](examples/2790-sum-of-integers-from-9-to-n.apl) | نجمع بحلقة |
| 2791 | [`2791-count-numbers-with-exactly-4-divisors-below-limit.apl`](examples/2791-count-numbers-with-exactly-4-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 2792 | [`2792-count-numbers-with-exactly-6-divisors-below-limit.apl`](examples/2792-count-numbers-with-exactly-6-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 2793 | [`2793-count-numbers-with-exactly-7-divisors-below-limit.apl`](examples/2793-count-numbers-with-exactly-7-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 2794 | [`2794-count-numbers-with-exactly-8-divisors-below-limit.apl`](examples/2794-count-numbers-with-exactly-8-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 2795 | [`2795-count-numbers-with-exactly-9-divisors-below-limit.apl`](examples/2795-count-numbers-with-exactly-9-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 2796 | [`2796-list-element-at-index-3-or-default.apl`](examples/2796-list-element-at-index-3-or-default.apl) | نتحقق من الطول |
| 2797 | [`2797-list-element-at-index-4-or-default.apl`](examples/2797-list-element-at-index-4-or-default.apl) | نتحقق من الطول |
| 2798 | [`2798-list-element-at-index-5-or-default.apl`](examples/2798-list-element-at-index-5-or-default.apl) | نتحقق من الطول |
| 2799 | [`2799-list-count-items-with-remainder-one-mod-4.apl`](examples/2799-list-count-items-with-remainder-one-mod-4.apl) | نعد |
| 2800 | [`2800-list-count-items-with-remainder-one-mod-6.apl`](examples/2800-list-count-items-with-remainder-one-mod-6.apl) | نعد |
| 2801 | [`2801-list-count-items-with-remainder-one-mod-7.apl`](examples/2801-list-count-items-with-remainder-one-mod-7.apl) | نعد |
| 2802 | [`2802-list-count-items-with-remainder-one-mod-8.apl`](examples/2802-list-count-items-with-remainder-one-mod-8.apl) | نعد |
| 2803 | [`2803-list-count-items-with-remainder-one-mod-9.apl`](examples/2803-list-count-items-with-remainder-one-mod-9.apl) | نعد |
| 2804 | [`2804-price-after-4-percent-discount-integer.apl`](examples/2804-price-after-4-percent-discount-integer.apl) | نطرح الخصم |
| 2805 | [`2805-price-after-6-percent-discount-integer.apl`](examples/2805-price-after-6-percent-discount-integer.apl) | نطرح الخصم |
| 2806 | [`2806-price-after-7-percent-discount-integer.apl`](examples/2806-price-after-7-percent-discount-integer.apl) | نطرح الخصم |
| 2807 | [`2807-price-after-8-percent-discount-integer.apl`](examples/2807-price-after-8-percent-discount-integer.apl) | نطرح الخصم |
| 2808 | [`2808-price-after-9-percent-discount-integer.apl`](examples/2808-price-after-9-percent-discount-integer.apl) | نطرح الخصم |
| 2809 | [`2809-price-with-4-percent-tax-integer.apl`](examples/2809-price-with-4-percent-tax-integer.apl) | نضيف الضريبة |
| 2810 | [`2810-price-with-6-percent-tax-integer.apl`](examples/2810-price-with-6-percent-tax-integer.apl) | نضيف الضريبة |
| 2811 | [`2811-price-with-7-percent-tax-integer.apl`](examples/2811-price-with-7-percent-tax-integer.apl) | نضيف الضريبة |
| 2812 | [`2812-price-with-8-percent-tax-integer.apl`](examples/2812-price-with-8-percent-tax-integer.apl) | نضيف الضريبة |
| 2813 | [`2813-price-with-9-percent-tax-integer.apl`](examples/2813-price-with-9-percent-tax-integer.apl) | نضيف الضريبة |
| 2814 | [`2814-split-bill-among-4-people-ceiling.apl`](examples/2814-split-bill-among-4-people-ceiling.apl) | نقرب لأعلى |
| 2815 | [`2815-split-bill-among-6-people-ceiling.apl`](examples/2815-split-bill-among-6-people-ceiling.apl) | نقرب لأعلى |
| 2816 | [`2816-split-bill-among-7-people-ceiling.apl`](examples/2816-split-bill-among-7-people-ceiling.apl) | نقرب لأعلى |
| 2817 | [`2817-split-bill-among-8-people-ceiling.apl`](examples/2817-split-bill-among-8-people-ceiling.apl) | نقرب لأعلى |
| 2818 | [`2818-split-bill-among-9-people-ceiling.apl`](examples/2818-split-bill-among-9-people-ceiling.apl) | نقرب لأعلى |
| 2819 | [`2819-minutes-to-hours-and-minutes-base-4.apl`](examples/2819-minutes-to-hours-and-minutes-base-4.apl) | نقسم على 4 |
| 2820 | [`2820-minutes-to-hours-and-minutes-base-6.apl`](examples/2820-minutes-to-hours-and-minutes-base-6.apl) | نقسم على 6 |
| 2821 | [`2821-minutes-to-hours-and-minutes-base-7.apl`](examples/2821-minutes-to-hours-and-minutes-base-7.apl) | نقسم على 7 |
| 2822 | [`2822-minutes-to-hours-and-minutes-base-8.apl`](examples/2822-minutes-to-hours-and-minutes-base-8.apl) | نقسم على 8 |
| 2823 | [`2823-minutes-to-hours-and-minutes-base-9.apl`](examples/2823-minutes-to-hours-and-minutes-base-9.apl) | نقسم على 9 |
| 2824 | [`2824-count-words-with-length-at-least-4.apl`](examples/2824-count-words-with-length-at-least-4.apl) | نعد الكلمات |
| 2825 | [`2825-count-words-with-length-at-least-6.apl`](examples/2825-count-words-with-length-at-least-6.apl) | نعد الكلمات |
| 2826 | [`2826-count-words-with-length-at-least-7.apl`](examples/2826-count-words-with-length-at-least-7.apl) | نعد الكلمات |
| 2827 | [`2827-count-words-with-length-at-least-8.apl`](examples/2827-count-words-with-length-at-least-8.apl) | نعد الكلمات |
| 2828 | [`2828-count-words-with-length-at-least-9.apl`](examples/2828-count-words-with-length-at-least-9.apl) | نعد الكلمات |
| 2829 | [`2829-count-letter-t-in-text-v5.apl`](examples/2829-count-letter-t-in-text-v5.apl) | نعد ظهور الحرف |
| 2830 | [`2830-count-letter-a-in-text-v6.apl`](examples/2830-count-letter-a-in-text-v6.apl) | نعد ظهور الحرف |
| 2831 | [`2831-count-letter-e-in-text-v7.apl`](examples/2831-count-letter-e-in-text-v7.apl) | نعد ظهور الحرف |
| 2832 | [`2832-count-letter-i-in-text-v8.apl`](examples/2832-count-letter-i-in-text-v8.apl) | نعد ظهور الحرف |
| 2833 | [`2833-count-letter-o-in-text-v9.apl`](examples/2833-count-letter-o-in-text-v9.apl) | نعد ظهور الحرف |
| 2834 | [`2834-sum-multiples-of-20-below-limit-v2.apl`](examples/2834-sum-multiples-of-20-below-limit-v2.apl) | نجمع مضاعفات 20 الأصغر من ن |
| 2835 | [`2835-sum-multiples-of-21-below-limit-v2.apl`](examples/2835-sum-multiples-of-21-below-limit-v2.apl) | نجمع مضاعفات 21 الأصغر من ن |
| 2836 | [`2836-sum-multiples-of-22-below-limit-v2.apl`](examples/2836-sum-multiples-of-22-below-limit-v2.apl) | نجمع مضاعفات 22 الأصغر من ن |
| 2837 | [`2837-sum-multiples-of-23-below-limit-v2.apl`](examples/2837-sum-multiples-of-23-below-limit-v2.apl) | نجمع مضاعفات 23 الأصغر من ن |
| 2838 | [`2838-sum-multiples-of-24-below-limit-v2.apl`](examples/2838-sum-multiples-of-24-below-limit-v2.apl) | نجمع مضاعفات 24 الأصغر من ن |
| 2839 | [`2839-count-multiples-of-20-up-to-limit.apl`](examples/2839-count-multiples-of-20-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2840 | [`2840-count-multiples-of-21-up-to-limit.apl`](examples/2840-count-multiples-of-21-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2841 | [`2841-count-multiples-of-22-up-to-limit.apl`](examples/2841-count-multiples-of-22-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2842 | [`2842-count-multiples-of-23-up-to-limit.apl`](examples/2842-count-multiples-of-23-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2843 | [`2843-count-multiples-of-24-up-to-limit.apl`](examples/2843-count-multiples-of-24-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2844 | [`2844-list-multiply-each-by-20.apl`](examples/2844-list-multiply-each-by-20.apl) | نبني قائمة جديدة |
| 2845 | [`2845-list-multiply-each-by-21.apl`](examples/2845-list-multiply-each-by-21.apl) | نبني قائمة جديدة |
| 2846 | [`2846-list-multiply-each-by-22.apl`](examples/2846-list-multiply-each-by-22.apl) | نبني قائمة جديدة |
| 2847 | [`2847-list-multiply-each-by-23.apl`](examples/2847-list-multiply-each-by-23.apl) | نبني قائمة جديدة |
| 2848 | [`2848-list-multiply-each-by-24.apl`](examples/2848-list-multiply-each-by-24.apl) | نبني قائمة جديدة |
| 2849 | [`2849-list-add-20-to-each-item.apl`](examples/2849-list-add-20-to-each-item.apl) | نزيد كل عنصر |
| 2850 | [`2850-list-add-21-to-each-item.apl`](examples/2850-list-add-21-to-each-item.apl) | نزيد كل عنصر |
| 2851 | [`2851-list-add-22-to-each-item.apl`](examples/2851-list-add-22-to-each-item.apl) | نزيد كل عنصر |
| 2852 | [`2852-list-add-23-to-each-item.apl`](examples/2852-list-add-23-to-each-item.apl) | نزيد كل عنصر |
| 2853 | [`2853-list-add-24-to-each-item.apl`](examples/2853-list-add-24-to-each-item.apl) | نزيد كل عنصر |
| 2854 | [`2854-list-count-greater-than-20.apl`](examples/2854-list-count-greater-than-20.apl) | نعد الأكبر |
| 2855 | [`2855-list-count-greater-than-21.apl`](examples/2855-list-count-greater-than-21.apl) | نعد الأكبر |
| 2856 | [`2856-list-count-greater-than-22.apl`](examples/2856-list-count-greater-than-22.apl) | نعد الأكبر |
| 2857 | [`2857-list-count-greater-than-23.apl`](examples/2857-list-count-greater-than-23.apl) | نعد الأكبر |
| 2858 | [`2858-list-count-greater-than-24.apl`](examples/2858-list-count-greater-than-24.apl) | نعد الأكبر |
| 2859 | [`2859-list-keep-divisible-by-20.apl`](examples/2859-list-keep-divisible-by-20.apl) | نصفي القائمة |
| 2860 | [`2860-list-keep-divisible-by-21.apl`](examples/2860-list-keep-divisible-by-21.apl) | نصفي القائمة |
| 2861 | [`2861-list-keep-divisible-by-22.apl`](examples/2861-list-keep-divisible-by-22.apl) | نصفي القائمة |
| 2862 | [`2862-list-keep-divisible-by-23.apl`](examples/2862-list-keep-divisible-by-23.apl) | نصفي القائمة |
| 2863 | [`2863-list-keep-divisible-by-24.apl`](examples/2863-list-keep-divisible-by-24.apl) | نصفي القائمة |
| 2864 | [`2864-digit-sum-of-20-to-the-power-n.apl`](examples/2864-digit-sum-of-20-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2865 | [`2865-digit-sum-of-21-to-the-power-n.apl`](examples/2865-digit-sum-of-21-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2866 | [`2866-digit-sum-of-22-to-the-power-n.apl`](examples/2866-digit-sum-of-22-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2867 | [`2867-digit-sum-of-23-to-the-power-n.apl`](examples/2867-digit-sum-of-23-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2868 | [`2868-digit-sum-of-24-to-the-power-n.apl`](examples/2868-digit-sum-of-24-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2869 | [`2869-sum-of-remainders-mod-20-up-to-n.apl`](examples/2869-sum-of-remainders-mod-20-up-to-n.apl) | نجمع ي % 20 |
| 2870 | [`2870-sum-of-remainders-mod-21-up-to-n.apl`](examples/2870-sum-of-remainders-mod-21-up-to-n.apl) | نجمع ي % 21 |
| 2871 | [`2871-sum-of-remainders-mod-22-up-to-n.apl`](examples/2871-sum-of-remainders-mod-22-up-to-n.apl) | نجمع ي % 22 |
| 2872 | [`2872-sum-of-remainders-mod-23-up-to-n.apl`](examples/2872-sum-of-remainders-mod-23-up-to-n.apl) | نجمع ي % 23 |
| 2873 | [`2873-sum-of-remainders-mod-24-up-to-n.apl`](examples/2873-sum-of-remainders-mod-24-up-to-n.apl) | نجمع ي % 24 |
| 2874 | [`2874-count-numbers-below-hundred-with-digit-sum-20.apl`](examples/2874-count-numbers-below-hundred-with-digit-sum-20.apl) | نعد الأعداد |
| 2875 | [`2875-count-numbers-below-hundred-with-digit-sum-21.apl`](examples/2875-count-numbers-below-hundred-with-digit-sum-21.apl) | نعد الأعداد |
| 2876 | [`2876-count-numbers-below-hundred-with-digit-sum-22.apl`](examples/2876-count-numbers-below-hundred-with-digit-sum-22.apl) | نعد الأعداد |
| 2877 | [`2877-count-numbers-below-hundred-with-digit-sum-23.apl`](examples/2877-count-numbers-below-hundred-with-digit-sum-23.apl) | نعد الأعداد |
| 2878 | [`2878-count-numbers-below-hundred-with-digit-sum-24.apl`](examples/2878-count-numbers-below-hundred-with-digit-sum-24.apl) | نعد الأعداد |
| 2879 | [`2879-list-take-every-20th-item.apl`](examples/2879-list-take-every-20th-item.apl) | شريحة بخطوة |
| 2880 | [`2880-list-take-every-21th-item.apl`](examples/2880-list-take-every-21th-item.apl) | شريحة بخطوة |
| 2881 | [`2881-list-take-every-22th-item.apl`](examples/2881-list-take-every-22th-item.apl) | شريحة بخطوة |
| 2882 | [`2882-list-take-every-23th-item.apl`](examples/2882-list-take-every-23th-item.apl) | شريحة بخطوة |
| 2883 | [`2883-list-take-every-24th-item.apl`](examples/2883-list-take-every-24th-item.apl) | شريحة بخطوة |
| 2884 | [`2884-list-rotate-left-by-19.apl`](examples/2884-list-rotate-left-by-19.apl) | نقص ونلصق |
| 2885 | [`2885-list-rotate-left-by-20.apl`](examples/2885-list-rotate-left-by-20.apl) | نقص ونلصق |
| 2886 | [`2886-list-rotate-left-by-21.apl`](examples/2886-list-rotate-left-by-21.apl) | نقص ونلصق |
| 2887 | [`2887-list-rotate-left-by-22.apl`](examples/2887-list-rotate-left-by-22.apl) | نقص ونلصق |
| 2888 | [`2888-list-rotate-left-by-23.apl`](examples/2888-list-rotate-left-by-23.apl) | نقص ونلصق |
| 2889 | [`2889-nth-term-arithmetic-sequence-step-20.apl`](examples/2889-nth-term-arithmetic-sequence-step-20.apl) | أ + (ن-1)*20 |
| 2890 | [`2890-nth-term-arithmetic-sequence-step-21.apl`](examples/2890-nth-term-arithmetic-sequence-step-21.apl) | أ + (ن-1)*21 |
| 2891 | [`2891-nth-term-arithmetic-sequence-step-22.apl`](examples/2891-nth-term-arithmetic-sequence-step-22.apl) | أ + (ن-1)*22 |
| 2892 | [`2892-nth-term-arithmetic-sequence-step-23.apl`](examples/2892-nth-term-arithmetic-sequence-step-23.apl) | أ + (ن-1)*23 |
| 2893 | [`2893-nth-term-arithmetic-sequence-step-24.apl`](examples/2893-nth-term-arithmetic-sequence-step-24.apl) | أ + (ن-1)*24 |
| 2894 | [`2894-sum-of-powers-of-20-up-to-n.apl`](examples/2894-sum-of-powers-of-20-up-to-n.apl) | نجمع 20^ي |
| 2895 | [`2895-sum-of-powers-of-21-up-to-n.apl`](examples/2895-sum-of-powers-of-21-up-to-n.apl) | نجمع 21^ي |
| 2896 | [`2896-sum-of-powers-of-22-up-to-n.apl`](examples/2896-sum-of-powers-of-22-up-to-n.apl) | نجمع 22^ي |
| 2897 | [`2897-sum-of-powers-of-23-up-to-n.apl`](examples/2897-sum-of-powers-of-23-up-to-n.apl) | نجمع 23^ي |
| 2898 | [`2898-sum-of-powers-of-24-up-to-n.apl`](examples/2898-sum-of-powers-of-24-up-to-n.apl) | نجمع 24^ي |
| 2899 | [`2899-clamp-list-values-to-max-20.apl`](examples/2899-clamp-list-values-to-max-20.apl) | نقص ما يزيد |
| 2900 | [`2900-clamp-list-values-to-max-21.apl`](examples/2900-clamp-list-values-to-max-21.apl) | نقص ما يزيد |
| 2901 | [`2901-clamp-list-values-to-max-22.apl`](examples/2901-clamp-list-values-to-max-22.apl) | نقص ما يزيد |
| 2902 | [`2902-clamp-list-values-to-max-23.apl`](examples/2902-clamp-list-values-to-max-23.apl) | نقص ما يزيد |
| 2903 | [`2903-clamp-list-values-to-max-24.apl`](examples/2903-clamp-list-values-to-max-24.apl) | نقص ما يزيد |
| 2904 | [`2904-caesar-shift-by-19-lowercase.apl`](examples/2904-caesar-shift-by-19-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2905 | [`2905-caesar-shift-by-20-lowercase.apl`](examples/2905-caesar-shift-by-20-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2906 | [`2906-caesar-shift-by-21-lowercase.apl`](examples/2906-caesar-shift-by-21-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2907 | [`2907-caesar-shift-by-22-lowercase.apl`](examples/2907-caesar-shift-by-22-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2908 | [`2908-caesar-shift-by-23-lowercase.apl`](examples/2908-caesar-shift-by-23-lowercase.apl) | نزيح الأحرف الصغيرة |
| 2909 | [`2909-repeat-text-20-times-with-dash.apl`](examples/2909-repeat-text-20-times-with-dash.apl) | نكرر ونفصل |
| 2910 | [`2910-repeat-text-21-times-with-dash.apl`](examples/2910-repeat-text-21-times-with-dash.apl) | نكرر ونفصل |
| 2911 | [`2911-repeat-text-22-times-with-dash.apl`](examples/2911-repeat-text-22-times-with-dash.apl) | نكرر ونفصل |
| 2912 | [`2912-repeat-text-23-times-with-dash.apl`](examples/2912-repeat-text-23-times-with-dash.apl) | نكرر ونفصل |
| 2913 | [`2913-repeat-text-24-times-with-dash.apl`](examples/2913-repeat-text-24-times-with-dash.apl) | نكرر ونفصل |
| 2914 | [`2914-pad-number-with-zeros-to-width-20.apl`](examples/2914-pad-number-with-zeros-to-width-20.apl) | zfill |
| 2915 | [`2915-pad-number-with-zeros-to-width-21.apl`](examples/2915-pad-number-with-zeros-to-width-21.apl) | zfill |
| 2916 | [`2916-pad-number-with-zeros-to-width-22.apl`](examples/2916-pad-number-with-zeros-to-width-22.apl) | zfill |
| 2917 | [`2917-pad-number-with-zeros-to-width-23.apl`](examples/2917-pad-number-with-zeros-to-width-23.apl) | zfill |
| 2918 | [`2918-pad-number-with-zeros-to-width-24.apl`](examples/2918-pad-number-with-zeros-to-width-24.apl) | zfill |
| 2919 | [`2919-truncate-text-to-first-19-chars.apl`](examples/2919-truncate-text-to-first-19-chars.apl) | شريحة |
| 2920 | [`2920-truncate-text-to-first-20-chars.apl`](examples/2920-truncate-text-to-first-20-chars.apl) | شريحة |
| 2921 | [`2921-truncate-text-to-first-21-chars.apl`](examples/2921-truncate-text-to-first-21-chars.apl) | شريحة |
| 2922 | [`2922-truncate-text-to-first-22-chars.apl`](examples/2922-truncate-text-to-first-22-chars.apl) | شريحة |
| 2923 | [`2923-truncate-text-to-first-23-chars.apl`](examples/2923-truncate-text-to-first-23-chars.apl) | شريحة |
| 2924 | [`2924-count-triples-sum-to-24-small.apl`](examples/2924-count-triples-sum-to-24-small.apl) | أ<=ب<=ج موجبة |
| 2925 | [`2925-count-triples-sum-to-25-small.apl`](examples/2925-count-triples-sum-to-25-small.apl) | أ<=ب<=ج موجبة |
| 2926 | [`2926-count-triples-sum-to-26-small.apl`](examples/2926-count-triples-sum-to-26-small.apl) | أ<=ب<=ج موجبة |
| 2927 | [`2927-square-of-radius-times-22-area-approx.apl`](examples/2927-square-of-radius-times-22-area-approx.apl) | المساحة ≈ 22×نق²/7 |
| 2928 | [`2928-square-of-radius-times-3-area-approx.apl`](examples/2928-square-of-radius-times-3-area-approx.apl) | المساحة ≈ 3×نق²/7 |
| 2929 | [`2929-square-of-radius-times-6-area-approx.apl`](examples/2929-square-of-radius-times-6-area-approx.apl) | المساحة ≈ 6×نق²/7 |
| 2930 | [`2930-rectangle-area-scaled-by-2.apl`](examples/2930-rectangle-area-scaled-by-2.apl) | نكبر الضلعين |
| 2931 | [`2931-rectangle-area-scaled-by-3.apl`](examples/2931-rectangle-area-scaled-by-3.apl) | نكبر الضلعين |
| 2932 | [`2932-rectangle-area-scaled-by-4.apl`](examples/2932-rectangle-area-scaled-by-4.apl) | نكبر الضلعين |
| 2933 | [`2933-interior-angle-sum-of-polygon-plus-1.apl`](examples/2933-interior-angle-sum-of-polygon-plus-1.apl) | (ن-2)*180 |
| 2934 | [`2934-interior-angle-sum-of-polygon-plus-2.apl`](examples/2934-interior-angle-sum-of-polygon-plus-2.apl) | (ن-2)*180 |
| 2935 | [`2935-interior-angle-sum-of-polygon-plus-3.apl`](examples/2935-interior-angle-sum-of-polygon-plus-3.apl) | (ن-2)*180 |
| 2936 | [`2936-sum-of-ord-values-offset-1.apl`](examples/2936-sum-of-ord-values-offset-1.apl) | نجمع ord+1 |
| 2937 | [`2937-sum-of-ord-values-offset-2.apl`](examples/2937-sum-of-ord-values-offset-2.apl) | نجمع ord+2 |
| 2938 | [`2938-sum-of-ord-values-offset-3.apl`](examples/2938-sum-of-ord-values-offset-3.apl) | نجمع ord+3 |
| 2939 | [`2939-linear-recurrence-a-n-equals-2-times-previous-plus-one.apl`](examples/2939-linear-recurrence-a-n-equals-2-times-previous-plus-one.apl) | نكرر القاعدة |
| 2940 | [`2940-linear-recurrence-a-n-equals-3-times-previous-plus-one.apl`](examples/2940-linear-recurrence-a-n-equals-3-times-previous-plus-one.apl) | نكرر القاعدة |
| 2941 | [`2941-linear-recurrence-a-n-equals-4-times-previous-plus-one.apl`](examples/2941-linear-recurrence-a-n-equals-4-times-previous-plus-one.apl) | نكرر القاعدة |
| 2942 | [`2942-top-1-largest-items-sorted-desc.apl`](examples/2942-top-1-largest-items-sorted-desc.apl) | نرتب تنازليا ونقطع |
| 2943 | [`2943-top-2-largest-items-sorted-desc.apl`](examples/2943-top-2-largest-items-sorted-desc.apl) | نرتب تنازليا ونقطع |
| 2944 | [`2944-top-3-largest-items-sorted-desc.apl`](examples/2944-top-3-largest-items-sorted-desc.apl) | نرتب تنازليا ونقطع |
| 2945 | [`2945-bottom-1-smallest-items-sorted.apl`](examples/2945-bottom-1-smallest-items-sorted.apl) | نرتب ونقطع |
| 2946 | [`2946-bottom-2-smallest-items-sorted.apl`](examples/2946-bottom-2-smallest-items-sorted.apl) | نرتب ونقطع |
| 2947 | [`2947-bottom-3-smallest-items-sorted.apl`](examples/2947-bottom-3-smallest-items-sorted.apl) | نرتب ونقطع |
| 2948 | [`2948-shift-left-by-1-then-mask-byte.apl`](examples/2948-shift-left-by-1-then-mask-byte.apl) | نزيح ونقطع 8 بتات |
| 2949 | [`2949-shift-left-by-2-then-mask-byte.apl`](examples/2949-shift-left-by-2-then-mask-byte.apl) | نزيح ونقطع 8 بتات |
| 2950 | [`2950-shift-left-by-3-then-mask-byte.apl`](examples/2950-shift-left-by-3-then-mask-byte.apl) | نزيح ونقطع 8 بتات |
| 2951 | [`2951-shift-left-by-4-then-mask-byte.apl`](examples/2951-shift-left-by-4-then-mask-byte.apl) | نزيح ونقطع 8 بتات |
| 2952 | [`2952-shift-right-by-1-bits.apl`](examples/2952-shift-right-by-1-bits.apl) | نزيح لليمين |
| 2953 | [`2953-shift-right-by-2-bits.apl`](examples/2953-shift-right-by-2-bits.apl) | نزيح لليمين |
| 2954 | [`2954-shift-right-by-3-bits.apl`](examples/2954-shift-right-by-3-bits.apl) | نزيح لليمين |
| 2955 | [`2955-shift-right-by-4-bits.apl`](examples/2955-shift-right-by-4-bits.apl) | نزيح لليمين |
| 2956 | [`2956-max-sum-of-window-size-2.apl`](examples/2956-max-sum-of-window-size-2.apl) | نزلق النافذة |
| 2957 | [`2957-max-sum-of-window-size-3.apl`](examples/2957-max-sum-of-window-size-3.apl) | نزلق النافذة |
| 2958 | [`2958-max-sum-of-window-size-4.apl`](examples/2958-max-sum-of-window-size-4.apl) | نزلق النافذة |
| 2959 | [`2959-multiplication-table-row-of-3.apl`](examples/2959-multiplication-table-row-of-3.apl) | من 1 إلى ن |
| 2960 | [`2960-multiplication-table-row-of-6.apl`](examples/2960-multiplication-table-row-of-6.apl) | من 1 إلى ن |
| 2961 | [`2961-multiplication-table-row-of-9.apl`](examples/2961-multiplication-table-row-of-9.apl) | من 1 إلى ن |
| 2962 | [`2962-sum-of-squares-from-1-to-n.apl`](examples/2962-sum-of-squares-from-1-to-n.apl) | نجمع المربعات |
| 2963 | [`2963-sum-of-squares-from-2-to-n.apl`](examples/2963-sum-of-squares-from-2-to-n.apl) | نجمع المربعات |
| 2964 | [`2964-sum-of-squares-from-5-to-n.apl`](examples/2964-sum-of-squares-from-5-to-n.apl) | نجمع المربعات |
| 2965 | [`2965-sum-multiples-of-25-below-limit-v2.apl`](examples/2965-sum-multiples-of-25-below-limit-v2.apl) | نجمع مضاعفات 25 الأصغر من ن |
| 2966 | [`2966-sum-multiples-of-26-below-limit-v2.apl`](examples/2966-sum-multiples-of-26-below-limit-v2.apl) | نجمع مضاعفات 26 الأصغر من ن |
| 2967 | [`2967-sum-multiples-of-27-below-limit-v2.apl`](examples/2967-sum-multiples-of-27-below-limit-v2.apl) | نجمع مضاعفات 27 الأصغر من ن |
| 2968 | [`2968-sum-multiples-of-28-below-limit-v2.apl`](examples/2968-sum-multiples-of-28-below-limit-v2.apl) | نجمع مضاعفات 28 الأصغر من ن |
| 2969 | [`2969-sum-multiples-of-29-below-limit-v2.apl`](examples/2969-sum-multiples-of-29-below-limit-v2.apl) | نجمع مضاعفات 29 الأصغر من ن |
| 2970 | [`2970-count-multiples-of-25-up-to-limit.apl`](examples/2970-count-multiples-of-25-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2971 | [`2971-count-multiples-of-26-up-to-limit.apl`](examples/2971-count-multiples-of-26-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2972 | [`2972-count-multiples-of-27-up-to-limit.apl`](examples/2972-count-multiples-of-27-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2973 | [`2973-count-multiples-of-28-up-to-limit.apl`](examples/2973-count-multiples-of-28-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2974 | [`2974-count-multiples-of-29-up-to-limit.apl`](examples/2974-count-multiples-of-29-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 2975 | [`2975-list-multiply-each-by-25.apl`](examples/2975-list-multiply-each-by-25.apl) | نبني قائمة جديدة |
| 2976 | [`2976-list-multiply-each-by-26.apl`](examples/2976-list-multiply-each-by-26.apl) | نبني قائمة جديدة |
| 2977 | [`2977-list-multiply-each-by-27.apl`](examples/2977-list-multiply-each-by-27.apl) | نبني قائمة جديدة |
| 2978 | [`2978-list-multiply-each-by-28.apl`](examples/2978-list-multiply-each-by-28.apl) | نبني قائمة جديدة |
| 2979 | [`2979-list-multiply-each-by-29.apl`](examples/2979-list-multiply-each-by-29.apl) | نبني قائمة جديدة |
| 2980 | [`2980-list-add-25-to-each-item.apl`](examples/2980-list-add-25-to-each-item.apl) | نزيد كل عنصر |
| 2981 | [`2981-list-add-26-to-each-item.apl`](examples/2981-list-add-26-to-each-item.apl) | نزيد كل عنصر |
| 2982 | [`2982-list-add-27-to-each-item.apl`](examples/2982-list-add-27-to-each-item.apl) | نزيد كل عنصر |
| 2983 | [`2983-list-add-28-to-each-item.apl`](examples/2983-list-add-28-to-each-item.apl) | نزيد كل عنصر |
| 2984 | [`2984-list-add-29-to-each-item.apl`](examples/2984-list-add-29-to-each-item.apl) | نزيد كل عنصر |
| 2985 | [`2985-list-count-greater-than-25.apl`](examples/2985-list-count-greater-than-25.apl) | نعد الأكبر |
| 2986 | [`2986-list-count-greater-than-26.apl`](examples/2986-list-count-greater-than-26.apl) | نعد الأكبر |
| 2987 | [`2987-list-count-greater-than-27.apl`](examples/2987-list-count-greater-than-27.apl) | نعد الأكبر |
| 2988 | [`2988-list-count-greater-than-28.apl`](examples/2988-list-count-greater-than-28.apl) | نعد الأكبر |
| 2989 | [`2989-list-count-greater-than-29.apl`](examples/2989-list-count-greater-than-29.apl) | نعد الأكبر |
| 2990 | [`2990-list-keep-divisible-by-25.apl`](examples/2990-list-keep-divisible-by-25.apl) | نصفي القائمة |
| 2991 | [`2991-list-keep-divisible-by-26.apl`](examples/2991-list-keep-divisible-by-26.apl) | نصفي القائمة |
| 2992 | [`2992-list-keep-divisible-by-27.apl`](examples/2992-list-keep-divisible-by-27.apl) | نصفي القائمة |
| 2993 | [`2993-list-keep-divisible-by-28.apl`](examples/2993-list-keep-divisible-by-28.apl) | نصفي القائمة |
| 2994 | [`2994-list-keep-divisible-by-29.apl`](examples/2994-list-keep-divisible-by-29.apl) | نصفي القائمة |
| 2995 | [`2995-digit-sum-of-25-to-the-power-n.apl`](examples/2995-digit-sum-of-25-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2996 | [`2996-digit-sum-of-26-to-the-power-n.apl`](examples/2996-digit-sum-of-26-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2997 | [`2997-digit-sum-of-27-to-the-power-n.apl`](examples/2997-digit-sum-of-27-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2998 | [`2998-digit-sum-of-28-to-the-power-n.apl`](examples/2998-digit-sum-of-28-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 2999 | [`2999-digit-sum-of-29-to-the-power-n.apl`](examples/2999-digit-sum-of-29-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 3000 | [`3000-sum-of-remainders-mod-25-up-to-n.apl`](examples/3000-sum-of-remainders-mod-25-up-to-n.apl) | نجمع ي % 25 |
| 3001 | [`3001-sum-of-remainders-mod-26-up-to-n.apl`](examples/3001-sum-of-remainders-mod-26-up-to-n.apl) | نجمع ي % 26 |
| 3002 | [`3002-sum-of-remainders-mod-27-up-to-n.apl`](examples/3002-sum-of-remainders-mod-27-up-to-n.apl) | نجمع ي % 27 |
| 3003 | [`3003-sum-of-remainders-mod-28-up-to-n.apl`](examples/3003-sum-of-remainders-mod-28-up-to-n.apl) | نجمع ي % 28 |
| 3004 | [`3004-sum-of-remainders-mod-29-up-to-n.apl`](examples/3004-sum-of-remainders-mod-29-up-to-n.apl) | نجمع ي % 29 |
| 3005 | [`3005-count-numbers-below-hundred-with-digit-sum-25.apl`](examples/3005-count-numbers-below-hundred-with-digit-sum-25.apl) | نعد الأعداد |
| 3006 | [`3006-count-numbers-below-hundred-with-digit-sum-26.apl`](examples/3006-count-numbers-below-hundred-with-digit-sum-26.apl) | نعد الأعداد |
| 3007 | [`3007-count-numbers-below-hundred-with-digit-sum-27.apl`](examples/3007-count-numbers-below-hundred-with-digit-sum-27.apl) | نعد الأعداد |
| 3008 | [`3008-count-numbers-below-hundred-with-digit-sum-28.apl`](examples/3008-count-numbers-below-hundred-with-digit-sum-28.apl) | نعد الأعداد |
| 3009 | [`3009-count-numbers-below-hundred-with-digit-sum-29.apl`](examples/3009-count-numbers-below-hundred-with-digit-sum-29.apl) | نعد الأعداد |
| 3010 | [`3010-list-take-every-25th-item.apl`](examples/3010-list-take-every-25th-item.apl) | شريحة بخطوة |
| 3011 | [`3011-list-take-every-26th-item.apl`](examples/3011-list-take-every-26th-item.apl) | شريحة بخطوة |
| 3012 | [`3012-list-take-every-27th-item.apl`](examples/3012-list-take-every-27th-item.apl) | شريحة بخطوة |
| 3013 | [`3013-list-take-every-28th-item.apl`](examples/3013-list-take-every-28th-item.apl) | شريحة بخطوة |
| 3014 | [`3014-list-take-every-29th-item.apl`](examples/3014-list-take-every-29th-item.apl) | شريحة بخطوة |
| 3015 | [`3015-list-rotate-left-by-25.apl`](examples/3015-list-rotate-left-by-25.apl) | نقص ونلصق |
| 3016 | [`3016-list-rotate-left-by-26.apl`](examples/3016-list-rotate-left-by-26.apl) | نقص ونلصق |
| 3017 | [`3017-list-rotate-left-by-27.apl`](examples/3017-list-rotate-left-by-27.apl) | نقص ونلصق |
| 3018 | [`3018-list-rotate-left-by-28.apl`](examples/3018-list-rotate-left-by-28.apl) | نقص ونلصق |
| 3019 | [`3019-list-rotate-left-by-29.apl`](examples/3019-list-rotate-left-by-29.apl) | نقص ونلصق |
| 3020 | [`3020-nth-term-arithmetic-sequence-step-25.apl`](examples/3020-nth-term-arithmetic-sequence-step-25.apl) | أ + (ن-1)*25 |
| 3021 | [`3021-nth-term-arithmetic-sequence-step-26.apl`](examples/3021-nth-term-arithmetic-sequence-step-26.apl) | أ + (ن-1)*26 |
| 3022 | [`3022-nth-term-arithmetic-sequence-step-27.apl`](examples/3022-nth-term-arithmetic-sequence-step-27.apl) | أ + (ن-1)*27 |
| 3023 | [`3023-nth-term-arithmetic-sequence-step-28.apl`](examples/3023-nth-term-arithmetic-sequence-step-28.apl) | أ + (ن-1)*28 |
| 3024 | [`3024-nth-term-arithmetic-sequence-step-29.apl`](examples/3024-nth-term-arithmetic-sequence-step-29.apl) | أ + (ن-1)*29 |
| 3025 | [`3025-sum-of-powers-of-25-up-to-n.apl`](examples/3025-sum-of-powers-of-25-up-to-n.apl) | نجمع 25^ي |
| 3026 | [`3026-sum-of-powers-of-26-up-to-n.apl`](examples/3026-sum-of-powers-of-26-up-to-n.apl) | نجمع 26^ي |
| 3027 | [`3027-sum-of-powers-of-27-up-to-n.apl`](examples/3027-sum-of-powers-of-27-up-to-n.apl) | نجمع 27^ي |
| 3028 | [`3028-sum-of-powers-of-28-up-to-n.apl`](examples/3028-sum-of-powers-of-28-up-to-n.apl) | نجمع 28^ي |
| 3029 | [`3029-sum-of-powers-of-29-up-to-n.apl`](examples/3029-sum-of-powers-of-29-up-to-n.apl) | نجمع 29^ي |
| 3030 | [`3030-clamp-list-values-to-max-25.apl`](examples/3030-clamp-list-values-to-max-25.apl) | نقص ما يزيد |
| 3031 | [`3031-clamp-list-values-to-max-26.apl`](examples/3031-clamp-list-values-to-max-26.apl) | نقص ما يزيد |
| 3032 | [`3032-clamp-list-values-to-max-27.apl`](examples/3032-clamp-list-values-to-max-27.apl) | نقص ما يزيد |
| 3033 | [`3033-clamp-list-values-to-max-28.apl`](examples/3033-clamp-list-values-to-max-28.apl) | نقص ما يزيد |
| 3034 | [`3034-clamp-list-values-to-max-29.apl`](examples/3034-clamp-list-values-to-max-29.apl) | نقص ما يزيد |
| 3035 | [`3035-repeat-text-25-times-with-dash.apl`](examples/3035-repeat-text-25-times-with-dash.apl) | نكرر ونفصل |
| 3036 | [`3036-repeat-text-26-times-with-dash.apl`](examples/3036-repeat-text-26-times-with-dash.apl) | نكرر ونفصل |
| 3037 | [`3037-repeat-text-27-times-with-dash.apl`](examples/3037-repeat-text-27-times-with-dash.apl) | نكرر ونفصل |
| 3038 | [`3038-repeat-text-28-times-with-dash.apl`](examples/3038-repeat-text-28-times-with-dash.apl) | نكرر ونفصل |
| 3039 | [`3039-repeat-text-29-times-with-dash.apl`](examples/3039-repeat-text-29-times-with-dash.apl) | نكرر ونفصل |
| 3040 | [`3040-pad-number-with-zeros-to-width-25.apl`](examples/3040-pad-number-with-zeros-to-width-25.apl) | zfill |
| 3041 | [`3041-pad-number-with-zeros-to-width-26.apl`](examples/3041-pad-number-with-zeros-to-width-26.apl) | zfill |
| 3042 | [`3042-pad-number-with-zeros-to-width-27.apl`](examples/3042-pad-number-with-zeros-to-width-27.apl) | zfill |
| 3043 | [`3043-pad-number-with-zeros-to-width-28.apl`](examples/3043-pad-number-with-zeros-to-width-28.apl) | zfill |
| 3044 | [`3044-pad-number-with-zeros-to-width-29.apl`](examples/3044-pad-number-with-zeros-to-width-29.apl) | zfill |
| 3045 | [`3045-truncate-text-to-first-25-chars.apl`](examples/3045-truncate-text-to-first-25-chars.apl) | شريحة |
| 3046 | [`3046-truncate-text-to-first-26-chars.apl`](examples/3046-truncate-text-to-first-26-chars.apl) | شريحة |
| 3047 | [`3047-truncate-text-to-first-27-chars.apl`](examples/3047-truncate-text-to-first-27-chars.apl) | شريحة |
| 3048 | [`3048-truncate-text-to-first-28-chars.apl`](examples/3048-truncate-text-to-first-28-chars.apl) | شريحة |
| 3049 | [`3049-truncate-text-to-first-29-chars.apl`](examples/3049-truncate-text-to-first-29-chars.apl) | شريحة |
| 3050 | [`3050-sum-of-integers-from-10-to-n.apl`](examples/3050-sum-of-integers-from-10-to-n.apl) | نجمع بحلقة |
| 3051 | [`3051-sum-of-integers-from-11-to-n.apl`](examples/3051-sum-of-integers-from-11-to-n.apl) | نجمع بحلقة |
| 3052 | [`3052-sum-of-integers-from-12-to-n.apl`](examples/3052-sum-of-integers-from-12-to-n.apl) | نجمع بحلقة |
| 3053 | [`3053-sum-of-integers-from-13-to-n.apl`](examples/3053-sum-of-integers-from-13-to-n.apl) | نجمع بحلقة |
| 3054 | [`3054-sum-of-integers-from-14-to-n.apl`](examples/3054-sum-of-integers-from-14-to-n.apl) | نجمع بحلقة |
| 3055 | [`3055-count-numbers-with-exactly-10-divisors-below-limit.apl`](examples/3055-count-numbers-with-exactly-10-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3056 | [`3056-count-numbers-with-exactly-11-divisors-below-limit.apl`](examples/3056-count-numbers-with-exactly-11-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3057 | [`3057-count-numbers-with-exactly-12-divisors-below-limit.apl`](examples/3057-count-numbers-with-exactly-12-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3058 | [`3058-count-numbers-with-exactly-13-divisors-below-limit.apl`](examples/3058-count-numbers-with-exactly-13-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3059 | [`3059-count-numbers-with-exactly-14-divisors-below-limit.apl`](examples/3059-count-numbers-with-exactly-14-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3060 | [`3060-list-count-items-with-remainder-one-mod-10.apl`](examples/3060-list-count-items-with-remainder-one-mod-10.apl) | نعد |
| 3061 | [`3061-list-count-items-with-remainder-one-mod-11.apl`](examples/3061-list-count-items-with-remainder-one-mod-11.apl) | نعد |
| 3062 | [`3062-list-count-items-with-remainder-one-mod-12.apl`](examples/3062-list-count-items-with-remainder-one-mod-12.apl) | نعد |
| 3063 | [`3063-list-count-items-with-remainder-one-mod-13.apl`](examples/3063-list-count-items-with-remainder-one-mod-13.apl) | نعد |
| 3064 | [`3064-list-count-items-with-remainder-one-mod-14.apl`](examples/3064-list-count-items-with-remainder-one-mod-14.apl) | نعد |
| 3065 | [`3065-price-after-10-percent-discount-integer.apl`](examples/3065-price-after-10-percent-discount-integer.apl) | نطرح الخصم |
| 3066 | [`3066-price-after-11-percent-discount-integer.apl`](examples/3066-price-after-11-percent-discount-integer.apl) | نطرح الخصم |
| 3067 | [`3067-price-after-12-percent-discount-integer.apl`](examples/3067-price-after-12-percent-discount-integer.apl) | نطرح الخصم |
| 3068 | [`3068-price-after-13-percent-discount-integer.apl`](examples/3068-price-after-13-percent-discount-integer.apl) | نطرح الخصم |
| 3069 | [`3069-price-after-14-percent-discount-integer.apl`](examples/3069-price-after-14-percent-discount-integer.apl) | نطرح الخصم |
| 3070 | [`3070-price-with-10-percent-tax-integer.apl`](examples/3070-price-with-10-percent-tax-integer.apl) | نضيف الضريبة |
| 3071 | [`3071-price-with-11-percent-tax-integer.apl`](examples/3071-price-with-11-percent-tax-integer.apl) | نضيف الضريبة |
| 3072 | [`3072-price-with-12-percent-tax-integer.apl`](examples/3072-price-with-12-percent-tax-integer.apl) | نضيف الضريبة |
| 3073 | [`3073-price-with-13-percent-tax-integer.apl`](examples/3073-price-with-13-percent-tax-integer.apl) | نضيف الضريبة |
| 3074 | [`3074-price-with-14-percent-tax-integer.apl`](examples/3074-price-with-14-percent-tax-integer.apl) | نضيف الضريبة |
| 3075 | [`3075-split-bill-among-10-people-ceiling.apl`](examples/3075-split-bill-among-10-people-ceiling.apl) | نقرب لأعلى |
| 3076 | [`3076-split-bill-among-11-people-ceiling.apl`](examples/3076-split-bill-among-11-people-ceiling.apl) | نقرب لأعلى |
| 3077 | [`3077-split-bill-among-12-people-ceiling.apl`](examples/3077-split-bill-among-12-people-ceiling.apl) | نقرب لأعلى |
| 3078 | [`3078-split-bill-among-13-people-ceiling.apl`](examples/3078-split-bill-among-13-people-ceiling.apl) | نقرب لأعلى |
| 3079 | [`3079-split-bill-among-14-people-ceiling.apl`](examples/3079-split-bill-among-14-people-ceiling.apl) | نقرب لأعلى |
| 3080 | [`3080-minutes-to-hours-and-minutes-base-10.apl`](examples/3080-minutes-to-hours-and-minutes-base-10.apl) | نقسم على 10 |
| 3081 | [`3081-minutes-to-hours-and-minutes-base-11.apl`](examples/3081-minutes-to-hours-and-minutes-base-11.apl) | نقسم على 11 |
| 3082 | [`3082-minutes-to-hours-and-minutes-base-12.apl`](examples/3082-minutes-to-hours-and-minutes-base-12.apl) | نقسم على 12 |
| 3083 | [`3083-minutes-to-hours-and-minutes-base-13.apl`](examples/3083-minutes-to-hours-and-minutes-base-13.apl) | نقسم على 13 |
| 3084 | [`3084-minutes-to-hours-and-minutes-base-14.apl`](examples/3084-minutes-to-hours-and-minutes-base-14.apl) | نقسم على 14 |
| 3085 | [`3085-count-words-with-length-at-least-10.apl`](examples/3085-count-words-with-length-at-least-10.apl) | نعد الكلمات |
| 3086 | [`3086-count-words-with-length-at-least-11.apl`](examples/3086-count-words-with-length-at-least-11.apl) | نعد الكلمات |
| 3087 | [`3087-count-words-with-length-at-least-12.apl`](examples/3087-count-words-with-length-at-least-12.apl) | نعد الكلمات |
| 3088 | [`3088-count-words-with-length-at-least-13.apl`](examples/3088-count-words-with-length-at-least-13.apl) | نعد الكلمات |
| 3089 | [`3089-count-words-with-length-at-least-14.apl`](examples/3089-count-words-with-length-at-least-14.apl) | نعد الكلمات |
| 3090 | [`3090-square-of-radius-times-5-area-approx.apl`](examples/3090-square-of-radius-times-5-area-approx.apl) | المساحة ≈ 5×نق²/7 |
| 3091 | [`3091-square-of-radius-times-11-area-approx.apl`](examples/3091-square-of-radius-times-11-area-approx.apl) | المساحة ≈ 11×نق²/7 |
| 3092 | [`3092-square-of-radius-times-13-area-approx.apl`](examples/3092-square-of-radius-times-13-area-approx.apl) | المساحة ≈ 13×نق²/7 |
| 3093 | [`3093-rectangle-area-scaled-by-5.apl`](examples/3093-rectangle-area-scaled-by-5.apl) | نكبر الضلعين |
| 3094 | [`3094-rectangle-area-scaled-by-6.apl`](examples/3094-rectangle-area-scaled-by-6.apl) | نكبر الضلعين |
| 3095 | [`3095-rectangle-area-scaled-by-7.apl`](examples/3095-rectangle-area-scaled-by-7.apl) | نكبر الضلعين |
| 3096 | [`3096-interior-angle-sum-of-polygon-plus-4.apl`](examples/3096-interior-angle-sum-of-polygon-plus-4.apl) | (ن-2)*180 |
| 3097 | [`3097-interior-angle-sum-of-polygon-plus-5.apl`](examples/3097-interior-angle-sum-of-polygon-plus-5.apl) | (ن-2)*180 |
| 3098 | [`3098-interior-angle-sum-of-polygon-plus-6.apl`](examples/3098-interior-angle-sum-of-polygon-plus-6.apl) | (ن-2)*180 |
| 3099 | [`3099-sum-of-ord-values-offset-4.apl`](examples/3099-sum-of-ord-values-offset-4.apl) | نجمع ord+4 |
| 3100 | [`3100-sum-of-ord-values-offset-5.apl`](examples/3100-sum-of-ord-values-offset-5.apl) | نجمع ord+5 |
| 3101 | [`3101-sum-of-ord-values-offset-6.apl`](examples/3101-sum-of-ord-values-offset-6.apl) | نجمع ord+6 |
| 3102 | [`3102-linear-recurrence-a-n-equals-5-times-previous-plus-one.apl`](examples/3102-linear-recurrence-a-n-equals-5-times-previous-plus-one.apl) | نكرر القاعدة |
| 3103 | [`3103-linear-recurrence-a-n-equals-6-times-previous-plus-one.apl`](examples/3103-linear-recurrence-a-n-equals-6-times-previous-plus-one.apl) | نكرر القاعدة |
| 3104 | [`3104-linear-recurrence-a-n-equals-7-times-previous-plus-one.apl`](examples/3104-linear-recurrence-a-n-equals-7-times-previous-plus-one.apl) | نكرر القاعدة |
| 3105 | [`3105-top-4-largest-items-sorted-desc.apl`](examples/3105-top-4-largest-items-sorted-desc.apl) | نرتب تنازليا ونقطع |
| 3106 | [`3106-top-5-largest-items-sorted-desc.apl`](examples/3106-top-5-largest-items-sorted-desc.apl) | نرتب تنازليا ونقطع |
| 3107 | [`3107-bottom-4-smallest-items-sorted.apl`](examples/3107-bottom-4-smallest-items-sorted.apl) | نرتب ونقطع |
| 3108 | [`3108-bottom-5-smallest-items-sorted.apl`](examples/3108-bottom-5-smallest-items-sorted.apl) | نرتب ونقطع |
| 3109 | [`3109-shift-left-by-5-then-mask-byte.apl`](examples/3109-shift-left-by-5-then-mask-byte.apl) | نزيح ونقطع 8 بتات |
| 3110 | [`3110-shift-left-by-6-then-mask-byte.apl`](examples/3110-shift-left-by-6-then-mask-byte.apl) | نزيح ونقطع 8 بتات |
| 3111 | [`3111-shift-left-by-7-then-mask-byte.apl`](examples/3111-shift-left-by-7-then-mask-byte.apl) | نزيح ونقطع 8 بتات |
| 3112 | [`3112-shift-right-by-5-bits.apl`](examples/3112-shift-right-by-5-bits.apl) | نزيح لليمين |
| 3113 | [`3113-shift-right-by-6-bits.apl`](examples/3113-shift-right-by-6-bits.apl) | نزيح لليمين |
| 3114 | [`3114-shift-right-by-7-bits.apl`](examples/3114-shift-right-by-7-bits.apl) | نزيح لليمين |
| 3115 | [`3115-shift-right-by-8-bits.apl`](examples/3115-shift-right-by-8-bits.apl) | نزيح لليمين |
| 3116 | [`3116-multiplication-table-row-of-11.apl`](examples/3116-multiplication-table-row-of-11.apl) | من 1 إلى ن |
| 3117 | [`3117-multiplication-table-row-of-12.apl`](examples/3117-multiplication-table-row-of-12.apl) | من 1 إلى ن |
| 3118 | [`3118-multiplication-table-row-of-13.apl`](examples/3118-multiplication-table-row-of-13.apl) | من 1 إلى ن |
| 3119 | [`3119-sum-of-squares-from-3-to-n.apl`](examples/3119-sum-of-squares-from-3-to-n.apl) | نجمع المربعات |
| 3120 | [`3120-sum-of-squares-from-4-to-n.apl`](examples/3120-sum-of-squares-from-4-to-n.apl) | نجمع المربعات |
| 3121 | [`3121-sum-of-squares-from-6-to-n.apl`](examples/3121-sum-of-squares-from-6-to-n.apl) | نجمع المربعات |
| 3122 | [`3122-sum-multiples-of-30-below-limit-v2.apl`](examples/3122-sum-multiples-of-30-below-limit-v2.apl) | نجمع مضاعفات 30 الأصغر من ن |
| 3123 | [`3123-sum-multiples-of-31-below-limit-v2.apl`](examples/3123-sum-multiples-of-31-below-limit-v2.apl) | نجمع مضاعفات 31 الأصغر من ن |
| 3124 | [`3124-sum-multiples-of-32-below-limit-v2.apl`](examples/3124-sum-multiples-of-32-below-limit-v2.apl) | نجمع مضاعفات 32 الأصغر من ن |
| 3125 | [`3125-sum-multiples-of-33-below-limit-v2.apl`](examples/3125-sum-multiples-of-33-below-limit-v2.apl) | نجمع مضاعفات 33 الأصغر من ن |
| 3126 | [`3126-sum-multiples-of-34-below-limit-v2.apl`](examples/3126-sum-multiples-of-34-below-limit-v2.apl) | نجمع مضاعفات 34 الأصغر من ن |
| 3127 | [`3127-count-multiples-of-30-up-to-limit.apl`](examples/3127-count-multiples-of-30-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 3128 | [`3128-count-multiples-of-31-up-to-limit.apl`](examples/3128-count-multiples-of-31-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 3129 | [`3129-count-multiples-of-32-up-to-limit.apl`](examples/3129-count-multiples-of-32-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 3130 | [`3130-count-multiples-of-33-up-to-limit.apl`](examples/3130-count-multiples-of-33-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 3131 | [`3131-count-multiples-of-34-up-to-limit.apl`](examples/3131-count-multiples-of-34-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 3132 | [`3132-list-multiply-each-by-30.apl`](examples/3132-list-multiply-each-by-30.apl) | نبني قائمة جديدة |
| 3133 | [`3133-list-multiply-each-by-31.apl`](examples/3133-list-multiply-each-by-31.apl) | نبني قائمة جديدة |
| 3134 | [`3134-list-multiply-each-by-32.apl`](examples/3134-list-multiply-each-by-32.apl) | نبني قائمة جديدة |
| 3135 | [`3135-list-multiply-each-by-33.apl`](examples/3135-list-multiply-each-by-33.apl) | نبني قائمة جديدة |
| 3136 | [`3136-list-multiply-each-by-34.apl`](examples/3136-list-multiply-each-by-34.apl) | نبني قائمة جديدة |
| 3137 | [`3137-list-add-30-to-each-item.apl`](examples/3137-list-add-30-to-each-item.apl) | نزيد كل عنصر |
| 3138 | [`3138-list-add-31-to-each-item.apl`](examples/3138-list-add-31-to-each-item.apl) | نزيد كل عنصر |
| 3139 | [`3139-list-add-32-to-each-item.apl`](examples/3139-list-add-32-to-each-item.apl) | نزيد كل عنصر |
| 3140 | [`3140-list-add-33-to-each-item.apl`](examples/3140-list-add-33-to-each-item.apl) | نزيد كل عنصر |
| 3141 | [`3141-list-add-34-to-each-item.apl`](examples/3141-list-add-34-to-each-item.apl) | نزيد كل عنصر |
| 3142 | [`3142-list-count-greater-than-30.apl`](examples/3142-list-count-greater-than-30.apl) | نعد الأكبر |
| 3143 | [`3143-list-count-greater-than-31.apl`](examples/3143-list-count-greater-than-31.apl) | نعد الأكبر |
| 3144 | [`3144-list-count-greater-than-32.apl`](examples/3144-list-count-greater-than-32.apl) | نعد الأكبر |
| 3145 | [`3145-list-count-greater-than-33.apl`](examples/3145-list-count-greater-than-33.apl) | نعد الأكبر |
| 3146 | [`3146-list-count-greater-than-34.apl`](examples/3146-list-count-greater-than-34.apl) | نعد الأكبر |
| 3147 | [`3147-list-keep-divisible-by-30.apl`](examples/3147-list-keep-divisible-by-30.apl) | نصفي القائمة |
| 3148 | [`3148-list-keep-divisible-by-31.apl`](examples/3148-list-keep-divisible-by-31.apl) | نصفي القائمة |
| 3149 | [`3149-list-keep-divisible-by-32.apl`](examples/3149-list-keep-divisible-by-32.apl) | نصفي القائمة |
| 3150 | [`3150-list-keep-divisible-by-33.apl`](examples/3150-list-keep-divisible-by-33.apl) | نصفي القائمة |
| 3151 | [`3151-list-keep-divisible-by-34.apl`](examples/3151-list-keep-divisible-by-34.apl) | نصفي القائمة |
| 3152 | [`3152-digit-sum-of-30-to-the-power-n.apl`](examples/3152-digit-sum-of-30-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 3153 | [`3153-digit-sum-of-31-to-the-power-n.apl`](examples/3153-digit-sum-of-31-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 3154 | [`3154-digit-sum-of-32-to-the-power-n.apl`](examples/3154-digit-sum-of-32-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 3155 | [`3155-digit-sum-of-33-to-the-power-n.apl`](examples/3155-digit-sum-of-33-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 3156 | [`3156-digit-sum-of-34-to-the-power-n.apl`](examples/3156-digit-sum-of-34-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 3157 | [`3157-sum-of-remainders-mod-30-up-to-n.apl`](examples/3157-sum-of-remainders-mod-30-up-to-n.apl) | نجمع ي % 30 |
| 3158 | [`3158-sum-of-remainders-mod-31-up-to-n.apl`](examples/3158-sum-of-remainders-mod-31-up-to-n.apl) | نجمع ي % 31 |
| 3159 | [`3159-sum-of-remainders-mod-32-up-to-n.apl`](examples/3159-sum-of-remainders-mod-32-up-to-n.apl) | نجمع ي % 32 |
| 3160 | [`3160-sum-of-remainders-mod-33-up-to-n.apl`](examples/3160-sum-of-remainders-mod-33-up-to-n.apl) | نجمع ي % 33 |
| 3161 | [`3161-sum-of-remainders-mod-34-up-to-n.apl`](examples/3161-sum-of-remainders-mod-34-up-to-n.apl) | نجمع ي % 34 |
| 3162 | [`3162-count-numbers-below-hundred-with-digit-sum-30.apl`](examples/3162-count-numbers-below-hundred-with-digit-sum-30.apl) | نعد الأعداد |
| 3163 | [`3163-count-numbers-below-hundred-with-digit-sum-31.apl`](examples/3163-count-numbers-below-hundred-with-digit-sum-31.apl) | نعد الأعداد |
| 3164 | [`3164-count-numbers-below-hundred-with-digit-sum-32.apl`](examples/3164-count-numbers-below-hundred-with-digit-sum-32.apl) | نعد الأعداد |
| 3165 | [`3165-count-numbers-below-hundred-with-digit-sum-33.apl`](examples/3165-count-numbers-below-hundred-with-digit-sum-33.apl) | نعد الأعداد |
| 3166 | [`3166-count-numbers-below-hundred-with-digit-sum-34.apl`](examples/3166-count-numbers-below-hundred-with-digit-sum-34.apl) | نعد الأعداد |
| 3167 | [`3167-list-take-every-30th-item.apl`](examples/3167-list-take-every-30th-item.apl) | شريحة بخطوة |
| 3168 | [`3168-list-take-every-31th-item.apl`](examples/3168-list-take-every-31th-item.apl) | شريحة بخطوة |
| 3169 | [`3169-list-take-every-32th-item.apl`](examples/3169-list-take-every-32th-item.apl) | شريحة بخطوة |
| 3170 | [`3170-list-take-every-33th-item.apl`](examples/3170-list-take-every-33th-item.apl) | شريحة بخطوة |
| 3171 | [`3171-list-take-every-34th-item.apl`](examples/3171-list-take-every-34th-item.apl) | شريحة بخطوة |
| 3172 | [`3172-list-rotate-left-by-30.apl`](examples/3172-list-rotate-left-by-30.apl) | نقص ونلصق |
| 3173 | [`3173-list-rotate-left-by-31.apl`](examples/3173-list-rotate-left-by-31.apl) | نقص ونلصق |
| 3174 | [`3174-list-rotate-left-by-32.apl`](examples/3174-list-rotate-left-by-32.apl) | نقص ونلصق |
| 3175 | [`3175-list-rotate-left-by-33.apl`](examples/3175-list-rotate-left-by-33.apl) | نقص ونلصق |
| 3176 | [`3176-list-rotate-left-by-34.apl`](examples/3176-list-rotate-left-by-34.apl) | نقص ونلصق |
| 3177 | [`3177-nth-term-arithmetic-sequence-step-30.apl`](examples/3177-nth-term-arithmetic-sequence-step-30.apl) | أ + (ن-1)*30 |
| 3178 | [`3178-nth-term-arithmetic-sequence-step-31.apl`](examples/3178-nth-term-arithmetic-sequence-step-31.apl) | أ + (ن-1)*31 |
| 3179 | [`3179-nth-term-arithmetic-sequence-step-32.apl`](examples/3179-nth-term-arithmetic-sequence-step-32.apl) | أ + (ن-1)*32 |
| 3180 | [`3180-nth-term-arithmetic-sequence-step-33.apl`](examples/3180-nth-term-arithmetic-sequence-step-33.apl) | أ + (ن-1)*33 |
| 3181 | [`3181-nth-term-arithmetic-sequence-step-34.apl`](examples/3181-nth-term-arithmetic-sequence-step-34.apl) | أ + (ن-1)*34 |
| 3182 | [`3182-sum-of-powers-of-30-up-to-n.apl`](examples/3182-sum-of-powers-of-30-up-to-n.apl) | نجمع 30^ي |
| 3183 | [`3183-sum-of-powers-of-31-up-to-n.apl`](examples/3183-sum-of-powers-of-31-up-to-n.apl) | نجمع 31^ي |
| 3184 | [`3184-sum-of-powers-of-32-up-to-n.apl`](examples/3184-sum-of-powers-of-32-up-to-n.apl) | نجمع 32^ي |
| 3185 | [`3185-sum-of-powers-of-33-up-to-n.apl`](examples/3185-sum-of-powers-of-33-up-to-n.apl) | نجمع 33^ي |
| 3186 | [`3186-sum-of-powers-of-34-up-to-n.apl`](examples/3186-sum-of-powers-of-34-up-to-n.apl) | نجمع 34^ي |
| 3187 | [`3187-clamp-list-values-to-max-30.apl`](examples/3187-clamp-list-values-to-max-30.apl) | نقص ما يزيد |
| 3188 | [`3188-clamp-list-values-to-max-31.apl`](examples/3188-clamp-list-values-to-max-31.apl) | نقص ما يزيد |
| 3189 | [`3189-clamp-list-values-to-max-32.apl`](examples/3189-clamp-list-values-to-max-32.apl) | نقص ما يزيد |
| 3190 | [`3190-clamp-list-values-to-max-33.apl`](examples/3190-clamp-list-values-to-max-33.apl) | نقص ما يزيد |
| 3191 | [`3191-clamp-list-values-to-max-34.apl`](examples/3191-clamp-list-values-to-max-34.apl) | نقص ما يزيد |
| 3192 | [`3192-repeat-text-30-times-with-dash.apl`](examples/3192-repeat-text-30-times-with-dash.apl) | نكرر ونفصل |
| 3193 | [`3193-repeat-text-31-times-with-dash.apl`](examples/3193-repeat-text-31-times-with-dash.apl) | نكرر ونفصل |
| 3194 | [`3194-repeat-text-32-times-with-dash.apl`](examples/3194-repeat-text-32-times-with-dash.apl) | نكرر ونفصل |
| 3195 | [`3195-repeat-text-33-times-with-dash.apl`](examples/3195-repeat-text-33-times-with-dash.apl) | نكرر ونفصل |
| 3196 | [`3196-repeat-text-34-times-with-dash.apl`](examples/3196-repeat-text-34-times-with-dash.apl) | نكرر ونفصل |
| 3197 | [`3197-pad-number-with-zeros-to-width-30.apl`](examples/3197-pad-number-with-zeros-to-width-30.apl) | zfill |
| 3198 | [`3198-pad-number-with-zeros-to-width-31.apl`](examples/3198-pad-number-with-zeros-to-width-31.apl) | zfill |
| 3199 | [`3199-pad-number-with-zeros-to-width-32.apl`](examples/3199-pad-number-with-zeros-to-width-32.apl) | zfill |
| 3200 | [`3200-pad-number-with-zeros-to-width-33.apl`](examples/3200-pad-number-with-zeros-to-width-33.apl) | zfill |
| 3201 | [`3201-pad-number-with-zeros-to-width-34.apl`](examples/3201-pad-number-with-zeros-to-width-34.apl) | zfill |
| 3202 | [`3202-truncate-text-to-first-30-chars.apl`](examples/3202-truncate-text-to-first-30-chars.apl) | شريحة |
| 3203 | [`3203-truncate-text-to-first-31-chars.apl`](examples/3203-truncate-text-to-first-31-chars.apl) | شريحة |
| 3204 | [`3204-truncate-text-to-first-32-chars.apl`](examples/3204-truncate-text-to-first-32-chars.apl) | شريحة |
| 3205 | [`3205-truncate-text-to-first-33-chars.apl`](examples/3205-truncate-text-to-first-33-chars.apl) | شريحة |
| 3206 | [`3206-truncate-text-to-first-34-chars.apl`](examples/3206-truncate-text-to-first-34-chars.apl) | شريحة |
| 3207 | [`3207-sum-of-integers-from-15-to-n.apl`](examples/3207-sum-of-integers-from-15-to-n.apl) | نجمع بحلقة |
| 3208 | [`3208-sum-of-integers-from-16-to-n.apl`](examples/3208-sum-of-integers-from-16-to-n.apl) | نجمع بحلقة |
| 3209 | [`3209-sum-of-integers-from-17-to-n.apl`](examples/3209-sum-of-integers-from-17-to-n.apl) | نجمع بحلقة |
| 3210 | [`3210-sum-of-integers-from-18-to-n.apl`](examples/3210-sum-of-integers-from-18-to-n.apl) | نجمع بحلقة |
| 3211 | [`3211-sum-of-integers-from-19-to-n.apl`](examples/3211-sum-of-integers-from-19-to-n.apl) | نجمع بحلقة |
| 3212 | [`3212-count-numbers-with-exactly-15-divisors-below-limit.apl`](examples/3212-count-numbers-with-exactly-15-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3213 | [`3213-count-numbers-with-exactly-16-divisors-below-limit.apl`](examples/3213-count-numbers-with-exactly-16-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3214 | [`3214-count-numbers-with-exactly-17-divisors-below-limit.apl`](examples/3214-count-numbers-with-exactly-17-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3215 | [`3215-count-numbers-with-exactly-18-divisors-below-limit.apl`](examples/3215-count-numbers-with-exactly-18-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3216 | [`3216-count-numbers-with-exactly-19-divisors-below-limit.apl`](examples/3216-count-numbers-with-exactly-19-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3217 | [`3217-list-count-items-with-remainder-one-mod-15.apl`](examples/3217-list-count-items-with-remainder-one-mod-15.apl) | نعد |
| 3218 | [`3218-list-count-items-with-remainder-one-mod-16.apl`](examples/3218-list-count-items-with-remainder-one-mod-16.apl) | نعد |
| 3219 | [`3219-list-count-items-with-remainder-one-mod-17.apl`](examples/3219-list-count-items-with-remainder-one-mod-17.apl) | نعد |
| 3220 | [`3220-list-count-items-with-remainder-one-mod-18.apl`](examples/3220-list-count-items-with-remainder-one-mod-18.apl) | نعد |
| 3221 | [`3221-list-count-items-with-remainder-one-mod-19.apl`](examples/3221-list-count-items-with-remainder-one-mod-19.apl) | نعد |
| 3222 | [`3222-price-after-15-percent-discount-integer.apl`](examples/3222-price-after-15-percent-discount-integer.apl) | نطرح الخصم |
| 3223 | [`3223-price-after-16-percent-discount-integer.apl`](examples/3223-price-after-16-percent-discount-integer.apl) | نطرح الخصم |
| 3224 | [`3224-price-after-17-percent-discount-integer.apl`](examples/3224-price-after-17-percent-discount-integer.apl) | نطرح الخصم |
| 3225 | [`3225-price-after-18-percent-discount-integer.apl`](examples/3225-price-after-18-percent-discount-integer.apl) | نطرح الخصم |
| 3226 | [`3226-price-after-19-percent-discount-integer.apl`](examples/3226-price-after-19-percent-discount-integer.apl) | نطرح الخصم |
| 3227 | [`3227-price-with-15-percent-tax-integer.apl`](examples/3227-price-with-15-percent-tax-integer.apl) | نضيف الضريبة |
| 3228 | [`3228-price-with-16-percent-tax-integer.apl`](examples/3228-price-with-16-percent-tax-integer.apl) | نضيف الضريبة |
| 3229 | [`3229-price-with-17-percent-tax-integer.apl`](examples/3229-price-with-17-percent-tax-integer.apl) | نضيف الضريبة |
| 3230 | [`3230-price-with-18-percent-tax-integer.apl`](examples/3230-price-with-18-percent-tax-integer.apl) | نضيف الضريبة |
| 3231 | [`3231-price-with-19-percent-tax-integer.apl`](examples/3231-price-with-19-percent-tax-integer.apl) | نضيف الضريبة |
| 3232 | [`3232-split-bill-among-15-people-ceiling.apl`](examples/3232-split-bill-among-15-people-ceiling.apl) | نقرب لأعلى |
| 3233 | [`3233-split-bill-among-16-people-ceiling.apl`](examples/3233-split-bill-among-16-people-ceiling.apl) | نقرب لأعلى |
| 3234 | [`3234-split-bill-among-17-people-ceiling.apl`](examples/3234-split-bill-among-17-people-ceiling.apl) | نقرب لأعلى |
| 3235 | [`3235-split-bill-among-18-people-ceiling.apl`](examples/3235-split-bill-among-18-people-ceiling.apl) | نقرب لأعلى |
| 3236 | [`3236-split-bill-among-19-people-ceiling.apl`](examples/3236-split-bill-among-19-people-ceiling.apl) | نقرب لأعلى |
| 3237 | [`3237-minutes-to-hours-and-minutes-base-15.apl`](examples/3237-minutes-to-hours-and-minutes-base-15.apl) | نقسم على 15 |
| 3238 | [`3238-minutes-to-hours-and-minutes-base-16.apl`](examples/3238-minutes-to-hours-and-minutes-base-16.apl) | نقسم على 16 |
| 3239 | [`3239-minutes-to-hours-and-minutes-base-17.apl`](examples/3239-minutes-to-hours-and-minutes-base-17.apl) | نقسم على 17 |
| 3240 | [`3240-minutes-to-hours-and-minutes-base-18.apl`](examples/3240-minutes-to-hours-and-minutes-base-18.apl) | نقسم على 18 |
| 3241 | [`3241-minutes-to-hours-and-minutes-base-19.apl`](examples/3241-minutes-to-hours-and-minutes-base-19.apl) | نقسم على 19 |
| 3242 | [`3242-count-words-with-length-at-least-15.apl`](examples/3242-count-words-with-length-at-least-15.apl) | نعد الكلمات |
| 3243 | [`3243-count-words-with-length-at-least-16.apl`](examples/3243-count-words-with-length-at-least-16.apl) | نعد الكلمات |
| 3244 | [`3244-count-words-with-length-at-least-17.apl`](examples/3244-count-words-with-length-at-least-17.apl) | نعد الكلمات |
| 3245 | [`3245-count-words-with-length-at-least-18.apl`](examples/3245-count-words-with-length-at-least-18.apl) | نعد الكلمات |
| 3246 | [`3246-count-words-with-length-at-least-19.apl`](examples/3246-count-words-with-length-at-least-19.apl) | نعد الكلمات |
| 3247 | [`3247-square-of-radius-times-17-area-approx.apl`](examples/3247-square-of-radius-times-17-area-approx.apl) | المساحة ≈ 17×نق²/7 |
| 3248 | [`3248-square-of-radius-times-19-area-approx.apl`](examples/3248-square-of-radius-times-19-area-approx.apl) | المساحة ≈ 19×نق²/7 |
| 3249 | [`3249-square-of-radius-times-23-area-approx.apl`](examples/3249-square-of-radius-times-23-area-approx.apl) | المساحة ≈ 23×نق²/7 |
| 3250 | [`3250-rectangle-area-scaled-by-8.apl`](examples/3250-rectangle-area-scaled-by-8.apl) | نكبر الضلعين |
| 3251 | [`3251-rectangle-area-scaled-by-9.apl`](examples/3251-rectangle-area-scaled-by-9.apl) | نكبر الضلعين |
| 3252 | [`3252-rectangle-area-scaled-by-10.apl`](examples/3252-rectangle-area-scaled-by-10.apl) | نكبر الضلعين |
| 3253 | [`3253-interior-angle-sum-of-polygon-plus-7.apl`](examples/3253-interior-angle-sum-of-polygon-plus-7.apl) | (ن-2)*180 |
| 3254 | [`3254-interior-angle-sum-of-polygon-plus-8.apl`](examples/3254-interior-angle-sum-of-polygon-plus-8.apl) | (ن-2)*180 |
| 3255 | [`3255-interior-angle-sum-of-polygon-plus-9.apl`](examples/3255-interior-angle-sum-of-polygon-plus-9.apl) | (ن-2)*180 |
| 3256 | [`3256-interior-angle-sum-of-polygon-plus-10.apl`](examples/3256-interior-angle-sum-of-polygon-plus-10.apl) | (ن-2)*180 |
| 3257 | [`3257-sum-of-ord-values-offset-7.apl`](examples/3257-sum-of-ord-values-offset-7.apl) | نجمع ord+7 |
| 3258 | [`3258-sum-of-ord-values-offset-8.apl`](examples/3258-sum-of-ord-values-offset-8.apl) | نجمع ord+8 |
| 3259 | [`3259-sum-of-ord-values-offset-9.apl`](examples/3259-sum-of-ord-values-offset-9.apl) | نجمع ord+9 |
| 3260 | [`3260-linear-recurrence-a-n-equals-8-times-previous-plus-one.apl`](examples/3260-linear-recurrence-a-n-equals-8-times-previous-plus-one.apl) | نكرر القاعدة |
| 3261 | [`3261-linear-recurrence-a-n-equals-9-times-previous-plus-one.apl`](examples/3261-linear-recurrence-a-n-equals-9-times-previous-plus-one.apl) | نكرر القاعدة |
| 3262 | [`3262-linear-recurrence-a-n-equals-10-times-previous-plus-one.apl`](examples/3262-linear-recurrence-a-n-equals-10-times-previous-plus-one.apl) | نكرر القاعدة |
| 3263 | [`3263-top-6-largest-items-sorted-desc.apl`](examples/3263-top-6-largest-items-sorted-desc.apl) | نرتب تنازليا ونقطع |
| 3264 | [`3264-bottom-6-smallest-items-sorted.apl`](examples/3264-bottom-6-smallest-items-sorted.apl) | نرتب ونقطع |
| 3265 | [`3265-multiplication-table-row-of-14.apl`](examples/3265-multiplication-table-row-of-14.apl) | من 1 إلى ن |
| 3266 | [`3266-multiplication-table-row-of-15.apl`](examples/3266-multiplication-table-row-of-15.apl) | من 1 إلى ن |
| 3267 | [`3267-multiplication-table-row-of-16.apl`](examples/3267-multiplication-table-row-of-16.apl) | من 1 إلى ن |
| 3268 | [`3268-sum-of-squares-from-7-to-n.apl`](examples/3268-sum-of-squares-from-7-to-n.apl) | نجمع المربعات |
| 3269 | [`3269-sum-of-squares-from-8-to-n.apl`](examples/3269-sum-of-squares-from-8-to-n.apl) | نجمع المربعات |
| 3270 | [`3270-sum-of-squares-from-9-to-n.apl`](examples/3270-sum-of-squares-from-9-to-n.apl) | نجمع المربعات |
| 3271 | [`3271-sum-multiples-of-35-below-limit-v2.apl`](examples/3271-sum-multiples-of-35-below-limit-v2.apl) | نجمع مضاعفات 35 الأصغر من ن |
| 3272 | [`3272-sum-multiples-of-36-below-limit-v2.apl`](examples/3272-sum-multiples-of-36-below-limit-v2.apl) | نجمع مضاعفات 36 الأصغر من ن |
| 3273 | [`3273-sum-multiples-of-37-below-limit-v2.apl`](examples/3273-sum-multiples-of-37-below-limit-v2.apl) | نجمع مضاعفات 37 الأصغر من ن |
| 3274 | [`3274-sum-multiples-of-38-below-limit-v2.apl`](examples/3274-sum-multiples-of-38-below-limit-v2.apl) | نجمع مضاعفات 38 الأصغر من ن |
| 3275 | [`3275-sum-multiples-of-39-below-limit-v2.apl`](examples/3275-sum-multiples-of-39-below-limit-v2.apl) | نجمع مضاعفات 39 الأصغر من ن |
| 3276 | [`3276-count-multiples-of-35-up-to-limit.apl`](examples/3276-count-multiples-of-35-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 3277 | [`3277-count-multiples-of-36-up-to-limit.apl`](examples/3277-count-multiples-of-36-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 3278 | [`3278-count-multiples-of-37-up-to-limit.apl`](examples/3278-count-multiples-of-37-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 3279 | [`3279-count-multiples-of-38-up-to-limit.apl`](examples/3279-count-multiples-of-38-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 3280 | [`3280-count-multiples-of-39-up-to-limit.apl`](examples/3280-count-multiples-of-39-up-to-limit.apl) | نعد المضاعفات من 1 إلى ن |
| 3281 | [`3281-list-multiply-each-by-35.apl`](examples/3281-list-multiply-each-by-35.apl) | نبني قائمة جديدة |
| 3282 | [`3282-list-multiply-each-by-36.apl`](examples/3282-list-multiply-each-by-36.apl) | نبني قائمة جديدة |
| 3283 | [`3283-list-multiply-each-by-37.apl`](examples/3283-list-multiply-each-by-37.apl) | نبني قائمة جديدة |
| 3284 | [`3284-list-multiply-each-by-38.apl`](examples/3284-list-multiply-each-by-38.apl) | نبني قائمة جديدة |
| 3285 | [`3285-list-multiply-each-by-39.apl`](examples/3285-list-multiply-each-by-39.apl) | نبني قائمة جديدة |
| 3286 | [`3286-list-add-35-to-each-item.apl`](examples/3286-list-add-35-to-each-item.apl) | نزيد كل عنصر |
| 3287 | [`3287-list-add-36-to-each-item.apl`](examples/3287-list-add-36-to-each-item.apl) | نزيد كل عنصر |
| 3288 | [`3288-list-add-37-to-each-item.apl`](examples/3288-list-add-37-to-each-item.apl) | نزيد كل عنصر |
| 3289 | [`3289-list-add-38-to-each-item.apl`](examples/3289-list-add-38-to-each-item.apl) | نزيد كل عنصر |
| 3290 | [`3290-list-add-39-to-each-item.apl`](examples/3290-list-add-39-to-each-item.apl) | نزيد كل عنصر |
| 3291 | [`3291-list-count-greater-than-35.apl`](examples/3291-list-count-greater-than-35.apl) | نعد الأكبر |
| 3292 | [`3292-list-count-greater-than-36.apl`](examples/3292-list-count-greater-than-36.apl) | نعد الأكبر |
| 3293 | [`3293-list-count-greater-than-37.apl`](examples/3293-list-count-greater-than-37.apl) | نعد الأكبر |
| 3294 | [`3294-list-count-greater-than-38.apl`](examples/3294-list-count-greater-than-38.apl) | نعد الأكبر |
| 3295 | [`3295-list-count-greater-than-39.apl`](examples/3295-list-count-greater-than-39.apl) | نعد الأكبر |
| 3296 | [`3296-list-keep-divisible-by-35.apl`](examples/3296-list-keep-divisible-by-35.apl) | نصفي القائمة |
| 3297 | [`3297-list-keep-divisible-by-36.apl`](examples/3297-list-keep-divisible-by-36.apl) | نصفي القائمة |
| 3298 | [`3298-list-keep-divisible-by-37.apl`](examples/3298-list-keep-divisible-by-37.apl) | نصفي القائمة |
| 3299 | [`3299-list-keep-divisible-by-38.apl`](examples/3299-list-keep-divisible-by-38.apl) | نصفي القائمة |
| 3300 | [`3300-list-keep-divisible-by-39.apl`](examples/3300-list-keep-divisible-by-39.apl) | نصفي القائمة |
| 3301 | [`3301-digit-sum-of-35-to-the-power-n.apl`](examples/3301-digit-sum-of-35-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 3302 | [`3302-digit-sum-of-36-to-the-power-n.apl`](examples/3302-digit-sum-of-36-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 3303 | [`3303-digit-sum-of-37-to-the-power-n.apl`](examples/3303-digit-sum-of-37-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 3304 | [`3304-digit-sum-of-38-to-the-power-n.apl`](examples/3304-digit-sum-of-38-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 3305 | [`3305-digit-sum-of-39-to-the-power-n.apl`](examples/3305-digit-sum-of-39-to-the-power-n.apl) | نحسب القوة ثم نجمع الأرقام |
| 3306 | [`3306-sum-of-remainders-mod-35-up-to-n.apl`](examples/3306-sum-of-remainders-mod-35-up-to-n.apl) | نجمع ي % 35 |
| 3307 | [`3307-sum-of-remainders-mod-36-up-to-n.apl`](examples/3307-sum-of-remainders-mod-36-up-to-n.apl) | نجمع ي % 36 |
| 3308 | [`3308-sum-of-remainders-mod-37-up-to-n.apl`](examples/3308-sum-of-remainders-mod-37-up-to-n.apl) | نجمع ي % 37 |
| 3309 | [`3309-sum-of-remainders-mod-38-up-to-n.apl`](examples/3309-sum-of-remainders-mod-38-up-to-n.apl) | نجمع ي % 38 |
| 3310 | [`3310-sum-of-remainders-mod-39-up-to-n.apl`](examples/3310-sum-of-remainders-mod-39-up-to-n.apl) | نجمع ي % 39 |
| 3311 | [`3311-count-numbers-below-hundred-with-digit-sum-35.apl`](examples/3311-count-numbers-below-hundred-with-digit-sum-35.apl) | نعد الأعداد |
| 3312 | [`3312-count-numbers-below-hundred-with-digit-sum-36.apl`](examples/3312-count-numbers-below-hundred-with-digit-sum-36.apl) | نعد الأعداد |
| 3313 | [`3313-count-numbers-below-hundred-with-digit-sum-37.apl`](examples/3313-count-numbers-below-hundred-with-digit-sum-37.apl) | نعد الأعداد |
| 3314 | [`3314-count-numbers-below-hundred-with-digit-sum-38.apl`](examples/3314-count-numbers-below-hundred-with-digit-sum-38.apl) | نعد الأعداد |
| 3315 | [`3315-count-numbers-below-hundred-with-digit-sum-39.apl`](examples/3315-count-numbers-below-hundred-with-digit-sum-39.apl) | نعد الأعداد |
| 3316 | [`3316-list-take-every-35th-item.apl`](examples/3316-list-take-every-35th-item.apl) | شريحة بخطوة |
| 3317 | [`3317-list-take-every-36th-item.apl`](examples/3317-list-take-every-36th-item.apl) | شريحة بخطوة |
| 3318 | [`3318-list-take-every-37th-item.apl`](examples/3318-list-take-every-37th-item.apl) | شريحة بخطوة |
| 3319 | [`3319-list-take-every-38th-item.apl`](examples/3319-list-take-every-38th-item.apl) | شريحة بخطوة |
| 3320 | [`3320-list-take-every-39th-item.apl`](examples/3320-list-take-every-39th-item.apl) | شريحة بخطوة |
| 3321 | [`3321-list-rotate-left-by-35.apl`](examples/3321-list-rotate-left-by-35.apl) | نقص ونلصق |
| 3322 | [`3322-list-rotate-left-by-36.apl`](examples/3322-list-rotate-left-by-36.apl) | نقص ونلصق |
| 3323 | [`3323-list-rotate-left-by-37.apl`](examples/3323-list-rotate-left-by-37.apl) | نقص ونلصق |
| 3324 | [`3324-list-rotate-left-by-38.apl`](examples/3324-list-rotate-left-by-38.apl) | نقص ونلصق |
| 3325 | [`3325-list-rotate-left-by-39.apl`](examples/3325-list-rotate-left-by-39.apl) | نقص ونلصق |
| 3326 | [`3326-nth-term-arithmetic-sequence-step-35.apl`](examples/3326-nth-term-arithmetic-sequence-step-35.apl) | أ + (ن-1)*35 |
| 3327 | [`3327-nth-term-arithmetic-sequence-step-36.apl`](examples/3327-nth-term-arithmetic-sequence-step-36.apl) | أ + (ن-1)*36 |
| 3328 | [`3328-nth-term-arithmetic-sequence-step-37.apl`](examples/3328-nth-term-arithmetic-sequence-step-37.apl) | أ + (ن-1)*37 |
| 3329 | [`3329-nth-term-arithmetic-sequence-step-38.apl`](examples/3329-nth-term-arithmetic-sequence-step-38.apl) | أ + (ن-1)*38 |
| 3330 | [`3330-nth-term-arithmetic-sequence-step-39.apl`](examples/3330-nth-term-arithmetic-sequence-step-39.apl) | أ + (ن-1)*39 |
| 3331 | [`3331-sum-of-powers-of-35-up-to-n.apl`](examples/3331-sum-of-powers-of-35-up-to-n.apl) | نجمع 35^ي |
| 3332 | [`3332-sum-of-powers-of-36-up-to-n.apl`](examples/3332-sum-of-powers-of-36-up-to-n.apl) | نجمع 36^ي |
| 3333 | [`3333-sum-of-powers-of-37-up-to-n.apl`](examples/3333-sum-of-powers-of-37-up-to-n.apl) | نجمع 37^ي |
| 3334 | [`3334-sum-of-powers-of-38-up-to-n.apl`](examples/3334-sum-of-powers-of-38-up-to-n.apl) | نجمع 38^ي |
| 3335 | [`3335-sum-of-powers-of-39-up-to-n.apl`](examples/3335-sum-of-powers-of-39-up-to-n.apl) | نجمع 39^ي |
| 3336 | [`3336-clamp-list-values-to-max-35.apl`](examples/3336-clamp-list-values-to-max-35.apl) | نقص ما يزيد |
| 3337 | [`3337-clamp-list-values-to-max-36.apl`](examples/3337-clamp-list-values-to-max-36.apl) | نقص ما يزيد |
| 3338 | [`3338-clamp-list-values-to-max-37.apl`](examples/3338-clamp-list-values-to-max-37.apl) | نقص ما يزيد |
| 3339 | [`3339-clamp-list-values-to-max-38.apl`](examples/3339-clamp-list-values-to-max-38.apl) | نقص ما يزيد |
| 3340 | [`3340-clamp-list-values-to-max-39.apl`](examples/3340-clamp-list-values-to-max-39.apl) | نقص ما يزيد |
| 3341 | [`3341-repeat-text-35-times-with-dash.apl`](examples/3341-repeat-text-35-times-with-dash.apl) | نكرر ونفصل |
| 3342 | [`3342-repeat-text-36-times-with-dash.apl`](examples/3342-repeat-text-36-times-with-dash.apl) | نكرر ونفصل |
| 3343 | [`3343-repeat-text-37-times-with-dash.apl`](examples/3343-repeat-text-37-times-with-dash.apl) | نكرر ونفصل |
| 3344 | [`3344-repeat-text-38-times-with-dash.apl`](examples/3344-repeat-text-38-times-with-dash.apl) | نكرر ونفصل |
| 3345 | [`3345-repeat-text-39-times-with-dash.apl`](examples/3345-repeat-text-39-times-with-dash.apl) | نكرر ونفصل |
| 3346 | [`3346-pad-number-with-zeros-to-width-35.apl`](examples/3346-pad-number-with-zeros-to-width-35.apl) | zfill |
| 3347 | [`3347-pad-number-with-zeros-to-width-36.apl`](examples/3347-pad-number-with-zeros-to-width-36.apl) | zfill |
| 3348 | [`3348-pad-number-with-zeros-to-width-37.apl`](examples/3348-pad-number-with-zeros-to-width-37.apl) | zfill |
| 3349 | [`3349-pad-number-with-zeros-to-width-38.apl`](examples/3349-pad-number-with-zeros-to-width-38.apl) | zfill |
| 3350 | [`3350-pad-number-with-zeros-to-width-39.apl`](examples/3350-pad-number-with-zeros-to-width-39.apl) | zfill |
| 3351 | [`3351-truncate-text-to-first-35-chars.apl`](examples/3351-truncate-text-to-first-35-chars.apl) | شريحة |
| 3352 | [`3352-truncate-text-to-first-36-chars.apl`](examples/3352-truncate-text-to-first-36-chars.apl) | شريحة |
| 3353 | [`3353-truncate-text-to-first-37-chars.apl`](examples/3353-truncate-text-to-first-37-chars.apl) | شريحة |
| 3354 | [`3354-truncate-text-to-first-38-chars.apl`](examples/3354-truncate-text-to-first-38-chars.apl) | شريحة |
| 3355 | [`3355-truncate-text-to-first-39-chars.apl`](examples/3355-truncate-text-to-first-39-chars.apl) | شريحة |
| 3356 | [`3356-sum-of-integers-from-20-to-n.apl`](examples/3356-sum-of-integers-from-20-to-n.apl) | نجمع بحلقة |
| 3357 | [`3357-sum-of-integers-from-21-to-n.apl`](examples/3357-sum-of-integers-from-21-to-n.apl) | نجمع بحلقة |
| 3358 | [`3358-sum-of-integers-from-22-to-n.apl`](examples/3358-sum-of-integers-from-22-to-n.apl) | نجمع بحلقة |
| 3359 | [`3359-sum-of-integers-from-23-to-n.apl`](examples/3359-sum-of-integers-from-23-to-n.apl) | نجمع بحلقة |
| 3360 | [`3360-sum-of-integers-from-24-to-n.apl`](examples/3360-sum-of-integers-from-24-to-n.apl) | نجمع بحلقة |
| 3361 | [`3361-count-numbers-with-exactly-20-divisors-below-limit.apl`](examples/3361-count-numbers-with-exactly-20-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3362 | [`3362-count-numbers-with-exactly-21-divisors-below-limit.apl`](examples/3362-count-numbers-with-exactly-21-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3363 | [`3363-count-numbers-with-exactly-22-divisors-below-limit.apl`](examples/3363-count-numbers-with-exactly-22-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3364 | [`3364-count-numbers-with-exactly-23-divisors-below-limit.apl`](examples/3364-count-numbers-with-exactly-23-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3365 | [`3365-count-numbers-with-exactly-24-divisors-below-limit.apl`](examples/3365-count-numbers-with-exactly-24-divisors-below-limit.apl) | نعد القواسم لكل عدد |
| 3366 | [`3366-list-count-items-with-remainder-one-mod-20.apl`](examples/3366-list-count-items-with-remainder-one-mod-20.apl) | نعد |
| 3367 | [`3367-list-count-items-with-remainder-one-mod-21.apl`](examples/3367-list-count-items-with-remainder-one-mod-21.apl) | نعد |
| 3368 | [`3368-list-count-items-with-remainder-one-mod-22.apl`](examples/3368-list-count-items-with-remainder-one-mod-22.apl) | نعد |
| 3369 | [`3369-list-count-items-with-remainder-one-mod-23.apl`](examples/3369-list-count-items-with-remainder-one-mod-23.apl) | نعد |
| 3370 | [`3370-list-count-items-with-remainder-one-mod-24.apl`](examples/3370-list-count-items-with-remainder-one-mod-24.apl) | نعد |
| 3371 | [`3371-price-after-20-percent-discount-integer.apl`](examples/3371-price-after-20-percent-discount-integer.apl) | نطرح الخصم |
| 3372 | [`3372-price-after-21-percent-discount-integer.apl`](examples/3372-price-after-21-percent-discount-integer.apl) | نطرح الخصم |
| 3373 | [`3373-price-after-22-percent-discount-integer.apl`](examples/3373-price-after-22-percent-discount-integer.apl) | نطرح الخصم |
| 3374 | [`3374-price-after-23-percent-discount-integer.apl`](examples/3374-price-after-23-percent-discount-integer.apl) | نطرح الخصم |
| 3375 | [`3375-price-after-24-percent-discount-integer.apl`](examples/3375-price-after-24-percent-discount-integer.apl) | نطرح الخصم |
| 3376 | [`3376-price-with-20-percent-tax-integer.apl`](examples/3376-price-with-20-percent-tax-integer.apl) | نضيف الضريبة |
| 3377 | [`3377-price-with-21-percent-tax-integer.apl`](examples/3377-price-with-21-percent-tax-integer.apl) | نضيف الضريبة |
| 3378 | [`3378-price-with-22-percent-tax-integer.apl`](examples/3378-price-with-22-percent-tax-integer.apl) | نضيف الضريبة |
| 3379 | [`3379-price-with-23-percent-tax-integer.apl`](examples/3379-price-with-23-percent-tax-integer.apl) | نضيف الضريبة |
| 3380 | [`3380-price-with-24-percent-tax-integer.apl`](examples/3380-price-with-24-percent-tax-integer.apl) | نضيف الضريبة |
| 3381 | [`3381-split-bill-among-20-people-ceiling.apl`](examples/3381-split-bill-among-20-people-ceiling.apl) | نقرب لأعلى |
| 3382 | [`3382-split-bill-among-21-people-ceiling.apl`](examples/3382-split-bill-among-21-people-ceiling.apl) | نقرب لأعلى |
| 3383 | [`3383-split-bill-among-22-people-ceiling.apl`](examples/3383-split-bill-among-22-people-ceiling.apl) | نقرب لأعلى |
| 3384 | [`3384-split-bill-among-23-people-ceiling.apl`](examples/3384-split-bill-among-23-people-ceiling.apl) | نقرب لأعلى |
| 3385 | [`3385-split-bill-among-24-people-ceiling.apl`](examples/3385-split-bill-among-24-people-ceiling.apl) | نقرب لأعلى |
| 3386 | [`3386-minutes-to-hours-and-minutes-base-20.apl`](examples/3386-minutes-to-hours-and-minutes-base-20.apl) | نقسم على 20 |
| 3387 | [`3387-minutes-to-hours-and-minutes-base-21.apl`](examples/3387-minutes-to-hours-and-minutes-base-21.apl) | نقسم على 21 |
| 3388 | [`3388-minutes-to-hours-and-minutes-base-22.apl`](examples/3388-minutes-to-hours-and-minutes-base-22.apl) | نقسم على 22 |
| 3389 | [`3389-minutes-to-hours-and-minutes-base-23.apl`](examples/3389-minutes-to-hours-and-minutes-base-23.apl) | نقسم على 23 |
| 3390 | [`3390-minutes-to-hours-and-minutes-base-24.apl`](examples/3390-minutes-to-hours-and-minutes-base-24.apl) | نقسم على 24 |
| 3391 | [`3391-count-words-with-length-at-least-20.apl`](examples/3391-count-words-with-length-at-least-20.apl) | نعد الكلمات |
| 3392 | [`3392-count-words-with-length-at-least-21.apl`](examples/3392-count-words-with-length-at-least-21.apl) | نعد الكلمات |
| 3393 | [`3393-count-words-with-length-at-least-22.apl`](examples/3393-count-words-with-length-at-least-22.apl) | نعد الكلمات |
| 3394 | [`3394-count-words-with-length-at-least-23.apl`](examples/3394-count-words-with-length-at-least-23.apl) | نعد الكلمات |
| 3395 | [`3395-count-words-with-length-at-least-24.apl`](examples/3395-count-words-with-length-at-least-24.apl) | نعد الكلمات |
| 3396 | [`3396-square-of-radius-times-29-area-approx.apl`](examples/3396-square-of-radius-times-29-area-approx.apl) | المساحة ≈ 29×نق²/7 |
| 3397 | [`3397-square-of-radius-times-31-area-approx.apl`](examples/3397-square-of-radius-times-31-area-approx.apl) | المساحة ≈ 31×نق²/7 |
| 3398 | [`3398-square-of-radius-times-37-area-approx.apl`](examples/3398-square-of-radius-times-37-area-approx.apl) | المساحة ≈ 37×نق²/7 |
| 3399 | [`3399-rectangle-area-scaled-by-11.apl`](examples/3399-rectangle-area-scaled-by-11.apl) | نكبر الضلعين |
| 3400 | [`3400-rectangle-area-scaled-by-12.apl`](examples/3400-rectangle-area-scaled-by-12.apl) | نكبر الضلعين |
| 3401 | [`3401-rectangle-area-scaled-by-13.apl`](examples/3401-rectangle-area-scaled-by-13.apl) | نكبر الضلعين |
| 3402 | [`3402-interior-angle-sum-of-polygon-plus-11.apl`](examples/3402-interior-angle-sum-of-polygon-plus-11.apl) | (ن-2)*180 |
| 3403 | [`3403-interior-angle-sum-of-polygon-plus-12.apl`](examples/3403-interior-angle-sum-of-polygon-plus-12.apl) | (ن-2)*180 |
| 3404 | [`3404-interior-angle-sum-of-polygon-plus-13.apl`](examples/3404-interior-angle-sum-of-polygon-plus-13.apl) | (ن-2)*180 |
| 3405 | [`3405-interior-angle-sum-of-polygon-plus-14.apl`](examples/3405-interior-angle-sum-of-polygon-plus-14.apl) | (ن-2)*180 |
| 3406 | [`3406-sum-of-ord-values-offset-10.apl`](examples/3406-sum-of-ord-values-offset-10.apl) | نجمع ord+10 |
| 3407 | [`3407-sum-of-ord-values-offset-11.apl`](examples/3407-sum-of-ord-values-offset-11.apl) | نجمع ord+11 |
| 3408 | [`3408-sum-of-ord-values-offset-12.apl`](examples/3408-sum-of-ord-values-offset-12.apl) | نجمع ord+12 |
| 3409 | [`3409-linear-recurrence-a-n-equals-11-times-previous-plus-one.apl`](examples/3409-linear-recurrence-a-n-equals-11-times-previous-plus-one.apl) | نكرر القاعدة |
| 3410 | [`3410-linear-recurrence-a-n-equals-12-times-previous-plus-one.apl`](examples/3410-linear-recurrence-a-n-equals-12-times-previous-plus-one.apl) | نكرر القاعدة |
| 3411 | [`3411-multiplication-table-row-of-17.apl`](examples/3411-multiplication-table-row-of-17.apl) | من 1 إلى ن |
| 3412 | [`3412-multiplication-table-row-of-18.apl`](examples/3412-multiplication-table-row-of-18.apl) | من 1 إلى ن |
| 3413 | [`3413-multiplication-table-row-of-19.apl`](examples/3413-multiplication-table-row-of-19.apl) | من 1 إلى ن |
| 3414 | [`3414-sum-of-squares-from-10-to-n.apl`](examples/3414-sum-of-squares-from-10-to-n.apl) | نجمع المربعات |
| 3415 | [`3415-sum-of-squares-from-11-to-n.apl`](examples/3415-sum-of-squares-from-11-to-n.apl) | نجمع المربعات |
| 3416 | [`3416-sum-of-squares-from-12-to-n.apl`](examples/3416-sum-of-squares-from-12-to-n.apl) | نجمع المربعات |
| 3417 | [`3417-list-count-items-below-3.apl`](examples/3417-list-count-items-below-3.apl) | نعد الأصغر |
| 3418 | [`3418-list-count-items-below-5.apl`](examples/3418-list-count-items-below-5.apl) | نعد الأصغر |
| 3419 | [`3419-list-count-items-below-7.apl`](examples/3419-list-count-items-below-7.apl) | نعد الأصغر |
| 3420 | [`3420-list-count-items-below-10.apl`](examples/3420-list-count-items-below-10.apl) | نعد الأصغر |
| 3421 | [`3421-list-sum-of-items-above-3.apl`](examples/3421-list-sum-of-items-above-3.apl) | نجمع الأكبر |
| 3422 | [`3422-list-sum-of-items-above-5.apl`](examples/3422-list-sum-of-items-above-5.apl) | نجمع الأكبر |
| 3423 | [`3423-list-sum-of-items-above-7.apl`](examples/3423-list-sum-of-items-above-7.apl) | نجمع الأكبر |
| 3424 | [`3424-list-sum-of-items-above-10.apl`](examples/3424-list-sum-of-items-above-10.apl) | نجمع الأكبر |
| 3425 | [`3425-list-sum-of-first-3-items.apl`](examples/3425-list-sum-of-first-3-items.apl) | شريحة ثم مجموع |
| 3426 | [`3426-list-sum-of-first-5-items.apl`](examples/3426-list-sum-of-first-5-items.apl) | شريحة ثم مجموع |
| 3427 | [`3427-list-sum-of-first-7-items.apl`](examples/3427-list-sum-of-first-7-items.apl) | شريحة ثم مجموع |
| 3428 | [`3428-list-sum-of-first-10-items.apl`](examples/3428-list-sum-of-first-10-items.apl) | شريحة ثم مجموع |
| 3429 | [`3429-list-sum-of-last-3-items.apl`](examples/3429-list-sum-of-last-3-items.apl) | شريحة سالبة |
| 3430 | [`3430-list-sum-of-last-5-items.apl`](examples/3430-list-sum-of-last-5-items.apl) | شريحة سالبة |
| 3431 | [`3431-list-sum-of-last-7-items.apl`](examples/3431-list-sum-of-last-7-items.apl) | شريحة سالبة |
| 3432 | [`3432-list-sum-of-last-10-items.apl`](examples/3432-list-sum-of-last-10-items.apl) | شريحة سالبة |
| 3433 | [`3433-nth-power-of-3-by-loop.apl`](examples/3433-nth-power-of-3-by-loop.apl) | نضرب ن مرات |
| 3434 | [`3434-nth-power-of-5-by-loop.apl`](examples/3434-nth-power-of-5-by-loop.apl) | نضرب ن مرات |
| 3435 | [`3435-nth-power-of-7-by-loop.apl`](examples/3435-nth-power-of-7-by-loop.apl) | نضرب ن مرات |
| 3436 | [`3436-nth-power-of-10-by-loop.apl`](examples/3436-nth-power-of-10-by-loop.apl) | نضرب ن مرات |
| 3437 | [`3437-last-digit-of-n-times-3.apl`](examples/3437-last-digit-of-n-times-3.apl) | باقي القسمة على 10 |
| 3438 | [`3438-last-digit-of-n-times-5.apl`](examples/3438-last-digit-of-n-times-5.apl) | باقي القسمة على 10 |
| 3439 | [`3439-last-digit-of-n-times-7.apl`](examples/3439-last-digit-of-n-times-7.apl) | باقي القسمة على 10 |
| 3440 | [`3440-last-digit-of-n-times-10.apl`](examples/3440-last-digit-of-n-times-10.apl) | باقي القسمة على 10 |
| 3441 | [`3441-count-digit-3-occurrences-up-to-n-v3.apl`](examples/3441-count-digit-3-occurrences-up-to-n-v3.apl) | نعد في كل عدد |
| 3442 | [`3442-count-digit-5-occurrences-up-to-n-v5.apl`](examples/3442-count-digit-5-occurrences-up-to-n-v5.apl) | نعد في كل عدد |
| 3443 | [`3443-count-digit-7-occurrences-up-to-n-v7.apl`](examples/3443-count-digit-7-occurrences-up-to-n-v7.apl) | نعد في كل عدد |
| 3444 | [`3444-count-digit-0-occurrences-up-to-n-v10.apl`](examples/3444-count-digit-0-occurrences-up-to-n-v10.apl) | نعد في كل عدد |
| 3445 | [`3445-join-first-3-chars-with-dots.apl`](examples/3445-join-first-3-chars-with-dots.apl) | نقطع ونربط |
| 3446 | [`3446-join-first-5-chars-with-dots.apl`](examples/3446-join-first-5-chars-with-dots.apl) | نقطع ونربط |
| 3447 | [`3447-join-first-7-chars-with-dots.apl`](examples/3447-join-first-7-chars-with-dots.apl) | نقطع ونربط |
| 3448 | [`3448-join-first-10-chars-with-dots.apl`](examples/3448-join-first-10-chars-with-dots.apl) | نقطع ونربط |

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
| `python scripts/check_duplicates.py` | لا يوجد مفتاحان عربيان يشيران إلى نفس الكائن الحقيقي (حتى لو اختلف المسار) |
| `python scripts/check_undefined_names.py` | لا مثال ولا كتلة ```apl في التوثيق تستعمل اسماً محذوفاً أو غير معرَّف (يحوّل ويفحص بـ ruff F821) |
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

افتح [`benchmarks/benchmark.html`](benchmarks/benchmark.html) لعرض التقرير العربي، أو حمّل إليه ملف JSON الناتج من الاختبار. الصفحة مكتفية ذاتياً ولا تحتاج إلى اتصال بالإنترنت.

> APL في هذا المشروع يحوّل الشيفرة العربية إلى Python؛ لذلك يستخدم قياس التنفيذ الصافي CPython في اللغتين، بينما يُظهر قياس تشغيل الملف كلفة بدء محرك APL والترجمة وذاكرتها المؤقتة.

## التوثيق الكامل

🚀 **[دليل البداية](docs/getting-started.md)** — من التثبيت إلى أول برنامج

🤔 **[لماذا APL؟](docs/why-apl.md)** — أين تتفوق وأين تضعف، بصراحة

📚 **[فهرس التوثيق](docs/README.md)** — مرجع كامل لكل التفاصيل

## المتطلبات

- Python 3.14+
- بدون مكتبات خارجية

## الرخصة

**Apache License 2.0** — رخصة مفتوحة المصدر معتمدة من OSI.

Ammar Programming Language (APL) — Copyright © 2026 Ammar Al-Khateeb (عمار الخطيب)

- ✅ مسموح: الاستخدام الشخصي والتجاري، التعديل، التوزيع، والاستخدام في مشاريع مغلقة المصدر.
- ✅ تمنحك الرخصة حقاً صريحاً في براءات الاختراع من المساهمين.
- 📌 الشرط: الاحتفاظ بإشعار حقوق النشر ونص الرخصة مع أي نسخة، وتوضيح التغييرات التي تجريها.
- ℹ️ لا تمنح الرخصة حق استخدام اسم المشروع أو علامته التجارية.

النص الكامل في ملف [LICENSE](LICENSE).

For inquiries: Ammar Al-Khateeb — inex.own@gmail.com

## المؤلف

**عمار الخطيب** — [GitHub](https://github.com/AmmarBasha2011) | [LinkedIn](https://www.linkedin.com/in/ammar2011)

---

**الإصدار:** APL v1.13 — 231,743 عنصراً عربياً — 106 مكتبة — 3448 مثال

## Language platform tools

Installable `apl` command, local multi-file projects, VS Code support and an
optional isolated local playground: [guide](docs/language-platform.md).

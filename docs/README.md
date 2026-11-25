# التوثيق الكامل — APL v1.13

جديد هنا؟ ابدأ بـ [دليل البداية](getting-started.md) — من التثبيت إلى أول برنامج.

أدلة إضافية: [برومبت وكيل الذكاء الاصطناعي](ai-agent-prompt.md) · [دليل النشر](deployment.md) · [لماذا APL](why-apl.md)

فهرس جميع ملفات التوثيق ومجلد الأمثلة الجاهزة:

| # | الملف | الوصف |
|---|-------|-------|
| 1 | [architecture.md](architecture.md) | هيكل المشروع، كيفية العمل، التصميم |
| 2 | [language-reference.md](language-reference.md) | مرجع اللغة — كل الكلمات المفتاحية والتراكيب |
| 3 | [language-features.md](language-features.md) | مميزات اللغة — match/case، معالجة الأخطاء، lambda، الوراثة |
| 4 | [error-messages.md](error-messages.md) | رسائل الأخطاء — كل أخطاء Python مترجمة بالعربي |
| 5 | [performance.md](performance.md) | تحسينات الأداء — التحميل الكسول، الذاكرة، طيّ الثوابت |
| 6 | [devtools-library.md](devtools-library.md) | مكتبة `devtools` — أدوات المطوّر: فحص، تصحيح، قياس أداء، ترجمة (inspect / ast / dis / pdb / doctest / timeit / profile / tracemalloc) (969 عنصراً) |
| 7 | [datafiles-library.md](datafiles-library.md) | مكتبة `datafiles` — البيانات والملفات: مسارات، ضغط، أرشيف، تسلسل، هياكل بيانات، XML، يونيكود (io / zipfile / tarfile / pickle / shelve / array / struct / xml.dom / xml.etree / unicodedata) (2,514 عنصراً) |
| 8 | [syslib-library.md](syslib-library.md) | مكتبة `syslib` — النظام والتشغيل والتشخيص: منصة، إشارات، موارد، تسجيل، اختبارات، عمليات متعددة، ctypes، سياق (platform / signal / resource / logging / unittest / multiprocessing / concurrent.futures / ctypes / termios) (3,712 عنصراً) |
| 9 | [weblibs-library.md](weblibs-library.md) | مكتبة `weblibs` — الويب والنصوص: بث متدفق، قوالب، ماركداون، تورنيدو، سطر الأوامر، تلوين الشيفرة (websockets / jinja2 / markdown / tornado / click / pygments) (1,431 عنصراً) |
| 10 | [webserver-library.md](webserver-library.md) | مكتبة `webserver` — الخوادم والشبكات: خوادم ASGI/WSGI، عملاء HTTP غير متزامنين، HTTP/1.1 (starlette / uvicorn / httpx / httpcore / h11 / anyio) (1,925 عنصراً) |
| 11 | [secauth-library.md](secauth-library.md) | مكتبة `secauth` — الأمان والمصادقة: تشفير وشهادات، قوالب معزولة، تحقق من المخططات، JWT (cryptography / jinja2 / jsonschema / jwt / cffi) (1,730 عنصراً) |
| 12 | [textdata-library.md](textdata-library.md) | مكتبة `textdata` — النصوص والبيانات: مطابقة الأنماط، أصناف الخصائص، الصور، النماذج الأولية (pathspec / attrs / PIL / markdown / proto) (1,571 عنصراً) |
| 13 | [utiltools-library.md](utiltools-library.md) | مكتبة `utiltools` — الأدوات المساعدة: الإصدارات والتواريخ، أشرطة التقدم، مراقبة العمليات (packaging / dateutil / tqdm / psutil / websockets) (1,401 عنصراً) |
| 14 | [idlelib-library.md](idlelib-library.md) | مكتبة `idlelib` — بيئة التطوير المدمجة: محرر، إكمال تلقائي، مصحح، إعدادات (idlelib) (720 عنصراً) |
| 15 | [cdp_use-library.md](cdp_use-library.md) | مكتبة `cdp_use` — بروتوكول أدوات تطوير كروم CDP (cdp_use) (1,164 عنصراً) |
| 16 | [acp-library.md](acp-library.md) | مكتبة `acp` — بروتوكول العميل-الوكيل ACP (acp) (403 عنصراً) |
| 17 | [aiohttp-library.md](aiohttp-library.md) | مكتبة `aiohttp` — عميل وخادم HTTP غير متزامنين (aiohttp) (1,310 عنصراً) |
| 18 | [stdlib_ext-library.md](stdlib_ext-library.md) | مكتبة `stdlib_ext` — توسعة المكتبة القياسية (encodings / inspect / doctest / pdb / tracemalloc) (6,607 عنصراً) |
| 19 | [numpy-library.md](numpy-library.md) | مكتبة `numpy` — الحساب العددي: مصفوفات، جبر خطي، تحويلات فورييه، عشوائيات (numpy) (2,124 عنصراً) |
| 20 | [scipy-library.md](scipy-library.md) | مكتبة `scipy` — الحساب العلمي: تكامل، تحسين، استيفاء، إحصاء، مصفوفات متناثرة (scipy) (3,913 عنصراً) |
| 21 | [telegram-library.md](telegram-library.md) | مكتبة `telegram` — بوتات تيليجرام: رسائل، محادثات، مستخدمون، لوحات مفاتيح (python-telegram-bot) (3,572 عنصراً) |
| 22 | [redis-library.md](redis-library.md) | مكتبة `redis` — تخزين المفاتيح والقيم والجلسات والمهام الموزعة (redis-py) (2,106 عنصراً) |
| 23 | [celery-library.md](celery-library.md) | مكتبة `celery` — طوابير المهام الموزعة والجدولة الزمنية (celery) (2,652 عنصراً) |
| 24 | [web-library.md](web-library.md) | مكتبة `web` — الويب والبريد: عناوين، HTTP، بريد، صناديق، كوكيز، HTML، WSGI، XML-RPC (http / urllib / email / mailbox / html / wsgiref / xmlrpc) (2,640 عنصراً) |
| 25 | [network-library.md](network-library.md) | مكتبة `net` — الشبكة: socket و ssl و http و email و SMTP/IMAP/FTP (1,006 عنصراً) |
| 26 | [fastapi-library.md](fastapi-library.md) | مكتبة `fastapi` — إطار عمل ويب حديث (531 عنصراً) |
| 27 | [requests-library.md](requests-library.md) | مكتبة `requests` — HTTP Client كامل (185 عنصراً) |
| 28 | [advanced-library.md](advanced-library.md) | مكتبة `advanced` — ميزات متقدمة (decorators, metaclasses, typing) (114 عنصراً) |
| 29 | [asyncio-library.md](asyncio-library.md) | مكتبة `asyncio` — برمجة غير متزامنة (101 عنصراً) |
| 30 | [argparse-library.md](argparse-library.md) | مكتبة `argparse` — تحليل وسائط سطر الأوامر (106 عنصراً) |
| 31 | [xml-library.md](xml-library.md) | مكتبة `xml` — قراءة وبناء وتعديل ملفات XML (ElementTree) (109 عنصراً) |
| 32 | [archive-library.md](archive-library.md) | مكتبة `archive` — أرشيف ZIP و TAR وضغط gzip / bz2 / xz (106 عنصراً) |
| 33 | [logging-library.md](logging-library.md) | مكتبة `logging` — تسجيل الأحداث (61 عنصراً) |
| 34 | [unittest-library.md](unittest-library.md) | مكتبة `unittest` — اختبارات الوحدة (81 عنصراً) |
| 35 | [flask-library.md](flask-library.md) | مكتبة `flask` — إطار عمل ويب (78 عنصراً) |
| 36 | [subprocess-library.md](subprocess-library.md) | مكتبة `subprocess` — أوامر النظام (67 عنصراً) |
| 37 | [dataclasses-library.md](dataclasses-library.md) | مكتبة `dataclasses` — فئات بيانات، تعدادات، ABC (51 عنصراً) |
| 38 | [math-library.md](math-library.md) | مكتبة `math` — مثلثات، لوغاريتمات، جذور، تقريب، هندسة (63 عنصراً) |
| 39 | [pathlib-library.md](pathlib-library.md) | مكتبة `pathlib` — التعامل مع المسارات ككائنات (39 عنصراً) |
| 40 | [datetime-library.md](datetime-library.md) | مكتبة `datetime` — التاريخ والوقت والتحويل بينهما (19 عنصراً) |
| 41 | [configparser-library.md](configparser-library.md) | مكتبة `configparser` — ملفات الإعدادات (32 عنصراً) |
| 42 | [os-library.md](os-library.md) | مكتبة `os` — ملفات، مجلدات، مسارات، فحص (20 عنصراً) |
| 43 | [threading-library.md](threading-library.md) | مكتبة `threading` — تعدد المهام (19 عنصراً) |
| 44 | [operator-library.md](operator-library.md) | مكتبة `operator` — المشغّلات كدوال (add, mul, itemgetter) (20 عنصراً) |
| 45 | [time-library.md](time-library.md) | مكتبة `time` — وقت، تاريخ، تأخير، تنسيق (18 عنصراً) |
| 46 | [re-library.md](re-library.md) | مكتبة `re` — تعابير نمطية، بحث، استبدال، تقسيم (24 عنصراً) |
| 47 | [sqlite3-library.md](sqlite3-library.md) | مكتبة `sqlite3` — قاعدة بيانات محلية (20 عنصراً) |
| 48 | [decimal-library.md](decimal-library.md) | مكتبة `decimal` — الحساب العشري الدقيق (بدون أخطاء تقريب) (21 عنصراً) |
| 49 | [random-library.md](random-library.md) | مكتبة `random` — أرقام عشوائية، توزيعات، خلط (20 عنصراً) |
| 50 | [itertools-library.md](itertools-library.md) | مكتبة `itertools` — أدوات تكرار، توافيق، تباديل (12 عنصراً) |
| 51 | [statistics-library.md](statistics-library.md) | مكتبة `statistics` — متوسط، وسيط، منوال، تباين، انحراف معياري (15 عنصراً) |
| 52 | [csv-library.md](csv-library.md) | مكتبة `csv` — ملفات بيانات (12 عنصراً) |
| 53 | [uuid-library.md](uuid-library.md) | مكتبة `uuid` — المعرفات الفريدة (UUID) (10 عنصراً) |
| 54 | [urllib-library.md](urllib-library.md) | مكتبة `urllib` — تحليل وبناء الروابط وترميزها (1 عنصراً) |
| 55 | [shutil-library.md](shutil-library.md) | مكتبة `shutil` — نسخ ونقل وحذف الملفات والمجلدات (8 عنصراً) |
| 56 | [base64-library.md](base64-library.md) | مكتبة `base64` — الترميز وفك الترميز (11 عنصراً) |
| 57 | [json-library.md](json-library.md) | مكتبة `json` — قراءة وكتابة JSON (5 عنصراً) |
| 58 | [string-library.md](string-library.md) | مكتبة `string` — مجموعات الأحرف والرموز الثابتة (10 عنصراً) |
| 59 | [collections-library.md](collections-library.md) | مكتبة `collections` — Counter, defaultdict, deque (3 عنصراً) |
| 60 | [textwrap-library.md](textwrap-library.md) | مكتبة `textwrap` — تنسيق النصوص ولفّها (5 عنصراً) |
| 61 | [functools-library.md](functools-library.md) | مكتبة `functools` — أدوات الدوال (partial, cache, wraps) (2 عنصراً) |
| 62 | [fractions-library.md](fractions-library.md) | مكتبة `fractions` — الكسور الرياضية الدقيقة (6 عنصراً) |
| 63 | [secrets-library.md](secrets-library.md) | مكتبة `secrets` — توليد قيم عشوائية آمنة تشفيرياً (7 عنصراً) |
| 64 | [zoneinfo-library.md](zoneinfo-library.md) | مكتبة `zoneinfo` — المناطق الزمنية (IANA) (6 عنصراً) |
| 65 | [hashlib-library.md](hashlib-library.md) | مكتبة `hashlib` — تجزئة وتشفير (4 عنصراً) |
| 66 | [enum-library.md](enum-library.md) | مكتبة `enum` — أنواع معدودة (Enums) — قيم مسمّاة بدل الأرقام السحرية (7 عنصراً) |
| 67 | [getpass-library.md](getpass-library.md) | مكتبة `getpass` — إدخال كلمات السر دون إظهارها (2 عنصراً) |
| 68 | [pprint-library.md](pprint-library.md) | مكتبة `pprint` — طباعة منسّقة للقواميس والقوائم (2 عنصراً) |
| 69 | [numdeep-library.md](numdeep-library.md) | مكتبة `numdeep` — الحساب العددي والعلمي العميق: مصفوفات وجبر خطي وإحصاء وتكامل (numpy / scipy) (936 عنصراً) |
| 70 | [botdeep-library.md](botdeep-library.md) | مكتبة `botdeep` — بوتات تيليجرام العميقة: كل أنواع الرسائل والتحديثات واللوحات (python-telegram-bot) (925 عنصراً) |
| 71 | [taskdeep-library.md](taskdeep-library.md) | مكتبة `taskdeep` — المهام الموزعة العميقة: طوابير ورسائل وجدولة ونتائج (celery / kombu / billiard / amqp) (3,449 عنصراً) |
| 72 | [storedeep-library.md](storedeep-library.md) | مكتبة `storedeep` — التخزين العميق: كل أوامر وأنواع redis (redis-py) (1,501 عنصراً) |
| 73 | [pygdeep-library.md](pygdeep-library.md) | مكتبة `pygdeep` — تلوين الشيفرة العميق: كل المُحلّلات والمُنسّقات والأنماط (pygments) (9,078 عنصراً) |
| 74 | [webdeep-library.md](webdeep-library.md) | مكتبة `webdeep` — الويب العميق: أطر وخوادم وبروتوكولات (fastapi / starlette / tornado / websockets) (1,778 عنصراً) |
| 75 | [datadeep-library.md](datadeep-library.md) | مكتبة `datadeep` — النماذج والتحقق العميق: مخططات وأنواع وتحقق (pydantic / jsonschema) (2,435 عنصراً) |
| 76 | [mediadeep-library.md](mediadeep-library.md) | مكتبة `mediadeep` — الصور والنصوص العميقة: صور وماركداون وقوالب وسطر أوامر (PIL / markdown / jinja2) (3,406 عنصراً) |
| 77 | [secdeep-library.md](secdeep-library.md) | مكتبة `secdeep` — الأمان وسحابة جوجل العميقة: تشفير وتوكنات وواجهات API (cryptography / google) (2,546 عنصراً) |
| 78 | [utildeep-library.md](utildeep-library.md) | مكتبة `utildeep` — الأدوات العميقة: تواريخ ومناطق ومراقبة وحزم مساعدة (dateutil / pytz / psutil) (478 عنصراً) |
| 79 | [stdfull-library.md](stdfull-library.md) | مكتبة `stdfull` — المكتبة القياسية الشاملة: كل ما تبقى من وحدات Python القياسية (4,326 عنصراً) |
| 80 | [sympy_ext-library.md](sympy_ext-library.md) | مكتبة `sympy_ext` — توسعة حزمة sympy: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (20,217 عنصراً) |
| 81 | [plotly_ext-library.md](plotly_ext-library.md) | مكتبة `plotly_ext` — توسعة حزمة plotly: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (11,595 عنصراً) |
| 82 | [sqlalchemy_ext-library.md](sqlalchemy_ext-library.md) | مكتبة `sqlalchemy_ext` — توسعة حزمة sqlalchemy: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (8,440 عنصراً) |
| 83 | [twisted_ext-library.md](twisted_ext-library.md) | مكتبة `twisted_ext` — توسعة حزمة twisted: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (8,144 عنصراً) |
| 84 | [astropy_ext-library.md](astropy_ext-library.md) | مكتبة `astropy_ext` — توسعة حزمة astropy: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (6,591 عنصراً) |
| 85 | [statsmodels_ext-library.md](statsmodels_ext-library.md) | مكتبة `statsmodels_ext` — توسعة حزمة statsmodels: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (5,180 عنصراً) |
| 86 | [bokeh_ext-library.md](bokeh_ext-library.md) | مكتبة `bokeh_ext` — توسعة حزمة bokeh: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (4,955 عنصراً) |
| 87 | [sphinx_ext-library.md](sphinx_ext-library.md) | مكتبة `sphinx_ext` — توسعة حزمة sphinx: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (4,645 عنصراً) |
| 88 | [nltk_ext-library.md](nltk_ext-library.md) | مكتبة `nltk_ext` — توسعة حزمة nltk: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (4,603 عنصراً) |
| 89 | [openpyxl_ext-library.md](openpyxl_ext-library.md) | مكتبة `openpyxl_ext` — توسعة حزمة openpyxl: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (4,404 عنصراً) |
| 90 | [pandas_ext-library.md](pandas_ext-library.md) | مكتبة `pandas_ext` — توسعة حزمة pandas: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (4,312 عنصراً) |
| 91 | [crypto_ext-library.md](crypto_ext-library.md) | مكتبة `crypto_ext` — توسعة حزمة Crypto: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (740 عنصراً) |
| 92 | [matplotlib_ext-library.md](matplotlib_ext-library.md) | مكتبة `matplotlib_ext` — توسعة حزمة matplotlib: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (4,035 عنصراً) |
| 93 | [docutils_ext-library.md](docutils_ext-library.md) | مكتبة `docutils_ext` — توسعة حزمة docutils: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (3,520 عنصراً) |
| 94 | [cv2_ext-library.md](cv2_ext-library.md) | مكتبة `cv2_ext` — توسعة حزمة cv2: أصنافها ودوالها وطرقها وثوابتها التي لا تغطّيها مكتبات APL الأخرى (3,298 عنصراً) |
| 95 | [pkgs_ext1-library.md](pkgs_ext1-library.md) | مكتبة `pkgs_ext1` — حزم متنوعة موسّعة (selenium / dask / xarray / pyarrow / sklearn / gevent / cdp_use / mpmath / networkx / botocore / jedi / aiohttp / telegram / markdown_it) (20,830 عنصراً) |
| 96 | [pkgs_ext2-library.md](pkgs_ext2-library.md) | مكتبة `pkgs_ext2` — حزم متنوعة موسّعة (scrapy / prompt_toolkit / lxml / hypothesis / peewee / arrow / alembic / rich / trio / paramiko / h5py / cryptography / pyasn1 / skimage / yaml / seaborn / pyparsing / bs4 / shapely / babel / redis / pendulum / mako / nacl / typer / google / PIL / kombu / marshmallow / requests / sqlparse / celery / packaging / six / httpx / jinja2 / acp / regex / uvicorn / websockets / markdown / tornado / anyio / httplib2 / pygments / cffi / click / fastapi / httpcore / googleapiclient / tqdm / starlette / dateutil / pydantic / attr / jsonschema / multidict / numpy / scipy) (19,295 عنصراً) |

---
## الأمثلة الجاهزة (956 مثالاً)

956 برنامجاً حقيقياً مكتوبة بالكامل بالعربي، جميعها مختبرة وتعمل بلا أخطاء:

| # | الملف | الوصف |
|--:|-------|-------|
| 1 | [`01-calculator.apl`](../examples/01-calculator.apl) | آلة حاسبة تفاعلية |
| 2 | [`02-sales-report.apl`](../examples/02-sales-report.apl) | تقرير مبيعات وتقدير الإجمالي |
| 3 | [`03-task-manager.apl`](../examples/03-task-manager.apl) | مدير المهام (Lists + Dictionary + Search) |
| 4 | [`04-text-analyzer.apl`](../examples/04-text-analyzer.apl) | تحليل نص ومطابقة الأنماط |
| 5 | [`05-report-writer.apl`](../examples/05-report-writer.apl) | كاتب التقارير |
| 6 | [`06-search-sort.apl`](../examples/06-search-sort.apl) | خوارزميات البحث والترتيب |
| 7 | [`07-sqlite-tasks.apl`](../examples/07-sqlite-tasks.apl) | قاعدة بيانات المهام (SQLite) |
| 8 | [`08-word-frequency.apl`](../examples/08-word-frequency.apl) | عدّاد الكلمات الم unique مع itertools |
| 9 | [`09-encoding-hashing.apl`](../examples/09-encoding-hashing.apl) | تشفير وفك تشفير البيانات (base64 + hashlib) |
| 10 | [`10-file-manager.apl`](../examples/10-file-manager.apl) | مدير الملفات والمجلدات |
| 11 | [`11-fibonacci.apl`](../examples/11-fibonacci.apl) | مثال تطبيقي |
| 12 | [`12-prime-check.apl`](../examples/12-prime-check.apl) | فحص الأعداد الأولية |
| 13 | [`13-matrix-ops.apl`](../examples/13-matrix-ops.apl) | عمليات المصفوفات |
| 14 | [`14-statistics-report.apl`](../examples/14-statistics-report.apl) | تقرير إحصائي للدرجات |
| 15 | [`15-string-processing.apl`](../examples/15-string-processing.apl) | معالجة النصوص |
| 16 | [`16-hash-passwords.apl`](../examples/16-hash-passwords.apl) | بصمات كلمات السر |
| 17 | [`17-bank-account.apl`](../examples/17-bank-account.apl) | نظام حساب بنكي مبسّط |
| 18 | [`18-linked-list.apl`](../examples/18-linked-list.apl) | قائمة مرتبطة |
| 19 | [`19-inventory-system.apl`](../examples/19-inventory-system.apl) | نظام إدارة مخزون |
| 20 | [`20-json-config.apl`](../examples/20-json-config.apl) | قراءة وكتابة إعدادات JSON |
| 21 | [`21-calculator-class.apl`](../examples/21-calculator-class.apl) | آلة حاسبة كصنف |
| 22 | [`22-temperature-converter.apl`](../examples/22-temperature-converter.apl) | محول درجات الحرارة |
| 23 | [`23-palindrome-check.apl`](../examples/23-palindrome-check.apl) | فحص الكلمات المتناظرة |
| 24 | [`24-roman-numerals.apl`](../examples/24-roman-numerals.apl) | تحويل إلى أرقام رومانية |
| 25 | [`25-caesar-cipher.apl`](../examples/25-caesar-cipher.apl) | شيفرة قيصر |
| 26 | [`26-queue-stack.apl`](../examples/26-queue-stack.apl) | طابور ومكدّس |
| 27 | [`27-expense-tracker.apl`](../examples/27-expense-tracker.apl) | متتبع المصروفات |
| 28 | [`28-binary-search.apl`](../examples/28-binary-search.apl) | البحث الثنائي |
| 29 | [`29-coin-change.apl`](../examples/29-coin-change.apl) | مشكلة تغيير العملات |
| 30 | [`30-lru-cache-decorator.apl`](../examples/30-lru-cache-decorator.apl) | كاش LRU مع functools |
| 31 | [`31-decorator-timer.apl`](../examples/31-decorator-timer.apl) | مزخرف قياس الأداء |
| 32 | [`32-generator-pipeline.apl`](../examples/32-generator-pipeline.apl) | خط أنابيب بالمولدات |
| 33 | [`33-comprehension-examples.apl`](../examples/33-comprehension-examples.apl) | القوائم فهم comprehensions |
| 34 | [`34-args-parser-cli.apl`](../examples/34-args-parser-cli.apl) | محلل وسائط سطر الأوامر |
| 35 | [`35-logging-setup.apl`](../examples/35-logging-setup.apl) | إعداد السجلات |
| 36 | [`36-threading-tasks.apl`](../examples/36-threading-tasks.apl) | تنفيذ مهام متوازية |
| 37 | [`37-csv-report.apl`](../examples/37-csv-report.apl) | قراءة وكتابة ملفات CSV |
| 38 | [`38-hashlib-integrity.apl`](../examples/38-hashlib-integrity.apl) | التحقق من سلامة البيانات |
| 39 | [`39-uuid-tokens.apl`](../examples/39-uuid-tokens.apl) | توليد معرفات فريدة |
| 40 | [`40-latin-converter.apl`](../examples/40-latin-converter.apl) | تحويل بين الأرقام العربية والهندية |
| 41 | [`41-word-frequency-top.apl`](../examples/41-word-frequency-top.apl) | أكثر الكلمات تكراراً |
| 42 | [`42-geometry-shapes.apl`](../examples/42-geometry-shapes.apl) | أشكال هندسية |
| 43 | [`43-parallel-processing.apl`](../examples/43-parallel-processing.apl) | المعالجة عبر map و filter |
| 44 | [`44-tic-tac-toe.apl`](../examples/44-tic-tac-toe.apl) | لعبة tic-tac-toe |
| 45 | [`45-simple-lexer.apl`](../examples/45-simple-lexer.apl) | محلّل نصوص بسيط |
| 46 | [`46-simple-interpreter.apl`](../examples/46-simple-interpreter.apl) | مفسّر حسابات مبسّط |
| 58 | [`47-simple-cache.apl`](../examples/47-simple-cache.apl) | كاش بسيط من الصفر |
| 58 | [`48-text-analyzer-advanced.apl`](../examples/48-text-analyzer-advanced.apl) | تحليل نص متقدم |
| 49 | [`49-validate-input.apl`](../examples/49-validate-input.apl) | التحقق من صحة المدخلات |
| 50 | [`50-final-showcase.apl`](../examples/50-final-showcase.apl) | العرض النهائي (شامل) |
| 51 | [`51-xml-read.apl`](../examples/51-xml-read.apl) | قراءة مستند XML وتحليله |
| 52 | [`52-xml-build.apl`](../examples/52-xml-build.apl) | بناء ملف XML وتعديله وحفظه |
| 58 | [`53-xml-namespaces.apl`](../examples/53-xml-namespaces.apl) | مساحات الأسماء والتحليل التدريجي والباني |
| 54 | [`54-archive-zip.apl`](../examples/54-archive-zip.apl) | أرشيف ZIP كامل: إنشاء، سرد، قراءة، تعديل، استخراج |
| 55 | [`55-archive-compress.apl`](../examples/55-archive-compress.apl) | الضغط: gzip و bz2 و xz ومقارنة الأحجام وأرشيف TAR |
| 56 | [`56-archive-backup.apl`](../examples/56-archive-backup.apl) | أداة نسخ احتياطي حقيقية: تحقق، تقليم، استعادة |
| 57 | [`57-net-tcp.apl`](../examples/57-net-tcp.apl) | مقابس TCP و UDP: خادم وعميل على نفس الجهاز |
| 58 | [`58-net-http.apl`](../examples/58-net-http.apl) | خادم HTTP محلي وعميله حتى تحليل JSON |
| 59 | [`59-net-email.apl`](../examples/59-net-email.apl) | بناء رسالة بريد ومرفق وحفظها `.eml` ثم قراءتها |
| 60 | [`60-net-tools.apl`](../examples/60-net-tools.apl) | أدوات بلا اتصال: IP و struct و ترميزات و MIME |
| 61 | [`61-devtools-inspect.apl`](../examples/61-devtools-inspect.apl) | فحص الكائنات: التوقيع، النوع، الأعضاء، شجرة الأصناف (devtools) |
| 62 | [`62-devtools-ast.apl`](../examples/62-devtools-ast.apl) | شجرة بناء الجملة: تحليل المصدر وتجوال العقد (devtools/ast) |
| 63 | [`63-devtools-dis.apl`](../examples/63-devtools-dis.apl) | تفكيك الشيفرة وتقطيع الرموز وجداول الرموز (devtools/dis) |
| 64 | [`64-devtools-traceback.apl`](../examples/64-devtools-traceback.apl) | تنسيق تتبع الأخطاء واختبارات الوثائق (devtools/traceback) |
| 65 | [`65-devtools-profile.apl`](../examples/65-devtools-profile.apl) | قياس الزمن وتحليل الأداء والذاكرة (devtools/timeit) |
| 66 | [`66-devtools-import.apl`](../examples/66-devtools-import.apl) | الاستيراد الديناميكي والتحذيرات وذاكرة الأسطر (devtools/importlib) |
| 67 | [`67-web-http-status.apl`](../examples/67-web-http-status.apl) | ثوابت حالات HTTP (web/http) |
| 68 | [`68-web-url-parse.apl`](../examples/68-web-url-parse.apl) | تحليل العناوين وترميزها وربطها (web/urllib.parse) |
| 69 | [`69-web-email-build.apl`](../examples/69-web-email-build.apl) | بناء رسائل البريد وإخراجها (web/email) |
| 70 | [`70-web-mailbox-mime.apl`](../examples/70-web-mailbox-mime.apl) | صناديق البريد وأنواع MIME (web/mailbox) |
| 71 | [`71-web-html-cookies.apl`](../examples/71-web-html-cookies.apl) | تهريب HTML وملفات تعريف الارتباط (web/html) |
| 72 | [`72-web-xmlrpc-wsgi.apl`](../examples/72-web-xmlrpc-wsgi.apl) | نداءات XML-RPC ورؤوس WSGI (web/xmlrpc) |
| 73 | [`73-web-robots-maildir.apl`](../examples/73-web-robots-maildir.apl) | تحليل robots.txt وصناديق Maildir (web/urllib) |
| 74 | [`74-df-paths.apl`](../examples/74-df-paths.apl) | المسارات والبحث النمطي (datafiles/os.path) |
| 75 | [`75-df-archive.apl`](../examples/75-df-archive.apl) | ضغط zip وgzip وbz2 (datafiles/zipfile) |
| 76 | [`76-df-serialize.apl`](../examples/76-df-serialize.apl) | تسلسل البيانات (datafiles/pickle) |
| 77 | [`77-df-structures.apl`](../examples/77-df-structures.apl) | هياكل البيانات (datafiles/array) |
| 78 | [`78-df-xml.apl`](../examples/78-df-xml.apl) | بناء XML وتحليله (datafiles/xml) |
| 79 | [`79-df-text.apl`](../examples/79-df-text.apl) | يونيكود والترميز (datafiles/unicodedata) |
| 80 | [`80-df-refs.apl`](../examples/80-df-refs.apl) | المراجع والسياق والفروق (datafiles/weakref) |
| 81 | [`81-syslib-system.apl`](../examples/81-syslib-system.apl) | معلومات النظام (syslib/platform) |
| 82 | [`82-syslib-signals.apl`](../examples/82-syslib-signals.apl) | الإشارات وحدود الموارد (syslib/signal) |
| 83 | [`83-syslib-logging.apl`](../examples/83-syslib-logging.apl) | التسجيل (syslib/logging) |
| 84 | [`84-syslib-docs.apl`](../examples/84-syslib-docs.apl) | التوثيق ويونيكود والفروق (syslib/pydoc) |
| 85 | [`85-syslib-processes.apl`](../examples/85-syslib-processes.apl) | العمليات المتعددة (syslib/multiprocessing) |
| 86 | [`86-syslib-ctypes.apl`](../examples/86-syslib-ctypes.apl) | ctypes والأنواع (syslib/ctypes) |
| 87 | [`87-syslib-context.apl`](../examples/87-syslib-context.apl) | السياق وتحليل الأوامر (syslib/contextvars) |
| 88 | [`88-weblibs.apl`](../examples/88-weblibs.apl) | الويب والنصوص (weblibs/markdown) |
| 89 | [`89-webserver.apl`](../examples/89-webserver.apl) | الخوادم (webserver/uvicorn) |
| 90 | [`90-secauth.apl`](../examples/90-secauth.apl) | الأمان والمصادقة (secauth/jinja2) |
| 91 | [`91-textdata.apl`](../examples/91-textdata.apl) | النصوص والبيانات (textdata/pathspec) |
| 92 | [`92-utiltools.apl`](../examples/92-utiltools.apl) | الأدوات (utiltools/dateutil) |
| 93 | [`93-idlelib.apl`](../examples/93-idlelib.apl) | بيئة التطوير (idlelib) |
| 94 | [`94-cdp-use.apl`](../examples/94-cdp-use.apl) | المتصفح (cdp_use) |
| 95 | [`95-acp.apl`](../examples/95-acp.apl) | الوكلاء (acp) |
| 96 | [`96-aiohttp2.apl`](../examples/96-aiohttp2.apl) | الويب غير المتزامن (aiohttp) |
| 97 | [`97-stdlib-ext.apl`](../examples/97-stdlib-ext.apl) | المكتبة الموسّعة (stdlib_ext) |
| 98 | [`98-numpy.apl`](../examples/98-numpy.apl) | الحساب العددي (numpy) |
| 99 | [`99-scipy.apl`](../examples/99-scipy.apl) | الحساب العلمي (scipy) |
| 100 | [`100-telegram.apl`](../examples/100-telegram.apl) | بوتات تيليجرام (telegram) |
| 101 | [`101-redis.apl`](../examples/101-redis.apl) | تخزين ريديس (redis) |
| 102 | [`102-celery.apl`](../examples/102-celery.apl) | طوابير المهام (celery) |
| 103 | [`103-gcd-lcm.apl`](../examples/103-gcd-lcm.apl) | القاسم المشترك والمضاعف المشترك ونظرية الأعداد |
| 104 | [`104-trig-table.apl`](../examples/104-trig-table.apl) | جدول الدوال المثلثية |
| 105 | [`105-log-exp.apl`](../examples/105-log-exp.apl) | اللوغاريتمات والأسس والجذور |
| 106 | [`106-rounding.apl`](../examples/106-rounding.apl) | التقريب بكل أنواعه |
| 107 | [`107-special-funcs.apl`](../examples/107-special-funcs.apl) | الدوال الخاصة: جاما ودالة الخطأ |
| 108 | [`108-decimal-money.apl`](../examples/108-decimal-money.apl) | حساب الأموال بدقة بلا أخطاء عشرية |
| 109 | [`109-fractions-ops.apl`](../examples/109-fractions-ops.apl) | الكسور الدقيقة والعمليات عليها |
| 110 | [`110-statistics-data.apl`](../examples/110-statistics-data.apl) | تقرير إحصائي لدرجات طلاب |
| 111 | [`111-random-dice.apl`](../examples/111-random-dice.apl) | محاكاة رمي نرد |
| 112 | [`112-montecarlo-pi.apl`](../examples/112-montecarlo-pi.apl) | تقدير ط بطريقة مونت كارلو |
| 113 | [`113-string-constants.apl`](../examples/113-string-constants.apl) | ثوابت النصوص وتصنيف الحروف |
| 114 | [`114-string-template.apl`](../examples/114-string-template.apl) | قوالب النصوص |
| 115 | [`115-textwrap-report.apl`](../examples/115-textwrap-report.apl) | تنسيق التقارير النصية |
| 116 | [`116-re-emails.apl`](../examples/116-re-emails.apl) | استخراج البريد الإلكتروني والأرقام من نص |
| 117 | [`117-re-arabic-words.apl`](../examples/117-re-arabic-words.apl) | البحث عن الكلمات العربية في نص |
| 118 | [`118-re-substitutions.apl`](../examples/118-re-substitutions.apl) | الاستبدال والتقسيم بالأنماط |
| 119 | [`119-text-palindromes.apl`](../examples/119-text-palindromes.apl) | كشف النصوص المتناظرة |
| 120 | [`120-text-slug.apl`](../examples/120-text-slug.apl) | توليد روابط صديقة من العناوين |
| 121 | [`121-text-wordcount.apl`](../examples/121-text-wordcount.apl) | تكرار الكلمات في نص عربي |
| 122 | [`122-text-case-tools.apl`](../examples/122-text-case-tools.apl) | أدوات الحالة والفحص في النصوص |
| 123 | [`123-text-split-join.apl`](../examples/123-text-split-join.apl) | التقسيم والدمج |
| 124 | [`124-text-validate.apl`](../examples/124-text-validate.apl) | التحقق من المدخلات بالأنماط |
| 125 | [`125-datetime-arithmetic.apl`](../examples/125-datetime-arithmetic.apl) | حسابات التواريخ والمدد |
| 126 | [`126-datetime-format.apl`](../examples/126-datetime-format.apl) | تنسيق وتحليل التواريخ |
| 127 | [`127-datetime-age.apl`](../examples/127-datetime-age.apl) | حساب العمر بالتفصيل |
| 128 | [`128-zoneinfo-meeting.apl`](../examples/128-zoneinfo-meeting.apl) | تحويل اجتماع بين المناطق الزمنية |
| 129 | [`129-time-stopwatch.apl`](../examples/129-time-stopwatch.apl) | ساعة إيقاف لقياس الأداء |
| 130 | [`130-datetime-weekday.apl`](../examples/130-datetime-weekday.apl) | أيام الأسبوع وعطلات نهاية الأسبوع |
| 131 | [`131-month-calendar.apl`](../examples/131-month-calendar.apl) | طباعة تقويم شهر |
| 132 | [`132-pathlib-ops.apl`](../examples/132-pathlib-ops.apl) | المسارات ككائنات |
| 133 | [`133-file-search-ext.apl`](../examples/133-file-search-ext.apl) | البحث عن ملفات بامتداد معين |
| 134 | [`134-file-dedup-hash.apl`](../examples/134-file-dedup-hash.apl) | كشف الملفات المكررة بالتجزئة |
| 135 | [`135-dir-size-report.apl`](../examples/135-dir-size-report.apl) | تقرير أحجام المجلدات |
| 136 | [`136-shutil-backup.apl`](../examples/136-shutil-backup.apl) | نسخ احتياطي لمجلد كامل |
| 137 | [`137-file-rename-batch.apl`](../examples/137-file-rename-batch.apl) | إعادة تسمية مجموعة ملفات |
| 138 | [`138-os-env.apl`](../examples/138-os-env.apl) | معلومات النظام والبيئة |
| 139 | [`139-file-read-write.apl`](../examples/139-file-read-write.apl) | القراءة والكتابة الأساسية للملفات |
| 140 | [`140-json-nested.apl`](../examples/140-json-nested.apl) | JSON متداخل: بناء وقراءة |
| 141 | [`141-json-files.apl`](../examples/141-json-files.apl) | حفظ وقراءة JSON من ملف |
| 142 | [`142-json-merge.apl`](../examples/142-json-merge.apl) | دمج وتحديث قواميس JSON |
| 143 | [`143-csv-write-read.apl`](../examples/143-csv-write-read.apl) | كتابة وقراءة CSV |
| 144 | [`144-csv-stats.apl`](../examples/144-csv-stats.apl) | إحصاءات على عمود CSV |
| 145 | [`145-configparser-settings.apl`](../examples/145-configparser-settings.apl) | ملفات الإعدادات |
| 146 | [`146-json-to-csv.apl`](../examples/146-json-to-csv.apl) | تحويل JSON إلى CSV |
| 147 | [`147-counter-advanced.apl`](../examples/147-counter-advanced.apl) | العداد المتقدم |
| 148 | [`148-deque-printer.apl`](../examples/148-deque-printer.apl) | صف انتظار مهام الطباعة |
| 149 | [`149-itertools-combos.apl`](../examples/149-itertools-combos.apl) | التوافيق والناتج الديكارتي |
| 150 | [`150-itertools-slicing.apl`](../examples/150-itertools-slicing.apl) | تقطيع المكررات وتجميعها |
| 151 | [`151-functools-reduce.apl`](../examples/151-functools-reduce.apl) | الاختزال بدوال العوامل |
| 152 | [`152-functools-cache.apl`](../examples/152-functools-cache.apl) | التخزين المؤقت للدوال |
| 153 | [`153-operator-sorting.apl`](../examples/153-operator-sorting.apl) | الترتيب بجالب العناصر |
| 154 | [`154-enum-states.apl`](../examples/154-enum-states.apl) | حالات الطلب بالتعداد |
| 155 | [`155-dataclass-inventory.apl`](../examples/155-dataclass-inventory.apl) | جرد المنتجات بفئات البيانات |
| 156 | [`156-sqlite-notes.apl`](../examples/156-sqlite-notes.apl) | دفتر ملاحظات بقاعدة بيانات |
| 157 | [`157-sqlite-grades.apl`](../examples/157-sqlite-grades.apl) | تقرير درجات باستعلامات تجميعية |
| 158 | [`158-sqlite-transactions.apl`](../examples/158-sqlite-transactions.apl) | المعاملات والتراجع |
| 159 | [`159-hash-integrity.apl`](../examples/159-hash-integrity.apl) | التحقق من سلامة الملفات |
| 160 | [`160-hash-pbkdf2.apl`](../examples/160-hash-pbkdf2.apl) | اشتقاق مفاتيح كلمات السر |
| 161 | [`161-base64-codec.apl`](../examples/161-base64-codec.apl) | الترميز وفكه بقاعدة 64 |
| 162 | [`162-secrets-tokens.apl`](../examples/162-secrets-tokens.apl) | توليد الرموز الآمنة |
| 163 | [`163-uuid-generate.apl`](../examples/163-uuid-generate.apl) | المعرفات الفريدة |
| 164 | [`164-hash-file.apl`](../examples/164-hash-file.apl) | تجزئة ملف قبل وبعد النسخ |
| 165 | [`165-xml-parse.apl`](../examples/165-xml-parse.apl) | قراءة بيانات من XML |
| 166 | [`166-xml-build.apl`](../examples/166-xml-build.apl) | بناء مستند XML من الصفر |
| 167 | [`167-xml-modify.apl`](../examples/167-xml-modify.apl) | تعديل مستند XML |
| 168 | [`168-archive-tar.apl`](../examples/168-archive-tar.apl) | أرشيف TAR كامل |
| 169 | [`169-archive-compress.apl`](../examples/169-archive-compress.apl) | ضغط النصوص بثلاث خوارزميات |
| 170 | [`170-archive-zip-info.apl`](../examples/170-archive-zip-info.apl) | فحص أرشيف ZIP وإحصاءاته |
| 171 | [`171-asyncio-tasks.apl`](../examples/171-asyncio-tasks.apl) | مهام غير متزامنة |
| 172 | [`172-asyncio-gather.apl`](../examples/172-asyncio-gather.apl) | تشغيل مهام متوازية وتجميع نتائجها |
| 173 | [`173-threading-lock.apl`](../examples/173-threading-lock.apl) | عداد مشترك بقفل بين الخيوط |
| 174 | [`174-threading-event.apl`](../examples/174-threading-event.apl) | إشارة بين خيطين |
| 175 | [`175-subprocess-run.apl`](../examples/175-subprocess-run.apl) | تشغيل أوامر النظام |
| 176 | [`176-logging-levels.apl`](../examples/176-logging-levels.apl) | تسجيل الأحداث بمستويات |
| 177 | [`177-match-case.apl`](../examples/177-match-case.apl) | التطابق بالحالات (match/case) |
| 178 | [`178-decorators-property.apl`](../examples/178-decorators-property.apl) | الخواص المحسوبة والمحددات |
| 179 | [`179-context-manager.apl`](../examples/179-context-manager.apl) | مدير السياق مع الملفات |
| 180 | [`180-generator-pipeline.apl`](../examples/180-generator-pipeline.apl) | خط معالجة متسلسل |
| 181 | [`181-inheritance.apl`](../examples/181-inheritance.apl) | الوراثة وتعدد الأشكال |
| 182 | [`182-error-handling.apl`](../examples/182-error-handling.apl) | معالجة الأخطاء |
| 183 | [`183-lambda-hof.apl`](../examples/183-lambda-hof.apl) | الدوال المجردة ودوال الرتبة العليا |
| 184 | [`184-comprehensions.apl`](../examples/184-comprehensions.apl) | التوليدات الشاملة المتقدمة |
| 185 | [`185-bubble-sort.apl`](../examples/185-bubble-sort.apl) | الترتيب الفقاعي |
| 186 | [`186-merge-sort.apl`](../examples/186-merge-sort.apl) | ترتيب الدمج |
| 187 | [`187-quick-sort.apl`](../examples/187-quick-sort.apl) | الترتيب السريع |
| 188 | [`188-binary-search.apl`](../examples/188-binary-search.apl) | البحث الثنائي بالعودية |
| 189 | [`189-balanced-brackets.apl`](../examples/189-balanced-brackets.apl) | فحص توازن الأقواس |
| 190 | [`190-two-sum.apl`](../examples/190-two-sum.apl) | مجموع العددين |
| 191 | [`191-anagrams.apl`](../examples/191-anagrams.apl) | كشف الجناس الناقص |
| 192 | [`192-collatz.apl`](../examples/192-collatz.apl) | متتالية كولاتز |
| 193 | [`193-fizzbuzz.apl`](../examples/193-fizzbuzz.apl) | فيزباز |
| 194 | [`194-sieve-primes.apl`](../examples/194-sieve-primes.apl) | غربال إراتوستينس |
| 195 | [`195-matrix-multiply.apl`](../examples/195-matrix-multiply.apl) | ضرب المصفوفات |
| 196 | [`196-number-to-words.apl`](../examples/196-number-to-words.apl) | تحويل الأرقام إلى كلمات عربية |
| 197 | [`197-temperature-stats.apl`](../examples/197-temperature-stats.apl) | إحصاءات درجات الحرارة |
| 198 | [`198-todo-json.apl`](../examples/198-todo-json.apl) | قائمة مهام محفوظة في ملف JSON |
| 199 | [`199-banking-oop.apl`](../examples/199-banking-oop.apl) | نظام بنكي بسيط بالكائنات |
| 200 | [`200-final-showcase-2.apl`](../examples/200-final-showcase-2.apl) | لوحة نتائج الطلاب |
| 201 | [`201-insertion-sort.apl`](../examples/201-insertion-sort.apl) | الترتيب بالإدراج |
| 202 | [`202-selection-sort.apl`](../examples/202-selection-sort.apl) | ترتيب الاختيار |
| 203 | [`203-counting-sort.apl`](../examples/203-counting-sort.apl) | الترتيب بالعد |
| 204 | [`204-radix-sort.apl`](../examples/204-radix-sort.apl) | الترتيب الجذري |
| 205 | [`205-heap-sort.apl`](../examples/205-heap-sort.apl) | ترتيب الكومة |
| 206 | [`206-linear-search.apl`](../examples/206-linear-search.apl) | البحث الخطي وكل المواضع |
| 207 | [`207-jump-search.apl`](../examples/207-jump-search.apl) | البحث بالقفز |
| 208 | [`208-fibonacci-memo.apl`](../examples/208-fibonacci-memo.apl) | فيبوناتشي بالتخزين |
| 209 | [`209-climbing-stairs.apl`](../examples/209-climbing-stairs.apl) | طرق صعود السلم (برمجة ديناميكية) |
| 210 | [`210-coin-change.apl`](../examples/210-coin-change.apl) | أقل عدد عملات (برمجة ديناميكية) |
| 211 | [`211-stack-class.apl`](../examples/211-stack-class.apl) | المكدس كصنف |
| 212 | [`212-queue-class.apl`](../examples/212-queue-class.apl) | الطابور كصنف |
| 213 | [`213-linked-list.apl`](../examples/213-linked-list.apl) | القائمة المترابطة |
| 214 | [`214-binary-tree.apl`](../examples/214-binary-tree.apl) | الشجرة الثنائية وجولاتها |
| 215 | [`215-bst.apl`](../examples/215-bst.apl) | شجرة البحث الثنائية |
| 216 | [`216-trie.apl`](../examples/216-trie.apl) | شجرة البادئات (Trie) |
| 217 | [`217-graph-bfs.apl`](../examples/217-graph-bfs.apl) | المسح بالعرض للرسم البياني |
| 218 | [`218-graph-dfs.apl`](../examples/218-graph-dfs.apl) | المسح بالعمق وإيجاد مسار |
| 219 | [`219-priority-queue.apl`](../examples/219-priority-queue.apl) | طابور الأولوية اليدوي |
| 220 | [`220-doubly-linked.apl`](../examples/220-doubly-linked.apl) | القائمة المترابطة المزدوجة |
| 221 | [`221-caesar-cipher.apl`](../examples/221-caesar-cipher.apl) | شيفرة قيصر |
| 222 | [`222-vigenere.apl`](../examples/222-vigenere.apl) | شيفرة فيجنير |
| 223 | [`223-rot13.apl`](../examples/223-rot13.apl) | ROT13 |
| 224 | [`224-morse.apl`](../examples/224-morse.apl) | شيفرة مورس |
| 225 | [`225-run-length.apl`](../examples/225-run-length.apl) | ضغط طول التكرار |
| 226 | [`226-pig-latin.apl`](../examples/226-pig-latin.apl) | لغة الخنزير اللاتينية |
| 227 | [`227-leet-speak.apl`](../examples/227-leet-speak.apl) | لغة الليت (1337) |
| 228 | [`228-acronym.apl`](../examples/228-acronym.apl) | توليد الاختصارات |
| 229 | [`229-word-reverser.apl`](../examples/229-word-reverser.apl) | عكس الكلمات والجمل |
| 230 | [`230-title-case.apl`](../examples/230-title-case.apl) | تنسيق العناوين الإنجليزية |
| 231 | [`231-factory-pattern.apl`](../examples/231-factory-pattern.apl) | نمط المصنع |
| 232 | [`232-singleton.apl`](../examples/232-singleton.apl) | نمط المفرد |
| 233 | [`233-observer.apl`](../examples/233-observer.apl) | نمط المراقب |
| 234 | [`234-strategy.apl`](../examples/234-strategy.apl) | نمط الاستراتيجية |
| 235 | [`235-builder.apl`](../examples/235-builder.apl) | نمط البنّاء |
| 236 | [`236-adapter.apl`](../examples/236-adapter.apl) | نمط المحوّل |
| 237 | [`237-state-machine.apl`](../examples/237-state-machine.apl) | آلة الحالات (إشارة مرور) |
| 238 | [`238-iterator-protocol.apl`](../examples/238-iterator-protocol.apl) | مكرر مخصص (عداد تنازلي) |
| 239 | [`239-template-method.apl`](../examples/239-template-method.apl) | نمط القالب |
| 240 | [`240-composite.apl`](../examples/240-composite.apl) | نمط المركّب (نظام ملفات) |
| 241 | [`241-tic-tac-toe.apl`](../examples/241-tic-tac-toe.apl) | لعبة إكس أو (منطق) |
| 242 | [`242-guess-number.apl`](../examples/242-guess-number.apl) | تخمين الرقم (محاكاة آلية) |
| 243 | [`243-rock-paper-scissors.apl`](../examples/243-rock-paper-scissors.apl) | حجر ورقة مقص |
| 244 | [`244-dice-stats.apl`](../examples/244-dice-stats.apl) | إحصاءات رمي النرد |
| 245 | [`245-card-deck.apl`](../examples/245-card-deck.apl) | مجموعة أوراق لعب |
| 246 | [`246-blackjack.apl`](../examples/246-blackjack.apl) | بلاك جاك مبسط |
| 247 | [`247-slot-machine.apl`](../examples/247-slot-machine.apl) | ماكينة الحظ |
| 248 | [`248-lottery.apl`](../examples/248-lottery.apl) | محاكاة يانصيب |
| 249 | [`249-bingo-card.apl`](../examples/249-bingo-card.apl) | بطاقة بنغو |
| 250 | [`250-hangman-logic.apl`](../examples/250-hangman-logic.apl) | منطق لعبة الرجل المشنوق |
| 251 | [`251-bmi.apl`](../examples/251-bmi.apl) | حاسبة كتلة الجسم |
| 252 | [`252-compound-interest.apl`](../examples/252-compound-interest.apl) | الفائدة المركبة |
| 253 | [`253-loan-amortization.apl`](../examples/253-loan-amortization.apl) | جدول سداد قرض |
| 254 | [`254-tip-split.apl`](../examples/254-tip-split.apl) | تقسيم الالحساب والإكرامية |
| 255 | [`255-leap-years.apl`](../examples/255-leap-years.apl) | السنوات الكبيسة |
| 256 | [`256-zeller-weekday.apl`](../examples/256-zeller-weekday.apl) | يوم الأسبوع بمعادلة زيلر |
| 257 | [`257-savings-goal.apl`](../examples/257-savings-goal.apl) | هدف الادخار |
| 258 | [`258-age-days.apl`](../examples/258-age-days.apl) | العمر بالأيام |
| 259 | [`259-countdown.apl`](../examples/259-countdown.apl) | عداد تنازلي لتاريخ |
| 260 | [`260-currency-static.apl`](../examples/260-currency-static.apl) | محول عملات بأسعار ثابتة |
| 261 | [`261-math-quiz.apl`](../examples/261-math-quiz.apl) | اختبار حساب آلي |
| 262 | [`262-password-strength.apl`](../examples/262-password-strength.apl) | قياس قوة كلمة المرور |
| 263 | [`263-atm.apl`](../examples/263-atm.apl) | صراف آلي مبسط |
| 264 | [`264-voting.apl`](../examples/264-voting.apl) | نظام تصويت |
| 265 | [`265-library-books.apl`](../examples/265-library-books.apl) | مكتبة كتب بسيطة |
| 266 | [`266-shopping-cart.apl`](../examples/266-shopping-cart.apl) | سلة تسوق |
| 267 | [`267-expense-categories.apl`](../examples/267-expense-categories.apl) | مصروفات بالفئات |
| 268 | [`268-grade-book.apl`](../examples/268-grade-book.apl) | سجل درجات فصل |
| 269 | [`269-parking.apl`](../examples/269-parking.apl) | موقف سيارات |
| 270 | [`270-flashcards.apl`](../examples/270-flashcards.apl) | بطاقات مراجعة |
| 271 | [`271-kadane.apl`](../examples/271-kadane.apl) | أكبر مجموع متتالي (كادان) |
| 272 | [`272-majority.apl`](../examples/272-majority.apl) | العنصر الأغلبي (بوير-مور) |
| 273 | [`273-dutch-flag.apl`](../examples/273-dutch-flag.apl) | مسألة العلم الهولندي |
| 274 | [`274-rotate-array.apl`](../examples/274-rotate-array.apl) | تدوير المصفوفة |
| 275 | [`275-merge-intervals.apl`](../examples/275-merge-intervals.apl) | دمج الفترات المتداخلة |
| 276 | [`276-product-except-self.apl`](../examples/276-product-except-self.apl) | حاصل ضرب ما عدا الذات |
| 277 | [`277-lis.apl`](../examples/277-lis.apl) | أطول متتالية متزايدة |
| 278 | [`278-lcs.apl`](../examples/278-lcs.apl) | أطول متتالية مشتركة |
| 279 | [`279-edit-distance.apl`](../examples/279-edit-distance.apl) | مسافة التحرير |
| 280 | [`280-knapsack.apl`](../examples/280-knapsack.apl) | حقيبة الظهر 0/1 |
| 281 | [`281-subsets.apl`](../examples/281-subsets.apl) | كل المجموعات الفرعية |
| 282 | [`282-permutations-manual.apl`](../examples/282-permutations-manual.apl) | التبديلات يدويا |
| 283 | [`283-generate-parentheses.apl`](../examples/283-generate-parentheses.apl) | توليد الأقواس المتوازنة |
| 284 | [`284-combination-sum.apl`](../examples/284-combination-sum.apl) | مجموعات بمبلغ مستهدف |
| 285 | [`285-n-queens.apl`](../examples/285-n-queens.apl) | ملكات الشطرنج (عد الحلول) |
| 286 | [`286-rat-maze.apl`](../examples/286-rat-maze.apl) | فأر في متاهة |
| 287 | [`287-word-search.apl`](../examples/287-word-search.apl) | البحث عن كلمة في شبكة |
| 288 | [`288-phone-letters.apl`](../examples/288-phone-letters.apl) | حروف لوحة الهاتف |
| 289 | [`289-sudoku-mini.apl`](../examples/289-sudoku-mini.apl) | سودوكو مصغر 4x4 |
| 290 | [`290-hanoi.apl`](../examples/290-hanoi.apl) | أبراج هانوي |
| 291 | [`291-string-search-count.apl`](../examples/291-string-search-count.apl) | عد تكرارات نموذج في نص |
| 292 | [`292-longest-palindrome-sub.apl`](../examples/292-longest-palindrome-sub.apl) | أطول مقطع متناظر |
| 293 | [`293-roman-to-int.apl`](../examples/293-roman-to-int.apl) | من أرقام رومانية إلى عشرية |
| 294 | [`294-int-to-roman.apl`](../examples/294-int-to-roman.apl) | من أرقام عشرية إلى رومانية |
| 295 | [`295-longest-common-prefix.apl`](../examples/295-longest-common-prefix.apl) | أطول مقدمة مشتركة |
| 296 | [`296-count-and-say.apl`](../examples/296-count-and-say.apl) | عد وقل |
| 297 | [`297-excel-column.apl`](../examples/297-excel-column.apl) | عنوان عمود إكسل |
| 298 | [`298-zigzag.apl`](../examples/298-zigzag.apl) | تحويل متعرج |
| 299 | [`299-valid-palindrome2.apl`](../examples/299-valid-palindrome2.apl) | متناظر بحذف حرف واحد |
| 300 | [`300-string-to-int.apl`](../examples/300-string-to-int.apl) | تحويل نص إلى عدد (atoi) |
| 301 | [`301-armstrong.apl`](../examples/301-armstrong.apl) | أعداد أرمسترونج |
| 302 | [`302-perfect-numbers.apl`](../examples/302-perfect-numbers.apl) | الأعداد الكاملة |
| 303 | [`303-happy-number.apl`](../examples/303-happy-number.apl) | الأعداد السعيدة |
| 304 | [`304-harshad.apl`](../examples/304-harshad.apl) | أعداد هارشاد |
| 305 | [`305-palindrome-number.apl`](../examples/305-palindrome-number.apl) | الأعداد المتناظرة |
| 306 | [`306-digital-root.apl`](../examples/306-digital-root.apl) | الجذر الرقمي |
| 307 | [`307-factorial.apl`](../examples/307-factorial.apl) | العاملي (مضروب العدد) |
| 308 | [`308-fast-power.apl`](../examples/308-fast-power.apl) | القوة السريعة |
| 309 | [`309-prime-factors.apl`](../examples/309-prime-factors.apl) | العوامل الأولية |
| 310 | [`310-totient.apl`](../examples/310-totient.apl) | دالة أويلر (مؤشر القواسم المشتركة) |
| 311 | [`311-tribonacci.apl`](../examples/311-tribonacci.apl) | متتالية تريبوناتشي |
| 312 | [`312-catalan.apl`](../examples/312-catalan.apl) | أعداد كاتالان |
| 313 | [`313-pascal.apl`](../examples/313-pascal.apl) | مثلث باسكال |
| 314 | [`314-look-and-say.apl`](../examples/314-look-and-say.apl) | متتالية انظر وقل |
| 315 | [`315-arithmetic-sequence.apl`](../examples/315-arithmetic-sequence.apl) | المتتالية الحسابية |
| 316 | [`316-geometric-sequence.apl`](../examples/316-geometric-sequence.apl) | المتتالية الهندسية |
| 317 | [`317-divisors.apl`](../examples/317-divisors.apl) | قواسم العدد |
| 318 | [`318-lcm-list.apl`](../examples/318-lcm-list.apl) | المضاعف المشترك الأصغر لقائمة |
| 319 | [`319-modular-inverse.apl`](../examples/319-modular-inverse.apl) | المعكوس الضربي التراكبي |
| 320 | [`320-sieve-count.apl`](../examples/320-sieve-count.apl) | عد الأولية وقائمتها حتى ن |
| 321 | [`321-chunk-list.apl`](../examples/321-chunk-list.apl) | تقسيم قائمة إلى قطع |
| 322 | [`322-flatten-nested.apl`](../examples/322-flatten-nested.apl) | تسطيح قائمة متداخلة (عودي) |
| 323 | [`323-pairwise.apl`](../examples/323-pairwise.apl) | أزواج متتالية |
| 324 | [`324-interleave.apl`](../examples/324-interleave.apl) | تداخل قائمتين |
| 325 | [`325-sliding-window.apl`](../examples/325-sliding-window.apl) | النافذة المنزلقة |
| 326 | [`326-dedupe-consecutive.apl`](../examples/326-dedupe-consecutive.apl) | إزالة التكرار المتتالي |
| 327 | [`327-unique-preserve.apl`](../examples/327-unique-preserve.apl) | فريد مع الحفاظ على الترتيب |
| 328 | [`328-zip-manual.apl`](../examples/328-zip-manual.apl) | دمج قائمتين يدويا (zip) |
| 329 | [`329-group-parity.apl`](../examples/329-group-parity.apl) | تجميع زوجي وفردي |
| 330 | [`330-running-total.apl`](../examples/330-running-total.apl) | المجموع التراكمي |
| 331 | [`331-next-birthday.apl`](../examples/331-next-birthday.apl) | العد التنازلي لعيد الميلاد |
| 332 | [`332-working-days.apl`](../examples/332-working-days.apl) | أيام العمل بين تاريخين |
| 333 | [`333-day-of-year.apl`](../examples/333-day-of-year.apl) | رقم اليوم في السنة |
| 334 | [`334-weeks-between.apl`](../examples/334-weeks-between.apl) | أسابيع بين تاريخين |
| 335 | [`335-month-start-end.apl`](../examples/335-month-start-end.apl) | أول وآخر يوم في الشهر |
| 336 | [`336-age-calculator.apl`](../examples/336-age-calculator.apl) | حاسبة العمر الدقيقة |
| 337 | [`337-quarter.apl`](../examples/337-quarter.apl) | الربع السنوي والفصل |
| 338 | [`338-first-weekdays.apl`](../examples/338-first-weekdays.apl) | أول اثنين من كل شهر |
| 339 | [`339-days-until-weekend.apl`](../examples/339-days-until-weekend.apl) | كم باقي على العطلة |
| 340 | [`340-date-list.apl`](../examples/340-date-list.apl) | قائمة تواريخ شهر |
| 341 | [`341-contacts-json.apl`](../examples/341-contacts-json.apl) | دليل جهات اتصال بملف JSON |
| 342 | [`342-notes-tags.apl`](../examples/342-notes-tags.apl) | ملاحظات بوسوم |
| 343 | [`343-inventory.apl`](../examples/343-inventory.apl) | مخزون منتجات |
| 344 | [`344-log-analyzer.apl`](../examples/344-log-analyzer.apl) | محلل سجلات |
| 345 | [`345-config-editor.apl`](../examples/345-config-editor.apl) | محرر إعدادات بسيط |
| 346 | [`346-duplicate-finder.apl`](../examples/346-duplicate-finder.apl) | كاشف المحتوى المكرر |
| 347 | [`347-backup-names.apl`](../examples/347-backup-names.apl) | مولد أسماء نسخ احتياطية |
| 348 | [`348-csv-manual.apl`](../examples/348-csv-manual.apl) | قراءة CSV يدويا |
| 349 | [`349-word-frequency-file.apl`](../examples/349-word-frequency-file.apl) | تكرار كلمات ملف |
| 350 | [`350-mini-database.apl`](../examples/350-mini-database.apl) | قاعدة بيانات JSON مصغرة |
| 351 | [`351-vector2d.apl`](../examples/351-vector2d.apl) | متجه ثنائي الأبعاد |
| 352 | [`352-complex-manual.apl`](../examples/352-complex-manual.apl) | أعداد مركبة يدويا |
| 353 | [`353-matrix-class.apl`](../examples/353-matrix-class.apl) | صنف مصفوفة |
| 354 | [`354-rational.apl`](../examples/354-rational.apl) | كسر اعتيادي يدوي |
| 355 | [`355-employee-payroll.apl`](../examples/355-employee-payroll.apl) | رواتب الموظفين |
| 356 | [`356-shapes-area.apl`](../examples/356-shapes-area.apl) | مساحات الأشكال |
| 357 | [`357-bank-accounts.apl`](../examples/357-bank-accounts.apl) | حسابات بنكية متعددة |
| 358 | [`358-school.apl`](../examples/358-school.apl) | مدرسة وطلاب ومواد |
| 359 | [`359-animals-farm.apl`](../examples/359-animals-farm.apl) | مزرعة حيوانات |
| 360 | [`360-temperature-class.apl`](../examples/360-temperature-class.apl) | صنف درجة حرارة |
| 361 | [`361-recursion-basics.apl`](../examples/361-recursion-basics.apl) | أساسيات العودية |
| 362 | [`362-gcd-euclid.apl`](../examples/362-gcd-euclid.apl) | القاسم المشترك بإقليدس العودي |
| 363 | [`363-reverse-string-rec.apl`](../examples/363-reverse-string-rec.apl) | عكس نص بالعودية |
| 364 | [`364-palindrome-rec.apl`](../examples/364-palindrome-rec.apl) | فحص التناظر بالعودية |
| 365 | [`365-sum-digits-rec.apl`](../examples/365-sum-digits-rec.apl) | مجموع الأرقام بالعودية |
| 366 | [`366-binary-rec.apl`](../examples/366-binary-rec.apl) | التحويل لثنائي بالعودية |
| 367 | [`367-flatten-rec.apl`](../examples/367-flatten-rec.apl) | عد عناصر متداخلة بالعودية |
| 368 | [`368-power-rec.apl`](../examples/368-power-rec.apl) | القوة بالعودية |
| 369 | [`369-tree-sum.apl`](../examples/369-tree-sum.apl) | مجموع شجرة بالعودية |
| 370 | [`370-fib-tree-count.apl`](../examples/370-fib-tree-count.apl) | عد استدعاءات فيبوناتشي |
| 371 | [`371-async-timeout.apl`](../examples/371-async-timeout.apl) | مهلة على مهمة غير متزامنة |
| 372 | [`372-async-tasks-list.apl`](../examples/372-async-tasks-list.apl) | قائمة مهام بأسماء |
| 373 | [`373-async-counter.apl`](../examples/373-async-counter.apl) | عداد متزامن مشترك |
| 374 | [`374-async-pipeline.apl`](../examples/374-async-pipeline.apl) | خط إنتاج واستهلاك مبسط |
| 375 | [`375-thread-semaphore.apl`](../examples/375-thread-semaphore.apl) | إشارة حد التزامن بين الخيوط |
| 376 | [`376-thread-timer.apl`](../examples/376-thread-timer.apl) | مؤقت خيط |
| 377 | [`377-thread-pool-manual.apl`](../examples/377-thread-pool-manual.apl) | مجمع خيوط يدوي |
| 378 | [`378-thread-name-id.apl`](../examples/378-thread-name-id.apl) | أسماء الخيوط |
| 379 | [`379-async-gather-mixed.apl`](../examples/379-async-gather-mixed.apl) | تجميع نتائج متنوعة |
| 380 | [`380-async-retry.apl`](../examples/380-async-retry.apl) | إعادة المحاولة غير المتزامنة |
| 381 | [`381-validate-emails.apl`](../examples/381-validate-emails.apl) | التحقق من قائمة بريدات |
| 382 | [`382-extract-numbers.apl`](../examples/382-extract-numbers.apl) | استخراج الأرقام والعمليات |
| 383 | [`383-parse-dates.apl`](../examples/383-parse-dates.apl) | استخراج التواريخ من نص |
| 384 | [`384-egypt-phones.apl`](../examples/384-egypt-phones.apl) | أرقام الهواتف المصرية |
| 385 | [`385-log-parser.apl`](../examples/385-log-parser.apl) | محلل سجل بالأنماط |
| 386 | [`386-strip-html.apl`](../examples/386-strip-html.apl) | إزالة وسوم HTML |
| 387 | [`387-camel-snake.apl`](../examples/387-camel-snake.apl) | تحويل camelCase إلى snake_case |
| 388 | [`388-markdown-headings.apl`](../examples/388-markdown-headings.apl) | فهرس عناوين ماركداون |
| 389 | [`389-find-arabic-numbers.apl`](../examples/389-find-arabic-numbers.apl) | الأرقام العربية المشرقية في نص |
| 390 | [`390-password-regex.apl`](../examples/390-password-regex.apl) | تحقق كلمة المرور بالأنماط |
| 391 | [`391-descriptive-stats.apl`](../examples/391-descriptive-stats.apl) | إحصاءات وصفية |
| 392 | [`392-variance-std.apl`](../examples/392-variance-std.apl) | التباين والانحراف المعياري |
| 393 | [`393-weighted-average.apl`](../examples/393-weighted-average.apl) | المتوسط المرجح |
| 394 | [`394-moving-average.apl`](../examples/394-moving-average.apl) | المتوسط المتحرك |
| 395 | [`395-percentiles.apl`](../examples/395-percentiles.apl) | المئينيات |
| 396 | [`396-correlation.apl`](../examples/396-correlation.apl) | معامل الارتباط |
| 397 | [`397-normalize-data.apl`](../examples/397-normalize-data.apl) | تطبيع البيانات |
| 398 | [`398-frequency-table.apl`](../examples/398-frequency-table.apl) | جدول التكرار |
| 399 | [`399-linear-regression.apl`](../examples/399-linear-regression.apl) | الانحدار الخطي |
| 400 | [`400-chi-square.apl`](../examples/400-chi-square.apl) | احتمالات بسيطة |
| 401 | [`401-hangman-game.apl`](../examples/401-hangman-game.apl) | لعبة الجلاد |
| 402 | [`402-rps-tournament.apl`](../examples/402-rps-tournament.apl) | بطولة حجر ورقة مقص |
| 403 | [`403-pig-dice.apl`](../examples/403-pig-dice.apl) | لعبة نرد الخنزير |
| 404 | [`404-higher-lower.apl`](../examples/404-higher-lower.apl) | أعلى أم أدنى |
| 405 | [`405-word-scramble.apl`](../examples/405-word-scramble.apl) | خلط الكلمات |
| 406 | [`406-typing-test.apl`](../examples/406-typing-test.apl) | اختبار سرعة الكتابة |
| 407 | [`407-simon-memory.apl`](../examples/407-simon-memory.apl) | لعبة ذاكرة الألوان |
| 408 | [`408-battleship-mini.apl`](../examples/408-battleship-mini.apl) | حرب السفن المصغرة |
| 409 | [`409-connect-four.apl`](../examples/409-connect-four.apl) | منطق أربعة تربح |
| 410 | [`410-slot-machine.apl`](../examples/410-slot-machine.apl) | ماكينة الحظ |
| 411 | [`411-base64-manual.apl`](../examples/411-base64-manual.apl) | ترميز Base64 يدويا |
| 412 | [`412-url-encode.apl`](../examples/412-url-encode.apl) | ترميز URL يدويا |
| 413 | [`413-unicode-explorer.apl`](../examples/413-unicode-explorer.apl) | مستكشف يونيكود |
| 414 | [`414-morse-code.apl`](../examples/414-morse-code.apl) | شيفرة مورس |
| 415 | [`415-run-length.apl`](../examples/415-run-length.apl) | ترميز طول التسلسل |
| 416 | [`416-hex-binary.apl`](../examples/416-hex-binary.apl) | تحويلات عددية |
| 417 | [`417-html-entities.apl`](../examples/417-html-entities.apl) | كيانات HTML |
| 418 | [`418-checksum.apl`](../examples/418-checksum.apl) | مجاميع تحقق |
| 419 | [`419-delta-encoding.apl`](../examples/419-delta-encoding.apl) | ترميز الفروقات |
| 420 | [`420-hamming-distance.apl`](../examples/420-hamming-distance.apl) | مسافة هامنج ورمز التصحيح |
| 421 | [`421-graph-coloring.apl`](../examples/421-graph-coloring.apl) | تلوين الرسم البياني |
| 422 | [`422-graph-components.apl`](../examples/422-graph-components.apl) | المكونات المتصلة |
| 423 | [`423-graph-bipartite.apl`](../examples/423-graph-bipartite.apl) | فحص الرسم الثنائي |
| 424 | [`424-topo-sort.apl`](../examples/424-topo-sort.apl) | الترتيب الطوبولوجي |
| 425 | [`425-kruskal-mst.apl`](../examples/425-kruskal-mst.apl) | شجرة كروسكال الممتدة |
| 426 | [`426-bellman-ford.apl`](../examples/426-bellman-ford.apl) | بيلمان فورد |
| 427 | [`427-floyd-warshall.apl`](../examples/427-floyd-warshall.apl) | فلويد وارشال |
| 428 | [`428-trie-autocomplete.apl`](../examples/428-trie-autocomplete.apl) | إكمال تلقائي بشجرة البادئات |
| 429 | [`429-union-find.apl`](../examples/429-union-find.apl) | مجموعات منفصلة |
| 430 | [`430-graph-diameter.apl`](../examples/430-graph-diameter.apl) | قطر الشجرة |
| 431 | [`431-table-formatter.apl`](../examples/431-table-formatter.apl) | منسق جداول نصية |
| 432 | [`432-progress-bar.apl`](../examples/432-progress-bar.apl) | شريط تقدم نصي |
| 433 | [`433-column-align.apl`](../examples/433-column-align.apl) | محاذاة النصوص |
| 434 | [`434-number-format.apl`](../examples/434-number-format.apl) | تنسيق الأرقام الكبيرة |
| 435 | [`435-duration-format.apl`](../examples/435-duration-format.apl) | تنسيق المدد الزمنية |
| 436 | [`436-byte-format.apl`](../examples/436-byte-format.apl) | تنسيق أحجام الملفات |
| 437 | [`437-sort-benchmark.apl`](../examples/437-sort-benchmark.apl) | مقارنة خوارزميات الترتيب |
| 438 | [`438-text-wrap.apl`](../examples/438-text-wrap.apl) | التفاف النص |
| 439 | [`439-pad-center.apl`](../examples/439-pad-center.apl) | توسيط وتعبئة النصوص |
| 440 | [`440-markdown-table.apl`](../examples/440-markdown-table.apl) | مولد جداول ماركداون |
| 441 | [`441-point-distance.apl`](../examples/441-point-distance.apl) | المسافة بين نقطتين |
| 442 | [`442-polygon-area.apl`](../examples/442-polygon-area.apl) | مساحة مضلع |
| 443 | [`443-circle-line.apl`](../examples/443-circle-line.apl) | حسابات الدائرة والخط |
| 444 | [`444-triangle-check.apl`](../examples/444-triangle-check.apl) | صحة المثلث ونوعه |
| 445 | [`445-angles.apl`](../examples/445-angles.apl) | تحويل الزوايا |
| 446 | [`446-vector-ops.apl`](../examples/446-vector-ops.apl) | عمليات المتجهات |
| 447 | [`447-quadratic.apl`](../examples/447-quadratic.apl) | حل المعادلة التربيعية |
| 448 | [`448-matrix-determinant.apl`](../examples/448-matrix-determinant.apl) | محدد المصفوفة |
| 449 | [`449-fractions-math.apl`](../examples/449-fractions-math.apl) | كسور رياضية |
| 450 | [`450-complex-manual.apl`](../examples/450-complex-manual.apl) | أعداد مركبة يدويا |
| 451 | [`451-arabic-lorem.apl`](../examples/451-arabic-lorem.apl) | مولد نص عشوائي عربي |
| 452 | [`452-name-generator.apl`](../examples/452-name-generator.apl) | مولد أسماء مستعارة |
| 453 | [`453-pronounceable-password.apl`](../examples/453-pronounceable-password.apl) | كلمة مرور قابلة للنطق |
| 454 | [`454-acronym.apl`](../examples/454-acronym.apl) | مولد الاختصارات |
| 455 | [`455-title-case.apl`](../examples/455-title-case.apl) | تنسيق العناوين الإنجليزية |
| 456 | [`456-slug-generator.apl`](../examples/456-slug-generator.apl) | مولد روابط Slug |
| 457 | [`457-hashtag-generator.apl`](../examples/457-hashtag-generator.apl) | مولد هاشتاجات |
| 458 | [`458-markov-lite.apl`](../examples/458-markov-lite.apl) | توليد جمل بسلاسل بسيطة |
| 459 | [`459-mad-libs.apl`](../examples/459-mad-libs.apl) | قصة بقوالب |
| 460 | [`460-palindrome-maker.apl`](../examples/460-palindrome-maker.apl) | مولد متناقضات لفظية |
| 461 | [`461-json-to-csv.apl`](../examples/461-json-to-csv.apl) | تحويل JSON إلى CSV |
| 462 | [`462-csv-to-json.apl`](../examples/462-csv-to-json.apl) | تحويل CSV إلى JSON |
| 463 | [`463-flatten-dict.apl`](../examples/463-flatten-dict.apl) | تسطيح القواميس المتداخلة |
| 464 | [`464-list-to-tree.apl`](../examples/464-list-to-tree.apl) | بناء شجرة من قائمة مسطحة |
| 465 | [`465-ini-parser.apl`](../examples/465-ini-parser.apl) | قارئ ملفات INI |
| 466 | [`466-yaml-lite.apl`](../examples/466-yaml-lite.apl) | قارئ YAML مبسط |
| 467 | [`467-env-parser.apl`](../examples/467-env-parser.apl) | قارئ ملفات البيئة |
| 468 | [`468-xml-lite.apl`](../examples/468-xml-lite.apl) | قارئ وسوم مبسط |
| 469 | [`469-html-table.apl`](../examples/469-html-table.apl) | سجلات إلى جدول HTML |
| 470 | [`470-properties-convert.apl`](../examples/470-properties-convert.apl) | تحويل خصائص إلى JSON |
| 471 | [`471-password-strength.apl`](../examples/471-password-strength.apl) | مقياس قوة كلمة المرور |
| 472 | [`472-login-limiter.apl`](../examples/472-login-limiter.apl) | محدد محاولات الدخول |
| 473 | [`473-pin-bruteforce.apl`](../examples/473-pin-bruteforce.apl) | تجربة كسر رمز PIN |
| 474 | [`474-otp-generator.apl`](../examples/474-otp-generator.apl) | مولد رموز تحقق |
| 475 | [`475-rbac.apl`](../examples/475-rbac.apl) | التحكم بالصلاحيات |
| 476 | [`476-fnv-hash.apl`](../examples/476-fnv-hash.apl) | دالة تجزية يدوية |
| 477 | [`477-salted-password.apl`](../examples/477-salted-password.apl) | تجزئة كلمة مرور بملح |
| 478 | [`478-token-generator.apl`](../examples/478-token-generator.apl) | مولد رموز الجلسات |
| 479 | [`479-firewall-sim.apl`](../examples/479-firewall-sim.apl) | محاكي جدار ناري |
| 480 | [`480-log-anomaly.apl`](../examples/480-log-anomaly.apl) | كاشف شذوذ السجلات |
| 481 | [`481-inventory-system.apl`](../examples/481-inventory-system.apl) | نظام مخزون |
| 482 | [`482-library-system.apl`](../examples/482-library-system.apl) | نظام مكتبة |
| 483 | [`483-grades-system.apl`](../examples/483-grades-system.apl) | نظام درجات مدرسي |
| 484 | [`484-clinic-queue.apl`](../examples/484-clinic-queue.apl) | طابور عيادة |
| 485 | [`485-parking-system.apl`](../examples/485-parking-system.apl) | نظام مواقف سيارات |
| 486 | [`486-expense-splitter.apl`](../examples/486-expense-splitter.apl) | مقسم المصاريف |
| 487 | [`487-survey-analyzer.apl`](../examples/487-survey-analyzer.apl) | محلل استبيان |
| 488 | [`488-tournament-bracket.apl`](../examples/488-tournament-bracket.apl) | شجرة بطولة |
| 489 | [`489-quiz-engine.apl`](../examples/489-quiz-engine.apl) | محرك اختبارات من ملف |
| 490 | [`490-chat-analyzer.apl`](../examples/490-chat-analyzer.apl) | محلل سجل محادثة |
| 491 | [`491-payroll-system.apl`](../examples/491-payroll-system.apl) | نظام رواتب |
| 492 | [`492-bus-booking.apl`](../examples/492-bus-booking.apl) | حجز مقاعد حافلة |
| 493 | [`493-recipe-manager.apl`](../examples/493-recipe-manager.apl) | مدير وصفات الطعام |
| 494 | [`494-habit-tracker.apl`](../examples/494-habit-tracker.apl) | متتبع العادات |
| 495 | [`495-flashcards.apl`](../examples/495-flashcards.apl) | بطاقات استذكار |
| 496 | [`496-invoice-generator.apl`](../examples/496-invoice-generator.apl) | مولد فواتير لملف |
| 497 | [`497-contact-search.apl`](../examples/497-contact-search.apl) | محرك بحث جهات اتصال |
| 498 | [`498-blog-engine.apl`](../examples/498-blog-engine.apl) | مولد مدونة ثابتة |
| 499 | [`499-event-planner.apl`](../examples/499-event-planner.apl) | مخطط فعاليات |
| 500 | [`500-task-manager-suite.apl`](../examples/500-task-manager-suite.apl) | نظام إدارة مهام متكامل |
| 501 | [`501-numdeep.apl`](../examples/501-numdeep.apl) | الحساب العلمي العميق (numdeep/numpy) |
| 502 | [`502-botdeep.apl`](../examples/502-botdeep.apl) | بوتات تيليجرام العميقة (botdeep/telegram) |
| 503 | [`503-taskdeep.apl`](../examples/503-taskdeep.apl) | المهام الموزعة العميقة (taskdeep/kombu) |
| 504 | [`504-storedeep.apl`](../examples/504-storedeep.apl) | التخزين العميق (storedeep/redis) |
| 505 | [`505-pygdeep.apl`](../examples/505-pygdeep.apl) | تلوين الشيفرة العميق (pygdeep/pygments) |
| 506 | [`506-webdeep.apl`](../examples/506-webdeep.apl) | الويب العميق (webdeep/fastapi) |
| 507 | [`507-datadeep.apl`](../examples/507-datadeep.apl) | النماذج والتحقق العميق (datadeep/pydantic) |
| 508 | [`508-mediadeep.apl`](../examples/508-mediadeep.apl) | الصور والنصوص العميقة (mediadeep/PIL) |
| 509 | [`509-secdeep.apl`](../examples/509-secdeep.apl) | الأمان العميق (secdeep/cryptography) |
| 510 | [`510-utildeep.apl`](../examples/510-utildeep.apl) | الأدوات العميق (utildeep/dateutil) |
| 511 | [`511-stdfull.apl`](../examples/511-stdfull.apl) | المكتبة القياسية الشاملة (stdfull) |
| 512 | [`512-dijkstra.apl`](../examples/512-dijkstra.apl) | خوارزمية ديكسترا لأقصر مسار في رسم موزون |
| 513 | [`513-kmp-search.apl`](../examples/513-kmp-search.apl) | بحث كنوث-موريس-برات عن نمط في نص |
| 514 | [`514-shell-sort.apl`](../examples/514-shell-sort.apl) | فرز شل بفجوات متناقصة |
| 515 | [`515-bucket-sort.apl`](../examples/515-bucket-sort.apl) | فرز الحاويات لأعداد كسرية |
| 516 | [`516-interpolation-search.apl`](../examples/516-interpolation-search.apl) | بحث بالاستكمال في قائمة متجانسة |
| 517 | [`517-ternary-search.apl`](../examples/517-ternary-search.apl) | بحث ثلاثي في قائمة مفرزة |
| 518 | [`518-segment-tree.apl`](../examples/518-segment-tree.apl) | شجرة المقاطع لمجاميع المجالات مع تحديث |
| 519 | [`519-fenwick-tree.apl`](../examples/519-fenwick-tree.apl) | شجرة فينويك للمجاميع البادئة |
| 520 | [`520-bloom-filter.apl`](../examples/520-bloom-filter.apl) | مرشح بلوم للعضوية التقريبية |
| 521 | [`521-chinese-remainder.apl`](../examples/521-chinese-remainder.apl) | مبرهنة الباقي الصينية |
| 522 | [`522-fib-doubling.apl`](../examples/522-fib-doubling.apl) | فيبوناتشي بالمضاعفة السريعة O(log n) |
| 523 | [`523-house-robber.apl`](../examples/523-house-robber.apl) | لص المنازل (برمجة ديناميكية) |
| 524 | [`524-word-break.apl`](../examples/524-word-break.apl) | تقطيع نص إلى كلمات قاموس (برمجة ديناميكية) |
| 525 | [`525-flood-fill-islands.apl`](../examples/525-flood-fill-islands.apl) | عدّ الجزر بملء غامر على شبكة |
| 526 | [`526-line-diff.apl`](../examples/526-line-diff.apl) | مقارنة نصين سطرياً بأطول تتابع مشترك |
| 527 | [`527-token-bucket.apl`](../examples/527-token-bucket.apl) | دلو الرموز لتحديد معدل الطلبات |
| 528 | [`528-luhn-check.apl`](../examples/528-luhn-check.apl) | تحقق لون لأرقام البطاقات |
| 529 | [`529-isbn13-check.apl`](../examples/529-isbn13-check.apl) | تحقق من ردمك ISBN-13 |
| 530 | [`530-hijri-convert.apl`](../examples/530-hijri-convert.apl) | تحويل ميلادي إلى هجري (الخوارزمية الكويتية) |
| 531 | [`531-arabic-indic-digits.apl`](../examples/531-arabic-indic-digits.apl) | تحويل الأرقام بين العربية الغربية والمشرقية |
| 532 | [`532-egypt-national-id.apl`](../examples/532-egypt-national-id.apl) | قراءة الرقم القومي المصري: الميلاد والمحافظة والنوع |
| 533 | [`533-zakat-calc.apl`](../examples/533-zakat-calc.apl) | حساب زكاة المال فوق النصاب |
| 534 | [`534-electricity-bill.apl`](../examples/534-electricity-bill.apl) | فاتورة كهرباء منزلية بشرائح تقريبية |
| 535 | [`535-vat-invoice.apl`](../examples/535-vat-invoice.apl) | فاتورة بضريبة قيمة مضافة 14% |
| 536 | [`536-prim-mst.apl`](../examples/536-prim-mst.apl) | شجرة بريم الممتدة الصغرى |
| 537 | [`537-a-star.apl`](../examples/537-a-star.apl) | بحث A* على شبكة بعوائق مع إعادة بناء المسار |
| 538 | [`538-topological-lex.apl`](../examples/538-topological-lex.apl) | ترتيب طوبولوجي بأصغر تسمية أولاً (خوارزمية كان) |
| 539 | [`539-rabin-karp.apl`](../examples/539-rabin-karp.apl) | بحث رابين-كارب بالتجزئة الدوارة |
| 540 | [`540-z-algorithm.apl`](../examples/540-z-algorithm.apl) | مصفوفة Z للبحث عن نمط |
| 541 | [`541-aho-corasick.apl`](../examples/541-aho-corasick.apl) | أتمتة أهو-كوراسيك للبحث بعدة أنماط معاً |
| 542 | [`542-huffman-coding.apl`](../examples/542-huffman-coding.apl) | ترميز هافمان: شجرة أكواد متغيرة الطول |
| 543 | [`543-burrows-wheeler.apl`](../examples/543-burrows-wheeler.apl) | تحويل بوروز-ويلر وعكسه |
| 544 | [`544-word-ladder.apl`](../examples/544-word-ladder.apl) | سلم الكلمات: أقصر تحويل بحرف واحد (BFS) |
| 545 | [`545-quickselect.apl`](../examples/545-quickselect.apl) | اختيار سريع: ك-أصغر عنصر دون فرز كامل |
| 546 | [`546-sliding-window-max.apl`](../examples/546-sliding-window-max.apl) | أقصى نافذة منزلقة بقائمة رتيبة |
| 547 | [`547-next-greater-element.apl`](../examples/547-next-greater-element.apl) | العنصر الأكبر التالي بمكدس رتيب |
| 548 | [`548-largest-rectangle.apl`](../examples/548-largest-rectangle.apl) | أكبر مستطيل في هيستوجرام بمكدس |
| 549 | [`549-trapping-rain-water.apl`](../examples/549-trapping-rain-water.apl) | حصر مياه الأمطار بين الحواجز بمؤشرين |
| 550 | [`550-count-inversions.apl`](../examples/550-count-inversions.apl) | عدّ المعكوسات بفرز الدمج |
| 551 | [`551-matrix-chain-dp.apl`](../examples/551-matrix-chain-dp.apl) | ترتيب ضرب المصفوفات بأقل كلفة (برمجة ديناميكية) |
| 552 | [`552-egg-drop-dp.apl`](../examples/552-egg-drop-dp.apl) | لغز البيض: أقل محاولات مضمونة (برمجة ديناميكية) |
| 553 | [`553-miller-rabin.apl`](../examples/553-miller-rabin.apl) | اختبار ميلر-رابين للأولية بقواعد حتمية |
| 554 | [`554-segmented-sieve.apl`](../examples/554-segmented-sieve.apl) | الغربال المقطعي: أوليات مجال بعيد |
| 555 | [`555-egyptian-fractions.apl`](../examples/555-egyptian-fractions.apl) | الكسور المصرية: تمثيل كسر بمجموع كسور وحدة |
| 556 | [`556-newton-sqrt.apl`](../examples/556-newton-sqrt.apl) | الجذر التربيعي بطريقة نيوتن-رافسون |
| 557 | [`557-josephus.apl`](../examples/557-josephus.apl) | مسألة جوزيفوس: الناجي من حلقة الإقصاء |
| 558 | [`558-gaussian-elimination.apl`](../examples/558-gaussian-elimination.apl) | حذف جاوس لحل نظام معادلات خطية |
| 559 | [`559-derangements.apl`](../examples/559-derangements.apl) | التباديل المُخلّة: لا عنصر في موضعه |
| 560 | [`560-continued-fractions.apl`](../examples/560-continued-fractions.apl) | الكسر المستمر لجذر غير نسبي |
| 561 | [`561-egypt-carriers.apl`](../examples/561-egypt-carriers.apl) | معرفة شركة المحمول المصرية من مقدمة الرقم |
| 562 | [`562-currency-change.apl`](../examples/562-currency-change.apl) | فك مبلغ إلى فئات الجنيه المصري (بالقروش) |
| 563 | [`563-gpa-calc.apl`](../examples/563-gpa-calc.apl) | المعدل التراكمي بالساعات المعتمدة |
| 564 | [`564-iban-check.apl`](../examples/564-iban-check.apl) | تحقق IBAN بمعيار mod-97 وتوليد رقم تحقق |
| 565 | [`565-base62-codec.apl`](../examples/565-base62-codec.apl) | ترميز base62 لروابط قصيرة |
| 566 | [`566-circuit-breaker.apl`](../examples/566-circuit-breaker.apl) | قاطع الدائرة: حماية من تكرار الفشل |
| 567 | [`567-semver-compare.apl`](../examples/567-semver-compare.apl) | مقارنة إصدارات دلالية semver |
| 568 | [`568-template-mini.apl`](../examples/568-template-mini.apl) | محرك قوالب مصغر بمتغيرات {{اسم}} |
| 569 | [`569-game-2048.apl`](../examples/569-game-2048.apl) | منطق دمج 2048: انزلاق ودمج صف |
| 570 | [`570-wordle-feedback.apl`](../examples/570-wordle-feedback.apl) | تقييم ووردل: أخضر/أصفر/رمادي بمرورين |
| 571 | [`571-mastermind-score.apl`](../examples/571-mastermind-score.apl) | تقييم ماسترمايند: دقيق ولون فقط |
| 572 | [`572-median-stream.apl`](../examples/572-median-stream.apl) | وسيط تدفق بكوميتين (أدنى وأقصى) |
| 573 | [`573-tarjan-scc.apl`](../examples/573-tarjan-scc.apl) | خوارزمية تارجان للمكونات القوية في رسم موجه |
| 574 | [`574-maze-bfs.apl`](../examples/574-maze-bfs.apl) | أقصر طريق في متاهة نصية مع جدران |
| 575 | [`575-suffix-array.apl`](../examples/575-suffix-array.apl) | مصفوفة السوابق والبحث فيها |
| 576 | [`576-longest-common-substring.apl`](../examples/576-longest-common-substring.apl) | أطول سلسلة فرعية مشتركة بين نصين |
| 577 | [`577-min-window-substring.apl`](../examples/577-min-window-substring.apl) | أصغر نافذة تحوي كل أحرف نمط |
| 578 | [`578-group-anagrams.apl`](../examples/578-group-anagrams.apl) | تجميع الكلمات المتناقضة الأحرف |
| 579 | [`579-jaro-winkler.apl`](../examples/579-jaro-winkler.apl) | مقياس تشابه الأسماء جارو-وينكلر |
| 580 | [`580-k-way-merge.apl`](../examples/580-k-way-merge.apl) | دمج عدة قوائم مرتبة بكومة |
| 581 | [`581-spiral-matrix.apl`](../examples/581-spiral-matrix.apl) | قراءة مصفوفة بالترتيب الحلزوني |
| 582 | [`582-rotate-matrix.apl`](../examples/582-rotate-matrix.apl) | تدوير مصفوفة 90 درجة |
| 583 | [`583-partition-subset-dp.apl`](../examples/583-partition-subset-dp.apl) | تقسيم مجموعة إلى نصفين متساويين |
| 584 | [`584-unbounded-knapsack.apl`](../examples/584-unbounded-knapsack.apl) | حقيبة الظهر غير المحدودة العناصر |
| 585 | [`585-bitmask-tsp.apl`](../examples/585-bitmask-tsp.apl) | أقصر جولة تزور كل المدن بأقنعة البتات |
| 586 | [`586-sqrt-decomposition.apl`](../examples/586-sqrt-decomposition.apl) | مجاميع المدى بتحليل الجذر التربيعي |
| 587 | [`587-circular-buffer.apl`](../examples/587-circular-buffer.apl) | مخزن دائري يكتب فوق الأقدم |
| 588 | [`588-lfu-cache.apl`](../examples/588-lfu-cache.apl) | ذاكرة مؤقتة تطرد الأقل استخداما |
| 589 | [`589-pollard-rho.apl`](../examples/589-pollard-rho.apl) | تحليل عدد إلى عوامل بطريقة بولارد-رو |
| 590 | [`590-linear-diophantine.apl`](../examples/590-linear-diophantine.apl) | حل معادلة ديوفانتية خطية بإقليدس الموسعة |
| 591 | [`591-stirling-digits.apl`](../examples/591-stirling-digits.apl) | عدد أرقام المضروب باللوغاريتمات دون حسابه |
| 592 | [`592-matrix-exponentiation.apl`](../examples/592-matrix-exponentiation.apl) | تريبوناتشي برفع مصفوفة لقوة |
| 593 | [`593-qibla-bearing.apl`](../examples/593-qibla-bearing.apl) | اتجاه القبلة من القاهرة بحساب كروي |
| 594 | [`594-cairo-metro-fare.apl`](../examples/594-cairo-metro-fare.apl) | تذكرة مترو القاهرة بعدد المحطات (تعريفة مبسطة) |
| 595 | [`595-egypt-income-tax.apl`](../examples/595-egypt-income-tax.apl) | ضريبة الدخل المصرية بشرائح تصاعدية تقريبية |
| 596 | [`596-consistent-hashing.apl`](../examples/596-consistent-hashing.apl) | توزيع مفاتيح مستقر على عقد متغيرة |
| 597 | [`597-bridges-articulation.apl`](../examples/597-bridges-articulation.apl) | كشف الحواف والعقد الحرجة في رسم غير موجه |
| 598 | [`598-euler-path.apl`](../examples/598-euler-path.apl) | مسار يعبر كل حافة مرة واحدة |
| 599 | [`599-manacher.apl`](../examples/599-manacher.apl) | أطول سلسلة متناظرة بخوارزمية ماناكر |
| 600 | [`600-lz77-lite.apl`](../examples/600-lz77-lite.apl) | ضغط LZ77 المبسط وفك الضغط |
| 601 | [`601-avl-tree.apl`](../examples/601-avl-tree.apl) | شجرة بحث ذاتية الاتزان بالتدويرات |
| 602 | [`602-sparse-table.apl`](../examples/602-sparse-table.apl) | أدنى مدى بزمن ثابت بعد تجهيز |
| 603 | [`603-xor-trie.apl`](../examples/603-xor-trie.apl) | أقصى أو-حصري لزوج بشجرة بتات |
| 604 | [`604-knight-tour.apl`](../examples/604-knight-tour.apl) | جولة الحصان بقاعدة وارنسدورف |
| 605 | [`605-minesweeper-reveal.apl`](../examples/605-minesweeper-reveal.apl) | كشف متتال للخلايا الفارغة |
| 606 | [`606-minimax-ab.apl`](../examples/606-minimax-ab.apl) | لعب مثالي في إكس-أو بتقليم ألفا-بيتا |
| 607 | [`607-othello-flips.apl`](../examples/607-othello-flips.apl) | قانونية النقلة وقلب الأقراص |
| 608 | [`608-puzzle-15.apl`](../examples/608-puzzle-15.apl) | هل وضع لغز الخمسة عشر قابل للحل |
| 609 | [`609-card-war.apl`](../examples/609-card-war.apl) | محاكاة لعبة الحرب بالورق |
| 610 | [`610-snake-step.apl`](../examples/610-snake-step.apl) | حركة ونمو واصطدام الثعبان |
| 611 | [`611-sliding-log-limiter.apl`](../examples/611-sliding-log-limiter.apl) | تحديد المعدل بسجل طوابع منزلق |
| 612 | [`612-ttl-cache.apl`](../examples/612-ttl-cache.apl) | ذاكرة مؤقتة بمدة صلاحية |
| 613 | [`613-undo-stack.apl`](../examples/613-undo-stack.apl) | محرر بسجل تراجع وإعادة |
| 614 | [`614-event-bus.apl`](../examples/614-event-bus.apl) | نشر واشتراك بين مكونات منفصلة |
| 615 | [`615-cron-parser.apl`](../examples/615-cron-parser.apl) | موعد الرنة التالية لجدول كرون |
| 616 | [`616-prayer-times-lite.apl`](../examples/616-prayer-times-lite.apl) | مواقيت الصلاة التقريبية للقاهرة بحساب شمسي |
| 617 | [`617-hijri-calendar-print.apl`](../examples/617-hijri-calendar-print.apl) | طباعة شهر هجري كشبكة أسابيع |
| 618 | [`618-ramadan-countdown.apl`](../examples/618-ramadan-countdown.apl) | أيام متبقية لرمضان بالتقويم الاصطلاحي |
| 619 | [`619-tafqeet.apl`](../examples/619-tafqeet.apl) | تحويل المبلغ إلى كلمات عربية |
| 620 | [`620-skip-list.apl`](../examples/620-skip-list.apl) | بحث سريع في قائمة مرتبة بمستويات |
| 621 | [`621-convex-hull-graham.apl`](../examples/621-convex-hull-graham.apl) | أصغر مضلع محدب يحوي النقاط |
| 622 | [`622-closest-pair.apl`](../examples/622-closest-pair.apl) | أقرب زوج نقاط بالفرز والفحص |
| 623 | [`623-point-in-polygon.apl`](../examples/623-point-in-polygon.apl) | هل النقطة داخل المضلع بقذف شعاع |
| 624 | [`624-line-intersection.apl`](../examples/624-line-intersection.apl) | تقاطع القطع المستقيمة باختبارات الاتجاه |
| 625 | [`625-karatsuba.apl`](../examples/625-karatsuba.apl) | ضرب الأعداد الكبيرة بتقسيم أسرع |
| 626 | [`626-crc32.apl`](../examples/626-crc32.apl) | مجموع CRC32 الاختباري بت بت |
| 627 | [`627-hamming-ecc.apl`](../examples/627-hamming-ecc.apl) | شفرة هامنغ (7,4) لتصحيح خطأ أحادي البت |
| 628 | [`628-glob-match.apl`](../examples/628-glob-match.apl) | مطابقة أنماط glob النجمة والاستفهام |
| 629 | [`629-regex-nfa-lite.apl`](../examples/629-regex-nfa-lite.apl) | محرك نمطية مصغر بحرف ونقطة ونجمة |
| 630 | [`630-json-parser.apl`](../examples/630-json-parser.apl) | محلل JSON مصغر من الصفر |
| 631 | [`631-bytecode-vm.apl`](../examples/631-bytecode-vm.apl) | آلة افتراضية كومة مصغرة |
| 632 | [`632-allocator-first-fit.apl`](../examples/632-allocator-first-fit.apl) | محاكي تخصيص ذاكرة بأول ملائم ودمج |
| 633 | [`633-merkle-tree.apl`](../examples/633-merkle-tree.apl) | إثبات سلامة البيانات بشجرة تجزئة |
| 634 | [`634-leader-election-bully.apl`](../examples/634-leader-election-bully.apl) | انتخاب قائد بخوارزمية التنمر |
| 635 | [`635-vector-clock.apl`](../examples/635-vector-clock.apl) | ترتيب الأحداث الموزعة بالساعات المتجهة |
| 636 | [`636-banker-algorithm.apl`](../examples/636-banker-algorithm.apl) | كشف الحالة الآمنة من الجمود |
| 637 | [`637-page-replacement.apl`](../examples/637-page-replacement.apl) | إحلال الصفحات FIFO والأمثل |
| 638 | [`638-disk-scan.apl`](../examples/638-disk-scan.apl) | جدولة القرص بخوارزمية المصعد |
| 639 | [`639-round-robin.apl`](../examples/639-round-robin.apl) | جدولة المعالج بالتناوب الدائري |
| 640 | [`640-dining-philosophers.apl`](../examples/640-dining-philosophers.apl) | تجنب الجمود بترتيب الموارد |
| 641 | [`641-faraid-lite.apl`](../examples/641-faraid-lite.apl) | الأنصبة الشرعية الثابتة المبسطة |
| 642 | [`642-arabic-light-stemmer.apl`](../examples/642-arabic-light-stemmer.apl) | تجذيع عربي خفيف بقص السوابق واللواحق |
| 643 | [`643-cairo-taxi-fare.apl`](../examples/643-cairo-taxi-fare.apl) | عداد التاكسي الأبيض بالقاهرة (تقريبي) |
| 644 | [`644-electricity-bill-egypt.apl`](../examples/644-electricity-bill-egypt.apl) | فاتورة كهرباء منزلية بشرائح (تقريبية) |
| 645 | [`645-b-tree-insert.apl`](../examples/645-b-tree-insert.apl) | إدخال في شجرة ب مع انقسام العقد الممتلئة |
| 646 | [`646-treap.apl`](../examples/646-treap.apl) | شجرة بحث متوازنة بأولويات كومة مشتقة |
| 647 | [`647-lca-binary-lifting.apl`](../examples/647-lca-binary-lifting.apl) | أدنى سلف مشترك بجداول قوى اثنين |
| 648 | [`648-mo-algorithm.apl`](../examples/648-mo-algorithm.apl) | إجابة استعلامات المدى بإعادة ترتيبها |
| 649 | [`649-meet-in-middle.apl`](../examples/649-meet-in-middle.apl) | عد المجموعات الجزئية باللقاء في المنتصف |
| 650 | [`650-gray-code.apl`](../examples/650-gray-code.apl) | تتابع ثنائي يختلف في بت واحد |
| 651 | [`651-bit-tricks.apl`](../examples/651-bit-tricks.apl) | حيل البتات الشائعة بالإزاحات والأقنعة |
| 652 | [`652-reservoir-sampling.apl`](../examples/652-reservoir-sampling.apl) | عينة عادلة ثابتة الحجم من تيار |
| 653 | [`653-weighted-random.apl`](../examples/653-weighted-random.apl) | اختيار عشوائي باحتمال يتناسب مع الوزن |
| 654 | [`654-count-min-sketch.apl`](../examples/654-count-min-sketch.apl) | تقدير تكرارات بذاكرة ثابتة |
| 655 | [`655-bresenham-line.apl`](../examples/655-bresenham-line.apl) | رسم خط مستقيم على شبكة بلا فاصلة عائمة |
| 656 | [`656-iterative-deepening.apl`](../examples/656-iterative-deepening.apl) | بحث يجد أضحل حل بذاكرة البحث العميق |
| 657 | [`657-suffix-automaton.apl`](../examples/657-suffix-automaton.apl) | بنية مدمجة لكل النصوص الفرعية |
| 658 | [`658-damerau-levenshtein.apl`](../examples/658-damerau-levenshtein.apl) | مسافة تحرير مع تبديل الحروف المتجاورة |
| 659 | [`659-arabic-number-parse.apl`](../examples/659-arabic-number-parse.apl) | قراءة الأرقام المشرقية ٠١٢٣ كأعداد |
| 660 | [`660-arabic-sort-collation.apl`](../examples/660-arabic-sort-collation.apl) | ترتيب الأسماء بالهجائية العربية |
| 661 | [`661-coptic-calendar.apl`](../examples/661-coptic-calendar.apl) | تحويل التواريخ من وإلى التقويم القبطي |
| 662 | [`662-kalman-lite.apl`](../examples/662-kalman-lite.apl) | دمج قياسات مزعجة في تقدير مستقر |
| 663 | [`663-pid-controller.apl`](../examples/663-pid-controller.apl) | متحكم نسبي تكاملي تفاضلي على نظام محاكى |
| 664 | [`664-shamir-secret.apl`](../examples/664-shamir-secret.apl) | تقسيم سر على حصص لا تكفي بعضها وحدها |
| 665 | [`665-bidirectional-bfs.apl`](../examples/665-bidirectional-bfs.apl) | أقصر طريق بجبهتين متعاكستين |
| 666 | [`666-zero-one-bfs.apl`](../examples/666-zero-one-bfs.apl) | أقصر تكلفة بأوزان صفر وواحد |
| 667 | [`667-mcts-lite.apl`](../examples/667-mcts-lite.apl) | معادلة الاختيار التي تقود بحث مونت كارلو |
| 668 | [`668-simulated-annealing-tsp.apl`](../examples/668-simulated-annealing-tsp.apl) | تحسين جولة مندوب السفر بالتلدين المحاكى |
| 669 | [`669-max-flow-ford-fulkerson.apl`](../examples/669-max-flow-ford-fulkerson.apl) | أقصى تدفق في شبكة بمسارات معززة |
| 670 | [`670-hungarian-lite.apl`](../examples/670-hungarian-lite.apl) | إسناد عامل لمهمة بأقل كلفة إجمالية |
| 671 | [`671-hyperloglog-lite.apl`](../examples/671-hyperloglog-lite.apl) | تقدير عدد العناصر المميزة بذاكرة ثابتة |
| 672 | [`672-lz78.apl`](../examples/672-lz78.apl) | ضغط وفك بقاموس عبارات متنام |
| 673 | [`673-arithmetic-coding-lite.apl`](../examples/673-arithmetic-coding-lite.apl) | ترميز رسالة ككسر في مدى احتمالي |
| 674 | [`674-rsa-toy.apl`](../examples/674-rsa-toy.apl) | توليد مفاتيح وتشفير RSA بأعداد صغيرة |
| 675 | [`675-diffie-hellman-toy.apl`](../examples/675-diffie-hellman-toy.apl) | اشتقاق سر مشترك عبر قناة علنية |
| 676 | [`676-chacha-quarter-round.apl`](../examples/676-chacha-quarter-round.apl) | العملية الأساسية في تشفير تشاتشا |
| 677 | [`677-easter-computus.apl`](../examples/677-easter-computus.apl) | تاريخ عيد الفصح الغربي لأي سنة |
| 678 | [`678-hebrew-calendar-lite.apl`](../examples/678-hebrew-calendar-lite.apl) | تحويل تقريبي من وإلى التقويم العبري |
| 679 | [`679-smith-waterman.apl`](../examples/679-smith-waterman.apl) | أقوى تشابه جزئي بين تسلسلي DNA |
| 680 | [`680-moon-phase-lite.apl`](../examples/680-moon-phase-lite.apl) | هل الليلة محاق أم بدر من التاريخ وحده |
| 681 | [`681-game-of-life.apl`](../examples/681-game-of-life.apl) | مذبذب ونمط ساكن بقواعد كونواي |
| 682 | [`682-langton-ant.apl`](../examples/682-langton-ant.apl) | فوضى تتحول إلى طريق سريع دوري |
| 683 | [`683-rule-110.apl`](../examples/683-rule-110.apl) | أتمتة خلوية أولية كاملة حسابيا |
| 684 | [`684-sprague-grundy.apl`](../examples/684-sprague-grundy.apl) | تحليل الألعاب المحايدة بأرقام غروندي |
| 685 | [`685-poker-hand-eval-lite.apl`](../examples/685-poker-hand-eval-lite.apl) | تصنيف يد من خمس ورقات |
| 686 | [`686-fen-parse.apl`](../examples/686-fen-parse.apl) | قراءة موقف شطرنج بترميز فورسيث-إدواردز |
| 687 | [`687-verhoeff-checksum.apl`](../examples/687-verhoeff-checksum.apl) | رقم تحقق يكشف تبديل الخانات المتجاورة |
| 688 | [`688-brainfuck-interp.apl`](../examples/688-brainfuck-interp.apl) | مفسر كامل للغة براين فك المصغرة |
| 689 | [`689-lisp-eval-lite.apl`](../examples/689-lisp-eval-lite.apl) | حساب تعابير البادئة المتداخلة |
| 690 | [`690-toml-lite.apl`](../examples/690-toml-lite.apl) | قراءة ملفات إعداد بصيغة TOML |
| 691 | [`691-ical-rrule-lite.apl`](../examples/691-ical-rrule-lite.apl) | توليد مواعيد متكررة يوميا وأسبوعيا وشهريا |
| 692 | [`692-mandelbrot-ascii.apl`](../examples/692-mandelbrot-ascii.apl) | رسم مجموعة ماندلبروت بالأحرف |
| 693 | [`693-perlin-noise-1d.apl`](../examples/693-perlin-noise-1d.apl) | ضوضاء ناعمة بلا مولد عشوائي |
| 694 | [`694-bezier-curve.apl`](../examples/694-bezier-curve.apl) | تقييم منحنيات بيزييه التربيعية والتكعيبية |
| 695 | [`695-catmull-rom.apl`](../examples/695-catmull-rom.apl) | منحنى يمر بكل نقاط التحكم |
| 696 | [`696-shoelace-area.apl`](../examples/696-shoelace-area.apl) | مساحة ومحيط مضلع من رؤوسه |
| 697 | [`697-circle-circle-intersection.apl`](../examples/697-circle-circle-intersection.apl) | نقاط تلاقي دائرتين وحالاتها الخاصة |
| 698 | [`698-kmeans-1d.apl`](../examples/698-kmeans-1d.apl) | تجميع نقاط على الخط في عنقودين |
| 699 | [`699-gradient-descent-1d.apl`](../examples/699-gradient-descent-1d.apl) | إيجاد أدنى دالة تربيعية بالنزول |
| 700 | [`700-perceptron-lite.apl`](../examples/700-perceptron-lite.apl) | أبسط عصبون يتعلم بوابة منطقية |
| 701 | [`701-julian-day-number.apl`](../examples/701-julian-day-number.apl) | حسابات التواريخ بالأرقام المطلقة |
| 702 | [`702-wav-header-parse.apl`](../examples/702-wav-header-parse.apl) | قراءة حقول ملف صوتي من بايتاته |
| 703 | [`703-bmp-ascii-render.apl`](../examples/703-bmp-ascii-render.apl) | تحويل بكسلات نقطية إلى فن نصي |
| 704 | [`704-maze-wilson.apl`](../examples/704-maze-wilson.apl) | متاهة مثالية بتوزيع منتظم |
| 705 | [`705-datalog-lite.apl`](../examples/705-datalog-lite.apl) | استنتاج علاقات السلف بالإغلاق المتعدي |
| 706 | [`706-prolog-unify-lite.apl`](../examples/706-prolog-unify-lite.apl) | مطابقة الحدود بالتوحيد |
| 707 | [`707-dpll-sat-lite.apl`](../examples/707-dpll-sat-lite.apl) | إشباع صيغ منطقية بالتقسيم |
| 708 | [`708-expectimax-lite.apl`](../examples/708-expectimax-lite.apl) | قرارات مثلى تحت عدم اليقين |
| 709 | [`709-pagerank-lite.apl`](../examples/709-pagerank-lite.apl) | ترتيب صفحات ويب بأهميتها |
| 710 | [`710-astar-grid.apl`](../examples/710-astar-grid.apl) | أقصر طريق حول العوائق |
| 711 | [`711-tf-idf-lite.apl`](../examples/711-tf-idf-lite.apl) | أهم كلمات مستند ضمن مجموعة |
| 712 | [`712-tashkeel-strip.apl`](../examples/712-tashkeel-strip.apl) | تنظيف النص العربي من الحركات |
| 713 | [`713-stopword-filter-ar.apl`](../examples/713-stopword-filter-ar.apl) | حذف الكلمات الشائعة قبل البحث |
| 714 | [`714-sentence-split-ar.apl`](../examples/714-sentence-split-ar.apl) | تقطيع النص إلى جمل بقواعد |
| 715 | [`715-soundex-en.apl`](../examples/715-soundex-en.apl) | رمز صوتي للأسماء الإنجليزية |
| 716 | [`716-iso-week-date.apl`](../examples/716-iso-week-date.apl) | سنة الأسبوع ورقمه ويومه |
| 717 | [`717-murmur-lite.apl`](../examples/717-murmur-lite.apl) | هاش 32-بت غير تشفيري للسلاسل |
| 718 | [`718-pearson-hash.apl`](../examples/718-pearson-hash.apl) | هاش 8-بت بجدول تبديل ثابت |
| 719 | [`719-adler32.apl`](../examples/719-adler32.apl) | مجموع فحص سريع للبيانات |
| 720 | [`720-fletcher16.apl`](../examples/720-fletcher16.apl) | كشف أخطاء بمجموعين متعاقبين |
| 721 | [`721-crc16-modbus.apl`](../examples/721-crc16-modbus.apl) | فحص دوري لبروتوكول مودباس |
| 722 | [`722-base58-codec.apl`](../examples/722-base58-codec.apl) | ترميز بيتكوين النصي وفكه |
| 723 | [`723-varint-protobuf.apl`](../examples/723-varint-protobuf.apl) | أعداد صحيحة متغيرة الطول |
| 724 | [`724-zigzag-encoding.apl`](../examples/724-zigzag-encoding.apl) | سالب وموجب بأعداد موجبة صغيرة |
| 725 | [`725-utf8-decode-manual.apl`](../examples/725-utf8-decode-manual.apl) | قراءة حروف يونيكود من بايتاتها |
| 726 | [`726-utf16-surrogates.apl`](../examples/726-utf16-surrogates.apl) | حروف فوق U+FFFF بوحدتين |
| 727 | [`727-punycode-lite.apl`](../examples/727-punycode-lite.apl) | أسماء نطاقات دولية بأحرف ASCII |
| 728 | [`728-phone-t9.apl`](../examples/728-phone-t9.apl) | كتابة نص بلوحة هاتف قديمة |
| 729 | [`729-braille-lite.apl`](../examples/729-braille-lite.apl) | تحويل نص إلى خلايا برايل |
| 730 | [`730-resistor-color-code.apl`](../examples/730-resistor-color-code.apl) | قراءة قيم مقاومة من ألوانها |
| 731 | [`731-dna-transcribe.apl`](../examples/731-dna-transcribe.apl) | تحويل تسلسل جيني ومكمله العكسي |
| 732 | [`732-gc-content.apl`](../examples/732-gc-content.apl) | قياس غنى قواعد DNA |
| 733 | [`733-fasta-parse.apl`](../examples/733-fasta-parse.apl) | قراءة ملفات تسلسل جينية |
| 734 | [`734-protein-mass.apl`](../examples/734-protein-mass.apl) | كتلة بروتين من أحماضه الأمينية |
| 735 | [`735-hebrew-numerals.apl`](../examples/735-hebrew-numerals.apl) | كتابة الأعداد بالحروف العبرية |
| 736 | [`736-chinese-numerals.apl`](../examples/736-chinese-numerals.apl) | كتابة الأعداد بالحروف الصينية |
| 737 | [`737-babylonian-numerals.apl`](../examples/737-babylonian-numerals.apl) | النظام الستيني للأعداد |
| 738 | [`738-simpson-integrate.apl`](../examples/738-simpson-integrate.apl) | تكامل عددي دقيق للدوال |
| 739 | [`739-horner-eval.apl`](../examples/739-horner-eval.apl) | تقييم كثيرات الحدود ومشتقاتها |
| 740 | [`740-golomb-coding.apl`](../examples/740-golomb-coding.apl) | ضغط الأعداد الصحيحة الموجبة |
| 741 | [`741-hmac-manual.apl`](../examples/741-hmac-manual.apl) | بناء HMAC من تجزئة SHA-256 (RFC 2104) |
| 742 | [`742-hkdf-lite.apl`](../examples/742-hkdf-lite.apl) | اشتقاق مفاتيح من مادة أولية (RFC 5869) |
| 743 | [`743-otp-hotp-lite.apl`](../examples/743-otp-hotp-lite.apl) | رموز HOTP من مفتاح وعداد |
| 744 | [`744-aes-sbox-lite.apl`](../examples/744-aes-sbox-lite.apl) | اشتقاق جدول S-Box رياضياً |
| 745 | [`745-xor-cipher-break.apl`](../examples/745-xor-cipher-break.apl) | كسر تشفير XOR بتحليل التكرار |
| 746 | [`746-vigenere-break.apl`](../examples/746-vigenere-break.apl) | كسر فيجنير بطول مفتاح معلوم |
| 747 | [`747-playfair-lite.apl`](../examples/747-playfair-lite.apl) | تشفير ثنائي الحروف التاريخي |
| 748 | [`748-enigma-lite.apl`](../examples/748-enigma-lite.apl) | محاكاة إنجما I التاريخية |
| 749 | [`749-rail-fence.apl`](../examples/749-rail-fence.apl) | تبديل مواضع بقضبان متعرجة |
| 750 | [`750-greek-numerals.apl`](../examples/750-greek-numerals.apl) | النظام الأيوني للأرقام |
| 751 | [`751-mayan-numerals.apl`](../examples/751-mayan-numerals.apl) | النظام العشريني بالنقاط والأصابع |
| 752 | [`752-emoji-grapheme-split.apl`](../examples/752-emoji-grapheme-split.apl) | تقسيم نص لوحدات مرئية صحيحة |
| 753 | [`753-arabic-reshaper-lite.apl`](../examples/753-arabic-reshaper-lite.apl) | حروف عربية بأشكال العرض الأربعة |
| 754 | [`754-json-path-lite.apl`](../examples/754-json-path-lite.apl) | استعلام $.a.b[0] عن بنى متداخلة |
| 755 | [`755-tokenizer-ar-lite.apl`](../examples/755-tokenizer-ar-lite.apl) | كلمات وأرقام وعلامات من نص عربي |
| 756 | [`756-keyboard-dvorak-lite.apl`](../examples/756-keyboard-dvorak-lite.apl) | تحويل QWERTY ودفوراك وكفاءتهما |
| 757 | [`757-quaternion-rotate.apl`](../examples/757-quaternion-rotate.apl) | تدوير متجهات ثلاثية الأبعاد |
| 758 | [`758-sun-position-lite.apl`](../examples/758-sun-position-lite.apl) | ارتفاع الشمس من اليوم وخط العرض |
| 759 | [`759-fastq-parse.apl`](../examples/759-fastq-parse.apl) | تسلسلات مع درجات جودة |
| 760 | [`760-newick-parse.apl`](../examples/760-newick-parse.apl) | أشجار تطور نصية |
| 761 | [`761-codon-table.apl`](../examples/761-codon-table.apl) | ترجمة DNA إلى بروتين |
| 762 | [`762-upgma-tree.apl`](../examples/762-upgma-tree.apl) | شجرة تطور من مصفوفة مسافات |
| 763 | [`763-boggle-solver.apl`](../examples/763-boggle-solver.apl) | كلمات من شبكة حروف متجاورة |
| 764 | [`764-fft-butterfly-lite.apl`](../examples/764-fft-butterfly-lite.apl) | تحويل فورييه السريع يدوياً |
| 765 | [`765-rc4-cipher.apl`](../examples/765-rc4-cipher.apl) | تشفير تدفقي بجدول تبديل 256 بايت |
| 766 | [`766-tea-cipher.apl`](../examples/766-tea-cipher.apl) | شبكة فيستل صغيرة بمفتاح 128-بت |
| 767 | [`767-affine-cipher.apl`](../examples/767-affine-cipher.apl) | شفرة أحادية الأبجدية الخطية |
| 768 | [`768-hill-cipher.apl`](../examples/768-hill-cipher.apl) | تشفير أزواج الحروف بمصفوفة |
| 769 | [`769-sha1-manual.apl`](../examples/769-sha1-manual.apl) | بناء SHA-1 من المواصفة |
| 770 | [`770-poly1305-lite.apl`](../examples/770-poly1305-lite.apl) | مصادقة رسائل (RFC 8439) |
| 771 | [`771-bech32-lite.apl`](../examples/771-bech32-lite.apl) | ترميز BIP 173 مع مجموع تحقق |
| 772 | [`772-fibonacci-coding.apl`](../examples/772-fibonacci-coding.apl) | شفرة أعداد ذاتية الفصل |
| 773 | [`773-elias-gamma.apl`](../examples/773-elias-gamma.apl) | شفرة عالمية للأعداد الصحيحة |
| 774 | [`774-natural-sort.apl`](../examples/774-natural-sort.apl) | img2 يأتي قبل img10 |
| 775 | [`775-fuzzy-search.apl`](../examples/775-fuzzy-search.apl) | ترتيب مرشحين بأسلوب fzf |
| 776 | [`776-bm25-lite.apl`](../examples/776-bm25-lite.apl) | ترتيب مستندات لاستعلام بحث |
| 777 | [`777-plural-ar.apl`](../examples/777-plural-ar.apl) | صيغ العدد: مفرد ومثنى وجمع |
| 778 | [`778-needleman-wunsch.apl`](../examples/778-needleman-wunsch.apl) | محاذاة تسلسلين من الطرف للطرف |
| 779 | [`779-forth-lite.apl`](../examples/779-forth-lite.apl) | مفسر لغة مكدسية مصغر |
| 780 | [`780-turing-machine.apl`](../examples/780-turing-machine.apl) | محاكاة آلة تورينغ: جمع أحادي |
| 781 | [`781-l-system.apl`](../examples/781-l-system.apl) | توليد نصوص الطحالب وكوخ |
| 782 | [`782-magic-square.apl`](../examples/782-magic-square.apl) | مربعات سحرية فردية الرتبة |
| 783 | [`783-dragon-curve.apl`](../examples/783-dragon-curve.apl) | متتالية منحنى التنين |
| 784 | [`784-z-order-curve.apl`](../examples/784-z-order-curve.apl) | ترميز مورتون للإحداثيات |
| 785 | [`785-turtle-graphics.apl`](../examples/785-turtle-graphics.apl) | رسم بأوامر F وR وL |
| 786 | [`786-business-days.apl`](../examples/786-business-days.apl) | حساب أيام العمل مع العطلات |
| 787 | [`787-ipv4-cidr.apl`](../examples/787-ipv4-cidr.apl) | تحليل عناوين وشبكات فرعية |
| 788 | [`788-genetic-algorithm.apl`](../examples/788-genetic-algorithm.apl) | حل Ones-Max بالتطور الصناعي |
| 789 | [`789-lfsr-prng.apl`](../examples/789-lfsr-prng.apl) | مسجل إزاحة بخطي راجع 16-بت |
| 790 | [`790-blum-blum-shub.apl`](../examples/790-blum-blum-shub.apl) | مولد عشوائي آمن نظرياً |
| 791 | [`791-xxhash-lite.apl`](../examples/791-xxhash-lite.apl) | تجزية غير تشفيرية سريعة |
| 792 | [`792-polybius-square.apl`](../examples/792-polybius-square.apl) | شفرة الإحداثيات اليونانية |
| 793 | [`793-nihilist-cipher.apl`](../examples/793-nihilist-cipher.apl) | شفرة بوليبيوس بمفتاح دوري |
| 794 | [`794-dct-lite.apl`](../examples/794-dct-lite.apl) | تحويل JPEG الترددي مباشرة |
| 795 | [`795-elgamal-toy.apl`](../examples/795-elgamal-toy.apl) | تشفير بمفتاح عام تعليمي |
| 796 | [`796-reed-solomon.apl`](../examples/796-reed-solomon.apl) | تصحيح أخطاء بحذف وإتلاف |
| 797 | [`797-quoted-printable.apl`](../examples/797-quoted-printable.apl) | ترميز بريد RFC 2045 |
| 798 | [`798-base85-codec.apl`](../examples/798-base85-codec.apl) | ترميز ثنائي-نصي كثيف |
| 799 | [`799-justify-text.apl`](../examples/799-justify-text.apl) | ضبط كامل بعرض ثابت |
| 800 | [`800-hex-dump.apl`](../examples/800-hex-dump.apl) | عارض بايتات بأسلوب hexdump |
| 801 | [`801-printf-format.apl`](../examples/801-printf-format.apl) | تنسيق نصوص بأسلوب C |
| 802 | [`802-shunting-yard.apl`](../examples/802-shunting-yard.apl) | من infix إلى postfix وتقييم |
| 803 | [`803-knn-classifier.apl`](../examples/803-knn-classifier.apl) | تصنيف بأقرب k جيران |
| 804 | [`804-naive-bayes.apl`](../examples/804-naive-bayes.apl) | تصنيف نصوص احتمالي |
| 805 | [`805-id3-tree.apl`](../examples/805-id3-tree.apl) | تعلم شجرة قرار من بيانات |
| 806 | [`806-discrete-log-bsgs.apl`](../examples/806-discrete-log-bsgs.apl) | حل اللوغاريتم بجذر تربيعي |
| 807 | [`807-integer-partitions.apl`](../examples/807-integer-partitions.apl) | عد p(n) وتعديد التقسيمات |
| 808 | [`808-barcode-code39.apl`](../examples/808-barcode-code39.apl) | توليد باركود مع خانة تحقق |
| 809 | [`809-pbm-image.apl`](../examples/809-pbm-image.apl) | صور نقطية بصيغة netpbm |
| 810 | [`810-ansi-color.apl`](../examples/810-ansi-color.apl) | تنسيق طرفية بالتسلسلات |
| 811 | [`811-hex-color.apl`](../examples/811-hex-color.apl) | نسبة تباين WCAG من hex |
| 812 | [`812-nim-game.apl`](../examples/812-nim-game.apl) | استراتيجية نيم المثلى |
| 813 | [`813-md5-manual.apl`](../examples/813-md5-manual.apl) | بناء MD5 من المواصفة |
| 814 | [`814-adfgvx.apl`](../examples/814-adfgvx.apl) | شفرة ألمانيا في الحرب الأولى |
| 815 | [`815-columnar-transposition.apl`](../examples/815-columnar-transposition.apl) | شفرة نقل كلاسيكية |
| 816 | [`816-robin-hood-hashing.apl`](../examples/816-robin-hood-hashing.apl) | جدول تجزئة بتباين منخفض |
| 817 | [`817-baudot-code.apl`](../examples/817-baudot-code.apl) | ترميز التليكس التاريخي |
| 818 | [`818-bifid-cipher.apl`](../examples/818-bifid-cipher.apl) | شفرة تجزيئة بدون مفتاح |
| 819 | [`819-djb2-hash.apl`](../examples/819-djb2-hash.apl) | تجزية نصوص شهيرة |
| 820 | [`820-xorshift.apl`](../examples/820-xorshift.apl) | عشوائية سريعة بدون ضرب |
| 821 | [`821-splitmix.apl`](../examples/821-splitmix.apl) | مولد بذور عالي الجودة |
| 822 | [`822-pcg-lite.apl`](../examples/822-pcg-lite.apl) | عشوائية مبسطة عالية الجودة |
| 823 | [`823-zobrist-hashing.apl`](../examples/823-zobrist-hashing.apl) | تجزئة وضعيات اللعب |
| 824 | [`824-cuckoo-filter.apl`](../examples/824-cuckoo-filter.apl) | عضوية تقريبية قابلة للحذف |
| 825 | [`825-quasi-random-halton.apl`](../examples/825-quasi-random-halton.apl) | توليد شبه عشوائي متجانس |
| 826 | [`826-kosaraju.apl`](../examples/826-kosaraju.apl) | مكونات قوية الاتصال |
| 827 | [`827-gale-shapley.apl`](../examples/827-gale-shapley.apl) | مطابقة مستقرة مضمونة |
| 828 | [`828-bipartite-matching.apl`](../examples/828-bipartite-matching.apl) | أقصى تطابق بخوارزمية كون |
| 829 | [`829-hill-climbing.apl`](../examples/829-hill-climbing.apl) | تحسين محلي بسيط |
| 830 | [`830-tabu-search.apl`](../examples/830-tabu-search.apl) | هروب من الحلول المحلية |
| 831 | [`831-ant-colony-lite.apl`](../examples/831-ant-colony-lite.apl) | أقصر جولة بالاستعارة النملية |
| 832 | [`832-particle-swarm-lite.apl`](../examples/832-particle-swarm-lite.apl) | تحسين جماعي مستمر |
| 833 | [`833-runge-kutta.apl`](../examples/833-runge-kutta.apl) | تكامل ODE بدقة رابعة |
| 834 | [`834-bisection-method.apl`](../examples/834-bisection-method.apl) | إيجاد جذور الدوال |
| 835 | [`835-kolmogorov-smirnov.apl`](../examples/835-kolmogorov-smirnov.apl) | اختبار مطابقة التوزيع |
| 836 | [`836-splay-tree.apl`](../examples/836-splay-tree.apl) | شجرة ذاتية التعديل |
| 837 | [`837-lu-decomposition.apl`](../examples/837-lu-decomposition.apl) | تحليل المصفوفة لحل الأنظمة |
| 838 | [`838-cholesky-decomposition.apl`](../examples/838-cholesky-decomposition.apl) | تحليل متماثل أسرع من LU |
| 839 | [`839-gram-schmidt.apl`](../examples/839-gram-schmidt.apl) | بناء قاعدة متعامدة معيارية |
| 840 | [`840-gauss-jordan.apl`](../examples/840-gauss-jordan.apl) | حل أنظمة المعادلات الخطية |
| 841 | [`841-thomas-tridiagonal.apl`](../examples/841-thomas-tridiagonal.apl) | حل ثلاثي القطر في زمن خطي |
| 842 | [`842-sieve-of-atkin.apl`](../examples/842-sieve-of-atkin.apl) | غربال أولي حديث نظرياً |
| 843 | [`843-wheel-factorization.apl`](../examples/843-wheel-factorization.apl) | قسمة تجريبية مسرعة |
| 844 | [`844-twin-primes.apl`](../examples/844-twin-primes.apl) | حدسية غير مثبتة حتى اليوم |
| 845 | [`845-sophie-germain.apl`](../examples/845-sophie-germain.apl) | استخدمت في برهان فيرما |
| 846 | [`846-emirp.apl`](../examples/846-emirp.apl) | أولية مقلوبة غير متناظرة |
| 847 | [`847-semiprime.apl`](../examples/847-semiprime.apl) | أساس أمن RSA |
| 848 | [`848-amicable-numbers.apl`](../examples/848-amicable-numbers.apl) | 220 و284 منذ فيثاغورس |
| 849 | [`849-kaprekar-number.apl`](../examples/849-kaprekar-number.apl) | كل رباعي يصل إلى 6174 |
| 850 | [`850-vampire-number.apl`](../examples/850-vampire-number.apl) | 1260 = 21 في 60 |
| 851 | [`851-taxicab-number.apl`](../examples/851-taxicab-number.apl) | 1729 وحوار رامانوجان |
| 852 | [`852-abundant-numbers.apl`](../examples/852-abundant-numbers.apl) | أول وفيرة فردية هي 945 |
| 853 | [`853-trailing-zeros-factorial.apl`](../examples/853-trailing-zeros-factorial.apl) | أسرع من حساب المضروب |
| 854 | [`854-primorial.apl`](../examples/854-primorial.apl) | مضروب الأولية وبرهان إقليدس |
| 855 | [`855-gregory-pi.apl`](../examples/855-gregory-pi.apl) | أبسط متسلسلة لط |
| 856 | [`856-nilakantha-pi.apl`](../examples/856-nilakantha-pi.apl) | مئة حد لخمس خانات |
| 857 | [`857-machin-pi.apl`](../examples/857-machin-pi.apl) | حسبت ط لمئة خانة عام 1706 |
| 858 | [`858-aliquot-sequence.apl`](../examples/858-aliquot-sequence.apl) | مصائر: واحد أو كامل أو متحاب |
| 859 | [`859-recaman-sequence.apl`](../examples/859-recaman-sequence.apl) | متتابعة ذاتية المرجع |
| 860 | [`860-boyer-moore-search.apl`](../examples/860-boyer-moore-search.apl) | بحث نصي بقفزات طويلة |
| 861 | [`861-lucas-numbers.apl`](../examples/861-lucas-numbers.apl) | نظير فيبوناتشي بالنسبة الذهبية |
| 862 | [`862-pell-numbers.apl`](../examples/862-pell-numbers.apl) | تقارب النسبة الفضية |
| 863 | [`863-jacobsthal-numbers.apl`](../examples/863-jacobsthal-numbers.apl) | صيغة مغلقة بقوى اثنين |
| 864 | [`864-stirling-second.apl`](../examples/864-stirling-second.apl) | تكرارية k*S+S |
| 865 | [`865-bell-numbers.apl`](../examples/865-bell-numbers.apl) | عدد تقسيمات المجموعة |
| 866 | [`866-three-sum.apl`](../examples/866-three-sum.apl) | ثلاثيات صفرية فريدة |
| 867 | [`867-integral-image.apl`](../examples/867-integral-image.apl) | مجاميع مستطيلات في O(1) |
| 868 | [`868-difference-array.apl`](../examples/868-difference-array.apl) | تراكم مؤجل واحد |
| 869 | [`869-stein-gcd.apl`](../examples/869-stein-gcd.apl) | قاسم مشترك للعتاد |
| 870 | [`870-russian-peasant.apl`](../examples/870-russian-peasant.apl) | ضرب بلا جدول ضرب |
| 871 | [`871-gauss-seidel.apl`](../examples/871-gauss-seidel.apl) | حل تكراري للأنظمة |
| 872 | [`872-power-iteration.apl`](../examples/872-power-iteration.apl) | أكبر قيمة ذاتية |
| 873 | [`873-euler-method.apl`](../examples/873-euler-method.apl) | أبسط تكامل ODE |
| 874 | [`874-jarvis-march.apl`](../examples/874-jarvis-march.apl) | غلاف محدب بسيط |
| 875 | [`875-monty-hall.apl`](../examples/875-monty-hall.apl) | التبديل يفوز بثلثين |
| 876 | [`876-birthday-paradox.apl`](../examples/876-birthday-paradox.apl) | 23 تكفي لخمسين بالمئة |
| 877 | [`877-coupon-collector.apl`](../examples/877-coupon-collector.apl) | متوسط جمع الأنواع |
| 878 | [`878-farey-sequence.apl`](../examples/878-farey-sequence.apl) | خاصية الجارين bc-ad=1 |
| 879 | [`879-stern-brocot.apl`](../examples/879-stern-brocot.apl) | مسار L/R لكل كسر |
| 880 | [`880-lehmer-code.apl`](../examples/880-lehmer-code.apl) | رتبة التبديل في n! |
| 881 | [`881-damm-algorithm.apl`](../examples/881-damm-algorithm.apl) | يكشف الأخطاء والتبديلات |
| 882 | [`882-floyd-cycle.apl`](../examples/882-floyd-cycle.apl) | دورة بذاكرة ثابتة |
| 883 | [`883-balanced-ternary.apl`](../examples/883-balanced-ternary.apl) | تمثيل فريد للسالب والموجب |
| 884 | [`884-zeckendorf.apl`](../examples/884-zeckendorf.apl) | جشع فريد لكل عدد |
| 885 | [`885-thue-morse.apl`](../examples/885-thue-morse.apl) | خالية من التكرار الثلاثي |
| 886 | [`886-kolakoski.apl`](../examples/886-kolakoski.apl) | متتابعة مولدة لنفسها |
| 887 | [`887-hofstadter-q.apl`](../examples/887-hofstadter-q.apl) | تكرارية ميتافيبوناتشي |
| 888 | [`888-fusc-diatomic.apl`](../examples/888-fusc-diatomic.apl) | تعد شجرة كوكينس |
| 889 | [`889-motzkin-numbers.apl`](../examples/889-motzkin-numbers.apl) | تنعيم كاتالان بخطوة مستوية |
| 890 | [`890-schroder-numbers.apl`](../examples/890-schroder-numbers.apl) | تقارب ضعفي مع كاتالان |
| 891 | [`891-delannoy-numbers.apl`](../examples/891-delannoy-numbers.apl) | وسطاء المسارات القطرية |
| 892 | [`892-narayana-numbers.apl`](../examples/892-narayana-numbers.apl) | تنعيم كاتالان بعدد القمم |
| 893 | [`893-eulerian-numbers.apl`](../examples/893-eulerian-numbers.apl) | مجموع الصف مضروب ن |
| 894 | [`894-cantor-pairing.apl`](../examples/894-cantor-pairing.apl) | فك ببحث مثلثي ثنائي |
| 895 | [`895-cantor-set.apl`](../examples/895-cantor-set.apl) | عضوية في فراكتل |
| 896 | [`896-exponential-search.apl`](../examples/896-exponential-search.apl) | بحث في مصفوفة غير محدودة |
| 897 | [`897-fibonacci-search.apl`](../examples/897-fibonacci-search.apl) | لوصول غير متجانس الكلفة |
| 898 | [`898-move-to-front.apl`](../examples/898-move-to-front.apl) | ضغط يستغل التكرار الموضعي |
| 899 | [`899-distinct-subsequences.apl`](../examples/899-distinct-subsequences.apl) | عد بلا تكرار |
| 900 | [`900-lyndon-words.apl`](../examples/900-lyndon-words.apl) | أدنى من كل تدويراتها |
| 901 | [`901-minimal-rotation.apl`](../examples/901-minimal-rotation.apl) | مطابقة السلاسل الدائرية |
| 902 | [`902-shannon-entropy.apl`](../examples/902-shannon-entropy.apl) | متوسط المعلومة بالبت |
| 903 | [`903-kl-divergence.apl`](../examples/903-kl-divergence.apl) | بعد احتمالي غير متماثل |
| 904 | [`904-gini-coefficient.apl`](../examples/904-gini-coefficient.apl) | قياس عدم المساواة |
| 905 | [`905-kendall-tau.apl`](../examples/905-kendall-tau.apl) | ارتباط ترتيبي |
| 906 | [`906-skewness-kurtosis.apl`](../examples/906-skewness-kurtosis.apl) | قياس شكل التوزيع |
| 907 | [`907-negabinary.apl`](../examples/907-negabinary.apl) | سالب وموجب بلا بت إشارة |
| 908 | [`908-iqr-outliers.apl`](../examples/908-iqr-outliers.apl) | فرز ووسائط وربيعيات |
| 909 | [`909-dutch-national-flag.apl`](../examples/909-dutch-national-flag.apl) | فرز ثلاثي في مكانه |
| 910 | [`910-cycle-sort.apl`](../examples/910-cycle-sort.apl) | أقل كتابات ممكنة |
| 911 | [`911-sliding-window-maximum.apl`](../examples/911-sliding-window-maximum.apl) | كل عنصر يعالج مرة |
| 912 | [`912-longest-increasing-subsequence.apl`](../examples/912-longest-increasing-subsequence.apl) | طول في n log n |
| 913 | [`913-lru-cache.apl`](../examples/913-lru-cache.apl) | إخلاء الأقدم عند الامتلاء |
| 914 | [`914-hyperloglog.apl`](../examples/914-hyperloglog.apl) | عد تقريبي بذاكرة ثابتة |
| 915 | [`915-bipartite-check.apl`](../examples/915-bipartite-check.apl) | لا جارين بلون واحد |
| 916 | [`916-bridges.apl`](../examples/916-bridges.apl) | أضلاع حذفها يفصل |
| 917 | [`917-matrix-chain.apl`](../examples/917-matrix-chain.apl) | أقل عدد عمليات |
| 918 | [`918-recaman.apl`](../examples/918-recaman.apl) | قفزات بحجم الموضع |
| 919 | [`919-van-eck.apl`](../examples/919-van-eck.apl) | صفر للجديد |
| 920 | [`920-egyptian-fraction.apl`](../examples/920-egyptian-fraction.apl) | تمثيل قديم للكسور |
| 921 | [`921-continued-fraction.apl`](../examples/921-continued-fraction.apl) | أفضل تقريب كسري |
| 922 | [`922-kaprekar.apl`](../examples/922-kaprekar.apl) | كل رباعي يبلغ 6174 |
| 923 | [`923-huffman.apl`](../examples/923-huffman.apl) | شيفرات مثلى بلا بادئة |
| 924 | [`924-lz77.apl`](../examples/924-lz77.apl) | أساس ZIP و gzip |
| 925 | [`925-base64.apl`](../examples/925-base64.apl) | أبجدية 64 قابلة للطباعة |
| 926 | [`926-varint.apl`](../examples/926-varint.apl) | أعداد صغيرة ببايتات أقل |
| 927 | [`927-kmeans.apl`](../examples/927-kmeans.apl) | تقسيم نقاط لمجموعات |
| 928 | [`928-logistic-regression.apl`](../examples/928-logistic-regression.apl) | تصنيف ثنائي احتمالي |
| 929 | [`929-median-of-medians.apl`](../examples/929-median-of-medians.apl) | اختيار خطي بأسوأ حالة |
| 930 | [`930-golden-section.apl`](../examples/930-golden-section.apl) | تقليل بلا مشتقات |
| 931 | [`931-soundex.apl`](../examples/931-soundex.apl) | أسماء متشابهة الصوت |
| 932 | [`932-jaro-winkler.apl`](../examples/932-jaro-winkler.apl) | قياس تقارب الأسماء |
| 933 | [`933-kmp.apl`](../examples/933-kmp.apl) | بحث بلا رجوع في النص |
| 934 | [`934-longest-common-subsequence.apl`](../examples/934-longest-common-subsequence.apl) | أساس diff الحيوي |
| 935 | [`935-regex-matcher.apl`](../examples/935-regex-matcher.apl) | مطابقة نمط كامل |
| 936 | [`936-arithmetic-coding.apl`](../examples/936-arithmetic-coding.apl) | سلسلة كاملة في كسر |
| 937 | [`937-lzw.apl`](../examples/937-lzw.apl) | أساس GIF |
| 938 | [`938-bitonic-sort.apl`](../examples/938-bitonic-sort.apl) | فرز قابل للتوازي |
| 939 | [`939-pancake-sort.apl`](../examples/939-pancake-sort.apl) | قلبتان لكل عنصر |
| 940 | [`940-cholesky.apl`](../examples/940-cholesky.apl) | للموجبة التعريف |
| 941 | [`941-simpson-rule.apl`](../examples/941-simpson-rule.apl) | تكامل بقطع مكافئ |
| 942 | [`942-dft.apl`](../examples/942-dft.apl) | من الزمن للتردد |
| 943 | [`943-haar-wavelet.apl`](../examples/943-haar-wavelet.apl) | أبسط تحويل مويجي |
| 944 | [`944-kalman.apl`](../examples/944-kalman.apl) | دمج قياسات مضججة |
| 945 | [`945-lucas-theorem.apl`](../examples/945-lucas-theorem.apl) | C(n,k) مودولو أولي |
| 946 | [`946-primitive-root.apl`](../examples/946-primitive-root.apl) | مولد مودولو أولي |
| 947 | [`947-shamir.apl`](../examples/947-shamir.apl) | ك حصة تكفي وأقل لا |
| 948 | [`948-hamming-code.apl`](../examples/948-hamming-code.apl) | تصحيح خطأ واحد |
| 949 | [`949-rule-30.apl`](../examples/949-rule-30.apl) | فوضى من قاعدة بسيطة |
| 950 | [`950-maze-generation.apl`](../examples/950-maze-generation.apl) | متاهة مثالية بشجرة |
| 951 | [`951-sudoku.apl`](../examples/951-sudoku.apl) | صف وعمود وصندوق |
| 952 | [`952-interval-scheduling.apl`](../examples/952-interval-scheduling.apl) | أكبر عدد مهام متوافقة |
| 953 | [`953-egg-drop.apl`](../examples/953-egg-drop.apl) | محاولات مضمونة |
| 954 | [`954-tf-idf.apl`](../examples/954-tf-idf.apl) | أهمية مصطلح لوثيقة |
| 955 | [`955-segment-intersection.apl`](../examples/955-segment-intersection.apl) | جداء تبادلي بإشارات |
| 956 | [`956-lagrange.apl`](../examples/956-lagrange.apl) | كثير حدود مار بنقاط |

**التشغيل:**
```bash
python apl.py examples/01-calculator.apl
```

**الاختبار:** `python test_examples.py`

## الميزات الجديدة (v1.8)

### Context Managers (إدارة السياق)
```apl
# استخدام with عربي
اكتب("ملف.txt", "محتوى تجريبي\n")

مع فتح("ملف.txt") مثل f:
    اطبع f.read().strip()

# أو بالإنجليزي
with open("ملف.txt") as f:
    print(f.read().strip())

احذف_ملف("ملف.txt")
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

## المكتبات المتاحة (91 مكتبة)

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

**الإجمالي: 211,038 عنصراً في 91 مكتبة** (211,023 مفتاحاً فريداً بعد إزالة التكرار).

تشمل العناصر: الدوال، خصائص الكائنات، دوال الكائن المتسلسلة، الثوابت، والمعاملات العربية.
إضافة إلى 231 عنصراً في اللغة الأساسية (كلمات مفتاحية، أنواع، ثوابت، أنماط، دوال مضمّنة)
في `core/apl_runner/patterns.py`، فيصبح إجمالي العناصر العربية الفريدة **211,254 عنصراً**،
مع **956 مثال جاهز** في `examples/`.

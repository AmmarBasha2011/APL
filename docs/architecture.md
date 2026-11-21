# هيكل المشروع — APL

## الملفات والمجلدات

```
APL/
├── apl.py                   ← نقطة الدخول (للتشغيل فقط)
├── core/                    ← المحرك (لا تلمس)
│   ├── __init__.py
│   ├── apl_runner/           ← تشغيل الـ APL
│   │   ├── __init__.py
│   │   ├── main.py           ← CLI, REPL, Help
│   │   ├── patterns.py       ← الأنماط والترجمات
│   │   ├── inline_replacer.py ← الترجمة الـ Inline
│   │   └── transpiler.py     ← ترجمة الأسطر
│   └── libraries/            ← المكتبات
│       ├── __init__.py
│       ├── math_funcs.py     ← مكتبة math
│       ├── random_funcs.py   ← مكتبة random
│       ├── xml_funcs.py      ← مكتبة xml (ElementTree)
│       ├── archive_funcs.py  ← مكتبة archive (ZIP / TAR / ضغط)
│       ├── net_funcs.py      ← مكتبة net (socket / ssl / http / email)
│       ├── lazy.py           ← تحميل كسول للمكتبات
│       └── time_funcs.py     ← مكتبة time/datetime
├── examples/                ← 60 مثالاً جاهزاً تعمل فعلياً
│   ├── 01-calculator.apl
│   ├── 02-sales-report.apl
│   ├── 03-task-manager.apl
│   ├── 04-text-analyzer.apl
│   ├── 05-report-writer.apl
│   ├── 06-search-sort.apl
│   ├── 07-sqlite-tasks.apl
│   ├── 08-word-frequency.apl
│   ├── 09-encoding-hashing.apl
│   └── 10-file-manager.apl
└── docs/                    ← التوثيق
    ├── README.md
    ├── architecture.md
    ├── language-reference.md
    ├── math-library.md
    ├── random-library.md
    ├── xml-library.md
    ├── archive-library.md
    ├── time-library.md
    └── error-messages.md
```

## كيف يعمل APL؟

APL هو **ترانسبايلر** (مصدر إلى مصدر):

1. يقرأ الكود العربي
2. يستبدل الكلمات المفتاحية العربية بما يقابلها في Python
3. يكتشف المكتبات المطلوبة ويضيف `import` تلقائياً
4. ينفذ الكود Python الناتج

```
كود APL ──→ ترانسبايلر ──→ كود Python ──→ تنفيذ
```

## التصميم المعياري (Modular)

كل مكتبة (مثل `math`، `random`) لها ملف خاص في `core/libraries/`:

- **FUNCS**: قاموس يربط الأسماء العربية بـ Python
- **PATTERN**: تعبير نمائي للبحث عن الدوال
- **HELP**: نص المساعدة للـ CLI
- **IMPORT_**: معلومات الاستيراد

استثناء واحد: `net_funcs.py` لا يبني أربعة تعبيرات نمائية، بل مسحاً واحداً
للكلمات الكاملة عبر `NET_SUBSTITUTE`. السبب أن 1006 كلمة كبديل
`a|b|c|…` تكلّف ~13 ms لمجرد بناء التعبير في كل تشغيل، بينما المسح الواحد
يكلّف 0.9 ms ويُحقّق مطابقة الكلمة كاملةً لا كبادئة. ولأن ~150 اسماً عربياً
تحتوي تشكيلاً (شدّة/فتحة) لا يطابقها `\w`، يضيف النمط نطاق
`\u064B-\u065F` صراحةً، ثم يتحقق المُولّد من أن كل اسم قابل للترجمة.

## كيف تُربط مكتبة جديدة؟

إضافة مكتبة تمرّ بخمس خطوات (نفس ما اتُّبع مع `xml`):

1. **ملف المكتبة** `core/libraries/<name>_funcs.py` يحتوي أربعة قواميس
   (`<NAME>_FUNCS`, `<NAME>_METHODS`, `<NAME>_PROPS`, `<NAME>_CONSTANTS`)،
   والأنماط المقابلة (`<NAME>_PATTERN`, `<NAME>_METHOD_PATTERN`, …)،
   و`<NAME>_HELP` و`IMPORT_NAME/IMPORT_CHECK/IMPORT_STATEMENT`.
2. **التسجيل** في `core/libraries/__init__.py` (استيراد + `LIBRARIES`).
3. **التحميل الكسول** في `core/libraries/lazy.py` (`_MODULE_NAMES`).
4. **أنماط الترجمة** في `core/apl_runner/inline_replacer.py`
   (طرق الكائن ← الخصائص ← الثوابت ← الدوال)، مع أي معاملات عربية
   في `_KW_ALIASES` الخاصة بالمكتبة.

   > **قاعدة ثابتة:** أنماط الأسماء العامة (الدوال والثوابت) لا تُطبَّق **بعد نقطة** —
   > الشرط `(?<![\w.\u0600-\u06FF])`. بدونها كان `كائن.عنصر(...)` (خاصية باسم
   > يشبه دالةً في مكتبة) يُترجم إلى `كائن._apl_xml_element(...)`.
5. **التوثيق والأمثلة**: `docs/<name>-library.md` + مثال في `examples/`
   + سطر في `print_help` داخل `main.py`.

الدوال المساعدة التي تحتاج منطقاً (وليست مجرد اسم Python) تُضاف إلى
`_RUNTIME` في `core/apl_runner/main.py` باسم يبدأ بـ `_apl_`، مع استيراد
كسول للمكتبة القياسية داخل الدالة نفسها حتى لا يدفع الإقلاع أي كلفة.

## لماذا `core/`؟

- **حماية**: المستخدم العادي لا يلمس المحرك
- **وضوح**: `apl.py` للتشغيل فقط
- **توسعه**: إضافة مكتبة جديدة = ملف جديد في `core/libraries/`

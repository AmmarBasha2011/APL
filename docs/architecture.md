# هيكل المشروع — APL

## الملفات والمجلدات

```
APL/
├── apl.py                   ← نقطة الدخول (للتشغيل فقط)
├── calculator.apl           ← مثال
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
│       └── time_funcs.py     ← مكتبة time/datetime
└── docs/                    ← التوثيق
    ├── index.md
    ├── architecture.md
    ├── language-reference.md
    ├── math-library.md
    ├── random-library.md
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

## لماذا `core/`؟

- **حماية**: المستخدم العادي لا يلمس المحرك
- **وضوح**: `apl.py` للتشغيل فقط
- **توسعه**: إضافة مكتبة جديدة = ملف جديد في `core/libraries/`

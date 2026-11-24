# مكتبة تحليل الوسائط — `argparse`

مكتبة argparse الكاملة بالعربي، تحليل وسائط سطر الأوامر:

**106 عنصراً عربياً** (الدوال: 91، المعاملات المسماة: 10، عناصر أخرى: 8).

## الدوال (88)

| العربي | Python |
|--------|--------|
| `محلل_وسائط` | `argparse.ArgumentParser` |
| `اسم_وسائط` | `parser.prog` |
| `وصف` | `parser.description` |
| `تلميح_استخدام` | `parser.usage` |
| `نهاية_مساعدة` | `parser.formatter_class` |
| `خاتمة_مساعدة` | `parser.epilog` |
| `بادئة_حجة` | `parser.prefix_chars` |
| `من_ملف_وسائط` | `parser.fromfile_prefix_chars` |
| `أب_وسائط` | `parser.parents` |
| `مُنسَق` | `parser.formatter_class` |
| `إضافة_مساعدة` | `parser.add_help` |
| `السماح_الاختصارات` | `parser.allow_abbrev` |
| `أضف_مجموعة` | `parser.add_argument_group` |
| `مجموعة_متنافية` | `parser.add_mutually_exclusive_group` |
| `مجموعة_حجة` | `parser.add_argument_group` |
| `مجموعة_حجج` | `parser.add_argument_group` |
| `أضف_حجة` | `parser.add_argument` |
| `حجة` | `parser.add_argument` |
| `أضف_حجة_وضعية` | `parser.add_argument` |
| `حجة_وضعية` | `parser.add_argument` |
| `أضف_خيار` | `parser.add_argument` |
| `خيار` | `parser.add_argument` |
| `أضف_علم` | `parser.add_argument` |
| `علم` | `parser.add_argument` |
| `اسم_حجة` | `name` |
| `وجهة` | `dest` |
| `نوع` | `type` |
| `افتراضي` | `default` |
| `مطلوب` | `required` |
| `تلميح` | `help` |
| `الإجراء` | `action` |
| `ثابت` | `const` |
| `خيارات_وسائط` | `choices` |
| ` nargs` | `nargs` |
| ` metavar` | `metavar` |
| `خزن` | `store` |
| `خزن_ثابت` | `store_const` |
| `خزن_صحيح` | `store_true` |
| `خزن_خطأ` | `store_false` |
| `أضف_قيمة` | `append` |
| `عد_مرات` | `count` |
| `أضف_وسيط` | `append` |
| `أضف_ثابت` | `append_const` |
| `عد_وسيط` | `count` |
| `مساعدة_وسائط` | `help` |
| `إصدار_وسائط` | `version` |
| `حلل` | `parser.parse_args` |
| `حلل_وسائط` | `parser.parse_args` |
| `حلل_معروف` | `parser.parse_known_args` |
| `حلل_من_سلسلة` | `parser.parse_args` |
| `وسائط` | `parser.parse_args` |
| `حلل_وسائط_من_ملف` | `parser.parse_args` |
| `إصدار_المحلل` | `parser.version` |
| `خطأ_وسائط` | `parser.error` |
| `خروج` | `parser.exit` |
| `استخدم_بعد_التحليل` | `parser.exit` |
| `اطبع_مساعدة` | `parser.print_help` |
| `اطبع_استخدام` | `parser.print_usage` |
| `مساعدة_كاملة` | `parser.format_help` |
| `استخدام_كامل` | `parser.format_usage` |
| `مساعدة_تلقائية` | `ArgumentDefaultsHelpFormatter` |
| `مساعدة_نصية` | `RawDescriptionHelpFormatter` |
| `مساعدة_نصية_فقط` | `RawTextHelpFormatter` |
| `مساعدة_Metavar` | `MetavarTypeHelpFormatter` |
| `من_ملف` | `parser.parse_args` |
| `إلى_ملف` | `parser.parse_args` |
| `قيمة_صحيح` | `True` |
| `قيمة_خطأ` | `False` |
| `قيمة_لا_شيء` | `None` |
| `فرعي` | `subparsers` |
| `أضف_فرعي` | `parser.add_subparsers` |
| `أضف_محلل_فرعي` | `subparsers.add_parser` |
| `محلل_فرعي` | `subparsers.add_parser` |
| `نوع_نص` | `str` |
| `نوع_عدد_صحيح` | `int` |
| `نوع_عدد_عشري` | `float` |
| `نوع_منطقي` | `bool` |
| `نوع_قائمة` | `list` |
| `نوع_صف` | `tuple` |
| `نوع_مجموعة` | `set` |
| `نوع_قاموس` | `dict` |
| `واحد` | `1` |
| `صفر` | `0` |
| `الكل` | `*` |
| `واحد_أو_أكثر` | `+` |
| `اختياري` | `?` |
| `Namespace` | `argparse.Namespace` |
| `FILE` | `argparse.FileType` |

## المعاملات المسماة (10) — `ARGPARSE_KWARGS`

| العربي | Python |
|--------|--------|
| `وجهة` | `dest` |
| `نوع` | `type` |
| `افتراضي` | `default` |
| `مطلوب` | `required` |
| `تلميح` | `help` |
| `الإجراء` | `action` |
| `ثابت` | `const` |
| `خيارات_وسائط` | `choices` |
| `nargs` | `nargs` |
| `metavar` | `metavar` |

## عناصر أخرى (8) — `ARGPARSE_STANDALONE`

| العربي | Python |
|--------|--------|
| `محلل_أضف_حجة` | `_apl_ap_add_argument` |
| `محلل_أضف_قيمة` | `_apl_ap_add_argument` |
| `محلل_أضف_مجموعة` | `_apl_ap_add_argument_group` |
| `محلل_حلل` | `_apl_ap_parse_args` |
| `محلل_حلل_معروف` | `_apl_ap_parse_known_args` |
| `محلل_مساعدة` | `_apl_ap_format_help` |
| `محلل_اطبع_مساعدة` | `_apl_ap_print_help` |
| `محلل_نسخ` | `_apl_ap_parser_copy` |

## مثال

```apl
# إنشاء محلل
المتغير parser = أنشئ_محلل()
parser.description = "برنامج اختبار"

# إضافة حجة وضعية
أضف_حجة("اسم", تلميح="اسم المستخدم")

# إضافة خيار
أضف_خيار("--عمر", نوع=int, افتراضي=25)

# عرض المساعدة كما يراها المستخدم
اطبع parser.format_help()

# تحليل قائمة وسائط صريحة
المتغير args = parser.parse_args(["عمار", "--عمر", "30"])
اطبع "الاسم:", args.اسم
اطبع "العمر:", args.عمر
```

# مكتبة ملفات الإعداد — `configparser`

مكتبة configparser الكاملة بالعربي، قراءة وكتابة ملفات الإعداد:

**32 عنصراً عربياً** (الدوال: 35).

## الدوال (32)

| العربي | Python |
|--------|--------|
| `مُكوِّن_إعدادات` | `configparser.ConfigParser` |
| `افتراضي_إعدادات` | `config.defaults` |
| `تكوين_افتراضي` | `configparser.DEFAULTSECT` |
| `اقرأ_إعداد` | `config.read` |
| `اقرأ_ملف` | `config.read_file` |
| `اقرأ_سلسلة` | `config.read_string` |
| `اقرأ_قاموس_إعدادات` | `config.read_dict` |
| `اكتب_إعداد` | `config.write` |
| `اكتب_ملف` | `config.write` |
| `أضف_قسم` | `config.add_section` |
| `أزل_قسم` | `config.remove_section` |
| `يوجد_قسم` | `config.has_section` |
| `الأقسام` | `config.sections` |
| `ضع` | `config.set` |
| `احصل` | `config.get` |
| `أزل_خيار` | `config.remove_option` |
| `يوجد_خيار` | `config.has_option` |
| `الخيارات` | `config.options` |
| `احصل_عدد_صحيح` | `config.getint` |
| `احصل_عدد_عشري` | `config.getfloat` |
| `احصل_منطقي` | `config.getboolean` |
| `items` | `config.items` |
| `احصل_كل` | `config.items` |
| `BasicInterpolation` | `configparser.BasicInterpolation` |
| `ExtendedInterpolation` | `configparser.ExtendedInterpolation` |
| `RawInterpolation` | `configparser.RawInterpolation` |
| `RawConfigParser` | `configparser.RawConfigParser` |
| `SafeConfigParser` | `configparser.SafeConfigParser` |
| `مفاتيح_افتراضية` | `config.defaults` |
| `بادئة_تعليق` | `config._comment_prefixes` |
| `DEFAULT` | `configparser.DEFAULTSECT` |
| `الافتراضي` | `configparser.DEFAULTSECT` |

## مثال

```apl
# إنشاء مُكوِّن
المتغير config = محلل_إعدادات()

# إضافة أقسام وقيم
أضف_قسم("قاعدة_بيانات")
ضع("قاعدة_بيانات", "مضيف", "localhost")
ضع("قاعدة_بيانات", "منفذ", "5432")
ضع("قاعدة_بيانات", "اسم", "mydb")

أضف_قسم("مستخدم")
ضع("مستخدم", "اسم", "admin")
ضع("مستخدم", "عمر", "25")

# كتابة الملف
المتغير ملف = فتح("config.ini", "w")
اكتب_إعداد(ملف)
ملف.close()

# قراءة الملف من جديد
المتغير config = محلل_إعدادات()
اقرأ_إعداد("config.ini")

اطبع "المضيف:", احصل("قاعدة_بيانات", "مضيف")
اطبع "المنفذ:", احصل_عدد_صحيح("قاعدة_بيانات", "منفذ")
اطبع "الأقسام:", الأقسام()

احذف_ملف("config.ini")
```

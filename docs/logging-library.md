# مكتبة التسجيل — `logging`

مكتبة logging الكاملة بالعربي، تسجيل الأحداث:

**87 عنصراً عربياً** (الدوال: 74، الثوابت: 5، عناصر أخرى: 8).

## الدوال (74)

| العربي | Python |
|--------|--------|
| `مسجّل` | `logging.getLogger` |
| `أنشئ_مسجل` | `logging.getLogger` |
| `مسجل` | `logging.getLogger` |
| `تكوين_تسجيل` | `logging.basicConfig` |
| `أساسي` | `logging.basicConfig` |
| `مستوى` | `setLevel` |
| `ضع_مستوى` | `setLevel` |
| `تنسيق` | `logging.Formatter` |
| `شكل` | `logging.Formatter` |
| `شكل_جديد` | `logging.Formatter` |
| `شكل_افتراضي` | `logging.Formatter` |
| `ضع_شكل` | `handler.setFormatter` |
| `صيغة` | `fmt` |
| `تاريخ_صيغة` | `datefmt` |
| `معالج` | `logging.Handler` |
| `معالج_ملف` | `logging.FileHandler` |
| `معالج_شاشة` | `logging.StreamHandler` |
| `معالج_دوار` | `logging.handlers.RotatingFileHandler` |
| `معجل_مؤقت` | `logging.handlers.TimedRotatingFileHandler` |
| `أنشئ_معالج` | `logging.Handler` |
| `أضف_معالج` | `logger.addHandler` |
| `أزل_معالج` | `logger.removeHandler` |
| `جذر_تسجيل` | `logging.root` |
| `سجل_جذر` | `logging.root` |
| `سجل_أساسي` | `logging` |
| `اطبع_تصحيح` | `logging.debug` |
| `اطبع_معلومات` | `logging.info` |
| `اطبع_تحذير` | `logging.warning` |
| `اطبع_خطأ` | `logging.error` |
| `اطبع_حرج` | `logging.critical` |
| `استثناء_تسجيل` | `logging.exception` |
| `تسجيل` | `logging.log` |
| `تصحيح` | `debug` |
| `معلومات` | `info` |
| `تحذير` | `warning` |
| `خطأ_تسجيل` | `error` |
| `حرج` | `critical` |
| `استثناء_سجل` | `exception` |
| `فلتر_تسجيل` | `logging.Filter` |
| `أنشئ_فلتر` | `logging.Filter` |
| `أضف_فلتر` | `logger.addFilter` |
| `أزل_فلتر` | `logger.removeFilter` |
| `اسم_فلتر` | `filter.name` |
| `اسم_المسجل` | `logger.name` |
| `أب` | `logger.parent` |
| `منتشر` | `logger.propagate` |
| `مكّن` | `logger.disabled` |
| `فعّل` | `logger.enable` |
| `عطّل` | `logger.disable` |
| `مستوى_فعّال` | `logger.getEffectiveLevel` |
| `مُعَطَّل` | `logger.disabled` |
| `سجل_إضافي` | `logging.LoggerAdapter` |
| `محول_سجل` | `logging.LoggerAdapter` |
| `بيانات_إضافية` | `logger.extra` |
| `أغلق` | `logging.shutdown` |
| `تنظيف` | `logging.shutdown` |
| `معالجات` | `logging.handlers` |
| `دوار` | `logging.handlers.RotatingFileHandler` |
| `مؤقت_دوار` | `logging.handlers.TimedRotatingFileHandler` |
| `معالج_tcp` | `logging.handlers.SocketHandler` |
| `معالج_udp` | `logging.handlers.DatagramHandler` |
| `معالج_بريد` | `logging.handlers.SMTPHandler` |
| `معالج_syslog` | `logging.handlers.SysLogHandler` |
| `معجل_nt` | `logging.handlers.NTEventLogHandler` |
| `معالج_http` | `logging.handlers.HTTPHandler` |
| `معالج_ذاكرة` | `logging.handlers.MemoryHandler` |
| `معالج_queue` | `logging.handlers.QueueHandler` |
| `طابور_سجل` | `logging.handlers.QueueHandler` |
| `مستمع_سجل` | `logging.handlers.QueueListener` |
| `قفل_سجل` | `logging._lock` |
| `تحذير_مرة` | `logging._warnings` |
| `تحذيرات_مرة` | `logging.captureWarnings` |
| `كتالوجات` | `logging.Logger.manager.loggerDict` |
| `كل_المسجلات` | `logging.Logger.manager` |

## الثوابت (5) — `LOGGING_CONSTANTS`

| العربي | Python |
|--------|--------|
| `مستوى_تصحيح` | `logging.DEBUG` |
| `مستوى_معلومات` | `logging.INFO` |
| `مستوى_تحذير` | `logging.WARNING` |
| `مستوى_خطأ` | `logging.ERROR` |
| `مستوى_حرج` | `logging.CRITICAL` |

## عناصر أخرى (8) — `LOGGING_VERBS`

| العربي | Python |
|--------|--------|
| `سجل_تصحيح` | `logging.debug` |
| `سجل_معلومات` | `logging.info` |
| `سجل_تحذير` | `logging.warning` |
| `سجل_خطأ` | `logging.error` |
| `سجل_حرج` | `logging.critical` |
| `سجل_استثناء` | `logging.exception` |
| `سجل_تهيئة` | `logging.basicConfig` |
| `سجل_مستوى` | `logging.getLogger` |

## مثال

```apl
تكوين_تسجيل(level=مستوى_معلومات)
المتغير مسجل_التطبيق = مسجّل("تطبيقي")
اطبع_معلومات("بدء التطبيق")
اطبع_خطأ("حدث خطأ")
حاول:
    raise ValueError("س")
إمسك:
    اطبع_تحذير("تم التقاط الخطأ")
```

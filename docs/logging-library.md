# مكتبة التسجيل — `logging`

مكتبة logging الكاملة بالعربي، تسجيل الأحداث:

**61 عنصراً عربياً** (الدوال: 74، الثوابت: 5، عناصر أخرى: 8).

## الدوال (49)

| العربي | Python |
|--------|--------|
| `مستوى` | `setLevel` |
| `ضع_مستوى` | `setLevel` |
| `شكل` | `logging.Formatter` |
| `ضع_شكل` | `handler.setFormatter` |
| `صيغة` | `fmt` |
| `تاريخ_صيغة` | `datefmt` |
| `معالج` | `logging.Handler` |
| `معالج_ملف` | `logging.FileHandler` |
| `أضف_معالج` | `logger.addHandler` |
| `أزل_معالج` | `logger.removeHandler` |
| `جذر_تسجيل` | `logging.root` |
| `سجل_جذر` | `logging.root` |
| `سجل_أساسي` | `logging` |
| `تسجيل` | `logging.log` |
| `تصحيح` | `debug` |
| `معلومات` | `info` |
| `تحذير` | `warning` |
| `خطأ_تسجيل` | `error` |
| `حرج` | `critical` |
| `استثناء_سجل` | `exception` |
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
| `محول_سجل` | `logging.LoggerAdapter` |
| `بيانات_إضافية` | `logger.extra` |
| `أغلق` | `logging.shutdown` |
| `معالجات` | `logging.handlers` |
| `دوار` | `logging.handlers.RotatingFileHandler` |
| `مؤقت_دوار` | `logging.handlers.TimedRotatingFileHandler` |
| `معالج_tcp` | `logging.handlers.SocketHandler` |
| `معالج_udp` | `logging.handlers.DatagramHandler` |
| `معالج_syslog` | `logging.handlers.SysLogHandler` |
| `معجل_nt` | `logging.handlers.NTEventLogHandler` |
| `معالج_http` | `logging.handlers.HTTPHandler` |
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

## عناصر أخرى (7) — `LOGGING_VERBS`

| العربي | Python |
|--------|--------|
| `سجل_تصحيح` | `logging.debug` |
| `سجل_معلومات` | `logging.info` |
| `سجل_تحذير` | `logging.warning` |
| `سجل_خطأ` | `logging.error` |
| `سجل_حرج` | `logging.critical` |
| `سجل_استثناء` | `logging.exception` |
| `سجل_تهيئة` | `logging.basicConfig` |

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

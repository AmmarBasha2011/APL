# مكتبة العمليات الفرعية — `subprocess`

مكتبة subprocess الكاملة بالعربي، تشغيل أوامر النظام:

## الإنشاء

| العربي | Python | الوصف |
|--------|--------|-------|
| `أنشئ_عملية_أوامر(أمر)` | `subprocess.run(أمر)` | تشغيل أمر |
| `عملية(أمر)` | `subprocess.run(أمر)` | عملية (مختصر) |
| `نفذ_أوامر(أمر)` | `subprocess.run(أمر)` | تنفيذ أمر |
| `Process(أمر)` | `subprocess.Popen(أمر)` | إنشاء Process |

## الخصائص

| العربي | Python |
|--------|--------|
| `حجة_أوامر(قائمة)` | args |
| `قشرة(صحيح)` | shell |
| `انتظر_أوامر(ثوان)` | timeout |
| `دليل(مسار)` | cwd |
| `متغيرات_بيئة(قاموس)` | env |
| `التقاط(صحيح)` | capture_output |
| `مدخل(نص)` | input |

## التنفيذ

| العربي | Python |
|--------|--------|
| `اتصل_أوامر()` | communicate |
| `انتظر_إنهاء()` | wait |
| `ألغى_أوامر()` | terminate |
| `اقتل()` | kill |
| `أرسل_إشارة(إشارة)` | send_signal |

## الحالة

| العربي | Python |
|--------|--------|
| `رمز_العودة()` | returncode |
| `pid()` | pid |
| `تم_إنهاء()` | poll |
| `نجاح_أوامر()` | returncode == 0 |

## المخرجات

| العربي | Python |
|--------|--------|
| `خرج_معياري_أوامر()` | stdout |
| `خطأ_معياري_أوامر()` | stderr |

## الأجهزة

| العربي | Python |
|--------|--------|
| `PIPE` | subprocess.PIPE |
| `STDOUT` | subprocess.STDOUT |
| `DEVNULL` | subprocess.DEVNULL |

## الإشارات

| العربي | Python |
|--------|--------|
| `SIGTERM` | signal.SIGTERM |
| `SIGKILL` | signal.SIGKILL |
| `SIGINT` | signal.SIGINT |

## مثال

```apl
# تنفيذ أمر بسيط
المتغير نتيجة = نفذ_أوامر(["echo", "مرحبا"], capture_output=True, text=True)
اطبع "رمز العودة:", نتيجة.returncode
اطبع "الخرج:", نتيجة.stdout.strip()

# عبر القشرة (shell)
المتغير نتيجة2 = نفذ_أوامر("echo hello", shell=True, capture_output=True, text=True)
اطبع "الخرج الثاني:", نتيجة2.stdout.strip()

# مهلة زمنية
حاول:
    المتغير نتيجة3 = نفذ_أوامر(["sleep", "5"], timeout=1)
إمسك:
    اطبع "انتهت المهلة كما هو متوقع"
```

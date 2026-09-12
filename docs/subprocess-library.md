# مكتبة العمليات الفرعية — `subprocess`

مكتبة subprocess الكاملة بالعربي، تشغيل أوامر النظام:

## الإنشاء

| العربي | Python | الوصف |
|--------|--------|-------|
| `أنشئ_عملية(أمر)` | `subprocess.run(أمر)` | تشغيل أمر |
| `عملية(أمر)` | `subprocess.run(أمر)` | عملية (مختصر) |
| `نفذ(أمر)` | `subprocess.run(أمر)` | تنفيذ أمر |
| `Process(أمر)` | `subprocess.Popen(أمر)` | إنشاء Process |

## الخصائص

| العربي | Python |
|--------|--------|
| `حجة(قائمة)` | args |
| `قشرة(صحيح)` | shell |
| `انتظر(ثوان)` | timeout |
| `دليل(مسار)` | cwd |
| `متغيرات_بيئة(قاموس)` | env |
| `التقاط(صحيح)` | capture_output |
| `مدخل(نص)` | input |

## التنفيذ

| العربي | Python |
|--------|--------|
| `اتصل()` | communicate |
| `انتظر_إنهاء()` | wait |
| `ألغى()` | terminate |
| `اقتل()` | kill |
| `أرسل_إشارة(إشارة)` | send_signal |

## الحالة

| العربي | Python |
|--------|--------|
| `رمز_العودة()` | returncode |
| `pid()` | pid |
| `تم_إنهاء()` | poll |
| `نجاح()` | returncode == 0 |

## المخرجات

| العربي | Python |
|--------|--------|
| `خرج_معياري()` | stdout |
| `خطأ_معياري()` | stderr |

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
المتغير r = نفذ(["ls", "-la"])
اطبع "رمز العودة:", r.returncode
اطبع "الخرج:", r.stdout

# استخدام القشرة
المتغير r2 = نفذ("echo hello", قشرة=صحيح)

# عملية مع مهلة
try:
    المتغير r3 = نفذ(["sleep", "10"], انتظر=5)
except TimeoutExpired:
   اطبع "انتهت المهلة"

# التقاط المخرجات
المتغير r4 = نفذ(["python", "--version"], التقاط=صحيح)
اطبع r4.stdout.decode().strip()
```

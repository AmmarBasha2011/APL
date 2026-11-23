# مكتبة تعدد المهام — `threading`

مكتبة threading الكاملة بالعربي، تعدد المهام:

**29 عنصراً عربياً** (الدوال: 29).

## الدوال (29)

| العربي | Python |
|--------|--------|
| `ثريد` | `threading.Thread` |
| `أنشئ_ثريد` | `threading.Thread` |
| `مهمة_خيوط` | `threading.Thread` |
| `أنشئ_مهمة_خيوط` | `threading.Thread` |
| `عامل` | `threading.Thread` |
| `ابدأ_خيوط` | `thread.start` |
| `انتظر_خيوط` | `thread.join` |
| `ألغى_خيوط` | `thread.cancel` |
| `نشط` | `thread.is_alive` |
| `اسم` | `thread.name` |
| `دايمون` | `thread.daemon` |
| `قفل_خيوط` | `threading.Lock` |
| `أنشئ_قفل` | `threading.Lock` |
| `امتلك_خيوط` | `lock.acquire` |
| `أطلق_خيوط` | `lock.release` |
| `إشارة_خيوط` | `threading.Semaphore` |
| `أنشئ_إشارة` | `threading.Semaphore` |
| `حدث_خيوط` | `threading.Event` |
| `أنشئ_حدث` | `threading.Event` |
| `انتظر_حدث_خيوط` | `event.wait` |
| `أطلق_حدث_خيوط` | `event.set` |
| `امسح_حدث_خيوط` | `event.clear` |
| `مؤقت_خيوط` | `threading.Timer` |
| `أنشئ_مؤقت_خيوط` | `threading.Timer` |
| `ثريد_حالي` | `threading.current_thread` |
| `الثريد_الحالي` | `threading.current_thread` |
| `عداد_ثريدات` | `threading.active_count` |
| `نوم_خيوط` | `time.sleep` |
| `انتظر_ثانية` | `time.sleep` |

## مثال

```apl
دالة_عمل(اسم):
    اطبع "بدء العمل:", اسم
    نوم_خيوط(0.1)
    اطبع "انتهاء العمل:", اسم

المتغير ت1 = ثريد(target=دالة_عمل, args=("أولى",))
المتغير ت2 = ثريد(target=دالة_عمل, args=("ثانية",))

ت1.start()
ت2.start()

ت1.join()
ت2.join()

اطبع "انتهت كل المهام"
```

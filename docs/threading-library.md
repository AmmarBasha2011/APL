# مكتبة تعدد المهام — `threading`

مكتبة threading الكاملة بالعربي، تعدد المهام:

**19 عنصراً عربياً** (الدوال: 29).

## الدوال (19)

| العربي | Python |
|--------|--------|
| `أنشئ_ثريد` | `threading.Thread` |
| `ابدأ_خيوط` | `thread.start` |
| `انتظر_خيوط` | `thread.join` |
| `ألغى_خيوط` | `thread.cancel` |
| `نشط` | `thread.is_alive` |
| `اسم` | `thread.name` |
| `دايمون` | `thread.daemon` |
| `أنشئ_قفل` | `threading.Lock` |
| `امتلك_خيوط` | `lock.acquire` |
| `أطلق_خيوط` | `lock.release` |
| `أنشئ_إشارة` | `threading.Semaphore` |
| `أنشئ_حدث` | `threading.Event` |
| `انتظر_حدث_خيوط` | `event.wait` |
| `أطلق_حدث_خيوط` | `event.set` |
| `امسح_حدث_خيوط` | `event.clear` |
| `أنشئ_مؤقت_خيوط` | `threading.Timer` |
| `ثريد_حالي` | `threading.current_thread` |
| `عداد_ثريدات` | `threading.active_count` |
| `نوم_خيوط` | `time.sleep` |

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

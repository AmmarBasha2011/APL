# مكتبة البرمجة غير المتزامنة — `asyncio`

مكتبة asyncio الكاملة بالعربي، برمجة غير متزامنة:

**101 عنصراً عربياً** (الدوال: 118).

## الدوال (101)

| العربي | Python |
|--------|--------|
| `غير_متزامن` | `async with` |
| `أنشئ_مهمة` | `asyncio.create_task` |
| `شغل_تزامن` | `asyncio.run` |
| `انتظر` | `asyncio.wait` |
| `انتظر_أي` | `asyncio.wait_for` |
| `اجمع` | `asyncio.gather` |
| `نوم` | `asyncio.sleep` |
| `حلقة` | `asyncio.get_event_loop` |
| `حلقة_جديدة` | `asyncio.new_event_loop` |
| `اجعل_حلقة` | `asyncio.set_event_loop` |
| `مهمة_تزامن` | `asyncio.Task` |
| `حالة_مهمة` | `task.done` |
| `نتيجة_مهمة` | `task.result` |
| `استثناء_مهمة` | `task.exception` |
| `أضف_استدعاء` | `task.add_done_callback` |
| `أزل_استدعاء` | `task.remove_done_callback` |
| `مكدس_مهمة` | `task.print_stack` |
| `اسم_مهمة` | `task.get_name` |
| `ضع_اسم` | `task.set_name` |
| `Coroutine_مهمة` | `task.get_coro` |
| `قفل` | `asyncio.Lock` |
| `امتلك` | `lock.acquire` |
| `أطلق` | `lock.release` |
| `إشارة` | `asyncio.Semaphore` |
| `امتلك_إشارة` | `semaphore.acquire` |
| `أطلق_إشارة` | `semaphore.release` |
| `حدث_تزامن` | `asyncio.Event` |
| `انتظر_حدث` | `event.wait` |
| `أطلق_حدث` | `event.set` |
| `امسح_حدث` | `event.clear` |
| `طابور` | `asyncio.Queue` |
| `ضع_في_طابور` | `queue.put` |
| `احصل_من_طابور` | `queue.get` |
| `تأكد_طابور` | `queue.task_done` |
| `انضم_طابور` | `queue.join` |
| `حجم_طابور` | `queue.qsize` |
| `طابور_فارغ` | `queue.empty` |
| `طابور_ممتلئ` | `queue.full` |
| `ضع_الآن` | `queue.put_nowait` |
| `احصل_الآن` | `queue.get_nowait` |
| `شرط` | `asyncio.Condition` |
| `انتظر_شرط` | `condition.wait` |
| `أبلغ_شرط` | `condition.notify` |
| `أبلغ_الكل` | `condition.notify_all` |
| `مجرى` | `asyncio.StreamReader` |
| `اتصال_تزامن` | `asyncio.StreamWriter` |
| `اكتب_مجرى` | `writer.write` |
| `فرغ_مجرى` | `writer.drain` |
| `أغلق_مجرى` | `writer.close` |
| `انتظر_إغلاق` | `writer.wait_closed` |
| `هل_مغلق` | `writer.is_closing` |
| `عنوان_مجرى` | `writer.get_extra_info` |
| `منفذ_مجرى` | `writer.get_extra_info` |
| `قابس_مجرى` | `writer.get_extra_info` |
| `أضف_إشارة` | `loop.add_signal_handler` |
| `أزل_إشارة` | `loop.remove_signal_handler` |
| `إشارة_إنهاء` | `signal.SIGINT` |
| `إشارة_قتل` | `signal.SIGTERM` |
| `أنشئ_عملية` | `asyncio.create_subprocess_exec` |
| `أنشئ_عملية_قشرة` | `asyncio.create_subprocess_shell` |
| `انتظر_عملية` | `process.wait` |
| `تواصل_عملية` | `process.communicate` |
| `أرسل_إشارة_عملية` | `process.send_signal` |
| `اقتل_عملية` | `process.kill` |
| `انتهت_عملية` | `process.returncode` |
| `خطأ_معياري` | `process.stderr` |
| `خرج_معياري` | `process.stdout` |
| `دخل_معياري` | `process.stdin` |
| `اكتب_لعملية` | `process.stdin.write` |
| `مهلة_تزامن` | `asyncio.timeout` |
| `داخل_مهلة` | `async with asyncio.timeout` |
| `ألغى` | `asyncio.CancelledError` |
| `مهام_مكتملة` | `done` |
| `مهام_معلقة` | `pending` |
| `قياس_وقت` | `asyncio.get_event_loop().time` |
| `وقت_حلقة` | `loop.time` |
| `أنشئ_مستقبل` | `loop.create_future` |
| `مستقبل_مكتمل` | `future.done` |
| `مستقبل_ملغى` | `future.cancelled` |
| `نتيجة_مستقبل` | `future.result` |
| `استثناء_مستقبل` | `future.exception` |
| `ضع_نتيجة` | `future.set_result` |
| `ضع_استثناء` | `future.set_exception` |
| `أضف_مستقبل` | `future.add_done_callback` |
| `أزل_مستقبل` | `future.remove_done_callback` |
| `أنشئ_خادم` | `asyncio.start_server` |
| `أغلق_خادم` | `server.close` |
| `انتظر_خادم` | `server.serve_forever` |
| `أغلق_اتصالات` | `server.close_clients` |
| `افتح_اتصال` | `asyncio.open_connection` |
| `أغلق_اتصال_تزامن` | `writer.close` |
| `اكتب_اتصال` | `writer.write` |
| `اقرأ_اتصال` | `reader.read` |
| `اقرأ_سطر` | `reader.readline` |
| `اقرأ_كل` | `reader.readexactly` |
| `استثناء_تزامن` | `Exception` |
| `ألقى_استثناء` | `raise` |
| `حاول` | `try` |
| `إلا` | `except` |
| `أخيرا` | `finally` |
| `ضمني_تزامن` | `async with` |

## مثال

```apl
import asyncio

async def رابط_ويب(رابط):
    اطبع "جاري الاتصال..."
    await نوم(0.1)
    اطبع "تم الاتصال:", رابط
    return {"url": رابط, "status": "ok"}

شغل_تزامن(رابط_ويب("https://example.com"))

async def مدير_المهام():
    المتغير مهام = [رابط_ويب("a"), رابط_ويب("b"), رابط_ويب("c")]
    النتائج = await اجمع(*مهام)
    اطبع النتائج

شغل_تزامن(مدير_المهام())
```

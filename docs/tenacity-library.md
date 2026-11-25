# مكتبة إعادة المحاولة بسياسات إيقاف وانتظار من حزمة tenacity — `tenacity`

**72 عنصراً عربياً** (الدوال: 71، الثوابت: 1).

## الدوال (71) — `TENACITY_FUNCS`

| العربي | Python |
|--------|--------|
| `تيناسيتي_أساس_اكتيون` | `tenacity.BaseAction` |
| `تيناسيتي_أساس_ريترينج` | `tenacity.BaseRetrying` |
| `تيناسيتي_أساس_ريترينج_انسخ` | `tenacity.BaseRetrying.copy` |
| `تيناسيتي_أساس_ريترينج_بداية` | `tenacity.BaseRetrying.begin` |
| `تيناسيتي_أساس_ريترينج_تكرار` | `tenacity.BaseRetrying.iter` |
| `تيناسيتي_أساس_ريترينج_يغلف` | `tenacity.BaseRetrying.wraps` |
| `تيناسيتي_إعادة_محاولة` | `tenacity.retry` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_أساس` | `tenacity.retry.retry_base` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_أي` | `tenacity.retry.retry_any` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_كل` | `tenacity.retry.retry_all` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_ونليس_استثناء_نوع` | `tenacity.retry.retry_unless_exception_type` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_يف_استثناء` | `tenacity.retry.retry_if_exception` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_يف_استثناء_كاوس_نوع` | `tenacity.retry.retry_if_exception_cause_type` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_يف_استثناء_ميساج` | `tenacity.retry.retry_if_exception_message` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_يف_استثناء_نوع` | `tenacity.retry.retry_if_exception_type` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_يف_نتيجة` | `tenacity.retry.retry_if_result` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_يف_نوت_استثناء_ميساج` | `tenacity.retry.retry_if_not_exception_message` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_يف_نوت_استثناء_نوع` | `tenacity.retry.retry_if_not_exception_type` |
| `تيناسيتي_إعادة_محاولة_إعادة_محاولة_يف_نوت_نتيجة` | `tenacity.retry.retry_if_not_result` |
| `تيناسيتي_إعادة_محاولة_استدعاء_حالة` | `tenacity.RetryCallState` |
| `تيناسيتي_إعادة_محاولة_استدعاء_حالة_بريبار_فور_التالي_محاولة` | `tenacity.RetryCallState.prepare_for_next_attempt` |
| `تيناسيتي_إعادة_محاولة_استدعاء_حالة_جلب_فن_اسم` | `tenacity.RetryCallState.get_fn_name` |
| `تيناسيتي_إعادة_محاولة_استدعاء_حالة_ضبط_استثناء` | `tenacity.RetryCallState.set_exception` |
| `تيناسيتي_إعادة_محاولة_استدعاء_حالة_ضبط_نتيجة` | `tenacity.RetryCallState.set_result` |
| `تيناسيتي_إعادة_محاولة_اكتيون` | `tenacity.RetryAction` |
| `تيناسيتي_إعادة_محاولة_خطأ` | `tenacity.RetryError` |
| `تيناسيتي_إعادة_محاولة_خطأ_ريريس` | `tenacity.RetryError.reraise` |
| `تيناسيتي_إيقاف_إيقاف_أساس` | `tenacity.stop.stop_base` |
| `تيناسيتي_إيقاف_إيقاف_أي` | `tenacity.stop.stop_any` |
| `تيناسيتي_إيقاف_إيقاف_بعد_تأخير` | `tenacity.stop.stop_after_delay` |
| `تيناسيتي_إيقاف_إيقاف_بعد_محاولة` | `tenacity.stop.stop_after_attempt` |
| `تيناسيتي_إيقاف_إيقاف_قبل_تأخير` | `tenacity.stop.stop_before_delay` |
| `تيناسيتي_إيقاف_إيقاف_كل` | `tenacity.stop.stop_all` |
| `تيناسيتي_إيقاف_إيقاف_وهين_يفينت_ضبط` | `tenacity.stop.stop_when_event_set` |
| `تيناسيتي_اسينسيو_إعادة_محاولة_إعادة_محاولة_أي` | `tenacity.asyncio.retry.retry_any` |
| `تيناسيتي_اسينسيو_إعادة_محاولة_إعادة_محاولة_كل` | `tenacity.asyncio.retry.retry_all` |
| `تيناسيتي_اسينسيو_إعادة_محاولة_إعادة_محاولة_يف_استثناء` | `tenacity.asyncio.retry.retry_if_exception` |
| `تيناسيتي_اسينسيو_إعادة_محاولة_إعادة_محاولة_يف_نتيجة` | `tenacity.asyncio.retry.retry_if_result` |
| `تيناسيتي_اسينسيو_إعادة_محاولة_اسينك_إعادة_محاولة_أساس` | `tenacity.asyncio.retry.async_retry_base` |
| `تيناسيتي_اسينسيو_اسينك_ريترينج` | `tenacity.asyncio.AsyncRetrying` |
| `تيناسيتي_اسينسيو_اسينك_ريترينج_تكرار` | `tenacity.asyncio.AsyncRetrying.iter` |
| `تيناسيتي_اسينسيو_اسينك_ريترينج_يغلف` | `tenacity.asyncio.AsyncRetrying.wraps` |
| `تيناسيتي_انتظار_انتظار_أساس` | `tenacity.wait.wait_base` |
| `تيناسيتي_انتظار_انتظار_أسّي` | `tenacity.wait.wait_exponential` |
| `تيناسيتي_انتظار_انتظار_أسّي_تذبذب` | `tenacity.wait.wait_exponential_jitter` |
| `تيناسيتي_انتظار_انتظار_استثناء` | `tenacity.wait.wait_exception` |
| `تيناسيتي_انتظار_انتظار_ثابت` | `tenacity.wait.wait_fixed` |
| `تيناسيتي_انتظار_انتظار_سلسلة` | `tenacity.wait.wait_chain` |
| `تيناسيتي_انتظار_انتظار_عشوائي` | `tenacity.wait.wait_random` |
| `تيناسيتي_انتظار_انتظار_عشوائي_أسّي` | `tenacity.wait.wait_random_exponential` |
| `تيناسيتي_انتظار_انتظار_كومبين` | `tenacity.wait.wait_combine` |
| `تيناسيتي_انتظار_انتظار_لاشيء` | `tenacity.wait.wait_none` |
| `تيناسيتي_انتظار_انتظار_ينكريمينتينج` | `tenacity.wait.wait_incrementing` |
| `تيناسيتي_بعد_بعد_سجل` | `tenacity.after.after_log` |
| `تيناسيتي_بعد_بعد_نوثينج` | `tenacity.after.after_nothing` |
| `تيناسيتي_تري_اجين` | `tenacity.TryAgain` |
| `تيناسيتي_تكرار_حالة` | `tenacity.IterState` |
| `تيناسيتي_تكرار_حالة_ريسيت` | `tenacity.IterState.reset` |
| `تيناسيتي_تورنادويب_تورنادو_ريترينج` | `tenacity.tornadoweb.TornadoRetrying` |
| `تيناسيتي_دو_محاولة` | `tenacity.DoAttempt` |
| `تيناسيتي_دو_نوم` | `tenacity.DoSleep` |
| `تيناسيتي_ريترينج` | `tenacity.Retrying` |
| `تيناسيتي_فوتور` | `tenacity.Future` |
| `تيناسيتي_فوتور_كونستروكت` | `tenacity.Future.construct` |
| `تيناسيتي_قبل_قبل_سجل` | `tenacity.before.before_log` |
| `تيناسيتي_قبل_قبل_نوثينج` | `tenacity.before.before_nothing` |
| `تيناسيتي_قبل_نوم_قبل_نوم_سجل` | `tenacity.before_sleep.before_sleep_log` |
| `تيناسيتي_قبل_نوم_قبل_نوم_نوثينج` | `tenacity.before_sleep.before_sleep_nothing` |
| `تيناسيتي_محاولة_ماناجير` | `tenacity.AttemptManager` |
| `تيناسيتي_ناب_نوم` | `tenacity.nap.sleep` |
| `تيناسيتي_ناب_نوم_وسينج_يفينت` | `tenacity.nap.sleep_using_event` |

## الثوابت (1) — `TENACITY_CONSTS`

| العربي | Python |
|--------|--------|
| `تيناسيتي_إعادة_محاولة_اكتيون_NAME` | `tenacity.RetryAction.NAME` |

"""
APL - Asyncio Library
Full asyncio wrapper with Arabic keywords
"""

ASYNCIO_FUNCS = {
    # الدوال الأساسية
    "غير_متزامن": "asyncio",
    "أنشئ_مهمة": "asyncio.create_task",
    "شغل": "asyncio.run",
    "انتظر": "asyncio.wait",
    "انتظر_أي": "asyncio.wait_for",
    "اجمع": "asyncio.gather",
    "نوم": "asyncio.sleep",
    "وقت_حالي": "asyncio.get_event_loop",
    "حلقة": "asyncio.get_event_loop",
    "حلقة_جديدة": "asyncio.new_event_loop",
    "اجعل_حلقة": "asyncio.set_event_loop",
    "تشغيل": "asyncio.run",
    
    # المهام (Tasks)
    "مهمة": "asyncio.Task",
    "أنشئ_مهمة_جديدة": "asyncio.create_task",
    "ألغى_مهمة": "task.cancel",
    "حالة_مهمة": "task.done",
    "نتيجة_مهمة": "task.result",
    "استثناء_مهمة": "task.exception",
    "أضف_استدعاء": "task.add_done_callback",
    "أزل_استدعاء": "task.remove_done_callback",
    "مكدس_مهمة": "task.print_stack",
    "اسم_مهمة": "task.get_name",
    "ضع_اسم": "task.set_name",
    "Coroutine_مهمة": "task.get_coro",
    
    # القفل (Lock)
    "قفل": "asyncio.Lock",
    "امتلك": "lock.acquire",
    "أطلق": "lock.release",
    
    # الإشارة (Semaphore)
    "إشارة": "asyncio.Semaphore",
    "امتلك_إشارة": "semaphore.acquire",
    "أطلق_إشارة": "semaphore.release",
    
    # الحدث (Event)
    "حدث": "asyncio.Event",
    "انتظر_حدث": "event.wait",
    "أطلق_حدث": "event.set",
    "امسح_حدث": "event.clear",
    
    # الطابور (Queue)
    "طابور": "asyncio.Queue",
    "طابور_محدود": "asyncio.Queue",
    "طابور_لانهائي": "asyncio.Queue",
    "ضع_في_طابور": "queue.put",
    "احصل_من_طابور": "queue.get",
    "تأكد_طابور": "queue.task_done",
    "انضم_طابور": "queue.join",
    "حجم_طابور": "queue.qsize",
    "طابور_فارغ": "queue.empty",
    "طابور_ممتلئ": "queue.full",
    "ضع_الآن": "queue.put_nowait",
    "احصل_الآن": "queue.get_nowait",
    
    # الشرط (Condition)
    "شرط": "asyncio.Condition",
    "انتظر_شرط": "condition.wait",
    "أبلغ_شرط": "condition.notify",
    "أبلغ_الكل": "condition.notify_all",
    
    # الأنابيب (Pipes)
    "استدعاء": "asyncio.StreamReader",
    "مجرى": "asyncio.StreamReader",
    "اتصال": "asyncio.StreamWriter",
    "اكتب_مجرى": "writer.write",
    "فرغ_مجرى": "writer.drain",
    "أغلق_مجرى": "writer.close",
    "انتظر_إغلاق": "writer.wait_closed",
    "هل_مغلق": "writer.is_closing",
    "عنوان_مجرى": "writer.get_extra_info",
    "منفذ_مجرى": "writer.get_extra_info",
    "قابس_مجرى": "writer.get_extra_info",
    
    # الإشارات (Signals)
    "أضف_إشارة": "loop.add_signal_handler",
    "أزل_إشارة": "loop.remove_signal_handler",
    "إشارة_إنهاء": "signal.SIGINT",
    "إشارة_قتل": "signal.SIGTERM",
    
    # العمليات (Processes)
    "أنشئ_عملية": "asyncio.create_subprocess_exec",
    "أنشئ_عملية_قشرة": "asyncio.create_subprocess_shell",
    "انتظر_عملية": "process.wait",
    "تواصل_عملية": "process.communicate",
    "أرسل_إشارة_عملية": "process.send_signal",
    "اقتل_عملية": "process.kill",
    "انتهت_عملية": "process.returncode",
    "خطأ_معياري": "process.stderr",
    "خرج_معياري": "process.stdout",
    "دخل_معياري": "process.stdin",
    "اكتب_لعملية": "process.stdin.write",
    
    # المهلة (Timeout)
    "مهلة": "asyncio.timeout",
    "داخل_مهلة": "async with asyncio.timeout",
    "انتهت_مهلة": "asyncio.TimeoutError",
    "ألغى": "asyncio.CancelledError",
    "ألغى_مهمة": "asyncio.CancelledError",
    
    # الانتظار
    "انتظر_مجموعة": "asyncio.wait",
    "اجمع_مهام": "asyncio.gather",
    "أول_مكتمل": "asyncio.wait",
    "أول_استثناء": "asyncio.wait",
    "اكتمل_الكل": "asyncio.wait",
    "انتظر_أول": "asyncio.wait",
    "مهام_مكتملة": "done",
    "مهام_معلقة": "pending",
    
    # الأداء
    "قياس_وقت": "asyncio.get_event_loop().time",
    "وقت_حلقة": "loop.time",
    "أنشئ_مستقبل": "loop.create_future",
    "مستقبل_مكتمل": "future.done",
    "مستقبل_ملغى": "future.cancelled",
    "نتيجة_مستقبل": "future.result",
    "استثناء_مستقبل": "future.exception",
    "ضع_نتيجة": "future.set_result",
    "ضع_استثناء": "future.set_exception",
    "أضف_مستقبل": "future.add_done_callback",
    "أزل_مستقبل": "future.remove_done_callback",
    
    # الخادم
    "أنشئ_خادم": "asyncio.start_server",
    "أغلق_خادم": "server.close",
    "انتظر_خادم": "server.serve_forever",
    "أغلق_اتصالات": "server.close_clients",
    
    # العميل
    "افتح_اتصال": "asyncio.open_connection",
    "أغلق_اتصال": "writer.close",
    "اكتب_اتصال": "writer.write",
    "اقرأ_اتصال": "reader.read",
    "اقرأ_سطر": "reader.readline",
    "اقرأ_كل": "reader.readexactly",
    
    # المهام المتزامنة
    "تزامن": "asyncio.Lock",
    "غير_متزامن": "async with",
    
    # التعامل مع الأخطاء
    "استثناء": "Exception",
    "ألقى_استثناء": "raise",
    "حاول": "try",
    "إلا": "except",
    "أخيرا": "finally",
    "ضمني": "async with",
}

ASYNCIO_PATTERN = r"(?<!\w)(" + "|".join(sorted(ASYNCIO_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

ASYNCIO_HELP = [
    "# === الدوال الأساسية ===",
    "شغل(دالة)              - تشغيل دالة غير متزامنة",
    "أنشئ_مهمة(دالة)       - إنشاء مهمة",
    "انتظر(مهمة)            - انتظار مهمة",
    "انتظر_أي(مهمة, مهلة)   - انتظار مع مهلة",
    "اجمع(مهام)             - جمع مهام",
    "نوم(ثوان)              - نوم لثواني",
    "# === المهام ===",
    "ألغى_مهمة(مهمة)       - إلغاء مهمة",
    "حالة_مهمة(مهمة)        - حالة المهمة",
    "نتيجة_مهمة(مهمة)      - نتيجة المهمة",
    "# === القفل ===",
    "قفل()                   - إنشاء قفل",
    "امتلك()                - امتلاك القفل",
    "أطلق()                - إطلاق القفل",
    "# === الطابور ===",
    "طابور()                - إنشاء طابور",
    "ضع_في_طابور(عنصر)     - وضع عنصر",
    "احصل_من_طابور()        - الحصول عنصر",
    "# === المؤقت ===",
    "مؤقت(ثوان, دالة)      - مؤقت",
    "# === الشرط ===",
    "شرط()                   - إنشاء شرط",
    "انتظر_شرط()            - انتظار الشرط",
    "أبلغ_شرط()            - إبلاغ الشرط",
    "# === العمليات ===",
    "أنشئ_عملية(برنامج)    - إنشاء عملية",
    "انتظر_عملية(عملية)    - انتظار عملية",
    "تواصل_عملية(عملية)    - تواصل مع عملية",
]

IMPORT_NAME = "asyncio"
IMPORT_CHECK = "asyncio\."
IMPORT_STATEMENT = "import asyncio"

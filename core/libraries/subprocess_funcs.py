"""
APL - Subprocess Library
Full subprocess wrapper with Arabic keywords
"""

SUBPROCESS_FUNCS = {
    # الإنشاء الأساسي
    "أنشئ_عملية_أوامر": "subprocess.run",
    "عملية": "subprocess.run",
    "نفذ_أوامر": "subprocess.run",
    "شغل_أوامر": "subprocess.run",
    
    # العملية الأساسية
    "Process": "subprocess.Popen",
    "أنشئ_Process": "subprocess.Popen",
    
    # الخصائص
    "حجة_أوامر": "args",
    "قشرة": "shell",
    "انتظر_أوامر": "timeout",
    "ترميز_أوامر": "encoding",
    "ترميز_خطأ": "errors",
    "مدخل": "stdin",
    "مخرج": "stdout",
    "خطأ_أوامر": "stderr",
    "دليل": "cwd",
    "متغيرات_بيئة": "env",
    "تجميع_مخرج": "text",
    "كائن_ثنائي": "text",
    "التقاط": "capture_output",
    "مدخل_نصي": "input",
    
    # العمليات
    "اتصل_أوامر": "process.communicate",
    "أرسل": "process.communicate",
    "انتظر_إنهاء": "process.wait",
    "ألغى_أوامر": "process.terminate",
    "اقتل": "process.kill",
    "أرسل_إشارة": "process.send_signal",
    "إشارة_أوامر": "process.send_signal",
    "رمز_العودة": "process.returncode",
    "pid": "process.pid",
    "معرف": "process.pid",
    
    # الإشارات
    "SIGTERM": "signal.SIGTERM",
    "SIGKILL": "signal.SIGKILL",
    "SIGINT": "signal.SIGINT",
    
    # الأجهزة
    "PIPE": "subprocess.PIPE",
    "STDOUT": "subprocess.STDOUT",
    "DEVNULL": "subprocess.DEVNULL",
    
    # الخصائص الخاصة
    "CreationFlags": "creationflags",
    "ShowWindow": "subprocess.SW_HIDE",
    
    # التحقق
    "تم_إنهاء": "process.poll",
    "انتهى": "process.poll",
    "نشط_أوامر": "process.poll",
    
    # الأخطاء
    "CalledProcessError": "subprocess.CalledProcessError",
    "ExpiredTimeout": "subprocess.TimeoutExpired",
    "FileNotFoundError": "FileNotFoundError",
    
    # التوجيه
    "تحويل_أوامر": "stderr_to_stdout",
    "دمج": "merge_outputs",
    
    # الخصائص الإضافية
    "universal_newlines": "text",
    "creationflags": "creationflags",
    "close_fds": "close_fds",
    "preexec_fn": "preexec_fn",
    "startupinfo": "startupinfo",
    "restore_signals": "restore_signals",
    "start_new_session": "start_new_session",
    "group": "group",
    "extra_groups": "extra_groups",
    "user": "user",
    "umask": "umask",
    "process_group": "process_group",
    
    # المدخلات
    "stdin": "stdin",
    "stdout": "stdout",
    "stderr": "stderr",
    
    # المخرجات
    "خرج_معياري_أوامر": "stdout",
    "خطأ_معياري_أوامر": "stderr",
    "دخرج_وخطأ": "stdout_and_stderr",
    
    # التحقق من الحالة
    "نجاح_أوامر": "returncode == 0",
    "فشل_أوامر": "returncode != 0",
    "رمز_نجاح": "0",
    
    # إدارة العمليات
    "عمليات_فرعية": "subprocess",
    "Popen": "subprocess.Popen",
    "call": "subprocess.call",
    "check_call": "subprocess.check_call",
    "check_output": "subprocess.check_output",
    "getoutput": "subprocess.getoutput",
    "getstatusoutput": "subprocess.getstatusoutput",
}

SUBPROCESS_PATTERN = r"(?<![\w.\u0600-\u06FF])(" + "|".join(sorted(SUBPROCESS_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

SUBPROCESS_HELP = [
    "# === الإنشاء ===",
    "أنشئ_عملية_أوامر(أمر)        - تشغيل أمر",
    "عملية(أمر)              - عملية (مختصر)",
    "نفذ_أوامر(أمر)                - تنفيذ أمر",
    "Process(أمر)            - إنشاء Process",
    "# === الخصائص ===",
    "حجة_أوامر(قائمة)              - حجة_أوامر الأمر",
    "قشرة(صحيح)              - استخدام القشرة",
    "انتظر_أوامر(ثوان)             - مهلة الانتظار",
    "دليل(مسار)              - دليل العمل",
    "متغيرات_بيئة(قاموس)     - متغيرات البيئة",
    "التقاط(صحيح)           - التقاط المخرجات",
    "مدخل(نص)                - مدخل العملية",
    "# === التنفيذ ===",
    "اتصل_أوامر()                  - تواصل مع العملية",
    "انتظر_إنهاء()            - انتظار الإنهاء",
    "ألغى_أوامر()                  - إنهاء العملية",
    "اقتل()                  - قتل العملية",
    "أرسل_إشارة(إشارة_أوامر)       - إرسال إشارة_أوامر",
    "# === الحالة ===",
    "رمز_العودة()            - رمز العودة",
    "pid()                    - معرف العملية",
    "تم_إنهاء()              - هل انتهت العملية",
    "# === المخرجات ===",
    "خرج_معياري_أوامر()            - الخرج المعياري",
    "خطأ_معياري_أوامر()            - الخطأ المعياري",
    "دخرج_وخطأ()            - دمج المخرجات",
    "# === الإشارات ===",
    "SIGTERM                  - إشارة_أوامر إنهاء",
    "SIGKILL                  - إشارة_أوامر قتل",
    "SIGINT                   - إشارة_أوامر مقاطعة",
    "# === الأجهزة ===",
    "PIPE                     - أنبوب",
    "STDOUT                   - خرج معياري",
    "DEVNULL                  - لا شيء",
    "# === التحقق ===",
    "نجاح_أوامر()                   - نجاح_أوامر العملية",
    "فشل_أوامر()                    - فشل_أوامر العملية",
    "رمز_نجاح                 - رمز النجاح (0)",
]

IMPORT_NAME = "subprocess"
IMPORT_CHECK = "subprocess\."
IMPORT_STATEMENT = "import subprocess"

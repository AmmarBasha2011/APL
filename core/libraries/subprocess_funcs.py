"""
APL - Subprocess Library
Full subprocess wrapper with Arabic keywords
"""

SUBPROCESS_FUNCS = {
    # الإنشاء الأساسي
    "أنشئ_عملية": "subprocess.run",
    "عملية": "subprocess.run",
    "نفذ": "subprocess.run",
    "شغل": "subprocess.run",
    
    # العملية الأساسية
    "Process": "subprocess.Popen",
    "أنشئ_Process": "subprocess.Popen",
    
    # الخصائص
    "حجة": "args",
    "قشرة": "shell",
    "انتظر": "timeout",
    "ترميز": "encoding",
    "ترميز_خطأ": "errors",
    "مدخل": "stdin",
    "مخرج": "stdout",
    "خطأ": "stderr",
    "دليل": "cwd",
    "متغيرات_بيئة": "env",
    "تجميع_مخرج": "text",
    "كائن_ثنائي": "text",
    "التقاط": "capture_output",
    "مدخل_نصي": "input",
    
    # العمليات
    "اتصل": "process.communicate",
    "أرسل": "process.communicate",
    "انتظر_إنهاء": "process.wait",
    "ألغى": "process.terminate",
    "اقتل": "process.kill",
    "أرسل_إشارة": "process.send_signal",
    "إشارة": "process.send_signal",
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
    "نشط": "process.poll",
    
    # الأخطاء
    "CalledProcessError": "subprocess.CalledProcessError",
    "ExpiredTimeout": "subprocess.TimeoutExpired",
    "FileNotFoundError": "FileNotFoundError",
    
    # التوجيه
    "تحويل": "stderr_to_stdout",
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
    "خرج_معياري": "stdout",
    "خطأ_معياري": "stderr",
    "دخرج_وخطأ": "stdout_and_stderr",
    
    # التحقق من الحالة
    "نجاح": "returncode == 0",
    "فشل": "returncode != 0",
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

SUBPROCESS_PATTERN = r"(?<!\w)(" + "|".join(sorted(SUBPROCESS_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

SUBPROCESS_HELP = [
    "# === الإنشاء ===",
    "أنشئ_عملية(أمر)        - تشغيل أمر",
    "عملية(أمر)              - عملية (مختصر)",
    "نفذ(أمر)                - تنفيذ أمر",
    "Process(أمر)            - إنشاء Process",
    "# === الخصائص ===",
    "حجة(قائمة)              - حجة الأمر",
    "قشرة(صحيح)              - استخدام القشرة",
    "انتظر(ثوان)             - مهلة الانتظار",
    "دليل(مسار)              - دليل العمل",
    "متغيرات_بيئة(قاموس)     - متغيرات البيئة",
    "التقاط(صحيح)           - التقاط المخرجات",
    "مدخل(نص)                - مدخل العملية",
    "# === التنفيذ ===",
    "اتصل()                  - تواصل مع العملية",
    "انتظر_إنهاء()            - انتظار الإنهاء",
    "ألغى()                  - إنهاء العملية",
    "اقتل()                  - قتل العملية",
    "أرسل_إشارة(إشارة)       - إرسال إشارة",
    "# === الحالة ===",
    "رمز_العودة()            - رمز العودة",
    "pid()                    - معرف العملية",
    "تم_إنهاء()              - هل انتهت العملية",
    "# === المخرجات ===",
    "خرج_معياري()            - الخرج المعياري",
    "خطأ_معياري()            - الخطأ المعياري",
    "دخرج_وخطأ()            - دمج المخرجات",
    "# === الإشارات ===",
    "SIGTERM                  - إشارة إنهاء",
    "SIGKILL                  - إشارة قتل",
    "SIGINT                   - إشارة مقاطعة",
    "# === الأجهزة ===",
    "PIPE                     - أنبوب",
    "STDOUT                   - خرج معياري",
    "DEVNULL                  - لا شيء",
    "# === التحقق ===",
    "نجاح()                   - نجاح العملية",
    "فشل()                    - فشل العملية",
    "رمز_نجاح                 - رمز النجاح (0)",
]

IMPORT_NAME = "subprocess"
IMPORT_CHECK = "subprocess\."
IMPORT_STATEMENT = "import subprocess"

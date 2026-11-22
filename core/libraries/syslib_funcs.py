"""
APL — مكتبة النظام والتشغيل والتشخيص (syslib)
==========================================

تُترجم الكلمات العربية إلى أدوات النظام والتشغيل والتشخيص:

    platform
    sysconfig
    site
    pkgutil
    runpy
    getopt
    signal
    select
    selectors
    resource
    errno
    mmap
    stat
    filecmp
    fileinput
    fcntl
    pty
    tty
    shlex
    cmd
    readline
    rlcompleter
    zipapp
    venv
    ensurepip
    types
    numbers
    abc
    copy
    copyreg
    contextlib
    contextvars
    graphlib
    dataclasses
    enum
    typing
    ctypes
    ctypes.wintypes
    multiprocessing
    multiprocessing.pool
    multiprocessing.managers
    multiprocessing.shared_memory
    multiprocessing.connection
    multiprocessing.synchronize
    concurrent.futures
    sched
    logging
    logging.handlers
    logging.config
    unittest
    unittest.mock
    unittest.loader
    unittest.runner
    unittest.case
    unittest.suite
    unittest.result
    pydoc
    reprlib
    difflib
    unicodedata
    stringprep
    io

التجميع كما في كل مكتبات APL:

    SYS_FUNCS      نداءات على مستوى الوحدة والأصناف
    SYS_METHODS    دوال الكائن بعد نقطة
    SYS_PROPS      خصائص وسمات أصناف بلا أقواس
    SYS_CONSTS     ثوابت تُكتب عارية

عدد العناصر: 3973 (793 نداء + 1609 طريقة + 488 خاصية + 1083 ثابت).
كل عنصر تم التحقق منه آلياً مقابل الكائن الحقيقي في Python.
"""

import re


SYS_FUNCS = {
    # نداءات الوحدة والأصناف
    # === abc ===
    "ABC_3": "abc.ABC",
    "ABC_احصل_ذاكرة_مؤقتة_رمز": "abc.get_cache_token",
    "ABC_حدّث_دوال_مجردة": "abc.update_abstractmethods",
    "ABC_خاصية_مجردة": "abc.abstractproperty",
    "ABC_دالة_ساكنة_مجردة": "abc.abstractstaticmethod",
    "ABC_دالة_صنف_مجردة": "abc.abstractclassmethod",
    # === ctypes ===
    "C_بايت": "ctypes.c_byte",
    "C_بايت_غير_سالب": "ctypes.c_ubyte",
    "C_حجم_T": "ctypes.c_size_t",
    "C_حرف": "ctypes.c_char",
    "C_حقل": "ctypes.CField",
    "C_صحيح16": "ctypes.c_int16",
    "C_صحيح16_غير_سالب": "ctypes.c_uint16",
    "C_صحيح64": "ctypes.c_int64",
    "C_صحيح_غير_سالب": "ctypes.c_uint",
    "C_عائم": "ctypes.c_float",
    "C_عائم_مركّب": "ctypes.c_float_complex",
    "C_عائم_مضاعف": "ctypes.c_longdouble",
    "C_عائم_مضاعف_مركّب": "ctypes.c_longdouble_complex",
    "C_محرف_عريض": "ctypes.c_wchar",
    "C_محرف_عريض_P": "ctypes.c_wchar_p",
    "C_مخزن_مؤقت": "ctypes.c_buffer",
    "C_مزدوج": "ctypes.c_double",
    "C_مزدوج_مركّب": "ctypes.c_double_complex",
    "C_منطقي": "ctypes.c_bool",
    # === pydoc ===
    "HTML_تمثيل": "pydoc.HTMLRepr",
    "HTML_توثيق": "pydoc.HTMLDoc",
    # === difflib ===
    "HTML_فرق": "difflib.HtmlDiff",
    # === multiprocessing ===
    "I_خريطة_غير_مرتّب_مكرّر": "multiprocessing.pool.IMapUnorderedIterator",
    "I_خريطة_مكرّر": "multiprocessing.pool.IMapIterator",
    # === ctypes ===
    "LPBOOL": "ctypes.wintypes.LPBOOL",
    "LPBYTE": "ctypes.wintypes.LPBYTE",
    "LPCOLORREF": "ctypes.wintypes.LPCOLORREF",
    "LPFILETIME": "ctypes.wintypes.LPFILETIME",
    "LPHANDLE": "ctypes.wintypes.LPHANDLE",
    "LPINT": "ctypes.wintypes.LPINT",
    "LPMSG": "ctypes.wintypes.LPMSG",
    "LPPOINT": "ctypes.wintypes.LPPOINT",
    "LPRECT": "ctypes.wintypes.LPRECT",
    "LPSIZE": "ctypes.wintypes.LPSIZE",
    "LPUINT": "ctypes.wintypes.LPUINT",
    "LPWIN_32_ابحث_بيانات_a": "ctypes.wintypes.LPWIN32_FIND_DATAA",
    "LPWIN_32_ابحث_بيانات_w": "ctypes.wintypes.LPWIN32_FIND_DATAW",
    "LPWORD": "ctypes.wintypes.LPWORD",
    # === multiprocessing ===
    "MAP_نجمة_نجمية": "multiprocessing.pool.starmapstar",
    # === logging ===
    "NT_حدث_سجل_معالج": "logging.handlers.NTEventLogHandler",
    # === ctypes ===
    "PY_كائن": "ctypes.py_object",
    "PY_مكتبة_ديناميكية": "ctypes.PyDLL",
    "RGB": "ctypes.wintypes.RGB",
    # === multiprocessing ===
    "R_اقفل": "multiprocessing.RLock",
    # === logging ===
    "SMTP_معالج": "logging.handlers.SMTPHandler",
    # === stat ===
    "S_IMODE": "stat.S_IMODE",
    "S_نوع_ملف": "stat.S_IFMT",
    "S_هو_أنبوب": "stat.S_ISFIFO",
    "S_هو_باب": "stat.S_ISDOOR",
    "S_هو_جهاز_حرفي": "stat.S_ISCHR",
    "S_هو_جهاز_كتلي": "stat.S_ISBLK",
    "S_هو_رابط_صلب": "stat.S_ISLNK",
    "S_هو_سوار": "stat.S_ISWHT",
    "S_هو_مجلد": "stat.S_ISDIR",
    "S_هو_مقبس": "stat.S_ISSOCK",
    "S_هو_ملف_عادي": "stat.S_ISREG",
    "S_هو_منفذ": "stat.S_ISPORT",
    # === multiprocessing ===
    "XML_عميل": "multiprocessing.connection.XmlClient",
    "XML_مُستمع": "multiprocessing.connection.XmlListener",
    # === ctypes ===
    "c_صحيح": "ctypes.c_int",
    "c_عدم": "ctypes.c_void_p",
    "c_نص": "ctypes.c_char_p",
    # === multiprocessing ===
    "mapstar": "multiprocessing.pool.mapstar",
    # === signal ===
    "pidfd_أرسل_إشارة": "signal.pidfd_send_signal",
    # === unittest ===
    "آمن_تمثيل": "unittest.mock.safe_repr",
    # === multiprocessing ===
    "أب_عالج": "multiprocessing.parent_process",
    # === platform ===
    "أبطِل_ذاكرة_مؤقتة": "platform.invalidate_caches",
    # === fileinput ===
    "أدخل_من_ملفات": "fileinput.input",
    # === readline ===
    "أدخل_نص": "readline.insert_text",
    # === unittest ===
    "أدرج_موعداً_وحدة_سياق": "unittest.enterModuleContext",
    # === pkgutil ===
    "أدوات_الحزم_صف_مسمّى": "pkgutil.namedtuple",
    # === contextlib ===
    "أدوات_السياق_إغلاق_غير_متزامن": "contextlib.aclosing",
    "أدوات_السياق_اخرج_مكدس": "contextlib.ExitStack",
    "أدوات_السياق_سياق_مُزيّن": "contextlib.ContextDecorator",
    "أدوات_السياق_غلاف": "contextlib.wraps",
    "أدوات_السياق_غير_متزامن_اخرج_مكدس": "contextlib.AsyncExitStack",
    "أدوات_السياق_غير_متزامن_سياق_مُزيّن": "contextlib.AsyncContextDecorator",
    "أدوات_السياق_غيّر_المجلد": "contextlib.chdir",
    "أدوات_السياق_مجرد_سياق_مدير": "contextlib.AbstractContextManager",
    "أدوات_السياق_مجرد_غير_متزامن_سياق_مدير": "contextlib.AbstractAsyncContextManager",
    "أدوات_السياق_مدير_سياق_غير_متزامن": "contextlib.asynccontextmanager",
    # === zipapp ===
    "أرشيف_مضغوط_تطبيق_خطأ": "zipapp.ZipAppError",
    # === unittest ===
    "أساس": "unittest.mock.Base",
    "أساس_اختبر_حزمة": "unittest.BaseTestSuite",
    # === logging ===
    "أساس_دوّار_معالج": "logging.handlers.BaseRotatingHandler",
    # === multiprocessing ===
    "أساس_قائمة_وكيل": "multiprocessing.managers.BaseListProxy",
    "أساس_مجموعة_وكيل": "multiprocessing.managers.BasePoolProxy",
    "أساس_مدير": "multiprocessing.managers.BaseManager",
    # === logging ===
    "أساس_مُضبط": "logging.config.BaseConfigurator",
    # === selectors ===
    "أساس_مُنتخِب": "selectors.BaseSelector",
    # === multiprocessing ===
    "أساس_وكيل": "multiprocessing.managers.BaseProxy",
    # === site ===
    "أضف_حزم_مستخدم": "site.addusersitepackages",
    "أضف_حزم_موقع": "site.addsitepackages",
    "أضف_حزمة": "site.addpackage",
    # === readline ===
    "أضف_ذيلياً_سجل_ملف": "readline.append_history_file",
    # === site ===
    "أضف_مجلد_موقع": "site.addsitedir",
    # === logging ===
    "أضف_مستوى_اسم": "logging.addLevelName",
    # === unittest ===
    "أضف_وحدة_نظّف": "unittest.addModuleCleanup",
    # === enum ===
    "أظهر_علامة_قيم": "enum.show_flag_values",
    # === multiprocessing ===
    "أعد_البناء_اتصال": "multiprocessing.connection.rebuild_connection",
    "أعد_البناء_استثناء": "multiprocessing.pool.rebuild_exc",
    "أعد_البناء_كـ_قائمة": "multiprocessing.managers.rebuild_as_list",
    "أعد_البناء_وكيل": "multiprocessing.managers.RebuildProxy",
    # === contextlib ===
    "أعد_توجيه_الإخراج": "contextlib.redirect_stdout",
    "أعد_توجيه_الخطأ": "contextlib.redirect_stderr",
    # === numbers ===
    "أعداد_حقيقي": "numbers.Real",
    "أعداد_صحيح": "numbers.Integral",
    "أعداد_عدد": "numbers.Number",
    "أعداد_مركّب": "numbers.Complex",
    "أعداد_نسبي": "numbers.Rational",
    # === readline ===
    "أعيد_العرض": "readline.redisplay",
    # === signal ===
    "أقنعة_الإشارات": "signal.Sigmasks",
    # === multiprocessing ===
    "أنبوب": "multiprocessing.Pipe",
    # === pydoc ===
    "أنبوب_صفّاح": "pydoc.pipe_pager",
    # === platform ===
    "أندرويد_إصدار": "platform.AndroidVer",
    # === venv ===
    "أنشئ": "venv.create",
    # === unittest ===
    "أنشئ_مخطط_تلقائي": "unittest.mock.create_autospec",
    # === ctypes ===
    "أنشئ_يونيكود_مخزن_مؤقت": "ctypes.create_unicode_buffer",
    # === types ===
    "أنواع_اتحاد_نوع": "types.UnionType",
    "أنواع_تعاونية": "types.coroutine",
    "أنواع_جديد_صنف": "types.new_class",
    "أنواع_جهّز_صنف": "types.prepare_class",
    "أنواع_ديناميكي_صنف_سمة": "types.DynamicClassAttribute",
    # === logging ===
    "أوقف_يستمع": "logging.config.stopListening",
    # === typing ===
    "أي": "typing.Any",
    # === select ===
    "إبول": "select.epoll",
    # === typing ===
    "إثقال": "typing.overload",
    # === multiprocessing ===
    "إجابة_تحدٍّ": "multiprocessing.connection.answer_challenge",
    # === typing ===
    "إدخال_إخراج": "typing.IO",
    # === io ===
    "إدخال_إخراج_أساس_2": "io.IOBase",
    # === platform ===
    "إدخال_إخراج_إصدار": "platform.ios_ver",
    "إدخال_إخراج_إصدار_معلومات": "platform.IOSVersionInfo",
    # === io ===
    "إدخال_إخراج_افتح_كود": "io.open_code",
    "إدخال_إخراج_تصاعدي_سطر_جديد_مفكّك": "io.IncrementalNewlineDecoder",
    "إدخال_إخراج_غير_مدعوم_عملية": "io.UnsupportedOperation",
    "إدخال_إخراج_قارئ": "io.Reader",
    "إدخال_إخراج_كاتب": "io.Writer",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي": "io.BufferedRandom",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج": "io.BufferedRWPair",
    "إدخال_إخراج_نص_ترميز": "io.text_encoding",
    # === fileinput ===
    "إدخال_اسم_ملف_2": "fileinput.filename",
    # === signal ===
    "إشارات": "signal.Signals",
    # === multiprocessing ===
    "إشارة_مرور": "multiprocessing.Semaphore",
    "إشارة_مرور_اقفل": "multiprocessing.synchronize.SemLock",
    "إشارة_مرور_فكّ_الرابط": "multiprocessing.synchronize.sem_unlink",
    # === signal ===
    "إشارة_معالجات": "signal.Handlers",
    # === platform ===
    "إصدار_بايثون": "platform.python_version",
    # === sysconfig ===
    "إعداد_النظام_مسار_حقيقي": "sysconfig.realpath",
    # === ensurepip ===
    "إقلاع": "ensurepip.bootstrap",
    # === dataclasses ===
    "ابدأ_تهيئة_متغير": "dataclasses.InitVar",
    # === multiprocessing ===
    "اتصال_غلاف": "multiprocessing.connection.ConnectionWrapper",
    # === tty ===
    "اجعل_تفعيل_حرفي": "tty.cfmakecbreak",
    "اجعل_خام": "tty.cfmakeraw",
    # === site ===
    "احذف_المسارات_المكررة": "site.removeduppaths",
    # === pydoc ===
    "احذف_المعرف": "pydoc.stripid",
    # === readline ===
    "احذف_سجل_عنصر": "readline.remove_history_item",
    # === unittest ===
    "احذف_معالج": "unittest.removeHandler",
    "احذف_نتيجة": "unittest.removeResult",
    # === types ===
    "احصل_أصلي_أسس": "types.get_original_bases",
    # === typing ===
    "احصل_إثقال": "typing.get_overloads",
    # === sysconfig ===
    "احصل_إعداد_H_اسم_ملف": "sysconfig.get_config_h_filename",
    "احصل_إعداد_متغير": "sysconfig.get_config_var",
    "احصل_إعداد_متغيرات": "sysconfig.get_config_vars",
    # === readline ===
    "احصل_إكمال_نوع": "readline.get_completion_type",
    # === multiprocessing ===
    "احصل_ابدأ_دالة": "multiprocessing.get_start_method",
    # === sysconfig ===
    "احصل_اعمل_ملفاً_اسم_ملف": "sysconfig.get_makefile_filename",
    "احصل_افتراضي_مخطط": "sysconfig.get_default_scheme",
    "احصل_بايثون_إصدار": "sysconfig.get_python_version",
    # === readline ===
    "احصل_بداية_الفهرس": "readline.get_begidx",
    # === typing ===
    "احصل_بروتوكول_أعضاء": "typing.get_protocol_members",
    # === pkgutil ===
    "احصل_بيانات": "pkgutil.get_data",
    # === multiprocessing ===
    "احصل_توليد_افتح_عملية": "multiprocessing.managers.get_spawning_popen",
    # === readline ===
    "احصل_حالي_سجل_طول": "readline.get_current_history_length",
    # === logging ===
    "احصل_سجل_سجل_مصنع": "logging.getLogRecordFactory",
    # === readline ===
    "احصل_سجل_طول": "readline.get_history_length",
    "احصل_سجل_عنصر": "readline.get_history_item",
    # === unittest ===
    "احصل_سمة_ظاهرية": "unittest.runner.get_theme",
    # === multiprocessing ===
    "احصل_سياق": "multiprocessing.get_context",
    # === pydoc ===
    "احصل_صفّاح": "pydoc.get_pager",
    # === rlcompleter ===
    "احصل_صنف_أعضاء": "rlcompleter.get_class_members",
    # === difflib ===
    "احصل_على_أقرب_التطابقات_2": "difflib.get_close_matches",
    # === resource ===
    "احصل_على_الاستخدام": "resource.getrusage",
    # === pydoc ===
    "احصل_على_التوثيق": "pydoc.getdoc",
    # === getopt ===
    "احصل_على_الخيارات": "getopt.getopt",
    "احصل_على_الخيارات_خطأ": "getopt.GetoptError",
    # === readline ===
    "احصل_على_السطر": "readline.get_line_buffer",
    # === signal ===
    "احصل_على_المؤقّت": "signal.getitimer",
    # === resource ===
    "احصل_على_حجم_الصفحة": "resource.getpagesize",
    # === tty ===
    "احصل_على_حجم_النافذة": "tty.tcgetwinsize",
    # === resource ===
    "احصل_على_حد_المورد": "resource.getrlimit",
    # === site ===
    "احصل_على_حزم_الموقع": "site.getsitepackages",
    "احصل_على_حزم_موقع_المستخدم": "site.getusersitepackages",
    # === ctypes ===
    "احصل_على_رقم_الخطأ": "ctypes.get_errno",
    # === pty ===
    "احصل_على_سمات_الطرفية": "pty.tcgetattr",
    # === site ===
    "احصل_على_قاعدة_المستخدم": "site.getuserbase",
    # === logging ===
    "احصل_على_مسجّل": "logging.getLogger",
    # === signal ===
    "احصل_على_معالج_الإشارة": "signal.getsignal",
    # === multiprocessing ===
    "احصل_على_معرف_العملية": "multiprocessing.managers.getpid",
    # === site ===
    "احصل_على_ملف_السجل": "site.gethistoryfile",
    # === multiprocessing ===
    "احصل_كل_ابدأ_دوال": "multiprocessing.get_all_start_methods",
    # === sysconfig ===
    "احصل_مخطط_أسماء": "sysconfig.get_scheme_names",
    "احصل_مسار": "sysconfig.get_path",
    "احصل_مسار_أسماء": "sysconfig.get_path_names",
    "احصل_مسارات": "sysconfig.get_paths",
    # === logging ===
    "احصل_مستوى_أسماء_خريطة": "logging.getLevelNamesMapping",
    "احصل_مستوى_اسم": "logging.getLevelName",
    # === multiprocessing ===
    "احصل_مسجّل": "multiprocessing.get_logger",
    # === logging ===
    "احصل_مسجّل_صنف": "logging.getLoggerClass",
    "احصل_معالج_أسماء": "logging.getHandlerNames",
    "احصل_معالج_بواسطة_اسم": "logging.getHandlerByName",
    # === typing ===
    "احصل_معطيات": "typing.get_args",
    # === zipapp ===
    "احصل_مفسّر": "zipapp.get_interpreter",
    # === sysconfig ===
    "احصل_مفضّل_مخطط": "sysconfig.get_preferred_scheme",
    # === typing ===
    "احصل_منشأ": "typing.get_origin",
    # === pkgutil ===
    "احصل_مُستورد": "pkgutil.get_importer",
    # === readline ===
    "احصل_مُكمل": "readline.get_completer",
    "احصل_مُكمل_محددات": "readline.get_completer_delims",
    "احصل_نهاية_الفهرس": "readline.get_endidx",
    # === typing ===
    "احصل_نوع_تلميحات": "typing.get_type_hints",
    # === unittest ===
    "اختبارات_وحدة_تجاوز": "unittest.skip",
    "اختبارات_وحدة_محمّل_طابق_نمطياً": "unittest.loader.fnmatch",
    "اختبارات_وحدة_محمّل_طابق_نمطياً_بالحالة": "unittest.loader.fnmatchcase",
    "اختبارات_وحدة_نتيجة_فشل_سريع": "unittest.result.failfast",
    "اختبارات_وحدة_وهمي_R_اقفل": "unittest.mock.RLock",
    "اختبارات_وحدة_وهمي_هو_دالة_تعاونية": "unittest.mock.iscoroutinefunction",
    "اختبر_برنامج": "unittest.TestProgram",
    "اختبر_نتيجة": "unittest.TestResult",
    # === select ===
    "اختر_عدة": "select.select",
    # === selectors ===
    "اختر_مُنتخِب": "selectors.SelectSelector",
    # === multiprocessing ===
    "اختزل_اتصال": "multiprocessing.connection.reduce_connection",
    "اختزل_مصفوفة": "multiprocessing.managers.reduce_array",
    # === unittest ===
    "اختم": "unittest.mock.seal",
    # === signal ===
    "ارفع_إشارة": "signal.raise_signal",
    # === readline ===
    "استبدل_سجل_عنصر": "readline.replace_history_item",
    # === unittest ===
    "استبدل_مؤقتاً": "unittest.mock.patch",
    # === multiprocessing ===
    "استثناء_بـ_تتبع": "multiprocessing.pool.ExceptionWithTraceback",
    # === select ===
    "استطلع_الملفات": "select.poll",
    # === selectors ===
    "استطلع_مُنتخِب": "selectors.PollSelector",
    # === pydoc ===
    "استيراد_آمن": "pydoc.safeimport",
    "اسم_الأب": "pydoc.parentname",
    "اسم_الصنف": "pydoc.classname",
    # === unicodedata ===
    "اسم_المحرف_2": "unicodedata.name",
    # === platform ===
    "اسم_النظام_2": "platform.uname",
    "اسم_النظام_نتيجة": "platform.uname_result",
    # === pydoc ===
    "اسم_ظاهر": "pydoc.visiblename",
    # === multiprocessing ===
    "اسمح_اتصال_تحويل_بايكن": "multiprocessing.allow_connection_pickling",
    # === logging ===
    "اضبط_أساسياً": "logging.basicConfig",
    # === multiprocessing ===
    "اعتباطي_عنوان": "multiprocessing.connection.arbitrary_address",
    # === logging ===
    "اعمل_سجل_سجل": "logging.makeLogRecord",
    # === dataclasses ===
    "اعمل_صنف_بيانات": "dataclasses.make_dataclass",
    # === site ===
    "اعمل_مساراً": "site.makepath",
    # === multiprocessing ===
    "اعمل_وكيل_نوع": "multiprocessing.managers.MakeProxyType",
    # === io ===
    "افتح_2": "io.open",
    # === pty ===
    "افتح_طرفية_وهمية": "pty.openpty",
    # === signal ===
    "افتراضي_عدد_صحيح_معالج": "signal.default_int_handler",
    # === selectors ===
    "افتراضي_مُنتخِب": "selectors.DefaultSelector",
    # === pydoc ===
    "افصل_التوثيق": "pydoc.splitdoc",
    # === getopt ===
    "افعل_صحيحات_طويلة": "getopt.do_longs",
    "افعل_قصires": "getopt.do_shorts",
    # === unittest ===
    "افعل_وحدة_تنظيفات": "unittest.doModuleCleanups",
    # === shlex ===
    "اقتبس_حجة": "shlex.quote",
    # === readline ===
    "اقرأ_ابدأ_تهيئة_ملف": "readline.read_init_file",
    "اقرأ_سجل_ملف": "readline.read_history_file",
    # === pkgutil ===
    "اقرأ_كود": "pkgutil.read_code",
    # === contextlib ===
    "اكبح_2": "contextlib.suppress",
    # === pydoc ===
    "اكتب_التوثيق": "pydoc.writedoc",
    "اكتب_التوثيقات": "pydoc.writedocs",
    # === readline ===
    "اكتب_سجل_ملف": "readline.write_history_file",
    # === typing ===
    "اكشف_نوع": "typing.reveal_type",
    # === multiprocessing ===
    "الأبناء_النشطون": "multiprocessing.active_children",
    # === signal ===
    "الإشارات_المعلقة": "signal.sigpending",
    # === logging ===
    "التقط_تحذيرات": "logging.captureWarnings",
    # === multiprocessing ===
    "العملية_الحالية": "multiprocessing.current_process",
    # === concurrent ===
    "المكتملة": "concurrent.futures.as_completed",
    # === platform ===
    "المنصة": "platform.platform",
    # === typing ===
    "امسح_إثقال": "typing.clear_overloads",
    # === readline ===
    "امسح_سجل": "readline.clear_history",
    # === pty ===
    "انتظر_PID": "pty.waitpid",
    # === signal ===
    "انتظر_إشارة": "signal.sigwait",
    # === tty ===
    "انتظر_الإفراغ": "tty.tcdrain",
    # === signal ===
    "انتظر_بإشارة": "signal.sigtimedwait",
    "انتظر_معلومات_إشارة": "signal.sigwaitinfo",
    # === ensurepip ===
    "انسخ2": "ensurepip.copy2",
    # === copy ===
    "انسخ_3": "copy.copy",
    "انسخ_استبدل_2": "copy.replace",
    # === contextvars ===
    "انسخ_السياق": "contextvars.copy_context",
    # === copy ===
    "انسخ_خطأ_2": "copy.Error",
    "انسخ_عميقاً_3": "copy.deepcopy",
    # === pydoc ===
    "بالأحرف_الأولى": "pydoc.apropos",
    # === ctypes ===
    "بالمرجع": "ctypes.byref",
    # === io ===
    "بايت_تدفق_2": "io.BytesIO",
    # === platform ===
    "بايثون_إصدار_صف": "platform.python_version_tuple",
    "بايثون_ابنِ": "platform.python_build",
    # === pydoc ===
    "بايثون_توثيق": "pydoc.Doc",
    "بايثون_توثيق_2": "pydoc.doc",
    # === platform ===
    "بايثون_فرع": "platform.python_branch",
    "بايثون_مترجم": "platform.python_compiler",
    "بايثون_مراجعة": "platform.python_revision",
    # === copyreg ===
    "بايكن": "copyreg.pickle",
    # === enum ===
    "بايكن_بواسطة_تعداد_اسم": "enum.pickle_by_enum_name",
    "بايكن_بواسطة_شامل_اسم": "enum.pickle_by_global_name",
    # === multiprocessing ===
    "بسيط_طابور": "multiprocessing.SimpleQueue",
    "بعيد_تتبع": "multiprocessing.pool.RemoteTraceback",
    "بعيد_خطأ": "multiprocessing.managers.RemoteError",
    # === typing ===
    "بلا_نوع_تحقق": "typing.no_type_check",
    "بلا_نوع_تحقق_مُزيّن": "typing.no_type_check_decorator",
    # === resource ===
    "بنية_استخدام": "resource.struct_rusage",
    # === signal ===
    "بنية_معلومات_الإشارة": "signal.struct_siginfo",
    # === site ===
    "بيئة_افتراضية": "site.venv",
    # === venv ===
    "بيئة_افتراضية_رئيسي": "venv.main",
    "بيئة_باني": "venv.EnvBuilder",
    # === unicodedata ===
    "بيانات_معيار_يونيكود": "unicodedata.UCD",
    "بيانات_يونيكود_بحث": "unicodedata.lookup",
    "بيانات_يونيكود_تفكيك_2": "unicodedata.decomposition",
    "بيانات_يونيكود_ثنائي_الاتجاه_2": "unicodedata.bidirectional",
    "بيانات_يونيكود_رقم": "unicodedata.digit",
    "بيانات_يونيكود_شرق_آسيوي_عرض": "unicodedata.east_asian_width",
    "بيانات_يونيكود_عددي": "unicodedata.numeric",
    "بيانات_يونيكود_عشري": "unicodedata.decimal",
    "بيانات_يونيكود_معكوس_2": "unicodedata.mirrored",
    "بيانات_يونيكود_مُركِّب": "unicodedata.combining",
    "بيانات_يونيكود_هو_موحّد": "unicodedata.is_normalized",
    # === typing ===
    "تأكد_مستحيل": "typing.assert_never",
    # === ensurepip ===
    "تثبيت_pip_إصدار": "ensurepip.version",
    "تثبيت_pip_سياق_فارغ": "ensurepip.nullcontext",
    # === typing ===
    "تجاوز": "typing.override",
    # === unittest ===
    "تجاوز_إذا": "unittest.skipIf",
    "تجاوز_إلا_إذا": "unittest.skipUnless",
    "تجاوز_اختبر": "unittest.SkipTest",
    # === pkgutil ===
    "تجوّل_حزم": "pkgutil.walk_packages",
    # === stringprep ===
    "تحضير_النص_خريطة_جدول_B2": "stringprep.map_table_b2",
    "تحضير_النص_خريطة_جدول_B3": "stringprep.map_table_b3",
    "تحضير_النص_في_جدول_A1": "stringprep.in_table_a1",
    "تحضير_النص_في_جدول_B1": "stringprep.in_table_b1",
    "تحضير_النص_في_جدول_D1": "stringprep.in_table_d1",
    "تحضير_النص_في_جدول_D2": "stringprep.in_table_d2",
    "تحضير_النص_في_جدول_توحيد11": "stringprep.in_table_c11",
    "تحضير_النص_في_جدول_توحيد11_توحيد12": "stringprep.in_table_c11_c12",
    "تحضير_النص_في_جدول_توحيد12": "stringprep.in_table_c12",
    "تحضير_النص_في_جدول_توحيد21": "stringprep.in_table_c21",
    "تحضير_النص_في_جدول_توحيد21_توحيد22": "stringprep.in_table_c21_c22",
    "تحضير_النص_في_جدول_توحيد22": "stringprep.in_table_c22",
    "تحضير_النص_في_جدول_توحيد3": "stringprep.in_table_c3",
    "تحضير_النص_في_جدول_توحيد4": "stringprep.in_table_c4",
    "تحضير_النص_في_جدول_توحيد5": "stringprep.in_table_c5",
    "تحضير_النص_في_جدول_توحيد6": "stringprep.in_table_c6",
    "تحضير_النص_في_جدول_توحيد7": "stringprep.in_table_c7",
    "تحضير_النص_في_جدول_توحيد8": "stringprep.in_table_c8",
    "تحضير_النص_في_جدول_توحيد9": "stringprep.in_table_c9",
    # === site ===
    "تحقق_فعّل_موقع_المستخدم": "site.check_enableusersite",
    # === fcntl ===
    "تحكم_إدخال": "fcntl.ioctl",
    # === tty ===
    "تحكم_الانسياب": "tty.tcflow",
    # === fcntl ===
    "تحكم_ملف": "fcntl.fcntl",
    # === shlex ===
    "تحليل_كلمات": "shlex.shlex",
    "تحليل_كلمات_اربط": "shlex.join",
    # === logging ===
    "تحويل_صف": "logging.config.ConvertingTuple",
    "تحويل_قاموس": "logging.config.ConvertingDict",
    "تحويل_مزيج": "logging.config.ConvertingMixin",
    "تخزين_مؤقت_معالج": "logging.handlers.BufferingHandler",
    "تخزين_مؤقت_مُنسّق": "logging.BufferingFormatter",
    # === unittest ===
    "ترابط_مزيج": "unittest.mock.ThreadingMixin",
    "ترابط_وهمي": "unittest.mock.ThreadingMock",
    # === concurrent ===
    "تزامن_مستقبلات_انتظر": "concurrent.futures.wait",
    "تزامن_مستقبلات_غير_صالح_حالة_خطأ": "concurrent.futures.InvalidStateError",
    # === logging ===
    "تسجيل_أوقف": "logging.shutdown",
    "تسجيل_إعداد_استمع": "logging.config.listen",
    "تسجيل_إعداد_تحويل_قائمة": "logging.config.ConvertingList",
    "تسجيل_استثناء": "logging.exception",
    "تسجيل_الإطار_الحالي": "logging.currentframe",
    # === copyreg ===
    "تسجيل_النسخ_أضف_امتداد": "copyreg.add_extension",
    "تسجيل_النسخ_احذف_امتداد": "copyreg.remove_extension",
    "تسجيل_النسخ_امسح_امتداد_ذاكرة_مؤقتة": "copyreg.clear_extension_cache",
    "تسجيل_النسخ_بايكن_أعلى": "copyreg.pickle_super",
    "تسجيل_النسخ_بايكن_اتحاد": "copyreg.pickle_union",
    "تسجيل_النسخ_بايكن_مركّب": "copyreg.pickle_complex",
    "تسجيل_النسخ_منشئ": "copyreg.constructor",
    # === logging ===
    "تسجيل_حذّر": "logging.warn",
    "تسجيل_سجل": "logging.log",
    "تسجيل_عطّل": "logging.disable",
    "تسجيل_عيّن_سجل_سجل_مصنع": "logging.setLogRecordFactory",
    "تسجيل_عيّن_مسجّل_صنف": "logging.setLoggerClass",
    "تسجيل_قاتل": "logging.fatal",
    "تسجيل_مدير": "logging.Manager",
    "تسجيل_مرشّح": "logging.Filterer",
    "تسجيل_معالج": "logging.Handler",
    "تسجيل_معالجات_HTTP_معالج": "logging.handlers.HTTPHandler",
    # === pydoc ===
    "تصفّح": "pydoc.browse",
    # === zipapp ===
    "تطبيق_مضغوط_أنشئ_أرشيف": "zipapp.create_archive",
    "تطبيق_مضغوط_رئيسي": "zipapp.main",
    # === enum ===
    "تعداد_2": "enum.Enum",
    "تعداد_تحقق": "enum.EnumCheck",
    "تعداد_تحقق_2": "enum.verify",
    "تعداد_تلقائي": "enum.auto",
    "تعداد_ثنائي": "enum.bin",
    "تعداد_علامة": "enum.Flag",
    "تعداد_فريد_2": "enum.unique",
    "تعداد_قاموس": "enum.EnumDict",
    "تعداد_وصفي": "enum.EnumMeta",
    # === pty ===
    "تفرّع": "pty.fork",
    # === multiprocessing ===
    "تلقائي_وكيل": "multiprocessing.managers.AutoProxy",
    # === enum ===
    "تمثيل_تعداد": "enum.ReprEnum",
    # === pydoc ===
    "توثيق_بايثون_استبدل": "pydoc.replace",
    "توثيق_بايثون_استيراد_ملف": "pydoc.importfile",
    "توثيق_بايثون_تمثيل": "pydoc.Repr",
    "توثيق_بايثون_صف": "pydoc.describe",
    "توثيق_بايثون_هو_حزمة": "pydoc.ispackage",
    # === multiprocessing ===
    "توزيع": "multiprocessing.managers.dispatch",
    # === signal ===
    "توقّف_حتى_إشارة": "signal.pause",
    # === unittest ===
    "ثبّت_معالج": "unittest.installHandler",
    # === typing ===
    "ثنائي_إدخال_إخراج": "typing.BinaryIO",
    # === platform ===
    "جافا_إصدار": "platform.java_ver",
    # === typing ===
    "جديد_نوع": "typing.NewType",
    # === logging ===
    "جذر_مسجّل": "logging.RootLogger",
    # === multiprocessing ===
    "جمّد_دعم": "multiprocessing.freeze_support",
    # === getopt ===
    "جنو_احصل_على_الخيارات": "getopt.gnu_getopt",
    # === multiprocessing ===
    "حاجز": "multiprocessing.Barrier",
    "حاجز_وكيل": "multiprocessing.managers.BarrierProxy",
    "حاصل_وكيل": "multiprocessing.managers.AcquirerProxy",
    # === unittest ===
    "حالة_اختبار_2": "unittest.TestCase",
    # === ctypes ===
    "حجة_خطأ": "ctypes.ArgumentError",
    "حجم": "ctypes.wintypes.SIZE",
    "حجم_النوع": "ctypes.sizeof",
    # === resource ===
    "حد_العمليات": "resource.prlimit",
    # === multiprocessing ===
    "حدث_وكيل": "multiprocessing.managers.EventProxy",
    # === pydoc ===
    "حدّد": "pydoc.locate",
    # === unittest ===
    "حزمة_اختبارات": "unittest.TestSuite",
    # === logging ===
    "حزمة_بيانات_معالج": "logging.handlers.DatagramHandler",
    # === sysconfig ===
    "حلل_إعداد_H": "sysconfig.parse_config_h",
    # === shlex ===
    "حلل_سطراً": "shlex.split",
    # === readline ===
    "حلل_و_اربط": "readline.parse_and_bind",
    # === pydoc ===
    "حلّ": "pydoc.resolve",
    # === types ===
    "حلّ_أسس": "types.resolve_bases",
    # === pkgutil ===
    "حلّ_اسم": "pkgutil.resolve_name",
    # === multiprocessing ===
    "حوّل_إلى_خطأ": "multiprocessing.managers.convert_to_error",
    # === typing ===
    "حوّل_نوع": "typing.cast",
    # === io ===
    "خام_إدخال_إخراج_أساس_2": "io.RawIOBase",
    # === multiprocessing ===
    "خام_قيمة": "multiprocessing.RawValue",
    "خام_مصفوفة": "multiprocessing.RawArray",
    "خريطة_نتيجة": "multiprocessing.pool.MapResult",
    # === pydoc ===
    "خطأ_أثناء_استيراد": "pydoc.ErrorDuringImport",
    "خلاصة": "pydoc.synopsis",
    # === signal ===
    "خيط_اقتل": "signal.pthread_kill",
    "خيط_قناع_الإشارات": "signal.pthread_sigmask",
    # === multiprocessing ===
    "خيط_مجموعة": "multiprocessing.pool.ThreadPool",
    # === unittest ===
    "دالة_اختبر_حالة": "unittest.FunctionTestCase",
    # === graphlib ===
    "دورة_خطأ": "graphlib.CycleError",
    # === logging ===
    "دوّار_ملف_معالج": "logging.handlers.RotatingFileHandler",
    "ذاكرة_معالج": "logging.handlers.MemoryHandler",
    # === mmap ===
    "ذاكرة_مُخزَّنة": "mmap.mmap",
    # === multiprocessing ===
    "ربما_ترميز_خطأ": "multiprocessing.pool.MaybeEncodingError",
    # === pydoc ===
    "رتّب_سمات": "pydoc.sort_attributes",
    # === logging ===
    "رشّح": "logging.Filter",
    # === multiprocessing ===
    "زامن_مدير": "multiprocessing.managers.SyncManager",
    # === typing ===
    "زمن_التشغيل_قابل_للتحديد": "typing.runtime_checkable",
    # === logging ===
    "سجل_2": "logging.LogRecord",
    # === multiprocessing ===
    "سجل_إلى_خطأ_قياسي": "multiprocessing.log_to_stderr",
    # === logging ===
    "سجّل_تحذيراً": "logging.warning",
    "سجّل_تصحيحاً": "logging.debug",
    "سجّل_حرجاً": "logging.critical",
    "سجّل_خطأ_2": "logging.error",
    # === site ===
    "سجّل_سطر_قراءة": "site.register_readline",
    # === logging ===
    "سجّل_معلومة": "logging.info",
    # === unittest ===
    "سجّل_نتيجة": "unittest.registerResult",
    "سحري_مزيج": "unittest.mock.MagicMixin",
    "سحري_وكيل": "unittest.mock.MagicProxy",
    "سحري_وهمي": "unittest.mock.MagicMock",
    # === platform ===
    "سطح_مكتب_حر_نظام_تشغيل_حرّر": "platform.freedesktop_os_release",
    # === cmd ===
    "سطر_أوامر": "cmd.Cmd",
    # === readline ===
    "سطر_قراءة_أضف_سجل": "readline.add_history",
    # === multiprocessing ===
    "سلّم_تحدٍّ": "multiprocessing.connection.deliver_challenge",
    # === enum ===
    "سمة_صنف": "enum.property",
    # === unittest ===
    "سمة_صنف_وهمي": "unittest.mock.PropertyMock",
    # === difflib ===
    "سياق_فرق": "difflib.context_diff",
    # === contextvars ===
    "سياق_متغيرات_رمز_2": "contextvars.Token",
    # === enum ===
    "شامل_تعداد": "enum.global_enum",
    "شامل_تعداد_تمثيل": "enum.global_enum_repr",
    "شامل_علامة_تمثيل": "enum.global_flag_repr",
    "شامل_نص": "enum.global_str",
    # === multiprocessing ===
    "شرط_وكيل": "multiprocessing.managers.ConditionProxy",
    # === runpy ===
    "شغّل_مسار": "runpy.run_path",
    "شغّل_وحدة": "runpy.run_module",
    # === signal ===
    "صالح_إشارات": "signal.valid_signals",
    # === logging ===
    "صالح_معرّف": "logging.config.valid_ident",
    # === ctypes ===
    "صغير_ترتيب_البايتات_اتحاد": "ctypes.LittleEndianUnion",
    "صغير_ترتيب_البايتات_بنية": "ctypes.LittleEndianStructure",
    "صغير_مستطيل": "ctypes.wintypes.SMALL_RECT",
    # === pydoc ===
    "صفّاح": "pydoc.pager",
    # === dataclasses ===
    "صنف_بيانات": "dataclasses.dataclass",
    "صنف_بيانات_استبدل": "dataclasses.replace",
    "صنف_بيانات_تكراري_تمثيل": "dataclasses.recursive_repr",
    "صنف_بيانات_حقل": "dataclasses.Field",
    "صنف_بيانات_حقل_2": "dataclasses.field",
    "صنف_بيانات_حقول": "dataclasses.fields",
    # === typing ===
    "صنف_بيانات_حوّل": "typing.dataclass_transform",
    # === pydoc ===
    "صنّف_صنف_سمات": "pydoc.classify_class_attrs",
    "صيّر_توثيقاً": "pydoc.render_doc",
    # === logging ===
    "ضع_حامل": "logging.PlaceHolder",
    # === multiprocessing ===
    "طابور_عمليات": "multiprocessing.Queue",
    # === logging ===
    "طابور_معالج": "logging.handlers.QueueHandler",
    "طابور_مُستمع": "logging.handlers.QueueListener",
    # === multiprocessing ===
    "طبّق_نتيجة": "multiprocessing.pool.ApplyResult",
    # === tty ===
    "طرفية_أرسل_فاصلة": "tty.tcsendbreak",
    "طرفية_أفرغ": "tty.tcflush",
    "طرفية_خطأ": "tty.error",
    # === pydoc ===
    "طرفية_صفّاح": "pydoc.tty_pager",
    # === pty ===
    "طرفية_وهمية_أغلق": "pty.close",
    # === getopt ===
    "طويل_له_معطيات": "getopt.long_has_args",
    # === pydoc ===
    "عادي": "pydoc.plain",
    "عادي_صفّاح": "pydoc.plain_pager",
    # === multiprocessing ===
    "عالج_خطأ": "multiprocessing.ProcessError",
    "عالج_محلي_عيّن": "multiprocessing.managers.ProcessLocalSet",
    # === typing ===
    "عام": "typing.Generic",
    # === pkgutil ===
    "عام_بسيط": "pkgutil.simplegeneric",
    # === multiprocessing ===
    "عام_دوال": "multiprocessing.managers.public_methods",
    # === enum ===
    "عدد_صحيح_تعداد": "enum.IntEnum",
    "عدد_صحيح_علامة": "enum.IntFlag",
    # === logging ===
    "عدم_معالج": "logging.NullHandler",
    # === ctypes ===
    "عرض_ذاكرة_عند": "ctypes.memoryview_at",
    # === enum ===
    "عضو": "enum.member",
    "علامة_حدّ": "enum.FlagBoundary",
    # === multiprocessing ===
    "عملية_2": "multiprocessing.Process",
    # === ctypes ===
    "عنوان_الكائن": "ctypes.addressof",
    # === multiprocessing ===
    "عنوان_نوع": "multiprocessing.connection.address_type",
    # === signal ===
    "عيّن_أيقِظ_واصف_ملف": "signal.set_wakeup_fd",
    # === readline ===
    "عيّن_إكمال_اعرض_تطابقات_خطاف": "readline.set_completion_display_matches_hook",
    # === multiprocessing ===
    "عيّن_ابدأ_دالة": "multiprocessing.set_start_method",
    # === tty ===
    "عيّن_التفعيل_الحرفي": "tty.setcbreak",
    # === pty ===
    "عيّن_الخام": "pty.setraw",
    # === site ===
    "عيّن_الخروج": "site.setquit",
    # === signal ===
    "عيّن_المؤقّت": "signal.setitimer",
    "عيّن_المنبّه": "signal.alarm",
    # === site ===
    "عيّن_المُساعد": "site.sethelper",
    # === readline ===
    "عيّن_بدء_خطاف": "readline.set_startup_hook",
    "عيّن_تلقائي_سجل": "readline.set_auto_history",
    # === tty ===
    "عيّن_حجم_النافذة": "tty.tcsetwinsize",
    # === resource ===
    "عيّن_حد_المورد": "resource.setrlimit",
    # === site ===
    "عيّن_حقوق_النشر": "site.setcopyright",
    # === multiprocessing ===
    "عيّن_خادم_التفرع_حمّل_مسبقاً": "multiprocessing.set_forkserver_preload",
    # === ctypes ===
    "عيّن_رقم_الخطأ": "ctypes.set_errno",
    # === readline ===
    "عيّن_سجل_طول": "readline.set_history_length",
    # === pty ===
    "عيّن_سمات_الطرفية": "pty.tcsetattr",
    # === multiprocessing ===
    "عيّن_قابل_للتنفيذ": "multiprocessing.set_executable",
    # === readline ===
    "عيّن_قبل_إدخال_خطاف": "readline.set_pre_input_hook",
    # === ctypes ===
    "عيّن_مؤشر_نوع": "ctypes.SetPointerType",
    # === signal ===
    "عيّن_معالج_الإشارة": "signal.signal",
    # === readline ===
    "عيّن_مُكمل": "readline.set_completer",
    "عيّن_مُكمل_محددات": "readline.set_completer_delims",
    # === multiprocessing ===
    "عيّن_وكيل": "multiprocessing.managers.SetProxy",
    # === io ===
    "غلاف_نصي_2": "io.TextIOWrapper",
    # === unittest ===
    "غير_صالح_مواصفة_خطأ": "unittest.mock.InvalidSpecError",
    # === enum ===
    "غير_عضو": "enum.nonmember",
    # === unittest ===
    "غير_قابل_للاستدعاء_سحري_وهمي": "unittest.mock.NonCallableMagicMock",
    "غير_قابل_للاستدعاء_وهمي": "unittest.mock.NonCallableMock",
    "غير_متزامن_سحري_مزيج": "unittest.mock.AsyncMagicMixin",
    "غير_متزامن_وهمي": "unittest.mock.AsyncMock",
    "غير_متزامن_وهمي_مزيج": "unittest.mock.AsyncMockMixin",
    # === unicodedata ===
    "فئة_يونيكود_2": "unicodedata.category",
    # === site ===
    "فعّل_الإكمال": "site.enablerlcompleter",
    # === multiprocessing ===
    "قائمة_وكيل": "multiprocessing.managers.ListProxy",
    # === unittest ===
    "قابل_للاستدعاء_مزيج": "unittest.mock.CallableMixin",
    # === multiprocessing ===
    "قابل_للانضمام_طابور": "multiprocessing.JoinableQueue",
    # === io ===
    "قارئ_مخزّن_2": "io.BufferedReader",
    # === filecmp ===
    "قارن_ملفين": "filecmp.cmp",
    # === logging ===
    "قاموس_إعداد": "logging.config.dictConfig",
    "قاموس_مُضبط": "logging.config.DictConfigurator",
    # === multiprocessing ===
    "قاموس_وكيل": "multiprocessing.managers.DictProxy",
    # === getopt ===
    "قصير_له_معطى": "getopt.short_has_arg",
    # === signal ===
    "قطع_الإشارة": "signal.siginterrupt",
    # === multiprocessing ===
    "قفل_عمليات": "multiprocessing.Lock",
    # === fcntl ===
    "قفل_ملف": "fcntl.flock",
    "قفل_نطاق": "fcntl.lockf",
    # === multiprocessing ===
    "قيمة_مشتركة_2": "multiprocessing.Value",
    "قيمة_وكيل": "multiprocessing.managers.ValueProxy",
    # === typing ===
    "قيّم_إلى_الأمام_مرجع": "typing.evaluate_forward_ref",
    # === io ===
    "كاتب_مخزّن_2": "io.BufferedWriter",
    # === ctypes ===
    "كبير_ترتيب_البايتات_اتحاد": "ctypes.BigEndianUnion",
    "كبير_ترتيب_البايتات_بنية": "ctypes.BigEndianStructure",
    # === typing ===
    "كتابة_أخير_2": "typing.final",
    "كتابة_بروتوكول": "typing.Protocol",
    "كتابة_تأكد_نوع": "typing.assert_type",
    "كتابة_معامل_مواصفة_وسائط_مفتاحية": "typing.ParamSpecKwargs",
    "كتابة_نص_إدخال_إخراج": "typing.TextIO",
    # === pydoc ===
    "كرام": "pydoc.cram",
    # === pkgutil ===
    "كرّر_استيراد_المضغوط_وحدات": "pkgutil.iter_zipimport_modules",
    "كرّر_مُستورد_وحدات": "pkgutil.iter_importer_modules",
    "كرّر_مُستوردون": "pkgutil.iter_importers",
    "كرّر_وحدات": "pkgutil.iter_modules",
    # === dataclasses ===
    "كصف": "dataclasses.astuple",
    "كقاموس": "dataclasses.asdict",
    # === pydoc ===
    "كل_الدوال": "pydoc.allmethods",
    # === multiprocessing ===
    "كل_دوال": "multiprocessing.managers.all_methods",
    # === ctypes ===
    "مؤشر_صغير_مستطيل": "ctypes.wintypes.PSMALL_RECT",
    "مؤشر_عائم": "ctypes.wintypes.PFLOAT",
    "مؤشر_قصير": "ctypes.wintypes.PSHORT",
    "مؤشر_محرف": "ctypes.wintypes.PCHAR",
    "مؤشر_محرف_عريض": "ctypes.wintypes.PWCHAR",
    # === signal ===
    "مؤقّت_خطأ": "signal.ItimerError",
    # === logging ===
    "مؤقّت_دوّار_ملف_معالج": "logging.handlers.TimedRotatingFileHandler",
    # === platform ===
    "ماك_إصدار": "platform.mac_ver",
    # === multiprocessing ===
    "متعدد_معالجة_اتصال": "multiprocessing.connection.Connection",
    "متعدد_معالجة_اتصال_أنبوب": "multiprocessing.connection.Pipe",
    "متعدد_معالجة_اتصال_عميل": "multiprocessing.connection.Client",
    "متعدد_معالجة_حدث": "multiprocessing.Event",
    "متعدد_معالجة_شرط": "multiprocessing.Condition",
    "متعدد_معالجة_مجموعة": "multiprocessing.pool.Pool",
    "متعدد_معالجة_مجموعة_انتظر": "multiprocessing.pool.wait",
    "متعدد_معالجة_مجموعة_عامل": "multiprocessing.pool.worker",
    "متعدد_معالجة_مدير_حالة": "multiprocessing.managers.State",
    "متعدد_معالجة_مدير_خادم": "multiprocessing.managers.Server",
    "متعدد_معالجة_مدير_رمز": "multiprocessing.managers.Token",
    "متعدد_معالجة_مدير_قيمة": "multiprocessing.managers.Value",
    "متعدد_معالجة_مدير_مصفوفة": "multiprocessing.managers.Array",
    "متعدد_معالجة_مدير_نطاق_اسم": "multiprocessing.managers.Namespace",
    "متعدد_معالجة_مزامنة_R_اقفل": "multiprocessing.synchronize.RLock",
    "متعدد_معالجة_مزامنة_إشارة_مرور_2": "multiprocessing.synchronize.Semaphore",
    "متعدد_معالجة_مزامنة_اقفل": "multiprocessing.synchronize.Lock",
    "متعدد_معالجة_مزامنة_حاجز": "multiprocessing.synchronize.Barrier",
    "متعدد_معالجة_مزامنة_حدث": "multiprocessing.synchronize.Event",
    "متعدد_معالجة_مزامنة_شرط": "multiprocessing.synchronize.Condition",
    "متعدد_معالجة_مزامنة_محدود_إشارة_مرور": "multiprocessing.synchronize.BoundedSemaphore",
    "متعدد_معالجة_مشترك_ذاكرة": "multiprocessing.shared_memory.SharedMemory",
    "متعدد_معالجة_مشترك_ذاكرة_قابل_للمشاركة_قائمة": "multiprocessing.shared_memory.ShareableList",
    # === contextvars ===
    "متغير_سياق": "contextvars.ContextVar",
    # === ctypes ===
    "متغير_منطقي": "ctypes.wintypes.VARIANT_BOOL",
    # === contextvars ===
    "متغيرات_سياق": "contextvars.Context",
    # === unittest ===
    "متوقع_فشل": "unittest.expectedFailure",
    # === reprlib ===
    "مثّل_2": "reprlib.repr",
    # === sched ===
    "مجدول_حدث": "sched.Event",
    "مجدول_وقت": "sched.scheduler",
    # === pydoc ===
    "مجلدات_المسار": "pydoc.pathdirs",
    # === multiprocessing ===
    "مجموعة_عمليات": "multiprocessing.Pool",
    "مجموعة_وكيل": "multiprocessing.managers.PoolProxy",
    # === dataclasses ===
    "مجمّد_نسخة_خطأ": "dataclasses.FrozenInstanceError",
    # === ctypes ===
    "محاذاة": "ctypes.alignment",
    # === multiprocessing ===
    "محدود_إشارة_مرور": "multiprocessing.BoundedSemaphore",
    # === unittest ===
    "محمّل_اختبارات": "unittest.TestLoader",
    # === multiprocessing ===
    "مخزن_مؤقت_أكثر_من_قصير": "multiprocessing.BufferTooShort",
    # === contextlib ===
    "مدير_سياق_2": "contextlib.contextmanager",
    # === multiprocessing ===
    "مدير_عمليات_2": "multiprocessing.Manager",
    # === graphlib ===
    "مرتّب_توبولوجي_2": "graphlib.TopologicalSorter",
    # === ctypes ===
    "مستطيل": "ctypes.wintypes.RECT",
    # === concurrent ===
    "مستقبل": "concurrent.futures.Future",
    # === logging ===
    "مسجّل_2": "logging.Logger",
    "مسجّل_مكيّف": "logging.LoggerAdapter",
    # === typing ===
    "مسمّى_صف": "typing.NamedTuple",
    "مسمّى_صف_وصفي": "typing.NamedTupleMeta",
    # === multiprocessing ===
    "مشترك_ذاكرة_خادم": "multiprocessing.managers.SharedMemoryServer",
    "مشترك_ذاكرة_مدير": "multiprocessing.managers.SharedMemoryManager",
    "مصادقة_خطأ": "multiprocessing.AuthenticationError",
    # === pydoc ===
    "مصدر_خلاصة": "pydoc.source_synopsis",
    # === multiprocessing ===
    "مصفوفة_مشتركة": "multiprocessing.Array",
    "مصفوفة_وكيل": "multiprocessing.managers.ArrayProxy",
    # === difflib ===
    "مطابق_التسلسل_2": "difflib.SequenceMatcher",
    # === site ===
    "مطلق_مسارات": "site.abs_paths",
    # === logging ===
    "معالج_التدفق": "logging.StreamHandler",
    "معالج_الملف": "logging.FileHandler",
    # === multiprocessing ===
    "معالج_عدّ": "multiprocessing.cpu_count",
    # === typing ===
    "معامل_مواصفة": "typing.ParamSpec",
    "معامل_مواصفة_معطيات": "typing.ParamSpecArgs",
    # === unittest ===
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة": "unittest.IsolatedAsyncioTestCase",
    # === platform ===
    "معمارية": "platform.architecture",
    "معمارية_الجهاز": "platform.machine",
    # === difflib ===
    "مفرّق_2": "difflib.Differ",
    # === concurrent ===
    "مفسّر_مجموعة_منفّذ": "concurrent.futures.InterpreterPoolExecutor",
    # === multiprocessing ===
    "مقبس_عميل": "multiprocessing.connection.SocketClient",
    # === logging ===
    "مقبس_معالج": "logging.handlers.SocketHandler",
    # === multiprocessing ===
    "مقبس_مُستمع": "multiprocessing.connection.SocketListener",
    # === ctypes ===
    "مكتبات_خارجية_أنواع_ويندوز_رسالة": "ctypes.wintypes.MSG",
    "مكتبات_خارجية_حوّل_نوع": "ctypes.cast",
    "مكتبات_خارجية_غيّر_الحجم": "ctypes.resize",
    "مكتبات_خارجية_مؤشر": "ctypes.POINTER",
    "مكتبات_خارجية_مؤشر_2": "ctypes.pointer",
    "مكتبات_خارجية_مصفوفة": "ctypes.ARRAY",
    "مكتبات_خارجية_مصفوفة_2": "ctypes.Array",
    # === platform ===
    "مكتبة_c_إصدار": "platform.libc_ver",
    # === reprlib ===
    "مكتبة_التمثيل_احصل_معرّف": "reprlib.get_ident",
    # === difflib ===
    "مكتبة_الفروق_استعد": "difflib.restore",
    "مكتبة_الفروق_طابق": "difflib.Match",
    "مكتبة_الفروق_فرق_بايتات": "difflib.diff_bytes",
    "مكتبة_الفروق_فرق_متجاور": "difflib.ndiff",
    "مكتبة_الفروق_هو_حرف_همل": "difflib.IS_CHARACTER_JUNK",
    "مكتبة_الفروق_هو_سطر_همل": "difflib.IS_LINE_JUNK",
    # === ctypes ===
    "مكتبة_ديناميكية": "ctypes.CDLL",
    "مكتبة_محمّل": "ctypes.LibraryLoader",
    # === typing ===
    "مكتوب_قاموس": "typing.TypedDict",
    # === multiprocessing ===
    "مكرّر_وكيل": "multiprocessing.managers.IteratorProxy",
    # === concurrent ===
    "مكسور_منفّذ": "concurrent.futures.BrokenExecutor",
    # === fileinput ===
    "ملف_إدخال_2": "fileinput.FileInput",
    "ملف_إدخال_أغلق_4": "fileinput.close",
    # === io ===
    "ملف_إدخال_إخراج_2": "io.FileIO",
    # === fileinput ===
    "ملف_إدخال_الملف_التالي_3": "fileinput.nextfile",
    "ملف_إدخال_خطاف_مرمّز": "fileinput.hook_encoded",
    "ملف_إدخال_خطاف_مضغوط": "fileinput.hook_compressed",
    "ملف_إدخال_رقم_السطر_4": "fileinput.lineno",
    "ملف_إدخال_رقم_الملف_4": "fileinput.fileno",
    "ملف_إدخال_سطر_الملف_3": "fileinput.filelineno",
    "ملف_إدخال_هو_السطر_الأول_3": "fileinput.isfirstline",
    # === logging ===
    "ملف_إعداد": "logging.config.fileConfig",
    # === filecmp ===
    "ملف_قارن_الملفات": "filecmp.cmpfiles",
    "ملف_قارن_امسح_ذاكرة_مؤقتة_2": "filecmp.clear_cache",
    "ملف_قارن_توضيحي": "filecmp.demo",
    "ملف_قارن_عام_اسم_مستعار": "filecmp.GenericAlias",
    "ملف_قارن_مقارنة_مجلدات": "filecmp.dircmp",
    # === pydoc ===
    "ملف_مؤقت_صفّاح": "pydoc.tempfile_pager",
    # === fileinput ===
    "ملف_هو_إدخال_قياسي_2": "fileinput.isstdin",
    # === ctypes ===
    "ملف_وقت": "ctypes.wintypes.FILETIME",
    # === platform ===
    "منصة_أندرويد_إصدار": "platform.android_ver",
    "منصة_إصدار": "platform.version",
    # === sysconfig ===
    "منصة_البناء": "sysconfig.get_platform",
    # === platform ===
    "منصة_بايثون_تنفيذ": "platform.python_implementation",
    "منصة_حرّر": "platform.release",
    "منصة_عُقدة": "platform.node",
    "منصة_معالج": "platform.processor",
    # === concurrent ===
    "منفّذ": "concurrent.futures.Executor",
    "منفّذ_خيوط": "concurrent.futures.ThreadPoolExecutor",
    "منفّذ_عمليات": "concurrent.futures.ProcessPoolExecutor",
    # === multiprocessing ===
    "مهلة_خطأ": "multiprocessing.TimeoutError",
    # === difflib ===
    "موحّد_فرق": "difflib.unified_diff",
    # === site ===
    "موقع_رئيسي": "site.main",
    # === io ===
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_2": "io.BufferedIOBase",
    # === logging ===
    "مُراقَب_ملف_معالج": "logging.handlers.WatchedFileHandler",
    # === pydoc ===
    "مُساعد": "pydoc.Helper",
    # === multiprocessing ===
    "مُستمع": "multiprocessing.connection.Listener",
    # === unittest ===
    "مُشغّل_اختبارات": "unittest.TextTestRunner",
    # === rlcompleter ===
    "مُكمل": "rlcompleter.Completer",
    # === concurrent ===
    "مُلغى_خطأ": "concurrent.futures.CancelledError",
    # === selectors ===
    "مُنتخِب_ABC_وصفي": "selectors.ABCMeta",
    "مُنتخِب_دالة_مجردة": "selectors.abstractmethod",
    "مُنتخِب_مفتاح": "selectors.SelectorKey",
    # === logging ===
    "مُنسّق_2": "logging.Formatter",
    "نسبة_مئوية_نمط": "logging.PercentStyle",
    # === multiprocessing ===
    "نسّق_استثناء": "multiprocessing.managers.format_exc",
    # === pydoc ===
    "نسّق_استثناء_فقط": "pydoc.format_exception_only",
    # === shlex ===
    "نص_إدخال_إخراج": "shlex.StringIO",
    # === io ===
    "نص_إدخال_إخراج_أساس_2": "io.TextIOBase",
    # === unittest ===
    "نص_اختبر_نتيجة": "unittest.TextTestResult",
    # === signal ===
    "نص_الإشارة": "signal.strsignal",
    # === unittest ===
    "نص_الصنف": "unittest.case.strclass",
    # === enum ===
    "نص_تعداد": "enum.StrEnum",
    # === pydoc ===
    "نص_تمثيل": "pydoc.TextRepr",
    "نص_توثيق": "pydoc.TextDoc",
    # === ctypes ===
    "نص_عريض_عند": "ctypes.wstring_at",
    "نص_عند": "ctypes.string_at",
    # === logging ===
    "نص_قالب_نمط": "logging.StringTemplateStyle",
    "نص_نسّق_نمط": "logging.StrFormatStyle",
    # === types ===
    "نطاق_اسم_بسيط": "types.SimpleNamespace",
    # === multiprocessing ===
    "نطاق_اسم_وكيل": "multiprocessing.managers.NamespaceProxy",
    # === platform ===
    "نظام_اسم_مستعار": "platform.system_alias",
    "نظام_التشغيل": "platform.system",
    # === logging ===
    "نظام_سجل_معالج": "logging.handlers.SysLogHandler",
    # === site ===
    "نفّذ_تخصيص_المستخدم": "site.execusercustomize",
    "نفّذ_تخصيص_الموقع": "site.execsitecustomize",
    # === ctypes ===
    "نقطة": "ctypes.wintypes.POINT",
    # === typing ===
    "نوع_اسم_مستعار_نوع": "typing.TypeAliasType",
    # === ctypes ===
    "نوع_دالة_c": "ctypes.CFUNCTYPE",
    "نوع_دالة_بايثون": "ctypes.PYFUNCTYPE",
    # === typing ===
    "نوع_متغير": "typing.TypeVar",
    "نوع_متغير_صف": "typing.TypeVarTuple",
    # === sysconfig ===
    "هو_بايثون_ابنِ": "sysconfig.is_python_build",
    # === typing ===
    "هو_بروتوكول": "typing.is_protocol",
    # === pydoc ===
    "هو_بيانات": "pydoc.isdata",
    # === dataclasses ===
    "هو_صنف_بيانات": "dataclasses.is_dataclass",
    # === typing ===
    "هو_قاموس_مُنوَّع": "typing.is_typeddict",
    # === pydoc ===
    "هو_مسار": "pydoc.ispath",
    "واجهة_سطر": "pydoc.cli",
    "وحدة_ماسح": "pydoc.ModuleScanner",
    # === pkgutil ===
    "وحدة_معلومات": "pkgutil.ModuleInfo",
    # === unicodedata ===
    "وحّد_يونيكود_2": "unicodedata.normalize",
    # === sysconfig ===
    "وسّع_اعمل_ملفاً_متغيرات": "sysconfig.expand_makefile_vars",
    # === pkgutil ===
    "وسّع_مسار": "pkgutil.extend_path",
    # === stat ===
    "وضع_الملف_2": "stat.filemode",
    # === pty ===
    "ولّد": "pty.spawn",
    # === unittest ===
    "وهمي": "unittest.mock.Mock",
    "وهمي_افتح": "unittest.mock.mock_open",
    # === platform ===
    "ويندوز32_إصدار": "platform.win32_ver",
    "ويندوز32_طبعة": "platform.win32_edition",
    "ويندوز32_هو_IOT": "platform.win32_is_iot",
    # === ctypes ===
    "ويندوز_32_ابحث_بيانات_a": "ctypes.wintypes.WIN32_FIND_DATAA",
    "ويندوز_32_ابحث_بيانات_w": "ctypes.wintypes.WIN32_FIND_DATAW",
    # === typing ===
    "يدعم_بايتات": "typing.SupportsBytes",
    "يدعم_عائم": "typing.SupportsFloat",
    "يدعم_عدد_صحيح": "typing.SupportsInt",
    "يدعم_فهرس": "typing.SupportsIndex",
    "يدعم_قرّب": "typing.SupportsRound",
    "يدعم_مركّب": "typing.SupportsComplex",
    "يدعم_مطلق": "typing.SupportsAbs",
    # === contextlib ===
    "يُغلق_2": "contextlib.closing",
}


SYS_METHODS = {
    # دوال الكائن بعد نقطة
    # === ctypes ===
    "C_حرف_P_من_معامل": "from_param",
    "C_فارغ_P_من_معامل": "from_param",
    "C_محرف_عريض_P_من_معامل": "from_param",
    # === pydoc ===
    "HTML_تمثيل_تمثيل": "repr",
    "HTML_تمثيل_تمثيل1": "repr1",
    "HTML_تمثيل_تمثيل_صف": "repr_tuple",
    "HTML_تمثيل_تمثيل_طابور_مزدوج": "repr_deque",
    "HTML_تمثيل_تمثيل_عدد_صحيح": "repr_int",
    "HTML_تمثيل_تمثيل_عيّن": "repr_set",
    "HTML_تمثيل_تمثيل_قائمة": "repr_list",
    "HTML_تمثيل_تمثيل_قاموس": "repr_dict",
    "HTML_تمثيل_تمثيل_مجموعة_مجمّدة": "repr_frozenset",
    "HTML_تمثيل_تمثيل_مصفوفة": "repr_array",
    "HTML_تمثيل_تمثيل_نسخة": "repr_instance",
    "HTML_تمثيل_تمثيل_نص": "repr_str",
    "HTML_تمثيل_هرب": "escape",
    "HTML_توثيق_احصل_على_مكان_التوثيق": "getdocloc",
    "HTML_توثيق_افشل": "fail",
    "HTML_توثيق_تمثيل": "repr",
    "HTML_توثيق_توثيق_الدالة": "docroutine",
    "HTML_توثيق_صفحة": "page",
    "HTML_توثيق_عنوان": "heading",
    "HTML_توثيق_فهرس": "index",
    "HTML_توثيق_قسم": "section",
    "HTML_توثيق_مستند": "document",
    "HTML_توثيق_نسّق_الشجرة": "formattree",
    "HTML_توثيق_نسّق_القيمة": "formatvalue",
    "HTML_توثيق_هرب": "escape",
    "HTML_توثيق_وثّق_البيانات": "docdata",
    "HTML_توثيق_وثّق_الخاصية": "docproperty",
    "HTML_توثيق_وثّق_الصنف": "docclass",
    "HTML_توثيق_وثّق_الوحدة": "docmodule",
    "HTML_توثيق_وثّق_غيره": "docother",
    "HTML_توثيق_وسم": "markup",
    # === difflib ===
    "HTML_فرق_اعمل_جدول": "make_table",
    "HTML_فرق_اعمل_ملف": "make_file",
    # === logging ===
    "HTTP_معالج_أصدر": "emit",
    "HTTP_معالج_أضف_رشّح": "addFilter",
    "HTTP_معالج_أفرغ": "flush",
    "HTTP_معالج_أنشئ_اقفل": "createLock",
    "HTTP_معالج_احذف_رشّح": "removeFilter",
    "HTTP_معالج_احصل": "acquire",
    "HTTP_معالج_احصل_اسم": "get_name",
    "HTTP_معالج_حرّر": "release",
    "HTTP_معالج_رشّح": "filter",
    "HTTP_معالج_عالج": "handle",
    "HTTP_معالج_عالج_خطأ": "handleError",
    "HTTP_معالج_عيّن_اسم": "set_name",
    "HTTP_معالج_عيّن_مستوى": "setLevel",
    "HTTP_معالج_عيّن_مُنسّق": "setFormatter",
    "HTTP_معالج_نسّق": "format",
    # === multiprocessing ===
    "I_خريطة_غير_مرتّب_مكرّر_التالي": "next",
    "I_خريطة_مكرّر_التالي": "next",
    # === logging ===
    "NT_حدث_سجل_معالج_أصدر": "emit",
    "NT_حدث_سجل_معالج_أضف_رشّح": "addFilter",
    "NT_حدث_سجل_معالج_أغلق": "close",
    "NT_حدث_سجل_معالج_أفرغ": "flush",
    "NT_حدث_سجل_معالج_أنشئ_اقفل": "createLock",
    "NT_حدث_سجل_معالج_احذف_رشّح": "removeFilter",
    "NT_حدث_سجل_معالج_احصل": "acquire",
    "NT_حدث_سجل_معالج_احصل_اسم": "get_name",
    "NT_حدث_سجل_معالج_حرّر": "release",
    "NT_حدث_سجل_معالج_رشّح": "filter",
    "NT_حدث_سجل_معالج_عالج": "handle",
    "NT_حدث_سجل_معالج_عالج_خطأ": "handleError",
    "NT_حدث_سجل_معالج_عيّن_اسم": "set_name",
    "NT_حدث_سجل_معالج_عيّن_مستوى": "setLevel",
    "NT_حدث_سجل_معالج_عيّن_مُنسّق": "setFormatter",
    "NT_حدث_سجل_معالج_نسّق": "format",
    # === multiprocessing ===
    "R_اقفل_مقفل": "locked",
    # === logging ===
    "SMTP_معالج_أصدر": "emit",
    "SMTP_معالج_أضف_رشّح": "addFilter",
    "SMTP_معالج_أغلق": "close",
    "SMTP_معالج_أفرغ": "flush",
    "SMTP_معالج_أنشئ_اقفل": "createLock",
    "SMTP_معالج_احذف_رشّح": "removeFilter",
    "SMTP_معالج_احصل": "acquire",
    "SMTP_معالج_احصل_اسم": "get_name",
    "SMTP_معالج_حرّر": "release",
    "SMTP_معالج_رشّح": "filter",
    "SMTP_معالج_عالج": "handle",
    "SMTP_معالج_عالج_خطأ": "handleError",
    "SMTP_معالج_عيّن_اسم": "set_name",
    "SMTP_معالج_عيّن_مستوى": "setLevel",
    "SMTP_معالج_عيّن_مُنسّق": "setFormatter",
    "SMTP_معالج_نسّق": "format",
    # === multiprocessing ===
    "XML_مُستمع_أغلق": "close",
    "XML_مُستمع_اقبل": "accept",
    "أجهض": "abort",
    # === logging ===
    "أدخل_الطابور": "enqueue",
    "أدخل_الطابور_حارس": "enqueue_sentinel",
    # === sched ===
    "أدرج_موعداً": "enter",
    # === contextlib ===
    "أدوات_السياق_اخرج_مكدس_أغلق": "close",
    "أدوات_السياق_اخرج_مكدس_ادفع": "push",
    "أدوات_السياق_اخرج_مكدس_اسحب_كل": "pop_all",
    "أدوات_السياق_غير_متزامن_اخرج_مكدس_ادفع": "push",
    "أدوات_السياق_غير_متزامن_اخرج_مكدس_اسحب_كل": "pop_all",
    # === multiprocessing ===
    "أرسل_بايتات": "send_bytes",
    # === venv ===
    "أرسل_جهّز": "post_setup",
    # === unittest ===
    "أساس_اختبر_حزمة_أضف_اختبارات": "addTests",
    "أساس_اختبر_حزمة_أضف_اختبر": "addTest",
    "أساس_اختبر_حزمة_تصحيح": "debug",
    "أساس_اختبر_حزمة_شغّل": "run",
    "أساس_اختبر_حزمة_عدّ_اختبر_حالات": "countTestCases",
    # === logging ===
    "أساس_دوّار_معالج_أصدر": "emit",
    "أساس_دوّار_معالج_أضف_رشّح": "addFilter",
    "أساس_دوّار_معالج_أغلق": "close",
    "أساس_دوّار_معالج_أفرغ": "flush",
    "أساس_دوّار_معالج_أنشئ_اقفل": "createLock",
    "أساس_دوّار_معالج_احذف_رشّح": "removeFilter",
    "أساس_دوّار_معالج_احصل": "acquire",
    "أساس_دوّار_معالج_احصل_اسم": "get_name",
    "أساس_دوّار_معالج_تدوير_اسم_ملف": "rotation_filename",
    "أساس_دوّار_معالج_حرّر": "release",
    "أساس_دوّار_معالج_دوّر": "rotate",
    "أساس_دوّار_معالج_رشّح": "filter",
    "أساس_دوّار_معالج_عالج": "handle",
    "أساس_دوّار_معالج_عالج_خطأ": "handleError",
    "أساس_دوّار_معالج_عيّن_اسم": "set_name",
    "أساس_دوّار_معالج_عيّن_تدفق": "setStream",
    "أساس_دوّار_معالج_عيّن_مستوى": "setLevel",
    "أساس_دوّار_معالج_عيّن_مُنسّق": "setFormatter",
    "أساس_دوّار_معالج_نسّق": "format",
    # === multiprocessing ===
    "أساس_قائمة_وكيل_أدخل": "insert",
    "أساس_قائمة_وكيل_أضف_ذيلياً": "append",
    "أساس_قائمة_وكيل_احذف": "remove",
    "أساس_قائمة_وكيل_اسحب": "pop",
    "أساس_قائمة_وكيل_اعكس": "reverse",
    "أساس_قائمة_وكيل_امسح": "clear",
    "أساس_قائمة_وكيل_انسخ": "copy",
    "أساس_قائمة_وكيل_رتّب": "sort",
    "أساس_قائمة_وكيل_عدّ": "count",
    "أساس_قائمة_وكيل_فهرس": "index",
    "أساس_قائمة_وكيل_وسّع": "extend",
    "أساس_مجموعة_وكيل_MAP_نجمة": "starmap",
    "أساس_مجموعة_وكيل_MAP_نجمة_غير_متزامن": "starmap_async",
    "أساس_مجموعة_وكيل_imap": "imap",
    "أساس_مجموعة_وكيل_imap_غير_مرتّب": "imap_unordered",
    "أساس_مجموعة_وكيل_أغلق": "close",
    "أساس_مجموعة_وكيل_أنهِ": "terminate",
    "أساس_مجموعة_وكيل_اربط": "join",
    "أساس_مجموعة_وكيل_خريطة": "map",
    "أساس_مجموعة_وكيل_خريطة_غير_متزامن": "map_async",
    "أساس_مجموعة_وكيل_طبّق": "apply",
    "أساس_مجموعة_وكيل_طبّق_غير_متزامن": "apply_async",
    "أساس_مدير_ابدأ": "start",
    "أساس_مدير_اتصل": "connect",
    "أساس_مدير_احصل_خادم": "get_server",
    "أساس_مدير_اربط": "join",
    "أساس_مدير_سجّل": "register",
    # === logging ===
    "أساس_مُضبط_إعداد_حوّل": "cfg_convert",
    "أساس_مُضبط_اضبط_مُخصّص": "configure_custom",
    "أساس_مُضبط_امتداد_حوّل": "ext_convert",
    "أساس_مُضبط_حلّ": "resolve",
    "أساس_مُضبط_حوّل": "convert",
    "أساس_مُضبط_كـ_صف": "as_tuple",
    "أساس_مُضبط_مُستورد": "importer",
    # === selectors ===
    "أساس_مُنتخِب_أغلق": "close",
    "أساس_مُنتخِب_ألغِ_التسجيل": "unregister",
    "أساس_مُنتخِب_احصل_خريطة": "get_map",
    "أساس_مُنتخِب_احصل_مفتاح": "get_key",
    "أساس_مُنتخِب_اختر": "select",
    "أساس_مُنتخِب_سجّل": "register",
    "أساس_مُنتخِب_عدّل": "modify",
    # === concurrent ===
    "أضف_تم_رد_النداء": "add_done_callback",
    # === unittest ===
    "أضف_غير_متزامن_نظّف": "addAsyncCleanup",
    # === logging ===
    "أضف_مرشّحات": "add_filters",
    "أضف_معالجات": "add_handlers",
    "أعد_الفتح_إذا_مطلوب": "reopenIfNeeded",
    # === numbers ===
    "أعداد_حقيقي_مرافق": "conjugate",
    "أعداد_صحيح_مرافق": "conjugate",
    "أعداد_مركّب_مرافق": "conjugate",
    "أعداد_نسبي_مرافق": "conjugate",
    # === cmd ===
    "أكمل_الافتراضي": "completedefault",
    "أكمل_مساعدة": "complete_help",
    "أمر_أكمل": "complete",
    "أمر_أكمل_الأسماء": "completenames",
    "أمر_أمر_واحد": "onecmd",
    "أمر_احصل_أسماء": "get_names",
    "أمر_افتراضي": "default",
    # === unittest ===
    "أنشئ_اختبارات": "createTests",
    # === venv ===
    "أنشئ_جيت_تجاهل_ملف": "create_git_ignore_file",
    "أنشئ_ضبط": "create_configuration",
    # === unittest ===
    "أنشئ_وهمي": "create_mock",
    # === concurrent ===
    "أنهِ_عامل": "terminate_workers",
    # === select ===
    "إبول_أغلق": "close",
    "إبول_ألغِ_التسجيل": "unregister",
    "إبول_استطلع": "poll",
    "إبول_رقم_الملف": "fileno",
    "إبول_سجّل": "register",
    "إبول_عدّل": "modify",
    # === io ===
    "إدخال_إخراج_أساس_أغلق_2": "close",
    "إدخال_إخراج_أساس_أفرغ_2": "flush",
    "إدخال_إخراج_أساس_اقتطع_2": "truncate",
    "إدخال_إخراج_أساس_اقرأ_الأسطر": "readlines",
    "إدخال_إخراج_أساس_اكتب_أسطراً_2": "writelines",
    "إدخال_إخراج_أساس_انتقل_2": "seek",
    "إدخال_إخراج_أساس_رقم_الملف_2": "fileno",
    "إدخال_إخراج_أساس_سطر_قراءة_3": "readline",
    "إدخال_إخراج_أساس_ضع_الموضع_2": "tell",
    "إدخال_إخراج_أساس_قابل_للانتقال_2": "seekable",
    "إدخال_إخراج_أساس_قابل_للقراءة_2": "readable",
    "إدخال_إخراج_أساس_قابل_للكتابة_2": "writable",
    "إدخال_إخراج_أساس_هو_طرفية_2": "isatty",
    # === typing ===
    "إدخال_إخراج_أغلق": "close",
    "إدخال_إخراج_أفرغ": "flush",
    "إدخال_إخراج_اقتطع": "truncate",
    "إدخال_إخراج_اقرأ": "read",
    "إدخال_إخراج_اقرأ_الأسطر": "readlines",
    "إدخال_إخراج_اكتب": "write",
    "إدخال_إخراج_اكتب_أسطراً": "writelines",
    "إدخال_إخراج_انتقل": "seek",
    # === io ===
    "إدخال_إخراج_تصاعدي_سطر_جديد_مفكّك_صفّر": "reset",
    "إدخال_إخراج_تصاعدي_سطر_جديد_مفكّك_فكّ_ترميز": "decode",
    # === typing ===
    "إدخال_إخراج_رقم_الملف": "fileno",
    "إدخال_إخراج_سطر_قراءة": "readline",
    "إدخال_إخراج_ضع_الموضع": "tell",
    "إدخال_إخراج_قابل_للانتقال": "seekable",
    "إدخال_إخراج_قابل_للقراءة": "readable",
    "إدخال_إخراج_قابل_للكتابة": "writable",
    # === io ===
    "إدخال_إخراج_قارئ_اقرأ": "read",
    "إدخال_إخراج_كاتب_اكتب": "write",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_أغلق": "close",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_أفرغ": "flush",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_اطّلع": "peek",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_افصل": "detach",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_اقتطع": "truncate",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_اقرأ": "read",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_اقرأ1": "read1",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_اقرأ_في": "readinto",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_اقرأ_في1": "readinto1",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_اكتب": "write",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_اكتب_أسطراً": "writelines",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_انتقل": "seek",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_رقم_الملف": "fileno",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_سطر_قراءة_2": "readline",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_ضع_الموضع": "tell",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_قابل_للانتقال": "seekable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_قابل_للقراءة": "readable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_قابل_للكتابة": "writable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_هو_طرفية": "isatty",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_أغلق": "close",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_أفرغ": "flush",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_اطّلع": "peek",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_افصل": "detach",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_اقتطع": "truncate",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_اقرأ": "read",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_اقرأ1": "read1",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_اقرأ_في": "readinto",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_اقرأ_في1": "readinto1",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_اكتب": "write",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_اكتب_أسطراً": "writelines",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_انتقل": "seek",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_رقم_الملف": "fileno",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_سطر_قراءة_2": "readline",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_ضع_الموضع": "tell",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_قابل_للانتقال": "seekable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_قابل_للقراءة": "readable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_قابل_للكتابة": "writable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_هو_طرفية": "isatty",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_أغلق": "close",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_أفرغ": "flush",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اطّلع": "peek",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_افصل": "detach",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اقتطع": "truncate",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اقرأ": "read",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اقرأ1": "read1",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اقرأ_في": "readinto",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اقرأ_في1": "readinto1",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اكتب": "write",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اكتب_أسطراً": "writelines",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_انتقل": "seek",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_رقم_الملف": "fileno",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_سطر_قراءة_2": "readline",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_ضع_الموضع": "tell",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_قابل_للانتقال": "seekable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_قابل_للقراءة": "readable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_قابل_للكتابة": "writable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_هو_طرفية": "isatty",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_أغلق": "close",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_أفرغ": "flush",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_افصل": "detach",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_اقتطع": "truncate",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_اقرأ": "read",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_اقرأ1": "read1",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_اقرأ_في": "readinto",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_اقرأ_في1": "readinto1",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_اكتب": "write",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_اكتب_أسطراً": "writelines",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_انتقل": "seek",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_رقم_الملف": "fileno",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_سطر_قراءة_2": "readline",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_ضع_الموضع": "tell",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_قابل_للانتقال": "seekable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_قابل_للقراءة": "readable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_قابل_للكتابة": "writable",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_هو_طرفية": "isatty",
    # === typing ===
    "إدخال_إخراج_هو_طرفية": "isatty",
    # === multiprocessing ===
    "إشارة_مرور_احصل_قيمة": "get_value",
    "إشارة_مرور_اقفل_مقفل": "locked",
    "إشارة_مرور_مقفل": "locked",
    # === mmap ===
    "ابحث_يميناً": "rfind",
    # === multiprocessing ===
    "اتصال_أرسل": "send",
    "اتصال_أغلق": "close",
    "اتصال_استطلع": "poll",
    "اتصال_استقبل": "recv",
    "اتصال_رقم_الملف": "fileno",
    "اتصال_غلاف_أرسل": "send",
    "اتصال_غلاف_استقبل": "recv",
    # === logging ===
    "احسب_تجاوز": "computeRollover",
    "احصل_اتصال": "getConnection",
    # === unittest ===
    "احصل_اختبر_حالة_أسماء": "getTestCaseNames",
    # === logging ===
    "احصل_حدث_فئة": "getEventCategory",
    "احصل_حدث_نوع": "getEventType",
    "احصل_رسالة": "getMessage",
    "احصل_رسالة_معرف": "getMessageID",
    # === shlex ===
    "احصل_رمز": "get_token",
    # === io ===
    "احصل_على_الحالة": "getstate",
    # === logging ===
    "احصل_ملفات_إلى_احذف": "getFilesToDelete",
    "احصل_موضوع": "getSubject",
    # === unittest ===
    "احصل_وصف": "getDescription",
    "اختبر_برنامج_حلل_معطيات": "parseArgs",
    "اختبر_حالة_أدرج_موعداً_سياق": "enterContext",
    "اختبر_حالة_أدرج_موعداً_صنف_سياق": "enterClassContext",
    "اختبر_حالة_أضف_صنف_نظّف": "addClassCleanup",
    "اختبر_حالة_أضف_نظّف": "addCleanup",
    "اختبر_حالة_أضف_نوع_مساواة_دالة": "addTypeEqualityFunc",
    "اختبر_حالة_افتراضي_اختبر_نتيجة": "defaultTestResult",
    "اختبر_حالة_افشل": "fail",
    "اختبر_حالة_افعل_تنظيفات": "doCleanups",
    "اختبر_حالة_افعل_صنف_تنظيفات": "doClassCleanups",
    "اختبر_حالة_تأكد_أصغر": "assertLess",
    "اختبر_حالة_تأكد_أصغر_يساوي": "assertLessEqual",
    "اختبر_حالة_تأكد_أكبر": "assertGreater",
    "اختبر_حالة_تأكد_أكبر_يساوي": "assertGreaterEqual",
    "اختبر_حالة_تأكد_بدايات_بـ": "assertStartsWith",
    "اختبر_حالة_تأكد_بلا_سجلات": "assertNoLogs",
    "اختبر_حالة_تأكد_تسلسل_يساوي": "assertSequenceEqual",
    "اختبر_حالة_تأكد_تعبير_نمطي": "assertRegex",
    "اختبر_حالة_تأكد_تقريباً_يساوي": "assertAlmostEqual",
    "اختبر_حالة_تأكد_خطأ": "assertFalse",
    "اختبر_حالة_تأكد_سجلات": "assertLogs",
    "اختبر_حالة_تأكد_صحيح": "assertTrue",
    "اختبر_حالة_تأكد_صف_يساوي": "assertTupleEqual",
    "اختبر_حالة_تأكد_عدّ_يساوي": "assertCountEqual",
    "اختبر_حالة_تأكد_عيّن_يساوي": "assertSetEqual",
    "اختبر_حالة_تأكد_في": "assertIn",
    "اختبر_حالة_تأكد_قائمة_يساوي": "assertListEqual",
    "اختبر_حالة_تأكد_قاموس_يساوي": "assertDictEqual",
    "اختبر_حالة_تأكد_لا_بدايات_بـ": "assertNotStartsWith",
    "اختبر_حالة_تأكد_لا_تعبير_نمطي": "assertNotRegex",
    "اختبر_حالة_تأكد_لا_تقريباً_يساوي": "assertNotAlmostEqual",
    "اختبر_حالة_تأكد_لا_في": "assertNotIn",
    "اختبر_حالة_تأكد_لا_له_سمة": "assertNotHasAttr",
    "اختبر_حالة_تأكد_لا_نهايات_بـ": "assertNotEndsWith",
    "اختبر_حالة_تأكد_لا_هو_صنف_فرعي": "assertNotIsSubclass",
    "اختبر_حالة_تأكد_لا_هو_نسخة": "assertNotIsInstance",
    "اختبر_حالة_تأكد_لا_يساوي": "assertNotEqual",
    "اختبر_حالة_تأكد_له_سمة": "assertHasAttr",
    "اختبر_حالة_تأكد_متعدد_سطر_يساوي": "assertMultiLineEqual",
    "اختبر_حالة_تأكد_نهايات_بـ": "assertEndsWith",
    "اختبر_حالة_تأكد_هو": "assertIs",
    "اختبر_حالة_تأكد_هو_صنف_فرعي": "assertIsSubclass",
    "اختبر_حالة_تأكد_هو_لا": "assertIsNot",
    "اختبر_حالة_تأكد_هو_لا_شيء": "assertIsNone",
    "اختبر_حالة_تأكد_هو_لا_لا_شيء": "assertIsNotNone",
    "اختبر_حالة_تأكد_هو_نسخة": "assertIsInstance",
    "اختبر_حالة_تأكد_يحذّر": "assertWarns",
    "اختبر_حالة_تأكد_يحذّر_تعبير_نمطي": "assertWarnsRegex",
    "اختبر_حالة_تأكد_يرفع": "assertRaises",
    "اختبر_حالة_تأكد_يرفع_تعبير_نمطي": "assertRaisesRegex",
    "اختبر_حالة_تأكد_يساوي": "assertEqual",
    "اختبر_حالة_تجاوز_اختبر": "skipTest",
    "اختبر_حالة_تصحيح": "debug",
    "اختبر_حالة_شغّل": "run",
    "اختبر_حالة_عدّ_اختبر_حالات": "countTestCases",
    "اختبر_حالة_عيّن_لأعلى": "setUp",
    "اختبر_حالة_عيّن_لأعلى_صنف": "setUpClass",
    "اختبر_حالة_فرعي_اختبر": "subTest",
    "اختبر_حالة_قصير_وصف": "shortDescription",
    "اختبر_حالة_مزّق_لأسفل": "tearDown",
    "اختبر_حالة_مزّق_لأسفل_صنف": "tearDownClass",
    "اختبر_حالة_معرف": "id",
    "اختبر_حزمة_أضف_اختبارات": "addTests",
    "اختبر_حزمة_أضف_اختبر": "addTest",
    "اختبر_حزمة_تصحيح": "debug",
    "اختبر_حزمة_شغّل": "run",
    "اختبر_حزمة_عدّ_اختبر_حالات": "countTestCases",
    "اختبر_نتيجة_أضف_تجاوز": "addSkip",
    "اختبر_نتيجة_أضف_خطأ": "addError",
    "اختبر_نتيجة_أضف_غير_متوقع_نجاح": "addUnexpectedSuccess",
    "اختبر_نتيجة_أضف_فرعي_اختبر": "addSubTest",
    "اختبر_نتيجة_أضف_فشل": "addFailure",
    "اختبر_نتيجة_أضف_متوقع_فشل": "addExpectedFailure",
    "اختبر_نتيجة_أضف_مدة": "addDuration",
    "اختبر_نتيجة_أضف_نجاح": "addSuccess",
    "اختبر_نتيجة_أوقف": "stop",
    "اختبر_نتيجة_أوقف_اختبر": "stopTest",
    "اختبر_نتيجة_أوقف_اختبر_شغّل": "stopTestRun",
    "اختبر_نتيجة_ابدأ_اختبر": "startTest",
    "اختبر_نتيجة_ابدأ_اختبر_شغّل": "startTestRun",
    "اختبر_نتيجة_اطبع_أخطاء": "printErrors",
    "اختبر_نتيجة_كان_ناجح": "wasSuccessful",
    # === selectors ===
    "اختر_مُنتخِب_أغلق": "close",
    "اختر_مُنتخِب_ألغِ_التسجيل": "unregister",
    "اختر_مُنتخِب_احصل_خريطة": "get_map",
    "اختر_مُنتخِب_احصل_مفتاح": "get_key",
    "اختر_مُنتخِب_اختر": "select",
    "اختر_مُنتخِب_سجّل": "register",
    "اختر_مُنتخِب_عدّل": "modify",
    # === contextlib ===
    "اخرج_مكدس_أدرج_موعداً_سياق": "enter_context",
    "اخرج_مكدس_رد_النداء": "callback",
    # === sched ===
    "ادخل_موعداً_مطلقاً": "enterabs",
    # === shlex ===
    "ادفع_رمز": "push_token",
    # === contextlib ===
    "ادفع_غير_متزامن_رد_النداء": "push_async_callback",
    # === shlex ===
    "ادفع_مصدر": "push_source",
    # === venv ===
    "اربط_رمزياً_أو_انسخ": "symlink_or_copy",
    "استبدل_متغيرات": "replace_variables",
    # === selectors ===
    "استطلع_مُنتخِب_أغلق": "close",
    "استطلع_مُنتخِب_ألغِ_التسجيل": "unregister",
    "استطلع_مُنتخِب_احصل_خريطة": "get_map",
    "استطلع_مُنتخِب_احصل_مفتاح": "get_key",
    "استطلع_مُنتخِب_اختر": "select",
    "استطلع_مُنتخِب_سجّل": "register",
    "استطلع_مُنتخِب_عدّل": "modify",
    # === multiprocessing ===
    "استقبل_بايتات": "recv_bytes",
    "استقبل_بايتات_إلى": "recv_bytes_into",
    "اسحب_عنصراً": "popitem",
    # === shlex ===
    "اسحب_مصدر": "pop_source",
    # === logging ===
    "اسحب_من_الطابور": "dequeue",
    # === platform ===
    "اسم_النظام_نتيجة_معالج": "processor",
    # === logging ===
    "اضبط": "configure",
    "اضبط_جذر": "configure_root",
    "اضبط_رشّح": "configure_filter",
    "اضبط_مسجّل": "configure_logger",
    "اضبط_معالج": "configure_handler",
    "اضبط_مُنسّق": "configure_formatter",
    # === unittest ===
    "اطبع_خطأ_قائمة": "printErrorList",
    # === cmd ===
    "اطبع_موضوعات": "print_topics",
    # === pydoc ===
    "اعرض_الرمز": "showsymbol",
    "اعرض_الرموز": "listsymbols",
    "اعرض_الكلمات": "listkeywords",
    "اعرض_الموضوع": "showtopic",
    "اعرض_الموضوعات": "listtopics",
    "اعرض_الوحدات": "listmodules",
    # === selectors ===
    "افتراضي_مُنتخِب_أغلق": "close",
    "افتراضي_مُنتخِب_ألغِ_التسجيل": "unregister",
    "افتراضي_مُنتخِب_احصل_خريطة": "get_map",
    "افتراضي_مُنتخِب_احصل_مفتاح": "get_key",
    "افتراضي_مُنتخِب_اختر": "select",
    "افتراضي_مُنتخِب_رقم_الملف": "fileno",
    "افتراضي_مُنتخِب_سجّل": "register",
    "افتراضي_مُنتخِب_عدّل": "modify",
    # === cmd ===
    "افعل_مساعدة": "do_help",
    # === concurrent ===
    "اقتل_عامل": "kill_workers",
    # === mmap ===
    "اقرأ_بايت": "read_byte",
    # === shlex ===
    "اقرأ_رمز": "read_token",
    # === multiprocessing ===
    "اقفل": "Lock",
    "اقفل_مقفل": "locked",
    # === mmap ===
    "اكتب_بايت": "write_byte",
    # === unittest ===
    "اكتشف": "discover",
    # === venv ===
    "امسح_مجلد": "clear_directory",
    # === io ===
    "بايتات_إدخال_إخراج_أغلق_2": "close",
    "بايتات_إدخال_إخراج_أفرغ_2": "flush",
    "بايتات_إدخال_إخراج_احصل_على_القيمة_2": "getvalue",
    "بايتات_إدخال_إخراج_احصل_على_المخزن": "getbuffer",
    "بايتات_إدخال_إخراج_افصل_2": "detach",
    "بايتات_إدخال_إخراج_اقتطع_2": "truncate",
    "بايتات_إدخال_إخراج_اقرأ1_2": "read1",
    "بايتات_إدخال_إخراج_اقرأ_2": "read",
    "بايتات_إدخال_إخراج_اقرأ_الأسطر": "readlines",
    "بايتات_إدخال_إخراج_اقرأ_في1_2": "readinto1",
    "بايتات_إدخال_إخراج_اقرأ_في_2": "readinto",
    "بايتات_إدخال_إخراج_اكتب_2": "write",
    "بايتات_إدخال_إخراج_اكتب_أسطراً_2": "writelines",
    "بايتات_إدخال_إخراج_انتقل_2": "seek",
    "بايتات_إدخال_إخراج_رقم_الملف_2": "fileno",
    "بايتات_إدخال_إخراج_سطر_قراءة_3": "readline",
    "بايتات_إدخال_إخراج_ضع_الموضع_2": "tell",
    "بايتات_إدخال_إخراج_قابل_للانتقال_2": "seekable",
    "بايتات_إدخال_إخراج_قابل_للقراءة_2": "readable",
    "بايتات_إدخال_إخراج_قابل_للكتابة_2": "writable",
    "بايتات_إدخال_إخراج_هو_طرفية_2": "isatty",
    # === cmd ===
    "بعد_الأمر": "postcmd",
    "بعد_الحلقة": "postloop",
    # === venv ===
    "بيئة_باني_أنشئ": "create",
    # === unicodedata ===
    "بيانات_معيار_يونيكود_اسم": "name",
    "بيانات_معيار_يونيكود_بحث": "lookup",
    "بيانات_معيار_يونيكود_تفكيك": "decomposition",
    "بيانات_معيار_يونيكود_عشري": "decimal",
    "بيانات_معيار_يونيكود_معكوس": "mirrored",
    "بيانات_معيار_يونيكود_وحّد": "normalize",
    # === venv ===
    "تأكد_مجلدات": "ensure_directories",
    # === multiprocessing ===
    "تتبّع_مقطع": "track_segment",
    # === shlex ===
    "تحليل_كلمات_نص_إدخال_إخراج_أغلق": "close",
    "تحليل_كلمات_نص_إدخال_إخراج_أفرغ": "flush",
    "تحليل_كلمات_نص_إدخال_إخراج_احصل_على_القيمة": "getvalue",
    "تحليل_كلمات_نص_إدخال_إخراج_افصل": "detach",
    "تحليل_كلمات_نص_إدخال_إخراج_اقتطع": "truncate",
    "تحليل_كلمات_نص_إدخال_إخراج_اقرأ": "read",
    "تحليل_كلمات_نص_إدخال_إخراج_اكتب": "write",
    "تحليل_كلمات_نص_إدخال_إخراج_اكتب_أسطراً": "writelines",
    "تحليل_كلمات_نص_إدخال_إخراج_انتقل": "seek",
    "تحليل_كلمات_نص_إدخال_إخراج_رقم_الملف": "fileno",
    "تحليل_كلمات_نص_إدخال_إخراج_سطر_قراءة": "readline",
    "تحليل_كلمات_نص_إدخال_إخراج_ضع_الموضع": "tell",
    "تحليل_كلمات_نص_إدخال_إخراج_قابل_للانتقال": "seekable",
    "تحليل_كلمات_نص_إدخال_إخراج_قابل_للقراءة": "readable",
    "تحليل_كلمات_نص_إدخال_إخراج_قابل_للكتابة": "writable",
    "تحليل_كلمات_نص_إدخال_إخراج_هو_طرفية": "isatty",
    # === logging ===
    "تحويل_صف_حوّل": "convert",
    "تحويل_صف_حوّل_بـ_مفتاح": "convert_with_key",
    "تحويل_قائمة_اسحب": "pop",
    "تحويل_قائمة_حوّل": "convert",
    "تحويل_قائمة_حوّل_بـ_مفتاح": "convert_with_key",
    "تحويل_قاموس_احصل": "get",
    "تحويل_قاموس_اسحب": "pop",
    "تحويل_قاموس_حوّل": "convert",
    "تحويل_قاموس_حوّل_بـ_مفتاح": "convert_with_key",
    "تحويل_مزيج_حوّل": "convert",
    "تحويل_مزيج_حوّل_بـ_مفتاح": "convert_with_key",
    "تخزين_مؤقت_معالج_أصدر": "emit",
    "تخزين_مؤقت_معالج_أضف_رشّح": "addFilter",
    "تخزين_مؤقت_معالج_أغلق": "close",
    "تخزين_مؤقت_معالج_أفرغ": "flush",
    "تخزين_مؤقت_معالج_أنشئ_اقفل": "createLock",
    "تخزين_مؤقت_معالج_احذف_رشّح": "removeFilter",
    "تخزين_مؤقت_معالج_احصل": "acquire",
    "تخزين_مؤقت_معالج_احصل_اسم": "get_name",
    "تخزين_مؤقت_معالج_حرّر": "release",
    "تخزين_مؤقت_معالج_رشّح": "filter",
    "تخزين_مؤقت_معالج_عالج": "handle",
    "تخزين_مؤقت_معالج_عالج_خطأ": "handleError",
    "تخزين_مؤقت_معالج_عيّن_اسم": "set_name",
    "تخزين_مؤقت_معالج_عيّن_مستوى": "setLevel",
    "تخزين_مؤقت_معالج_عيّن_مُنسّق": "setFormatter",
    "تخزين_مؤقت_معالج_نسّق": "format",
    "تخزين_مؤقت_معالج_ينبغي_أفرغ": "shouldFlush",
    "تخزين_مؤقت_مُنسّق_نسّق": "format",
    "تدفق_معالج_أصدر": "emit",
    "تدفق_معالج_أضف_رشّح": "addFilter",
    "تدفق_معالج_أغلق": "close",
    "تدفق_معالج_أفرغ": "flush",
    "تدفق_معالج_أنشئ_اقفل": "createLock",
    "تدفق_معالج_احذف_رشّح": "removeFilter",
    "تدفق_معالج_احصل": "acquire",
    "تدفق_معالج_احصل_اسم": "get_name",
    "تدفق_معالج_حرّر": "release",
    "تدفق_معالج_رشّح": "filter",
    "تدفق_معالج_عالج": "handle",
    "تدفق_معالج_عالج_خطأ": "handleError",
    "تدفق_معالج_عيّن_اسم": "set_name",
    "تدفق_معالج_عيّن_تدفق": "setStream",
    "تدفق_معالج_عيّن_مستوى": "setLevel",
    "تدفق_معالج_عيّن_مُنسّق": "setFormatter",
    "تدفق_معالج_نسّق": "format",
    # === unittest ===
    "ترابط_مزيج_انتظر_حتى_أي_استدعِ_بـ": "wait_until_any_call_with",
    "ترابط_مزيج_انتظر_حتى_مُستدعى": "wait_until_called",
    "ترابط_مزيج_صفّر_وهمي": "reset_mock",
    "ترابط_وهمي_اربط_وهمي": "attach_mock",
    "ترابط_وهمي_اضبط_وهمي": "configure_mock",
    "ترابط_وهمي_انتظر_حتى_أي_استدعِ_بـ": "wait_until_any_call_with",
    "ترابط_وهمي_انتظر_حتى_مُستدعى": "wait_until_called",
    "ترابط_وهمي_تأكد_أي_استدعِ": "assert_any_call",
    "ترابط_وهمي_تأكد_لا_مُستدعى": "assert_not_called",
    "ترابط_وهمي_تأكد_له_استدعاءات": "assert_has_calls",
    "ترابط_وهمي_تأكد_مُستدعى": "assert_called",
    "ترابط_وهمي_تأكد_مُستدعى_بـ": "assert_called_with",
    "ترابط_وهمي_تأكد_مُستدعى_مرة_واحدة": "assert_called_once",
    "ترابط_وهمي_تأكد_مُستدعى_مرة_واحدة_بـ": "assert_called_once_with",
    "ترابط_وهمي_صفّر_وهمي": "reset_mock",
    "ترابط_وهمي_وهمي_أضف_مواصفة": "mock_add_spec",
    # === concurrent ===
    "تزامن_مستقبلات_مستقبل_استثناء": "exception",
    # === logging ===
    "تسجيل_احصل_مسجّل": "getLogger",
    "تسجيل_معالجات_HTTP_معالج_أغلق": "close",
    "تسجيل_ملف_معالج_أغلق": "close",
    "تسجيل_نسّق_استثناء": "formatException",
    # === difflib ===
    "تسلسل_مطابِق_ابحث_أطول_طابق": "find_longest_match",
    "تسلسل_مطابِق_احصل_رموز_التشغيل": "get_opcodes",
    "تسلسل_مطابِق_احصل_مجمّع_رموز_التشغيل": "get_grouped_opcodes",
    "تسلسل_مطابِق_احصل_مطابقة_كتل": "get_matching_blocks",
    "تسلسل_مطابِق_حقيقي_سريع_نسبة": "real_quick_ratio",
    "تسلسل_مطابِق_سريع_نسبة": "quick_ratio",
    "تسلسل_مطابِق_عيّن_تسلسل1": "set_seq1",
    "تسلسل_مطابِق_عيّن_تسلسل2": "set_seq2",
    "تسلسل_مطابِق_عيّن_تسلسلات": "set_seqs",
    # === enum ===
    "تعداد_قاموس_حدّث": "update",
    # === pydoc ===
    "تفاعل": "interact",
    # === multiprocessing ===
    "تقاطع_حدّث": "intersection_update",
    "تماثلي_فرق": "symmetric_difference",
    "تماثلي_فرق_حدّث": "symmetric_difference_update",
    # === pydoc ===
    "تمثيل_تمثيل": "repr",
    "تمثيل_تمثيل1": "repr1",
    "تمثيل_تمثيل_صف": "repr_tuple",
    "تمثيل_تمثيل_طابور_مزدوج": "repr_deque",
    "تمثيل_تمثيل_عدد_صحيح": "repr_int",
    "تمثيل_تمثيل_عيّن": "repr_set",
    "تمثيل_تمثيل_قائمة": "repr_list",
    "تمثيل_تمثيل_قاموس": "repr_dict",
    "تمثيل_تمثيل_مجموعة_مجمّدة": "repr_frozenset",
    "تمثيل_تمثيل_مصفوفة": "repr_array",
    "تمثيل_تمثيل_نسخة": "repr_instance",
    "تمثيل_تمثيل_نص": "repr_str",
    "تمثيل_يونيكود": "repr_unicode",
    # === graphlib ===
    "توبولوجي_مرتّب_احصل_جاهز": "get_ready",
    "توبولوجي_مرتّب_تم": "done",
    "توبولوجي_مرتّب_ثابت_ترتيب": "static_order",
    "توبولوجي_مرتّب_جهّز": "prepare",
    "توبولوجي_مرتّب_هو_نشط": "is_active",
    # === pydoc ===
    "توثيق_احصل_على_مكان_التوثيق": "getdocloc",
    "توثيق_افشل": "fail",
    "توثيق_بايثون_HTML_تمثيل_تمثيل_نص": "repr_string",
    "توثيق_بايثون_احصل_على_السطر": "getline",
    "توثيق_بايثون_نص_تمثيل_تمثيل_نص": "repr_string",
    "توثيق_توثيق_الدالة": "docroutine",
    "توثيق_مستند": "document",
    "توثيق_وثّق_البيانات": "docdata",
    "توثيق_وثّق_الخاصية": "docproperty",
    "توثيق_وثّق_الصنف": "docclass",
    "توثيق_وثّق_الوحدة": "docmodule",
    "توثيق_وثّق_غيره": "docother",
    # === venv ===
    "ثبّت_سكوردات": "install_scripts",
    # === typing ===
    "ثنائي_إدخال_إخراج_أغلق": "close",
    "ثنائي_إدخال_إخراج_أفرغ": "flush",
    "ثنائي_إدخال_إخراج_اقتطع": "truncate",
    "ثنائي_إدخال_إخراج_اقرأ": "read",
    "ثنائي_إدخال_إخراج_اقرأ_الأسطر": "readlines",
    "ثنائي_إدخال_إخراج_اكتب": "write",
    "ثنائي_إدخال_إخراج_اكتب_أسطراً": "writelines",
    "ثنائي_إدخال_إخراج_انتقل": "seek",
    "ثنائي_إدخال_إخراج_رقم_الملف": "fileno",
    "ثنائي_إدخال_إخراج_سطر_قراءة": "readline",
    "ثنائي_إدخال_إخراج_ضع_الموضع": "tell",
    "ثنائي_إدخال_إخراج_قابل_للانتقال": "seekable",
    "ثنائي_إدخال_إخراج_قابل_للقراءة": "readable",
    "ثنائي_إدخال_إخراج_قابل_للكتابة": "writable",
    "ثنائي_إدخال_إخراج_هو_طرفية": "isatty",
    # === logging ===
    "جذر_مسجّل_أضف_رشّح": "addFilter",
    "جذر_مسجّل_أضف_معالج": "addHandler",
    "جذر_مسجّل_ابحث_مُستدعية": "findCaller",
    "جذر_مسجّل_احذف_رشّح": "removeFilter",
    "جذر_مسجّل_احذف_معالج": "removeHandler",
    "جذر_مسجّل_احصل_أبناء": "getChildren",
    "جذر_مسجّل_احصل_ابن": "getChild",
    "جذر_مسجّل_احصل_فعّال_مستوى": "getEffectiveLevel",
    "جذر_مسجّل_استثناء": "exception",
    "جذر_مسجّل_استدعِ_معالجات": "callHandlers",
    "جذر_مسجّل_اعمل_سجل": "makeRecord",
    "جذر_مسجّل_تحذير": "warning",
    "جذر_مسجّل_تصحيح": "debug",
    "جذر_مسجّل_حذّر": "warn",
    "جذر_مسجّل_حرج": "critical",
    "جذر_مسجّل_خطأ": "error",
    "جذر_مسجّل_رشّح": "filter",
    "جذر_مسجّل_سجل": "log",
    "جذر_مسجّل_عالج": "handle",
    "جذر_مسجّل_عيّن_مستوى": "setLevel",
    "جذر_مسجّل_قاتل": "fatal",
    "جذر_مسجّل_له_معالجات": "hasHandlers",
    "جذر_مسجّل_معلومات": "info",
    "جذر_مسجّل_هو_مُفعّل_لأجل": "isEnabledFor",
    # === venv ===
    "جهّز_بايثون": "setup_python",
    "جهّز_سكوردات": "setup_scripts",
    # === multiprocessing ===
    "حاجز_وكيل_انتظر": "wait",
    "حاجز_وكيل_صفّر": "reset",
    "حاصل_وكيل_احصل": "acquire",
    "حاصل_وكيل_حرّر": "release",
    "حاصل_وكيل_مقفل": "locked",
    "حدث_امسح": "clear",
    "حدث_انتظر": "wait",
    "حدث_عيّن": "set",
    "حدث_هو_عيّن": "is_set",
    "حدث_وكيل_امسح": "clear",
    "حدث_وكيل_انتظر": "wait",
    "حدث_وكيل_عيّن": "set",
    "حدث_وكيل_هو_عيّن": "is_set",
    "حرّر_مقطع": "release_segment",
    # === mmap ===
    "حرّك": "move",
    # === logging ===
    "حزمة_بيانات_معالج_أرسل": "send",
    "حزمة_بيانات_معالج_أصدر": "emit",
    "حزمة_بيانات_معالج_أضف_رشّح": "addFilter",
    "حزمة_بيانات_معالج_أغلق": "close",
    "حزمة_بيانات_معالج_أفرغ": "flush",
    "حزمة_بيانات_معالج_أنشئ_اقفل": "createLock",
    "حزمة_بيانات_معالج_أنشئ_مقبس": "createSocket",
    "حزمة_بيانات_معالج_احذف_رشّح": "removeFilter",
    "حزمة_بيانات_معالج_احصل": "acquire",
    "حزمة_بيانات_معالج_احصل_اسم": "get_name",
    "حزمة_بيانات_معالج_اعمل_بايكن": "makePickle",
    "حزمة_بيانات_معالج_اعمل_مقبس": "makeSocket",
    "حزمة_بيانات_معالج_حرّر": "release",
    "حزمة_بيانات_معالج_رشّح": "filter",
    "حزمة_بيانات_معالج_عالج": "handle",
    "حزمة_بيانات_معالج_عالج_خطأ": "handleError",
    "حزمة_بيانات_معالج_عيّن_اسم": "set_name",
    "حزمة_بيانات_معالج_عيّن_مستوى": "setLevel",
    "حزمة_بيانات_معالج_عيّن_مُنسّق": "setFormatter",
    "حزمة_بيانات_معالج_نسّق": "format",
    # === cmd ===
    "حلقة_الأوامر": "cmdloop",
    "حلل_السطر": "parseline",
    # === unittest ===
    "حمّل_اختبارات_من_أسماء": "loadTestsFromNames",
    "حمّل_اختبارات_من_اختبر_حالة": "loadTestsFromTestCase",
    "حمّل_اختبارات_من_اسم": "loadTestsFromName",
    "حمّل_اختبارات_من_وحدة": "loadTestsFromModule",
    # === ctypes ===
    "حمّل_مكتبة": "LoadLibrary",
    # === multiprocessing ===
    "خادم_أنشئ": "create",
    "خادم_أنقِص_المرجع": "decref",
    "خادم_أوقف": "shutdown",
    "خادم_احصل_دوال": "get_methods",
    "خادم_اقبل_اتصال": "accept_connection",
    "خادم_بديل_احصل_على_القيمة": "fallback_getvalue",
    "خادم_بديل_تمثيل": "fallback_repr",
    "خادم_بديل_نص": "fallback_str",
    "خادم_تصحيح_معلومات": "debug_info",
    "خادم_خدّم_عميل": "serve_client",
    "خادم_خدّم_للأبد": "serve_forever",
    "خادم_زِد_المرجع": "incref",
    "خادم_عالج_اطلب": "handle_request",
    "خادم_عدد_من_كائنات": "number_of_objects",
    "خادم_مقبل": "accepter",
    "خادم_وهمي": "dummy",
    # === io ===
    "خام_إدخال_إخراج_أساس_أغلق_2": "close",
    "خام_إدخال_إخراج_أساس_أفرغ_2": "flush",
    "خام_إدخال_إخراج_أساس_اقتطع_2": "truncate",
    "خام_إدخال_إخراج_أساس_اقرأ_2": "read",
    "خام_إدخال_إخراج_أساس_اقرأ_الأسطر": "readlines",
    "خام_إدخال_إخراج_أساس_اقرأ_في_2": "readinto",
    "خام_إدخال_إخراج_أساس_اقرأ_كل_2": "readall",
    "خام_إدخال_إخراج_أساس_اكتب_2": "write",
    "خام_إدخال_إخراج_أساس_اكتب_أسطراً_2": "writelines",
    "خام_إدخال_إخراج_أساس_انتقل_2": "seek",
    "خام_إدخال_إخراج_أساس_رقم_الملف_2": "fileno",
    "خام_إدخال_إخراج_أساس_سطر_قراءة_3": "readline",
    "خام_إدخال_إخراج_أساس_ضع_الموضع_2": "tell",
    "خام_إدخال_إخراج_أساس_قابل_للانتقال_2": "seekable",
    "خام_إدخال_إخراج_أساس_قابل_للقراءة_2": "readable",
    "خام_إدخال_إخراج_أساس_قابل_للكتابة_2": "writable",
    "خام_إدخال_إخراج_أساس_هو_طرفية_2": "isatty",
    # === logging ===
    "خريطة_أولوية": "mapPriority",
    "خريطة_سجل_سجل": "mapLogRecord",
    # === multiprocessing ===
    "خريطة_نتيجة_احصل": "get",
    "خريطة_نتيجة_انتظر": "wait",
    "خريطة_نتيجة_جاهز": "ready",
    "خريطة_نتيجة_ناجح": "successful",
    # === shlex ===
    "خطأ_زعيم": "error_leader",
    "خطاف_المصدر": "sourcehook",
    # === multiprocessing ===
    "خيط_مجموعة_MAP_نجمة": "starmap",
    "خيط_مجموعة_MAP_نجمة_غير_متزامن": "starmap_async",
    "خيط_مجموعة_imap": "imap",
    "خيط_مجموعة_imap_غير_مرتّب": "imap_unordered",
    "خيط_مجموعة_أغلق": "close",
    "خيط_مجموعة_أنهِ": "terminate",
    "خيط_مجموعة_اربط": "join",
    "خيط_مجموعة_خريطة": "map",
    "خيط_مجموعة_خريطة_غير_متزامن": "map_async",
    "خيط_مجموعة_طبّق": "apply",
    "خيط_مجموعة_طبّق_غير_متزامن": "apply_async",
    "خيط_مجموعة_عالج": "Process",
    # === concurrent ===
    "خيط_مجموعة_منفّذ_أرسل": "submit",
    "خيط_مجموعة_منفّذ_أوقف": "shutdown",
    "خيط_مجموعة_منفّذ_جهّز_سياق": "prepare_context",
    "خيط_مجموعة_منفّذ_خريطة": "map",
    # === unittest ===
    "دالة_اختبر_حالة_أدرج_موعداً_سياق": "enterContext",
    "دالة_اختبر_حالة_أدرج_موعداً_صنف_سياق": "enterClassContext",
    "دالة_اختبر_حالة_أضف_صنف_نظّف": "addClassCleanup",
    "دالة_اختبر_حالة_أضف_نظّف": "addCleanup",
    "دالة_اختبر_حالة_أضف_نوع_مساواة_دالة": "addTypeEqualityFunc",
    "دالة_اختبر_حالة_افتراضي_اختبر_نتيجة": "defaultTestResult",
    "دالة_اختبر_حالة_افشل": "fail",
    "دالة_اختبر_حالة_افعل_تنظيفات": "doCleanups",
    "دالة_اختبر_حالة_افعل_صنف_تنظيفات": "doClassCleanups",
    "دالة_اختبر_حالة_تأكد_أصغر": "assertLess",
    "دالة_اختبر_حالة_تأكد_أصغر_يساوي": "assertLessEqual",
    "دالة_اختبر_حالة_تأكد_أكبر": "assertGreater",
    "دالة_اختبر_حالة_تأكد_أكبر_يساوي": "assertGreaterEqual",
    "دالة_اختبر_حالة_تأكد_بدايات_بـ": "assertStartsWith",
    "دالة_اختبر_حالة_تأكد_بلا_سجلات": "assertNoLogs",
    "دالة_اختبر_حالة_تأكد_تسلسل_يساوي": "assertSequenceEqual",
    "دالة_اختبر_حالة_تأكد_تعبير_نمطي": "assertRegex",
    "دالة_اختبر_حالة_تأكد_تقريباً_يساوي": "assertAlmostEqual",
    "دالة_اختبر_حالة_تأكد_خطأ": "assertFalse",
    "دالة_اختبر_حالة_تأكد_سجلات": "assertLogs",
    "دالة_اختبر_حالة_تأكد_صحيح": "assertTrue",
    "دالة_اختبر_حالة_تأكد_صف_يساوي": "assertTupleEqual",
    "دالة_اختبر_حالة_تأكد_عدّ_يساوي": "assertCountEqual",
    "دالة_اختبر_حالة_تأكد_عيّن_يساوي": "assertSetEqual",
    "دالة_اختبر_حالة_تأكد_في": "assertIn",
    "دالة_اختبر_حالة_تأكد_قائمة_يساوي": "assertListEqual",
    "دالة_اختبر_حالة_تأكد_قاموس_يساوي": "assertDictEqual",
    "دالة_اختبر_حالة_تأكد_لا_بدايات_بـ": "assertNotStartsWith",
    "دالة_اختبر_حالة_تأكد_لا_تعبير_نمطي": "assertNotRegex",
    "دالة_اختبر_حالة_تأكد_لا_تقريباً_يساوي": "assertNotAlmostEqual",
    "دالة_اختبر_حالة_تأكد_لا_في": "assertNotIn",
    "دالة_اختبر_حالة_تأكد_لا_له_سمة": "assertNotHasAttr",
    "دالة_اختبر_حالة_تأكد_لا_نهايات_بـ": "assertNotEndsWith",
    "دالة_اختبر_حالة_تأكد_لا_هو_صنف_فرعي": "assertNotIsSubclass",
    "دالة_اختبر_حالة_تأكد_لا_هو_نسخة": "assertNotIsInstance",
    "دالة_اختبر_حالة_تأكد_لا_يساوي": "assertNotEqual",
    "دالة_اختبر_حالة_تأكد_له_سمة": "assertHasAttr",
    "دالة_اختبر_حالة_تأكد_متعدد_سطر_يساوي": "assertMultiLineEqual",
    "دالة_اختبر_حالة_تأكد_نهايات_بـ": "assertEndsWith",
    "دالة_اختبر_حالة_تأكد_هو": "assertIs",
    "دالة_اختبر_حالة_تأكد_هو_صنف_فرعي": "assertIsSubclass",
    "دالة_اختبر_حالة_تأكد_هو_لا": "assertIsNot",
    "دالة_اختبر_حالة_تأكد_هو_لا_شيء": "assertIsNone",
    "دالة_اختبر_حالة_تأكد_هو_لا_لا_شيء": "assertIsNotNone",
    "دالة_اختبر_حالة_تأكد_هو_نسخة": "assertIsInstance",
    "دالة_اختبر_حالة_تأكد_يحذّر": "assertWarns",
    "دالة_اختبر_حالة_تأكد_يحذّر_تعبير_نمطي": "assertWarnsRegex",
    "دالة_اختبر_حالة_تأكد_يرفع": "assertRaises",
    "دالة_اختبر_حالة_تأكد_يرفع_تعبير_نمطي": "assertRaisesRegex",
    "دالة_اختبر_حالة_تأكد_يساوي": "assertEqual",
    "دالة_اختبر_حالة_تجاوز_اختبر": "skipTest",
    "دالة_اختبر_حالة_تصحيح": "debug",
    "دالة_اختبر_حالة_شغّل": "run",
    "دالة_اختبر_حالة_عدّ_اختبر_حالات": "countTestCases",
    "دالة_اختبر_حالة_عيّن_لأعلى": "setUp",
    "دالة_اختبر_حالة_عيّن_لأعلى_صنف": "setUpClass",
    "دالة_اختبر_حالة_فرعي_اختبر": "subTest",
    "دالة_اختبر_حالة_قصير_وصف": "shortDescription",
    "دالة_اختبر_حالة_مزّق_لأسفل": "tearDown",
    "دالة_اختبر_حالة_مزّق_لأسفل_صنف": "tearDownClass",
    "دالة_اختبر_حالة_معرف": "id",
    # === logging ===
    "دوّار_ملف_معالج_أصدر": "emit",
    "دوّار_ملف_معالج_أضف_رشّح": "addFilter",
    "دوّار_ملف_معالج_أغلق": "close",
    "دوّار_ملف_معالج_أفرغ": "flush",
    "دوّار_ملف_معالج_أنشئ_اقفل": "createLock",
    "دوّار_ملف_معالج_احذف_رشّح": "removeFilter",
    "دوّار_ملف_معالج_احصل": "acquire",
    "دوّار_ملف_معالج_احصل_اسم": "get_name",
    "دوّار_ملف_معالج_افعل_تجاوز": "doRollover",
    "دوّار_ملف_معالج_تدوير_اسم_ملف": "rotation_filename",
    "دوّار_ملف_معالج_حرّر": "release",
    "دوّار_ملف_معالج_دوّر": "rotate",
    "دوّار_ملف_معالج_رشّح": "filter",
    "دوّار_ملف_معالج_عالج": "handle",
    "دوّار_ملف_معالج_عالج_خطأ": "handleError",
    "دوّار_ملف_معالج_عيّن_اسم": "set_name",
    "دوّار_ملف_معالج_عيّن_تدفق": "setStream",
    "دوّار_ملف_معالج_عيّن_مستوى": "setLevel",
    "دوّار_ملف_معالج_عيّن_مُنسّق": "setFormatter",
    "دوّار_ملف_معالج_نسّق": "format",
    "دوّار_ملف_معالج_ينبغي_تجاوز": "shouldRollover",
    # === types ===
    "ديناميكي_صنف_سمة_محذوف": "deleter",
    "ديناميكي_صنف_سمة_مُستخرج": "getter",
    "ديناميكي_صنف_سمة_مُعيّن": "setter",
    # === logging ===
    "ذاكرة_معالج_أصدر": "emit",
    "ذاكرة_معالج_أضف_رشّح": "addFilter",
    "ذاكرة_معالج_أغلق": "close",
    "ذاكرة_معالج_أفرغ": "flush",
    "ذاكرة_معالج_أنشئ_اقفل": "createLock",
    "ذاكرة_معالج_احذف_رشّح": "removeFilter",
    "ذاكرة_معالج_احصل": "acquire",
    "ذاكرة_معالج_احصل_اسم": "get_name",
    "ذاكرة_معالج_حرّر": "release",
    "ذاكرة_معالج_رشّح": "filter",
    "ذاكرة_معالج_عالج": "handle",
    "ذاكرة_معالج_عالج_خطأ": "handleError",
    "ذاكرة_معالج_عيّن_اسم": "set_name",
    "ذاكرة_معالج_عيّن_مستوى": "setLevel",
    "ذاكرة_معالج_عيّن_مُنسّق": "setFormatter",
    "ذاكرة_معالج_نسّق": "format",
    "ذاكرة_معالج_ينبغي_أفرغ": "shouldFlush",
    # === mmap ===
    "ذاكرة_مُخزَّنة_أغلق": "close",
    "ذاكرة_مُخزَّنة_أفرغ": "flush",
    "ذاكرة_مُخزَّنة_ابحث": "find",
    "ذاكرة_مُخزَّنة_اقرأ": "read",
    "ذاكرة_مُخزَّنة_اكتب": "write",
    "ذاكرة_مُخزَّنة_انتقل": "seek",
    "ذاكرة_مُخزَّنة_حجم": "size",
    "ذاكرة_مُخزَّنة_سطر_قراءة": "readline",
    "ذاكرة_مُخزَّنة_ضع_الموضع": "tell",
    "ذاكرة_مُخزَّنة_قابل_للانتقال": "seekable",
    # === pydoc ===
    "رابط_الأب": "parentlink",
    "رابط_الاسم": "namelink",
    "رابط_الوحدة": "modulelink",
    "رابط_حزمة": "modpkglink",
    "رابط_ملف": "filelink",
    # === unittest ===
    "رتّب_اختبر_دوال_باستخدام": "sortTestMethodsUsing",
    # === graphlib ===
    "رسوم_بيانية_توبولوجي_مرتّب_أضف": "add",
    # === logging ===
    "رشّح_رشّح": "filter",
    # === venv ===
    "رقّ_اعتماديات": "upgrade_dependencies",
    # === pydoc ===
    "رمادي": "grey",
    # === logging ===
    "رمّز_أولوية": "encodePriority",
    # === multiprocessing ===
    "زامن_مدير_ابدأ": "start",
    "زامن_مدير_اتصل": "connect",
    "زامن_مدير_احصل_خادم": "get_server",
    "زامن_مدير_اربط": "join",
    "زامن_مدير_حدث": "Event",
    "زامن_مدير_سجّل": "register",
    "زامن_مدير_شرط": "Condition",
    "زامن_مدير_طابور": "Queue",
    "زامن_مدير_عيّن": "set",
    "زامن_مدير_قائمة": "list",
    "زامن_مدير_قاموس": "dict",
    "زامن_مدير_قيمة": "Value",
    "زامن_مدير_مجموعة": "Pool",
    "زامن_مدير_مصفوفة": "Array",
    "زامن_مدير_نطاق_اسم": "Namespace",
    # === unittest ===
    "سحري_وهمي_اربط_وهمي": "attach_mock",
    "سحري_وهمي_اضبط_وهمي": "configure_mock",
    "سحري_وهمي_تأكد_أي_استدعِ": "assert_any_call",
    "سحري_وهمي_تأكد_لا_مُستدعى": "assert_not_called",
    "سحري_وهمي_تأكد_له_استدعاءات": "assert_has_calls",
    "سحري_وهمي_تأكد_مُستدعى": "assert_called",
    "سحري_وهمي_تأكد_مُستدعى_بـ": "assert_called_with",
    "سحري_وهمي_تأكد_مُستدعى_مرة_واحدة": "assert_called_once",
    "سحري_وهمي_تأكد_مُستدعى_مرة_واحدة_بـ": "assert_called_once_with",
    "سحري_وهمي_صفّر_وهمي": "reset_mock",
    "سحري_وهمي_وهمي_أضف_مواصفة": "mock_add_spec",
    # === cmd ===
    "سطر_فارغ": "emptyline",
    # === rlcompleter ===
    "سمة_تطابقات": "attr_matches",
    # === enum ===
    "سمة_صنف_محذوف": "deleter",
    "سمة_صنف_مُستخرج": "getter",
    "سمة_صنف_مُعيّن": "setter",
    # === unittest ===
    "سمة_صنف_وهمي_اربط_وهمي": "attach_mock",
    "سمة_صنف_وهمي_اضبط_وهمي": "configure_mock",
    "سمة_صنف_وهمي_تأكد_أي_استدعِ": "assert_any_call",
    "سمة_صنف_وهمي_تأكد_لا_مُستدعى": "assert_not_called",
    "سمة_صنف_وهمي_تأكد_له_استدعاءات": "assert_has_calls",
    "سمة_صنف_وهمي_تأكد_مُستدعى": "assert_called",
    "سمة_صنف_وهمي_تأكد_مُستدعى_بـ": "assert_called_with",
    "سمة_صنف_وهمي_تأكد_مُستدعى_مرة_واحدة": "assert_called_once",
    "سمة_صنف_وهمي_تأكد_مُستدعى_مرة_واحدة_بـ": "assert_called_once_with",
    "سمة_صنف_وهمي_صفّر_وهمي": "reset_mock",
    "سمة_صنف_وهمي_وهمي_أضف_مواصفة": "mock_add_spec",
    # === contextvars ===
    "سياق_شغّل": "run",
    # === logging ===
    "شائع_مسجّل_إعداد": "common_logger_config",
    # === rlcompleter ===
    "شامل_تطابقات": "global_matches",
    # === multiprocessing ===
    "شرط_انتظر": "wait",
    "شرط_انتظر_لأجل": "wait_for",
    "شرط_نبّه": "notify",
    "شرط_نبّه_كل": "notify_all",
    "شرط_وكيل_احصل": "acquire",
    "شرط_وكيل_انتظر": "wait",
    "شرط_وكيل_انتظر_لأجل": "wait_for",
    "شرط_وكيل_حرّر": "release",
    "شرط_وكيل_مقفل": "locked",
    "شرط_وكيل_نبّه": "notify",
    "شرط_وكيل_نبّه_كل": "notify_all",
    # === unittest ===
    "شغّل_اختبارات": "runTests",
    "شغّل_اختبر": "runTest",
    # === logging ===
    "ضع_حامل_أضف_ذيلياً": "append",
    "طابور_معالج_أصدر": "emit",
    "طابور_معالج_أضف_رشّح": "addFilter",
    "طابور_معالج_أغلق": "close",
    "طابور_معالج_أفرغ": "flush",
    "طابور_معالج_أنشئ_اقفل": "createLock",
    "طابور_معالج_احذف_رشّح": "removeFilter",
    "طابور_معالج_احصل": "acquire",
    "طابور_معالج_احصل_اسم": "get_name",
    "طابور_معالج_جهّز": "prepare",
    "طابور_معالج_حرّر": "release",
    "طابور_معالج_رشّح": "filter",
    "طابور_معالج_عالج": "handle",
    "طابور_معالج_عالج_خطأ": "handleError",
    "طابور_معالج_عيّن_اسم": "set_name",
    "طابور_معالج_عيّن_مستوى": "setLevel",
    "طابور_معالج_عيّن_مُنسّق": "setFormatter",
    "طابور_معالج_نسّق": "format",
    "طابور_مُستمع_أوقف": "stop",
    "طابور_مُستمع_ابدأ": "start",
    "طابور_مُستمع_جهّز": "prepare",
    "طابور_مُستمع_عالج": "handle",
    # === multiprocessing ===
    "طبّق_نتيجة_احصل": "get",
    "طبّق_نتيجة_انتظر": "wait",
    "طبّق_نتيجة_جاهز": "ready",
    "طبّق_نتيجة_ناجح": "successful",
    "عالج_أغلق": "close",
    "عالج_أنهِ": "terminate",
    "عالج_ابدأ": "start",
    "عالج_اربط": "join",
    "عالج_اقتل": "kill",
    "عالج_شغّل": "run",
    # === concurrent ===
    "عالج_مجموعة_منفّذ_أرسل": "submit",
    "عالج_مجموعة_منفّذ_أوقف": "shutdown",
    "عالج_مجموعة_منفّذ_خريطة": "map",
    # === logging ===
    "عدم_معالج_أصدر": "emit",
    "عدم_معالج_أضف_رشّح": "addFilter",
    "عدم_معالج_أغلق": "close",
    "عدم_معالج_أفرغ": "flush",
    "عدم_معالج_أنشئ_اقفل": "createLock",
    "عدم_معالج_احذف_رشّح": "removeFilter",
    "عدم_معالج_احصل": "acquire",
    "عدم_معالج_احصل_اسم": "get_name",
    "عدم_معالج_حرّر": "release",
    "عدم_معالج_رشّح": "filter",
    "عدم_معالج_عالج": "handle",
    "عدم_معالج_عالج_خطأ": "handleError",
    "عدم_معالج_عيّن_اسم": "set_name",
    "عدم_معالج_عيّن_مستوى": "setLevel",
    "عدم_معالج_عيّن_مُنسّق": "setFormatter",
    "عدم_معالج_نسّق": "format",
    # === pydoc ===
    "عريض": "bold",
    # === cmd ===
    "عمودي": "columnize",
    # === concurrent ===
    "عيّن_استثناء": "set_exception",
    # === multiprocessing ===
    "عيّن_افتراضياً": "setdefault",
    # === io ===
    "عيّن_الحالة": "setstate",
    # === logging ===
    "عيّن_سجل_سجل_مصنع": "setLogRecordFactory",
    "عيّن_مسجّل_صنف": "setLoggerClass",
    # === concurrent ===
    "عيّن_نتيجة": "set_result",
    # === logging ===
    "عيّن_هدف": "setTarget",
    # === multiprocessing ===
    "عيّن_وكيل_أضف": "add",
    "عيّن_وكيل_اتحاد": "union",
    "عيّن_وكيل_احذف": "remove",
    "عيّن_وكيل_ارمِ": "discard",
    "عيّن_وكيل_اسحب": "pop",
    "عيّن_وكيل_امسح": "clear",
    "عيّن_وكيل_انسخ": "copy",
    "عيّن_وكيل_تقاطع": "intersection",
    "عيّن_وكيل_حدّث": "update",
    "عيّن_وكيل_فرق": "difference",
    # === concurrent ===
    "عيّن_يشتغل_أو_نبّه_ألغِ": "set_running_or_notify_cancel",
    # === unittest ===
    "غير_قابل_للاستدعاء_سحري_وهمي_اربط_وهمي": "attach_mock",
    "غير_قابل_للاستدعاء_سحري_وهمي_اضبط_وهمي": "configure_mock",
    "غير_قابل_للاستدعاء_سحري_وهمي_تأكد_أي_استدعِ": "assert_any_call",
    "غير_قابل_للاستدعاء_سحري_وهمي_تأكد_لا_مُستدعى": "assert_not_called",
    "غير_قابل_للاستدعاء_سحري_وهمي_تأكد_له_استدعاءات": "assert_has_calls",
    "غير_قابل_للاستدعاء_سحري_وهمي_تأكد_مُستدعى": "assert_called",
    "غير_قابل_للاستدعاء_سحري_وهمي_تأكد_مُستدعى_بـ": "assert_called_with",
    "غير_قابل_للاستدعاء_سحري_وهمي_تأكد_مُستدعى_مرة_واحدة": "assert_called_once",
    "غير_قابل_للاستدعاء_سحري_وهمي_تأكد_مُستدعى_مرة_واحدة_بـ": "assert_called_once_with",
    "غير_قابل_للاستدعاء_سحري_وهمي_صفّر_وهمي": "reset_mock",
    "غير_قابل_للاستدعاء_سحري_وهمي_وهمي_أضف_مواصفة": "mock_add_spec",
    "غير_قابل_للاستدعاء_وهمي_اربط_وهمي": "attach_mock",
    "غير_قابل_للاستدعاء_وهمي_اضبط_وهمي": "configure_mock",
    "غير_قابل_للاستدعاء_وهمي_تأكد_أي_استدعِ": "assert_any_call",
    "غير_قابل_للاستدعاء_وهمي_تأكد_لا_مُستدعى": "assert_not_called",
    "غير_قابل_للاستدعاء_وهمي_تأكد_له_استدعاءات": "assert_has_calls",
    "غير_قابل_للاستدعاء_وهمي_تأكد_مُستدعى": "assert_called",
    "غير_قابل_للاستدعاء_وهمي_تأكد_مُستدعى_بـ": "assert_called_with",
    "غير_قابل_للاستدعاء_وهمي_تأكد_مُستدعى_مرة_واحدة": "assert_called_once",
    "غير_قابل_للاستدعاء_وهمي_تأكد_مُستدعى_مرة_واحدة_بـ": "assert_called_once_with",
    "غير_قابل_للاستدعاء_وهمي_صفّر_وهمي": "reset_mock",
    "غير_قابل_للاستدعاء_وهمي_وهمي_أضف_مواصفة": "mock_add_spec",
    # === contextlib ===
    "غير_متزامن_اخرج_مكدس_أدرج_موعداً_سياق": "enter_context",
    "غير_متزامن_اخرج_مكدس_أدرج_موعداً_غير_متزامن_سياق": "enter_async_context",
    "غير_متزامن_اخرج_مكدس_أغلق_غير_متزامن": "aclose",
    "غير_متزامن_اخرج_مكدس_ادفع_غير_متزامن_اخرج": "push_async_exit",
    "غير_متزامن_اخرج_مكدس_رد_النداء": "callback",
    # === unittest ===
    "غير_متزامن_عيّن_لأعلى": "asyncSetUp",
    "غير_متزامن_مزّق_لأسفل": "asyncTearDown",
    "غير_متزامن_وهمي_اربط_وهمي": "attach_mock",
    "غير_متزامن_وهمي_اضبط_وهمي": "configure_mock",
    "غير_متزامن_وهمي_تأكد_أي_استدعِ": "assert_any_call",
    "غير_متزامن_وهمي_تأكد_أي_انتظر": "assert_any_await",
    "غير_متزامن_وهمي_تأكد_لا_مُستدعى": "assert_not_called",
    "غير_متزامن_وهمي_تأكد_لا_مُنتظر": "assert_not_awaited",
    "غير_متزامن_وهمي_تأكد_له_استدعاءات": "assert_has_calls",
    "غير_متزامن_وهمي_تأكد_له_ينتظر": "assert_has_awaits",
    "غير_متزامن_وهمي_تأكد_مُستدعى": "assert_called",
    "غير_متزامن_وهمي_تأكد_مُستدعى_بـ": "assert_called_with",
    "غير_متزامن_وهمي_تأكد_مُستدعى_مرة_واحدة": "assert_called_once",
    "غير_متزامن_وهمي_تأكد_مُستدعى_مرة_واحدة_بـ": "assert_called_once_with",
    "غير_متزامن_وهمي_تأكد_مُنتظر": "assert_awaited",
    "غير_متزامن_وهمي_تأكد_مُنتظر_بـ": "assert_awaited_with",
    "غير_متزامن_وهمي_تأكد_مُنتظر_مرة_واحدة": "assert_awaited_once",
    "غير_متزامن_وهمي_تأكد_مُنتظر_مرة_واحدة_بـ": "assert_awaited_once_with",
    "غير_متزامن_وهمي_صفّر_وهمي": "reset_mock",
    "غير_متزامن_وهمي_مزيج_تأكد_أي_انتظر": "assert_any_await",
    "غير_متزامن_وهمي_مزيج_تأكد_لا_مُنتظر": "assert_not_awaited",
    "غير_متزامن_وهمي_مزيج_تأكد_له_ينتظر": "assert_has_awaits",
    "غير_متزامن_وهمي_مزيج_تأكد_مُنتظر": "assert_awaited",
    "غير_متزامن_وهمي_مزيج_تأكد_مُنتظر_بـ": "assert_awaited_with",
    "غير_متزامن_وهمي_مزيج_تأكد_مُنتظر_مرة_واحدة": "assert_awaited_once",
    "غير_متزامن_وهمي_مزيج_تأكد_مُنتظر_مرة_واحدة_بـ": "assert_awaited_once_with",
    "غير_متزامن_وهمي_مزيج_صفّر_وهمي": "reset_mock",
    "غير_متزامن_وهمي_وهمي_أضف_مواصفة": "mock_add_spec",
    # === mmap ===
    "غيّر_الحجم": "resize",
    # === multiprocessing ===
    "فرق_حدّث": "difference_update",
    "فكّ_الرابط": "unlink",
    "قائمة_مقاطع": "list_segments",
    "قائمة_وكيل_أدخل": "insert",
    "قائمة_وكيل_أضف_ذيلياً": "append",
    "قائمة_وكيل_احذف": "remove",
    "قائمة_وكيل_اسحب": "pop",
    "قائمة_وكيل_اعكس": "reverse",
    "قائمة_وكيل_امسح": "clear",
    "قائمة_وكيل_انسخ": "copy",
    "قائمة_وكيل_رتّب": "sort",
    "قائمة_وكيل_عدّ": "count",
    "قائمة_وكيل_فهرس": "index",
    "قائمة_وكيل_وسّع": "extend",
    "قابل_للمشاركة_قائمة": "ShareableList",
    "قابل_للمشاركة_قائمة_عدّ": "count",
    "قابل_للمشاركة_قائمة_فهرس": "index",
    # === logging ===
    "قاموس_مُضبط_إعداد_حوّل": "cfg_convert",
    "قاموس_مُضبط_اضبط_مُخصّص": "configure_custom",
    "قاموس_مُضبط_امتداد_حوّل": "ext_convert",
    "قاموس_مُضبط_حلّ": "resolve",
    "قاموس_مُضبط_حوّل": "convert",
    "قاموس_مُضبط_كـ_صف": "as_tuple",
    "قاموس_مُضبط_مُستورد": "importer",
    # === multiprocessing ===
    "قاموس_وكيل_احصل": "get",
    "قاموس_وكيل_اسحب": "pop",
    "قاموس_وكيل_امسح": "clear",
    "قاموس_وكيل_انسخ": "copy",
    "قاموس_وكيل_حدّث": "update",
    "قاموس_وكيل_عناصر": "items",
    "قاموس_وكيل_قيم": "values",
    "قاموس_وكيل_مفاتيح": "keys",
    # === cmd ===
    "قبل_الأمر": "precmd",
    "قبل_الحلقة": "preloop",
    # === pydoc ===
    "قسم_كبير": "bigsection",
    # === multiprocessing ===
    "قطع": "interrupt",
    "قيمة_احصل": "get",
    "قيمة_عيّن": "set",
    "قيمة_وكيل_احصل": "get",
    "قيمة_وكيل_عيّن": "set",
    # === typing ===
    "كتابة_نص_إدخال_إخراج_أغلق": "close",
    "كتابة_نص_إدخال_إخراج_أفرغ": "flush",
    "كتابة_نص_إدخال_إخراج_اقتطع": "truncate",
    "كتابة_نص_إدخال_إخراج_اقرأ": "read",
    "كتابة_نص_إدخال_إخراج_اقرأ_الأسطر": "readlines",
    "كتابة_نص_إدخال_إخراج_اكتب": "write",
    "كتابة_نص_إدخال_إخراج_اكتب_أسطراً": "writelines",
    "كتابة_نص_إدخال_إخراج_انتقل": "seek",
    "كتابة_نص_إدخال_إخراج_رقم_الملف": "fileno",
    "كتابة_نص_إدخال_إخراج_سطر_قراءة": "readline",
    "كتابة_نص_إدخال_إخراج_ضع_الموضع": "tell",
    "كتابة_نص_إدخال_إخراج_قابل_للانتقال": "seekable",
    "كتابة_نص_إدخال_إخراج_قابل_للقراءة": "readable",
    "كتابة_نص_إدخال_إخراج_قابل_للكتابة": "writable",
    "كتابة_نص_إدخال_إخراج_هو_طرفية": "isatty",
    # === ctypes ===
    "مؤشر_محرف_عريض_من_معامل": "from_param",
    "مؤشر_محرف_من_معامل": "from_param",
    # === logging ===
    "مؤقّت_دوّار_ملف_معالج_أصدر": "emit",
    "مؤقّت_دوّار_ملف_معالج_أضف_رشّح": "addFilter",
    "مؤقّت_دوّار_ملف_معالج_أغلق": "close",
    "مؤقّت_دوّار_ملف_معالج_أفرغ": "flush",
    "مؤقّت_دوّار_ملف_معالج_أنشئ_اقفل": "createLock",
    "مؤقّت_دوّار_ملف_معالج_احذف_رشّح": "removeFilter",
    "مؤقّت_دوّار_ملف_معالج_احصل": "acquire",
    "مؤقّت_دوّار_ملف_معالج_احصل_اسم": "get_name",
    "مؤقّت_دوّار_ملف_معالج_افعل_تجاوز": "doRollover",
    "مؤقّت_دوّار_ملف_معالج_تدوير_اسم_ملف": "rotation_filename",
    "مؤقّت_دوّار_ملف_معالج_حرّر": "release",
    "مؤقّت_دوّار_ملف_معالج_دوّر": "rotate",
    "مؤقّت_دوّار_ملف_معالج_رشّح": "filter",
    "مؤقّت_دوّار_ملف_معالج_عالج": "handle",
    "مؤقّت_دوّار_ملف_معالج_عالج_خطأ": "handleError",
    "مؤقّت_دوّار_ملف_معالج_عيّن_اسم": "set_name",
    "مؤقّت_دوّار_ملف_معالج_عيّن_تدفق": "setStream",
    "مؤقّت_دوّار_ملف_معالج_عيّن_مستوى": "setLevel",
    "مؤقّت_دوّار_ملف_معالج_عيّن_مُنسّق": "setFormatter",
    "مؤقّت_دوّار_ملف_معالج_نسّق": "format",
    "مؤقّت_دوّار_ملف_معالج_ينبغي_تجاوز": "shouldRollover",
    # === pydoc ===
    "متعدد_الأعمدة": "multicolumn",
    # === multiprocessing ===
    "متعدد_معالجة_مدير_R_اقفل": "RLock",
    "متعدد_معالجة_مدير_إشارة_مرور": "Semaphore",
    "متعدد_معالجة_مدير_حاجز": "Barrier",
    "متعدد_معالجة_مدير_قابل_للانضمام_طابور": "JoinableQueue",
    "متعدد_معالجة_مدير_محدود_إشارة_مرور": "BoundedSemaphore",
    # === contextvars ===
    "متغيرات_سياق_احصل": "get",
    "متغيرات_سياق_انسخ": "copy",
    "متغيرات_سياق_عناصر": "items",
    "متغيرات_سياق_قيم": "values",
    "متغيرات_سياق_متغير_احصل": "get",
    "متغيرات_سياق_متغير_صفّر": "reset",
    "متغيرات_سياق_متغير_عيّن": "set",
    "متغيرات_سياق_مفاتيح": "keys",
    # === sched ===
    "مجدول_ألغِ": "cancel",
    "مجدول_شغّل": "run",
    "مجدول_فارغ": "empty",
    # === multiprocessing ===
    "مجموعة_MAP_نجمة": "starmap",
    "مجموعة_MAP_نجمة_غير_متزامن": "starmap_async",
    "مجموعة_imap": "imap",
    "مجموعة_imap_غير_مرتّب": "imap_unordered",
    "مجموعة_أغلق": "close",
    "مجموعة_أنهِ": "terminate",
    "مجموعة_اربط": "join",
    "مجموعة_خريطة": "map",
    "مجموعة_خريطة_غير_متزامن": "map_async",
    "مجموعة_طبّق": "apply",
    "مجموعة_طبّق_غير_متزامن": "apply_async",
    "مجموعة_عالج": "Process",
    "مجموعة_وكيل_MAP_نجمة": "starmap",
    "مجموعة_وكيل_MAP_نجمة_غير_متزامن": "starmap_async",
    "مجموعة_وكيل_imap": "imap",
    "مجموعة_وكيل_imap_غير_مرتّب": "imap_unordered",
    "مجموعة_وكيل_أغلق": "close",
    "مجموعة_وكيل_أنهِ": "terminate",
    "مجموعة_وكيل_اربط": "join",
    "مجموعة_وكيل_خريطة": "map",
    "مجموعة_وكيل_خريطة_غير_متزامن": "map_async",
    "مجموعة_وكيل_طبّق": "apply",
    "مجموعة_وكيل_طبّق_غير_متزامن": "apply_async",
    "محدود_إشارة_مرور_احصل_قيمة": "get_value",
    "محدود_إشارة_مرور_مقفل": "locked",
    # === logging ===
    "محول": "converter",
    "مرشّح_أضف_رشّح": "addFilter",
    "مرشّح_احذف_رشّح": "removeFilter",
    "مرشّح_رشّح": "filter",
    # === concurrent ===
    "مستقبل_ألغِ": "cancel",
    "مستقبل_تم": "done",
    "مستقبل_نتيجة": "result",
    # === logging ===
    "مسجّل_أضف_رشّح": "addFilter",
    "مسجّل_أضف_معالج": "addHandler",
    "مسجّل_ابحث_مُستدعية": "findCaller",
    "مسجّل_احذف_رشّح": "removeFilter",
    "مسجّل_احذف_معالج": "removeHandler",
    "مسجّل_احصل_أبناء": "getChildren",
    "مسجّل_احصل_ابن": "getChild",
    "مسجّل_احصل_فعّال_مستوى": "getEffectiveLevel",
    "مسجّل_استثناء": "exception",
    "مسجّل_استدعِ_معالجات": "callHandlers",
    "مسجّل_اعمل_سجل": "makeRecord",
    "مسجّل_تحذير": "warning",
    "مسجّل_تصحيح": "debug",
    "مسجّل_حذّر": "warn",
    "مسجّل_حرج": "critical",
    "مسجّل_خطأ": "error",
    "مسجّل_رشّح": "filter",
    "مسجّل_سجل": "log",
    "مسجّل_عالج": "handle",
    "مسجّل_عيّن_مستوى": "setLevel",
    "مسجّل_قاتل": "fatal",
    "مسجّل_له_معالجات": "hasHandlers",
    "مسجّل_معلومات": "info",
    "مسجّل_مكيّف_احصل_فعّال_مستوى": "getEffectiveLevel",
    "مسجّل_مكيّف_استثناء": "exception",
    "مسجّل_مكيّف_تحذير": "warning",
    "مسجّل_مكيّف_تصحيح": "debug",
    "مسجّل_مكيّف_حذّر": "warn",
    "مسجّل_مكيّف_حرج": "critical",
    "مسجّل_مكيّف_خطأ": "error",
    "مسجّل_مكيّف_سجل": "log",
    "مسجّل_مكيّف_عالج": "process",
    "مسجّل_مكيّف_عيّن_مستوى": "setLevel",
    "مسجّل_مكيّف_له_معالجات": "hasHandlers",
    "مسجّل_مكيّف_معلومات": "info",
    "مسجّل_مكيّف_هو_مُفعّل_لأجل": "isEnabledFor",
    "مسجّل_هو_مُفعّل_لأجل": "isEnabledFor",
    # === multiprocessing ===
    "مشترك_ذاكرة": "SharedMemory",
    "مشترك_ذاكرة_أغلق": "close",
    "مشترك_ذاكرة_خادم_أنشئ": "create",
    "مشترك_ذاكرة_خادم_أنقِص_المرجع": "decref",
    "مشترك_ذاكرة_خادم_أوقف": "shutdown",
    "مشترك_ذاكرة_خادم_احصل_دوال": "get_methods",
    "مشترك_ذاكرة_خادم_اقبل_اتصال": "accept_connection",
    "مشترك_ذاكرة_خادم_بديل_احصل_على_القيمة": "fallback_getvalue",
    "مشترك_ذاكرة_خادم_بديل_تمثيل": "fallback_repr",
    "مشترك_ذاكرة_خادم_بديل_نص": "fallback_str",
    "مشترك_ذاكرة_خادم_تصحيح_معلومات": "debug_info",
    "مشترك_ذاكرة_خادم_خدّم_عميل": "serve_client",
    "مشترك_ذاكرة_خادم_خدّم_للأبد": "serve_forever",
    "مشترك_ذاكرة_خادم_زِد_المرجع": "incref",
    "مشترك_ذاكرة_خادم_عالج_اطلب": "handle_request",
    "مشترك_ذاكرة_خادم_عدد_من_كائنات": "number_of_objects",
    "مشترك_ذاكرة_خادم_مقبل": "accepter",
    "مشترك_ذاكرة_خادم_وهمي": "dummy",
    "مشترك_ذاكرة_مدير_ابدأ": "start",
    "مشترك_ذاكرة_مدير_اتصل": "connect",
    "مشترك_ذاكرة_مدير_احصل_خادم": "get_server",
    "مشترك_ذاكرة_مدير_اربط": "join",
    "مشترك_ذاكرة_مدير_سجّل": "register",
    # === logging ===
    "معالج_أصدر": "emit",
    "معالج_أضف_رشّح": "addFilter",
    "معالج_أغلق": "close",
    "معالج_أفرغ": "flush",
    "معالج_أنشئ_اقفل": "createLock",
    "معالج_احذف_رشّح": "removeFilter",
    "معالج_احصل": "acquire",
    "معالج_احصل_اسم": "get_name",
    "معالج_حرّر": "release",
    "معالج_رشّح": "filter",
    "معالج_عالج": "handle",
    "معالج_عالج_خطأ": "handleError",
    "معالج_عيّن_اسم": "set_name",
    "معالج_عيّن_مستوى": "setLevel",
    "معالج_عيّن_مُنسّق": "setFormatter",
    "معالج_نسّق": "format",
    # === typing ===
    "معامل_مواصفة_له_افتراضي": "has_default",
    # === unittest ===
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_أدرج_موعداً_سياق": "enterContext",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_أدرج_موعداً_صنف_سياق": "enterClassContext",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_أدرج_موعداً_غير_متزامن_سياق": "enterAsyncContext",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_أضف_صنف_نظّف": "addClassCleanup",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_أضف_نظّف": "addCleanup",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_أضف_نوع_مساواة_دالة": "addTypeEqualityFunc",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_افتراضي_اختبر_نتيجة": "defaultTestResult",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_افشل": "fail",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_افعل_تنظيفات": "doCleanups",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_افعل_صنف_تنظيفات": "doClassCleanups",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_أصغر": "assertLess",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_أصغر_يساوي": "assertLessEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_أكبر": "assertGreater",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_أكبر_يساوي": "assertGreaterEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_بدايات_بـ": "assertStartsWith",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_بلا_سجلات": "assertNoLogs",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_تسلسل_يساوي": "assertSequenceEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_تعبير_نمطي": "assertRegex",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_تقريباً_يساوي": "assertAlmostEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_خطأ": "assertFalse",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_سجلات": "assertLogs",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_صحيح": "assertTrue",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_صف_يساوي": "assertTupleEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_عدّ_يساوي": "assertCountEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_عيّن_يساوي": "assertSetEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_في": "assertIn",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_قائمة_يساوي": "assertListEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_قاموس_يساوي": "assertDictEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_لا_بدايات_بـ": "assertNotStartsWith",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_لا_تعبير_نمطي": "assertNotRegex",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_لا_تقريباً_يساوي": "assertNotAlmostEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_لا_في": "assertNotIn",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_لا_له_سمة": "assertNotHasAttr",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_لا_نهايات_بـ": "assertNotEndsWith",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_لا_هو_صنف_فرعي": "assertNotIsSubclass",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_لا_هو_نسخة": "assertNotIsInstance",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_لا_يساوي": "assertNotEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_له_سمة": "assertHasAttr",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_متعدد_سطر_يساوي": "assertMultiLineEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_نهايات_بـ": "assertEndsWith",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_هو": "assertIs",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_هو_صنف_فرعي": "assertIsSubclass",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_هو_لا": "assertIsNot",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_هو_لا_شيء": "assertIsNone",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_هو_لا_لا_شيء": "assertIsNotNone",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_هو_نسخة": "assertIsInstance",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_يحذّر": "assertWarns",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_يحذّر_تعبير_نمطي": "assertWarnsRegex",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_يرفع": "assertRaises",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_يرفع_تعبير_نمطي": "assertRaisesRegex",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تأكد_يساوي": "assertEqual",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تجاوز_اختبر": "skipTest",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_تصحيح": "debug",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_شغّل": "run",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_عدّ_اختبر_حالات": "countTestCases",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_عيّن_لأعلى": "setUp",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_عيّن_لأعلى_صنف": "setUpClass",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_فرعي_اختبر": "subTest",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_قصير_وصف": "shortDescription",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_مزّق_لأسفل": "tearDown",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_مزّق_لأسفل_صنف": "tearDownClass",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_معرف": "id",
    # === unicodedata ===
    "معيار_يونيكود_ثنائي_الاتجاه": "bidirectional",
    "معيار_يونيكود_رقم": "digit",
    "معيار_يونيكود_شرق_آسيوي_عرض": "east_asian_width",
    "معيار_يونيكود_عددي": "numeric",
    "معيار_يونيكود_فئة": "category",
    "معيار_يونيكود_مُركِّب": "combining",
    "معيار_يونيكود_هو_موحّد": "is_normalized",
    # === difflib ===
    "مفرّق_قارن": "compare",
    # === concurrent ===
    "مفسّر_مجموعة_منفّذ_أرسل": "submit",
    "مفسّر_مجموعة_منفّذ_أوقف": "shutdown",
    "مفسّر_مجموعة_منفّذ_جهّز_سياق": "prepare_context",
    "مفسّر_مجموعة_منفّذ_خريطة": "map",
    # === filecmp ===
    "مقارنة_مجلدات_أبلغ": "report",
    "مقارنة_مجلدات_أبلغ_جزئي_إغلاق": "report_partial_closure",
    "مقارنة_مجلدات_أبلغ_كامل_إغلاق": "report_full_closure",
    "مقارنة_مجلدات_مرحلة0": "phase0",
    "مقارنة_مجلدات_مرحلة1": "phase1",
    "مقارنة_مجلدات_مرحلة2": "phase2",
    "مقارنة_مجلدات_مرحلة3": "phase3",
    "مقارنة_مجلدات_مرحلة4": "phase4",
    "مقارنة_مجلدات_مرحلة4_إغلاق": "phase4_closure",
    # === logging ===
    "مقبس_معالج_أرسل": "send",
    "مقبس_معالج_أصدر": "emit",
    "مقبس_معالج_أضف_رشّح": "addFilter",
    "مقبس_معالج_أغلق": "close",
    "مقبس_معالج_أفرغ": "flush",
    "مقبس_معالج_أنشئ_اقفل": "createLock",
    "مقبس_معالج_أنشئ_مقبس": "createSocket",
    "مقبس_معالج_احذف_رشّح": "removeFilter",
    "مقبس_معالج_احصل": "acquire",
    "مقبس_معالج_احصل_اسم": "get_name",
    "مقبس_معالج_اعمل_بايكن": "makePickle",
    "مقبس_معالج_اعمل_مقبس": "makeSocket",
    "مقبس_معالج_حرّر": "release",
    "مقبس_معالج_رشّح": "filter",
    "مقبس_معالج_عالج": "handle",
    "مقبس_معالج_عالج_خطأ": "handleError",
    "مقبس_معالج_عيّن_اسم": "set_name",
    "مقبس_معالج_عيّن_مستوى": "setLevel",
    "مقبس_معالج_عيّن_مُنسّق": "setFormatter",
    "مقبس_معالج_نسّق": "format",
    # === multiprocessing ===
    "مقبس_مُستمع_أغلق": "close",
    "مقبس_مُستمع_اقبل": "accept",
    # === difflib ===
    "مكتبة_الفروق_تسلسل_مطابِق_نسبة": "ratio",
    # === multiprocessing ===
    "مكرّر_وكيل_أرسل": "send",
    "مكرّر_وكيل_أغلق": "close",
    "مكرّر_وكيل_ارمِ": "throw",
    # === fileinput ===
    "ملف_إدخال_أغلق_3": "close",
    # === io ===
    "ملف_إدخال_إخراج_أغلق_2": "close",
    "ملف_إدخال_إخراج_أفرغ_2": "flush",
    "ملف_إدخال_إخراج_اقتطع_2": "truncate",
    "ملف_إدخال_إخراج_اقرأ_2": "read",
    "ملف_إدخال_إخراج_اقرأ_الأسطر": "readlines",
    "ملف_إدخال_إخراج_اقرأ_في_2": "readinto",
    "ملف_إدخال_إخراج_اقرأ_كل_2": "readall",
    "ملف_إدخال_إخراج_اكتب_2": "write",
    "ملف_إدخال_إخراج_اكتب_أسطراً_2": "writelines",
    "ملف_إدخال_إخراج_انتقل_2": "seek",
    "ملف_إدخال_إخراج_رقم_الملف_2": "fileno",
    "ملف_إدخال_إخراج_سطر_قراءة_3": "readline",
    "ملف_إدخال_إخراج_ضع_الموضع_2": "tell",
    "ملف_إدخال_إخراج_قابل_للانتقال_2": "seekable",
    "ملف_إدخال_إخراج_قابل_للقراءة_2": "readable",
    "ملف_إدخال_إخراج_قابل_للكتابة_2": "writable",
    "ملف_إدخال_إخراج_هو_طرفية_2": "isatty",
    # === fileinput ===
    "ملف_إدخال_اسم_ملف_2": "filename",
    "ملف_إدخال_الملف_التالي_2": "nextfile",
    "ملف_إدخال_رقم_السطر_3": "lineno",
    "ملف_إدخال_رقم_الملف_3": "fileno",
    "ملف_إدخال_سطر_الملف_2": "filelineno",
    "ملف_إدخال_سطر_قراءة_2": "readline",
    "ملف_إدخال_هو_إدخال_قياسي": "isstdin",
    "ملف_إدخال_هو_السطر_الأول_2": "isfirstline",
    # === logging ===
    "ملف_معالج_أصدر": "emit",
    "ملف_معالج_أضف_رشّح": "addFilter",
    "ملف_معالج_أفرغ": "flush",
    "ملف_معالج_أنشئ_اقفل": "createLock",
    "ملف_معالج_احذف_رشّح": "removeFilter",
    "ملف_معالج_احصل": "acquire",
    "ملف_معالج_احصل_اسم": "get_name",
    "ملف_معالج_حرّر": "release",
    "ملف_معالج_رشّح": "filter",
    "ملف_معالج_عالج": "handle",
    "ملف_معالج_عالج_خطأ": "handleError",
    "ملف_معالج_عيّن_اسم": "set_name",
    "ملف_معالج_عيّن_تدفق": "setStream",
    "ملف_معالج_عيّن_مستوى": "setLevel",
    "ملف_معالج_عيّن_مُنسّق": "setFormatter",
    "ملف_معالج_نسّق": "format",
    # === multiprocessing ===
    "من_مفاتيح": "fromkeys",
    # === select ===
    "من_واصف": "fromfd",
    # === concurrent ===
    "منفّذ_أرسل": "submit",
    "منفّذ_أوقف": "shutdown",
    "منفّذ_خريطة": "map",
    # === io ===
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_أغلق_2": "close",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_أفرغ_2": "flush",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_افصل_2": "detach",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اقتطع_2": "truncate",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اقرأ1_2": "read1",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اقرأ_2": "read",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اقرأ_الأسطر": "readlines",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اقرأ_في1_2": "readinto1",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اقرأ_في_2": "readinto",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اكتب_2": "write",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اكتب_أسطراً_2": "writelines",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_انتقل_2": "seek",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_رقم_الملف_2": "fileno",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_سطر_قراءة_3": "readline",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_ضع_الموضع_2": "tell",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_قابل_للانتقال_2": "seekable",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_قابل_للقراءة_2": "readable",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_قابل_للكتابة_2": "writable",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_هو_طرفية_2": "isatty",
    "مُخزّن_مؤقتاً_عشوائي_اقرأ_الأسطر": "readlines",
    "مُخزّن_مؤقتاً_قارئ_اقرأ_الأسطر": "readlines",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اقرأ_الأسطر": "readlines",
    "مُخزّن_مؤقتاً_كاتب_اقرأ_الأسطر": "readlines",
    # === logging ===
    "مُراقَب_ملف_معالج_أصدر": "emit",
    "مُراقَب_ملف_معالج_أضف_رشّح": "addFilter",
    "مُراقَب_ملف_معالج_أغلق": "close",
    "مُراقَب_ملف_معالج_أفرغ": "flush",
    "مُراقَب_ملف_معالج_أنشئ_اقفل": "createLock",
    "مُراقَب_ملف_معالج_احذف_رشّح": "removeFilter",
    "مُراقَب_ملف_معالج_احصل": "acquire",
    "مُراقَب_ملف_معالج_احصل_اسم": "get_name",
    "مُراقَب_ملف_معالج_حرّر": "release",
    "مُراقَب_ملف_معالج_رشّح": "filter",
    "مُراقَب_ملف_معالج_عالج": "handle",
    "مُراقَب_ملف_معالج_عالج_خطأ": "handleError",
    "مُراقَب_ملف_معالج_عيّن_اسم": "set_name",
    "مُراقَب_ملف_معالج_عيّن_تدفق": "setStream",
    "مُراقَب_ملف_معالج_عيّن_مستوى": "setLevel",
    "مُراقَب_ملف_معالج_عيّن_مُنسّق": "setFormatter",
    "مُراقَب_ملف_معالج_نسّق": "format",
    # === pydoc ===
    "مُساعد_قائمة": "list",
    "مُساعد_مساعدة": "help",
    "مُساعد_مقدمة": "intro",
    # === multiprocessing ===
    "مُستمع_أغلق": "close",
    "مُستمع_اقبل": "accept",
    # === rlcompleter ===
    "مُكمل_أكمل": "complete",
    # === concurrent ===
    "مُلغى": "cancelled",
    # === selectors ===
    "مُنتخِب_ABC_وصفي_سجّل": "register",
    # === logging ===
    "مُنسّق_نسّق": "format",
    "مُنسّق_يستخدم_وقت": "usesTime",
    "نسبة_مئوية_نمط_تحقق": "validate",
    "نسبة_مئوية_نمط_نسّق": "format",
    "نسبة_مئوية_نمط_يستخدم_وقت": "usesTime",
    "نسّق_تذييل": "formatFooter",
    "نسّق_رأس": "formatHeader",
    "نسّق_رسالة": "formatMessage",
    # === pydoc ===
    "نسّق_مسبقاً": "preformat",
    # === logging ===
    "نسّق_مكدس": "formatStack",
    "نسّق_وقت": "formatTime",
    # === io ===
    "نص_إدخال_إخراج_أساس_أغلق_2": "close",
    "نص_إدخال_إخراج_أساس_أفرغ_2": "flush",
    "نص_إدخال_إخراج_أساس_افصل_2": "detach",
    "نص_إدخال_إخراج_أساس_اقتطع_2": "truncate",
    "نص_إدخال_إخراج_أساس_اقرأ_2": "read",
    "نص_إدخال_إخراج_أساس_اقرأ_الأسطر": "readlines",
    "نص_إدخال_إخراج_أساس_اكتب_2": "write",
    "نص_إدخال_إخراج_أساس_اكتب_أسطراً_2": "writelines",
    "نص_إدخال_إخراج_أساس_انتقل_2": "seek",
    "نص_إدخال_إخراج_أساس_رقم_الملف_2": "fileno",
    "نص_إدخال_إخراج_أساس_سطر_قراءة_3": "readline",
    "نص_إدخال_إخراج_أساس_ضع_الموضع_2": "tell",
    "نص_إدخال_إخراج_أساس_قابل_للانتقال_2": "seekable",
    "نص_إدخال_إخراج_أساس_قابل_للقراءة_2": "readable",
    "نص_إدخال_إخراج_أساس_قابل_للكتابة_2": "writable",
    "نص_إدخال_إخراج_أساس_هو_طرفية_2": "isatty",
    # === shlex ===
    "نص_إدخال_إخراج_اقرأ_الأسطر": "readlines",
    # === io ===
    "نص_إدخال_إخراج_غلاف_أعد_الضبط": "reconfigure",
    "نص_إدخال_إخراج_غلاف_أغلق_2": "close",
    "نص_إدخال_إخراج_غلاف_أفرغ_2": "flush",
    "نص_إدخال_إخراج_غلاف_افصل_2": "detach",
    "نص_إدخال_إخراج_غلاف_اقتطع_2": "truncate",
    "نص_إدخال_إخراج_غلاف_اقرأ_2": "read",
    "نص_إدخال_إخراج_غلاف_اقرأ_الأسطر": "readlines",
    "نص_إدخال_إخراج_غلاف_اكتب_2": "write",
    "نص_إدخال_إخراج_غلاف_اكتب_أسطراً_2": "writelines",
    "نص_إدخال_إخراج_غلاف_انتقل_2": "seek",
    "نص_إدخال_إخراج_غلاف_رقم_الملف_2": "fileno",
    "نص_إدخال_إخراج_غلاف_سطر_قراءة_3": "readline",
    "نص_إدخال_إخراج_غلاف_ضع_الموضع_2": "tell",
    "نص_إدخال_إخراج_غلاف_قابل_للانتقال_2": "seekable",
    "نص_إدخال_إخراج_غلاف_قابل_للقراءة_2": "readable",
    "نص_إدخال_إخراج_غلاف_قابل_للكتابة_2": "writable",
    "نص_إدخال_إخراج_غلاف_هو_طرفية_2": "isatty",
    # === unittest ===
    "نص_اختبر_مُشغّل_شغّل": "run",
    "نص_اختبر_نتيجة_أضف_تجاوز": "addSkip",
    "نص_اختبر_نتيجة_أضف_خطأ": "addError",
    "نص_اختبر_نتيجة_أضف_غير_متوقع_نجاح": "addUnexpectedSuccess",
    "نص_اختبر_نتيجة_أضف_فرعي_اختبر": "addSubTest",
    "نص_اختبر_نتيجة_أضف_فشل": "addFailure",
    "نص_اختبر_نتيجة_أضف_متوقع_فشل": "addExpectedFailure",
    "نص_اختبر_نتيجة_أضف_مدة": "addDuration",
    "نص_اختبر_نتيجة_أضف_نجاح": "addSuccess",
    "نص_اختبر_نتيجة_أوقف": "stop",
    "نص_اختبر_نتيجة_أوقف_اختبر": "stopTest",
    "نص_اختبر_نتيجة_أوقف_اختبر_شغّل": "stopTestRun",
    "نص_اختبر_نتيجة_ابدأ_اختبر": "startTest",
    "نص_اختبر_نتيجة_ابدأ_اختبر_شغّل": "startTestRun",
    "نص_اختبر_نتيجة_اطبع_أخطاء": "printErrors",
    "نص_اختبر_نتيجة_كان_ناجح": "wasSuccessful",
    # === pydoc ===
    "نص_تمثيل_تمثيل": "repr",
    "نص_تمثيل_تمثيل1": "repr1",
    "نص_تمثيل_تمثيل_صف": "repr_tuple",
    "نص_تمثيل_تمثيل_طابور_مزدوج": "repr_deque",
    "نص_تمثيل_تمثيل_عدد_صحيح": "repr_int",
    "نص_تمثيل_تمثيل_عيّن": "repr_set",
    "نص_تمثيل_تمثيل_قائمة": "repr_list",
    "نص_تمثيل_تمثيل_قاموس": "repr_dict",
    "نص_تمثيل_تمثيل_مجموعة_مجمّدة": "repr_frozenset",
    "نص_تمثيل_تمثيل_مصفوفة": "repr_array",
    "نص_تمثيل_تمثيل_نسخة": "repr_instance",
    "نص_تمثيل_تمثيل_نص": "repr_str",
    "نص_توثيق_احصل_على_مكان_التوثيق": "getdocloc",
    "نص_توثيق_افشل": "fail",
    "نص_توثيق_تمثيل": "repr",
    "نص_توثيق_توثيق_الدالة": "docroutine",
    "نص_توثيق_قسم": "section",
    "نص_توثيق_مسافة_بادئة": "indent",
    "نص_توثيق_مستند": "document",
    "نص_توثيق_نسّق_الشجرة": "formattree",
    "نص_توثيق_نسّق_القيمة": "formatvalue",
    "نص_توثيق_وثّق_البيانات": "docdata",
    "نص_توثيق_وثّق_الخاصية": "docproperty",
    "نص_توثيق_وثّق_الصنف": "docclass",
    "نص_توثيق_وثّق_الوحدة": "docmodule",
    "نص_توثيق_وثّق_غيره": "docother",
    # === logging ===
    "نص_قالب_نمط_تحقق": "validate",
    "نص_قالب_نمط_نسّق": "format",
    "نص_قالب_نمط_يستخدم_وقت": "usesTime",
    "نص_نسّق_نمط_تحقق": "validate",
    "نص_نسّق_نمط_نسّق": "format",
    "نص_نسّق_نمط_يستخدم_وقت": "usesTime",
    # === mmap ===
    "نصيحة": "madvise",
    # === logging ===
    "نظام_سجل_معالج_أصدر": "emit",
    "نظام_سجل_معالج_أضف_رشّح": "addFilter",
    "نظام_سجل_معالج_أغلق": "close",
    "نظام_سجل_معالج_أفرغ": "flush",
    "نظام_سجل_معالج_أنشئ_اقفل": "createLock",
    "نظام_سجل_معالج_أنشئ_مقبس": "createSocket",
    "نظام_سجل_معالج_احذف_رشّح": "removeFilter",
    "نظام_سجل_معالج_احصل": "acquire",
    "نظام_سجل_معالج_احصل_اسم": "get_name",
    "نظام_سجل_معالج_حرّر": "release",
    "نظام_سجل_معالج_رشّح": "filter",
    "نظام_سجل_معالج_عالج": "handle",
    "نظام_سجل_معالج_عالج_خطأ": "handleError",
    "نظام_سجل_معالج_عيّن_اسم": "set_name",
    "نظام_سجل_معالج_عيّن_مستوى": "setLevel",
    "نظام_سجل_معالج_عيّن_مُنسّق": "setFormatter",
    "نظام_سجل_معالج_نسّق": "format",
    # === typing ===
    "نوع_متغير_صف_له_افتراضي": "has_default",
    "نوع_متغير_له_افتراضي": "has_default",
    # === multiprocessing ===
    "هو_حيّ": "is_alive",
    "هو_مجموعة_جزئية": "issubset",
    "هو_مجموعة_شاملة": "issuperset",
    "هو_منفصل": "isdisjoint",
    # === pydoc ===
    "وحدة_ماسح_شغّل": "run",
    "وصلة_الصنف": "classlink",
    # === unittest ===
    "وهمي_اربط_وهمي": "attach_mock",
    "وهمي_اضبط_وهمي": "configure_mock",
    "وهمي_تأكد_أي_استدعِ": "assert_any_call",
    "وهمي_تأكد_لا_مُستدعى": "assert_not_called",
    "وهمي_تأكد_له_استدعاءات": "assert_has_calls",
    "وهمي_تأكد_مُستدعى": "assert_called",
    "وهمي_تأكد_مُستدعى_بـ": "assert_called_with",
    "وهمي_تأكد_مُستدعى_مرة_واحدة": "assert_called_once",
    "وهمي_تأكد_مُستدعى_مرة_واحدة_بـ": "assert_called_once_with",
    "وهمي_صفّر_وهمي": "reset_mock",
    "وهمي_وهمي_أضف_مواصفة": "mock_add_spec",
    # === concurrent ===
    "يشتغل": "running",
}


SYS_PROPS = {
    # خصائص الأصناف
    # === platform ===
    "API_مستوى": "api_level",
    # === ctypes ===
    "CX": "cx",
    "CY": "cy",
    "C_بايت_غير_سالب_قيمة": "value",
    "C_بايت_قيمة": "value",
    "C_حجم_T_قيمة": "value",
    "C_حرف_P_قيمة": "value",
    "C_حرف_قيمة": "value",
    "C_حقل_إزاحة": "offset",
    "C_حقل_اسم": "name",
    "C_حقل_حجم": "size",
    "C_حقل_نوع": "type",
    "C_صحيح16_غير_سالب_قيمة": "value",
    "C_صحيح16_قيمة": "value",
    "C_صحيح64_قيمة": "value",
    "C_صحيح_غير_سالب_قيمة": "value",
    "C_عائم_قيمة": "value",
    "C_عائم_مركّب_قيمة": "value",
    "C_عائم_مضاعف_قيمة": "value",
    "C_عائم_مضاعف_مركّب_قيمة": "value",
    "C_عدد_صحيح_قيمة": "value",
    "C_فارغ_P_قيمة": "value",
    "C_محرف_عريض_P_قيمة": "value",
    "C_محرف_عريض_قيمة": "value",
    "C_مزدوج_قيمة": "value",
    "C_مزدوج_مركّب_قيمة": "value",
    "C_منطقي_قيمة": "value",
    "DW_عالٍ_تاريخ_وقت": "dwHighDateTime",
    "DW_منخفض_تاريخ_وقت": "dwLowDateTime",
    # === pydoc ===
    "HTML_توثيق_توثيق_بايثون": "PYTHONDOCS",
    # === logging ===
    "HTTP_معالج_اسم": "name",
    # === ctypes ===
    "H_نافذة": "hWnd",
    # === dataclasses ===
    "KW_فقط": "kw_only",
    # === ctypes ===
    "LPBOOL_محتويات": "contents",
    "LPBYTE_محتويات": "contents",
    "LPCOLORREF_محتويات": "contents",
    "LPFILETIME_محتويات": "contents",
    "LPHANDLE_محتويات": "contents",
    "LPINT_محتويات": "contents",
    "LPMSG_محتويات": "contents",
    "LPPOINT_محتويات": "contents",
    "LPRECT_محتويات": "contents",
    "LPSIZE_محتويات": "contents",
    "LPUINT_محتويات": "contents",
    "LPWIN_32_ابحث_بيانات_a_محتويات": "contents",
    "LPWIN_32_ابحث_بيانات_w_محتويات": "contents",
    "LPWORD_محتويات": "contents",
    "L_معامل": "lParam",
    # === logging ===
    "NT_حدث_سجل_معالج_اسم": "name",
    # === multiprocessing ===
    "N_بانتظار": "n_waiting",
    "PID": "pid",
    # === ctypes ===
    "PT": "pt",
    "PY_كائن_قيمة": "value",
    # === resource ===
    "RU_IXRSS": "ru_ixrss",
    "RU_OUBLOCK": "ru_oublock",
    "RU_isrss": "ru_isrss",
    "RU_nivcsw": "ru_nivcsw",
    "RU_nswap": "ru_nswap",
    "RU_nvcsw": "ru_nvcsw",
    "RU_أرسل_رسالة": "ru_msgsnd",
    "RU_أقصى_ذاكرة_محجوزة": "ru_maxrss",
    "RU_استقبل_رسالة": "ru_msgrcv",
    "RU_خطأ_صغير": "ru_minflt",
    "RU_خطأ_كبير": "ru_majflt",
    "RU_ذاكرة_محجوزة": "ru_idrss",
    "RU_عدد_الإشارات": "ru_nsignals",
    "RU_في_الكتلة": "ru_inblock",
    "RU_وقت_الاستخدام": "ru_utime",
    "RU_وقت_النظام": "ru_stime",
    # === signal ===
    "SI_PID": "si_pid",
    "SI_UID": "si_uid",
    "SI_حالة": "si_status",
    "SI_حزم": "si_band",
    "SI_رقم_الإشارة": "si_signo",
    "SI_رقم_الخطأ": "si_errno",
    "SI_كود": "si_code",
    # === logging ===
    "SMTP_معالج_اسم": "name",
    # === ctypes ===
    "W_معامل": "wParam",
    "X": "x",
    # === multiprocessing ===
    "XML_مُستمع_أخير_مقبول": "last_accepted",
    "XML_مُستمع_عنوان": "address",
    # === ctypes ===
    "Y": "y",
    # === logging ===
    "أساس_دوّار_معالج_اسم": "name",
    "أساس_دوّار_معالج_دوّار": "rotator",
    "أساس_دوّار_معالج_مُسمّي": "namer",
    "أساس_دوّار_معالج_مُنهِي": "terminator",
    # === multiprocessing ===
    "أساس_مدير_عنوان": "address",
    # === logging ===
    "أساس_مُضبط_حوّل_نمط": "CONVERT_PATTERN",
    "أساس_مُضبط_رقم_نمط": "DIGIT_PATTERN",
    "أساس_مُضبط_فهرس_نمط": "INDEX_PATTERN",
    "أساس_مُضبط_قيمة_محولات": "value_converters",
    "أساس_مُضبط_كلمة_نمط": "WORD_PATTERN",
    "أساس_مُضبط_نقطة_نمط": "DOT_PATTERN",
    "أضف_ذيلياً_NUL": "append_nul",
    # === multiprocessing ===
    "أطراف": "parties",
    # === numbers ===
    "أعداد_حقيقي_جزء_تخيلي": "imag",
    "أعداد_حقيقي_حقيقي": "real",
    "أعداد_صحيح_بسط": "numerator",
    "أعداد_صحيح_جزء_تخيلي": "imag",
    "أعداد_صحيح_حقيقي": "real",
    "أعداد_صحيح_مقام": "denominator",
    "أعداد_مركّب_جزء_تخيلي": "imag",
    "أعداد_مركّب_حقيقي": "real",
    "أعداد_نسبي_بسط": "numerator",
    "أعداد_نسبي_جزء_تخيلي": "imag",
    "أعداد_نسبي_حقيقي": "real",
    "أعداد_نسبي_مقام": "denominator",
    # === cmd ===
    "أمر_مقدمة": "intro",
    # === platform ===
    "أندرويد_إصدار_جهاز": "device",
    "أندرويد_إصدار_حرّر": "release",
    "أندرويد_إصدار_نموذج": "model",
    "أندرويد_إصدار_هو_مُحاكٍ": "is_emulator",
    # === sched ===
    "أولوية": "priority",
    # === logging ===
    "أولوية_أسماء": "priority_names",
    "أولوية_خريطة": "priority_map",
    # === select ===
    "إبول_مغلق": "closed",
    # === sched ===
    "إجراء": "action",
    # === pydoc ===
    "إخراج": "output",
    # === io ===
    "إدخال_إخراج_أساس_مغلق_2": "closed",
    # === platform ===
    "إدخال_إخراج_إصدار_معلومات_حرّر": "release",
    "إدخال_إخراج_إصدار_معلومات_نظام": "system",
    "إدخال_إخراج_إصدار_معلومات_نموذج": "model",
    "إدخال_إخراج_إصدار_معلومات_هو_مُحاكٍ": "is_simulator",
    # === typing ===
    "إدخال_إخراج_اسم": "name",
    "إدخال_إخراج_مغلق": "closed",
    # === io ===
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_اسم": "name",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_خام": "raw",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_مغلق": "closed",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_وضع": "mode",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_اسم": "name",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_خام": "raw",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_مغلق": "closed",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_وضع": "mode",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_مغلق": "closed",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_اسم": "name",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_خام": "raw",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_مغلق": "closed",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_وضع": "mode",
    # === typing ===
    "إدخال_إخراج_وضع": "mode",
    # === multiprocessing ===
    "ابتدائي": "INITIAL",
    # === dataclasses ===
    "ابدأ_تهيئة_متغير_نوع": "type",
    # === multiprocessing ===
    "اتصال_قابل_للقراءة": "readable",
    "اتصال_قابل_للكتابة": "writable",
    "اتصال_مغلق": "closed",
    # === getopt ===
    "احصل_على_الخيارات_خطأ_خيار": "opt",
    "احصل_على_الخيارات_خطأ_رسالة": "msg",
    # === unittest ===
    "اختبر_برنامج_اختبر_اسم_أنماط": "testNamePatterns",
    "اختبر_برنامج_فشل_سريع": "failfast",
    "اختبر_برنامج_مخزن_مؤقت": "buffer",
    "اختبر_حالة_أقصى_فرق": "maxDiff",
    "اختبر_حالة_طويل_رسالة": "longMessage",
    "اختبر_حالة_فشل_استثناء": "failureException",
    "اختبر_دالة_بادئة": "testMethodPrefix",
    "اختبر_محمّل_اختبر_اسم_أنماط": "testNamePatterns",
    # === multiprocessing ===
    "اخرج_كود": "exitcode",
    # === cmd ===
    "استخدم_إدخال_خام": "use_rawinput",
    # === platform ===
    "اسم_النظام_نتيجة_إصدار": "version",
    "اسم_النظام_نتيجة_جهاز": "machine",
    "اسم_النظام_نتيجة_حرّر": "release",
    "اسم_النظام_نتيجة_عُقدة": "node",
    "اسم_النظام_نتيجة_نظام": "system",
    # === dataclasses ===
    "افتراضي_مصنع": "default_factory",
    # === logging ===
    "افتراضي_ملي_ثانية_نسّق": "default_msec_format",
    "افتراضي_وقت_نسّق": "default_time_format",
    # === cmd ===
    "الأمر_الأخير": "lastcmd",
    # === unittest ===
    "التقط_الفاصلة": "catchbreak",
    # === ctypes ===
    "بايت_إزاحة": "byte_offset",
    "بايت_حجم": "byte_size",
    # === io ===
    "بايتات_إدخال_إخراج_مغلق_2": "closed",
    # === ctypes ===
    "بت_إزاحة": "bit_offset",
    "بت_حجم": "bit_size",
    # === multiprocessing ===
    "بدأ": "STARTED",
    # === unittest ===
    "برنامج_اسم": "progName",
    # === cmd ===
    "بلا_مساعدة": "nohelp",
    # === resource ===
    "بنية_استخدام_N_تسلسل_حقول": "n_sequence_fields",
    "بنية_استخدام_N_حقول": "n_fields",
    "بنية_استخدام_N_غير_مسمّى_حقول": "n_unnamed_fields",
    # === signal ===
    "بنية_معلومات_الإشارة_N_تسلسل_حقول": "n_sequence_fields",
    "بنية_معلومات_الإشارة_N_حقول": "n_fields",
    "بنية_معلومات_الإشارة_N_غير_مسمّى_حقول": "n_unnamed_fields",
    # === unittest ===
    "تحذيرات": "warnings",
    # === shlex ===
    "تحليل_كلمات_نص_إدخال_إخراج_أخطاء": "errors",
    "تحليل_كلمات_نص_إدخال_إخراج_ترميز": "encoding",
    "تحليل_كلمات_نص_إدخال_إخراج_سطر_تخزين_مؤقت": "line_buffering",
    "تحليل_كلمات_نص_إدخال_إخراج_مغلق": "closed",
    # === logging ===
    "تخزين_مؤقت_معالج_اسم": "name",
    "تدفق_معالج_اسم": "name",
    "تدفق_معالج_مُنهِي": "terminator",
    # === unittest ===
    "ترابط_مزيج_افتراضي_مهلة": "DEFAULT_TIMEOUT",
    "ترابط_وهمي_أرجع_قيمة": "return_value",
    "ترابط_وهمي_استدعِ_عدّ": "call_count",
    "ترابط_وهمي_استدعِ_معطيات": "call_args",
    "ترابط_وهمي_استدعِ_معطيات_قائمة": "call_args_list",
    "ترابط_وهمي_افتراضي_مهلة": "DEFAULT_TIMEOUT",
    "ترابط_وهمي_جانب_تأثير": "side_effect",
    "ترابط_وهمي_مُستدعى": "called",
    "ترابط_وهمي_وهمي_استدعاءات": "mock_calls",
    # === shlex ===
    "ترقيم_أحرف": "punctuation_chars",
    # === io ===
    "تصاعدي_سطر_جديد_مفكّك_أسطر_جديدة": "newlines",
    # === multiprocessing ===
    "تصديق_مفتاح": "authkey",
    # === enum ===
    "تعداد_عضو": "member",
    # === unittest ===
    "تفصيل": "verbosity",
    # === logging ===
    "تنسيق_مواصفة": "fmt_spec",
    # === pydoc ===
    "توثيق_توثيق_بايثون": "PYTHONDOCS",
    # === cmd ===
    "توثيق_رأس": "doc_header",
    "توثيق_زعيم": "doc_leader",
    # === typing ===
    "ثنائي_إدخال_إخراج_اسم": "name",
    "ثنائي_إدخال_إخراج_مغلق": "closed",
    "ثنائي_إدخال_إخراج_وضع": "mode",
    # === logging ===
    "جذر_مسجّل_جذر": "root",
    "جذر_مسجّل_مدير": "manager",
    # === multiprocessing ===
    "حاجز_وكيل_مكسور": "broken",
    "حارس": "sentinel",
    "حالة_أوقف": "SHUTDOWN",
    "حالة_قيمة": "value",
    # === sched ===
    "حدث_حجة": "argument",
    "حدث_وسائط_مفتاحية": "kwargs",
    "حدث_وقت": "time",
    # === logging ===
    "حزمة_بيانات_معالج_اسم": "name",
    # === unittest ===
    "حزمة_صنف": "suiteClass",
    # === dataclasses ===
    "حقل_ابدأ_تهيئة": "init",
    "حقل_اسم": "name",
    "حقل_افتراضي": "default",
    "حقل_بيانات_وصفية": "metadata",
    "حقل_تجزئة": "hash",
    "حقل_تمثيل": "repr",
    "حقل_توثيق": "doc",
    "حقل_قارن": "compare",
    # === logging ===
    "حقل_مواصفة": "field_spec",
    # === dataclasses ===
    "حقل_نوع": "type",
    # === unittest ===
    "حلقة_مصنع": "loop_factory",
    # === multiprocessing ===
    "خادم_بديل_خريطة": "fallback_mapping",
    "خادم_خلفي": "daemon",
    "خادم_عام": "public",
    # === io ===
    "خام_إدخال_إخراج_أساس_مغلق_2": "closed",
    # === filecmp ===
    "خريطة_الدوال": "methodmap",
    # === concurrent ===
    "خيط_مجموعة_منفّذ_مكسور": "BROKEN",
    # === unittest ===
    "دالة_اختبر_حالة_أقصى_فرق": "maxDiff",
    "دالة_اختبر_حالة_طويل_رسالة": "longMessage",
    "دالة_اختبر_حالة_فشل_استثناء": "failureException",
    # === logging ===
    "دوّار_ملف_معالج_اسم": "name",
    "دوّار_ملف_معالج_دوّار": "rotator",
    "دوّار_ملف_معالج_مُسمّي": "namer",
    "دوّار_ملف_معالج_مُنهِي": "terminator",
    "ذاكرة_معالج_اسم": "name",
    # === mmap ===
    "ذاكرة_مُخزَّنة_مغلق": "closed",
    # === ctypes ===
    "رسالة_رسالة": "message",
    "رسالة_وقت": "time",
    # === multiprocessing ===
    "رمز_عنوان": "address",
    # === contextvars ===
    "رمز_قديم_قيمة": "old_value",
    "رمز_متغير": "var",
    # === multiprocessing ===
    "رمز_معرف": "id",
    # === pydoc ===
    "رموز": "symbols",
    # === multiprocessing ===
    "زامن_مدير_عنوان": "address",
    # === logging ===
    "سجل_FTP": "LOG_FTP",
    "سجل_NTP": "LOG_NTP",
    "سجل_solcron": "LOG_SOLCRON",
    "سجل_أخبار": "LOG_NEWS",
    "سجل_أمان": "LOG_SECURITY",
    "سجل_بريد": "LOG_MAIL",
    "سجل_تصديق": "LOG_AUTH",
    "سجل_تصريف_خاص": "LOG_AUTHPRIV",
    "سجل_تنبيه": "LOG_ALERT",
    "سجل_خادم_خلفي": "LOG_DAEMON",
    "سجل_سجل_النظام": "LOG_SYSLOG",
    "سجل_طابعة": "LOG_LPR",
    "سجل_طارئ": "LOG_EMERG",
    "سجل_لوحة_مفاتيح": "LOG_CONSOLE",
    "سجل_مجدول": "LOG_CRON",
    "سجل_محلي_0": "LOG_LOCAL0",
    "سجل_محلي_1": "LOG_LOCAL1",
    "سجل_محلي_2": "LOG_LOCAL2",
    "سجل_محلي_3": "LOG_LOCAL3",
    "سجل_محلي_4": "LOG_LOCAL4",
    "سجل_محلي_5": "LOG_LOCAL5",
    "سجل_محلي_6": "LOG_LOCAL6",
    "سجل_محلي_7": "LOG_LOCAL7",
    "سجل_مستخدم": "LOG_USER",
    "سجل_ملاحظة": "LOG_NOTICE",
    "سجل_نواة": "LOG_KERN",
    "سجل_يو_يو_سي_بي": "LOG_UUCP",
    # === unittest ===
    "سحري_وهمي_أرجع_قيمة": "return_value",
    "سحري_وهمي_استدعِ_عدّ": "call_count",
    "سحري_وهمي_استدعِ_معطيات": "call_args",
    "سحري_وهمي_استدعِ_معطيات_قائمة": "call_args_list",
    "سحري_وهمي_جانب_تأثير": "side_effect",
    "سحري_وهمي_مُستدعى": "called",
    "سحري_وهمي_وهمي_استدعاءات": "mock_calls",
    "سمة_صنف_وهمي_أرجع_قيمة": "return_value",
    "سمة_صنف_وهمي_استدعِ_عدّ": "call_count",
    "سمة_صنف_وهمي_استدعِ_معطيات": "call_args",
    "سمة_صنف_وهمي_استدعِ_معطيات_قائمة": "call_args_list",
    "سمة_صنف_وهمي_جانب_تأثير": "side_effect",
    "سمة_صنف_وهمي_مُستدعى": "called",
    "سمة_صنف_وهمي_وهمي_استدعاءات": "mock_calls",
    # === contextvars ===
    "سياق_متغيرات_رمز_ناقص": "MISSING",
    # === ctypes ===
    "صغير_مستطيل_أسفل": "Bottom",
    "صغير_مستطيل_أعلى": "Top",
    "صغير_مستطيل_يسار": "Left",
    "صغير_مستطيل_يمين": "Right",
    # === unittest ===
    "صنف_النتيجة": "resultclass",
    # === difflib ===
    "طابق_B": "b",
    "طابق_أ": "a",
    # === logging ===
    "طابور_معالج_اسم": "name",
    # === multiprocessing ===
    "عالج_اسم": "name",
    "عالج_معرّف": "ident",
    # === logging ===
    "عدم_معالج_اسم": "name",
    # === unittest ===
    "غير_قابل_للاستدعاء_سحري_وهمي_أرجع_قيمة": "return_value",
    "غير_قابل_للاستدعاء_سحري_وهمي_استدعِ_عدّ": "call_count",
    "غير_قابل_للاستدعاء_سحري_وهمي_استدعِ_معطيات": "call_args",
    "غير_قابل_للاستدعاء_سحري_وهمي_استدعِ_معطيات_قائمة": "call_args_list",
    "غير_قابل_للاستدعاء_سحري_وهمي_جانب_تأثير": "side_effect",
    "غير_قابل_للاستدعاء_سحري_وهمي_مُستدعى": "called",
    "غير_قابل_للاستدعاء_سحري_وهمي_وهمي_استدعاءات": "mock_calls",
    "غير_قابل_للاستدعاء_وهمي_أرجع_قيمة": "return_value",
    "غير_قابل_للاستدعاء_وهمي_استدعِ_عدّ": "call_count",
    "غير_قابل_للاستدعاء_وهمي_استدعِ_معطيات": "call_args",
    "غير_قابل_للاستدعاء_وهمي_استدعِ_معطيات_قائمة": "call_args_list",
    "غير_قابل_للاستدعاء_وهمي_جانب_تأثير": "side_effect",
    "غير_قابل_للاستدعاء_وهمي_مُستدعى": "called",
    "غير_قابل_للاستدعاء_وهمي_وهمي_استدعاءات": "mock_calls",
    "غير_متزامن_وهمي_أرجع_قيمة": "return_value",
    "غير_متزامن_وهمي_استدعِ_عدّ": "call_count",
    "غير_متزامن_وهمي_استدعِ_معطيات": "call_args",
    "غير_متزامن_وهمي_استدعِ_معطيات_قائمة": "call_args_list",
    "غير_متزامن_وهمي_انتظر_عدّ": "await_count",
    "غير_متزامن_وهمي_انتظر_معطيات": "await_args",
    "غير_متزامن_وهمي_انتظر_معطيات_قائمة": "await_args_list",
    "غير_متزامن_وهمي_جانب_تأثير": "side_effect",
    "غير_متزامن_وهمي_مزيج_انتظر_عدّ": "await_count",
    "غير_متزامن_وهمي_مزيج_انتظر_معطيات": "await_args",
    "غير_متزامن_وهمي_مزيج_انتظر_معطيات_قائمة": "await_args_list",
    "غير_متزامن_وهمي_مُستدعى": "called",
    "غير_متزامن_وهمي_وهمي_استدعاءات": "mock_calls",
    # === cmd ===
    "غير_موثّق_رأس": "undoc_header",
    # === unittest ===
    "فاصل1": "separator1",
    "فاصل2": "separator2",
    # === multiprocessing ===
    "قابل_للمشاركة_قائمة_نسّق": "format",
    # === logging ===
    "قاموس_مُضبط_حوّل_نمط": "CONVERT_PATTERN",
    "قاموس_مُضبط_رقم_نمط": "DIGIT_PATTERN",
    "قاموس_مُضبط_فهرس_نمط": "INDEX_PATTERN",
    "قاموس_مُضبط_قيمة_محولات": "value_converters",
    "قاموس_مُضبط_كلمة_نمط": "WORD_PATTERN",
    "قاموس_مُضبط_نقطة_نمط": "DOT_PATTERN",
    # === multiprocessing ===
    "قيمة_قيمة": "value",
    "قيمة_وكيل_قيمة": "value",
    # === typing ===
    "قيّم_قيمة": "evaluate_value",
    "قيّم_قيود": "evaluate_constraints",
    "قيّم_مقيّد": "evaluate_bound",
    "كتابة_نص_إدخال_إخراج_أخطاء": "errors",
    "كتابة_نص_إدخال_إخراج_أسطر_جديدة": "newlines",
    "كتابة_نص_إدخال_إخراج_ترميز": "encoding",
    "كتابة_نص_إدخال_إخراج_سطر_تخزين_مؤقت": "line_buffering",
    "كتابة_نص_إدخال_إخراج_مغلق": "closed",
    # === ctypes ===
    "مؤشر_صغير_مستطيل_محتويات": "contents",
    "مؤشر_عائم_محتويات": "contents",
    "مؤشر_قصير_محتويات": "contents",
    "مؤشر_محرف_عريض_محتويات": "contents",
    "مؤشر_محرف_محتويات": "contents",
    # === logging ===
    "مؤقّت_دوّار_ملف_معالج_اسم": "name",
    "مؤقّت_دوّار_ملف_معالج_دوّار": "rotator",
    "مؤقّت_دوّار_ملف_معالج_مُسمّي": "namer",
    "مؤقّت_دوّار_ملف_معالج_مُنهِي": "terminator",
    # === ctypes ===
    "متغير_منطقي_قيمة": "value",
    # === contextvars ===
    "متغيرات_سياق_متغير_اسم": "name",
    # === cmd ===
    "متفرقات_رأس": "misc_header",
    # === sched ===
    "مجدول_تسلسل": "sequence",
    "مجدول_طابور": "queue",
    # === cmd ===
    "محارف_المعرّف": "identchars",
    # === multiprocessing ===
    "مخزن": "buf",
    # === logging ===
    "مدير_عطّل": "disable",
    "مرفق_أسماء": "facility_names",
    # === ctypes ===
    "مستطيل_أسفل": "bottom",
    "مستطيل_أعلى": "top",
    "مستطيل_يسار": "left",
    "مستطيل_يمين": "right",
    # === logging ===
    "مسجّل_جذر": "root",
    "مسجّل_مدير": "manager",
    "مسجّل_مكيّف_اسم": "name",
    "مسجّل_مكيّف_مدير": "manager",
    # === cmd ===
    "مسطرة": "ruler",
    # === multiprocessing ===
    "مشترك_ذاكرة_اسم": "name",
    "مشترك_ذاكرة_حجم": "size",
    "مشترك_ذاكرة_خادم_بديل_خريطة": "fallback_mapping",
    "مشترك_ذاكرة_خادم_عام": "public",
    "مشترك_ذاكرة_مدير_عنوان": "address",
    # === cmd ===
    "مطالبة": "prompt",
    # === logging ===
    "معالج_اسم": "name",
    # === typing ===
    "معامل_مواصفة_قيّم_افتراضي": "evaluate_default",
    "معامل_مواصفة_وسائط_مفتاحية": "kwargs",
    # === multiprocessing ===
    "معرف_النوع": "typeid",
    # === unittest ===
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_أقصى_فرق": "maxDiff",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_طويل_رسالة": "longMessage",
    "معزول_غير_متزامن_إدخال_إخراج_اختبر_حالة_فشل_استثناء": "failureException",
    # === typing ===
    "معطيات": "args",
    # === unicodedata ===
    "معيار_يونيكود_بيانات_يونيكود_إصدار": "unidata_version",
    # === concurrent ===
    "مفسّر_مجموعة_منفّذ_مكسور": "BROKEN",
    # === logging ===
    "مقبس_معالج_اسم": "name",
    # === difflib ===
    "مكتبة_الفروق_طابق_حجم": "size",
    # === io ===
    "ملف_إدخال_إخراج_أغلق_الملف": "closefd",
    "ملف_إدخال_إخراج_مغلق_2": "closed",
    "ملف_إدخال_إخراج_وضع_2": "mode",
    # === logging ===
    "ملف_معالج_اسم": "name",
    "ملف_معالج_مُنهِي": "terminator",
    # === pydoc ===
    "موضوعات": "topics",
    # === io ===
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_مغلق_2": "closed",
    # === logging ===
    "مُراقَب_ملف_معالج_اسم": "name",
    "مُراقَب_ملف_معالج_مُنهِي": "terminator",
    # === pydoc ===
    "مُساعد_إدخال": "input",
    "مُساعد_كلمات_مفتاحية": "keywords",
    # === multiprocessing ===
    "مُستمع_أخير_مقبول": "last_accepted",
    "مُستمع_عنوان": "address",
    # === platform ===
    "مُصنِّع": "manufacturer",
    # === selectors ===
    "مُنتخِب_مفتاح_أحداث": "events",
    "مُنتخِب_مفتاح_بيانات": "data",
    "مُنتخِب_مفتاح_كائن_ملف": "fileobj",
    # === logging ===
    "نسبة_مئوية_نمط_افتراضي_نسّق": "default_format",
    "نسبة_مئوية_نمط_تاريخ_نصي_ابحث": "asctime_search",
    "نسبة_مئوية_نمط_تاريخ_نصي_نسّق": "asctime_format",
    "نسبة_مئوية_نمط_تحقق_نمط": "validation_pattern",
    # === io ===
    "نص_إدخال_إخراج_أساس_أخطاء_2": "errors",
    "نص_إدخال_إخراج_أساس_أسطر_جديدة": "newlines",
    "نص_إدخال_إخراج_أساس_ترميز_2": "encoding",
    "نص_إدخال_إخراج_أساس_مغلق_2": "closed",
    # === shlex ===
    "نص_إدخال_إخراج_أسطر_جديدة": "newlines",
    # === typing ===
    "نص_إدخال_إخراج_اسم": "name",
    # === io ===
    "نص_إدخال_إخراج_غلاف_أخطاء_2": "errors",
    "نص_إدخال_إخراج_غلاف_أسطر_جديدة": "newlines",
    "نص_إدخال_إخراج_غلاف_اسم_2": "name",
    "نص_إدخال_إخراج_غلاف_اكتب_عبر": "write_through",
    "نص_إدخال_إخراج_غلاف_ترميز_2": "encoding",
    "نص_إدخال_إخراج_غلاف_سطر_تخزين_مؤقت_2": "line_buffering",
    "نص_إدخال_إخراج_غلاف_مخزن_مؤقت": "buffer",
    "نص_إدخال_إخراج_غلاف_مغلق_2": "closed",
    # === typing ===
    "نص_إدخال_إخراج_مخزن_مؤقت": "buffer",
    "نص_إدخال_إخراج_وضع": "mode",
    # === pydoc ===
    "نص_توثيق_توثيق_بايثون": "PYTHONDOCS",
    # === logging ===
    "نص_قالب_نمط_افتراضي_نسّق": "default_format",
    "نص_قالب_نمط_تاريخ_نصي_ابحث": "asctime_search",
    "نص_قالب_نمط_تاريخ_نصي_نسّق": "asctime_format",
    "نص_قالب_نمط_تحقق_نمط": "validation_pattern",
    "نص_نسّق_نمط_افتراضي_نسّق": "default_format",
    "نص_نسّق_نمط_تاريخ_نصي_ابحث": "asctime_search",
    "نص_نسّق_نمط_تاريخ_نصي_نسّق": "asctime_format",
    "نص_نسّق_نمط_تحقق_نمط": "validation_pattern",
    "نظام_سجل_معالج_اسم": "name",
    "نظام_سجل_معالج_سجل_تحذير": "LOG_WARNING",
    "نظام_سجل_معالج_سجل_تصحيح": "LOG_DEBUG",
    "نظام_سجل_معالج_سجل_حرج": "LOG_CRIT",
    "نظام_سجل_معالج_سجل_خطأ": "LOG_ERR",
    "نظام_سجل_معالج_سجل_معلومات": "LOG_INFO",
    "نظام_سجل_معالج_معرّف": "ident",
    # === typing ===
    "نوع_متغير_صف_قيّم_افتراضي": "evaluate_default",
    "نوع_متغير_قيّم_افتراضي": "evaluate_default",
    # === ctypes ===
    "هو_حقل_بت": "is_bitfield",
    "هو_مجهول": "is_anonymous",
    # === selectors ===
    "واصف_ملف": "fd",
    # === unittest ===
    "وحدة": "module",
    # === pkgutil ===
    "وحدة_باحث": "module_finder",
    "وحدة_معلومات_اسم": "name",
    "وحدة_معلومات_هو_حزمة": "ispkg",
    # === unittest ===
    "وهمي_أرجع_قيمة": "return_value",
    "وهمي_استدعِ_عدّ": "call_count",
    "وهمي_استدعِ_معطيات": "call_args",
    "وهمي_استدعِ_معطيات_قائمة": "call_args_list",
    "وهمي_جانب_تأثير": "side_effect",
    "وهمي_مُستدعى": "called",
    "وهمي_وهمي_استدعاءات": "mock_calls",
    # === ctypes ===
    "ويندوز_32_ابحث_بيانات_a_C_بديل_ملف_اسم": "cAlternateFileName",
    "ويندوز_32_ابحث_بيانات_a_C_ملف_اسم": "cFileName",
    "ويندوز_32_ابحث_بيانات_a_DW_محجوز0": "dwReserved0",
    "ويندوز_32_ابحث_بيانات_a_DW_محجوز1": "dwReserved1",
    "ويندوز_32_ابحث_بيانات_a_DW_ملف_سمات": "dwFileAttributes",
    "ويندوز_32_ابحث_بيانات_a_FT_أخير_اكتب_وقت": "ftLastWriteTime",
    "ويندوز_32_ابحث_بيانات_a_FT_أخير_وصول_وقت": "ftLastAccessTime",
    "ويندوز_32_ابحث_بيانات_a_FT_إنشاء_وقت": "ftCreationTime",
    "ويندوز_32_ابحث_بيانات_a_N_ملف_حجم_عالٍ": "nFileSizeHigh",
    "ويندوز_32_ابحث_بيانات_a_N_ملف_حجم_منخفض": "nFileSizeLow",
    "ويندوز_32_ابحث_بيانات_w_C_بديل_ملف_اسم": "cAlternateFileName",
    "ويندوز_32_ابحث_بيانات_w_C_ملف_اسم": "cFileName",
    "ويندوز_32_ابحث_بيانات_w_DW_محجوز0": "dwReserved0",
    "ويندوز_32_ابحث_بيانات_w_DW_محجوز1": "dwReserved1",
    "ويندوز_32_ابحث_بيانات_w_DW_ملف_سمات": "dwFileAttributes",
    "ويندوز_32_ابحث_بيانات_w_FT_أخير_اكتب_وقت": "ftLastWriteTime",
    "ويندوز_32_ابحث_بيانات_w_FT_أخير_وصول_وقت": "ftLastAccessTime",
    "ويندوز_32_ابحث_بيانات_w_FT_إنشاء_وقت": "ftCreationTime",
    "ويندوز_32_ابحث_بيانات_w_N_ملف_حجم_عالٍ": "nFileSizeHigh",
    "ويندوز_32_ابحث_بيانات_w_N_ملف_حجم_منخفض": "nFileSizeLow",
}


SYS_CONSTS = {
    # ثوابت تُكتب عارية
    # === tty ===
    "B_0": "tty.B0",
    "B_1": "tty.BS1",
    "B_1000000": "tty.B1000000",
    "B_110": "tty.B110",
    "B_115200": "tty.B115200",
    "B_1152000": "tty.B1152000",
    "B_1200": "tty.B1200",
    "B_134": "tty.B134",
    "B_150": "tty.B150",
    "B_1500000": "tty.B1500000",
    "B_1800": "tty.B1800",
    "B_19200": "tty.B19200",
    "B_200": "tty.B200",
    "B_2000000": "tty.B2000000",
    "B_230400": "tty.B230400",
    "B_2400": "tty.B2400",
    "B_2500000": "tty.B2500000",
    "B_300": "tty.B300",
    "B_3000000": "tty.B3000000",
    "B_3500000": "tty.B3500000",
    "B_38400": "tty.B38400",
    "B_4000000": "tty.B4000000",
    "B_460800": "tty.B460800",
    "B_4800": "tty.B4800",
    "B_50": "tty.B50",
    "B_500000": "tty.B500000",
    "B_57600": "tty.B57600",
    "B_576000": "tty.B576000",
    "B_600": "tty.B600",
    "B_75": "tty.B75",
    "B_921600": "tty.B921600",
    "B_9600": "tty.B9600",
    "CR_0": "tty.CR0",
    "CR_1": "tty.CR1",
    "CR_2": "tty.CR2",
    "CR_3": "tty.CR3",
    "C_5": "tty.CS5",
    "C_6": "tty.CS6",
    "C_7": "tty.CS7",
    "C_8": "tty.CS8",
    # === fcntl ===
    "DN_أعد_التسمية": "fcntl.DN_RENAME",
    "DN_أنشئ": "fcntl.DN_CREATE",
    "DN_احذف": "fcntl.DN_DELETE",
    "DN_سمة": "fcntl.DN_ATTRIB",
    "DN_عدّل": "fcntl.DN_MODIFY",
    "DN_متعدد_الطلقات": "fcntl.DN_MULTISHOT",
    "DN_وصول": "fcntl.DN_ACCESS",
    # === ctypes ===
    "Dll_بايثون": "ctypes.pydll",
    # === errno ===
    "EL_2_nsync": "errno.EL2NSYNC",
    "EL_2_أوقف_النقرة": "errno.EL2HLT",
    "EL_3_RST": "errno.EL3RST",
    "EL_3_أوقف_النقرة": "errno.EL3HLT",
    # === fcntl ===
    "FASYNC": "fcntl.FASYNC",
    # === tty ===
    "FF_0": "tty.FF0",
    "FF_1": "tty.FF1",
    # === fcntl ===
    "F_EXLCK": "fcntl.F_EXLCK",
    "F_RDLCK": "fcntl.F_RDLCK",
    "F_SHLCK": "fcntl.F_SHLCK",
    "F_UNLCK": "fcntl.F_UNLCK",
    "F_WRLCK": "fcntl.F_WRLCK",
    "F_احصل_على_الأعلام": "fcntl.F_GETFL",
    "F_احصل_على_الأنبوب_حجم": "fcntl.F_GETPIPE_SZ",
    "F_احصل_على_الإشارة": "fcntl.F_GETSIG",
    "F_احصل_على_الإيجار": "fcntl.F_GETLEASE",
    "F_احصل_على_القفل": "fcntl.F_GETLK",
    "F_احصل_على_القفل_64": "fcntl.F_GETLK64",
    "F_احصل_على_المالك": "fcntl.F_GETOWN",
    "F_احصل_على_المالك_EX": "fcntl.F_GETOWN_EX",
    "F_احصل_على_الواصف": "fcntl.F_GETFD",
    "F_المالك_PID": "fcntl.F_OWNER_PID",
    "F_المالك_مجموعة_العمليات": "fcntl.F_OWNER_PGRP",
    "F_المالك_معرف_الخيط": "fcntl.F_OWNER_TID",
    "F_عيّن_الأعلام": "fcntl.F_SETFL",
    "F_عيّن_الأنبوب_حجم": "fcntl.F_SETPIPE_SZ",
    "F_عيّن_الإشارة": "fcntl.F_SETSIG",
    "F_عيّن_الإيجار": "fcntl.F_SETLEASE",
    "F_عيّن_القفل": "fcntl.F_SETLK",
    "F_عيّن_القفل_64": "fcntl.F_SETLK64",
    "F_عيّن_القفل_وانتظر": "fcntl.F_SETLKW",
    "F_عيّن_القفل_وانتظر_64": "fcntl.F_SETLKW64",
    "F_عيّن_المالك": "fcntl.F_SETOWN",
    "F_عيّن_المالك_EX": "fcntl.F_SETOWN_EX",
    "F_عيّن_الواصف": "fcntl.F_SETFD",
    "F_كرّر_الواصف": "fcntl.F_DUPFD",
    "F_كرّر_الواصف_أغلق_عند_التنفيذ": "fcntl.F_DUPFD_CLOEXEC",
    "F_نبّه": "fcntl.F_NOTIFY",
    # === pydoc ===
    "HTML": "pydoc.html",
    # === typing ===
    "KT": "typing.KT",
    # === mmap ===
    "MADV_احذف": "mmap.MADV_REMOVE",
    "MADV_افعل_التفرع": "mmap.MADV_DOFORK",
    "MADV_افعل_التفريغ": "mmap.MADV_DODUMP",
    "MADV_بلا_صفحة_ضخمة": "mmap.MADV_NOHUGEPAGE",
    "MADV_تسلسلي": "mmap.MADV_SEQUENTIAL",
    "MADV_تسميم_аппаратي": "mmap.MADV_HWPOISON",
    "MADV_سيحتاج": "mmap.MADV_WILLNEED",
    "MADV_صفحة_ضخمة": "mmap.MADV_HUGEPAGE",
    "MADV_عادي": "mmap.MADV_NORMAL",
    "MADV_عشوائي": "mmap.MADV_RANDOM",
    "MADV_غير_قابل_للدمج": "mmap.MADV_UNMERGEABLE",
    "MADV_قابل_للدمج": "mmap.MADV_MERGEABLE",
    "MADV_لا_تتفرّع": "mmap.MADV_DONTFORK",
    "MADV_لا_تحتاج": "mmap.MADV_DONTNEED",
    "MADV_لا_تفرّغ": "mmap.MADV_DONTDUMP",
    # === tty ===
    "NL_0": "tty.NL0",
    "NL_1": "tty.NL1",
    "N_ppp": "tty.N_PPP",
    "N_slip": "tty.N_SLIP",
    "N_جرّد": "tty.N_STRIP",
    "N_طرفية": "tty.N_TTY",
    "N_فأرة": "tty.N_MOUSE",
    # === ctypes ===
    "RTLD_شامل": "ctypes.RTLD_GLOBAL",
    "RTLD_محلي": "ctypes.RTLD_LOCAL",
    # === signal ===
    "SIG_CLD": "signal.SIGCLD",
    "SIG_IOT": "signal.SIGIOT",
    "SIG_POLL": "signal.SIGPOLL",
    # === stat ===
    "ST_UID": "stat.ST_UID",
    "ST_inode": "stat.ST_INO",
    "ST_جهاز": "stat.ST_DEV",
    "ST_وضع": "stat.ST_MODE",
    "S_IRWXG": "stat.S_IRWXG",
    "S_IRWXU": "stat.S_IRWXU",
    "S_iexec": "stat.S_IEXEC",
    "S_ifdoor": "stat.S_IFDOOR",
    "S_ifport": "stat.S_IFPORT",
    "S_ifwht": "stat.S_IFWHT",
    "S_iread": "stat.S_IREAD",
    "S_irgrp": "stat.S_IRGRP",
    "S_iroth": "stat.S_IROTH",
    "S_irusr": "stat.S_IRUSR",
    "S_irwxo": "stat.S_IRWXO",
    "S_iwgrp": "stat.S_IWGRP",
    "S_iwoth": "stat.S_IWOTH",
    "S_iwrite": "stat.S_IWRITE",
    "S_iwusr": "stat.S_IWUSR",
    "S_ixgrp": "stat.S_IXGRP",
    "S_ixoth": "stat.S_IXOTH",
    "S_ixusr": "stat.S_IXUSR",
    "S_غير_مُنسّق": "stat.S_ENFMT",
    "S_نوع_أنبوب": "stat.S_IFIFO",
    "S_نوع_جهاز_حرفي": "stat.S_IFCHR",
    "S_نوع_جهاز_كتلي": "stat.S_IFBLK",
    "S_نوع_رابط_صلب": "stat.S_IFLNK",
    "S_نوع_مجلد": "stat.S_IFDIR",
    "S_نوع_مقبس": "stat.S_IFSOCK",
    "S_نوع_ملف_عادي": "stat.S_IFREG",
    "S_هو_معرف_المجموعة": "stat.S_ISGID",
    "S_هو_معرف_المستخدم": "stat.S_ISUID",
    "S_هو_ناقل": "stat.S_ISVTX",
    # === typing ===
    "T": "typing.T",
    # === tty ===
    "TIOCM_CD": "tty.TIOCM_CD",
    "TIOCM_DSR": "tty.TIOCM_DSR",
    "TIOCM_DTR": "tty.TIOCM_DTR",
    "TIOCM_LE": "tty.TIOCM_LE",
    "TIOCM_RI": "tty.TIOCM_RI",
    "TIOCM_RNG": "tty.TIOCM_RNG",
    "TIOCM_RTS": "tty.TIOCM_RTS",
    "TIOCM_SR": "tty.TIOCM_SR",
    "TIOCM_ST": "tty.TIOCM_ST",
    "TIOCM_ct": "tty.TIOCM_CTS",
    "TIOCM_ناقل": "tty.TIOCM_CAR",
    "TIOC_CONS": "tty.TIOCCONS",
    "TIOC_EXCL": "tty.TIOCEXCL",
    "TIOC_GETD": "tty.TIOCGETD",
    "TIOC_GICOUNT": "tty.TIOCGICOUNT",
    "TIOC_GLCKTRMIOS": "tty.TIOCGLCKTRMIOS",
    "TIOC_GPGRP": "tty.TIOCGPGRP",
    "TIOC_GSERIAL": "tty.TIOCGSERIAL",
    "TIOC_GSOFTCAR": "tty.TIOCGSOFTCAR",
    "TIOC_GWINSZ": "tty.TIOCGWINSZ",
    "TIOC_INQ": "tty.TIOCINQ",
    "TIOC_LINUX": "tty.TIOCLINUX",
    "TIOC_MBIC": "tty.TIOCMBIC",
    "TIOC_MBIS": "tty.TIOCMBIS",
    "TIOC_MGET": "tty.TIOCMGET",
    "TIOC_MIWAIT": "tty.TIOCMIWAIT",
    "TIOC_MSET": "tty.TIOCMSET",
    "TIOC_NOTTY": "tty.TIOCNOTTY",
    "TIOC_NXCL": "tty.TIOCNXCL",
    "TIOC_OUTQ": "tty.TIOCOUTQ",
    "TIOC_PKT": "tty.TIOCPKT",
    "TIOC_PKT_أفرغ_اقرأ": "tty.TIOCPKT_FLUSHREAD",
    "TIOC_PKT_أفرغ_اكتب": "tty.TIOCPKT_FLUSHWRITE",
    "TIOC_PKT_أوقف": "tty.TIOCPKT_DOSTOP",
    "TIOC_PKT_ابدأ": "tty.TIOCPKT_START",
    "TIOC_PKT_بلا_إيقاف": "tty.TIOCPKT_NOSTOP",
    "TIOC_PKT_بيانات": "tty.TIOCPKT_DATA",
    "TIOC_SCTTY": "tty.TIOCSCTTY",
    "TIOC_SERCONFIG": "tty.TIOCSERCONFIG",
    "TIOC_SERGETLSR": "tty.TIOCSERGETLSR",
    "TIOC_SERGETMULTI": "tty.TIOCSERGETMULTI",
    "TIOC_SERGSTRUCT": "tty.TIOCSERGSTRUCT",
    "TIOC_SERGWILD": "tty.TIOCSERGWILD",
    "TIOC_SERSETMULTI": "tty.TIOCSERSETMULTI",
    "TIOC_SERSWILD": "tty.TIOCSERSWILD",
    "TIOC_SER_TEMT": "tty.TIOCSER_TEMT",
    "TIOC_SETD": "tty.TIOCSETD",
    "TIOC_SLCKTRMIOS": "tty.TIOCSLCKTRMIOS",
    "TIOC_SPGRP": "tty.TIOCSPGRP",
    "TIOC_SSERIAL": "tty.TIOCSSERIAL",
    "TIOC_SSOFTCAR": "tty.TIOCSSOFTCAR",
    "TIOC_STI": "tty.TIOCSTI",
    "TIOC_SWINSZ": "tty.TIOCSWINSZ",
    # === typing ===
    "T_استدعاء_مشترك": "typing.T_co",
    "T_عكس": "typing.T_contra",
    # === stat ===
    "UF_أضف_ذيلياً": "stat.UF_APPEND",
    "UF_بلا_تفريغ": "stat.UF_NODUMP",
    "UF_بلا_رابط": "stat.UF_NOUNLINK",
    "UF_خزنة_بيانات": "stat.UF_DATAVAULT",
    "UF_غير_قابل_للتعديل": "stat.UF_IMMUTABLE",
    "UF_مضغوط": "stat.UF_COMPRESSED",
    "UF_معتم": "stat.UF_OPAQUE",
    "UF_مُتتبَّع": "stat.UF_TRACKED",
    # === tty ===
    "VEOL": "tty.VEOL",
    "VEOL_2": "tty.VEOL2",
    # === typing ===
    "VT": "typing.VT",
    # === tty ===
    "VT_0": "tty.VT0",
    "VT_1": "tty.VT1",
    # === typing ===
    "VT_استدعاء_مشترك": "typing.VT_co",
    "V_استدعاء_مشترك": "typing.V_co",
    # === tty ===
    "cc": "tty.CC",
    # === typing ===
    "ct_استدعاء_مشترك": "typing.CT_co",
    # === errno ===
    "e_2_كبير": "errno.E2BIG",
    # === select ===
    "pollmsg": "select.POLLMSG",
    "pollrdhup": "select.POLLRDHUP",
    "pollwrband": "select.POLLWRBAND",
    # === enum ===
    "أبقِ": "enum.KEEP",
    # === errno ===
    "أبناء_كثيرون": "errno.ECHILD",
    # === logging ===
    "أخير_أعد_الترتيب": "logging.lastResort",
    # === signal ===
    "أدنى_إشارة_حقيقية": "signal.SIGRTMIN",
    # === tty ===
    "أرسل_فاصلة": "tty.TCSBRK",
    "أرسل_فاصلة_طويلة": "tty.TCSBRKP",
    # === logging ===
    "أساسي_نسّق": "logging.BASIC_FORMAT",
    # === errno ===
    "أعد_البدء": "errno.ERESTART",
    # === tty ===
    "أعلام_الإخراج": "tty.OFLAG",
    "أعلام_الإدخال": "tty.IFLAG",
    "أعلام_التحكم": "tty.CFLAG",
    "أعلام_محلية": "tty.LFLAG",
    "أفرغ_الآن": "tty.TCSANOW",
    "أفرغ_الإخراج": "tty.FLUSHO",
    "أفرغ_الإدخال": "tty.TCIFLUSH",
    "أفرغ_الإدخال_كله": "tty.TCIOFLUSH",
    "أفرغ_الطرفية": "tty.TCFLSH",
    "أفرغ_كل": "tty.CFLUSH",
    "أفرغ_كل_وانتظر": "tty.TCSAFLUSH",
    # === signal ===
    "أقصى_إشارة_حقيقية": "signal.SIGRTMAX",
    # === tty ===
    "أقصى_جرس": "tty.IMAXBEL",
    # === ctypes ===
    "أقصى_مسار": "ctypes.wintypes.MAX_PATH",
    # === signal ===
    "أقنعة_الإشارات_إشارة_احجب": "signal.Sigmasks.SIG_BLOCK",
    "أقنعة_الإشارات_إشارة_افتح_الحجز": "signal.Sigmasks.SIG_UNBLOCK",
    "أقنعة_الإشارات_إشارة_عيّن_القناع": "signal.Sigmasks.SIG_SETMASK",
    # === cmd ===
    "أمر_محارف_المعرّف": "cmd.IDENTCHARS",
    "أمر_مطالبة": "cmd.PROMPT",
    # === select ===
    "أنبوب_مخزن": "select.PIPE_BUF",
    # === errno ===
    "أنبوب_مكسور": "errno.EPIPE",
    # === tty ===
    "أوقف_الإخراج": "tty.TCOOFF",
    "أوقف_الإدخال": "tty.TCIOFF",
    "أوقف_الانسياب": "tty.IXOFF",
    "أوقف_الخرج": "tty.TOSTOP",
    # === concurrent ===
    "أول_اكتمل": "concurrent.futures.FIRST_COMPLETED",
    # === select ===
    "أولوية_إبول": "select.EPOLLPRI",
    "أولوية_استطلاع": "select.POLLPRI",
    # === typing ===
    "أي_نص": "typing.AnyStr",
    # === errno ===
    "أُلغِي": "errno.ECANCELED",
    # === select ===
    "إبول_أغلق_عند_التنفيذ": "select.EPOLL_CLOEXEC",
    "إبول_في": "select.EPOLLIN",
    # === stat ===
    "إحصاء_ملف_SF_أضف_ذيلياً": "stat.SF_APPEND",
    "إحصاء_ملف_SF_بلا_بيانات": "stat.SF_DATALESS",
    "إحصاء_ملف_SF_بلا_رابط": "stat.SF_NOUNLINK",
    "إحصاء_ملف_SF_رابط_نير": "stat.SF_FIRMLINK",
    "إحصاء_ملف_SF_غير_قابل_للتعديل": "stat.SF_IMMUTABLE",
    "إحصاء_ملف_SF_قابل_للتعيين": "stat.SF_SETTABLE",
    "إحصاء_ملف_SF_لقطة": "stat.SF_SNAPSHOT",
    "إحصاء_ملف_SF_مؤرشَف": "stat.SF_ARCHIVED",
    "إحصاء_ملف_SF_مقيّد": "stat.SF_RESTRICTED",
    "إحصاء_ملف_ST_GID": "stat.ST_GID",
    "إحصاء_ملف_ST_حجم": "stat.ST_SIZE",
    "إحصاء_ملف_ST_عدد_الروابط": "stat.ST_NLINK",
    "إحصاء_ملف_ST_وقت_الإنشاء": "stat.ST_CTIME",
    "إحصاء_ملف_ST_وقت_التعديل": "stat.ST_MTIME",
    "إحصاء_ملف_ST_وقت_الوصول": "stat.ST_ATIME",
    "إحصاء_ملف_UF_قابل_للتعيين": "stat.UF_SETTABLE",
    "إحصاء_ملف_UF_مخفي": "stat.UF_HIDDEN",
    "إحصاء_ملف_سمة_أرشيف": "stat.FILE_ATTRIBUTE_ARCHIVE",
    "إحصاء_ملف_سمة_إعادة_تحليل_نقطة": "stat.FILE_ATTRIBUTE_REPARSE_POINT",
    "إحصاء_ملف_سمة_افتراضي": "stat.FILE_ATTRIBUTE_VIRTUAL",
    "إحصاء_ملف_سمة_بلا_امسح_الزيادة_بيانات": "stat.FILE_ATTRIBUTE_NO_SCRUB_DATA",
    "إحصاء_ملف_سمة_جهاز": "stat.FILE_ATTRIBUTE_DEVICE",
    "إحصاء_ملف_سمة_دون_اتصال": "stat.FILE_ATTRIBUTE_OFFLINE",
    "إحصاء_ملف_سمة_سلامة_تدفق": "stat.FILE_ATTRIBUTE_INTEGRITY_STREAM",
    "إحصاء_ملف_سمة_عادي": "stat.FILE_ATTRIBUTE_NORMAL",
    "إحصاء_ملف_سمة_لا_محتوى_مُفهرس": "stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED",
    "إحصاء_ملف_سمة_مؤقت": "stat.FILE_ATTRIBUTE_TEMPORARY",
    "إحصاء_ملف_سمة_متفرّق_ملف": "stat.FILE_ATTRIBUTE_SPARSE_FILE",
    "إحصاء_ملف_سمة_مجلد": "stat.FILE_ATTRIBUTE_DIRECTORY",
    "إحصاء_ملف_سمة_مشفّر": "stat.FILE_ATTRIBUTE_ENCRYPTED",
    "إحصاء_ملف_سمة_مضغوط": "stat.FILE_ATTRIBUTE_COMPRESSED",
    "إحصاء_ملف_سمة_نظام": "stat.FILE_ATTRIBUTE_SYSTEM",
    # === select ===
    "إخراج_استطلاع": "select.POLLOUT",
    # === pty ===
    "إخراج_قياسي_رقم_الملف": "pty.STDOUT_FILENO",
    # === unittest ===
    "إخراج_قياسي_سطر": "unittest.result.STDOUT_LINE",
    # === io ===
    "إدخال_إخراج_افتراضي_مخزن_مؤقت_حجم": "io.DEFAULT_BUFFER_SIZE",
    "إدخال_إخراج_انتقل_أنهِ": "io.SEEK_END",
    "إدخال_إخراج_انتقل_حالي": "io.SEEK_CUR",
    "إدخال_إخراج_انتقل_عيّن": "io.SEEK_SET",
    # === select ===
    "إدخال_استطلاع": "select.POLLIN",
    # === tty ===
    "إدخال_غير_حاجب": "tty.FIONBIO",
    "إدخال_غير_متزامن": "tty.FIOASYNC",
    # === pty ===
    "إدخال_قياسي_رقم_الملف": "pty.STDIN_FILENO",
    # === signal ===
    "إشارات_أدنى_إشارة_حقيقية": "signal.Signals.SIGRTMIN",
    "إشارات_أقصى_إشارة_حقيقية": "signal.Signals.SIGRTMAX",
    "إشارات_إشارة_إيقاف_طرفية": "signal.Signals.SIGTSTP",
    "إشارات_إشارة_الأمر_غير_القانوني": "signal.Signals.SIGILL",
    "إشارات_إشارة_الأنبوب": "signal.Signals.SIGPIPE",
    "إشارات_إشارة_الإجهاض": "signal.Signals.SIGABRT",
    "إشارات_إشارة_الإدخال": "signal.Signals.SIGIO",
    "إشارات_إشارة_الإنهاء": "signal.Signals.SIGTERM",
    "إشارات_إشارة_الإيقاف": "signal.Signals.SIGSTOP",
    "إشارات_إشارة_الابن": "signal.Signals.SIGCHLD",
    "إشارات_إشارة_الاستئناف": "signal.Signals.SIGCONT",
    "إشارات_إشارة_الاستعجال": "signal.Signals.SIGURG",
    "إشارات_إشارة_التجزئة": "signal.Signals.SIGSEGV",
    "إشارات_إشارة_التحليل": "signal.Signals.SIGPROF",
    "إشارات_إشارة_التعليق": "signal.Signals.SIGHUP",
    "إشارات_إشارة_الخروج": "signal.Signals.SIGQUIT",
    "إشارات_إشارة_الطاقة": "signal.Signals.SIGPWR",
    "إشارات_إشارة_العائم": "signal.Signals.SIGFPE",
    "إشارات_إشارة_الفخ": "signal.Signals.SIGTRAP",
    "إشارات_إشارة_القتل": "signal.Signals.SIGKILL",
    "إشارات_إشارة_المستخدم_1": "signal.Signals.SIGUSR1",
    "إشارات_إشارة_المستخدم_2": "signal.Signals.SIGUSR2",
    "إشارات_إشارة_المقاطعة": "signal.Signals.SIGINT",
    "إشارات_إشارة_المكدس": "signal.Signals.SIGSTKFLT",
    "إشارات_إشارة_المنبّه": "signal.Signals.SIGALRM",
    "إشارات_إشارة_المنبّه_الافتراضي": "signal.Signals.SIGVTALRM",
    "إشارات_إشارة_الناقل": "signal.Signals.SIGBUS",
    "إشارات_إشارة_النظام": "signal.Signals.SIGSYS",
    "إشارات_إشارة_تغيير_النافذة": "signal.Signals.SIGWINCH",
    "إشارات_إشارة_حجم_الملف": "signal.Signals.SIGXFSZ",
    "إشارات_إشارة_قراءة_طرفية": "signal.Signals.SIGTTIN",
    "إشارات_إشارة_كتابة_طرفية": "signal.Signals.SIGTTOU",
    "إشارات_إشارة_وقت_المعالج": "signal.Signals.SIGXCPU",
    "إشارة_إيقاف_طرفية": "signal.SIGTSTP",
    "إشارة_احجب": "signal.SIG_BLOCK",
    "إشارة_افتح_الحجز": "signal.SIG_UNBLOCK",
    "إشارة_افتراضي": "signal.SIG_DFL",
    "إشارة_الأمر_غير_القانوني": "signal.SIGILL",
    "إشارة_الأنبوب": "signal.SIGPIPE",
    "إشارة_الإجهاض": "signal.SIGABRT",
    "إشارة_الإدخال": "signal.SIGIO",
    "إشارة_الإنهاء": "signal.SIGTERM",
    "إشارة_الإيقاف": "signal.SIGSTOP",
    "إشارة_الابن": "signal.SIGCHLD",
    "إشارة_الاستئناف": "signal.SIGCONT",
    "إشارة_الاستعجال": "signal.SIGURG",
    "إشارة_التجزئة": "signal.SIGSEGV",
    "إشارة_التحليل": "signal.SIGPROF",
    "إشارة_التعليق": "signal.SIGHUP",
    "إشارة_الخروج": "signal.SIGQUIT",
    "إشارة_الطاقة": "signal.SIGPWR",
    "إشارة_العائم": "signal.SIGFPE",
    "إشارة_الفخ": "signal.SIGTRAP",
    "إشارة_القتل": "signal.SIGKILL",
    "إشارة_المستخدم_1": "signal.SIGUSR1",
    "إشارة_المستخدم_2": "signal.SIGUSR2",
    "إشارة_المقاطعة": "signal.SIGINT",
    "إشارة_المكدس": "signal.SIGSTKFLT",
    "إشارة_المنبّه": "signal.SIGALRM",
    "إشارة_المنبّه_الافتراضي": "signal.SIGVTALRM",
    "إشارة_الناقل": "signal.SIGBUS",
    "إشارة_النظام": "signal.SIGSYS",
    "إشارة_تجاهل": "signal.SIG_IGN",
    "إشارة_تغيير_النافذة": "signal.SIGWINCH",
    "إشارة_حجم_الملف": "signal.SIGXFSZ",
    "إشارة_عيّن_القناع": "signal.SIG_SETMASK",
    "إشارة_قراءة_طرفية": "signal.SIGTTIN",
    "إشارة_كتابة_طرفية": "signal.SIGTTOU",
    # === multiprocessing ===
    "إشارة_مرور_قيمة_أقصى": "multiprocessing.synchronize.SEM_VALUE_MAX",
    # === signal ===
    "إشارة_وقت_المعالج": "signal.SIGXCPU",
    # === tty ===
    "إعادة_الطباعة": "tty.CRPRNT",
    # === errno ===
    "إعلان_خطأ": "errno.EADV",
    # === select ===
    "إيقاظ_إبول": "select.EPOLLWAKEUP",
    # === tty ===
    "إيقاف_ثنائي": "tty.CSTOPB",
    # === pty ===
    "ابن": "pty.CHILD",
    # === multiprocessing ===
    "اتصال_مهلة": "multiprocessing.connection.CONNECTION_TIMEOUT",
    # === tty ===
    "احصل_على_السمات": "tty.TCGETS",
    "احصل_على_كل": "tty.TCGETA",
    # === unittest ===
    "اختبارات_وحدة_وهمي_أي": "unittest.mock.ANY",
    "اختبارات_وحدة_وهمي_افتراضي": "unittest.mock.DEFAULT",
    "اختبارات_وحدة_وهمي_حارس": "unittest.mock.sentinel",
    # === logging ===
    "ارفع_استثناءات": "logging.raiseExceptions",
    # === tty ===
    "استثناء_الإدخال": "tty.FIOCLEX",
    "استثناء_غير_حاجب": "tty.FIONCLEX",
    # === resource ===
    "استخدام_أبناء": "resource.RUSAGE_CHILDREN",
    "استخدام_خيط": "resource.RUSAGE_THREAD",
    "استخدام_ذات": "resource.RUSAGE_SELF",
    # === unittest ===
    "استدعِ": "unittest.mock.call",
    # === select ===
    "استطلاع_عدم_صلاحية": "select.POLLNVAL",
    "استطلع_خطأ": "select.POLLERR",
    # === fcntl ===
    "استنساخ_ملف": "fcntl.FICLONE",
    "استنساخ_نطاق": "fcntl.FICLONERANGE",
    # === logging ===
    "افتراضي_HTTP_تسجيل_منفذ": "logging.handlers.DEFAULT_HTTP_LOGGING_PORT",
    "افتراضي_TCP_تسجيل_منفذ": "logging.handlers.DEFAULT_TCP_LOGGING_PORT",
    "افتراضي_UDP_تسجيل_منفذ": "logging.handlers.DEFAULT_UDP_LOGGING_PORT",
    # === unittest ===
    "افتراضي_اختبر_محمّل": "unittest.defaultTestLoader",
    # === logging ===
    "افتراضي_تسجيل_إعداد_منفذ": "logging.config.DEFAULT_LOGGING_CONFIG_PORT",
    "افتراضي_صابون_تسجيل_منفذ": "logging.handlers.DEFAULT_SOAP_LOGGING_PORT",
    # === multiprocessing ===
    "افتراضي_عائلة": "multiprocessing.connection.default_family",
    # === typing ===
    "افتراضي_قاموس": "typing.DefaultDict",
    # === ctypes ===
    "افتراضي_وضع": "ctypes.DEFAULT_MODE",
    # === filecmp ===
    "افتراضي_يتجاهل": "filecmp.DEFAULT_IGNORES",
    # === typing ===
    "اقرأ_فقط": "typing.ReadOnly",
    # === fcntl ===
    "اقفل_EX": "fcntl.LOCK_EX",
    "اقفل_MAND": "fcntl.LOCK_MAND",
    "اقفل_NB": "fcntl.LOCK_NB",
    "اقفل_SH": "fcntl.LOCK_SH",
    "اقفل_UN": "fcntl.LOCK_UN",
    "اقفل_اقرأ": "fcntl.LOCK_READ",
    "اقفل_اكتب": "fcntl.LOCK_WRITE",
    "اقفل_قراءة_كتابة": "fcntl.LOCK_RW",
    # === errno ===
    "الاتصال_أُجهض": "errno.ECONNABORTED",
    "الاتصال_أُعيد": "errno.ECONNRESET",
    "الاتصال_رُفض": "errno.ECONNREFUSED",
    "الاسم_طويل_جداً": "errno.ENAMETOOLONG",
    "الاسم_غير_فريد": "errno.ENOTUNIQ",
    "البروتوكول_غير_مدعوم": "errno.EPROTONOSUPPORT",
    "البروتوكول_غير_مربوط": "errno.EUNATCH",
    "الجمود_مات": "errno.EDEADLK",
    "الرابط_انقطع": "errno.ENOLINK",
    "الرسالة_طويلة_جداً": "errno.EMSGSIZE",
    "الشبكة_أُعيدت": "errno.ENETRESET",
    "الشبكة_غير_قابلة_للوصول": "errno.ENETUNREACH",
    "الشبكة_متوقفة": "errno.ENETDOWN",
    "العائلة_غير_مدعومة": "errno.EAFNOSUPPORT",
    "العملية_غير_مدعومة": "errno.EOPNOTSUPP",
    "العملية_غير_مسموحة": "errno.EPERM",
    "العنوان_غير_متاح": "errno.EADDRNOTAVAIL",
    "العنوان_مستخدم": "errno.EADDRINUSE",
    "المالك_مات": "errno.EOWNERDEAD",
    "المجلد_غير_فارغ": "errno.ENOTEMPTY",
    "المضيف_غير_قابل_للوصول": "errno.EHOSTUNREACH",
    "المضيف_متوقف": "errno.EHOSTDOWN",
    "المعرف_حُذف": "errno.EIDRM",
    "المفتاح_أُبطِل": "errno.EKEYREVOKED",
    "المفتاح_انتهى": "errno.EKEYEXPIRED",
    "المفتاح_رُفض": "errno.EKEYREJECTED",
    "المكتبة_تالفة": "errno.ELIBBAD",
    "الملف_كبير_جداً": "errno.EFBIG",
    # === tty ===
    "المهلة": "tty.VTIME",
    # === errno ===
    "الهيكل_غير_نظيف": "errno.EUCLEAN",
    "الوصول_للمكتبة_مرفوض": "errno.ELIBACC",
    "الوصول_مرفوض": "errno.EACCES",
    # === tty ===
    "امتداد_a": "tty.EXTA",
    "امتداد_b": "tty.EXTB",
    # === ctypes ===
    "املأ_الذاكرة": "ctypes.memset",
    # === tty ===
    "انتظر_الإفراغ_كله": "tty.TCSADRAIN",
    # === errno ===
    "انتهت_المهلة": "errno.ETIME",
    # === copy ===
    "انسخ_توزيع_جدول": "copy.dispatch_table",
    # === tty ===
    "انسياب_أي": "tty.IXANY",
    # === ctypes ===
    "انقل_الذاكرة": "ctypes.memmove",
    # === site ===
    "بادئات": "site.PREFIXES",
    # === typing ===
    "بايت_نص": "typing.ByteString",
    # === mmap ===
    "بروتوكول_اقرأ": "mmap.PROT_READ",
    "بروتوكول_اكتب": "mmap.PROT_WRITE",
    "بروتوكول_تنفيذ": "mmap.PROT_EXEC",
    # === typing ===
    "بلا_أرجع": "typing.NoReturn",
    # === tty ===
    "بلا_إفراغ": "tty.NOFLSH",
    # === typing ===
    "بلا_افتراضي": "typing.NoDefault",
    # === tty ===
    "بلا_خرج_رج_السيارة": "tty.ONOCR",
    # === venv ===
    "بيئة_افتراضية_مسجّل": "venv.logger",
    # === unicodedata ===
    "بيانات_معيار_يونيكود_3_2_0": "unicodedata.ucd_3_2_0",
    "بيانات_يونيكود_إصدار_3": "unicodedata.unidata_version",
    # === tty ===
    "تأخير_bsd": "tty.BSDLY",
    "تأخير_ff": "tty.FFDLY",
    "تأخير_الجدولة": "tty.TABDLY",
    "تأخير_السطر": "tty.NLDLY",
    "تأخير_الطرفية_الافتراضية": "tty.VTDLY",
    "تأخير_رج_السيارة": "tty.CRDLY",
    # === errno ===
    "تبادل_ممتلئ": "errno.EXFULL",
    # === tty ===
    "تبديل_الشاشة": "tty.VSWTCH",
    "تجاهل_التكافؤ": "tty.IGNPAR",
    "تجاهل_الكسر": "tty.IGNBRK",
    "تجاهل_رج_السيارة": "tty.IGNCR",
    # === errno ===
    "تجاوز_سعة": "errno.EOVERFLOW",
    "تجاوز_عدد_المكتبات": "errno.ELIBMAX",
    # === tty ===
    "تجريد_البت": "tty.ISTRIP",
    # === multiprocessing ===
    "تحذير_فرعي": "multiprocessing.SUBWARNING",
    # === stringprep ===
    "تحضير_النص_B1_عيّن": "stringprep.b1_set",
    "تحضير_النص_B3_استثناءات": "stringprep.b3_exceptions",
    "تحضير_النص_توحيد22_خواص": "stringprep.c22_specials",
    "تحضير_النص_توحيد6_عيّن": "stringprep.c6_set",
    "تحضير_النص_توحيد7_عيّن": "stringprep.c7_set",
    "تحضير_النص_توحيد8_عيّن": "stringprep.c8_set",
    "تحضير_النص_توحيد9_عيّن": "stringprep.c9_set",
    # === tty ===
    "تحكم_إيقاف_إضافي": "tty.CDSUSP",
    "تحكم_تدفق_عتاد": "tty.CRTSCTS",
    "تحويل_الحالة": "tty.IUCLC",
    "تحويل_السطر": "tty.INLCR",
    "تحويل_خرج_رج_السيارة": "tty.OCRNL",
    "تحويل_خرج_سطر": "tty.ONLCR",
    "تحويل_رج_السيارة": "tty.ICRNL",
    "تحويل_صغير": "tty.OLCUC",
    # === errno ===
    "تدفق_مكسور": "errno.ESTRPIPE",
    # === tty ===
    "ترميز_يونيكود_8": "tty.IUTF8",
    # === concurrent ===
    "تزامن_مستقبلات_أول_استثناء": "concurrent.futures.FIRST_EXCEPTION",
    # === logging ===
    "تسجيل_تحذير": "logging.WARNING",
    "تسجيل_تصحيح": "logging.DEBUG",
    "تسجيل_جذر": "logging.root",
    "تسجيل_حرج": "logging.CRITICAL",
    "تسجيل_خطأ": "logging.ERROR",
    "تسجيل_معلومات": "logging.INFO",
    # === typing ===
    "تسلسل": "typing.Sequence",
    # === errno ===
    "تسلسل_بايت_غير_قانوني": "errno.EILSEQ",
    "تسميم_аппаратي": "errno.EHWPOISON",
    # === multiprocessing ===
    "تصحيح_فرعي": "multiprocessing.SUBDEBUG",
    # === enum ===
    "تعداد_أخرج": "enum.EJECT",
    "تعداد_تحقق_فريد": "enum.EnumCheck.UNIQUE",
    "تعداد_تحقق_مستمر": "enum.EnumCheck.CONTINUOUS",
    "تعداد_تحقق_مسمّى_علامات": "enum.EnumCheck.NAMED_FLAGS",
    "تعداد_صارم": "enum.STRICT",
    "تعداد_طابق": "enum.CONFORM",
    "تعداد_فريد": "enum.UNIQUE",
    # === select ===
    "تعليق_إبول": "select.EPOLLHUP",
    "تعليق_استطلاع": "select.POLLHUP",
    "تعليق_قراءة_إبول": "select.EPOLLRDHUP",
    # === errno ===
    "تغيير_عن_بُعد": "errno.EREMCHG",
    # === tty ===
    "تكافؤ_زوجي": "tty.PARENB",
    "تكافؤ_فردي": "tty.PARODD",
    # === multiprocessing ===
    "تكراري_قفل_متبادل": "multiprocessing.synchronize.RECURSIVE_MUTEX",
    # === tty ===
    "تمديد_داخلي": "tty.IEXTEN",
    # === errno ===
    "تنفيذ_المكتبة_مرفوض": "errno.ELIBEXEC",
    # === pydoc ===
    "توثيق_بايثون_نص": "pydoc.text",
    # === tty ===
    "جدولة_0": "tty.TAB0",
    "جدولة_1": "tty.TAB1",
    "جدولة_2": "tty.TAB2",
    "جدولة_3": "tty.TAB3",
    # === errno ===
    "جمود": "errno.EDEADLOCK",
    "جهاز_خارجي": "errno.EXDEV",
    # === select ===
    "حافة_إبول": "select.EPOLLET",
    # === tty ===
    "حجم_التحكم_ازح": "tty.IOCSIZE_SHIFT",
    "حجم_التحكم_قناع": "tty.IOCSIZE_MASK",
    "حجم_المحارف": "tty.CSIZE",
    # === ctypes ===
    "حجم_وقت_T": "ctypes.SIZEOF_TIME_T",
    # === resource ===
    "حد_المورد_أولوية_الحقيقي": "resource.RLIMIT_RTPRIO",
    "حد_المورد_أولوية_اللطف": "resource.RLIMIT_NICE",
    "حد_المورد_الإشارات_المعلقة": "resource.RLIMIT_SIGPENDING",
    "حد_المورد_الذاكرة_المحجوزة": "resource.RLIMIT_RSS",
    "حد_المورد_بيانات": "resource.RLIMIT_DATA",
    "حد_المورد_حجم_الملف": "resource.RLIMIT_FSIZE",
    "حد_المورد_طابور_الرسائل": "resource.RLIMIT_MSGQUEUE",
    "حد_المورد_عدد_العمليات": "resource.RLIMIT_NPROC",
    "حد_المورد_عدد_الملفات": "resource.RLIMIT_NOFILE",
    "حد_المورد_قفل_الذاكرة": "resource.RLIMIT_MEMLOCK",
    "حد_المورد_كـ": "resource.RLIMIT_AS",
    "حد_المورد_معالج": "resource.RLIMIT_CPU",
    "حد_المورد_مكدس": "resource.RLIMIT_STACK",
    "حد_المورد_ملف_الإخراج": "resource.RLIMIT_OFILE",
    "حد_المورد_نواة": "resource.RLIMIT_CORE",
    "حد_المورد_وقت_الحقيقي": "resource.RLIMIT_RTTIME",
    "حد_لا_نهاية": "resource.RLIM_INFINITY",
    # === selectors ===
    "حدث_اقرأ": "selectors.EVENT_READ",
    "حدث_اكتب": "selectors.EVENT_WRITE",
    # === logging ===
    "حذّر": "logging.WARN",
    # === tty ===
    "حرف_التحكم": "tty.TCXONC",
    # === typing ===
    "حرفي": "typing.Literal",
    "حرفي_نص": "typing.LiteralString",
    # === tty ===
    "حشو_حذف": "tty.OFDEL",
    "حشو_ملء": "tty.OFILL",
    # === errno ===
    "حلقة_روابط_كثيرة": "errno.ELOOP",
    # === select ===
    "خارج_إبول": "select.EPOLLOUT",
    # === errno ===
    "خارج_المجال": "errno.EDOM",
    "خارج_المدى": "errno.ERANGE",
    # === tty ===
    "خرج_سطر": "tty.ONLRET",
    # === mmap ===
    "خريطة_32_بت": "mmap.MAP_32BIT",
    "خريطة_املأ": "mmap.MAP_POPULATE",
    "خريطة_امنع_الكتابة": "mmap.MAP_DENYWRITE",
    "خريطة_بلا_حجز": "mmap.MAP_NORESERVE",
    "خريطة_خاص": "mmap.MAP_PRIVATE",
    # === typing ===
    "خريطة_عرض": "typing.MappingView",
    # === mmap ===
    "خريطة_قابل_للتنفيذ": "mmap.MAP_EXECUTABLE",
    "خريطة_مجهول": "mmap.MAP_ANON",
    "خريطة_مشترك": "mmap.MAP_SHARED",
    "خريطة_مكدس": "mmap.MAP_STACK",
    # === select ===
    "خطأ_إبول": "select.EPOLLERR",
    # === errno ===
    "خطأ_إدخال": "errno.EIO",
    "خطأ_إدخال_عن_بعد": "errno.EREMOTEIO",
    "خطأ_الاتصال": "errno.ECOMM",
    # === pty ===
    "خطأ_قياسي_رقم_الملف": "pty.STDERR_FILENO",
    # === unittest ===
    "خطأ_قياسي_سطر": "unittest.result.STDERR_LINE",
    # === errno ===
    "خيار_البروتوكول_غير_متاح": "errno.ENOPROTOOPT",
    # === unittest ===
    "دالة_أنواع": "unittest.mock.FunctionTypes",
    # === mmap ===
    "دقة_التخصيص": "mmap.ALLOCATIONGRANULARITY",
    "ذاكرة_مُخزَّنة_حجم_الصفحة": "mmap.PAGESIZE",
    "ذاكرة_مُخزَّنة_خريطة_مجهول": "mmap.MAP_ANONYMOUS",
    # === zipapp ===
    "رئيسي_قالب": "zipapp.MAIN_TEMPLATE",
    # === errno ===
    "رابط_قديم": "errno.ESTALE",
    # === select ===
    "رسالة_إبول": "select.EPOLLMSG",
    # === errno ===
    "رسالة_سيئة": "errno.EBADMSG",
    # === multiprocessing ===
    "رسالة_طول": "multiprocessing.connection.MESSAGE_LENGTH",
    # === unittest ===
    "رشّح_مجلد": "unittest.mock.FILTER_DIR",
    # === errno ===
    "رقم_الخطأ_أعد_المحاولة": "errno.EAGAIN",
    "رقم_الخطأ_أنبوب_مكسور": "errno.ESPIPE",
    "رقم_الخطأ_العائلة_غير_مدعومة": "errno.EPFNOSUPPORT",
    "رقم_الخطأ_انتهت_المهلة": "errno.ETIMEDOUT",
    "رقم_الخطأ_خارج_النطاق": "errno.ECHRNG",
    "رقم_الخطأ_خطأ_بروتوكول": "errno.EPROTO",
    "رقم_الخطأ_عنوان_سيئ": "errno.EFAULT",
    "رقم_الخطأ_غير_مدعوم": "errno.ENOTSUP",
    "رقم_الخطأ_لا_جهاز": "errno.ENXIO",
    "رقم_الخطأ_موجود": "errno.EEXIST",
    "رقم_الخطأ_نظام_ملفات_للقراءة_فقط": "errno.ESRMNT",
    "رقم_الخطأ_هو_مجلد": "errno.EISDIR",
    "رقم_الخطأ_واصف_ملف_سيئ": "errno.EBADFD",
    "رقم_خارج_النطاق": "errno.ELNRNG",
    "رموز_الأخطاء": "errno.errorcode",
    "روابط_كثيرة_جداً": "errno.EMLINK",
    # === zipapp ===
    "س_هاش_بان_ترميز": "zipapp.shebang_encoding",
    # === logging ===
    "سجل_النظام_TCP_منفذ": "logging.handlers.SYSLOG_TCP_PORT",
    "سجل_النظام_UDP_منفذ": "logging.handlers.SYSLOG_UDP_PORT",
    "سجل_خيط": "logging.logThreads",
    "سجل_عالج": "logging.logProcesses",
    "سجل_غير_متزامن_إدخال_إخراج_مهمة": "logging.logAsyncioTasks",
    "سجل_متعدد_معالجة": "logging.logMultiprocessing",
    # === unittest ===
    "سحري_دوال": "unittest.mock.magic_methods",
    # === tty ===
    "سرعة_الإخراج": "tty.OSPEED",
    "سرعة_الإدخال": "tty.ISPEED",
    "سرعة_الباود": "tty.CBAUD",
    "سرعة_الباود_إضافية": "tty.CBAUDEX",
    "سرعة_الباود_داخلية": "tty.CIBAUD",
    # === readline ===
    "سطر_قراءة_خلفية": "readline.backend",
    # === typing ===
    "سلسل": "typing.Concatenate",
    "سلسلة_خريطة": "typing.ChainMap",
    # === errno ===
    "سيُحجب": "errno.EWOULDBLOCK",
    # === tty ===
    "صدى": "tty.ECHO",
    "صدى_التحكم": "tty.ECHOCTL",
    "صدى_السطر": "tty.ECHONL",
    "صدى_الطباعة": "tty.ECHOPRT",
    "صدى_المسح": "tty.ECHOE",
    "صدى_الموافقة": "tty.ECHOK",
    # === termios ===
    "صفات_أفرغ_الطرفية": "termios.TCFLSH",
    "صفات_الطرفية_B_0": "termios.B0",
    "صفات_الطرفية_B_0_2": "termios.BS0",
    "صفات_الطرفية_B_1": "termios.BS1",
    "صفات_الطرفية_B_1000000": "termios.B1000000",
    "صفات_الطرفية_B_110": "termios.B110",
    "صفات_الطرفية_B_115200": "termios.B115200",
    "صفات_الطرفية_B_1152000": "termios.B1152000",
    "صفات_الطرفية_B_1200": "termios.B1200",
    "صفات_الطرفية_B_134": "termios.B134",
    "صفات_الطرفية_B_150": "termios.B150",
    "صفات_الطرفية_B_1500000": "termios.B1500000",
    "صفات_الطرفية_B_1800": "termios.B1800",
    "صفات_الطرفية_B_19200": "termios.B19200",
    "صفات_الطرفية_B_200": "termios.B200",
    "صفات_الطرفية_B_2000000": "termios.B2000000",
    "صفات_الطرفية_B_230400": "termios.B230400",
    "صفات_الطرفية_B_2400": "termios.B2400",
    "صفات_الطرفية_B_2500000": "termios.B2500000",
    "صفات_الطرفية_B_300": "termios.B300",
    "صفات_الطرفية_B_3000000": "termios.B3000000",
    "صفات_الطرفية_B_3500000": "termios.B3500000",
    "صفات_الطرفية_B_38400": "termios.B38400",
    "صفات_الطرفية_B_4000000": "termios.B4000000",
    "صفات_الطرفية_B_460800": "termios.B460800",
    "صفات_الطرفية_B_4800": "termios.B4800",
    "صفات_الطرفية_B_50": "termios.B50",
    "صفات_الطرفية_B_500000": "termios.B500000",
    "صفات_الطرفية_B_57600": "termios.B57600",
    "صفات_الطرفية_B_576000": "termios.B576000",
    "صفات_الطرفية_B_600": "termios.B600",
    "صفات_الطرفية_B_75": "termios.B75",
    "صفات_الطرفية_B_921600": "termios.B921600",
    "صفات_الطرفية_B_9600": "termios.B9600",
    "صفات_الطرفية_CR_0": "termios.CR0",
    "صفات_الطرفية_CR_1": "termios.CR1",
    "صفات_الطرفية_CR_2": "termios.CR2",
    "صفات_الطرفية_CR_3": "termios.CR3",
    "صفات_الطرفية_C_5": "termios.CS5",
    "صفات_الطرفية_C_6": "termios.CS6",
    "صفات_الطرفية_C_7": "termios.CS7",
    "صفات_الطرفية_C_8": "termios.CS8",
    "صفات_الطرفية_FF_0": "termios.FF0",
    "صفات_الطرفية_FF_1": "termios.FF1",
    "صفات_الطرفية_NL_0": "termios.NL0",
    "صفات_الطرفية_NL_1": "termios.NL1",
    "صفات_الطرفية_N_ppp": "termios.N_PPP",
    "صفات_الطرفية_N_slip": "termios.N_SLIP",
    "صفات_الطرفية_N_جرّد": "termios.N_STRIP",
    "صفات_الطرفية_N_طرفية": "termios.N_TTY",
    "صفات_الطرفية_N_فأرة": "termios.N_MOUSE",
    "صفات_الطرفية_TIOCM_CD": "termios.TIOCM_CD",
    "صفات_الطرفية_TIOCM_DSR": "termios.TIOCM_DSR",
    "صفات_الطرفية_TIOCM_DTR": "termios.TIOCM_DTR",
    "صفات_الطرفية_TIOCM_LE": "termios.TIOCM_LE",
    "صفات_الطرفية_TIOCM_RI": "termios.TIOCM_RI",
    "صفات_الطرفية_TIOCM_RNG": "termios.TIOCM_RNG",
    "صفات_الطرفية_TIOCM_RTS": "termios.TIOCM_RTS",
    "صفات_الطرفية_TIOCM_SR": "termios.TIOCM_SR",
    "صفات_الطرفية_TIOCM_ST": "termios.TIOCM_ST",
    "صفات_الطرفية_TIOCM_ct": "termios.TIOCM_CTS",
    "صفات_الطرفية_TIOCM_ناقل": "termios.TIOCM_CAR",
    "صفات_الطرفية_TIOC_CONS": "termios.TIOCCONS",
    "صفات_الطرفية_TIOC_EXCL": "termios.TIOCEXCL",
    "صفات_الطرفية_TIOC_GETD": "termios.TIOCGETD",
    "صفات_الطرفية_TIOC_GICOUNT": "termios.TIOCGICOUNT",
    "صفات_الطرفية_TIOC_GLCKTRMIOS": "termios.TIOCGLCKTRMIOS",
    "صفات_الطرفية_TIOC_GPGRP": "termios.TIOCGPGRP",
    "صفات_الطرفية_TIOC_GSERIAL": "termios.TIOCGSERIAL",
    "صفات_الطرفية_TIOC_GSOFTCAR": "termios.TIOCGSOFTCAR",
    "صفات_الطرفية_TIOC_GWINSZ": "termios.TIOCGWINSZ",
    "صفات_الطرفية_TIOC_INQ": "termios.TIOCINQ",
    "صفات_الطرفية_TIOC_LINUX": "termios.TIOCLINUX",
    "صفات_الطرفية_TIOC_MBIC": "termios.TIOCMBIC",
    "صفات_الطرفية_TIOC_MBIS": "termios.TIOCMBIS",
    "صفات_الطرفية_TIOC_MGET": "termios.TIOCMGET",
    "صفات_الطرفية_TIOC_MIWAIT": "termios.TIOCMIWAIT",
    "صفات_الطرفية_TIOC_MSET": "termios.TIOCMSET",
    "صفات_الطرفية_TIOC_NOTTY": "termios.TIOCNOTTY",
    "صفات_الطرفية_TIOC_NXCL": "termios.TIOCNXCL",
    "صفات_الطرفية_TIOC_OUTQ": "termios.TIOCOUTQ",
    "صفات_الطرفية_TIOC_PKT": "termios.TIOCPKT",
    "صفات_الطرفية_TIOC_PKT_أفرغ_اقرأ": "termios.TIOCPKT_FLUSHREAD",
    "صفات_الطرفية_TIOC_PKT_أفرغ_اكتب": "termios.TIOCPKT_FLUSHWRITE",
    "صفات_الطرفية_TIOC_PKT_أوقف": "termios.TIOCPKT_DOSTOP",
    "صفات_الطرفية_TIOC_PKT_أوقف_2": "termios.TIOCPKT_STOP",
    "صفات_الطرفية_TIOC_PKT_ابدأ": "termios.TIOCPKT_START",
    "صفات_الطرفية_TIOC_PKT_بلا_إيقاف": "termios.TIOCPKT_NOSTOP",
    "صفات_الطرفية_TIOC_PKT_بيانات": "termios.TIOCPKT_DATA",
    "صفات_الطرفية_TIOC_SCTTY": "termios.TIOCSCTTY",
    "صفات_الطرفية_TIOC_SERCONFIG": "termios.TIOCSERCONFIG",
    "صفات_الطرفية_TIOC_SERGETLSR": "termios.TIOCSERGETLSR",
    "صفات_الطرفية_TIOC_SERGETMULTI": "termios.TIOCSERGETMULTI",
    "صفات_الطرفية_TIOC_SERGSTRUCT": "termios.TIOCSERGSTRUCT",
    "صفات_الطرفية_TIOC_SERGWILD": "termios.TIOCSERGWILD",
    "صفات_الطرفية_TIOC_SERSETMULTI": "termios.TIOCSERSETMULTI",
    "صفات_الطرفية_TIOC_SERSWILD": "termios.TIOCSERSWILD",
    "صفات_الطرفية_TIOC_SER_TEMT": "termios.TIOCSER_TEMT",
    "صفات_الطرفية_TIOC_SETD": "termios.TIOCSETD",
    "صفات_الطرفية_TIOC_SLCKTRMIOS": "termios.TIOCSLCKTRMIOS",
    "صفات_الطرفية_TIOC_SPGRP": "termios.TIOCSPGRP",
    "صفات_الطرفية_TIOC_SSERIAL": "termios.TIOCSSERIAL",
    "صفات_الطرفية_TIOC_SSOFTCAR": "termios.TIOCSSOFTCAR",
    "صفات_الطرفية_TIOC_STI": "termios.TIOCSTI",
    "صفات_الطرفية_TIOC_SWINSZ": "termios.TIOCSWINSZ",
    "صفات_الطرفية_VEOL": "termios.VEOL",
    "صفات_الطرفية_VEOL_2": "termios.VEOL2",
    "صفات_الطرفية_VT_0": "termios.VT0",
    "صفات_الطرفية_VT_1": "termios.VT1",
    "صفات_الطرفية_أرسل_فاصلة": "termios.TCSBRK",
    "صفات_الطرفية_أرسل_فاصلة_طويلة": "termios.TCSBRKP",
    "صفات_الطرفية_أفرغ_الآن": "termios.TCSANOW",
    "صفات_الطرفية_أفرغ_الإخراج": "termios.FLUSHO",
    "صفات_الطرفية_أفرغ_الإخراج_2": "termios.TCOFLUSH",
    "صفات_الطرفية_أفرغ_الإدخال": "termios.TCIFLUSH",
    "صفات_الطرفية_أفرغ_الإدخال_كله": "termios.TCIOFLUSH",
    "صفات_الطرفية_أفرغ_كل": "termios.CFLUSH",
    "صفات_الطرفية_أفرغ_كل_وانتظر": "termios.TCSAFLUSH",
    "صفات_الطرفية_أقصى_جرس": "termios.IMAXBEL",
    "صفات_الطرفية_أوقف_الإخراج": "termios.TCOOFF",
    "صفات_الطرفية_أوقف_الإدخال": "termios.TCIOFF",
    "صفات_الطرفية_أوقف_الانسياب": "termios.IXOFF",
    "صفات_الطرفية_أوقف_الخرج": "termios.TOSTOP",
    "صفات_الطرفية_إدخال_غير_حاجب": "termios.FIONBIO",
    "صفات_الطرفية_إدخال_غير_متزامن": "termios.FIOASYNC",
    "صفات_الطرفية_إشارات": "termios.ISIG",
    "صفات_الطرفية_إعادة_الطباعة": "termios.CRPRNT",
    "صفات_الطرفية_إيقاف_ثنائي": "termios.CSTOPB",
    "صفات_الطرفية_احصل_على_السمات": "termios.TCGETS",
    "صفات_الطرفية_احصل_على_كل": "termios.TCGETA",
    "صفات_الطرفية_استثناء_الإدخال": "termios.FIOCLEX",
    "صفات_الطرفية_استثناء_غير_حاجب": "termios.FIONCLEX",
    "صفات_الطرفية_الحد_الأدنى": "termios.VMIN",
    "صفات_الطرفية_المهلة": "termios.VTIME",
    "صفات_الطرفية_امتداد_a": "termios.EXTA",
    "صفات_الطرفية_امتداد_b": "termios.EXTB",
    "صفات_الطرفية_انتظر_الإفراغ_كله": "termios.TCSADRAIN",
    "صفات_الطرفية_انسياب_أي": "termios.IXANY",
    "صفات_الطرفية_بلا_إفراغ": "termios.NOFLSH",
    "صفات_الطرفية_بلا_خرج_رج_السيارة": "termios.ONOCR",
    "صفات_الطرفية_تأخير_bsd": "termios.BSDLY",
    "صفات_الطرفية_تأخير_ff": "termios.FFDLY",
    "صفات_الطرفية_تأخير_الجدولة": "termios.TABDLY",
    "صفات_الطرفية_تأخير_السطر": "termios.NLDLY",
    "صفات_الطرفية_تأخير_رج_السيارة": "termios.CRDLY",
    "صفات_الطرفية_تبديل": "termios.VSWTC",
    "صفات_الطرفية_تبديل_الشاشة": "termios.VSWTCH",
    "صفات_الطرفية_تجاهل_التكافؤ": "termios.IGNPAR",
    "صفات_الطرفية_تجاهل_الكسر": "termios.IGNBRK",
    "صفات_الطرفية_تجاهل_رج_السيارة": "termios.IGNCR",
    "صفات_الطرفية_تجريد_البت": "termios.ISTRIP",
    "صفات_الطرفية_تحكم_إيقاف_إضافي": "termios.CDSUSP",
    "صفات_الطرفية_تحكم_تدفق_عتاد": "termios.CRTSCTS",
    "صفات_الطرفية_تحويل_الحالة": "termios.IUCLC",
    "صفات_الطرفية_تحويل_الحالة_2": "termios.XCASE",
    "صفات_الطرفية_تحويل_السطر": "termios.INLCR",
    "صفات_الطرفية_تحويل_خرج_رج_السيارة": "termios.OCRNL",
    "صفات_الطرفية_تحويل_خرج_سطر": "termios.ONLCR",
    "صفات_الطرفية_تحويل_رج_السيارة": "termios.ICRNL",
    "صفات_الطرفية_تحويل_صغير": "termios.OLCUC",
    "صفات_الطرفية_ترميز_يونيكود_8": "termios.IUTF8",
    "صفات_الطرفية_تكافؤ_زوجي": "termios.PARENB",
    "صفات_الطرفية_تكافؤ_فردي": "termios.PARODD",
    "صفات_الطرفية_تمديد_داخلي": "termios.IEXTEN",
    "صفات_الطرفية_جدولة_0": "termios.TAB0",
    "صفات_الطرفية_جدولة_1": "termios.TAB1",
    "صفات_الطرفية_جدولة_2": "termios.TAB2",
    "صفات_الطرفية_جدولة_3": "termios.TAB3",
    "صفات_الطرفية_حجم_التحكم_ازح": "termios.IOCSIZE_SHIFT",
    "صفات_الطرفية_حجم_التحكم_قناع": "termios.IOCSIZE_MASK",
    "صفات_الطرفية_حجم_المحارف": "termios.CSIZE",
    "صفات_الطرفية_حرف_التحكم": "termios.TCXONC",
    "صفات_الطرفية_حشو_حذف": "termios.OFDEL",
    "صفات_الطرفية_حشو_ملء": "termios.OFILL",
    "صفات_الطرفية_خرج_سطر": "termios.ONLRET",
    "صفات_الطرفية_سرعة_الباود": "termios.CBAUD",
    "صفات_الطرفية_سرعة_الباود_إضافية": "termios.CBAUDEX",
    "صفات_الطرفية_سرعة_الباود_داخلية": "termios.CIBAUD",
    "صفات_الطرفية_صدى": "termios.ECHO",
    "صفات_الطرفية_صدى_التحكم": "termios.ECHOCTL",
    "صفات_الطرفية_صدى_السطر": "termios.ECHONL",
    "صفات_الطرفية_صدى_الطباعة": "termios.ECHOPRT",
    "صفات_الطرفية_صدى_المسح": "termios.ECHOE",
    "صفات_الطرفية_صدى_المسح_2": "termios.ECHOKE",
    "صفات_الطرفية_صدى_الموافقة": "termios.ECHOK",
    "صفات_الطرفية_عدد_المقروء": "termios.FIONREAD",
    "صفات_الطرفية_علامات_الجدولة": "termios.XTABS",
    "صفات_الطرفية_علامة_التكافؤ": "termios.PARMRK",
    "صفات_الطرفية_علّق_عند_الإغلاق": "termios.HUPCL",
    "صفات_الطرفية_عيّن_السمات": "termios.TCSETS",
    "صفات_الطرفية_عيّن_السمات_وأفرغ": "termios.TCSETSF",
    "صفات_الطرفية_عيّن_السمات_وانتظر": "termios.TCSETSW",
    "صفات_الطرفية_عيّن_كل": "termios.TCSETA",
    "صفات_الطرفية_عيّن_كل_وأفرغ": "termios.TCSETAF",
    "صفات_الطرفية_عيّن_كل_وانتظر": "termios.TCSETAW",
    "صفات_الطرفية_فحص_التكافؤ": "termios.INPCK",
    "صفات_الطرفية_فعّل_الإخراج": "termios.TCOON",
    "صفات_الطرفية_فعّل_الإدخال": "termios.TCION",
    "صفات_الطرفية_فعّل_الانسياب": "termios.IXON",
    "صفات_الطرفية_قانوني": "termios.ICANON",
    "صفات_الطرفية_قيد_الانتظار": "termios.PENDIN",
    "صفات_الطرفية_محارف_التحكم": "termios.NCCS",
    "صفات_الطرفية_محرف_إعادة_الطباعة": "termios.VREPRINT",
    "صفات_الطرفية_محرف_الإيقاف": "termios.CSTOP",
    "صفات_الطرفية_محرف_الإيقاف_2": "termios.VSTOP",
    "صفات_الطرفية_محرف_البدء": "termios.CSTART",
    "صفات_الطرفية_محرف_البدء_2": "termios.VSTART",
    "صفات_الطرفية_محرف_التالي": "termios.CLNEXT",
    "صفات_الطرفية_محرف_التالي_2": "termios.VLNEXT",
    "صفات_الطرفية_محرف_التخلص": "termios.VDISCARD",
    "صفات_الطرفية_محرف_التعليق": "termios.CSUSP",
    "صفات_الطرفية_محرف_التعليق_2": "termios.VSUSP",
    "صفات_الطرفية_محرف_الخروج": "termios.CQUIT",
    "صفات_الطرفية_محرف_الخروج_2": "termios.VQUIT",
    "صفات_الطرفية_محرف_القتل": "termios.CKILL",
    "صفات_الطرفية_محرف_القتل_2": "termios.VKILL",
    "صفات_الطرفية_محرف_القراءة": "termios.CREAD",
    "صفات_الطرفية_محرف_المسح": "termios.VERASE",
    "صفات_الطرفية_محرف_المقاطعة": "termios.CINTR",
    "صفات_الطرفية_محرف_المقاطعة_2": "termios.VINTR",
    "صفات_الطرفية_محرف_مسح_الكلمة": "termios.CWERASE",
    "صفات_الطرفية_محرف_مسح_الكلمة_2": "termios.VWERASE",
    "صفات_الطرفية_محرف_نهاية_الملف": "termios.VEOF",
    "صفات_الطرفية_محلي": "termios.CLOCAL",
    "صفات_الطرفية_مسح_محرف": "termios.CERASE",
    "صفات_الطرفية_معالجة_الإخراج": "termios.OPOST",
    "صفات_الطرفية_معالجة_خارجية": "termios.EXTPROC",
    "صفات_الطرفية_مقاطعة_السطر": "termios.BRKINT",
    "صفات_الطرفية_نهاية_سطر": "termios.CEOL",
    "صفات_الطرفية_نهاية_ملف": "termios.CEOF",
    "صفات_الطرفية_نهاية_نقل": "termios.CEOT",
    "صفات_تأخير_الطرفية_الافتراضية": "termios.VTDLY",
    # === logging ===
    "صفّر_خطأ": "logging.config.RESET_ERROR",
    # === dataclasses ===
    "صنف_بيانات_KW_فقط": "dataclasses.KW_ONLY",
    "صنف_بيانات_ناقص": "dataclasses.MISSING",
    # === typing ===
    "صنف_متغير": "typing.ClassVar",
    "طابور_مزدوج": "typing.Deque",
    # === tty ===
    "طرفية_B_0": "tty.BS0",
    "طرفية_TIOC_PKT_أوقف": "tty.TIOCPKT_STOP",
    "طرفية_أفرغ_الإخراج": "tty.TCOFLUSH",
    "طرفية_إشارات": "tty.ISIG",
    "طرفية_الحد_الأدنى": "tty.VMIN",
    "طرفية_تبديل": "tty.VSWTC",
    "طرفية_تحويل_الحالة": "tty.XCASE",
    "طرفية_صدى_المسح": "tty.ECHOKE",
    "طرفية_محرف_الإيقاف": "tty.VSTOP",
    "طرفية_محرف_البدء": "tty.VSTART",
    "طرفية_محرف_التالي": "tty.VLNEXT",
    "طرفية_محرف_التعليق": "tty.VSUSP",
    "طرفية_محرف_الخروج": "tty.VQUIT",
    "طرفية_محرف_القتل": "tty.VKILL",
    "طرفية_محرف_المقاطعة": "tty.VINTR",
    "طرفية_محرف_مسح_الكلمة": "tty.VWERASE",
    # === errno ===
    "طلب_عنوان_سيئ": "errno.EBADRQC",
    # === multiprocessing ===
    "عائلات": "multiprocessing.connection.families",
    # === signal ===
    "عدد_الإشارات": "signal.NSIG",
    # === tty ===
    "عدد_المقروء": "tty.FIONREAD",
    # === unittest ===
    "عدديات": "unittest.mock.numerics",
    # === typing ===
    "عدّاد": "typing.Counter",
    # === tty ===
    "علامات_الجدولة": "tty.XTABS",
    # === errno ===
    "علامة_اقتباس_ناقصة": "errno.EDQUOT",
    # === tty ===
    "علامة_التكافؤ": "tty.PARMRK",
    # === enum ===
    "علامة_حدّ_أبقِ": "enum.FlagBoundary.KEEP",
    "علامة_حدّ_أخرج": "enum.FlagBoundary.EJECT",
    "علامة_حدّ_صارم": "enum.FlagBoundary.STRICT",
    "علامة_حدّ_طابق": "enum.FlagBoundary.CONFORM",
    # === tty ===
    "علّق_عند_الإغلاق": "tty.HUPCL",
    # === errno ===
    "عن_بُعد": "errno.EREMOTE",
    # === typing ===
    "عناصر_عرض": "typing.ItemsView",
    # === errno ===
    "عنوان_الوجهة_مطلوب": "errno.EDESTADDRREQ",
    "عنوان_سيئ": "errno.EBADR",
    "عنوان_مقبس_سيئ": "errno.EBADSLT",
    # === tty ===
    "عيّن_السمات": "tty.TCSETS",
    "عيّن_السمات_وأفرغ": "tty.TCSETSF",
    "عيّن_السمات_وانتظر": "tty.TCSETSW",
    "عيّن_كل": "tty.TCSETA",
    "عيّن_كل_وأفرغ": "tty.TCSETAF",
    "عيّن_كل_وانتظر": "tty.TCSETAW",
    # === errno ===
    "غير_قابل_للاسترجاع": "errno.ENOTRECOVERABLE",
    "غير_متاح": "errno.ENAVAIL",
    # === typing ===
    "غير_متزامن_قابل_للتكرار": "typing.AsyncIterable",
    "غير_متزامن_مكرّر": "typing.AsyncIterator",
    "غير_متزامن_مولّد": "typing.AsyncGenerator",
    # === errno ===
    "غير_متصل": "errno.ENOTCONN",
    "غير_مدعوم": "errno.ENOSYS",
    # === logging ===
    "غير_مُعيَّن": "logging.NOTSET",
    # === tty ===
    "فحص_التكافؤ": "tty.INPCK",
    # === unittest ===
    "فرق_محذوف": "unittest.case.DIFF_OMITTED",
    # === errno ===
    "فشل_إنهاء": "errno.ERFKILL",
    "فشل_التنفيذ": "errno.ENOEXEC",
    # === tty ===
    "فعّل_الإخراج": "tty.TCOON",
    "فعّل_الإدخال": "tty.TCION",
    "فعّل_الانسياب": "tty.IXON",
    # === site ===
    "فعّل_مستخدم_موقع": "site.ENABLE_USER_SITE",
    # === unittest ===
    "في_المكان": "unittest.mock.inplace",
    # === typing ===
    "قابل_للاستدعاء": "typing.Callable",
    "قابل_للانتظار": "typing.Awaitable",
    "قابل_للتجزئة": "typing.Hashable",
    "قابل_للتعديل_تسلسل": "typing.MutableSequence",
    "قابل_للتعديل_خريطة": "typing.MutableMapping",
    "قابل_للتعديل_عيّن": "typing.MutableSet",
    "قابل_للتكرار": "typing.Iterable",
    "قابل_للعكس": "typing.Reversible",
    # === logging ===
    "قاتل": "logging.FATAL",
    # === tty ===
    "قانوني": "tty.ICANON",
    # === select ===
    "قراءة_استطلاع": "select.POLLRDNORM",
    "قراءة_عادية_إبول": "select.EPOLLRDNORM",
    # === errno ===
    "قسم_المكتبة_تالف": "errno.ELIBSCN",
    "قطع_استدعاء": "errno.EINTR",
    "قفزات_كثيرة": "errno.EMULTIHOP",
    # === tty ===
    "قيد_الانتظار": "tty.PENDIN",
    # === errno ===
    "قيد_التنفيذ": "errno.EINPROGRESS",
    # === typing ===
    "قيم_عرض": "typing.ValuesView",
    "كتابة_أخير": "typing.Final",
    "كتابة_اختياري": "typing.Optional",
    # === select ===
    "كتابة_استطلاع": "select.POLLWRNORM",
    # === typing ===
    "كتابة_تعاونية": "typing.Coroutine",
    "كتابة_حاوية": "typing.Container",
    "كتابة_خريطة": "typing.Mapping",
    "كتابة_صف": "typing.Tuple",
    # === select ===
    "كتابة_عادية_إبول": "select.EPOLLWRNORM",
    # === typing ===
    "كتابة_عيّن": "typing.Set",
    "كتابة_فكّ_الحزمة": "typing.Unpack",
    "كتابة_قائمة": "typing.List",
    "كتابة_قاموس": "typing.Dict",
    "كتابة_مجموعة": "typing.Collection",
    "كتابة_مطلوب": "typing.Required",
    "كتابة_نوع": "typing.Type",
    # === concurrent ===
    "كل_اكتمل": "concurrent.futures.ALL_COMPLETED",
    # === errno ===
    "لا_CSI": "errno.ENOCSI",
    "لا_أقفال_متاحة": "errno.ENOLCK",
    "لا_بيانات": "errno.ENODATA",
    "لا_جهاز": "errno.ENODEV",
    "لا_حزمة": "errno.ENOPKG",
    "لا_ذاكرة": "errno.ENOMEM",
    "لا_رسالة": "errno.ENOMSG",
    "لا_شبكة": "errno.ENONET",
    "لا_عملية": "errno.ESRCH",
    "لا_مخازن_متاحة": "errno.ENOBUFS",
    "لا_مساحة": "errno.ENOSPC",
    # === typing ===
    "لا_مطلوب": "typing.NotRequired",
    # === errno ===
    "لا_مفتاح": "errno.ENOKEY",
    "لا_ملف": "errno.ENOENT",
    "لا_موارد": "errno.ENOSR",
    "لا_وسيط": "errno.ENOMEDIUM",
    "لا_يمكن_الإرسال_بعد_الإغلاق": "errno.ESHUTDOWN",
    "لا_يوجد_ثقب": "errno.ENOANO",
    # === multiprocessing ===
    "له_ذاكرة_مشتركة": "multiprocessing.managers.HAS_SHMEM",
    # === errno ===
    "ليس_اسماً": "errno.ENOTNAM",
    "ليس_تدفقاً": "errno.ENOSTR",
    "ليس_جهاز_كتلي": "errno.ENOTBLK",
    "ليس_طرفية": "errno.ENOTTY",
    "ليس_مجلداً": "errno.ENOTDIR",
    "ليس_مقبساً": "errno.ENOTSOCK",
    # === signal ===
    "مؤقّت_افتراضي": "signal.ITIMER_VIRTUAL",
    "مؤقّت_تحليل": "signal.ITIMER_PROF",
    "مؤقّت_حقيقي": "signal.ITIMER_REAL",
    # === errno ===
    "متصل_بالفعل": "errno.EISCONN",
    # === multiprocessing ===
    "متعدد_معالجة_اتصال_حجم_المخزن": "multiprocessing.connection.BUFSIZE",
    "متعدد_معالجة_مجموعة_أغلق": "multiprocessing.pool.CLOSE",
    "متعدد_معالجة_مجموعة_أنهِ": "multiprocessing.pool.TERMINATE",
    "متعدد_معالجة_مجموعة_ابدأ_تهيئة": "multiprocessing.pool.INIT",
    "متعدد_معالجة_مجموعة_شغّل": "multiprocessing.pool.RUN",
    "متعدد_معالجة_مزامنة_إشارة_مرور": "multiprocessing.synchronize.SEMAPHORE",
    # === typing ===
    "مجرد_عيّن": "typing.AbstractSet",
    "مجمّد_عيّن": "typing.FrozenSet",
    # === tty ===
    "محارف_التحكم": "tty.NCCS",
    "محرف_إعادة_الطباعة": "tty.VREPRINT",
    "محرف_الإيقاف": "tty.CSTOP",
    "محرف_البدء": "tty.CSTART",
    "محرف_التالي": "tty.CLNEXT",
    "محرف_التخلص": "tty.VDISCARD",
    "محرف_التعليق": "tty.CSUSP",
    "محرف_الخروج": "tty.CQUIT",
    "محرف_القتل": "tty.CKILL",
    "محرف_القراءة": "tty.CREAD",
    "محرف_المسح": "tty.VERASE",
    "محرف_المقاطعة": "tty.CINTR",
    "محرف_مسح_الكلمة": "tty.CWERASE",
    "محرف_نهاية_الملف": "tty.VEOF",
    "محلي": "tty.CLOCAL",
    # === errno ===
    "مراجع_كثيرة_جداً": "errno.ETOOMANYREFS",
    # === select ===
    "مرة_إبول": "select.EPOLLONESHOT",
    # === typing ===
    "مرتّب_قاموس": "typing.OrderedDict",
    # === pydoc ===
    "مساعدة_2": "pydoc.help",
    # === typing ===
    "مستبعد_سمات": "typing.EXCLUDED_ATTRIBUTES",
    "مستحيل": "typing.Never",
    # === site ===
    "مستخدم_أساس": "site.USER_BASE",
    "مستخدم_موقع": "site.USER_SITE",
    # === errno ===
    "مستخدمون_كثيرون": "errno.EUSERS",
    # === enum ===
    "مستمر": "enum.CONTINUOUS",
    # === tty ===
    "مسح_محرف": "tty.CERASE",
    # === enum ===
    "مسمّى_علامات": "enum.NAMED_FLAGS",
    # === errno ===
    "مشغول": "errno.EBUSY",
    # === signal ===
    "معالجات_إشارة_افتراضي": "signal.Handlers.SIG_DFL",
    "معالجات_إشارة_تجاهل": "signal.Handlers.SIG_IGN",
    # === tty ===
    "معالجة_الإخراج": "tty.OPOST",
    "معالجة_خارجية": "tty.EXTPROC",
    # === errno ===
    "معامل_غير_صالح": "errno.EINVAL",
    # === typing ===
    "مفاتيح_عرض": "typing.KeysView",
    # === tty ===
    "مقاطعة_السطر": "tty.BRKINT",
    # === ctypes ===
    "مكتبة_cd": "ctypes.cdll",
    # === reprlib ===
    "مكتبة_التمثيل_أ_تمثيل": "reprlib.aRepr",
    # === typing ===
    "مكرّر": "typing.Iterator",
    # === stat ===
    "ملف_سمة_للقراءة_فقط": "stat.FILE_ATTRIBUTE_READONLY",
    "ملف_سمة_مخفي": "stat.FILE_ATTRIBUTE_HIDDEN",
    # === filecmp ===
    "ملف_قارن_حجم_المخزن": "filecmp.BUFSIZE",
    # === unittest ===
    "ملف_مواصفة": "unittest.mock.file_spec",
    # === errno ===
    "ملف_نصي_مشغول": "errno.ETXTBSY",
    "ملف_نط_سيئ": "errno.EBFONT",
    "ملفات_كثيرة": "errno.ENFILE",
    "ملفات_كثيرة_جداً": "errno.EMFILE",
    # === multiprocessing ===
    "مهمة_عدّاد": "multiprocessing.pool.job_counter",
    # === errno ===
    "موجود_بالفعل": "errno.EALREADY",
    # === typing ===
    "مولّد": "typing.Generator",
    # === multiprocessing ===
    "مُستمع_عميل": "multiprocessing.managers.listener_client",
    # === typing ===
    "مُعلَّق": "typing.Annotated",
    "مُقيّم": "typing.Sized",
    # === pydoc ===
    "نص_صريح": "pydoc.plaintext",
    # === select ===
    "نطاق_قراءة_إبول": "select.EPOLLRDBAND",
    "نطاق_قراءة_استطلاع": "select.POLLRDBAND",
    "نطاق_كتابة_إبول": "select.EPOLLWRBAND",
    # === errno ===
    "نظام_ملفات_للقراءة_فقط": "errno.EROFS",
    "نقاط_زائدة": "errno.EDOTDOT",
    # === tty ===
    "نهاية_سطر": "tty.CEOL",
    "نهاية_ملف": "tty.CEOF",
    "نهاية_نقل": "tty.CEOT",
    # === venv ===
    "نواة_بيئة_افتراضية_اعتماديات": "venv.CORE_VENV_DEPS",
    # === typing ===
    "نوع_اسم_مستعار": "typing.TypeAlias",
    # === errno ===
    "نوع_المقبس_غير_مدعوم": "errno.ESOCKTNOSUPPORT",
    "نوع_بروتوكول_خاطئ": "errno.EPROTOTYPE",
    # === typing ===
    "نوع_حارس": "typing.TypeGuard",
    "نوع_فحص": "typing.TYPE_CHECKING",
    "نوع_هو": "typing.TypeIs",
    # === errno ===
    "نوع_وسيط_خاطئ": "errno.EMEDIUMTYPE",
    "هو_اسم": "errno.EISNAM",
    # === ctypes ===
    "واجهة_بايثون": "ctypes.pythonapi",
    # === errno ===
    "واصف_سيئ": "errno.EBADF",
    # === fcntl ===
    "واصف_ملف_أغلق_عند_التنفيذ": "fcntl.FD_CLOEXEC",
    # === errno ===
    "واصف_ملف_سيئ": "errno.EBADE",
    # === mmap ===
    "وصول_افتراضي": "mmap.ACCESS_DEFAULT",
    "وصول_اقرأ": "mmap.ACCESS_READ",
    "وصول_اكتب": "mmap.ACCESS_WRITE",
    "وصول_انسخ": "mmap.ACCESS_COPY",
    # === unittest ===
    "يمين": "unittest.mock.right",
}


# --- الاسم الواحد يمرّ مرة واحدة ---
_SYS_TOKEN = re.compile(
    r"(?P<dot>\.)?"
    r"(?P<word>(?!\d)[\w\u064B-\u065F\u0670]+)"
    r"(?P<open>\s*\()?"
)

USER_NAMES = set()


def _sys_replace(match):
    dot = match.group("dot")
    word = match.group("word")
    open_paren = match.group("open")

    if word in USER_NAMES:
        return match.group(0)

    if dot:
        if open_paren and word in SYS_METHODS:
            return "." + SYS_METHODS[word] + open_paren
        if word in SYS_PROPS:
            return "." + SYS_PROPS[word]
        return match.group(0)

    if word in SYS_CONSTS:
        return SYS_CONSTS[word]
    if word in SYS_FUNCS:
        return SYS_FUNCS[word] + (open_paren or "")
    return match.group(0)


def SYS_SUBSTITUTE(text):
    """يترجم كلمات البيانات والملفات في نص واحد ويُرجع المترجم."""
    if not text:
        return text
    return _SYS_TOKEN.sub(_sys_replace, text)

IMPORT_NAME = "os"
IMPORT_MODULES = ["platform", "sysconfig", "site", "pkgutil", "runpy", "getopt", "signal", "select", "selectors", "resource", "errno", "mmap", "stat", "filecmp", "fileinput", "fcntl", "pty", "tty", "shlex", "cmd", "readline", "rlcompleter", "zipapp", "venv", "ensurepip", "types", "numbers", "abc", "copy", "copyreg", "contextlib", "contextvars", "graphlib", "dataclasses", "enum", "typing", "ctypes", "ctypes.wintypes", "multiprocessing", "multiprocessing.pool", "multiprocessing.managers", "multiprocessing.shared_memory", "multiprocessing.connection", "multiprocessing.synchronize", "concurrent.futures", "sched", "logging", "logging.handlers", "logging.config", "unittest", "unittest.mock", "unittest.loader", "unittest.runner", "unittest.case", "unittest.suite", "unittest.result", "pydoc", "reprlib", "difflib", "unicodedata", "stringprep", "io"]
IMPORT_CHECK = r"(?:platform|sysconfig|site|pkgutil|runpy|getopt|signal|select|selectors|resource|errno|mmap|stat|filecmp|fileinput|fcntl|pty|tty|shlex|cmd|readline|rlcompleter|zipapp|venv|ensurepip|types|numbers|abc|copy|copyreg|contextlib|contextvars|graphlib|dataclasses|enum|typing|ctypes|ctypes\.wintypes|multiprocessing|multiprocessing\.pool|multiprocessing\.managers|multiprocessing\.shared_memory|multiprocessing\.connection|multiprocessing\.synchronize|concurrent\.futures|sched|logging|logging\.handlers|logging\.config|unittest|unittest\.mock|unittest\.loader|unittest\.runner|unittest\.case|unittest\.suite|unittest\.result|pydoc|reprlib|difflib|unicodedata|stringprep|io)\."
IMPORT_STATEMENT = "import platform, sysconfig, site, pkgutil, runpy, getopt, signal, select, selectors, resource, errno, mmap, stat, filecmp, fileinput, fcntl, pty, tty, shlex, cmd, readline, rlcompleter, zipapp, venv, ensurepip, types, numbers, abc, copy, copyreg, contextlib, contextvars, graphlib, dataclasses, enum, typing, ctypes, ctypes.wintypes, multiprocessing, multiprocessing.pool, multiprocessing.managers, multiprocessing.shared_memory, multiprocessing.connection, multiprocessing.synchronize, concurrent.futures, sched, logging, logging.handlers, logging.config, unittest, unittest.mock, unittest.loader, unittest.runner, unittest.case, unittest.suite, unittest.result, pydoc, reprlib, difflib, unicodedata, stringprep, io"


SYS_HELP = [
    "# syslib — النظام والتشغيل والتشخيص (platform, signal, ctypes, unittest)",
    "منصة() / معمارية_الجهاز()        - معلومات النظام",
    "عيّن_معالج_الإشارة(إشارة, معالج)  - معالجة الإشارات",
    "بحث_نمطي(نمط)                  - بحث عن ملفات",
    "عملية(هدف, حجج) / مجموعة_عمليات() - عمليات متعددة",
    "احصل_على_مسجّل(اسم) / سجّل_معلومة - التسجيل",
    "حالة_اختبار / حزمة_اختبارات        - الاختبارات",
    "مكتبات_خارجية.مكتبة_ديناميكية    - ctypes",
    "متغير_سياق / مرتّب_توبولوجي        - سياق ورسوم",
    "اختر_عدة() / استطلع_الملفات        - اختيار الملفات",
]

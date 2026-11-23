# مكتبة العمليات الفرعية — `subprocess`

مكتبة subprocess الكاملة بالعربي، تشغيل أوامر النظام:

**74 عنصراً عربياً** (الدوال: 74).

## الدوال (74)

| العربي | Python |
|--------|--------|
| `أنشئ_عملية_أوامر` | `subprocess.run` |
| `عملية` | `subprocess.run` |
| `نفذ_أوامر` | `subprocess.run` |
| `شغل_أوامر` | `subprocess.run` |
| `Process` | `subprocess.Popen` |
| `أنشئ_Process` | `subprocess.Popen` |
| `حجة_أوامر` | `args` |
| `قشرة` | `shell` |
| `انتظر_أوامر` | `timeout` |
| `ترميز_أوامر` | `encoding` |
| `ترميز_خطأ` | `errors` |
| `مدخل` | `stdin` |
| `مخرج` | `stdout` |
| `خطأ_أوامر` | `stderr` |
| `دليل` | `cwd` |
| `متغيرات_بيئة` | `env` |
| `تجميع_مخرج` | `text` |
| `كائن_ثنائي` | `text` |
| `التقاط` | `capture_output` |
| `مدخل_نصي` | `input` |
| `اتصل_أوامر` | `process.communicate` |
| `أرسل` | `process.communicate` |
| `انتظر_إنهاء` | `process.wait` |
| `ألغى_أوامر` | `process.terminate` |
| `اقتل` | `process.kill` |
| `أرسل_إشارة` | `process.send_signal` |
| `إشارة_أوامر` | `process.send_signal` |
| `رمز_العودة` | `process.returncode` |
| `pid` | `process.pid` |
| `معرف` | `process.pid` |
| `SIGTERM` | `signal.SIGTERM` |
| `SIGKILL` | `signal.SIGKILL` |
| `SIGINT` | `signal.SIGINT` |
| `PIPE` | `subprocess.PIPE` |
| `STDOUT` | `subprocess.STDOUT` |
| `DEVNULL` | `subprocess.DEVNULL` |
| `CreationFlags` | `creationflags` |
| `ShowWindow` | `subprocess.SW_HIDE` |
| `تم_إنهاء` | `process.poll` |
| `انتهى` | `process.poll` |
| `نشط_أوامر` | `process.poll` |
| `CalledProcessError` | `subprocess.CalledProcessError` |
| `ExpiredTimeout` | `subprocess.TimeoutExpired` |
| `FileNotFoundError` | `FileNotFoundError` |
| `تحويل_أوامر` | `stderr_to_stdout` |
| `دمج` | `merge_outputs` |
| `universal_newlines` | `text` |
| `creationflags` | `creationflags` |
| `close_fds` | `close_fds` |
| `preexec_fn` | `preexec_fn` |
| `startupinfo` | `startupinfo` |
| `restore_signals` | `restore_signals` |
| `start_new_session` | `start_new_session` |
| `group` | `group` |
| `extra_groups` | `extra_groups` |
| `user` | `user` |
| `umask` | `umask` |
| `process_group` | `process_group` |
| `stdin` | `stdin` |
| `stdout` | `stdout` |
| `stderr` | `stderr` |
| `خرج_معياري_أوامر` | `stdout` |
| `خطأ_معياري_أوامر` | `stderr` |
| `دخرج_وخطأ` | `stdout_and_stderr` |
| `نجاح_أوامر` | `returncode == 0` |
| `فشل_أوامر` | `returncode != 0` |
| `رمز_نجاح` | `0` |
| `عمليات_فرعية` | `subprocess` |
| `Popen` | `subprocess.Popen` |
| `call` | `subprocess.call` |
| `check_call` | `subprocess.check_call` |
| `check_output` | `subprocess.check_output` |
| `getoutput` | `subprocess.getoutput` |
| `getstatusoutput` | `subprocess.getstatusoutput` |

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

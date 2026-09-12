"""
APL - Requests HTTP Library
Full HTTP client with Arabic keywords
"""

REQUESTS_FUNCS = {
    # === الطرق الأساسية (Basic Methods) ===
    "احصل_على": "requests.get",
    "أرسل_إلى": "requests.post",
    "ضع_في": "requests.put",
    "احذف": "requests.delete",
    "صحح": "requests.patch",
    "رأس": "requests.head",
    "خيارات": "requests.options",
    "اطلب": "requests.request",
    "طلب": "requests.request",
    "اتصل": "requests.Session",
    
    # === اختصارات (Shortcuts) ===
    "get": "requests.get",
    "post": "requests.post",
    "put": "requests.put",
    "delete": "requests.delete",
    "patch": "requests.patch",
    "head": "requests.head",
    "options": "requests.options",
    "request": "requests.request",
    "session": "requests.Session",
    
    # === GET requests ===
    "جيت": "requests.get",
    "جلب": "requests.get",
    "تنزيل": "requests.get",
    "download": "requests.get",
    "فتح": "requests.get",
    "visit": "requests.get",
    "تابع": "requests.get",
    "تصفح": "requests.get",
    "استعرض": "requests.get",
    "اقرأ": "requests.get",
    "فتش": "requests.get",
    "ابحث": "requests.get",
    "جد": "requests.get",
    "هات": "requests.get",
    
    # === POST requests ===
    "بوست": "requests.post",
    "ارسل": "requests.post",
    "أنزل": "requests.post",
    "رفع": "requests.post",
    "سجل": "requests.post",
    "احفظ": "requests.post",
    "ادخل": "requests.post",
    "اكتب": "requests.post",
    "نشر": "requests.post",
    "أعلن": "requests.post",
    "أضف": "requests.post",
    "ضمن": "requests.post",
    "حط": "requests.post",
    
    # === PUT requests ===
    "put": "requests.put",
    "غير": "requests.put",
    "عدل": "requests.put",
    "حدث": "requests.put",
    "بدل": "requests.put",
    "قلب": "requests.put",
    "تحول": "requests.put",
    "تحديث": "requests.put",
    "تعديل": "requests.put",
    "تبديل": "requests.put",
    
    # === DELETE requests ===
    "delete": "requests.delete",
    "امسح": "requests.delete",
    "شيل": "requests.delete",
    "الغي": "requests.delete",
    "انزع": "requests.delete",
    "اطرد": "requests.delete",
    "اقلع": "requests.delete",
    
    # === PATCH requests ===
    "patch": "requests.patch",
    "رمم": "requests.patch",
    "جبر": "requests.patch",
    "كمل": "requests.patch",
    
    # === Session ===
    "جلسة": "requests.Session",
    "اتصال": "requests.Session",
    "وصلة": "requests.Session",
    "رابطة": "requests.Session",
    
    # === الاستجابة (Response) ===
    "استجابة": "response",
    "رد": "response",
    "نتيجة": "response",
    "مخرجات": "response",
    "خرج": "response",
    
    # === محتوى الاستجابة (Response Content) ===
    "نص": "response.text",
    "نص_الاستجابة": "response.text",
    "محتوى": "response.content",
    "محتوى_الاستجابة": "response.content",
    "بايت": "response.content",
    "خام": "response.raw",
    "جسون": "response.json()",
    "بيانات_جسون": "response.json()",
    "html": "response.text",
    "صفحة": "response.text",
    "مصدر": "response.text",
    "كود": "response.text",
    
    # === حالة الاستجابة (Response Status) ===
    "حالة": "response.status_code",
    "رمز_الحالة": "response.status_code",
    "ناجح": "response.ok",
    "نجاح": "response.ok",
    "فشل": "response.status_code >= 400",
    "خطأ": "response.status_code >= 400",
    "غير_موجود": "response.status_code == 404",
    "ممنوع": "response.status_code == 403",
    "غير_مصرح": "response.status_code == 401",
    "توجيه": "response.is_redirect",
    "توجيه_دائم": "response.is_permanent_redirect",
    
    # === رؤوس الاستجابة (Response Headers) ===
    "رؤوس": "response.headers",
    "رأس": "response.headers.get",
    "نوع_المحتوى": "response.headers.get('Content-Type')",
    "طول_المحتوى": "response.headers.get('Content-Length')",
    "الترميز": "response.encoding",
    "زمن_الاستجابة": "response.elapsed",
    "رابط_الاستجابة": "response.url",
    "روابط_التوجيه": "response.history",
    "كوكيز": "response.cookies",
    
    # === ملفات تعريف الارتباط (Cookies) ===
    "كوكي": "response.cookies.get",
    "ضع_كوكي": "requests.cookies.set",
    "احذف_كوكي": "requests.cookies.clear",
    "مسح_كوكي": "requests.cookies.clear",
    
    # === روابط (URLs) ===
    "رابط_كامل": "response.url",
    "رابط_أساسي": "response.url.split('?')[0]",
    "رابط_توجيهي": "response.headers.get('Location')",
    "رابط_التالي": "response.headers.get('Location')",
    
    # === معاملات الطلب (Request Parameters) ===
    "معاملات": "params",
    "استعلام": "params",
    "بحث": "params",
    "فلتر": "params",
    "حد": "params",
    "صفحة": "params",
    "ترتيب": "params",
    
    # === بيانات الطلب (Request Data) ===
    "بيانات": "data",
    "نموذج": "data",
    "جسم": "json",
    "json_data": "json",
    "ملف": "files",
    "مرفقات": "files",
    
    # === رؤوس الطلب (Request Headers) ===
    "رؤوس_الطلب": "headers",
    "وكيل_المستخدم": "headers",
    "تفويض": "headers",
    "رمز": "headers",
    "مفتاح_ api": "headers",
    
    # === المهلة (Timeouts) ===
    "مهلة": "timeout",
    "انتظار": "timeout",
    "محاولة_جديدة": "retry",
    "أعد_المحاولة": "retry",
    "عدد_المحاولات": "max_retries",
    
    # === التحقق (Validation) ===
    "تحقق": "verify",
    "شهادة": "verify",
    "اسمح_التوجيه": "allow_redirects",
    "تابع_التوجيه": "allow_redirects",
    "بروكسي": "proxies",
    "وكيل": "proxies",
    
    # === المصادقة (Authentication) ===
    "مصادقة": "auth",
    "مستخدم": "auth",
    "كلمة_مرور": "auth",
    "مصادقة_أساسية": "HTTPBasicAuth",
    "مصادقة_ملخصة": "HTTPDigestAuth",
    
    # === الأخطاء (Errors) ===
    "خطأ_http": "requests.exceptions.HTTPError",
    "خطأ_اتصال": "requests.exceptions.ConnectionError",
    "انتهت_مهلة": "requests.exceptions.Timeout",
    "انتهت_مهلة_الاتصال": "requests.exceptions.ConnectTimeout",
    "انتهت_مهلة_القراءة": "requests.exceptions.ReadTimeout",
    "توجيهات_كثيرة": "requests.exceptions.TooManyRedirects",
    "رابط_غير_صالح": "requests.exceptions.InvalidURL",
    
    # === التخزين المؤقت (Caching) ===
    "كاش": "cache",
    "تخزين_مؤقت": "cache",
    "مسح_الكاش": "requests.cache.clear",
    "تعطيل_الكاش": "requests.cache.disabled",
    "تفعيل_الكاش": "requests.cache.enabled",
    
    # === الأداء (Performance) ===
    "مدة_الطلب": "response.elapsed.total_seconds",
    "سرعة_التنزيل": "len(response.content) / response.elapsed.total_seconds",
    
    # === التحميل (Downloads) ===
    "حمل": "requests.get",
    "حمل_ملف": "requests.get",
    "احفظ_ملف": "open",
    "تدفق": "stream",
    "محتوى_تدفقي": "response.iter_content",
    "حجم_القطعة": "chunk_size",
    
    # === الرفع (Uploads) ===
    "ارفع": "requests.post",
    "رفع_ملف": "requests.post",
    "متعدد_الأجزاء": "requests.post",
    
    # === الجلسات (Sessions) ===
    "افتح_جلسة": "requests.Session",
    "أغلق_جلسة": "session.close",
    "جلسة_جيت": "session.get",
    "جلسة_بوست": "session.post",
    "جلسة_حذف": "session.delete",
    
    # === التصفح (Pagination) ===
    "تصفح": "params",
    "صفحة_تالية": "response.links.get('next')",
    "صفحة_سابقة": "response.links.get('prev')",
    "صفحة_أولى": "response.links.get('first')",
    "صفحة_أخيرة": "response.links.get('last')",
    "رقم_الصفحة": "params.get('page')",
    "حجم_الصفحة": "params.get('per_page')",
    "إجمالي_الصفحات": "response.headers.get('X-Total-Pages')",
    "إجمالي_العناصر": "response.headers.get('X-Total-Count')",
    
    # === الفلترة (Filtering) ===
    "فلتر": "params",
    "حيث": "params",
    "يساوي": "params",
    "أكبر_من": "params",
    "أصغر_من": "params",
    "مثل": "params",
    "في": "params",
    "بين": "params",
    "فارغ": "params",
    "غير_فارغ": "params",
    
    # === الترتيب (Sorting) ===
    "رتب_حسب": "params",
    "ترتيب_حسب": "params",
    "تصاعدي": "params",
    "تنازلي": "params",
    "أحدث": "params",
    "أقدم": "params",
    
    # === الحقول (Fields) ===
    "حقول": "params",
    "اختر": "params",
    "أدرج": "params",
    "استبعد": "params",
    "عدد": "params",
    "مجموع": "params",
    "متوسط": "params",
    "أدنى": "params",
    "أعلى": "params",
    
    # === الأمان (Security) ===
    "آمن": "verify=True",
    "غير_آمن": "verify=False",
    "تحقق_ssl": "verify",
    "شهادة_عميل": "cert",
    "مفتاح_عميل": "cert",
    "حزمة_ca": "verify",
    
    # === البروكسي (Proxy) ===
    "استخدم_بروكسي": "proxies",
    "بروكسي_http": "proxies",
    "بروكسي_https": "proxies",
    "بروكسي_socks5": "proxies",
    "بدون_بروكسي": "proxies",
    
    # === الضغط (Compression) ===
    "ضغط_gzip": "headers",
    "قبول_الضغط": "headers",
    "فك_الضغط": "response.content",
    
    # === الترميز (Encoding) ===
    "ضع_الترميز": "response.encoding",
    "ترميز_ظاهري": "response.apparent_encoding",
    "ترميز_utf8": "response.encoding = 'utf-8'",
    
    # === التخزين المؤقت HTTP (HTTP Caching) ===
    "etag_الرد": "response.headers.get('ETag')",
    "آخر_تعديل": "response.headers.get('Last-Modified')",
    "تحكم_التخزين": "response.headers.get('Cache-Control')",
    "انتهاء": "response.headers.get('Expires')",
    
    # === الأمان المتقدم (Advanced Security) ===
    "رمز_csrf": "headers",
    "خيارات_الإطار": "headers",
    "أمان_النقل_الصارم": "headers",
    "سياسة_أمان_المحتوى": "headers",
    
    # === الوكيل (User Agent) ===
    "وكيل_المستخدم": "headers",
    "متصفح": "headers",
    "هاتف": "headers",
    "سطح_مكتب": "headers",
    "كروم": "headers",
    "فايرفوكس": "headers",
    "سفاري": "headers",
    "روبوت": "headers",
    
    # === اللغة (Language) ===
    "قبول_اللغة": "headers",
    "العربية": "headers",
    "الإنجليزية": "headers",
    "الفرنسية": "headers",
    
    # === القبول (Accept) ===
    "قبول_جسون": "headers",
    "قبول_html": "headers",
    "قبول_xml": "headers",
    "قبول_نص": "headers",
    "قبول_الكل": "headers",
    
    # === التتبع (Tracing) ===
    "معرف_الطلب": "response.headers.get('X-Request-Id')",
    "معرف_الارتباط": "response.headers.get('X-Correlation-Id')",
    "معرف_التتبع": "response.headers.get('X-Trace-Id')",
}

REQUESTS_PATTERN = r"(?<!\w)(" + "|".join(sorted(REQUESTS_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

REQUESTS_HELP = [
    "# === الطرق الأساسية ===",
    "احصل_على(رابط)          - GET request",
    "أرسل_إلى(رابط, بيانات)  - POST request",
    "ضع_في(رابط, بيانات)     - PUT request",
    "احذف(رابط)               - DELETE request",
    "صحح(رابط, بيانات)       - PATCH request",
    "# === اختصارات ===",
    "get(رابط)                - GET (مختصر)",
    "post(رابط)               - POST (مختصر)",
    "put(رابط)                - PUT (مختصر)",
    "delete(رابط)             - DELETE (مختصر)",
    "جيت(رابط)                - GET (عربي)",
    "بوست(رابط)               - POST (عربي)",
    "# === الاستجابة ===",
    "نص                       - response.text",
    "محتوى                    - response.content",
    "جسون()                   - response.json()",
    "حالة                     - response.status_code",
    "ناجح                     - response.ok",
    "رؤوس                     - response.headers",
    "كوكيز                   - response.cookies",
    "# === الأمان ===",
    "مصادقة                   - auth",
    "مهلة                     - timeout",
    "تحقق                     - verify (SSL)",
    "بروكسي                   - proxies",
    "# === الجلسات ===",
    "جلسة()                   - requests.Session()",
    "جلسة_جيت(رابط)          - session.get()",
    "جلسة_بوست(رابط)         - session.post()",
]

IMPORT_NAME = "requests"
IMPORT_CHECK = "requests\."
IMPORT_STATEMENT = "import requests"

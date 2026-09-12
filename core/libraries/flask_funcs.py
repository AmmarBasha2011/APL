"""
APL - Flask Web Framework Library
Full Flask wrapper with Arabic keywords
Note: Remove duplicates with json_funcs (جسون, جسون_تحويل)
"""

FLASK_FUNCS = {
    # إنشاء التطبيق (App Creation)
    "تطبيق_فلاسك": "Flask",
    "فلاسك": "Flask",
    "خدمة_ويب": "Flask",
    
    # المسارات (Routing)
    "مسار_فلاسك": "@app.route",
    "متحكم": "@app.route",
    
    # تشغيل (Running)
    "شغل": "app.run",
    "شغل_خدمة": "app.run",
    "استمع": "app.run",
    "ابدأ": "app.run",
    
    # الطلب (Request)
    "طلب": "request",
    "طلب_جيت": "request.args",
    "طلب_نموذج": "request.form",
    "طلب_ملف": "request.files",
    "طلب_رأس": "request.headers",
    "طلب_كوكي": "request.cookies",
    "طلب_جلسة": "session",
    "طلب_طريقة": "request.method",
    "طلب_مسار": "request.path",
    "طلب_عنوان": "request.url",
    "طلب_أي_بي": "request.remote_addr",
    
    # الاستجابة (Response)
    "استجابة": "make_response",
    "استجابة_نص": "make_response",
    "استجابة_جسون": "jsonify",
    "جسونيا": "jsonify",
    
    # إعادة توجيه (Redirect)
    "حول": "redirect",
    "إعادة_توجيه": "redirect",
    "رابط_دائم": "url_for",
    "بناء_رابط": "url_for",
    
    # القوالب (Templates)
    "عرض": "render_template",
    "قالب": "render_template",
    "عرض_قالب": "render_template",
    
    # الأخطاء (Errors)
    "خطأ": "abort",
    "خطأ_400": "abort",
    "خطأ_401": "abort",
    "خطأ_403": "abort",
    "خطأ_404": "abort",
    "خطأ_500": "abort",
    "إحباط": "abort",
    "معالج_خطأ": "app.errorhandler",
    "معالج_استثناء": "app.errorhandler",
    
    # الجلسة (Session)
    "جلسة": "session",
    "ضع_جلسة": "session.__setitem__",
    "احذف_جلسة": "session.pop",
    
    # رفع الملفات (File Upload)
    "احفظ_ملف": "file.save",
    "ملف_آمن": "secure_filename",
    "اسم_آمن": "secure_filename",
    
    # التخزين المؤقت (Caching)
    "ذاكرة_مؤقتة": "after_request",
    "قبل_طلب": "before_request",
    "بعد_طلب": "after_request",
    "وسطاء": "before_request",
    
    # التكوين (Config)
    "ضبط": "app.config.update",
    "ضع_تكوين": "app.config.__setitem__",
    "وضع_تصحيح": "app.debug",
    "مفتاح_سري": "app.secret_key",
    
    # قاعدة البيانات (Database - SQLAlchemy patterns)
    "قاعدة": "db",
    "جدول": "db.Model",
    "نموذج_قاعدة": "db.Model",
    "استعلام": "db.session.query",
    "نفذ": "db.session.commit",
    "أضف": "db.session.add",
    "احذف_سجل": "db.session.delete",
    "تراجع": "db.session.rollback",
    "هجرة": "db.create_all",
    
    # المصادقة (Auth patterns)
    "سجل_دخول": "login_user",
    "سجل_خروج": "logout_user",
    "المستخدم_الحالي": "current_user",
    "محمي": "login_required",
    "تأكد_دخول": "login_required",
    "تحقق_من": "check_password_hash",
    "شفر_كلمة": "generate_password_hash",
    
    # الاختبار (Testing)
    "اختبار_عميل": "app.test_client",
    "عميل": "app.test_client",
    
    # أنماط الـ API (API Patterns)
    "api_مسار": "api.add_resource",
    "مورد": "Resource",
    "تحقق_من_بيانات": "request.get_json",
    "احصل_على_جسون": "request.get_json",
    "تأكد_نوع": "request.is_json",
}

FLASK_PATTERN = r"(?<!\w)(" + "|".join(sorted(FLASK_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
FLASK_HELP = [
    "# === إنشاء التطبيق ===",
    "فلاسك(اسم)             - إنشاء تطبيق Flask",
    "خدمة_ويب(اسم)          - إنشاء تطبيق ويب",
    "# === المسارات ===",
    "مسار_فلاسك('/path')     - إضافة مسار (GET افتراضي)",
    "متحكم('/path')          - متحكم بالمسار",
    "# === تشغيل الخادم ===",
    "شغل(منفذ, تصحيح)       - تشغيل الخادم",
    "استمع(المنفذ)           - الاستماع على منفذ",
    "# === التعامل مع الطلب ===",
    "طلب                       - كائن الطلب",
    "طلب_جيت('مفتاح')        - معاملات GET",
    "طلب_نموذج('حقل')        - بيانات النموذج",
    "طلب_ملف('اسم')          - ملف مرفوع",
    "# === الاستجابة ===",
    "استجابة(نص)            - إنشاء استجابة",
    "جسونيا(بيانات)         - استجابة JSON",
    "# === إعادة التوجيه ===",
    "حول('/path')             - إعادة توجيه",
    "# === القوالب ===",
    "عرض('قالب.html')       - عرض قالب",
    "قالب('قالب.html', **ctx) - عرض قالب مع بيانات",
    "# === الجلسة ===",
    "جلسة                     - كائن الجلسة",
    "# === الأخطاء ===",
    "خطأ(رمز)               - إطلاق خطأ",
    "خطأ_404()               - خطأ Not Found",
]

IMPORT_NAME = "flask"
IMPORT_CHECK = "flask\."
IMPORT_STATEMENT = "from flask import Flask, request, jsonify, render_template, redirect, url_for, abort, session, make_response"

# مكتبة Flask — إطار عمل ويب بالعربي

مكتبة Flask الكاملة بالعربي، إطار عمل ويب:

**78 عنصراً عربياً** (الدوال: 78).

## الدوال (78)

| العربي | Python |
|--------|--------|
| `تطبيق_فلاسك` | `Flask` |
| `فلاسك` | `Flask` |
| `خدمة_ويب` | `Flask` |
| `مسار_فلاسك` | `@app.route` |
| `متحكم` | `@app.route` |
| `سجل_أضف` | `current_app.db.session.add` |
| `شغل` | `app.run` |
| `شغل_خدمة` | `app.run` |
| `استمع` | `app.run` |
| `ابدأ` | `app.run` |
| `طلب_فلاسك` | `request` |
| `طلب_جيت` | `request.args` |
| `طلب_نموذج` | `request.form` |
| `طلب_ملف` | `request.files` |
| `طلب_رأس` | `request.headers` |
| `طلب_كوكي` | `request.cookies` |
| `طلب_جلسة` | `session` |
| `طلب_طريقة` | `request.method` |
| `طلب_مسار` | `request.path` |
| `طلب_عنوان` | `request.url` |
| `طلب_أي_بي` | `request.remote_addr` |
| `استجابة` | `make_response` |
| `استجابة_نص` | `make_response` |
| `استجابة_جسون` | `jsonify` |
| `جسونيا` | `jsonify` |
| `حول` | `redirect` |
| `إعادة_توجيه` | `redirect` |
| `رابط_دائم` | `url_for` |
| `بناء_رابط` | `url_for` |
| `عرض` | `render_template` |
| `قالب` | `render_template` |
| `عرض_قالب` | `render_template` |
| `خطأ` | `abort` |
| `خطأ_400` | `abort` |
| `خطأ_401` | `abort` |
| `خطأ_403` | `abort` |
| `خطأ_404` | `abort` |
| `خطأ_500` | `abort` |
| `إحباط` | `abort` |
| `معالج_خطأ` | `app.errorhandler` |
| `معالج_استثناء` | `app.errorhandler` |
| `جلسة` | `session` |
| `ضع_جلسة` | `session.__setitem__` |
| `احذف_جلسة` | `session.pop` |
| `احفظ_ملف` | `file.save` |
| `ملف_آمن` | `secure_filename` |
| `اسم_آمن` | `secure_filename` |
| `ذاكرة_مؤقتة` | `after_request` |
| `قبل_طلب` | `before_request` |
| `بعد_طلب` | `after_request` |
| `وسطاء` | `before_request` |
| `ضبط` | `app.config.update` |
| `ضع_تكوين` | `app.config.__setitem__` |
| `وضع_تصحيح` | `app.debug` |
| `مفتاح_سري` | `app.secret_key` |
| `قاعدة_فلاسك` | `db` |
| `جدول` | `_apl_flask_db.Model` |
| `نموذج_قاعدة` | `_apl_flask_db.Model` |
| `استعلام` | `_apl_db.session.query` |
| `نفذ_فلاسك` | `_apl_db.session.commit` |
| `أضف_فلاسك` | `_apl_db.session.add` |
| `احذف_سجل` | `_apl_db.session.delete` |
| `تراجع_فلاسك` | `_apl_db.session.rollback` |
| `هجرة` | `_apl_db.create_all` |
| `سجل_دخول` | `login_user` |
| `سجل_خروج` | `logout_user` |
| `المستخدم_الحالي` | `current_user` |
| `محمي` | `login_required` |
| `تأكد_دخول` | `login_required` |
| `تحقق_من` | `check_password_hash` |
| `شفر_كلمة` | `generate_password_hash` |
| `اختبار_عميل` | `app.test_client` |
| `عميل` | `app.test_client` |
| `api_مسار` | `api.add_resource` |
| `مورد` | `Resource` |
| `تحقق_من_بيانات` | `request.get_json` |
| `احصل_على_جسون` | `request.get_json` |
| `تأكد_نوع` | `request.is_json` |

## مثال

```apl
المتغير app = فلاسك("تطبيقي")

@مسار_فلاسك("/")
دالة_رئيسية():
    ارجع "مرحباً من فلاسك"

@مسار_فلاسك("/api/بيانات")
دالة_api_بيانات():
    ارجع استجابة_جسون({"رسالة": "مرحباً"})

اطبع [قاعدة.rule for قاعدة in app.url_map.iter_rules()]
```

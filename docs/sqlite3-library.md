# مكتبة قواعد البيانات — `sqlite3`

مكتبة SQLite3 الكاملة بالعربي، قاعدة بيانات محلية:

**24 عنصراً عربياً** (الدوال: 10، دوال الكائنات: 14).

## الدوال (10)

| العربي | Python |
|--------|--------|
| `افتح_قاعدة` | `sqlite3.connect` |
| `افتح_قاعدة_بيانات` | `sqlite3.connect` |
| `اتصل_قاعدة` | `sqlite3.connect` |
| `قاعدة` | `sqlite3.connect` |
| `مؤشر` | `cursor` |
| `أنشئ_مؤشر` | `connection.cursor` |
| `صف_مصنع` | `connection.row_factory` |
| `نص_مصنع` | `connection.text_factory` |
| `عزل_مستوى` | `connection.isolation_level` |
| `نسخ_احتياطي` | `sqlite3.connect` |

## دوال الكائنات (14) — `SQLITE3_METHODS`

| العربي | Python |
|--------|--------|
| `مؤشر` | `cursor` |
| `نفذ` | `execute` |
| `نفذ_استعلام` | `execute` |
| `نفذ_كثير` | `executemany` |
| `نفذ_سكريبت` | `executescript` |
| `جلب_واحد` | `fetchone` |
| `جلب_الكل` | `fetchall` |
| `جلب_عدد` | `fetchmany` |
| `أغلق_مؤشر` | `close` |
| `تأكد` | `commit` |
| `احفظ_قاعدة` | `commit` |
| `تراجع` | `rollback` |
| `أغلق_قاعدة` | `close` |
| `أغلق_اتصال` | `close` |

## مثال

```apl
# إنشاء قاعدة بيانات
المتغير اتصال = افتح_قاعدة("_تجربة.db")
المتغير مؤشر_ج = اتصال.cursor()

# إنشاء جدول
مؤشر_ج.نفذ("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# إدراج بيانات
مؤشر_ج.نفذ("INSERT INTO users (name, age) VALUES (?, ?)", ("عمار", 25))
مؤشر_ج.نفذ("INSERT INTO users (name, age) VALUES (?, ?)", ("محمد", 30))

# تأكيد
اتصال.تأكد()

# استعلام
مؤشر_ج.نفذ("SELECT name, age FROM users")
المتغير صفوف = مؤشر_ج.جلب_الكل()
لكل صف في صفوف:
    اطبع صف

# إغلاق
اتصال.أغلق_قاعدة()
احذف_ملف("_تجربة.db")
```

# مكتبة المسارات — `pathlib`

التعامل مع مسارات نظام الملفات ككائنات بدلاً من نصوص.

**61 عنصراً عربياً** (الدوال: 31، دوال الكائنات: 21، الخصائص: 7، المعاملات المسماة: 2).

## الدوال (31)

| العربي | Python |
|--------|--------|
| `مسار_جديد` | `pathlib.Path` |
| `درب` | `pathlib.Path` |
| `أنشئ_مسار` | `pathlib.Path` |
| `المسار_الحالي` | `pathlib.Path.cwd` |
| `المسار_المنزل` | `pathlib.Path.home` |
| `مسار_ادمج` | `pathlib.Path.joinpath` |
| `مسار_نص` | `pathlib.Path.as_posix` |
| `مسار_مطلق_كامل` | `pathlib.Path.resolve` |
| `مسار_نسبي_كامل` | `pathlib.Path.absolute` |
| `مسار_موجود` | `_apl_path_exists` |
| `مسار_هو_مجلد` | `pathlib.Path.is_dir` |
| `مسار_هو_ملف` | `pathlib.Path.is_file` |
| `مسار_رابط_رمزي` | `pathlib.Path.is_symlink` |
| `مسار_إحصاء` | `pathlib.Path.stat` |
| `مسار_لمس` | `pathlib.Path.touch` |
| `مسار_فتح` | `pathlib.Path.open` |
| `مسار_اقرأ` | `pathlib.Path.read_text` |
| `مسار_اكتب` | `pathlib.Path.write_text` |
| `مسار_اقرأ_ثنائي` | `pathlib.Path.read_bytes` |
| `مسار_اكتب_ثنائي` | `pathlib.Path.write_bytes` |
| `مسار_ابحث` | `pathlib.Path.glob` |
| `مسار_ابحث_الكل` | `pathlib.Path.rglob` |
| `مسار_إعادة_تسمية` | `pathlib.Path.rename` |
| `مسار_استبدال` | `pathlib.Path.replace` |
| `مسار_محتويات` | `pathlib.Path.iterdir` |
| `مسار_أنشئ_مجلد` | `pathlib.Path.mkdir` |
| `أنشئ_مجلد_مسار` | `pathlib.Path.mkdir` |
| `مسار_احذف` | `pathlib.Path.unlink` |
| `مسار_احذف_مجلد` | `pathlib.Path.rmdir` |
| `مسار_نفسه` | `pathlib.Path.samefile` |
| `مسار_أنشئ_رابط` | `pathlib.Path.symlink_to` |

## دوال الكائنات (21) — `PATHLIB_METHODS`

| العربي | Python |
|--------|--------|
| `ادمج` | `joinpath` |
| `نص_له` | `as_posix` |
| `مطلق_له` | `resolve` |
| `نسبي_له` | `absolute` |
| `موجود_له` | `exists` |
| `هو_مجلد_له` | `is_dir` |
| `هو_ملف_له` | `is_file` |
| `اقرأ_له` | `read_text` |
| `اكتب_له` | `write_text` |
| `افتح_له` | `open` |
| `لمس_له` | `touch` |
| `ابحث_له` | `glob` |
| `محتويات_له` | `iterdir` |
| `أعد_تسمية_له` | `rename` |
| `استبدل_له` | `replace` |
| `إحصاء_له` | `stat` |
| `اسم_له` | `name` |
| `امتداد_له` | `suffix` |
| `بدون_امتداد_له` | `stem` |
| `أبوين_له` | `parent` |
| `أجزاء_له` | `parts` |

## الخصائص (7) — `PATHLIB_PROPS`

| العربي | Python |
|--------|--------|
| `مسار_اسم` | `name` |
| `مسار_بدون_امتداد` | `stem` |
| `مسار_امتداد` | `suffix` |
| `مسار_امتدادات` | `suffixes` |
| `مسار_أبوين` | `parent` |
| `مسار_أصول` | `parents` |
| `مسار_أجزاء` | `parts` |

## المعاملات المسماة (2) — `PATHLIB_KWARGS`

| العربي | Python |
|--------|--------|
| `آباء` | `parents` |
| `موجود_سلفا` | `exist_ok` |

## مثال

```apl
المتغير مس = مسار_جديد("docs").ادمج("README.md")
اطبع "المسار:", مسار_نص(مس)
اطبع "موجود:", مسار_موجود(مس)
اطبع "الاسم:", مس.مسار_اسم
اطبع "الامتداد:", مس.مسار_امتداد

# قراءة وكتابة
مسار_اكتب(مسار_جديد("ملف.txt"), "محتوى")
اطبع مسار_اقرأ(مسار_جديد("ملف.txt"))

# البحث عن ملفات
لكل ملف في مسار_ابحث(مسار_جديد("."), "*.py"):
    اطبع ملف.مسار_اسم
```

# مثال 145 — ملفات الإعدادات
# Config files with configparser
# Demonstrates: مُكوِّن_إعدادات، read_string، sections، get
#
# Run:  python apl.py examples/145-configparser-settings.apl

المتغير نص = "[app]\nname = APL\nversion = 1.13\n[ui]\ndark = true\n"

المتغير م = مُكوِّن_إعدادات()
م.read_string(نص)
اطبع "الأقسام:", م.sections()
اطبع "اسم التطبيق:", م.get("app", "name")
اطبع "الإصدار:", م.get("app", "version")
اطبع "الوضع الداكن:", م.getboolean("ui", "dark")
اطبع "يوجد قسم db؟", م.has_section("db")

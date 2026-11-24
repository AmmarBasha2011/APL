# مثال 470 — تحويل خصائص إلى JSON
# Properties to JSON
# Demonstrates: key=value إلى قاموس
#
# Run:  python apl.py examples/470-properties-convert.apl

اكتب("/tmp/apl-470.properties", "name=APL\nversion=1.0\nlang=arabic")

المتغير خصائص = {}
المتغير سطور = اقرأ("/tmp/apl-470.properties").تقليم().تقسيم("\n")
لكل سطر في سطور:
    المتغير أجزاء = سطر.تقسيم("=")
    خصائص[أجزاء[0]] = أجزاء[1]

اكتب_ملف_جسون(خصائص, "/tmp/apl-470.json")
اطبع "JSON محفوظ:", اقرأ_ملف_جسون("/tmp/apl-470.json")

احذف_ملف("/tmp/apl-470.properties")
احذف_ملف("/tmp/apl-470.json")

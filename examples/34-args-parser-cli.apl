# مثال 34 — محلل وسائط سطر الأوامر
# Command Line Argument Parser
# Demonstrates: argparse library, argument parsing, namespaces
#
# Run:  python apl.py examples/34-args-parser-cli.apl

المتغير محلي = محلل_وسائط()
محلل_أضف_حجة(محلي, "-v", "--verbose", action="store_true", help="وضع تفصيلي")
محلل_أضف_حجة(محلي, "-o", "--output", default="output.txt", help="ملف الإخراج")
محلل_أضف_قيمة(محلي, "input", help="ملف الإدخال")

المتغير الخيارات = محلل_حلل(محلي, ["-v", "-o", "out.txt", "data.csv"])

اطبع "=== محلل وسائط سطر الأوامر ==="
اطبع ""
اطبع "--- بعد تحليل الوسائط ---"
اطبع "  verbose : " + نص(الخيارات.verbose)
اطبع "  output  : " + الخيارات.output
اطبع "  input   : " + الخيارات.input
اطبع ""
اطبع "--- بدون وسائط (القيم الافتراضية) ---"
المتغير افتراضي = محلل_حلل(محلي, ["ملف.txt"])
اطبع "  verbose : " + نص(افتراضي.verbose)
اطبع "  output  : " + افتراضي.output
اطبع "  input   : " + افتراضي.input

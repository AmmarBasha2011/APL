# مثال 114 — قوالب النصوص
# String templates
# Demonstrates: قالب_نص، substitute
#
# Run:  python apl.py examples/114-string-template.apl

المتغير قالب = قالب_نص("أهلاً $name، رصيدك الحالي $balance جنيه.")
اطبع قالب.substitute(name="عمار", balance=1500)
اطبع قالب.substitute(name="سارة", balance=2300)

اطبع ""
المتغير قالب_بريد = قالب_نص("الموضوع: $subject\nالمرسل: $sender\nالأولوية: $priority")
اطبع قالب_بريد.substitute(subject="اجتماع مهم", sender="المدير", priority="عالية")

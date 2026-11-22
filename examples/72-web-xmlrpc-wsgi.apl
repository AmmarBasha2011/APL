# مثال 72 — XML-RPC وWSGI (مكتبة web)
# XML-RPC marshalling and WSGI headers (xmlrpc.client / wsgiref)
#
# Run:  python apl.py examples/72-web-xmlrpc-wsgi.apl

اطبع "=== تجميع نداء XML-RPC ==="
المتغير حجة = (1, "نص", {"مفتاح": True})
المتغير مُجمّع = أفرغ_XMLRPC(حجة)
اطبع "النوع:", نوع(مُجمّع)
اطبع "يبدأ بـ:", مُجمّع[0:6]

اطبع ""
اطبع "=== فك التجميع ==="
المتغير مفكوك = حمّل_XMLRPC(مُجمّع)
المتغير معاملات = مفكوك[0]
اطبع "العدد:", معاملات[0]
اطبع "النص:", معاملات[1]
اطبع "القاموس:", معاملات[2]
اطبع "اسم الدالة:", مفكوك[1]

اطبع ""
اطبع "=== رؤوس WSGI ==="
المتغير رؤوس = رؤوس_WSGI()
رؤوس.رؤوس_أضف_رأس("Content-Type", "text/plain; charset=utf-8")
رؤوس.رؤوس_أضف_رأس("Content-Length", "42")
اطبع "Content-Type:", رؤوس.رؤوس_احصل("Content-Type")
اطبع "Content-Length:", رؤوس.رؤوس_احصل("Content-Length")

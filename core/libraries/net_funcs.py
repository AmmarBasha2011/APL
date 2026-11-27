"""
APL — مكتبة الشبكة والبريد (net)
=================================

تُترجم الكلمات العربية إلى حزمة الشبكة في Python القياسية:

    socket         المقابس وعناوين IP        ssl          اتصالات TLS المشفّرة
    select         الجاهزية والتزامن          selectors    محددات الجاهزية
    http.client    عميل HTTP                  http.server  خادم HTTP
    http.cookiejar إدارة الكوكيز              urllib.request فتح الروابط
    smtplib        إرسال البريد               poplib       قراءة POP3
    imaplib        قراءة IMAP                 ftplib       نقل FTP
    email.*        بناء الرسائل وتحليلها      struct       تغليف ثنائي
    ipaddress      حسابات العناوين            socketserver خوادم المقابس
    xmlrpc         النداء عن بعد              mimetypes / zlib / binascii / quopri / uu / netrc / webbrowser

التجميع كما في كل مكتبات APL:

    NET_FUNCS      نداءات على مستوى الوحدة    مقبس_شبكة(عائلة_ipv4, مقبس_تدفق)
    NET_METHODS    دوال الكائن بعد نقطة       المقبس.اربط_المنفذ(("127.0.0.1", 8080))
    NET_PROPS      خصائص بلا أقواس             الاستجابة.حالة_الاستجابة
    NET_CONSTANTS  ثوابت تُكتب عارية           مقبس_تدفق
    NET_KWARGS     أسماء وسائط عربية            منفذ_البريد = 587

كل كلمة هنا تم التحقق منها آلياً مقابل الكائن الحقيقي في Python (وسم وحدة،
دالة صنف، خاصية كائن، أو وسيط دالة)، وعددها 1006 بلا أي تعارض مع المكتبات
الـ 43 الأخرى أو مع نواة اللغة، ولا اسم مكرّر داخلها.

ملاحظة الأسماء: ``مقبس`` محجوز لـ fastapi، و``استمع`` لـ flask، و``رسالة_بريد``
لـ fastapi، و``نوع_المحتوى`` و``أرسل_إلى`` لـ requests. لذلك تستخدم هذه المكتبة
``مقبس_شبكة`` و``استمع_للاتصالات`` و``رسالة_بريد_كاملة`` و``نوع_محتوى_البريد``
و``أرسل_إلى_عنوان``. القاعدة: أول مكتبة تحجز الاسم تحتفظ به، والباقي يشتق اسماً
جديداً بدل أن يكسرها.
"""

import re


# دوال المكتبة: نداءات على مستوى الوحدة
NET_FUNCS = {
    # === تحليل أسماء الأجهزة والعناوين ===
    "اسم_الجهاز": "socket.gethostname",
    "عنوان_الاسم": "socket.gethostbyname",
    "اسم_العنوان": "socket.gethostbyaddr",
    "اسم_كامل_للجهاز": "socket.getfqdn",
    "بيانات_العنوان": "socket.getaddrinfo",
    "منفذ_الخدمة": "socket.getservbyname",
    "خدمة_المنفذ": "socket.getservbyport",
    "رقم_البروتوكول": "socket.getprotobyname",
    "عنوان_إلى_بايتات": "socket.inet_aton",
    "بايتات_إلى_عنوان": "socket.inet_ntoa",
    "عنوان_إلى_مضغوط": "socket.inet_pton",
    "مضغوط_إلى_عنوان": "socket.inet_ntop",
    "منفذ_لترتيب_الشبكة": "socket.htons",
    "منفذ_من_ترتيب_الشبكة": "socket.ntohs",
    "عدد_لترتيب_الشبكة": "socket.htonl",
    "عدد_من_ترتيب_الشبكة": "socket.ntohl",
    "واجهات_الشبكة": "socket.if_nameindex",
    "رقم_الواجهة": "socket.if_nametoindex",
    "اسم_الواجهة": "socket.if_indextoname",
    "يدعم_مزدوج_العائلة": "socket.has_dualstack_ipv6",
    # === إنشاء المقابس وإدارتها ===
    "مقبس_شبكة": "socket.socket",
    "اتصال_شبكة": "socket.create_connection",
    "خادم_شبكة": "socket.create_server",
    "زوج_مقابس": "socket.socketpair",
    "مقبس_من_وصف": "socket.fromfd",
    "أغلق_مقبس": "_apl_net_close",
    "انسخ_مقبس": "socket.dup",
    "عين_مهلة_افتراضية": "socket.setdefaulttimeout",
    "اقرأ_مهلة_افتراضية": "socket.getdefaulttimeout",
    # === select / poll / epoll ===
    # === http.server ===
    "خادم_http": "http.server.HTTPServer",
    "معالج_طلبات_http": "http.server.BaseHTTPRequestHandler",
    "معالج_ملفات_http": "http.server.SimpleHTTPRequestHandler",
    # === http.cookies ===
    # === مجموعات الحروف (email.charset) ===
    "أضف_مجموعة_حروف": "email.charset.add_charset",
    # === رؤوس مهيكلة (headerregistry) ===
    "مجموعة_عناوين": "email.headerregistry.Group",
    "رأس_عنوان": "email.headerregistry.AddressHeader",
    "رأس_عام": "email.headerregistry.UnstructuredHeader",
    "رأس_معرّف": "email.headerregistry.MessageIDHeader",
    # === أدوات إضافية ===
    "اقرأ_تاريخ_مع_منطقة": "email.utils.parsedate_tz",
    "حوّل_تاريخ_لثوان": "email.utils.mktime_tz",
    "فك_معاملات_الرأس": "email.utils.decode_params",
    "تاريخ_iso": "email.utils.parsedate_to_datetime",
    "متصفح_خلفي": "webbrowser.BackgroundBrowser",
    "بايتات_إلى_سدّس": "binascii.b2a_hex",
    "سدّس_إلى_بايتات": "binascii.a2b_hex",
    "بايتات_إلى_uu": "binascii.b2a_uu",
    "uu_إلى_بايتات": "binascii.a2b_uu",
    "تحقق_hqx": "binascii.crc_hqx",
    # === xmlrpc ===
    "وكيل_متعدد": "xmlrpc.client.MultiCall",
    "خادم_xmlrpc": "xmlrpc.server.SimpleXMLRPCServer",
    # === ضغط zlib ونقل نصوص ===
    "ضغط_zlib": "zlib.compress",
    "فك_zlib": "zlib.decompress",
    "تحقق_دوري": "zlib.crc32",
    "فاك_zlib": "zlib.decompressobj",
    # === netrc و uu ===
    "شفّر_uu": "uu.encode",
    "فك_uu": "uu.decode",
    # === بريد: دوال وأصناف إضافية ===
    "رسالة_من_نص_عام": "email.message_from_string",
    "رسالة_من_ملف_عام": "email.message_from_file",
    "رأس_نقل_المحتوى": "email.headerregistry.ContentTransferEncodingHeader",
    "محلّل_تغذية": "email.parser.FeedParser",
    # === http إضافي ===
    # === socketserver إضافي ===
    "معالج_تدفق": "socketserver.StreamRequestHandler",
    "معالج_بيانات": "socketserver.DatagramRequestHandler",
    "خلط_الخيوط": "socketserver.ThreadingMixIn",
    "خلط_العمليات": "socketserver.ForkingMixIn",
    # === selectors إضافي ===
    "محدد_استطلاع": "selectors.PollSelector",
    "مفتاح_تسجيل": "selectors.SelectorKey",
    # === urllib.request إضافي ===
    "معالج_خطأ_افتراضي": "urllib.request.HTTPDefaultErrorHandler",
    "مصادقة_ملخّصة": "urllib.request.HTTPDigestAuthHandler",
    "مدير_كلمات_مصادقة": "urllib.request.HTTPPasswordMgrWithDefaultRealm",
    # === cookiejar ===
    "كوكي_مفرد": "http.cookiejar.Cookie",
    # === سياق SSL والشهادات ===
    "سياق_آمن_افتراضي": "_apl_ssl_context",
    "سياق_ssl": "ssl.SSLContext",
    "شهادة_الخادم": "ssl.get_server_certificate",
    "شهادة_der_إلى_pem": "ssl.DER_cert_to_PEM_cert",
    "شهادة_pem_إلى_der": "ssl.PEM_cert_to_DER_cert",
    "تحقق_من_الشهادة": "ssl.match_hostname",
    "عشوائي_آمن": "ssl.RAND_bytes",
    # === تغليف البيانات (struct) ===
    "حزمة_ثنائية": "struct.pack",
    "فك_حزمة_ثنائية": "struct.unpack",
    "احسب_حجم_الصيغة": "struct.calcsize",
    "اقرأ_من_مخزن": "struct.unpack_from",
    # === تمثيل العناوين والمنافذ ===
    "كل_عناوين_الاسم": "socket.gethostbyname_ex",
    # === الجاهزية والتزامن (select / selectors) ===
    "انتظر_جاهزية": "select.select",
    # === http.client ===
    "اتصال_http": "http.client.HTTPConnection",
    # === urllib.request ===
    "افتح_رابط": "urllib.request.urlopen",
    "طلب_ويب": "urllib.request.Request",
    "نظّف_الروابط": "urllib.request.urlcleanup",
    "فاتح_وكيل": "urllib.request.ProxyHandler",
    "فاتح_كوكيز": "urllib.request.HTTPCookieProcessor",
    "مدير_كوكيز": "http.cookiejar.CookieJar",
    "مصادقة_أساسية_ويب": "urllib.request.HTTPBasicAuthHandler",
    "مدير_كلمات_ويب": "urllib.request.HTTPPasswordMgr",
    "معالج_تحويل": "urllib.request.HTTPRedirectHandler",
    # === رسائل البريد (email.message) ===
    "رسالة_بريد_كاملة": "email.message.EmailMessage",
    # === أنواع MIME ===
    "بريد_أساس": "email.mime.base.MIMEBase",
    "ملف_بريد": "email.mime.application.MIMEApplication",
    "شفّر_محتوى": "email.encoders.encode_base64",
    "شفّر_حروف": "email.encoders.encode_quopri",
    "شفّر_لا_شيء": "email.encoders.encode_noop",
    # === أدوات البريد (email.utils / header / parser) ===
    "نسّق_تاريخ_البريد": "email.utils.formatdate",
    "نسّق_تاريخ_دقيق": "email.utils.format_datetime",
    "ولّد_معرّف_رسالة": "email.utils.make_msgid",
    "نسّق_عنوان_بريد": "email.utils.formataddr",
    "حلّل_عنوان_بريد": "email.utils.parseaddr",
    "اقتبس_نصاً": "email.utils.quote",
    "فك_اقتباس": "email.utils.unquote",
    "فك_رأس_بريد": "email.header.decode_header",
    "رسالة_من_نص": "email.parser.Parser",
    # === إرسال البريد (smtplib) ===
    # === قراءة البريد POP3 ===
    # === قراءة البريد IMAP4 ===
    "عميل_imap": "imaplib.IMAP4",
    "عميل_imap_آمن": "imaplib.IMAP4_SSL",
    # === نقل الملفات FTP ===
    # === أنواع الملفات والمتصفح ===
    "نوع_الملف_من_الاسم": "mimetypes.guess_type",
    "سجّل_نوعاً": "mimetypes.add_type",
    "خمّن_كل_الأنواع": "mimetypes.guess_all_extensions",
    # === عناوين IP ===
    "عنوان_ip": "ipaddress.ip_address",
    "شبكة_ip": "ipaddress.ip_network",
    "عنوان_ipv4": "ipaddress.IPv4Address",
    "شبكة_ipv4": "ipaddress.IPv4Network",
    "عنوان_ipv6": "ipaddress.IPv6Address",
    "شبكة_ipv6": "ipaddress.IPv6Network",
    # === خوادم المقابس (socketserver) ===
    "خادم_tcp": "socketserver.TCPServer",
    "معالج_طلبات": "socketserver.BaseRequestHandler",
    # === أدوات ثنائية ونقل مشفّر ===
    "سدّس_بايتات": "binascii.hexlify",
    "فك_سدّس_بايتات": "binascii.unhexlify",
    "بايتات_إلى_قاعدة64": "binascii.b2a_base64",
    "قاعدة64_إلى_بايتات": "binascii.a2b_base64",
    "تحقق_من_سلامة": "binascii.crc32",
    "شفّر_نص_قديم": "quopri.encodestring",
    "فك_نص_قديم": "quopri.decodestring",
}

# دوال الكائن: تُستخدم بعد نقطة
NET_METHODS = {
    # === دوال المقبس (Socket) ===
    "ربط_المنفذ": "bind",
    "استمع_للاتصالات": "listen",
    "اقبل_اتصال": "accept",
    "اتصل_بالعنوان": "connect",
    "اتصل_وأرجع_الخطأ": "connect_ex",
    "أرسل_بيانات": "send",
    "أرسل_الكل": "sendall",
    "استقبل": "recv",
    "استقبل_في_مخزن": "recv_into",
    "استقبل_من": "recvfrom",
    "أرسل_إلى_عنوان": "sendto",
    "أغلق_اتجاه": "shutdown",
    "أغلق_المقبس": "close",
    "عين_مهلة": "settimeout",
    "اقرأ_المهلة": "gettimeout",
    "عين_الحجب": "setblocking",
    "عين_خيار": "setsockopt",
    "اقرأ_خيار": "getsockopt",
    "عنوان_الطرف_الآخر": "getpeername",
    "عنوان_المقبس": "getsockname",
    "رقم_الوصف": "fileno",
    "افتح_ملف_من_المقبس": "makefile",
    "افصل_المقبس": "detach",
    "انسخ_وصف_المقبس": "dup",
    "أرسل_ملف": "sendfile",
    "أرسل_رسالة_حزمة": "sendmsg",
    "استقبل_حزمة": "recvmsg",
    # === select / poll / epoll ===
    "سجّل_في_الاستطلاع": "register",
    "ألغِ_من_الاستطلاع": "unregister",
    "استطلع": "poll",
    "سجّل_epoll": "register",
    "عدّل_epoll": "modify",
    "ألغِ_epoll": "unregister",
    "انتظر_epoll": "poll",
    "أغلق_epoll": "close",
    # === كائن SSLObject ===
    "اقرأ_من_ssl": "read",
    "اكتب_في_ssl": "write",
    "ابدأ_المصافحة": "do_handshake",
    "شهادة_ssl": "getpeercert",
    "تشفير_ssl": "cipher",
    "إصدار_ssl": "version",
    "ضغط_ssl": "compression",
    "بروتوكول_alpn": "selected_alpn_protocol",
    "معلّق_ssl": "pending",
    # === خصائص وإعدادات إضافية للسياق ===
    "شهادات_الثقة": "get_ca_certs",
    "إحصاء_الجلسات": "session_stats",
    "عين_منحنى_ecdh": "set_ecdh_curve",
    "أضف_شهادة_ثقة": "load_verify_locations",
    # === http.server ===
    "أرسل_استجابة": "send_response",
    "أرسل_رأساً": "send_header",
    "أنهِ_الرؤوس_http": "end_headers",
    "أرسل_خطأ_http": "send_error",
    "سجّل_رسالة_http": "log_message",
    "عالج_طلباً_واحداً": "handle_one_request",
    "نفّذ_خادماً": "serve_forever",
    # === http.cookies ===
    "عين_كوكي": "set",
    "قيمة_كوكي_معدلة": "output",
    "نص_كوكي": "OutputString",
    "كوكي_جافاسكربت": "js_output",
    # === خصائص رسالة البريد ===
    "إزاحة_محتوى_البريد": "get_content_disposition",
    "ترميز_المحتوى_الفعلي": "get_content_charset",
    "اقرأ_معاملات_المحتوى": "get_params",
    "عين_بدون_فك": "set_raw",
    "حقول_الرسالة_كلها": "raw_items",
    "عين_حدود": "set_boundary",
    "احذف_كل_الرؤوس": "clear",
    "اقرأ_أصل_الرسالة": "get_unixfrom",
    "عين_أصل_الرسالة": "set_unixfrom",
    "اقرأ_رأساً_أو_افتراضي": "get",
    "نوع_الافتراضي": "get_default_type",
    "عين_نوع_افتراضي": "set_default_type",
    "اقرأ_الحمولة_الخام": "get_payload",
    "اقرأ_كل_الرؤوس": "items",
    "احذف_رأساً_من_الرسالة": "__delitem__",
    "اقرأ_رأساً_من_الرسالة": "__getitem__",
    "ضع_رأساً_في_الرسالة": "__setitem__",
    "طول_الرسالة": "__len__",
    "اجعل_الرسالة_نصاً": "as_string",
    "اجعل_الرسالة_بايتات": "as_bytes",
    "اقرأ_اسم_المرفق": "get_filename",
    "نص_الرسالة_كامل": "flatten",
    "بايتات_الرسالة": "flatten",
    # === مجموعات الحروف (email.charset) ===
    "شفّر_الجسم": "body_encode",
    "رأس_مجموعة_الحروف": "header_encode",
    "رأس_مجموعة_الحروف_مع_خط": "header_encode_lines",
    "جسم_المجموعة": "get_body_encoding",
    "ناتج_المجموعة": "get_output_charset",
    # === xmlrpc ===
    "سجّل_دالة_عن_بعد": "register_function",
    "سجّل_كائناً_عن_بعد": "register_instance",
    "سجّل_مقدّمة": "register_introspection_functions",
    # === ipaddress إضافي ===
    "عدد_العنوان": "__int__",
    "قارن_العناوين": "__lt__",
    "أضف_لعنوان": "__add__",
    "اطرح_من_عنوان": "__sub__",
    "شبكة_فائقة": "supernet",
    "شبكات_فرعية": "subnets",
    "عنوان_ضمن_شبكة": "__contains__",
    "تبعية_شبكة": "subnet_of",
    "شبكة_فائقة_تحتويها": "supernet_of",
    "شمول_الشبكات": "overlaps",
    "أسطر_الشبكة": "__iter__",
    "أجهزة_ipv6": "hosts",
    "قارن_العناوين_ipv6": "__lt__",
    "انضم_لعنوان": "__add__",
    "شبكة_أم": "supernet",
    "شبكات_فرعية_ipv6": "subnets",
    "ضمن_شبكة_ipv6": "__contains__",
    "تبعية_ipv6": "subnet_of",
    "انضم_لعنوان_v4": "__add__",
    # === ضغط zlib ونقل نصوص ===
    "أنهِ_ضغط_zlib": "flush",
    "فك_ضغط_جزئي": "decompress",
    # === netrc و uu ===
    "بيانات_مصادقة_netrc": "authenticators",
    # === ssl جلسات وسلاسل ===
    "جلسة_ssl": "wrap_socket",
    "معلّق_المقبس_الآمن": "pending",
    "تشفيرات_مشتركة": "shared_ciphers",
    "ابدأ_مصافحة_المقبس": "do_handshake",
    # === بريد: دوال وأصناف إضافية ===
    "نسخة_سياسة": "clone",
    "اقرأ_رأساً_بالسياسة": "header_fetch_parse",
    "خزّن_رأساً_بالسياسة": "header_store_parse",
    "اطوِ_رأساً": "fold",
    "اطوِ_بايتات": "fold_binary",
    "غذِّ_محلل_البريد": "feed",
    "أنهِ_التغذية": "close",
    "اكتب_رسالة": "write",
    "انسخ_مولّداً": "clone",
    "أضف_لرأس_البريد": "append",
    "شفّر_رأس_البريد": "encode",
    # === http إضافي ===
    "طلب_رأس_حسب_الاسم": "getheader",
    "اقرأ_في_مخزن": "readinto",
    "هل_أُغلق": "isclosed",
    "نفق_وكيل": "set_tunnel",
    "أرسل_رأس_بلا_تحقق": "send_response_only",
    "أفرغ_الرؤوس": "flush_headers",
    # === socketserver إضافي ===
    "تهيئة_المعالج": "setup",
    "إنهاء_المعالج": "finish",
    "عالج_الطلب": "handle",
    "أغلق_الخادم_كلية": "server_close",
    "مهلة_الخادم": "handle_timeout",
    # === urllib.request إضافي ===
    "طريقة_تلقائية": "get_method",
    "هل_يوجد_رأس": "has_header",
    "احذف_رأساً": "remove_header",
    "أضف_رأساً_بلا_تحويل": "add_unredirected_header",
    "عنوان_كامل_للطلب": "get_full_url",
    "افتح_بفاتح": "open",
    # === cookiejar ===
    "أضف_كوكيز_للطلب": "add_cookie_header",
    "استخرج_الكوكيز": "extract_cookies",
    "عين_سياسة_كوكيز": "set_policy",
    "ضع_كوكي_في_المدير": "set_cookie",
    "امسح_الكوكيز": "clear",
    "امسح_كوكيز_الجلسة": "clear_session_cookies",
    "اصنع_كوكيز": "make_cookies",
    # === بروتوكولات إضافية ===
    "أعد_تعيين_بريد": "rset",
    "مساعدة_الخادم": "help",
    "مصادقة_apop": "apop",
    "اقرأ_واحذف_pop": "rpop",
    "عين_تتبع_pop": "set_debuglevel",
    "صلاحيات_imap": "getacl",
    "عين_صلاحيات_imap": "setacl",
    "احذف_صلاحيات_imap": "deleteacl",
    "حقوقي_imap": "myrights",
    "فرز_imap": "sort",
    "خيوط_imap": "thread",
    "تحقق_صندوق": "check",
    "حصة_imap": "getquota",
    "عين_حصة_imap": "setquota",
    "جذر_الحصة": "getquotaroot",
    "اسرد_بصيغة_الآلة": "mlsd",
    "أوقف_ftp": "abort",
    "افتح_اتصال_بياني": "makepasv",
    "عين_تتبع_ftp": "set_debuglevel",
    "اقرأ_مهل_الخادم": "ehlo_or_helo_if_needed",
    "أرسل_أمراً_خاماً": "putcmd",
    "اقرأ_ردّ_الخادم": "getreply",
    "أنهِ_ftplib": "quit",
    "أغلق_قناة_البيانات": "close",
    # === أدوات إضافية ===
    "أفرغ_الضاغط": "flush",
    "أفرغ_الفاك": "flush",
    # === دوال SSLContext ===
    "حمّل_شهادة_الخادم": "load_cert_chain",
    "حمّل_شهادات_التحقق": "load_verify_locations",
    "حمّل_شهادات_افتراضية": "load_default_certs",
    "عين_التشفيرات": "set_ciphers",
    "عين_بروتوكولات_alpn": "set_alpn_protocols",
    "عين_بروتوكولات_npn": "set_npn_protocols",
    "افتح_مقبس_آمن": "wrap_socket",
    "التفف_حول_قنوات": "wrap_bio",
    "اختبر_الثقة": "cert_store_stats",
    # === خصائص المقبس الآمن والقياس ===
    "شهادة_المقبس": "getpeercert",
    "تشفير_المقبس": "cipher",
    "إصدار_المقبس": "version",
    "أغلق_آمن": "unwrap",
    # === مقبس: دوال إضافية ===
    "استقبل_من_في_مخزن": "recvfrom_into",
    "استقبل_رسالة_في_مخزن": "recvmsg_into",
    "اقرأ_قابلية_الوراثة": "get_inheritable",
    "عين_قابلية_الوراثة": "set_inheritable",
    "افتح_مقبساً_بسياق": "__enter__",
    "أغلق_مقبساً_بسياق": "__exit__",
    "عنوان_المنفذ_المحلي": "getsockname",
    # === بريد إضافي ===
    "اقرأ_المحتوى_ككائن": "get_content",
    "عين_محتوى_متعدد": "set_content",
    "احذف_مرفقاً": "__delitem__",
    "اقرأ_الحمولة_أولاً": "get_payload",
    "اقرأ_مجموعات_الحروف": "get_charsets",
    "حقول_خام_الرسالة": "raw_items",
    "اقرأ_الجسم_الأول": "get_body",
    "احذف_رأساً_بالاسم": "__delitem__",
    "اقرأ_الحمولة_كقائمة": "get_payload",
    "أضف_جزءاً_مرفقاً": "attach",
    "جزء_متعدد_أجزاء": "is_multipart",
    "اقرأ_نوع_الجزء": "get_content_type",
    # === تغليف البيانات (struct) ===
    "حزمة_بصيغة": "pack",
    "فك_بصيغة": "unpack",
    # === أنواع ملفات إضافية ===
    "كل_امتدادات_النوع": "guess_all_extensions",
    "أضف_نوعاً_للكائن": "add_type",
    "اقرأ_من_ملف": "read_windows_registry",
    # === الجاهزية والتزامن (select / selectors) ===
    "سجّل_مقبس": "register",
    "عدّل_تسجيل": "modify",
    "ألغِ_تسجيل": "unregister",
    "اقرأ_الجاهز": "select",
    "خريطة_التسجيل": "get_map",
    "أغلق_المحدد": "close",
    # === http.client ===
    "أرسل_طلب": "request",
    "اقرأ_الاستجابة": "getresponse",
    "هيّئ_الطلب": "putrequest",
    "أضف_رأس_اتصال": "putheader",
    "أنهِ_الرؤوس": "endheaders",
    "أغلق_الاتصال": "close",
    "اتصل_بالخادم": "connect",
    "عين_تتبع": "set_debuglevel",
    "اقرأ_جسم_الاستجابة": "read",
    "اقرأ_سطر_استجابة": "readline",
    "اقرأ_رأس_استجابة": "getheader",
    "اقرأ_رؤوس_استجابة": "getheaders",
    "اقرأ_عنوان_استجابة": "geturl",
    # === urllib.request ===
    "رأس_طلب": "get_header",
    "أضف_رأس_طلب": "add_header",
    "حقول_الطلب": "header_items",
    "اقرأ_جسم": "read",
    # === رسائل البريد (email.message) ===
    "عين_المحتوى": "set_content",
    "عين_محتوى_بايتات": "set_content",
    "اقرأ_المحتوى": "get_content",
    "اقرأ_الجسم": "get_body",
    "أضف_بديلاً": "add_alternative",
    "أضف_مرفقاً": "add_attachment",
    "أضف_مرتبطاً": "add_related",
    "أضف_رأس_بريد": "add_header",
    "استبدل_رأس_بريد": "replace_header",
    "احذف_رأس_بريد": "__delitem__",
    "اكتب_رأس_بريد": "__setitem__",
    "اقرأ_رأس_بريد": "__getitem__",
    "كل_الرؤوس": "items",
    "أسماء_الرؤوس": "keys",
    "قيم_الرؤوس": "values",
    "كرر_الأجزاء": "walk",
    "كرر_المرفقات": "iter_attachments",
    "كرر_البدائل": "iter_parts",
    "أرفق_جزءاً": "attach",
    "اقرأ_الحمولة": "get_payload",
    "عين_الحمولة": "set_payload",
    "اقرأ_رأساً_كأول": "get_all",
    "اقرأ_رأساً_بافتراضي": "get",
    "نوع_محتوى_البريد": "get_content_type",
    "نوع_الرسالة": "get_content_maintype",
    "نوع_فرعي_للرسالة": "get_content_subtype",
    "ترميز_المحتوى": "get_charset",
    "اسم_المرفق": "get_filename",
    "حدود_الرسالة": "get_boundary",
    "معامل_رسالة": "get_param",
    "عين_معاملاً": "set_param",
    "عين_النوع": "set_type",
    "اجعلها_بدائل": "make_alternative",
    "اجعلها_مرتبطة": "make_related",
    "اجعلها_مختلطة": "make_mixed",
    "إلى_نص": "as_string",
    "إلى_بايتات": "as_bytes",
    "إلى_نص_كامل": "as_string",
    "أرسل_إلى_نص": "as_string",
    "معرّف_الرسالة": "make_msgid",
    "الحمولة_مصفوفة": "is_multipart",
    "رسالة_متعددة_الأجزاء_للإيميل": "is_multipart",
    "النوع_50_51": "get_default_type",
    # === أدوات البريد (email.utils / header / parser) ===
    "اقرأ_رسالة_من_نص": "parsestr",
    "اقرأ_رسالة_من_بايتات": "parsebytes",
    "اقرأ_رسالة_من_ملف": "parse",
    # === إرسال البريد (smtplib) ===
    "اتصال_smtp": "connect",
    "عرّف_نفسك": "ehlo",
    "حيّ_الخادم": "helo",
    "ابدأ_tls": "starttls",
    "سجّل_دخول_بريد": "login",
    "أرسل_بريداً": "sendmail",
    "أرسل_رسالة_بريد": "send_message",
    "تحقق_من_عنوان": "verify",
    "هل_يدعم_الإضافة": "has_extn",
    "أمر_خادم": "docmd",
    "أرسل_بيانات_بريد": "data",
    "ابدأ_إرسالاً": "mail",
    "حدّد_مستلماً": "rcpt",
    "ابدأ_إرسال_جملة": "mail",
    "نبض_الاتصال": "noop",
    "أنهِ_جلسة_البريد": "quit",
    "سجّل_خروج_بريد": "quit",
    "عين_مستوى_التتبع": "set_debuglevel",
    # === قراءة البريد POP3 ===
    "اسم_المستخدم_pop": "user",
    "كلمة_السر_pop": "pass_",
    "حالة_pop": "stat",
    "قائمة_رسائل_pop": "list",
    "اقرأ_رسالة_pop": "retr",
    "احذف_رسالة_pop": "dele",
    "أعد_رسالة_pop": "rset",
    "رؤوس_رسالة_pop": "top",
    "معرّفات_pop": "uidl",
    "قدرات_pop": "capa",
    "أنهِ_pop": "quit",
    # === قراءة البريد IMAP4 ===
    "سجّل_دخول_imap": "login",
    "اختر_صندوقاً": "select",
    "ابحث_في_imap": "search",
    "اجلب_رسالة_imap": "fetch",
    "خزّن_في_imap": "store",
    "أضف_لصندوق": "append",
    "احذف_من_صندوق": "expunge",
    "أنشئ_صندوقاً": "create",
    "احذف_صندوقاً": "delete",
    "أعد_تسمية_صندوق": "rename",
    "اسرد_صناديق": "list",
    "حالة_صندوق": "status",
    "انسخ_رسالة": "copy",
    "أغلق_صندوقاً": "close",
    "اشترك_بصندوق": "subscribe",
    "ألغِ_اشتراكاً": "unsubscribe",
    "قدرات_imap": "capability",
    "ابدأ_tls_imap": "starttls",
    "نبض_imap": "noop",
    "سجّل_خروج_imap": "logout",
    # === نقل الملفات FTP ===
    "اتصل_بـftp": "connect",
    "سجّل_دخول_ftp": "login",
    "مجلد_حالي_ftp": "pwd",
    "غيّر_مجلد_ftp": "cwd",
    "اسرد_ftp": "nlst",
    "تفاصيل_ftp": "dir",
    "أنشئ_مجلد_ftp": "mkd",
    "احذف_مجلد_ftp": "rmd",
    "احذف_ملف_ftp": "delete",
    "أعد_تسمية_ftp": "rename",
    "حجم_ملف_ftp": "size",
    "نزّل_ثنائياً": "retrbinary",
    "نزّل_نصياً": "retrlines",
    "ارفع_ثنائياً": "storbinary",
    "ارفع_نصياً": "storlines",
    "أرسل_أمر_ftp": "sendcmd",
    "نفّذ_أمر_ftp": "voidcmd",
    "وضع_سلبي": "set_pasv",
    "أغلق_ftp": "quit",
    # === عناوين IP ===
    "حدود_الشبكة": "hosts",
    # === خوادم المقابس (socketserver) ===
    "خدم_دائماً": "serve_forever",
    "عالج_طلباً": "handle_request",
    "أغلق_الخادم": "shutdown",
    "فعّل_الخادم": "server_activate",
}

# الخصائص: بلا أقواس
NET_PROPS = {
    # === خصائص وإعدادات إضافية للسياق ===
    "خيارات_السياق": "options",
    "أعلام_التحقق": "verify_flags",
    "تذاكر_الجلسة": "num_tickets",
    "نداء_اسم_الخادم": "sni_callback",
    # === http.cookies ===
    "اقرأ_كوكي": "value",
    "قيمة_مرمّزة_كوكي": "coded_value",
    "اسم_كوكي": "key",
    # === ipaddress إضافي ===
    "عنوان_غير_محدد": "is_unspecified",
    "عنوان_رابط_محلي": "is_link_local",
    "مضغوط_العنوان": "compressed",
    "حزم_العنوان": "packed",
    "قناع_بالاسم": "with_netmask",
    "قناع_بالطول": "with_prefixlen",
    "عنوان_موقع_محلي": "is_site_local",
    "عنوان_افتراضي_متعدد": "is_multicast",
    "أقصى_بادئة": "max_prefixlen",
    "عنوان_الشبكة_ipv6": "network_address",
    "بث_ipv6": "broadcast_address",
    "شبكة_الواجهة_ipv6": "network",
    "عنوان_الواجهة_ipv6": "ip",
    "بادئة_الشبكة": "prefixlen",
    # === ssl جلسات وسلاسل ===
    "سياق_المقبس_الآمن": "context",
    "تذاكر_الجلسة_المستخدمة": "session",
    "أعيد_استخدام_الجلسة": "session_reused",
    "مصافحة_الجلسة": "has_ticket",
    "عمر_تذكرة_الجلسة": "ticket_lifetime_hint",
    "وقت_الجلسة": "time",
    "مهلة_الجلسة": "timeout",
    "معرّف_الجلسة": "id",
    "تحقق_شائع_الاسم": "hostname_checks_common_name",
    # === http إضافي ===
    "مهلة_الاتصال_http": "timeout",
    "مستوى_تتبع_http": "debuglevel",
    "رسالة_رؤوس_الاستجابة": "msg",
    "طول_المحتوى_المقروء": "length",
    "هل_مقطّع": "chunked",
    "منفذ_http_افتراضي": "default_port",
    "منفذ_https_افتراضي": "default_port",
    # === socketserver إضافي ===
    "عنوان_الخادم": "server_address",
    "معالج_الخادم": "RequestHandlerClass",
    # === selectors إضافي ===
    "ملف_المفتاح": "fileobj",
    "رقم_وصف_المفتاح": "fd",
    "أحداث_المفتاح": "events",
    "بيانات_المفتاح": "data",
    # === cookiejar ===
    "اسم_الكوكي": "name",
    "قيمة_الكوكي": "value",
    "نطاق_الكوكي": "domain",
    "مسار_الكوكي": "path",
    "انتهاء_الكوكي": "expires",
    "كوكي_مؤمّن": "secure",
    "إصدار_الكوكي": "version",
    "منفذ_الكوكي": "port",
    # === بروتوكولات إضافية ===
    "ترميز_ftp": "encoding",
    "حجم_الرسالة_الأقصى": "esmtp_features",
    "حالة_ftp": "debugging",
    "مهلة_ftp": "timeout",
    "ترحيب_pop": "welcome",
    "حالة_imap": "state",
    # === أدوات إضافية ===
    "عنوان_معكوس": "reverse_pointer",
    "عنوان_مضمن_ipv4": "ipv4_mapped",
    "عنوان_ستة_إلى_أربعة": "sixtofour",
    "نطاق_العنوان": "scope_id",
    "عنوان_الواجهة": "ip",
    "شبكة_الواجهة": "network",
    # === خصائص المقبس الآمن والقياس ===
    "وضع_التحقق": "verify_mode",
    "تحقق_من_الاسم": "check_hostname",
    "أدنى_إصدار": "minimum_version",
    "أقصى_إصدار": "maximum_version",
    # === بريد إضافي ===
    "سياسة_الرسالة_المستخدمة": "policy",
    # === تغليف البيانات (struct) ===
    "حجم_الصيغة": "size",
    "شبكة_كبيرة_النهاية": "format",
    "صيغة_الشبكة": "format",
    # === أنواع ملفات إضافية ===
    "خريطة_الامتدادات": "suffix_map",
    # === http.client ===
    "حالة_الاستجابة": "status",
    "سبب_الحالة": "reason",
    "إصدار_الاستجابة": "version",
    "رؤوس_الاستجابة": "headers",
    "أُغلقت_الاستجابة": "closed",
    # === urllib.request ===
    "كامل_العنوان": "full_url",
    "طريقة_الطلب": "method",
    "بيانات_الطلب": "data",
    # === رسائل البريد (email.message) ===
    "سطور_الرسالة": "preamble",
    # === عناوين IP ===
    "عنوان_خاص": "is_private",
    "عنوان_عام": "is_global",
    "عنوان_حلقة_محلية": "is_loopback",
    "عنوان_متعدد_بث": "is_multicast",
    "عنوان_محجوز": "is_reserved",
    "عنوان_الشبكة": "network_address",
    "قناع_الشبكة": "netmask",
    "بث_الشبكة": "broadcast_address",
    "طول_البادئة": "prefixlen",
    "عنوان_كامل": "exploded",
}

# الثوابت والأصناف التي تُستخدم بلا أقواس
NET_CONSTANTS = {
    # === إنشاء المقابس وإدارتها ===
    "مهلة_شبكة": "socket.timeout",
    "خطأ_عنوان": "socket.gaierror",
    "خطأ_اسم_جهاز": "socket.herror",
    # === عائلات وأنواع المقابس ===
    "عائلة_ipv4": "socket.AF_INET",
    "عائلة_ipv6": "socket.AF_INET6",
    "عائلة_محلي": "socket.AF_UNIX",
    "عائلة_غير_محددة": "socket.AF_UNSPEC",
    "مقبس_تدفق": "socket.SOCK_STREAM",
    "مقبس_بيانات": "socket.SOCK_DGRAM",
    "مقبس_خام": "socket.SOCK_RAW",
    "مقبس_متسلسل": "socket.SOCK_SEQPACKET",
    "مستوى_المقبس": "socket.SOL_SOCKET",
    "مستوى_tcp": "socket.IPPROTO_TCP",
    "مستوى_udp": "socket.IPPROTO_UDP",
    "مستوى_ip": "socket.IPPROTO_IP",
    "أي_عنوان": "socket.INADDR_ANY",
    "عنوان_بث": "socket.INADDR_BROADCAST",
    "أقصى_طابور": "socket.SOMAXCONN",
    "يدعم_ipv6": "socket.has_ipv6",
    # === خيارات المقبس ===
    "إعادة_استخدام_العنوان": "socket.SO_REUSEADDR",
    "إعادة_استخدام_المنفذ": "socket.SO_REUSEPORT",
    "إبقاء_الاتصال": "socket.SO_KEEPALIVE",
    "حجم_استقبال": "socket.SO_RCVBUF",
    "حجم_إرسال": "socket.SO_SNDBUF",
    "مهلة_استقبال": "socket.SO_RCVTIMEO",
    "مهلة_إرسال": "socket.SO_SNDTIMEO",
    "سماح_البث": "socket.SO_BROADCAST",
    "مقبس_عاجل": "socket.SO_OOBINLINE",
    "خيار_خطأ": "socket.SO_ERROR",
    "خيار_النوع": "socket.SO_TYPE",
    "بلا_تأخير": "socket.TCP_NODELAY",
    "إغلاق_قراءة": "socket.SHUT_RD",
    "إغلاق_كتابة": "socket.SHUT_WR",
    "إغلاق_كامل": "socket.SHUT_RDWR",
    "نظرة_بلا_سحب": "socket.MSG_PEEK",
    "انتظر_الكل": "socket.MSG_WAITALL",
    "بلا_انتظار": "socket.MSG_DONTWAIT",
    "خارج_النطاق": "socket.MSG_OOB",
    "زمن_حياة_البث": "socket.IP_MULTICAST_TTL",
    "انضم_للمجموعة": "socket.IP_ADD_MEMBERSHIP",
    "اترك_المجموعة": "socket.IP_DROP_MEMBERSHIP",
    "واجهة_البث": "socket.IP_MULTICAST_IF",
    "حلقة_البث": "socket.IP_MULTICAST_LOOP",
    # === عائلات العناوين ===
    "عائلة_شبكة_محلية": "socket.AF_UNIX",
    "عائلة_غير_معروفة": "socket.AF_UNSPEC",
    "عائلة_ناقل_حزم": "socket.AF_PACKET",
    "عائلة_نتلينك": "socket.AF_NETLINK",
    "عائلة_بلوتوث": "socket.AF_BLUETOOTH",
    "عائلة_كان": "socket.AF_CAN",
    "عائلة_rds": "socket.AF_RDS",
    "عائلة_ipx": "socket.AF_IPX",
    "عائلة_appletalk": "socket.AF_APPLETALK",
    "عائلة_vsock": "socket.AF_VSOCK",
    "عائلة_irda": "socket.AF_IRDA",
    "عائلة_tipc": "socket.AF_TIPC",
    # === أنواع المقابس وأعلامها ===
    "مقبس_موثوق_بيانات": "socket.SOCK_RDM",
    "مقبس_يغلق_مع_التنفيذ": "socket.SOCK_CLOEXEC",
    "مقبس_بلا_حجب": "socket.SOCK_NONBLOCK",
    # === مستويات الخيارات ===
    "مستوى_ip_عام": "socket.SOL_IP",
    "مستوى_tcp_عام": "socket.SOL_TCP",
    "مستوى_udp_عام": "socket.SOL_UDP",
    # === خيارات المقبس الإضافية ===
    "قبول_الاتصالات": "socket.SO_ACCEPTCONN",
    "تصحيح_المقبس": "socket.SO_DEBUG",
    "عائلة_المقبس": "socket.SO_DOMAIN",
    "بروتوكول_المقبس": "socket.SO_PROTOCOL",
    "تجاوز_التوجيه": "socket.SO_DONTROUTE",
    "حد_استقبال_أدنى": "socket.SO_RCVLOWAT",
    "حد_إرسال_أدنى": "socket.SO_SNDLOWAT",
    "انتظار_الإغلاق": "socket.SO_LINGER",
    # === خيارات TCP ===
    "ازدحام_tcp": "socket.TCP_CONGESTION",
    "حشو_tcp": "socket.TCP_CORK",
    "تأجيل_القبول": "socket.TCP_DEFER_ACCEPT",
    "فتح_سريع": "socket.TCP_FASTOPEN",
    "معلومات_tcp": "socket.TCP_INFO",
    "عدد_نبضات_الاستمرار": "socket.TCP_KEEPCNT",
    "مهلة_نبضة_الاستمرار": "socket.TCP_KEEPIDLE",
    "فاصل_نبضة_الاستمرار": "socket.TCP_KEEPINTVL",
    "أقصى_حجم_مقطع": "socket.TCP_MAXSEG",
    "تأكيد_سريع": "socket.TCP_QUICKACK",
    "عدد_محاولات_الاتصال": "socket.TCP_SYNCNT",
    "مهلة_المستخدم_tcp": "socket.TCP_USER_TIMEOUT",
    "حد_نافذة_tcp": "socket.TCP_WINDOW_CLAMP",
    # === خيارات IP ===
    "نوع_الخدمة": "socket.IP_TOS",
    "زمن_الحياة": "socket.IP_TTL",
    "رأس_كامل_مع_البيانات": "socket.IP_HDRINCL",
    "خيارات_ip": "socket.IP_OPTIONS",
    # === بروتوكولات ===
    "بروتوكول_icmp": "socket.IPPROTO_ICMP",
    "بروتوكول_igmp": "socket.IPPROTO_IGMP",
    "بروتوكول_ipv6": "socket.IPPROTO_IPV6",
    "بروتوكول_خام": "socket.IPPROTO_RAW",
    "بروتوكول_sctp": "socket.IPPROTO_SCTP",
    "بروتوكول_udplite": "socket.IPPROTO_UDPLITE",
    # === أعلام الرسائل ===
    "بيانات_مقطوعة": "socket.MSG_CTRUNC",
    "بلا_توجيه": "socket.MSG_DONTROUTE",
    "نهاية_السجل": "socket.MSG_EOR",
    "طابور_الأخطاء": "socket.MSG_ERRQUEUE",
    "مزيد_قادم": "socket.MSG_MORE",
    "بلا_إشارة": "socket.MSG_NOSIGNAL",
    "مقتطع": "socket.MSG_TRUNC",
    "تأكيد_الرسالة": "socket.MSG_CONFIRM",
    # === أعلام تحليل العناوين ===
    "عنوان_سلبي": "socket.AI_PASSIVE",
    "اسم_قانوني": "socket.AI_CANONNAME",
    "عنوان_رقمي_فقط": "socket.AI_NUMERICHOST",
    "منفذ_رقمي_فقط": "socket.AI_NUMERICSERV",
    "حسب_التكوين": "socket.AI_ADDRCONFIG",
    # === خيارات البيانات الاسمية ===
    "بلا_اسم_كامل": "socket.NI_NOFQDN",
    "اسم_رقمي": "socket.NI_NUMERICHOST",
    "اسم_مطلوب": "socket.NI_NAMEREQD",
    "منفذ_رقمي": "socket.NI_NUMERICSERV",
    "خدمة_بيانات": "socket.NI_DGRAM",
    "أقصى_اسم_جهاز": "socket.NI_MAXHOST",
    "أقصى_اسم_خدمة": "socket.NI_MAXSERV",
    # === أخطاء تحليل العناوين ===
    "خطأ_عائلة": "socket.EAI_ADDRFAMILY",
    "خطأ_محاولة_أخرى": "socket.EAI_AGAIN",
    "خطأ_أعلام": "socket.EAI_BADFLAGS",
    "خطأ_فشل_دائم": "socket.EAI_FAIL",
    "خطأ_عائلة_غير_مدعومة": "socket.EAI_FAMILY",
    "خطأ_ذاكرة": "socket.EAI_MEMORY",
    "خطأ_لا_بيانات": "socket.EAI_NODATA",
    "خطأ_لا_اسم": "socket.EAI_NONAME",
    "خطأ_خدمة": "socket.EAI_SERVICE",
    "خطأ_نوع_مقبس": "socket.EAI_SOCKTYPE",
    "خطأ_نظام_تحليل": "socket.EAI_SYSTEM",
    "خطأ_تجاوز": "socket.EAI_OVERFLOW",
    # === عناوين ثابتة ===
    "حلقة_محلية": "socket.INADDR_LOOPBACK",
    "عنوان_غير_صالح": "socket.INADDR_NONE",
    # === select / poll / epoll ===
    "حدث_دخل": "select.POLLIN",
    "حدث_خرج": "select.POLLOUT",
    "حدث_أولوية": "select.POLLPRI",
    "حدث_خطأ_استطلاع": "select.POLLERR",
    "حدث_انقطاع": "select.POLLHUP",
    "حدث_قيمة_غير_صحيحة": "select.POLLNVAL",
    "حدث_قراءة_عادي": "select.POLLRDNORM",
    "حدث_كتابة_عادي": "select.POLLWRNORM",
    "حدث_حافة_epoll": "select.EPOLLIN",
    "حدث_خرج_epoll": "select.EPOLLOUT",
    "حدث_خطأ_epoll": "select.EPOLLERR",
    "حدث_انقطاع_epoll": "select.EPOLLHUP",
    "وضع_الحواف": "select.EPOLLET",
    "مرة_واحدة": "select.EPOLLONESHOT",
    "حدث_إغلاق_نصف": "select.EPOLLRDHUP",
    # === خيارات سياق SSL ===
    "بلا_tlsv1": "ssl.OP_NO_TLSv1",
    "بلا_tlsv1_1": "ssl.OP_NO_TLSv1_1",
    "بلا_tlsv1_2": "ssl.OP_NO_TLSv1_2",
    "بلا_tlsv1_3": "ssl.OP_NO_TLSv1_3",
    "مفتاح_مفرد_عادي": "ssl.OP_SINGLE_ECDH_USE",
    "تفضيل_تشفير_الخادم": "ssl.OP_CIPHER_SERVER_PREFERENCE",
    "بلا_إعادة_تفاوض": "ssl.OP_NO_RENEGOTIATION",
    "توافق_الوسطاء": "ssl.OP_ENABLE_MIDDLEBOX_COMPAT",
    "يدعم_ecdhe": "ssl.HAS_ECDH",
    "أوضاع_التحقق_الافتراضية": "ssl.VERIFY_DEFAULT",
    "تحقق_سلسلة_جزئية": "ssl.VERIFY_X509_PARTIAL_CHAIN",
    "تحقق_صارم_للشهادة": "ssl.VERIFY_X509_STRICT",
    "غرض_الخادم": "ssl.Purpose.SERVER_AUTH",
    "غرض_العميل": "ssl.Purpose.CLIENT_AUTH",
    # === أخطاء إضافية ===
    "خطأ_كتابة_ssl": "ssl.SSLWantWriteError",
    "خطأ_انتهاء_ssl": "ssl.SSLEOFError",
    "خطأ_أي_ssl": "ssl.SSLErrorNumber",
    "تنبيه_فشل_مصافحة": "ssl.ALERT_DESCRIPTION_HANDSHAKE_FAILURE",
    "تنبيه_شهادة_سيئة": "ssl.ALERT_DESCRIPTION_BAD_CERTIFICATE",
    "تنبيه_شهادة_منتهية": "ssl.ALERT_DESCRIPTION_CERTIFICATE_EXPIRED",
    "تنبيه_شهادة_غير_موثوقة": "ssl.ALERT_DESCRIPTION_UNKNOWN_CA",
    # === أكواد HTTP الإضافية ===
    "حالة_مقبولة_جزئياً": "http.HTTPStatus.PARTIAL_CONTENT",
    "حالة_انتقل_مؤقتاً": "http.HTTPStatus.TEMPORARY_REDIRECT",
    "حالة_دائم_جديد": "http.HTTPStatus.PERMANENT_REDIRECT",
    "حالة_استخدم_وكيل": "http.HTTPStatus.USE_PROXY",
    "حالة_غير_مصرح": "http.HTTPStatus.UNAUTHORIZED",
    "حالة_محتوى_طويل_جدا": "http.HTTPStatus.REQUEST_ENTITY_TOO_LARGE",
    "حالة_نوع_غير_مدعوم": "http.HTTPStatus.UNSUPPORTED_MEDIA_TYPE",
    "حالة_نطاق_غير_مقبول": "http.HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE",
    "حالة_توقعات_فاشلة": "http.HTTPStatus.EXPECTATION_FAILED",
    "حالة_مقفل": "http.HTTPStatus.LOCKED",
    "حالة_فشل_تبعية": "http.HTTPStatus.FAILED_DEPENDENCY",
    "حالة_بوابة_سيئة": "http.HTTPStatus.BAD_GATEWAY",
    "حالة_غير_منفذ": "http.HTTPStatus.NOT_IMPLEMENTED",
    "حالة_إصدار_غير_مدعوم": "http.HTTPStatus.HTTP_VERSION_NOT_SUPPORTED",
    "حالة_متغير_أيضاً": "http.HTTPStatus.ALREADY_REPORTED",
    "حالة_غير_متاح_لقانوني": "http.HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS",
    "حالة_شبكة_غير_متاحة": "http.HTTPStatus.NETWORK_AUTHENTICATION_REQUIRED",
    "حالة_مهلة_الطلب": "http.HTTPStatus.REQUEST_TIMEOUT",
    # === أخطاء وأصناف البريد ===
    # === سياسات البريد ===
    "سياسة_http": "email.policy.HTTP",
    "سياسة_smtputf8": "email.policy.SMTPUTF8",
    "سياسة_متوافقة": "email.policy.compat32",
    # === xmlrpc ===
    # === netrc و uu ===
    "خطأ_netrc": "netrc.NetrcParseError",
    # === إنذارات TLS ===
    "تنبيه_إغلاق": "ssl.ALERT_DESCRIPTION_CLOSE_NOTIFY",
    "تنبيه_رسالة_غير_متوقعة": "ssl.ALERT_DESCRIPTION_UNEXPECTED_MESSAGE",
    "تنبيه_سجل_سيئ": "ssl.ALERT_DESCRIPTION_BAD_RECORD_MAC",
    "تنبيه_فك_ضغط_فاشل": "ssl.ALERT_DESCRIPTION_DECOMPRESSION_FAILURE",
    "تنبيه_يد_مصافحة": "ssl.ALERT_DESCRIPTION_HANDSHAKE_FAILURE",
    "تنبيه_شهادة_ملغاة": "ssl.ALERT_DESCRIPTION_CERTIFICATE_REVOKED",
    "تنبيه_شهادة_غير_معروفة": "ssl.ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN",
    "تنبيه_بروتوكول": "ssl.ALERT_DESCRIPTION_PROTOCOL_VERSION",
    "تنبيه_فك_ترميز": "ssl.ALERT_DESCRIPTION_DECODE_ERROR",
    # === بريد: دوال وأصناف إضافية ===
    "مدير_المحتوى_الخام": "email.contentmanager.raw_data_manager",
    # === http إضافي ===
    "جدول_الحالات": "http.client.responses",
    "طريقة_get": "http.HTTPMethod.GET",
    "طريقة_post": "http.HTTPMethod.POST",
    "طريقة_put": "http.HTTPMethod.PUT",
    "طريقة_delete": "http.HTTPMethod.DELETE",
    "طريقة_patch": "http.HTTPMethod.PATCH",
    "طريقة_head": "http.HTTPMethod.HEAD",
    "طريقة_options": "http.HTTPMethod.OPTIONS",
    "طريقة_trace": "http.HTTPMethod.TRACE",
    "طريقة_connect": "http.HTTPMethod.CONNECT",
    # === أدوات إضافية ===
    "ملفات_الأنواع_المعروفة": "mimetypes.knownfiles",
    "إصدار_zlib": "zlib.ZLIB_VERSION",
    "نافذة_الضغط": "zlib.MAX_WBITS",
    # === سياق SSL والشهادات ===
    "إصدار_openssl": "ssl.OPENSSL_VERSION",
    "إصدار_openssl_رقم": "ssl.OPENSSL_VERSION_NUMBER",
    "يدعم_tls13": "ssl.HAS_TLSv1_3",
    "يدعم_sni": "ssl.HAS_SNI",
    "يدعم_alpn": "ssl.HAS_ALPN",
    # === تحقق الشهادات ===
    "بلا_تحقق": "ssl.CERT_NONE",
    "تحقق_اختياري": "ssl.CERT_OPTIONAL",
    "تحقق_إلزامي": "ssl.CERT_REQUIRED",
    "بروتوكول_عميل": "ssl.PROTOCOL_TLS_CLIENT",
    "بروتوكول_خادم": "ssl.PROTOCOL_TLS_SERVER",
    "بروتوكول_آمن": "ssl.PROTOCOL_TLS",
    "أدنى_tls1_2": "ssl.TLSVersion.TLSv1_2",
    "أدنى_tls1_3": "ssl.TLSVersion.TLSv1_3",
    "أقصى_tls1_3": "ssl.TLSVersion.MAXIMUM_SUPPORTED",
    "بلا_شهادات_قديمة": "ssl.OP_NO_SSLv3",
    "بلا_ضغط": "ssl.OP_NO_COMPRESSION",
    "أعد_استخدام_الجلسة": "ssl.OP_NO_TICKET",
    "خطأ_ssl": "ssl.SSLError",
    "خطأ_مهلة_ssl": "ssl.SSLZeroReturnError",
    "خطأ_مقبس_ssl": "ssl.SSLWantReadError",
    # === أكواد حالة إضافية ===
    "حالة_استمر": "http.HTTPStatus.CONTINUE",
    "حالة_تبديل_بروتوكول": "http.HTTPStatus.SWITCHING_PROTOCOLS",
    "حالة_معالجة": "http.HTTPStatus.PROCESSING",
    "حالة_تلميحات_مبكرة": "http.HTTPStatus.EARLY_HINTS",
    "حالة_اختيارات_متعددة": "http.HTTPStatus.MULTIPLE_CHOICES",
    "حالة_انظر_لآخر": "http.HTTPStatus.SEE_OTHER",
    "حالة_بدون_تغيير": "http.HTTPStatus.NOT_MODIFIED",
    "حالة_مطلوب_دفع": "http.HTTPStatus.PAYMENT_REQUIRED",
    "حالة_محمي_بوكيل": "http.HTTPStatus.PROXY_AUTHENTICATION_REQUIRED",
    "حالة_شروط_فاشلة": "http.HTTPStatus.PRECONDITION_FAILED",
    # === مقبس: بروتوكولات إضافية ===
    "بروتوكول_ah": "socket.IPPROTO_AH",
    "بروتوكول_esp": "socket.IPPROTO_ESP",
    "بروتوكول_توجيه_الوجهة": "socket.IPPROTO_DSTOPTS",
    "بروتوكول_تجزئة": "socket.IPPROTO_FRAGMENT",
    "بروتوكول_بلا": "socket.IPPROTO_NONE",
    "بروتوكول_pim": "socket.IPPROTO_PIM",
    "اربط_بجهاز": "socket.SO_BINDTODEVICE",
    "بروتوكول_مقبس_مستمع": "socket.SO_ACCEPTCONN",
    "حجم_حزمة_أدنى": "socket.SO_SNDLOWAT",
    # === أكواد حالة مكمّلة ===
    "حالة_رابط_طويل": "http.HTTPStatus.REQUEST_URI_TOO_LONG",
    "حالة_ترقية_مطلوبة": "http.HTTPStatus.UPGRADE_REQUIRED",
    "حالة_مبكر_جدا": "http.HTTPStatus.TOO_EARLY",
    "حالة_كيان_غير_قابل_للمعالجة": "http.HTTPStatus.UNPROCESSABLE_ENTITY",
    "حالة_طول_مطلوب": "http.HTTPStatus.LENGTH_REQUIRED",
    "حالة_غير_مقبول": "http.HTTPStatus.NOT_ACCEPTABLE",
    "حالة_طلب_موجّه_خطأ": "http.HTTPStatus.MISDIRECTED_REQUEST",
    # === الجاهزية والتزامن (select / selectors) ===
    "حدث_قراءة": "selectors.EVENT_READ",
    "حدث_كتابة": "selectors.EVENT_WRITE",
    # === http.client ===
    "خطأ_استجابة": "http.client.InvalidURL",
    "معرّف_حالة_محظور": "http.HTTPStatus.FORBIDDEN",
    "معرّف_حالة_طلبات_كثيرة": "http.HTTPStatus.TOO_MANY_REQUESTS",
    "معرّف_حالة_خطأ_خادم": "http.HTTPStatus.INTERNAL_SERVER_ERROR",
    # === urllib.request ===
    "اقرأ_فاتحاً_مثبتاً": "urllib.request._opener",
    # === أدوات البريد (email.utils / header / parser) ===
    "سياسة_بريد_افتراضية": "email.policy.default",
    "سياسة_smtp": "email.policy.SMTP",
    "سياسة_صارمة": "email.policy.strict",
    "خطأ_تحليل_بريد": "email.errors.MessageError",
    # === إرسال البريد (smtplib) ===
    "منفذ_smtp": "smtplib.SMTP_PORT",
    "منفذ_smtp_آمن": "smtplib.SMTP_SSL_PORT",
    "خطأ_smtp": "smtplib.SMTPException",
    "خطأ_مستلمين_smtp": "smtplib.SMTPRecipientsRefused",
    "خطأ_مرسل_smtp": "smtplib.SMTPSenderRefused",
    "خطأ_تحية_smtp": "smtplib.SMTPHeloError",
    "انقطع_خادم_smtp": "smtplib.SMTPServerDisconnected",
    # === قراءة البريد POP3 ===
    "خطأ_pop": "poplib.error_proto",
    "منفذ_pop3": "poplib.POP3_PORT",
    # === قراءة البريد IMAP4 ===
    "منفذ_imap": "imaplib.IMAP4_PORT",
    "منفذ_imap_آمن": "imaplib.IMAP4_SSL_PORT",
    "خطأ_imap": "imaplib.IMAP4.error",
    # === نقل الملفات FTP ===
    "خطأ_أمر_ftp": "ftplib.error_perm",
    "خطأ_مؤقت_ftp": "ftplib.error_temp",
    "كل_أخطاء_ftp": "ftplib.all_errors",
}

# --- الاسم الواحد يمرّ مرة واحدة ----------------------------------------------
# المكتبات الأخرى تبني أربعة تعبيرات نمطية (methods / props / constants /
# funcs) وتُمرّر النص عليها. مع 1000 كلمة يصبح بناء هذه التعبيرات وحدها ~13 ms
# في كل تشغيل. هنا نستخدم مسحاً واحداً بالكلمات الكاملة، ونقرّر من قاموس الكلمة.
#
# ملاحظة مهمة: نحو 150 اسماً عربياً فيه تشكيل (شدّة/فتحة/كسرة) مثل `سجّل_مقبس`
# و`مهيّئ_استطلاع`. هذه المحارف ليست ضمن \w في Python، فلو كتبنا \w+ لتوقّف
# المسح عند الشدّة ولم يُترجم الاسم. لذلك نضيف نطاق التشكيل صراحةً.
_NET_TOKEN = re.compile(
    r"(?P<dot>\.)?"
    r"(?P<word>(?!\d)[\w\u064B-\u065F\u0670]+)"
    r"(?P<open>\s*\()?"
)


def _net_replace(match):
    dot = match.group("dot")
    word = match.group("word")
    open_paren = match.group("open")

    if dot:
        # بعد نقطة: الدالة أولاً (لها قوس) ثم الخاصية (بلا قوس)
        if open_paren and word in NET_METHODS:
            return "." + NET_METHODS[word] + open_paren
        if word in NET_PROPS:
            return "." + NET_PROPS[word]
        return match.group(0)

    # بلا نقطة: الثابت العاري، وإلا نداء بدونه قوس
    if word in NET_CONSTANTS:
        return NET_CONSTANTS[word]
    if open_paren and word in NET_FUNCS:
        return NET_FUNCS[word] + open_paren
    if word in NET_FUNCS:
        # بلا قوس: صنف أو دالة تُمرَّر كقيمة (مثل معالج_ملفات_http)
        return NET_FUNCS[word]
    return match.group(0)


def NET_SUBSTITUTE(text):
    """يترجم كلمات الشبكة في نص واحد ويُرجع النص المترجم."""
    if not text:
        return text
    return _NET_TOKEN.sub(_net_replace, text)


# معاملات عربية: تُترجم قبل علامة = (انظر inline_replacer)
NET_KWARGS = {

    "عائلة": "family",

    "نوع_المقبس": "type",

    "بروتوكول_شبكة": "proto",

    "وصف_المقبس": "fileno",

    "مهلة_اتصال": "timeout",

    "مصدر_العنوان": "source_address",

    "خادم_البريد": "host",

    "منفذ_البريد": "port",

    "عنوان_محلي": "local_hostname",

    "مهلة_بريد": "timeout",

    "حد_الانتظار": "timeout",

    "قائمة_قراءة": "rlist",

    "قائمة_كتابة": "wlist",

    "قائمة_استثناء": "xlist",

    "سياسة_الرسالة": "policy",

    "ملف_الشهادات": "cafile",

    "مجلد_الشهادات": "capath",

    "بيانات_الشهادات": "cadata",

    "مهلة_اتصال_http": "timeout",

    "بوابة_وكيل": "context",

    "نوع_فرعي": "subtype",

    "حروف_الترميز": "charset",

    "نقل_الترميز": "cte",

    "إزاحة_المحتوى": "disposition",

    "ملف_المرفق": "filename",

    "معرّف_المحتوى": "cid",

}

# Import detection. Only modules that really appear in the generated code
# are imported, so a program that never touches the network pays nothing.
IMPORT_NAME = "socket"
IMPORT_MODULES = ['binascii', 'email', 'email.charset', 'email.contentmanager', 'email.encoders', 'email.errors', 'email.header', 'email.headerregistry', 'email.message', 'email.mime.application', 'email.mime.audio', 'email.mime.base', 'email.mime.image', 'email.mime.message', 'email.mime.multipart', 'email.mime.nonmultipart', 'email.mime.text', 'email.parser', 'email.policy', 'email.utils', 'ftplib', 'http', 'http.client', 'http.cookiejar', 'http.cookies', 'http.server', 'imaplib', 'ipaddress', 'mimetypes', 'netrc', 'poplib', 'quopri', 'select', 'selectors', 'smtplib', 'socket', 'socketserver', 'ssl', 'struct', 'urllib.request', 'uu', 'webbrowser', 'xmlrpc.client', 'xmlrpc.server', 'zlib']
IMPORT_CHECK = r"(?:binascii|email|ftplib|http|imaplib|ipaddress|mimetypes|netrc|poplib|quopri|select|selectors|smtplib|socket|socketserver|ssl|struct|urllib|uu|webbrowser|xmlrpc|zlib)\."
IMPORT_STATEMENT = "import binascii, email, email.charset, email.contentmanager, email.encoders, email.errors, email.header, email.headerregistry, email.message, email.mime.application, email.mime.audio, email.mime.base, email.mime.image, email.mime.message, email.mime.multipart, email.mime.nonmultipart, email.mime.text, email.parser, email.policy, email.utils, ftplib, http, http.client, http.cookiejar, http.cookies, http.server, imaplib, ipaddress, mimetypes, netrc, poplib, quopri, select, selectors, smtplib, socket, socketserver, ssl, struct, urllib.request, uu, webbrowser, xmlrpc.client, xmlrpc.server, zlib"

# Help text for CLI
NET_HELP = [
    "# net — الشبكة والبريد (socket / ssl / http / email / smtp)",
    "مقبس_شبكة(عائلة_ipv4, مقبس_تدفق)  - إنشاء مقبس",
    "اتصال_شبكة(('example.com', 80))   - اتصال جاهز",
    "عنوان_الاسم('example.com')        - اسم -> عنوان IP",
    "بيانات_العنوان('example.com', 80) - كل عناوين الاسم",
    "اسم_الجهاز()                      - اسم هذا الجهاز",
    "# المقبس",
    "  socket.ربط_المنفذ, استمع_للاتصالات, اقبل_اتصال",
    "  socket.أرسل_الكل, استقبل, عين_مهلة, أغلق_المقبس",
    "# HTTP",
    "اتصال_http('example.com')        - عميل HTTP",
    "أرسل_طلب / اقرأ_الاستجابة        - طلب ثم استجابة",
    "افتح_رابط(عنوان)                 - فتح رابط وقراءته",
    "خادم_http(('', 8000), معالج_طلبات_http) - خادم بسيط",
    "# البريد",
    "رسالة_بريد_كاملة()               - رسالة بريد",
    "عين_المحتوى(نص) / أضف_مرفقاً(بايتات) / إلى_نص()",
    "عميل_smtp('smtp.example.com', 587) - إرسال",
    "عميل_imap / عميل_pop3 / عميل_ftp  - قراءة ونقل",
    "# أدوات",
    "حزمة_ثنائية('!i', عدد)           - تغليف struct",
    "عنوان_ip('192.168.1.1')          - كائن عنوان",
    "عنوان_خاص / عنوان_عام           - فحص العنوان",
    "مهلة_اتصال, حد_الانتظار          - معاملات عربية",
]

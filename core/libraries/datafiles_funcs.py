"""
APL — مكتبة البيانات والملفات (datafiles)
==========================================

تُترجم الكلمات العربية إلى أدوات الملفات والأرشيف وهياكل البيانات:

    io
    codecs
    stat
    filecmp
    fileinput
    glob
    fnmatch
    os.path
    zipfile
    tarfile
    gzip
    bz2
    lzma
    pickle
    shelve
    dbm
    dbm.dumb
    marshal
    plistlib
    array
    struct
    bisect
    heapq
    queue
    types
    copy
    copyreg
    weakref
    numbers
    abc
    contextlib
    contextvars
    graphlib
    xml.dom
    xml.dom.minidom
    xml.dom.pulldom
    xml.sax
    xml.sax.handler
    xml.sax.saxutils
    xml.sax.xmlreader
    xml.etree.ElementTree
    xml.parsers.expat
    unicodedata
    difflib
    stringprep
    reprlib
    gettext
    locale

التجميع كما في كل مكتبات APL:

    DF_FUNCS      نداءات على مستوى الوحدة والأصناف
    DF_METHODS    دوال الكائن بعد نقطة
    DF_PROPS      خصائص وسمات أصناف بلا أقواس
    DF_CONSTS     ثوابت تُكتب عارية

عدد العناصر: 2631 (542 نداء + 1195 طريقة + 578 خاصية + 316 ثابت).
كل عنصر تم التحقق منه آلياً مقابل الكائن الحقيقي في Python.
"""

import re


DF_FUNCS = {
    # نداءات الوحدة والأصناف
    # === abc ===
    "ABC_2": "abc.ABC",
    # === numbers ===
    "ABC_وصفي": "numbers.ABCMeta",
    # === codecs ===
    "ASCII_رمّز": "codecs.ascii_encode",
    "ASCII_فكّ_ترميز": "codecs.ascii_decode",
    # === bz2 ===
    "BZ_2_ضاغط": "bz2.BZ2Compressor",
    "BZ_2_فكّ_ضغط": "bz2.BZ2Decompressor",
    "BZ_2_ملف": "bz2.BZ2File",
    # === gettext ===
    "C2PY": "gettext.c2py",
    # === xml ===
    "C_14_N_كاتب_هدف": "xml.etree.ElementTree.C14NWriterTarget",
    # === dbm ===
    "DBM_افتح": "dbm.open",
    "DBM_بسيط_افتح": "dbm.dumb.open",
    # === tarfile ===
    "EX_ملف_كائن": "tarfile.ExFileObject",
    "ITN": "tarfile.itn",
    # === locale ===
    "NL_معلومات_اللغة": "locale.nl_langinfo",
    # === tarfile ===
    "NTI": "tarfile.nti",
    "NTS": "tarfile.nts",
    # === xml ===
    "PI": "xml.etree.ElementTree.PI",
    # === zipfile ===
    "PY_أرشيف_مضغوط_ملف": "zipfile.PyZipFile",
    # === tarfile ===
    "STN": "tarfile.stn",
    # === codecs ===
    "UTF_16_B_رمّز": "codecs.utf_16_be_encode",
    "UTF_16_B_فكّ_ترميز": "codecs.utf_16_be_decode",
    "UTF_16_EX_فكّ_ترميز": "codecs.utf_16_ex_decode",
    "UTF_16_LE_رمّز": "codecs.utf_16_le_encode",
    "UTF_16_LE_فكّ_ترميز": "codecs.utf_16_le_decode",
    "UTF_16_رمّز": "codecs.utf_16_encode",
    "UTF_16_فكّ_ترميز": "codecs.utf_16_decode",
    "UTF_32_B_رمّز": "codecs.utf_32_be_encode",
    "UTF_32_B_فكّ_ترميز": "codecs.utf_32_be_decode",
    "UTF_32_EX_فكّ_ترميز": "codecs.utf_32_ex_decode",
    "UTF_32_LE_رمّز": "codecs.utf_32_le_encode",
    "UTF_32_LE_فكّ_ترميز": "codecs.utf_32_le_decode",
    "UTF_32_رمّز": "codecs.utf_32_encode",
    "UTF_32_فكّ_ترميز": "codecs.utf_32_decode",
    "UTF_7_رمّز": "codecs.utf_7_encode",
    "UTF_7_فكّ_ترميز": "codecs.utf_7_decode",
    "UTF_8_رمّز": "codecs.utf_8_encode",
    "UTF_8_فكّ_ترميز": "codecs.utf_8_decode",
    # === xml ===
    "XML_DOM_صغير_احصل_نموذج_كائن_تنفيذ": "xml.dom.minidom.getDOMImplementation",
    "XML_اسحب_محلل": "xml.etree.ElementTree.XMLPullParser",
    "XML_رشّح_أساس": "xml.sax.saxutils.XMLFilterBase",
    "XML_شجرة_عناصر_عنصر_شجرة_أفرغ": "xml.etree.ElementTree.dump",
    "XML_شجرة_عناصر_عنصر_شجرة_مسافة_بادئة": "xml.etree.ElementTree.indent",
    "XML_شجرة_عناصر_عنصر_شجرة_وحّد": "xml.etree.ElementTree.canonicalize",
    "XML_محلل": "xml.etree.ElementTree.XMLParser",
    "XML_محلل_ساكس_خطأ_معالج": "xml.sax.ErrorHandler",
    "XML_مولّد": "xml.sax.saxutils.XMLGenerator",
    "XML_نموذج_كائن_DOM_صغير_ترميز": "xml.dom.minidom.Notation",
    "XML_نموذج_كائن_DOM_صغير_نص": "xml.dom.minidom.Text",
    "XML_نموذج_كائن_اسحب_نموذج_كائن_حلل": "xml.dom.pulldom.parse",
    "XML_نموذج_كائن_اسحب_نموذج_كائن_خطأ_معالج": "xml.dom.pulldom.ErrorHandler",
    "XML_نموذج_كائن_غير_صالح_تعديل_خطأ": "xml.dom.InvalidModificationErr",
    "XML_نموذج_كائن_غير_صالح_حالة_خطأ": "xml.dom.InvalidStateErr",
    # === shelve ===
    "bsd_قاعدة_رف": "shelve.BsdDbShelf",
    # === bisect ===
    "أدرج_مرتّباً": "bisect.insort",
    "أدرج_مرتّباً_يسار": "bisect.insort_left",
    # === contextlib ===
    "أدوات_السياق_مدير_سياق": "contextlib.contextmanager",
    # === zipfile ===
    "أرشيف_مضغوط_امتداد_ملف": "zipfile.ZipExtFile",
    # === heapq ===
    "أصغر_ن": "heapq.nsmallest",
    # === copyreg ===
    "أضف_امتداد": "copyreg.add_extension",
    # === marshal ===
    "أفرغ": "marshal.dump",
    # === pickle ===
    "أفرغ_بايكن": "pickle.dumps",
    # === plistlib ===
    "أفرغ_قائمة": "plistlib.dumps",
    # === marshal ===
    "أفرغ_مارشال": "marshal.dumps",
    # === locale ===
    "أقليّم": "locale.localize",
    # === heapq ===
    "أكبر_ن": "heapq.nlargest",
    # === locale ===
    "ألغ_الإقليم": "locale.delocalize",
    # === codecs ===
    "ألغِ_التسجيل": "codecs.unregister",
    # === queue ===
    "أوقف_لأسفل": "queue.ShutDown",
    # === dbm ===
    "أي_قاعدة": "dbm.whichdb",
    # === pickle ===
    "أي_وحدة": "pickle.whichmodule",
    # === fileinput ===
    "إدخال": "fileinput.input",
    # === io ===
    "إدخال_إخراج_أساس": "io.IOBase",
    # === fileinput ===
    "إدخال_اسم_ملف": "fileinput.filename",
    # === xml ===
    "إدخال_مصدر": "xml.sax.InputSource",
    # === contextlib ===
    "إعادة_توجيه_إخراج_قياسي": "contextlib.redirect_stdout",
    "إعادة_توجيه_خطأ_قياسي": "contextlib.redirect_stderr",
    "إغلاق_غير_متزامن": "contextlib.aclosing",
    # === xml ===
    "إكسبات_خطأ": "xml.parsers.expat.ExpatError",
    "إلى_قائمة_نصوص": "xml.etree.ElementTree.tostringlist",
    "إلى_نص_2": "xml.etree.ElementTree.tostring",
    # === unicodedata ===
    "ابحث_عن_محرف": "unicodedata.lookup",
    # === codecs ===
    "ابحث_عن_مرمّز": "codecs.lookup",
    # === bisect ===
    "ابحث_موضع": "bisect.bisect",
    "ابحث_يساراً": "bisect.bisect_left",
    # === locale ===
    "اتفاقيات_الإقليم": "locale.localeconv",
    # === copyreg ===
    "احذف_امتداد": "copyreg.remove_extension",
    # === struct ===
    "احسب_الحجم": "struct.calcsize",
    # === tarfile ===
    "احسب_مجاميع_الفحص": "tarfile.calc_chksums",
    # === types ===
    "احصل_أصلي_أساس": "types.get_original_bases",
    # === abc ===
    "احصل_ذاكرة_مؤقتة_رمز": "abc.get_cache_token",
    # === difflib ===
    "احصل_على_أقرب_التطابقات": "difflib.get_close_matches",
    # === locale ===
    "احصل_على_الإقليم": "locale.getlocale",
    "احصل_على_الإقليم_الافتراضي": "locale.getdefaultlocale",
    "احصل_على_الترميز": "locale.getencoding",
    "احصل_على_الترميز_المفضّل": "locale.getpreferredencoding",
    # === codecs ===
    "احصل_على_القارئ": "codecs.getreader",
    "احصل_على_الكاتب": "codecs.getwriter",
    # === weakref ===
    "احصل_على_المراجع_الضعيفة": "weakref.getweakrefs",
    # === codecs ===
    "احصل_على_المفكّك": "codecs.getdecoder",
    "احصل_على_المفكّك_التصاعدي": "codecs.getincrementaldecoder",
    "احصل_على_المُرمّز": "codecs.getencoder",
    "احصل_على_المُرمّز_التصاعدي": "codecs.getincrementalencoder",
    # === gettext ===
    "احصل_على_النص": "gettext.gettext",
    "احصل_على_النص_ابحث": "gettext.find",
    "احصل_على_النص_الجمع_لنطاق": "gettext.dngettext",
    "احصل_على_النص_جمع_لنطاق": "gettext.dnpgettext",
    "احصل_على_النص_سياق_2": "gettext.dpgettext",
    "احصل_على_النص_فهرس": "gettext.Catalog",
    # === locale ===
    "احصل_على_النص_للفئة": "locale.dcgettext",
    "احصل_على_النص_لنطاق": "locale.dgettext",
    # === weakref ===
    "احصل_على_عدد_المراجع_الضعيفة": "weakref.getweakrefcount",
    # === gettext ===
    "احصل_على_نص_الجمع": "gettext.ngettext",
    "احصل_على_نص_النطاق": "gettext.dgettext",
    "احصل_على_نص_بسياق": "gettext.pgettext",
    "احصل_على_نص_جمع_سياق": "gettext.npgettext",
    # === reprlib ===
    "احصل_معرّف": "reprlib.get_ident",
    # === xml ===
    "احصل_نموذج_كائن_تنفيذ": "xml.dom.getDOMImplementation",
    # === contextlib ===
    "اخرج_مكدس": "contextlib.ExitStack",
    # === heapq ===
    "ادفع_للكومة": "heapq.heappush",
    "ادفع_للكومة_أقصى": "heapq.heappush_max",
    "ادفع_واسحب": "heapq.heappushpop",
    "ادفع_واسحب_أقصى": "heapq.heappushpop_max",
    # === os ===
    "اربط_مسارين": "os.path.join",
    # === gettext ===
    "اربط_نطاق_النص": "gettext.bindtextdomain",
    # === locale ===
    "اربط_نطاق_النص_مجموعة_الرموز": "locale.bind_textdomain_codeset",
    # === codecs ===
    "استبدال_شرطة_أخطاء": "codecs.backslashreplace_errors",
    "استبدال_مرجع_إكس_إم_إم_أخطاء": "codecs.xmlcharrefreplace_errors",
    "استبدل_أخطاء": "codecs.replace_errors",
    # === heapq ===
    "استبدل_القمة": "heapq.heapreplace",
    "استبدل_قمة_الكومة_أقصى": "heapq.heapreplace_max",
    # === tarfile ===
    "استخرج_خطأ": "tarfile.ExtractError",
    # === difflib ===
    "استعد": "difflib.restore",
    # === heapq ===
    "اسحب_من_الكومة": "heapq.heappop",
    "اسحب_من_الكومة_أقصى": "heapq.heappop_max",
    # === xml ===
    "اسحب_نموذج_كائن": "xml.dom.pulldom.PullDOM",
    # === os ===
    "اسم_الأساس": "os.path.basename",
    "اسم_المجلد": "os.path.dirname",
    # === unicodedata ===
    "اسم_المحرف": "unicodedata.name",
    # === codecs ===
    "اسم_بديل_أخطاء": "codecs.namereplace_errors",
    # === shelve ===
    "اسم_ملف_القاعدة_رف": "shelve.DbfilenameShelf",
    # === gzip ===
    "اضغط": "gzip.compress",
    # === codecs ===
    "اعمل_ترميز_خريطة": "codecs.make_encoding_map",
    # === xml ===
    "اعمل_محللاً": "xml.sax.make_parser",
    # === codecs ===
    "اعمل_هوية_قاموس": "codecs.make_identity_dict",
    # === io ===
    "افتح": "io.open",
    # === bz2 ===
    "افتح_bz2_2": "bz2.open",
    # === gzip ===
    "افتح_gzip_2": "gzip.open",
    # === lzma ===
    "افتح_lzma": "lzma.open",
    # === tarfile ===
    "افتح_شريطاً_2": "tarfile.open",
    # === io ===
    "افتح_كود": "io.open_code",
    # === codecs ===
    "افتح_مرمّزاً": "codecs.open",
    # === os ===
    "افصل_الامتداد": "os.path.splitext",
    "افصل_الجذر": "os.path.splitroot",
    "افصل_المحرك": "os.path.splitdrive",
    "افصل_مسار": "os.path.split",
    # === xml ===
    "اقتبس_سمة": "xml.sax.saxutils.quoteattr",
    # === pickle ===
    "اقرأ_بايكن": "pickle.load",
    # === tarfile ===
    "اقرأ_خطأ": "tarfile.ReadError",
    # === xml ===
    "اقرأ_فقط_تسلسلي_مسمّى_عُقدة_خريطة": "xml.dom.minidom.ReadOnlySequentialNamedNodeMap",
    # === plistlib ===
    "اقرأ_قائمة": "plistlib.load",
    # === contextlib ===
    "اكبح": "contextlib.suppress",
    # === gzip ===
    "اكتب32": "gzip.write32u",
    # === pickle ===
    "اكتب_بايكن": "pickle.dump",
    # === plistlib ===
    "اكتب_قائمة": "plistlib.dump",
    # === copyreg ===
    "امسح_امتداد_ذاكرة_مؤقتة": "copyreg.clear_extension_cache",
    # === copy ===
    "انسخ_2": "copy.copy",
    "انسخ_استبدل": "copy.replace",
    "انسخ_خطأ": "copy.Error",
    # === contextvars ===
    "انسخ_سياق": "contextvars.copy_context",
    # === copy ===
    "انسخ_عميقاً_2": "copy.deepcopy",
    # === tarfile ===
    "انسخ_كائن_ملف": "tarfile.copyfileobj",
    # === xml ===
    "اهرب_إكس_إم_إم": "xml.sax.saxutils.escape",
    # === os ===
    "بادئة_مشتركة": "os.path.commonprefix",
    # === tarfile ===
    "بالكامل_موثوق_رشّح": "tarfile.fully_trusted_filter",
    # === io ===
    "بايت_تدفق": "io.BytesIO",
    # === copyreg ===
    "بايكن_أعلى": "copyreg.pickle_super",
    "بايكن_اتحاد": "copyreg.pickle_union",
    # === pickle ===
    "بايكن_احزم": "pickle.pack",
    "بايكن_خطأ_2": "pickle.PickleError",
    "بايكن_مخزن_مؤقت": "pickle.PickleBuffer",
    # === copyreg ===
    "بايكن_مركّب": "copyreg.pickle_complex",
    # === codecs ===
    "بحث_خطأ": "codecs.lookup_error",
    # === glob ===
    "بحث_نمطي0": "glob.glob0",
    "بحث_نمطي1": "glob.glob1",
    "بحث_نمطي_2": "glob.glob",
    "بحث_نمطي_هرب": "glob.escape",
    # === types ===
    "بسيط_نطاق_اسم": "types.SimpleNamespace",
    # === xml ===
    "بلا_أبناء": "xml.dom.minidom.Childless",
    "بلا_بيانات_مسموح_خطأ": "xml.dom.NoDataAllowedErr",
    "بلا_تعديل_مسموح_خطأ": "xml.dom.NoModificationAllowedErr",
    # === weakref ===
    "بمفاتيح_مرجع": "weakref.KeyedRef",
    # === struct ===
    "بنية": "struct.Struct",
    "بنية_احزم_إلى": "struct.pack_into",
    "بنية_خطأ": "struct.error",
    "بنية_فكّ_الحزمة_من": "struct.unpack_from",
    "بنية_كرّر_فكّ_الحزمة": "struct.iter_unpack",
    # === xml ===
    "بيانات_ج_قسم": "xml.dom.minidom.CDATASection",
    # === tarfile ===
    "بيانات_رشّح": "tarfile.data_filter",
    # === unicodedata ===
    "بيانات_يونيكود_تفكيك": "unicodedata.decomposition",
    "بيانات_يونيكود_ثنائي_الاتجاه": "unicodedata.bidirectional",
    "بيانات_يونيكود_معكوس": "unicodedata.mirrored",
    # === codecs ===
    "تجاهل_أخطاء": "codecs.ignore_errors",
    # === xml ===
    "تحقق_خطأ": "xml.dom.ValidationErr",
    # === pickle ===
    "تحويل_بايكن_خطأ": "pickle.PicklingError",
    # === tarfile ===
    "تدفق_خطأ": "tarfile.StreamError",
    # === codecs ===
    "تدفق_قارئ": "codecs.StreamReader",
    "تدفق_قارئ_كاتب": "codecs.StreamReaderWriter",
    "تدفق_كاتب": "codecs.StreamWriter",
    "تدفق_مُعادِل_الترميز": "codecs.StreamRecoder",
    # === glob ===
    "ترجم": "glob.translate",
    # === xml ===
    "تسلسل_هرمي_اطلب_خطأ": "xml.dom.HierarchyRequestErr",
    # === io ===
    "تصاعدي_سطر_جديد_مفكّك": "io.IncrementalNewlineDecoder",
    # === xml ===
    "تصاعدي_محلل": "xml.sax.xmlreader.IncrementalParser",
    # === codecs ===
    "تصاعدي_مرمّز": "codecs.IncrementalEncoder",
    "تصاعدي_مفكّك": "codecs.IncrementalDecoder",
    # === types ===
    "تعاونية": "types.coroutine",
    # === xml ===
    "تعريف_نوع_المستند_معالج": "xml.sax.handler.DTDHandler",
    "تعليق": "xml.dom.minidom.Comment",
    "تعليق_عنصر": "xml.etree.ElementTree.Comment",
    # === glob ===
    "تكرار_بحث_نمطي": "glob.iglob",
    # === reprlib ===
    "تكراري_تمثيل": "reprlib.recursive_repr",
    # === gettext ===
    "تنسيق_gnu_ترجمات": "gettext.GNUTranslations",
    # === filecmp ===
    "توضيحي": "filecmp.demo",
    # === gettext ===
    "ثبّت": "gettext.install",
    # === types ===
    "جديد_صنف": "types.new_class",
    # === xml ===
    "جهّز_إدخال_مصدر": "xml.sax.saxutils.prepare_input_source",
    # === types ===
    "جهّز_صنف": "types.prepare_class",
    # === os ===
    "حجم_ملف_2": "os.path.getsize",
    # === abc ===
    "حدّث_دوال_مجردة": "abc.update_abstractmethods",
    # === xml ===
    "حرف_بيانات": "xml.dom.minidom.CharacterData",
    # === numbers ===
    "حقيقي": "numbers.Real",
    # === xml ===
    "حلل_خطأ": "xml.etree.ElementTree.ParseError",
    "حلل_ساكس": "xml.sax.parse",
    "حلل_شجرة": "xml.etree.ElementTree.parse",
    "حلل_مستنداً": "xml.dom.minidom.parse",
    "حلل_نص": "xml.dom.pulldom.parseString",
    "حلل_نصاً": "xml.dom.minidom.parseString",
    "حلل_نصاً_ساكس": "xml.sax.parseString",
    # === types ===
    "حلّ_أساس": "types.resolve_bases",
    # === pickle ===
    "حمّل_بايكن": "pickle.loads",
    # === plistlib ===
    "حمّل_قائمة": "plistlib.loads",
    # === marshal ===
    "حمّل_مارشال": "marshal.loads",
    # === heapq ===
    "حوّل_إلى_كومة": "heapq.heapify",
    "حوّل_إلى_كومة_أقصى": "heapq.heapify_max",
    # === locale ===
    "حوّل_للمقارنة": "locale.strxfrm",
    # === tarfile ===
    "خارج_وجهة_خطأ": "tarfile.OutsideDestinationError",
    "خاص_ملف_خطأ": "tarfile.SpecialFileError",
    # === io ===
    "خام_إدخال_إخراج_أساس": "io.RawIOBase",
    # === codecs ===
    "خام_يونيكود_هرب_رمّز": "codecs.raw_unicode_escape_encode",
    "خام_يونيكود_هرب_فكّ_ترميز": "codecs.raw_unicode_escape_decode",
    "خريطة_المحارف_ابنِ": "codecs.charmap_build",
    "خريطة_المحارف_رمّز": "codecs.charmap_encode",
    "خريطة_المحارف_فكّ_ترميز": "codecs.charmap_decode",
    # === stringprep ===
    "خريطة_جدول_B2": "stringprep.map_table_b2",
    "خريطة_جدول_B3": "stringprep.map_table_b3",
    # === graphlib ===
    "خطأ_دورة": "graphlib.CycleError",
    # === xml ===
    "خطأ_مستند_خطأ": "xml.dom.WrongDocumentErr",
    "خطأ_نص": "xml.parsers.expat.ErrorString",
    # === fileinput ===
    "خطاف_مرمّز": "fileinput.hook_encoded",
    "خطاف_مضغوط": "fileinput.hook_compressed",
    # === abc ===
    "دالة_ساكنة_مجردة": "abc.abstractstaticmethod",
    "دالة_صنف_مجردة": "abc.abstractclassmethod",
    # === types ===
    "ديناميكي_صنف_سمة": "types.DynamicClassAttribute",
    # === tarfile ===
    "رأس_خطأ": "tarfile.HeaderError",
    # === unicodedata ===
    "رتبة_التركيب": "unicodedata.combining",
    # === fnmatch ===
    "رشّح_المعكوس": "fnmatch.filterfalse",
    # === tarfile ===
    "رشّح_خطأ": "tarfile.FilterError",
    # === fnmatch ===
    "رشّح_نمطياً": "fnmatch.filter",
    # === shelve ===
    "رف": "shelve.Shelf",
    "رفوف_افتح": "shelve.open",
    # === unicodedata ===
    "رقم_يونيكود": "unicodedata.digit",
    # === codecs ===
    "رمّز": "codecs.encode",
    # === pickle ===
    "رمّز_طويل": "pickle.encode_long",
    # === copyreg ===
    "سجّل_بايكن": "copyreg.pickle",
    # === codecs ===
    "سجّل_خطأ": "codecs.register_error",
    # === xml ===
    "سجّل_نطاقاً": "xml.etree.ElementTree.register_namespace",
    "سجّل_نموذج_كائن_تنفيذ": "xml.dom.registerDOMImplementation",
    "سمات_NS_تنفيذ": "xml.sax.xmlreader.AttributesNSImpl",
    "سمات_تنفيذ": "xml.sax.xmlreader.AttributesImpl",
    "سمة": "xml.dom.minidom.Attr",
    "سمة_قائمة": "xml.dom.minidom.AttributeList",
    # === zipfile ===
    "سيئ_أرشيف_مضغوط_ملف": "zipfile.BadZipFile",
    # === gzip ===
    "سيئ_ضغط_gzip_ملف": "gzip.BadGzipFile",
    # === contextvars ===
    "سياق": "contextvars.Context",
    # === contextlib ===
    "سياق_فارغ": "contextlib.nullcontext",
    # === contextvars ===
    "سياق_متغير": "contextvars.ContextVar",
    "سياق_متغيرات_رمز": "contextvars.Token",
    # === contextlib ===
    "سياق_مُزيّن": "contextlib.ContextDecorator",
    # === xml ===
    "شجرة_باني": "xml.etree.ElementTree.TreeBuilder",
    "شجرة_عناصر": "xml.etree.ElementTree.ElementTree",
    "شجرة_عناصر_عنصر_شجرة_XML": "xml.etree.ElementTree.XML",
    # === tarfile ===
    "شريط_أرشيف_خطأ": "tarfile.TarError",
    "شريط_أرشيف_رشّح": "tarfile.tar_filter",
    # === codecs ===
    "صارم_أخطاء": "codecs.strict_errors",
    # === numbers ===
    "صحيح_2": "numbers.Integral",
    # === xml ===
    "صياغة_خطأ": "xml.dom.SyntaxErr",
    # === weakref ===
    "ضعيف_دالة": "weakref.WeakMethod",
    # === bz2 ===
    "ضغط_bz2_اضغط": "bz2.compress",
    "ضغط_bz2_فكّ_الضغط": "bz2.decompress",
    # === gzip ===
    "ضغط_gzip_رئيسي": "gzip.main",
    # === lzma ===
    "ضغط_lzma_اضغط": "lzma.compress",
    "ضغط_lzma_خطأ": "lzma.LZMAError",
    # === zipfile ===
    "ضغط_lzma_ضاغط": "zipfile.LZMACompressor",
    # === lzma ===
    "ضغط_lzma_ضاغط_2": "lzma.LZMACompressor",
    "ضغط_lzma_فكّ_الضغط": "lzma.decompress",
    # === zipfile ===
    "ضغط_lzma_فكّ_ضغط": "zipfile.LZMADecompressor",
    # === lzma ===
    "ضغط_lzma_فكّ_ضغط_2": "lzma.LZMADecompressor",
    "ضغط_lzma_ملف": "lzma.LZMAFile",
    # === tarfile ===
    "ضغط_خطأ": "tarfile.CompressionError",
    # === difflib ===
    "طابق": "difflib.Match",
    # === fnmatch ===
    "طابق_نمطياً": "fnmatch.fnmatch",
    "طابق_نمطياً_بالحالة": "fnmatch.fnmatchcase",
    "طابق_نمطياً_ترجم": "fnmatch.translate",
    # === queue ===
    "طابور_2": "queue.Queue",
    # === xml ===
    "طابور_اسم": "xml.etree.ElementTree.QName",
    # === queue ===
    "طابور_بأولوية": "queue.PriorityQueue",
    "طابور_بسيط": "queue.SimpleQueue",
    "طابور_عكسي": "queue.LifoQueue",
    "طابور_فارغ_2": "queue.Empty",
    "طابور_ممتلئ_2": "queue.Full",
    "طابور_وقت": "queue.time",
    # === io ===
    "عام_اسم_مستعار": "io.GenericAlias",
    # === numbers ===
    "عدد_2": "numbers.Number",
    # === gettext ===
    "عدم_ترجمات": "gettext.NullTranslations",
    # === unicodedata ===
    "عرض_آسيوي": "unicodedata.east_asian_width",
    # === xml ===
    "عرّف_خاصية": "xml.dom.minidom.defproperty",
    # === locale ===
    "عملة": "locale.currency",
    # === xml ===
    "عنصر_2": "xml.dom.minidom.Element",
    "عنصر_3": "xml.etree.ElementTree.Element",
    "عنصر_فرعي": "xml.etree.ElementTree.SubElement",
    "عنصر_معلومات": "xml.dom.minidom.ElementInfo",
    # === locale ===
    "عيّن_الإقليم": "locale.setlocale",
    # === xml ===
    "عُقدة": "xml.dom.Node",
    "عُقدة_2": "xml.dom.minidom.Node",
    # === contextlib ===
    "غلاف": "contextlib.wraps",
    # === io ===
    "غلاف_نصي": "io.TextIOWrapper",
    # === xml ===
    "غير_صالح_حرف_خطأ": "xml.dom.InvalidCharacterErr",
    # === tarfile ===
    "غير_صالح_رأس_خطأ": "tarfile.InvalidHeaderError",
    # === plistlib ===
    "غير_صالح_ملف_استثناء": "plistlib.InvalidFileException",
    # === xml ===
    "غير_صالح_وصول_خطأ": "xml.dom.InvalidAccessErr",
    # === contextlib ===
    "غير_متزامن_اخرج_مكدس": "contextlib.AsyncExitStack",
    "غير_متزامن_سياق_مُزيّن": "contextlib.AsyncContextDecorator",
    # === io ===
    "غير_مدعوم_عملية": "io.UnsupportedOperation",
    # === contextlib ===
    "غيّر_المجلد": "contextlib.chdir",
    # === unicodedata ===
    "فئة_يونيكود": "unicodedata.category",
    # === tarfile ===
    "فارغ_رأس_خطأ": "tarfile.EmptyHeaderError",
    # === zipfile ===
    "فحص_تكرار32": "zipfile.crc32",
    # === difflib ===
    "فرق_بايتات": "difflib.diff_bytes",
    "فرق_بسياق": "difflib.context_diff",
    "فرق_متجاور": "difflib.ndiff",
    "فرق_موحّد": "difflib.unified_diff",
    # === pickle ===
    "فك_التحويل_خطأ": "pickle.UnpicklingError",
    "فكّ_الحزمة": "pickle.unpack",
    # === gzip ===
    "فكّ_الضغط": "gzip.decompress",
    # === codecs ===
    "فكّ_ترميز": "codecs.decode",
    # === pickle ===
    "فكّ_ترميز_طويل": "pickle.decode_long",
    # === xml ===
    "فكّ_هروب_إكس_إم_إم": "xml.sax.saxutils.unescape",
    "فهرس_حجم_خطأ": "xml.dom.IndexSizeErr",
    # === stringprep ===
    "في_جدول_A1": "stringprep.in_table_a1",
    "في_جدول_B1": "stringprep.in_table_b1",
    "في_جدول_D1": "stringprep.in_table_d1",
    "في_جدول_D2": "stringprep.in_table_d2",
    "في_جدول_توحيد11": "stringprep.in_table_c11",
    "في_جدول_توحيد11_توحيد12": "stringprep.in_table_c11_c12",
    "في_جدول_توحيد12": "stringprep.in_table_c12",
    "في_جدول_توحيد21": "stringprep.in_table_c21",
    "في_جدول_توحيد21_توحيد22": "stringprep.in_table_c21_c22",
    "في_جدول_توحيد22": "stringprep.in_table_c22",
    "في_جدول_توحيد3": "stringprep.in_table_c3",
    "في_جدول_توحيد4": "stringprep.in_table_c4",
    "في_جدول_توحيد5": "stringprep.in_table_c5",
    "في_جدول_توحيد6": "stringprep.in_table_c6",
    "في_جدول_توحيد7": "stringprep.in_table_c7",
    "في_جدول_توحيد8": "stringprep.in_table_c8",
    "في_جدول_توحيد9": "stringprep.in_table_c9",
    # === plistlib ===
    "قائمة_نسّق": "plistlib.PlistFormat",
    # === weakref ===
    "قابل_للاستدعاء_وكيل_نوع": "weakref.CallableProxyType",
    # === io ===
    "قارئ": "io.Reader",
    # === xml ===
    "قارئ_إكس_إم_إم": "xml.sax.xmlreader.XMLReader",
    # === io ===
    "قارئ_مخزّن": "io.BufferedReader",
    # === filecmp ===
    "قارن": "filecmp.cmp",
    "قارن_الملفات": "filecmp.cmpfiles",
    # === locale ===
    "قارن_نصياً": "locale.strcoll",
    # === weakref ===
    "قاموس_قيم_ضعيفة": "weakref.WeakValueDictionary",
    "قاموس_مفاتيح_ضعيفة": "weakref.WeakKeyDictionary",
    # === unicodedata ===
    "قيمة_عددية": "unicodedata.numeric",
    "قيمة_عشرية": "unicodedata.decimal",
    # === io ===
    "كاتب": "io.Writer",
    "كاتب_مخزّن": "io.BufferedWriter",
    # === zipfile ===
    "كبير_أرشيف_مضغوط_ملف": "zipfile.LargeZipFile",
    # === xml ===
    "كرّر_التحليل": "xml.etree.ElementTree.iterparse",
    # === codecs ===
    "كرّر_الترميز": "codecs.iterencode",
    "كرّر_الفك": "codecs.iterdecode",
    # === heapq ===
    "كومة_ادمج": "heapq.merge",
    # === xml ===
    "كيان": "xml.dom.minidom.Entity",
    "كيان_محلّل": "xml.sax.handler.EntityResolver",
    "لا_مدعوم_خطأ": "xml.dom.NotSupportedErr",
    "لا_موجود_خطأ": "xml.dom.NotFoundErr",
    # === codecs ===
    "لاتيني_1_رمّز": "codecs.latin_1_encode",
    "لاتيني_1_فكّ_ترميز": "codecs.latin_1_decode",
    # === tarfile ===
    "لاحق_رأس_خطأ": "tarfile.SubsequentHeaderError",
    # === glob ===
    "له_سحري": "glob.has_magic",
    # === marshal ===
    "مارشال_حمّل": "marshal.load",
    # === reprlib ===
    "مثّل": "reprlib.repr",
    # === numbers ===
    "مجرد_دالة": "numbers.abstractmethod",
    # === abc ===
    "مجرد_سمة_صنف": "abc.abstractproperty",
    # === contextlib ===
    "مجرد_سياق_مدير": "contextlib.AbstractContextManager",
    "مجرد_غير_متزامن_سياق_مدير": "contextlib.AbstractAsyncContextManager",
    # === xml ===
    "محتوى_معالج": "xml.sax.ContentHandler",
    "محدّد": "xml.sax.xmlreader.Locator",
    # === plistlib ===
    "محلل_أنشئ": "plistlib.ParserCreate",
    # === xml ===
    "محلل_ساكس_2_نموذج_كائن": "xml.dom.pulldom.SAX2DOM",
    # === locale ===
    "محلي_احصل_على_النص": "locale.gettext",
    "محلي_اربط_نطاق_النص": "locale.bindtextdomain",
    "محلي_خطأ": "locale.Error",
    "محلي_نص": "locale.str",
    "محلي_نطاق_النص": "locale.textdomain",
    # === codecs ===
    "مخزن_القراءة_رمّز": "codecs.readbuffer_encode",
    # === contextlib ===
    "مدير_سياق_غير_متزامن": "contextlib.asynccontextmanager",
    # === graphlib ===
    "مرتّب_توبولوجي": "graphlib.TopologicalSorter",
    # === weakref ===
    "مرجع_ضعيف_أنهِ": "weakref.finalize",
    "مرجع_نوع": "weakref.ReferenceType",
    # === numbers ===
    "مركّب": "numbers.Complex",
    # === codecs ===
    "مرمّز": "codecs.Codec",
    "مرمّز_سجّل": "codecs.register",
    "مرمّز_معلومات": "codecs.CodecInfo",
    "مرمّز_ملف": "codecs.EncodedFile",
    # === os ===
    "مسار_حقيقي": "os.path.realpath",
    "مسار_مشترك": "os.path.commonpath",
    "مسار_مطلق_2": "os.path.abspath",
    "مسار_موجود_2": "os.path.exists",
    "مسار_نسبي_2": "os.path.relpath",
    # === xml ===
    "مستخدم_بيانات_معالج": "xml.dom.UserDataHandler",
    "مستند": "xml.dom.minidom.Document",
    "مستند_جزء": "xml.dom.minidom.DocumentFragment",
    "مستند_نوع": "xml.dom.minidom.DocumentType",
    # === array ===
    "مصفوفة_نوع": "array.ArrayType",
    # === difflib ===
    "مطابق_التسلسل": "difflib.SequenceMatcher",
    # === tarfile ===
    "مطلق_مسار_خطأ": "tarfile.AbsolutePathError",
    "مطلق_وصلة_خطأ": "tarfile.AbsoluteLinkError",
    # === xml ===
    "معالجة_تعليمة": "xml.dom.minidom.ProcessingInstruction",
    "معجمي_معالج": "xml.sax.handler.LexicalHandler",
    "معرف_إكس_إم_إم": "xml.etree.ElementTree.XMLID",
    # === tarfile ===
    "معلومات_شريط_2": "tarfile.TarInfo",
    # === zipfile ===
    "معلومات_مضغوط": "zipfile.ZipInfo",
    # === unicodedata ===
    "معيار_يونيكود": "unicodedata.UCD",
    # === difflib ===
    "مفرّق": "difflib.Differ",
    "مفرّق_HTML": "difflib.HtmlDiff",
    # === pickle ===
    "مفكّك_تحويل": "pickle.Unpickler",
    # === filecmp ===
    "مقارنة_مجلدات": "filecmp.dircmp",
    # === tarfile ===
    "مقطوع_رأس_خطأ": "tarfile.TruncatedHeaderError",
    # === plistlib ===
    "مكتبة_القوائم_UID": "plistlib.UID",
    # === gzip ===
    "ملف_gzip": "gzip.GzipFile",
    # === fileinput ===
    "ملف_إدخال": "fileinput.FileInput",
    "ملف_إدخال_أغلق_2": "fileinput.close",
    # === io ===
    "ملف_إدخال_إخراج": "io.FileIO",
    # === fileinput ===
    "ملف_إدخال_الملف_التالي": "fileinput.nextfile",
    "ملف_إدخال_رقم_السطر_2": "fileinput.lineno",
    "ملف_إدخال_رقم_الملف_2": "fileinput.fileno",
    "ملف_إدخال_سطر_الملف": "fileinput.filelineno",
    "ملف_إدخال_هو_السطر_الأول": "fileinput.isfirstline",
    # === tarfile ===
    "ملف_شريط": "tarfile.TarFile",
    "ملف_شريط_رئيسي": "tarfile.main",
    # === filecmp ===
    "ملف_قارن_امسح_ذاكرة_مؤقتة": "filecmp.clear_cache",
    # === zipfile ===
    "ملف_مضغوط_2": "zipfile.ZipFile",
    "ملف_مضغوط_رئيسي": "zipfile.main",
    # === fileinput ===
    "ملف_هو_إدخال_قياسي": "fileinput.isstdin",
    # === xml ===
    "من_قائمة_نصوص": "xml.etree.ElementTree.fromstringlist",
    # === locale ===
    "من_نص_إلى_صحيح": "locale.atoi",
    "من_نص_إلى_عائم": "locale.atof",
    # === copyreg ===
    "منشئ": "copyreg.constructor",
    # === os ===
    "موجود_بترابط": "os.path.lexists",
    # === xml ===
    "مُتعرّف": "xml.dom.minidom.Identified",
    # === pickle ===
    "مُحوِّل": "pickle.Pickler",
    # === io ===
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس": "io.BufferedIOBase",
    # === codecs ===
    "مُخزّن_مؤقتاً_تصاعدي_مرمّز": "codecs.BufferedIncrementalEncoder",
    "مُخزّن_مؤقتاً_تصاعدي_مفكّك": "codecs.BufferedIncrementalDecoder",
    # === io ===
    "مُخزّن_مؤقتاً_عشوائي": "io.BufferedRandom",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج": "io.BufferedRWPair",
    # === xml ===
    "مُستعمَل_سمة_خطأ": "xml.dom.InuseAttributeErr",
    # === reprlib ===
    "مُمثِّل": "reprlib.Repr",
    # === numbers ===
    "نسبي": "numbers.Rational",
    # === locale ===
    "نسّق_نص": "locale.format_string",
    # === stat ===
    "نص_IMODE": "stat.S_IMODE",
    # === io ===
    "نص_إدخال_إخراج_أساس": "io.TextIOBase",
    "نص_تدفق": "io.StringIO",
    "نص_ترميز": "io.text_encoding",
    # === xml ===
    "نص_نموذج_حجم_خطأ": "xml.dom.DomstringSizeErr",
    # === stat ===
    "نص_نوع_ملف": "stat.S_IFMT",
    "نص_هو_أنبوب": "stat.S_ISFIFO",
    "نص_هو_باب": "stat.S_ISDOOR",
    "نص_هو_جهاز_حرفي": "stat.S_ISCHR",
    "نص_هو_جهاز_كتلي": "stat.S_ISBLK",
    "نص_هو_رابط_صلب": "stat.S_ISLNK",
    "نص_هو_سوار": "stat.S_ISWHT",
    "نص_هو_مجلد": "stat.S_ISDIR",
    "نص_هو_مقبس": "stat.S_ISSOCK",
    "نص_هو_ملف_عادي": "stat.S_ISREG",
    "نص_هو_منفذ": "stat.S_ISPORT",
    # === xml ===
    "نطاق_اسم_خطأ": "xml.dom.NamespaceErr",
    # === gettext ===
    "نطاق_النص": "gettext.textdomain",
    # === os ===
    "نفس_الإحصاء": "os.path.samestat",
    "نفس_الملف": "os.path.samefile",
    "نفس_الملف_المفتوح": "os.path.sameopenfile",
    # === xml ===
    "نموذج_كائن_استثناء": "xml.dom.DOMException",
    "نموذج_كائن_تنفيذ": "xml.dom.minidom.DOMImplementation",
    "نموذج_كائن_حدث_تدفق": "xml.dom.pulldom.DOMEventStream",
    # === tarfile ===
    "نهاية_الملف_رأس_خطأ": "tarfile.EOFHeaderError",
    # === xml ===
    "نوع_معلومات": "xml.dom.minidom.TypeInfo",
    # === codecs ===
    "هرب_رمّز": "codecs.escape_encode",
    "هرب_فكّ_ترميز": "codecs.escape_decode",
    # === lzma ===
    "هو_تحقق_مدعوم": "lzma.is_check_supported",
    # === difflib ===
    "هو_حرف_همل": "difflib.IS_CHARACTER_JUNK",
    # === os ===
    "هو_رابط": "os.path.islink",
    # === difflib ===
    "هو_سطر_همل": "difflib.IS_LINE_JUNK",
    # === xml ===
    "هو_عنصر": "xml.etree.ElementTree.iselement",
    # === os ===
    "هو_مجلد_2": "os.path.isdir",
    "هو_محرك_جهاز": "os.path.isdevdrive",
    "هو_مطلق": "os.path.isabs",
    "هو_ملف_2": "os.path.isfile",
    # === tarfile ===
    "هو_ملف_شريط": "tarfile.is_tarfile",
    # === zipfile ===
    "هو_ملف_مضغوط": "zipfile.is_zipfile",
    # === unicodedata ===
    "هو_موحّد_2": "unicodedata.is_normalized",
    # === os ===
    "هو_نقطة_تحميل": "os.path.ismount",
    "هو_وصلة": "os.path.isjunction",
    # === locale ===
    "وحّد_الإقليم": "locale.normalize",
    # === os ===
    "وحّد_الحالة": "os.path.normcase",
    "وحّد_المسار": "os.path.normpath",
    # === unicodedata ===
    "وحّد_يونيكود": "unicodedata.normalize",
    # === os ===
    "وسّع_المتغيرات": "os.path.expandvars",
    "وسّع_المستخدم": "os.path.expanduser",
    # === tarfile ===
    "وصلة_بديل_خطأ": "tarfile.LinkFallbackError",
    "وصلة_خارج_وجهة_خطأ": "tarfile.LinkOutsideDestinationError",
    # === stat ===
    "وضع_الملف": "stat.filemode",
    # === os ===
    "وقت_الإنشاء": "os.path.getctime",
    "وقت_التعديل_2": "os.path.getmtime",
    "وقت_الوصول": "os.path.getatime",
    # === weakref ===
    "وكيل_ضعيف": "weakref.proxy",
    "وكيل_نوع": "weakref.ProxyType",
    # === codecs ===
    "يونيكود_هرب_رمّز": "codecs.unicode_escape_encode",
    "يونيكود_هرب_فكّ_ترميز": "codecs.unicode_escape_decode",
    # === contextlib ===
    "يُغلق": "contextlib.closing",
}


DF_METHODS = {
    # دوال الكائن بعد نقطة
    # === numbers ===
    "ABC_وصفي_سجّل": "register",
    # === bz2 ===
    "BZ_2_ضاغط_أفرغ": "flush",
    "BZ_2_ضاغط_اضغط": "compress",
    "BZ_2_فكّ_ضغط_فكّ_الضغط": "decompress",
    "BZ_2_ملف_أغلق": "close",
    "BZ_2_ملف_أفرغ": "flush",
    "BZ_2_ملف_اطّلع": "peek",
    "BZ_2_ملف_افصل": "detach",
    "BZ_2_ملف_اقتطع": "truncate",
    "BZ_2_ملف_اقرأ": "read",
    "BZ_2_ملف_اقرأ1": "read1",
    "BZ_2_ملف_اقرأ_في": "readinto",
    "BZ_2_ملف_اقرأ_في1": "readinto1",
    "BZ_2_ملف_اكتب": "write",
    "BZ_2_ملف_اكتب_أسطراً": "writelines",
    "BZ_2_ملف_انتقل": "seek",
    "BZ_2_ملف_رقم_الملف": "fileno",
    "BZ_2_ملف_سطر_قراءة": "readline",
    "BZ_2_ملف_ضع_الموضع": "tell",
    "BZ_2_ملف_قابل_للانتقال": "seekable",
    "BZ_2_ملف_قابل_للقراءة": "readable",
    "BZ_2_ملف_قابل_للكتابة": "writable",
    "BZ_2_ملف_هو_طرفية": "isatty",
    # === xml ===
    "C_14_N_كاتب_هدف_PI": "pi",
    "C_14_N_كاتب_هدف_أنهِ": "end",
    "C_14_N_كاتب_هدف_ابدأ": "start",
    "C_14_N_كاتب_هدف_بيانات": "data",
    "C_14_N_كاتب_هدف_تعليق": "comment",
    # === tarfile ===
    "EX_ملف_كائن_أغلق": "close",
    "EX_ملف_كائن_أفرغ": "flush",
    "EX_ملف_كائن_اطّلع": "peek",
    "EX_ملف_كائن_افصل": "detach",
    "EX_ملف_كائن_اقتطع": "truncate",
    "EX_ملف_كائن_اقرأ": "read",
    "EX_ملف_كائن_اقرأ1": "read1",
    "EX_ملف_كائن_اقرأ_في": "readinto",
    "EX_ملف_كائن_اقرأ_في1": "readinto1",
    "EX_ملف_كائن_اكتب": "write",
    "EX_ملف_كائن_اكتب_أسطراً": "writelines",
    "EX_ملف_كائن_انتقل": "seek",
    "EX_ملف_كائن_رقم_الملف": "fileno",
    "EX_ملف_كائن_سطر_قراءة": "readline",
    "EX_ملف_كائن_ضع_الموضع": "tell",
    "EX_ملف_كائن_قابل_للانتقال": "seekable",
    "EX_ملف_كائن_قابل_للقراءة": "readable",
    "EX_ملف_كائن_قابل_للكتابة": "writable",
    "EX_ملف_كائن_هو_طرفية": "isatty",
    # === zipfile ===
    "PY_أرشيف_مضغوط_ملف_أغلق": "close",
    "PY_أرشيف_مضغوط_ملف_احصل_على_المعلومات": "getinfo",
    "PY_أرشيف_مضغوط_ملف_اختبر_الأرشيف": "testzip",
    "PY_أرشيف_مضغوط_ملف_استخرج": "extract",
    "PY_أرشيف_مضغوط_ملف_استخرج_الكل": "extractall",
    "PY_أرشيف_مضغوط_ملف_اطبع_المجلد": "printdir",
    "PY_أرشيف_مضغوط_ملف_اعمل_مجلداً": "mkdir",
    "PY_أرشيف_مضغوط_ملف_افتح": "open",
    "PY_أرشيف_مضغوط_ملف_اقرأ": "read",
    "PY_أرشيف_مضغوط_ملف_اكتب": "write",
    "PY_أرشيف_مضغوط_ملف_اكتب_نصاً": "writestr",
    "PY_أرشيف_مضغوط_ملف_عيّن_كلمة_المرور": "setpassword",
    "PY_أرشيف_مضغوط_ملف_قائمة_الأسماء": "namelist",
    "PY_أرشيف_مضغوط_ملف_قائمة_المعلومات": "infolist",
    # === xml ===
    "XML_اسحب_محلل_أغلق": "close",
    "XML_اسحب_محلل_أفرغ": "flush",
    "XML_اسحب_محلل_غذّ": "feed",
    "XML_رشّح_أساس_أحرف": "characters",
    "XML_رشّح_أساس_أنهِ_بادئة_خريطة": "endPrefixMapping",
    "XML_رشّح_أساس_أنهِ_عنصر": "endElement",
    "XML_رشّح_أساس_أنهِ_عنصر_NS": "endElementNS",
    "XML_رشّح_أساس_أنهِ_مستند": "endDocument",
    "XML_رشّح_أساس_ابدأ_بادئة_خريطة": "startPrefixMapping",
    "XML_رشّح_أساس_ابدأ_عنصر": "startElement",
    "XML_رشّح_أساس_ابدأ_عنصر_NS": "startElementNS",
    "XML_رشّح_أساس_ابدأ_مستند": "startDocument",
    "XML_رشّح_أساس_احصل_تعريف_نوع_المستند_معالج": "getDTDHandler",
    "XML_رشّح_أساس_احصل_خطأ_معالج": "getErrorHandler",
    "XML_رشّح_أساس_احصل_سمة_صنف": "getProperty",
    "XML_رشّح_أساس_احصل_كيان_محلّل": "getEntityResolver",
    "XML_رشّح_أساس_احصل_محتوى_معالج": "getContentHandler",
    "XML_رشّح_أساس_احصل_ميزة": "getFeature",
    "XML_رشّح_أساس_تحذير": "warning",
    "XML_رشّح_أساس_ترميز_إعلان": "notationDecl",
    "XML_رشّح_أساس_حلل": "parse",
    "XML_رشّح_أساس_حلّ_كيان": "resolveEntity",
    "XML_رشّح_أساس_خطأ": "error",
    "XML_رشّح_أساس_عيّن_تعريف_نوع_المستند_معالج": "setDTDHandler",
    "XML_رشّح_أساس_عيّن_خطأ_معالج": "setErrorHandler",
    "XML_رشّح_أساس_عيّن_سمة_صنف": "setProperty",
    "XML_رشّح_أساس_عيّن_كيان_محلّل": "setEntityResolver",
    "XML_رشّح_أساس_عيّن_محتوى_معالج": "setContentHandler",
    "XML_رشّح_أساس_عيّن_محلي": "setLocale",
    "XML_رشّح_أساس_عيّن_مستند_محدّد": "setDocumentLocator",
    "XML_رشّح_أساس_عيّن_ميزة": "setFeature",
    "XML_رشّح_أساس_غير_محلَّل_كيان_إعلان": "unparsedEntityDecl",
    "XML_رشّح_أساس_قابل_للتجاهل_مسافة_بيضاء": "ignorableWhitespace",
    "XML_رشّح_أساس_قاتل_خطأ": "fatalError",
    "XML_رشّح_أساس_معالجة_تعليمة": "processingInstruction",
    "XML_رشّح_أساس_مُتخطَّى_كيان": "skippedEntity",
    "XML_قارئ_احصل_تعريف_نوع_المستند_معالج": "getDTDHandler",
    "XML_قارئ_احصل_خطأ_معالج": "getErrorHandler",
    "XML_قارئ_احصل_سمة_صنف": "getProperty",
    "XML_قارئ_احصل_كيان_محلّل": "getEntityResolver",
    "XML_قارئ_احصل_محتوى_معالج": "getContentHandler",
    "XML_قارئ_احصل_ميزة": "getFeature",
    "XML_قارئ_حلل": "parse",
    "XML_قارئ_عيّن_تعريف_نوع_المستند_معالج": "setDTDHandler",
    "XML_قارئ_عيّن_خطأ_معالج": "setErrorHandler",
    "XML_قارئ_عيّن_سمة_صنف": "setProperty",
    "XML_قارئ_عيّن_كيان_محلّل": "setEntityResolver",
    "XML_قارئ_عيّن_محتوى_معالج": "setContentHandler",
    "XML_قارئ_عيّن_محلي": "setLocale",
    "XML_قارئ_عيّن_ميزة": "setFeature",
    "XML_محلل_أغلق": "close",
    "XML_محلل_أفرغ": "flush",
    "XML_محلل_ساكس_خطأ_معالج_تحذير": "warning",
    "XML_محلل_ساكس_خطأ_معالج_خطأ": "error",
    "XML_محلل_ساكس_خطأ_معالج_قاتل_خطأ": "fatalError",
    "XML_محلل_غذّ": "feed",
    "XML_مولّد_أحرف": "characters",
    "XML_مولّد_أنهِ_بادئة_خريطة": "endPrefixMapping",
    "XML_مولّد_أنهِ_عنصر": "endElement",
    "XML_مولّد_أنهِ_عنصر_NS": "endElementNS",
    "XML_مولّد_أنهِ_مستند": "endDocument",
    "XML_مولّد_ابدأ_بادئة_خريطة": "startPrefixMapping",
    "XML_مولّد_ابدأ_عنصر": "startElement",
    "XML_مولّد_ابدأ_عنصر_NS": "startElementNS",
    "XML_مولّد_ابدأ_مستند": "startDocument",
    "XML_مولّد_عيّن_مستند_محدّد": "setDocumentLocator",
    "XML_مولّد_قابل_للتجاهل_مسافة_بيضاء": "ignorableWhitespace",
    "XML_مولّد_معالجة_تعليمة": "processingInstruction",
    "XML_مولّد_مُتخطَّى_كيان": "skippedEntity",
    # === shelve ===
    "bsd_قاعدة_رف_أغلق": "close",
    "bsd_قاعدة_رف_احصل": "get",
    "bsd_قاعدة_رف_التالي": "next",
    "bsd_قاعدة_رف_تزامن": "sync",
    # === filecmp ===
    "أبلغ": "report",
    "أبلغ_جزئي_إغلاق": "report_partial_closure",
    "أبلغ_كامل_إغلاق": "report_full_closure",
    # === shelve ===
    "أخير": "last",
    # === queue ===
    "أخِر_دخَل_أخِر_خرج_طابور_أوقف": "shutdown",
    "أخِر_دخَل_أخِر_خرج_طابور_احصل": "get",
    "أخِر_دخَل_أخِر_خرج_طابور_احصل_بلا_انتظار": "get_nowait",
    "أخِر_دخَل_أخِر_خرج_طابور_اربط": "join",
    "أخِر_دخَل_أخِر_خرج_طابور_حجم_الطابور": "qsize",
    "أخِر_دخَل_أخِر_خرج_طابور_ضع": "put",
    "أخِر_دخَل_أخِر_خرج_طابور_ضع_بلا_انتظار": "put_nowait",
    "أخِر_دخَل_أخِر_خرج_طابور_فارغ": "empty",
    "أخِر_دخَل_أخِر_خرج_طابور_كامل": "full",
    "أخِر_دخَل_أخِر_خرج_طابور_مهمة_تم": "task_done",
    # === zipfile ===
    "أرشيف_مضغوط_امتداد_ملف_أغلق": "close",
    "أرشيف_مضغوط_امتداد_ملف_أفرغ": "flush",
    "أرشيف_مضغوط_امتداد_ملف_اطّلع": "peek",
    "أرشيف_مضغوط_امتداد_ملف_افصل": "detach",
    "أرشيف_مضغوط_امتداد_ملف_اقتطع": "truncate",
    "أرشيف_مضغوط_امتداد_ملف_اقرأ": "read",
    "أرشيف_مضغوط_امتداد_ملف_اقرأ1": "read1",
    "أرشيف_مضغوط_امتداد_ملف_اقرأ_في": "readinto",
    "أرشيف_مضغوط_امتداد_ملف_اقرأ_في1": "readinto1",
    "أرشيف_مضغوط_امتداد_ملف_اكتب": "write",
    "أرشيف_مضغوط_امتداد_ملف_اكتب_أسطراً": "writelines",
    "أرشيف_مضغوط_امتداد_ملف_انتقل": "seek",
    "أرشيف_مضغوط_امتداد_ملف_رقم_الملف": "fileno",
    "أرشيف_مضغوط_امتداد_ملف_سطر_قراءة": "readline",
    "أرشيف_مضغوط_امتداد_ملف_سطر_قراءة_2": "readlines",
    "أرشيف_مضغوط_امتداد_ملف_ضع_الموضع": "tell",
    "أرشيف_مضغوط_امتداد_ملف_قابل_للانتقال": "seekable",
    "أرشيف_مضغوط_امتداد_ملف_قابل_للقراءة": "readable",
    "أرشيف_مضغوط_امتداد_ملف_قابل_للكتابة": "writable",
    "أرشيف_مضغوط_امتداد_ملف_هو_طرفية": "isatty",
    "أرشيف_مضغوط_معلومات_من_ملف": "from_file",
    "أرشيف_مضغوط_معلومات_هو_مجلد": "is_dir",
    "أرشيف_مضغوط_ملف_أغلق": "close",
    "أرشيف_مضغوط_ملف_احصل_على_المعلومات": "getinfo",
    "أرشيف_مضغوط_ملف_اختبر_الأرشيف": "testzip",
    "أرشيف_مضغوط_ملف_استخرج": "extract",
    "أرشيف_مضغوط_ملف_استخرج_الكل": "extractall",
    "أرشيف_مضغوط_ملف_اطبع_المجلد": "printdir",
    "أرشيف_مضغوط_ملف_اعمل_مجلداً": "mkdir",
    "أرشيف_مضغوط_ملف_افتح": "open",
    "أرشيف_مضغوط_ملف_اقرأ": "read",
    "أرشيف_مضغوط_ملف_اكتب": "write",
    "أرشيف_مضغوط_ملف_اكتب_نصاً": "writestr",
    "أرشيف_مضغوط_ملف_عيّن_كلمة_المرور": "setpassword",
    "أرشيف_مضغوط_ملف_قائمة_الأسماء": "namelist",
    "أرشيف_مضغوط_ملف_قائمة_المعلومات": "infolist",
    # === tarfile ===
    "أضف_ملفاً": "addfile",
    # === xml ===
    "أعد_التسمية_عُقدة": "renameNode",
    # === io ===
    "أعد_الضبط": "reconfigure",
    # === contextlib ===
    "أغلق_غير_متزامن": "aclose",
    # === xml ===
    "أنشئ_بيانات_ج_قسم": "createCDATASection",
    "أنشئ_تعليق": "createComment",
    # === tarfile ===
    "أنشئ_تنسيق_gnu_رأس": "create_gnu_header",
    "أنشئ_تنسيق_pax_رأس": "create_pax_header",
    "أنشئ_تنسيق_pax_شامل_رأس": "create_pax_global_header",
    "أنشئ_تنسيق_ustar_رأس": "create_ustar_header",
    # === xml ===
    "أنشئ_سمة": "createAttribute",
    "أنشئ_سمة_NS": "createAttributeNS",
    "أنشئ_عنصر_NS": "createElementNS",
    "أنشئ_مستند": "createDocument",
    "أنشئ_مستند_جزء": "createDocumentFragment",
    "أنشئ_مستند_نوع": "createDocumentType",
    "أنشئ_معالجة_تعليمة": "createProcessingInstruction",
    "أنشئ_نص_عُقدة": "createTextNode",
    # === weakref ===
    "أنهِ_اطّلع": "peek",
    "أنهِ_افصل": "detach",
    # === xml ===
    "أنهِ_بيانات_ج": "endCDATA",
    "أنهِ_تعريف_نوع_المستند": "endDTD",
    # === shelve ===
    "أول": "first",
    # === queue ===
    "أولوية_طابور_أوقف": "shutdown",
    "أولوية_طابور_احصل": "get",
    "أولوية_طابور_احصل_بلا_انتظار": "get_nowait",
    "أولوية_طابور_اربط": "join",
    "أولوية_طابور_حجم_الطابور": "qsize",
    "أولوية_طابور_ضع": "put",
    "أولوية_طابور_ضع_بلا_انتظار": "put_nowait",
    "أولوية_طابور_فارغ": "empty",
    "أولوية_طابور_كامل": "full",
    "أولوية_طابور_مهمة_تم": "task_done",
    # === io ===
    "إدخال_إخراج_أساس_أغلق": "close",
    "إدخال_إخراج_أساس_أفرغ": "flush",
    "إدخال_إخراج_أساس_اقتطع": "truncate",
    "إدخال_إخراج_أساس_اكتب_أسطراً": "writelines",
    "إدخال_إخراج_أساس_انتقل": "seek",
    "إدخال_إخراج_أساس_رقم_الملف": "fileno",
    "إدخال_إخراج_أساس_سطر_قراءة": "readline",
    "إدخال_إخراج_أساس_سطر_قراءة_2": "readlines",
    "إدخال_إخراج_أساس_ضع_الموضع": "tell",
    "إدخال_إخراج_أساس_قابل_للانتقال": "seekable",
    "إدخال_إخراج_أساس_قابل_للقراءة": "readable",
    "إدخال_إخراج_أساس_قابل_للكتابة": "writable",
    "إدخال_إخراج_أساس_هو_طرفية": "isatty",
    "إدخال_إخراج_مُخزّن_مؤقتاً_عشوائي_سطر_قراءة": "readlines",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قارئ_سطر_قراءة": "readlines",
    "إدخال_إخراج_مُخزّن_مؤقتاً_قراءة_كتابة_زوج_سطر_قراءة": "readlines",
    "إدخال_إخراج_مُخزّن_مؤقتاً_كاتب_سطر_قراءة": "readlines",
    # === xml ===
    "إدخال_مصدر_احصل_عام_معرف": "getPublicId",
    "إدخال_مصدر_احصل_نظام_معرف": "getSystemId",
    # === array ===
    "إلى_قائمة": "tolist",
    # === tarfile ===
    "إلى_مخزن": "tobuf",
    # === array ===
    "إلى_يونيكود": "tounicode",
    # === difflib ===
    "ابحث_أطول_طابق": "find_longest_match",
    # === pickle ===
    "ابحث_صنف": "find_class",
    # === xml ===
    "ابدأ_NS": "start_ns",
    "ابدأ_بيانات_ج": "startCDATA",
    "ابدأ_تعريف_نوع_المستند": "startDTD",
    "احذف_سمة": "removeAttribute",
    "احذف_سمة_NS": "removeAttributeNS",
    "احذف_سمة_عُقدة": "removeAttributeNode",
    "احذف_سمة_عُقدة_NS": "removeAttributeNodeNS",
    # === struct ===
    "احزم_إلى": "pack_into",
    # === xml ===
    "احصل_أب": "getParent",
    "احصل_بايت_تدفق": "getByteStream",
    "احصل_ترميز": "getEncoding",
    # === graphlib ===
    "احصل_جاهز": "get_ready",
    # === xml ===
    "احصل_حدث": "getEvent",
    "احصل_حرف_تدفق": "getCharacterStream",
    # === difflib ===
    "احصل_رموز_التشغيل": "get_opcodes",
    # === xml ===
    "احصل_سطر_عدد": "getLineNumber",
    "احصل_سمة": "getAttribute",
    "احصل_سمة_NS": "getAttributeNS",
    "احصل_سمة_عُقدة": "getAttributeNode",
    "احصل_سمة_عُقدة_NS": "getAttributeNodeNS",
    "احصل_سمة_نوع": "getAttributeType",
    "احصل_سمة_نوع_NS": "getAttributeTypeNS",
    # === tarfile ===
    "احصل_على_الأسماء": "getnames",
    "احصل_على_الأعضاء": "getmembers",
    # === xml ===
    "احصل_على_الجذر": "getroot",
    # === io ===
    "احصل_على_المخزن": "getbuffer",
    # === tarfile ===
    "احصل_على_عضو": "getmember",
    "احصل_على_معلومات_شريط": "gettarinfo",
    # === xml ===
    "احصل_عمود_عدد": "getColumnNumber",
    "احصل_عنصر_بواسطة_معرف": "getElementById",
    # === difflib ===
    "احصل_مجمّع_رموز_التشغيل": "get_grouped_opcodes",
    "احصل_مطابقة_كتل": "get_matching_blocks",
    # === tarfile ===
    "احصل_معلومات": "get_info",
    # === contextlib ===
    "اخرج_مكدس_أغلق": "close",
    "اخرج_مكدس_ادخل_سياق": "enter_context",
    "اخرج_مكدس_ادفع": "push",
    "اخرج_مكدس_اسحب_كل": "pop_all",
    "اخرج_مكدس_ردّ_النداء": "callback",
    "ادخل_غير_متزامن_سياق": "enter_async_context",
    "ادفع_غير_متزامن_اخرج": "push_async_exit",
    "ادفع_غير_متزامن_ردّ_النداء": "push_async_callback",
    # === gzip ===
    "ارجع_للخلف": "rewind",
    # === tarfile ===
    "استخرج_ملفاً": "extractfile",
    # === xml ===
    "استيراد_عُقدة": "importNode",
    "اسحب_نموذج_كائن_أحرف": "characters",
    "اسحب_نموذج_كائن_أنهِ_بادئة_خريطة": "endPrefixMapping",
    "اسحب_نموذج_كائن_أنهِ_عنصر": "endElement",
    "اسحب_نموذج_كائن_أنهِ_عنصر_NS": "endElementNS",
    "اسحب_نموذج_كائن_أنهِ_مستند": "endDocument",
    "اسحب_نموذج_كائن_ابدأ_بادئة_خريطة": "startPrefixMapping",
    "اسحب_نموذج_كائن_ابدأ_عنصر": "startElement",
    "اسحب_نموذج_كائن_ابدأ_عنصر_NS": "startElementNS",
    "اسحب_نموذج_كائن_ابدأ_مستند": "startDocument",
    "اسحب_نموذج_كائن_ابنِ_مستند": "buildDocument",
    "اسحب_نموذج_كائن_اسحب": "pop",
    "اسحب_نموذج_كائن_امسح": "clear",
    "اسحب_نموذج_كائن_تعليق": "comment",
    "اسحب_نموذج_كائن_عيّن_مستند_محدّد": "setDocumentLocator",
    "اسحب_نموذج_كائن_قابل_للتجاهل_مسافة_بيضاء": "ignorableWhitespace",
    "اسحب_نموذج_كائن_معالجة_تعليمة": "processingInstruction",
    "اسحب_نموذج_كائن_مُتخطَّى_كيان": "skippedEntity",
    # === shelve ===
    "اسم_ملف_القاعدة_رف_أغلق": "close",
    "اسم_ملف_القاعدة_رف_احصل": "get",
    "اسم_ملف_القاعدة_رف_امسح": "clear",
    "اسم_ملف_القاعدة_رف_تزامن": "sync",
    # === tarfile ===
    "اعمل_أنبوباً": "makefifo",
    # === difflib ===
    "اعمل_جدول": "make_table",
    # === tarfile ===
    "اعمل_جهازاً": "makedev",
    "اعمل_رابطاً": "makelink",
    "اعمل_رابطاً_بـ_رشّح": "makelink_with_filter",
    # === xml ===
    "اعمل_عنصراً": "makeelement",
    # === tarfile ===
    "اعمل_مجهول": "makeunknown",
    # === difflib ===
    "اعمل_ملف": "make_file",
    # === tarfile ===
    "اعمل_ملفاً": "makefile",
    "افتح_bz2": "bz2open",
    "افتح_gzip": "gzopen",
    "افتح_xz": "xzopen",
    "افتح_zst": "zstopen",
    "افتح_شريطاً": "taropen",
    # === xml ===
    "اقرأ_أحداث": "read_events",
    "اقرأ_فقط_تسلسلي_مسمّى_عُقدة_خريطة_احذف_مسمّى_عنصر": "removeNamedItem",
    "اقرأ_فقط_تسلسلي_مسمّى_عُقدة_خريطة_احذف_مسمّى_عنصر_NS": "removeNamedItemNS",
    "اقرأ_فقط_تسلسلي_مسمّى_عُقدة_خريطة_احصل_مسمّى_عنصر": "getNamedItem",
    "اقرأ_فقط_تسلسلي_مسمّى_عُقدة_خريطة_احصل_مسمّى_عنصر_NS": "getNamedItemNS",
    "اقرأ_فقط_تسلسلي_مسمّى_عُقدة_خريطة_عنصر": "item",
    "اقرأ_فقط_تسلسلي_مسمّى_عُقدة_خريطة_عيّن_مسمّى_عنصر": "setNamedItem",
    "اقرأ_فقط_تسلسلي_مسمّى_عُقدة_خريطة_عيّن_مسمّى_عنصر_NS": "setNamedItemNS",
    # === zipfile ===
    "اكتب_بايثون": "writepy",
    # === xml ===
    "اكتب_توحيد_إكس_إم_إم": "write_c14n",
    # === shelve ===
    "السابق": "previous",
    # === fileinput ===
    "الملف_التالي": "nextfile",
    # === pickle ===
    "امسح_ذاكرة_تحويل": "clear_memo",
    # === io ===
    "بايتات_إدخال_إخراج_أغلق": "close",
    "بايتات_إدخال_إخراج_أفرغ": "flush",
    "بايتات_إدخال_إخراج_احصل_على_القيمة": "getvalue",
    "بايتات_إدخال_إخراج_افصل": "detach",
    "بايتات_إدخال_إخراج_اقتطع": "truncate",
    "بايتات_إدخال_إخراج_اقرأ": "read",
    "بايتات_إدخال_إخراج_اقرأ1": "read1",
    "بايتات_إدخال_إخراج_اقرأ_في": "readinto",
    "بايتات_إدخال_إخراج_اقرأ_في1": "readinto1",
    "بايتات_إدخال_إخراج_اكتب": "write",
    "بايتات_إدخال_إخراج_اكتب_أسطراً": "writelines",
    "بايتات_إدخال_إخراج_انتقل": "seek",
    "بايتات_إدخال_إخراج_رقم_الملف": "fileno",
    "بايتات_إدخال_إخراج_سطر_قراءة": "readline",
    "بايتات_إدخال_إخراج_سطر_قراءة_2": "readlines",
    "بايتات_إدخال_إخراج_ضع_الموضع": "tell",
    "بايتات_إدخال_إخراج_قابل_للانتقال": "seekable",
    "بايتات_إدخال_إخراج_قابل_للقراءة": "readable",
    "بايتات_إدخال_إخراج_قابل_للكتابة": "writable",
    "بايتات_إدخال_إخراج_هو_طرفية": "isatty",
    # === pickle ===
    "بايكن_مخزن_مؤقت_خام": "raw",
    # === array ===
    "بدّل_البايتات": "byteswap",
    # === queue ===
    "بسيط_طابور_احصل": "get",
    "بسيط_طابور_احصل_بلا_انتظار": "get_nowait",
    "بسيط_طابور_حجم_الطابور": "qsize",
    "بسيط_طابور_ضع": "put",
    "بسيط_طابور_ضع_بلا_انتظار": "put_nowait",
    "بسيط_طابور_فارغ": "empty",
    # === xml ===
    "بلا_أبناء_أدخل_قبل": "insertBefore",
    "بلا_أبناء_أضف_ذيلياً_ابن": "appendChild",
    "بلا_أبناء_احذف_ابن": "removeChild",
    "بلا_أبناء_استبدل_ابن": "replaceChild",
    "بلا_أبناء_له_ابن_عُقد": "hasChildNodes",
    "بلا_أبناء_وحّد": "normalize",
    # === struct ===
    "بنية_احزم": "pack",
    "بنية_فكّ_الحزمة": "unpack",
    # === xml ===
    "بيانات_ج_قسم_أدخل_بيانات": "insertData",
    "بيانات_ج_قسم_أدخل_قبل": "insertBefore",
    "بيانات_ج_قسم_أضف_ذيلياً_ابن": "appendChild",
    "بيانات_ج_قسم_أضف_ذيلياً_بيانات": "appendData",
    "بيانات_ج_قسم_إلى_إكس_إم_إم": "toxml",
    "بيانات_ج_قسم_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "بيانات_ج_قسم_احذف_ابن": "removeChild",
    "بيانات_ج_قسم_احذف_بيانات": "deleteData",
    "بيانات_ج_قسم_احصل_مستخدم_بيانات": "getUserData",
    "بيانات_ج_قسم_احصل_واجهة": "getInterface",
    "بيانات_ج_قسم_استبدل_ابن": "replaceChild",
    "بيانات_ج_قسم_استبدل_بيانات": "replaceData",
    "بيانات_ج_قسم_استبدل_كامل_نص": "replaceWholeText",
    "بيانات_ج_قسم_استنسخ_عُقدة": "cloneNode",
    "بيانات_ج_قسم_افصل_نص": "splitText",
    "بيانات_ج_قسم_اكتب_إكس_إم_إم": "writexml",
    "بيانات_ج_قسم_عيّن_مستخدم_بيانات": "setUserData",
    "بيانات_ج_قسم_فكّ_الرابط": "unlink",
    "بيانات_ج_قسم_له_ابن_عُقد": "hasChildNodes",
    "بيانات_ج_قسم_نص_فرعي_بيانات": "substringData",
    "بيانات_ج_قسم_هو_مدعوم": "isSupported",
    "بيانات_ج_قسم_هو_نفس_عُقدة": "isSameNode",
    "بيانات_ج_قسم_وحّد": "normalize",
    # === codecs ===
    "تدفق_قارئ_اقرأ": "read",
    "تدفق_قارئ_انتقل": "seek",
    "تدفق_قارئ_رمّز": "encode",
    "تدفق_قارئ_سطر_قراءة": "readline",
    "تدفق_قارئ_صفّر": "reset",
    "تدفق_قارئ_فكّ_ترميز": "decode",
    "تدفق_قارئ_كاتب_اقرأ": "read",
    "تدفق_قارئ_كاتب_اكتب": "write",
    "تدفق_قارئ_كاتب_اكتب_أسطراً": "writelines",
    "تدفق_قارئ_كاتب_انتقل": "seek",
    "تدفق_قارئ_كاتب_سطر_قراءة": "readline",
    "تدفق_قارئ_كاتب_صفّر": "reset",
    "تدفق_كاتب_اكتب": "write",
    "تدفق_كاتب_اكتب_أسطراً": "writelines",
    "تدفق_كاتب_انتقل": "seek",
    "تدفق_كاتب_رمّز": "encode",
    "تدفق_كاتب_صفّر": "reset",
    "تدفق_كاتب_فكّ_ترميز": "decode",
    "تدفق_مُعادِل_الترميز_اقرأ": "read",
    "تدفق_مُعادِل_الترميز_اكتب": "write",
    "تدفق_مُعادِل_الترميز_اكتب_أسطراً": "writelines",
    "تدفق_مُعادِل_الترميز_انتقل": "seek",
    "تدفق_مُعادِل_الترميز_سطر_قراءة": "readline",
    "تدفق_مُعادِل_الترميز_صفّر": "reset",
    # === xml ===
    "ترميز_أدخل_قبل": "insertBefore",
    "ترميز_أضف_ذيلياً_ابن": "appendChild",
    "ترميز_إلى_إكس_إم_إم": "toxml",
    "ترميز_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "ترميز_احذف_ابن": "removeChild",
    "ترميز_احصل_مستخدم_بيانات": "getUserData",
    "ترميز_احصل_واجهة": "getInterface",
    "ترميز_استبدل_ابن": "replaceChild",
    "ترميز_استنسخ_عُقدة": "cloneNode",
    "ترميز_عيّن_مستخدم_بيانات": "setUserData",
    "ترميز_فكّ_الرابط": "unlink",
    "ترميز_له_ابن_عُقد": "hasChildNodes",
    "ترميز_هو_مدعوم": "isSupported",
    "ترميز_هو_نفس_عُقدة": "isSameNode",
    "ترميز_وحّد": "normalize",
    # === difflib ===
    "تسلسل_مطابِق_نسبة": "ratio",
    # === io ===
    "تصاعدي_سطر_جديد_مفكّك_احصل_على_الحالة": "getstate",
    "تصاعدي_سطر_جديد_مفكّك_صفّر": "reset",
    "تصاعدي_سطر_جديد_مفكّك_عيّن_الحالة": "setstate",
    "تصاعدي_سطر_جديد_مفكّك_فكّ_ترميز": "decode",
    # === xml ===
    "تصاعدي_محلل_أغلق": "close",
    "تصاعدي_محلل_احصل_تعريف_نوع_المستند_معالج": "getDTDHandler",
    "تصاعدي_محلل_احصل_خطأ_معالج": "getErrorHandler",
    "تصاعدي_محلل_احصل_سمة_صنف": "getProperty",
    "تصاعدي_محلل_احصل_كيان_محلّل": "getEntityResolver",
    "تصاعدي_محلل_احصل_محتوى_معالج": "getContentHandler",
    "تصاعدي_محلل_احصل_ميزة": "getFeature",
    "تصاعدي_محلل_حلل": "parse",
    "تصاعدي_محلل_صفّر": "reset",
    "تصاعدي_محلل_عيّن_تعريف_نوع_المستند_معالج": "setDTDHandler",
    "تصاعدي_محلل_عيّن_خطأ_معالج": "setErrorHandler",
    "تصاعدي_محلل_عيّن_سمة_صنف": "setProperty",
    "تصاعدي_محلل_عيّن_كيان_محلّل": "setEntityResolver",
    "تصاعدي_محلل_عيّن_محتوى_معالج": "setContentHandler",
    "تصاعدي_محلل_عيّن_محلي": "setLocale",
    "تصاعدي_محلل_عيّن_ميزة": "setFeature",
    "تصاعدي_محلل_غذّ": "feed",
    # === codecs ===
    "تصاعدي_مرمّز_احصل_على_الحالة": "getstate",
    "تصاعدي_مرمّز_رمّز": "encode",
    "تصاعدي_مرمّز_صفّر": "reset",
    "تصاعدي_مرمّز_عيّن_الحالة": "setstate",
    "تصاعدي_مفكّك_احصل_على_الحالة": "getstate",
    "تصاعدي_مفكّك_صفّر": "reset",
    "تصاعدي_مفكّك_عيّن_الحالة": "setstate",
    "تصاعدي_مفكّك_فكّ_ترميز": "decode",
    # === xml ===
    "تعريف_نوع_المستند_معالج_ترميز_إعلان": "notationDecl",
    "تعريف_نوع_المستند_معالج_غير_محلَّل_كيان_إعلان": "unparsedEntityDecl",
    "تعليق_أدخل_بيانات": "insertData",
    "تعليق_أدخل_قبل": "insertBefore",
    "تعليق_أضف_ذيلياً_ابن": "appendChild",
    "تعليق_أضف_ذيلياً_بيانات": "appendData",
    "تعليق_إلى_إكس_إم_إم": "toxml",
    "تعليق_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "تعليق_احذف_ابن": "removeChild",
    "تعليق_احذف_بيانات": "deleteData",
    "تعليق_احصل_مستخدم_بيانات": "getUserData",
    "تعليق_احصل_واجهة": "getInterface",
    "تعليق_استبدل_ابن": "replaceChild",
    "تعليق_استبدل_بيانات": "replaceData",
    "تعليق_استنسخ_عُقدة": "cloneNode",
    "تعليق_اكتب_إكس_إم_إم": "writexml",
    "تعليق_عيّن_مستخدم_بيانات": "setUserData",
    "تعليق_فكّ_الرابط": "unlink",
    "تعليق_له_ابن_عُقد": "hasChildNodes",
    "تعليق_نص_فرعي_بيانات": "substringData",
    "تعليق_هو_مدعوم": "isSupported",
    "تعليق_هو_نفس_عُقدة": "isSameNode",
    "تعليق_وحّد": "normalize",
    # === graphlib ===
    "تم": "done",
    # === reprlib ===
    "تمثيل": "repr",
    "تمثيل1": "repr1",
    "تمثيل_صف": "repr_tuple",
    "تمثيل_طابور_مزدوج": "repr_deque",
    "تمثيل_عدد_صحيح": "repr_int",
    "تمثيل_عيّن": "repr_set",
    "تمثيل_قائمة": "repr_list",
    "تمثيل_قاموس": "repr_dict",
    "تمثيل_مجموعة_مجمّدة": "repr_frozenset",
    "تمثيل_مصفوفة": "repr_array",
    "تمثيل_نسخة": "repr_instance",
    "تمثيل_نص": "repr_str",
    # === gettext ===
    "تنسيق_gnu_ترجمات_أضف_بديل": "add_fallback",
    "تنسيق_gnu_ترجمات_احصل_على_النص": "gettext",
    "تنسيق_gnu_ترجمات_احصل_على_نص_بسياق": "pgettext",
    "تنسيق_gnu_ترجمات_احصل_على_نص_جمع": "ngettext",
    "تنسيق_gnu_ترجمات_احصل_على_نص_جمع_سياق": "npgettext",
    "تنسيق_gnu_ترجمات_ثبّت": "install",
    "تنسيق_gnu_ترجمات_مجموعة_محارف": "charset",
    "تنسيق_gnu_ترجمات_معلومات": "info",
    # === graphlib ===
    "توبولوجي_مرتّب_أضف": "add",
    "ثابت_ترتيب": "static_order",
    # === unicodedata ===
    "ثنائي_الاتجاه": "bidirectional",
    # === graphlib ===
    "جهّز": "prepare",
    # === xml ===
    "جهّز_محلل": "prepareParser",
    "حرف_بيانات_أدخل_بيانات": "insertData",
    "حرف_بيانات_أدخل_قبل": "insertBefore",
    "حرف_بيانات_أضف_ذيلياً_ابن": "appendChild",
    "حرف_بيانات_أضف_ذيلياً_بيانات": "appendData",
    "حرف_بيانات_إلى_إكس_إم_إم": "toxml",
    "حرف_بيانات_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "حرف_بيانات_احذف_ابن": "removeChild",
    "حرف_بيانات_احذف_بيانات": "deleteData",
    "حرف_بيانات_احصل_مستخدم_بيانات": "getUserData",
    "حرف_بيانات_احصل_واجهة": "getInterface",
    "حرف_بيانات_استبدل_ابن": "replaceChild",
    "حرف_بيانات_استبدل_بيانات": "replaceData",
    "حرف_بيانات_استنسخ_عُقدة": "cloneNode",
    "حرف_بيانات_عيّن_مستخدم_بيانات": "setUserData",
    "حرف_بيانات_فكّ_الرابط": "unlink",
    "حرف_بيانات_له_ابن_عُقد": "hasChildNodes",
    "حرف_بيانات_نص_فرعي_بيانات": "substringData",
    "حرف_بيانات_هو_مدعوم": "isSupported",
    "حرف_بيانات_هو_نفس_عُقدة": "isSameNode",
    "حرف_بيانات_وحّد": "normalize",
    # === pickle ===
    "حرّر": "release",
    # === difflib ===
    "حقيقي_سريع_نسبة": "real_quick_ratio",
    # === numbers ===
    "حقيقي_مرافق": "conjugate",
    # === pickle ===
    "حمّل": "load",
    # === io ===
    "خام_إدخال_إخراج_أساس_أغلق": "close",
    "خام_إدخال_إخراج_أساس_أفرغ": "flush",
    "خام_إدخال_إخراج_أساس_اقتطع": "truncate",
    "خام_إدخال_إخراج_أساس_اقرأ": "read",
    "خام_إدخال_إخراج_أساس_اقرأ_في": "readinto",
    "خام_إدخال_إخراج_أساس_اقرأ_كل": "readall",
    "خام_إدخال_إخراج_أساس_اكتب": "write",
    "خام_إدخال_إخراج_أساس_اكتب_أسطراً": "writelines",
    "خام_إدخال_إخراج_أساس_انتقل": "seek",
    "خام_إدخال_إخراج_أساس_رقم_الملف": "fileno",
    "خام_إدخال_إخراج_أساس_سطر_قراءة": "readline",
    "خام_إدخال_إخراج_أساس_سطر_قراءة_2": "readlines",
    "خام_إدخال_إخراج_أساس_ضع_الموضع": "tell",
    "خام_إدخال_إخراج_أساس_قابل_للانتقال": "seekable",
    "خام_إدخال_إخراج_أساس_قابل_للقراءة": "readable",
    "خام_إدخال_إخراج_أساس_قابل_للكتابة": "writable",
    "خام_إدخال_إخراج_أساس_هو_طرفية": "isatty",
    # === xml ===
    "خطأ_معالج_تحذير": "warning",
    "خطأ_معالج_خطأ": "error",
    "خطأ_معالج_قاتل_خطأ": "fatalError",
    # === pickle ===
    "دائم_حمّل": "persistent_load",
    "دائم_معرف": "persistent_id",
    # === shelve ===
    "رف_أغلق": "close",
    "رف_احصل": "get",
    "رف_تزامن": "sync",
    # === unicodedata ===
    "رقم": "digit",
    # === difflib ===
    "سريع_نسبة": "quick_ratio",
    # === fileinput ===
    "سطر_الملف": "filelineno",
    # === xml ===
    "سمات_NS_تنفيذ_احصل": "get",
    "سمات_NS_تنفيذ_احصل_أسماء": "getNames",
    "سمات_NS_تنفيذ_احصل_اسم_بواسطة_طابور_اسم": "getNameByQName",
    "سمات_NS_تنفيذ_احصل_طابور_أسماء": "getQNames",
    "سمات_NS_تنفيذ_احصل_طابور_اسم_بواسطة_اسم": "getQNameByName",
    "سمات_NS_تنفيذ_احصل_طول": "getLength",
    "سمات_NS_تنفيذ_احصل_قيمة": "getValue",
    "سمات_NS_تنفيذ_احصل_قيمة_بواسطة_طابور_اسم": "getValueByQName",
    "سمات_NS_تنفيذ_احصل_نوع": "getType",
    "سمات_NS_تنفيذ_انسخ": "copy",
    "سمات_NS_تنفيذ_عناصر": "items",
    "سمات_NS_تنفيذ_قيم": "values",
    "سمات_NS_تنفيذ_مفاتيح": "keys",
    "سمات_تنفيذ_احصل": "get",
    "سمات_تنفيذ_احصل_أسماء": "getNames",
    "سمات_تنفيذ_احصل_اسم_بواسطة_طابور_اسم": "getNameByQName",
    "سمات_تنفيذ_احصل_طابور_أسماء": "getQNames",
    "سمات_تنفيذ_احصل_طابور_اسم_بواسطة_اسم": "getQNameByName",
    "سمات_تنفيذ_احصل_طول": "getLength",
    "سمات_تنفيذ_احصل_قيمة": "getValue",
    "سمات_تنفيذ_احصل_قيمة_بواسطة_طابور_اسم": "getValueByQName",
    "سمات_تنفيذ_احصل_نوع": "getType",
    "سمات_تنفيذ_انسخ": "copy",
    "سمات_تنفيذ_عناصر": "items",
    "سمات_تنفيذ_قيم": "values",
    "سمات_تنفيذ_مفاتيح": "keys",
    "سمة_أدخل_قبل": "insertBefore",
    "سمة_أضف_ذيلياً_ابن": "appendChild",
    "سمة_إلى_إكس_إم_إم": "toxml",
    "سمة_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "سمة_احذف_ابن": "removeChild",
    "سمة_احصل_مستخدم_بيانات": "getUserData",
    "سمة_احصل_واجهة": "getInterface",
    "سمة_استبدل_ابن": "replaceChild",
    "سمة_استنسخ_عُقدة": "cloneNode",
    "سمة_عيّن_مستخدم_بيانات": "setUserData",
    "سمة_فكّ_الرابط": "unlink",
    "سمة_قائمة_احذف_مسمّى_عنصر": "removeNamedItem",
    "سمة_قائمة_احذف_مسمّى_عنصر_NS": "removeNamedItemNS",
    "سمة_قائمة_احصل": "get",
    "سمة_قائمة_احصل_مسمّى_عنصر": "getNamedItem",
    "سمة_قائمة_احصل_مسمّى_عنصر_NS": "getNamedItemNS",
    "سمة_قائمة_عناصر": "items",
    "سمة_قائمة_عنصر": "item",
    "سمة_قائمة_عيّن_مسمّى_عنصر": "setNamedItem",
    "سمة_قائمة_عيّن_مسمّى_عنصر_NS": "setNamedItemNS",
    "سمة_قائمة_قيم": "values",
    "سمة_قائمة_مفاتيح": "keys",
    "سمة_له_ابن_عُقد": "hasChildNodes",
    "سمة_هو_مدعوم": "isSupported",
    "سمة_هو_نفس_عُقدة": "isSameNode",
    "سمة_وحّد": "normalize",
    # === contextvars ===
    "سياق_احصل": "get",
    "سياق_انسخ": "copy",
    "سياق_عناصر": "items",
    "سياق_قيم": "values",
    "سياق_متغير_احصل": "get",
    "سياق_متغير_صفّر": "reset",
    "سياق_متغير_عيّن": "set",
    "سياق_مفاتيح": "keys",
    # === xml ===
    "شجرة_باني_PI": "pi",
    "شجرة_باني_أغلق": "close",
    "شجرة_باني_أنهِ": "end",
    "شجرة_باني_ابدأ": "start",
    "شجرة_باني_بيانات": "data",
    "شجرة_باني_تعليق": "comment",
    # === unicodedata ===
    "شرق_آسيوي_عرض": "east_asian_width",
    # === tarfile ===
    "شريط_EX_ملف_كائن_سطر_قراءة": "readlines",
    "شريط_أرشيف_معلومات_استبدل": "replace",
    "شريط_أرشيف_معلومات_هو_مجلد": "isdir",
    "شريط_أرشيف_معلومات_هو_ملف": "isfile",
    "شريط_أرشيف_ملف_أضف": "add",
    "شريط_أرشيف_ملف_أغلق": "close",
    "شريط_أرشيف_ملف_استخرج": "extract",
    "شريط_أرشيف_ملف_استخرج_الكل": "extractall",
    "شريط_أرشيف_ملف_اعمل_مجلداً": "makedir",
    "شريط_أرشيف_ملف_افتح": "open",
    "شريط_أرشيف_ملف_التالي": "next",
    "شريط_أرشيف_ملف_قائمة": "list",
    # === contextvars ===
    "شغّل": "run",
    # === numbers ===
    "صحيح_مرافق": "conjugate",
    # === weakref ===
    "ضعيف_قيمة_قاموس_احصل": "get",
    "ضعيف_قيمة_قاموس_اسحب": "pop",
    "ضعيف_قيمة_قاموس_اسحب_عنصراً": "popitem",
    "ضعيف_قيمة_قاموس_انسخ": "copy",
    "ضعيف_قيمة_قاموس_حدّث": "update",
    "ضعيف_قيمة_قاموس_عناصر": "items",
    "ضعيف_قيمة_قاموس_عيّن_افتراضياً": "setdefault",
    "ضعيف_قيمة_قاموس_قيم": "values",
    "ضعيف_قيمة_قاموس_مفاتيح": "keys",
    "ضعيف_مفتاح_قاموس_احصل": "get",
    "ضعيف_مفتاح_قاموس_اسحب": "pop",
    "ضعيف_مفتاح_قاموس_اسحب_عنصراً": "popitem",
    "ضعيف_مفتاح_قاموس_انسخ": "copy",
    "ضعيف_مفتاح_قاموس_حدّث": "update",
    "ضعيف_مفتاح_قاموس_عناصر": "items",
    "ضعيف_مفتاح_قاموس_عيّن_افتراضياً": "setdefault",
    "ضعيف_مفتاح_قاموس_قيم": "values",
    "ضعيف_مفتاح_قاموس_مفاتيح": "keys",
    # === bz2 ===
    "ضغط_bz2_BZ_2_ملف_سطر_قراءة": "readlines",
    # === gzip ===
    "ضغط_gzip_ملف_أغلق": "close",
    "ضغط_gzip_ملف_أفرغ": "flush",
    "ضغط_gzip_ملف_اطّلع": "peek",
    "ضغط_gzip_ملف_افصل": "detach",
    "ضغط_gzip_ملف_اقتطع": "truncate",
    "ضغط_gzip_ملف_اقرأ": "read",
    "ضغط_gzip_ملف_اقرأ1": "read1",
    "ضغط_gzip_ملف_اقرأ_في": "readinto",
    "ضغط_gzip_ملف_اقرأ_في1": "readinto1",
    "ضغط_gzip_ملف_اكتب": "write",
    "ضغط_gzip_ملف_اكتب_أسطراً": "writelines",
    "ضغط_gzip_ملف_انتقل": "seek",
    "ضغط_gzip_ملف_رقم_الملف": "fileno",
    "ضغط_gzip_ملف_سطر_قراءة": "readline",
    "ضغط_gzip_ملف_سطر_قراءة_2": "readlines",
    "ضغط_gzip_ملف_ضع_الموضع": "tell",
    "ضغط_gzip_ملف_قابل_للانتقال": "seekable",
    "ضغط_gzip_ملف_قابل_للقراءة": "readable",
    "ضغط_gzip_ملف_قابل_للكتابة": "writable",
    "ضغط_gzip_ملف_هو_طرفية": "isatty",
    # === zipfile ===
    "ضغط_lzma_ضاغط_أفرغ": "flush",
    # === lzma ===
    "ضغط_lzma_ضاغط_أفرغ_2": "flush",
    # === zipfile ===
    "ضغط_lzma_ضاغط_اضغط": "compress",
    # === lzma ===
    "ضغط_lzma_ضاغط_اضغط_2": "compress",
    # === zipfile ===
    "ضغط_lzma_فكّ_ضغط_فكّ_الضغط": "decompress",
    # === lzma ===
    "ضغط_lzma_فكّ_ضغط_فكّ_الضغط_2": "decompress",
    "ضغط_lzma_ملف_أغلق": "close",
    "ضغط_lzma_ملف_أفرغ": "flush",
    "ضغط_lzma_ملف_اطّلع": "peek",
    "ضغط_lzma_ملف_افصل": "detach",
    "ضغط_lzma_ملف_اقتطع": "truncate",
    "ضغط_lzma_ملف_اقرأ": "read",
    "ضغط_lzma_ملف_اقرأ1": "read1",
    "ضغط_lzma_ملف_اقرأ_في": "readinto",
    "ضغط_lzma_ملف_اقرأ_في1": "readinto1",
    "ضغط_lzma_ملف_اكتب": "write",
    "ضغط_lzma_ملف_اكتب_أسطراً": "writelines",
    "ضغط_lzma_ملف_انتقل": "seek",
    "ضغط_lzma_ملف_رقم_الملف": "fileno",
    "ضغط_lzma_ملف_سطر_قراءة": "readline",
    "ضغط_lzma_ملف_سطر_قراءة_2": "readlines",
    "ضغط_lzma_ملف_ضع_الموضع": "tell",
    "ضغط_lzma_ملف_قابل_للانتقال": "seekable",
    "ضغط_lzma_ملف_قابل_للقراءة": "readable",
    "ضغط_lzma_ملف_قابل_للكتابة": "writable",
    "ضغط_lzma_ملف_هو_طرفية": "isatty",
    # === queue ===
    "طابور_أوقف": "shutdown",
    "طابور_احصل": "get",
    "طابور_احصل_بلا_انتظار": "get_nowait",
    "طابور_اربط": "join",
    "طابور_حجم_الطابور": "qsize",
    "طابور_ضع": "put",
    "طابور_ضع_بلا_انتظار": "put_nowait",
    "طابور_فارغ_3": "empty",
    "طابور_كامل": "full",
    "طابور_مهمة_تم": "task_done",
    # === unicodedata ===
    "عددي": "numeric",
    # === gettext ===
    "عدم_ترجمات_أضف_بديل": "add_fallback",
    "عدم_ترجمات_احصل_على_النص": "gettext",
    "عدم_ترجمات_احصل_على_نص_بسياق": "pgettext",
    "عدم_ترجمات_احصل_على_نص_جمع": "ngettext",
    "عدم_ترجمات_احصل_على_نص_جمع_سياق": "npgettext",
    "عدم_ترجمات_ثبّت": "install",
    "عدم_ترجمات_مجموعة_محارف": "charset",
    "عدم_ترجمات_معلومات": "info",
    # === array ===
    "عدّ": "count",
    # === xml ===
    "عناصر_NS": "itemsNS",
    "عنصر_أدخل": "insert",
    "عنصر_أدخل_قبل": "insertBefore",
    "عنصر_أضف_ذيلياً": "append",
    "عنصر_أضف_ذيلياً_ابن": "appendChild",
    "عنصر_إلى_إكس_إم_إم": "toxml",
    "عنصر_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "عنصر_ابحث": "find",
    "عنصر_احذف": "remove",
    "عنصر_احذف_ابن": "removeChild",
    "عنصر_احصل": "get",
    "عنصر_احصل_على_الكل": "findall",
    "عنصر_احصل_على_النص": "findtext",
    "عنصر_احصل_عناصر_بواسطة_وسم_اسم": "getElementsByTagName",
    "عنصر_احصل_عناصر_بواسطة_وسم_اسم_NS": "getElementsByTagNameNS",
    "عنصر_احصل_مستخدم_بيانات": "getUserData",
    "عنصر_احصل_واجهة": "getInterface",
    "عنصر_استبدل_ابن": "replaceChild",
    "عنصر_استنسخ_عُقدة": "cloneNode",
    "عنصر_اكتب_إكس_إم_إم": "writexml",
    "عنصر_امسح": "clear",
    "عنصر_شجرة_ابحث": "find",
    "عنصر_شجرة_احصل_على_الكل": "findall",
    "عنصر_شجرة_احصل_على_النص": "findtext",
    "عنصر_شجرة_اكتب": "write",
    "عنصر_شجرة_حلل": "parse",
    "عنصر_شجرة_كرّر": "iter",
    "عنصر_شجرة_كرّر_البحث": "iterfind",
    "عنصر_عناصر": "items",
    "عنصر_عيّن": "set",
    "عنصر_عيّن_مستخدم_بيانات": "setUserData",
    "عنصر_فكّ_الرابط": "unlink",
    "عنصر_كرّر": "iter",
    "عنصر_كرّر_البحث": "iterfind",
    "عنصر_له_ابن_عُقد": "hasChildNodes",
    "عنصر_معلومات_هو_معرف": "isId",
    "عنصر_مفاتيح": "keys",
    "عنصر_هو_مدعوم": "isSupported",
    "عنصر_هو_نفس_عُقدة": "isSameNode",
    "عنصر_وحّد": "normalize",
    "عنصر_وسّع": "extend",
    "عيّن_أب": "setParent",
    "عيّن_بايت_تدفق": "setByteStream",
    "عيّن_ترميز": "setEncoding",
    # === difflib ===
    "عيّن_تسلسل1": "set_seq1",
    "عيّن_تسلسل2": "set_seq2",
    "عيّن_تسلسلات": "set_seqs",
    # === xml ===
    "عيّن_حرف_تدفق": "setCharacterStream",
    "عيّن_سمة": "setAttribute",
    "عيّن_سمة_NS": "setAttributeNS",
    "عيّن_سمة_عُقدة": "setAttributeNode",
    "عيّن_سمة_عُقدة_NS": "setAttributeNodeNS",
    "عيّن_عام_معرف": "setPublicId",
    "عيّن_معرف_سمة": "setIdAttribute",
    "عيّن_معرف_سمة_NS": "setIdAttributeNS",
    "عيّن_معرف_سمة_عُقدة": "setIdAttributeNode",
    # === shelve ===
    "عيّن_موضع": "set_location",
    # === xml ===
    "عيّن_نظام_معرف": "setSystemId",
    "عُقدة_أدخل_قبل": "insertBefore",
    "عُقدة_أضف_ذيلياً_ابن": "appendChild",
    "عُقدة_إلى_إكس_إم_إم": "toxml",
    "عُقدة_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "عُقدة_احذف_ابن": "removeChild",
    "عُقدة_احصل_مستخدم_بيانات": "getUserData",
    "عُقدة_احصل_واجهة": "getInterface",
    "عُقدة_استبدل_ابن": "replaceChild",
    "عُقدة_استنسخ_عُقدة": "cloneNode",
    "عُقدة_عيّن_مستخدم_بيانات": "setUserData",
    "عُقدة_فكّ_الرابط": "unlink",
    "عُقدة_له_ابن_عُقد": "hasChildNodes",
    "عُقدة_هو_مدعوم": "isSupported",
    "عُقدة_هو_نفس_عُقدة": "isSameNode",
    "عُقدة_وحّد": "normalize",
    # === contextlib ===
    "غير_متزامن_اخرج_مكدس_ادخل_سياق": "enter_context",
    "غير_متزامن_اخرج_مكدس_ادفع": "push",
    "غير_متزامن_اخرج_مكدس_اسحب_كل": "pop_all",
    "غير_متزامن_اخرج_مكدس_ردّ_النداء": "callback",
    # === tarfile ===
    "غيّر_الإذن": "chmod",
    "غيّر_المالك": "chown",
    # === unicodedata ===
    "فئة": "category",
    # === struct ===
    "فكّ_الحزمة_من": "unpack_from",
    # === array ===
    "فهرس": "index",
    # === io ===
    "قارئ_اقرأ": "read",
    "كاتب_اكتب": "write",
    # === xml ===
    "كرّر_النصوص": "itertext",
    # === struct ===
    "كرّر_فكّ_الحزمة": "iter_unpack",
    # === weakref ===
    "كرّر_مراجع_القيم": "itervaluerefs",
    # === xml ===
    "كيان_أدخل_قبل": "insertBefore",
    "كيان_أضف_ذيلياً_ابن": "appendChild",
    "كيان_إلى_إكس_إم_إم": "toxml",
    "كيان_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "كيان_احذف_ابن": "removeChild",
    "كيان_احصل_مستخدم_بيانات": "getUserData",
    "كيان_احصل_واجهة": "getInterface",
    "كيان_استبدل_ابن": "replaceChild",
    "كيان_استنسخ_عُقدة": "cloneNode",
    "كيان_عيّن_مستخدم_بيانات": "setUserData",
    "كيان_فكّ_الرابط": "unlink",
    "كيان_له_ابن_عُقد": "hasChildNodes",
    "كيان_محلّل_حلّ_كيان": "resolveEntity",
    "كيان_هو_مدعوم": "isSupported",
    "كيان_هو_نفس_عُقدة": "isSameNode",
    "كيان_وحّد": "normalize",
    "له_سمات": "hasAttributes",
    "له_سمة": "hasAttribute",
    "له_سمة_NS": "hasAttributeNS",
    "له_ميزة": "hasFeature",
    "محتوى_معالج_أحرف": "characters",
    "محتوى_معالج_أنهِ_بادئة_خريطة": "endPrefixMapping",
    "محتوى_معالج_أنهِ_عنصر": "endElement",
    "محتوى_معالج_أنهِ_عنصر_NS": "endElementNS",
    "محتوى_معالج_أنهِ_مستند": "endDocument",
    "محتوى_معالج_ابدأ_بادئة_خريطة": "startPrefixMapping",
    "محتوى_معالج_ابدأ_عنصر": "startElement",
    "محتوى_معالج_ابدأ_عنصر_NS": "startElementNS",
    "محتوى_معالج_ابدأ_مستند": "startDocument",
    "محتوى_معالج_عيّن_مستند_محدّد": "setDocumentLocator",
    "محتوى_معالج_قابل_للتجاهل_مسافة_بيضاء": "ignorableWhitespace",
    "محتوى_معالج_معالجة_تعليمة": "processingInstruction",
    "محتوى_معالج_مُتخطَّى_كيان": "skippedEntity",
    "محدّد_احصل_عام_معرف": "getPublicId",
    "محدّد_احصل_نظام_معرف": "getSystemId",
    # === types ===
    "محذوف": "deleter",
    # === xml ===
    "محلل_ساكس_2_نموذج_كائن_أحرف": "characters",
    "محلل_ساكس_2_نموذج_كائن_أنهِ_بادئة_خريطة": "endPrefixMapping",
    "محلل_ساكس_2_نموذج_كائن_أنهِ_عنصر": "endElement",
    "محلل_ساكس_2_نموذج_كائن_أنهِ_عنصر_NS": "endElementNS",
    "محلل_ساكس_2_نموذج_كائن_أنهِ_مستند": "endDocument",
    "محلل_ساكس_2_نموذج_كائن_ابدأ_بادئة_خريطة": "startPrefixMapping",
    "محلل_ساكس_2_نموذج_كائن_ابدأ_عنصر": "startElement",
    "محلل_ساكس_2_نموذج_كائن_ابدأ_عنصر_NS": "startElementNS",
    "محلل_ساكس_2_نموذج_كائن_ابدأ_مستند": "startDocument",
    "محلل_ساكس_2_نموذج_كائن_ابنِ_مستند": "buildDocument",
    "محلل_ساكس_2_نموذج_كائن_اسحب": "pop",
    "محلل_ساكس_2_نموذج_كائن_امسح": "clear",
    "محلل_ساكس_2_نموذج_كائن_تعليق": "comment",
    "محلل_ساكس_2_نموذج_كائن_عيّن_مستند_محدّد": "setDocumentLocator",
    "محلل_ساكس_2_نموذج_كائن_قابل_للتجاهل_مسافة_بيضاء": "ignorableWhitespace",
    "محلل_ساكس_2_نموذج_كائن_معالجة_تعليمة": "processingInstruction",
    "محلل_ساكس_2_نموذج_كائن_مُتخطَّى_كيان": "skippedEntity",
    # === array ===
    "مخزن_مؤقت_معلومات": "buffer_info",
    # === weakref ===
    "مراجع_القيم": "valuerefs",
    "مراجع_المفاتيح": "keyrefs",
    # === filecmp ===
    "مرحلة0": "phase0",
    "مرحلة1": "phase1",
    "مرحلة2": "phase2",
    "مرحلة3": "phase3",
    "مرحلة4": "phase4",
    "مرحلة4_إغلاق": "phase4_closure",
    # === numbers ===
    "مركّب_مرافق": "conjugate",
    # === codecs ===
    "مرمّز_تدفق_قارئ_سطر_قراءة": "readlines",
    "مرمّز_تدفق_قارئ_كاتب_سطر_قراءة": "readlines",
    "مرمّز_تدفق_مُعادِل_الترميز_سطر_قراءة": "readlines",
    "مرمّز_رمّز": "encode",
    "مرمّز_فكّ_ترميز": "decode",
    # === xml ===
    "مستند_أدخل_قبل": "insertBefore",
    "مستند_أضف_ذيلياً_ابن": "appendChild",
    "مستند_أنشئ_عنصر": "createElement",
    "مستند_إلى_إكس_إم_إم": "toxml",
    "مستند_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "مستند_احذف_ابن": "removeChild",
    "مستند_احصل_عناصر_بواسطة_وسم_اسم": "getElementsByTagName",
    "مستند_احصل_عناصر_بواسطة_وسم_اسم_NS": "getElementsByTagNameNS",
    "مستند_احصل_مستخدم_بيانات": "getUserData",
    "مستند_احصل_واجهة": "getInterface",
    "مستند_استبدل_ابن": "replaceChild",
    "مستند_استنسخ_عُقدة": "cloneNode",
    "مستند_اكتب_إكس_إم_إم": "writexml",
    "مستند_جزء_أدخل_قبل": "insertBefore",
    "مستند_جزء_أضف_ذيلياً_ابن": "appendChild",
    "مستند_جزء_إلى_إكس_إم_إم": "toxml",
    "مستند_جزء_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "مستند_جزء_احذف_ابن": "removeChild",
    "مستند_جزء_احصل_مستخدم_بيانات": "getUserData",
    "مستند_جزء_احصل_واجهة": "getInterface",
    "مستند_جزء_استبدل_ابن": "replaceChild",
    "مستند_جزء_استنسخ_عُقدة": "cloneNode",
    "مستند_جزء_عيّن_مستخدم_بيانات": "setUserData",
    "مستند_جزء_فكّ_الرابط": "unlink",
    "مستند_جزء_له_ابن_عُقد": "hasChildNodes",
    "مستند_جزء_هو_مدعوم": "isSupported",
    "مستند_جزء_هو_نفس_عُقدة": "isSameNode",
    "مستند_جزء_وحّد": "normalize",
    "مستند_عيّن_مستخدم_بيانات": "setUserData",
    "مستند_فكّ_الرابط": "unlink",
    "مستند_له_ابن_عُقد": "hasChildNodes",
    "مستند_نوع_أدخل_قبل": "insertBefore",
    "مستند_نوع_أضف_ذيلياً_ابن": "appendChild",
    "مستند_نوع_إلى_إكس_إم_إم": "toxml",
    "مستند_نوع_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "مستند_نوع_احذف_ابن": "removeChild",
    "مستند_نوع_احصل_مستخدم_بيانات": "getUserData",
    "مستند_نوع_احصل_واجهة": "getInterface",
    "مستند_نوع_استبدل_ابن": "replaceChild",
    "مستند_نوع_استنسخ_عُقدة": "cloneNode",
    "مستند_نوع_اكتب_إكس_إم_إم": "writexml",
    "مستند_نوع_عيّن_مستخدم_بيانات": "setUserData",
    "مستند_نوع_فكّ_الرابط": "unlink",
    "مستند_نوع_له_ابن_عُقد": "hasChildNodes",
    "مستند_نوع_هو_مدعوم": "isSupported",
    "مستند_نوع_هو_نفس_عُقدة": "isSameNode",
    "مستند_نوع_وحّد": "normalize",
    "مستند_هو_مدعوم": "isSupported",
    "مستند_هو_نفس_عُقدة": "isSameNode",
    "مستند_وحّد": "normalize",
    # === array ===
    "مصفوفة_نوع_أدخل": "insert",
    "مصفوفة_نوع_أضف_ذيلياً": "append",
    "مصفوفة_نوع_إلى_بايتات": "tobytes",
    "مصفوفة_نوع_إلى_ملف": "tofile",
    "مصفوفة_نوع_احذف": "remove",
    "مصفوفة_نوع_اسحب": "pop",
    "مصفوفة_نوع_اعكس": "reverse",
    "مصفوفة_نوع_امسح": "clear",
    "مصفوفة_نوع_من_قائمة": "fromlist",
    "مصفوفة_نوع_من_ملف": "fromfile",
    "مصفوفة_نوع_وسّع": "extend",
    # === xml ===
    "معالجة_تعليمة_أدخل_قبل": "insertBefore",
    "معالجة_تعليمة_أضف_ذيلياً_ابن": "appendChild",
    "معالجة_تعليمة_إلى_إكس_إم_إم": "toxml",
    "معالجة_تعليمة_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "معالجة_تعليمة_احذف_ابن": "removeChild",
    "معالجة_تعليمة_احصل_مستخدم_بيانات": "getUserData",
    "معالجة_تعليمة_احصل_واجهة": "getInterface",
    "معالجة_تعليمة_استبدل_ابن": "replaceChild",
    "معالجة_تعليمة_استنسخ_عُقدة": "cloneNode",
    "معالجة_تعليمة_اكتب_إكس_إم_إم": "writexml",
    "معالجة_تعليمة_عيّن_مستخدم_بيانات": "setUserData",
    "معالجة_تعليمة_فكّ_الرابط": "unlink",
    "معالجة_تعليمة_له_ابن_عُقد": "hasChildNodes",
    "معالجة_تعليمة_هو_مدعوم": "isSupported",
    "معالجة_تعليمة_هو_نفس_عُقدة": "isSameNode",
    "معالجة_تعليمة_وحّد": "normalize",
    "معجمي_معالج_تعليق": "comment",
    # === unicodedata ===
    "معيار_يونيكود_اسم": "name",
    "معيار_يونيكود_بحث": "lookup",
    "معيار_يونيكود_تفكيك": "decomposition",
    "معيار_يونيكود_عشري": "decimal",
    "معيار_يونيكود_معكوس": "mirrored",
    "معيار_يونيكود_وحّد": "normalize",
    # === xml ===
    "مفاتيح_NS": "keysNS",
    # === difflib ===
    "مكتبة_الفروق_قارن": "compare",
    # === fileinput ===
    "ملف_إدخال_أغلق": "close",
    # === io ===
    "ملف_إدخال_إخراج_أغلق": "close",
    "ملف_إدخال_إخراج_أفرغ": "flush",
    "ملف_إدخال_إخراج_اقتطع": "truncate",
    "ملف_إدخال_إخراج_اقرأ": "read",
    "ملف_إدخال_إخراج_اقرأ_في": "readinto",
    "ملف_إدخال_إخراج_اقرأ_كل": "readall",
    "ملف_إدخال_إخراج_اكتب": "write",
    "ملف_إدخال_إخراج_اكتب_أسطراً": "writelines",
    "ملف_إدخال_إخراج_انتقل": "seek",
    "ملف_إدخال_إخراج_رقم_الملف": "fileno",
    "ملف_إدخال_إخراج_سطر_قراءة": "readline",
    "ملف_إدخال_إخراج_سطر_قراءة_2": "readlines",
    "ملف_إدخال_إخراج_ضع_الموضع": "tell",
    "ملف_إدخال_إخراج_قابل_للانتقال": "seekable",
    "ملف_إدخال_إخراج_قابل_للقراءة": "readable",
    "ملف_إدخال_إخراج_قابل_للكتابة": "writable",
    "ملف_إدخال_إخراج_هو_طرفية": "isatty",
    # === fileinput ===
    "ملف_إدخال_اسم_ملف": "filename",
    "ملف_إدخال_رقم_السطر": "lineno",
    "ملف_إدخال_رقم_الملف": "fileno",
    "ملف_إدخال_سطر_قراءة": "readline",
    # === zipfile ===
    "ملف_رأس": "FileHeader",
    # === array ===
    "من_بايتات": "frombytes",
    # === tarfile ===
    "من_مخزن": "frombuf",
    "من_ملف_شريط": "fromtarfile",
    # === array ===
    "من_يونيكود": "fromunicode",
    # === pickle ===
    "مُحوِّل_أفرغ": "dump",
    # === io ===
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_أغلق": "close",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_أفرغ": "flush",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_افصل": "detach",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اقتطع": "truncate",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اقرأ": "read",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اقرأ1": "read1",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اقرأ_في": "readinto",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اقرأ_في1": "readinto1",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اكتب": "write",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_اكتب_أسطراً": "writelines",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_انتقل": "seek",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_رقم_الملف": "fileno",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_سطر_قراءة": "readline",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_سطر_قراءة_2": "readlines",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_ضع_الموضع": "tell",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_قابل_للانتقال": "seekable",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_قابل_للقراءة": "readable",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_قابل_للكتابة": "writable",
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_هو_طرفية": "isatty",
    # === codecs ===
    "مُخزّن_مؤقتاً_تصاعدي_مرمّز_احصل_على_الحالة": "getstate",
    "مُخزّن_مؤقتاً_تصاعدي_مرمّز_رمّز": "encode",
    "مُخزّن_مؤقتاً_تصاعدي_مرمّز_صفّر": "reset",
    "مُخزّن_مؤقتاً_تصاعدي_مرمّز_عيّن_الحالة": "setstate",
    "مُخزّن_مؤقتاً_تصاعدي_مفكّك_احصل_على_الحالة": "getstate",
    "مُخزّن_مؤقتاً_تصاعدي_مفكّك_صفّر": "reset",
    "مُخزّن_مؤقتاً_تصاعدي_مفكّك_عيّن_الحالة": "setstate",
    "مُخزّن_مؤقتاً_تصاعدي_مفكّك_فكّ_ترميز": "decode",
    # === io ===
    "مُخزّن_مؤقتاً_عشوائي_أغلق": "close",
    "مُخزّن_مؤقتاً_عشوائي_أفرغ": "flush",
    "مُخزّن_مؤقتاً_عشوائي_اطّلع": "peek",
    "مُخزّن_مؤقتاً_عشوائي_افصل": "detach",
    "مُخزّن_مؤقتاً_عشوائي_اقتطع": "truncate",
    "مُخزّن_مؤقتاً_عشوائي_اقرأ": "read",
    "مُخزّن_مؤقتاً_عشوائي_اقرأ1": "read1",
    "مُخزّن_مؤقتاً_عشوائي_اقرأ_في": "readinto",
    "مُخزّن_مؤقتاً_عشوائي_اقرأ_في1": "readinto1",
    "مُخزّن_مؤقتاً_عشوائي_اكتب": "write",
    "مُخزّن_مؤقتاً_عشوائي_اكتب_أسطراً": "writelines",
    "مُخزّن_مؤقتاً_عشوائي_انتقل": "seek",
    "مُخزّن_مؤقتاً_عشوائي_رقم_الملف": "fileno",
    "مُخزّن_مؤقتاً_عشوائي_سطر_قراءة": "readline",
    "مُخزّن_مؤقتاً_عشوائي_ضع_الموضع": "tell",
    "مُخزّن_مؤقتاً_عشوائي_قابل_للانتقال": "seekable",
    "مُخزّن_مؤقتاً_عشوائي_قابل_للقراءة": "readable",
    "مُخزّن_مؤقتاً_عشوائي_قابل_للكتابة": "writable",
    "مُخزّن_مؤقتاً_عشوائي_هو_طرفية": "isatty",
    "مُخزّن_مؤقتاً_قارئ_أغلق": "close",
    "مُخزّن_مؤقتاً_قارئ_أفرغ": "flush",
    "مُخزّن_مؤقتاً_قارئ_اطّلع": "peek",
    "مُخزّن_مؤقتاً_قارئ_افصل": "detach",
    "مُخزّن_مؤقتاً_قارئ_اقتطع": "truncate",
    "مُخزّن_مؤقتاً_قارئ_اقرأ": "read",
    "مُخزّن_مؤقتاً_قارئ_اقرأ1": "read1",
    "مُخزّن_مؤقتاً_قارئ_اقرأ_في": "readinto",
    "مُخزّن_مؤقتاً_قارئ_اقرأ_في1": "readinto1",
    "مُخزّن_مؤقتاً_قارئ_اكتب": "write",
    "مُخزّن_مؤقتاً_قارئ_اكتب_أسطراً": "writelines",
    "مُخزّن_مؤقتاً_قارئ_انتقل": "seek",
    "مُخزّن_مؤقتاً_قارئ_رقم_الملف": "fileno",
    "مُخزّن_مؤقتاً_قارئ_سطر_قراءة": "readline",
    "مُخزّن_مؤقتاً_قارئ_ضع_الموضع": "tell",
    "مُخزّن_مؤقتاً_قارئ_قابل_للانتقال": "seekable",
    "مُخزّن_مؤقتاً_قارئ_قابل_للقراءة": "readable",
    "مُخزّن_مؤقتاً_قارئ_قابل_للكتابة": "writable",
    "مُخزّن_مؤقتاً_قارئ_هو_طرفية": "isatty",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_أغلق": "close",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_أفرغ": "flush",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اطّلع": "peek",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_افصل": "detach",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اقتطع": "truncate",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اقرأ": "read",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اقرأ1": "read1",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اقرأ_في": "readinto",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اقرأ_في1": "readinto1",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اكتب": "write",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_اكتب_أسطراً": "writelines",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_انتقل": "seek",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_رقم_الملف": "fileno",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_سطر_قراءة": "readline",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_ضع_الموضع": "tell",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_قابل_للانتقال": "seekable",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_قابل_للقراءة": "readable",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_قابل_للكتابة": "writable",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_هو_طرفية": "isatty",
    "مُخزّن_مؤقتاً_كاتب_أغلق": "close",
    "مُخزّن_مؤقتاً_كاتب_أفرغ": "flush",
    "مُخزّن_مؤقتاً_كاتب_افصل": "detach",
    "مُخزّن_مؤقتاً_كاتب_اقتطع": "truncate",
    "مُخزّن_مؤقتاً_كاتب_اقرأ": "read",
    "مُخزّن_مؤقتاً_كاتب_اقرأ1": "read1",
    "مُخزّن_مؤقتاً_كاتب_اقرأ_في": "readinto",
    "مُخزّن_مؤقتاً_كاتب_اقرأ_في1": "readinto1",
    "مُخزّن_مؤقتاً_كاتب_اكتب": "write",
    "مُخزّن_مؤقتاً_كاتب_اكتب_أسطراً": "writelines",
    "مُخزّن_مؤقتاً_كاتب_انتقل": "seek",
    "مُخزّن_مؤقتاً_كاتب_رقم_الملف": "fileno",
    "مُخزّن_مؤقتاً_كاتب_سطر_قراءة": "readline",
    "مُخزّن_مؤقتاً_كاتب_ضع_الموضع": "tell",
    "مُخزّن_مؤقتاً_كاتب_قابل_للانتقال": "seekable",
    "مُخزّن_مؤقتاً_كاتب_قابل_للقراءة": "readable",
    "مُخزّن_مؤقتاً_كاتب_قابل_للكتابة": "writable",
    "مُخزّن_مؤقتاً_كاتب_هو_طرفية": "isatty",
    # === unicodedata ===
    "مُركِّب": "combining",
    # === types ===
    "مُستخرج": "getter",
    "مُعيّن": "setter",
    # === numbers ===
    "نسبي_مرافق": "conjugate",
    # === xml ===
    "نص_أدخل_بيانات": "insertData",
    "نص_أدخل_قبل": "insertBefore",
    "نص_أضف_ذيلياً_ابن": "appendChild",
    "نص_أضف_ذيلياً_بيانات": "appendData",
    # === io ===
    "نص_إدخال_إخراج_أساس_أغلق": "close",
    "نص_إدخال_إخراج_أساس_أفرغ": "flush",
    "نص_إدخال_إخراج_أساس_افصل": "detach",
    "نص_إدخال_إخراج_أساس_اقتطع": "truncate",
    "نص_إدخال_إخراج_أساس_اقرأ": "read",
    "نص_إدخال_إخراج_أساس_اكتب": "write",
    "نص_إدخال_إخراج_أساس_اكتب_أسطراً": "writelines",
    "نص_إدخال_إخراج_أساس_انتقل": "seek",
    "نص_إدخال_إخراج_أساس_رقم_الملف": "fileno",
    "نص_إدخال_إخراج_أساس_سطر_قراءة": "readline",
    "نص_إدخال_إخراج_أساس_سطر_قراءة_2": "readlines",
    "نص_إدخال_إخراج_أساس_ضع_الموضع": "tell",
    "نص_إدخال_إخراج_أساس_قابل_للانتقال": "seekable",
    "نص_إدخال_إخراج_أساس_قابل_للقراءة": "readable",
    "نص_إدخال_إخراج_أساس_قابل_للكتابة": "writable",
    "نص_إدخال_إخراج_أساس_هو_طرفية": "isatty",
    "نص_إدخال_إخراج_أغلق": "close",
    "نص_إدخال_إخراج_أفرغ": "flush",
    "نص_إدخال_إخراج_احصل_على_القيمة": "getvalue",
    "نص_إدخال_إخراج_افصل": "detach",
    "نص_إدخال_إخراج_اقتطع": "truncate",
    "نص_إدخال_إخراج_اقرأ": "read",
    "نص_إدخال_إخراج_اكتب": "write",
    "نص_إدخال_إخراج_اكتب_أسطراً": "writelines",
    "نص_إدخال_إخراج_انتقل": "seek",
    "نص_إدخال_إخراج_رقم_الملف": "fileno",
    "نص_إدخال_إخراج_سطر_قراءة": "readline",
    "نص_إدخال_إخراج_سطر_قراءة_2": "readlines",
    "نص_إدخال_إخراج_ضع_الموضع": "tell",
    "نص_إدخال_إخراج_غلاف_أغلق": "close",
    "نص_إدخال_إخراج_غلاف_أفرغ": "flush",
    "نص_إدخال_إخراج_غلاف_افصل": "detach",
    "نص_إدخال_إخراج_غلاف_اقتطع": "truncate",
    "نص_إدخال_إخراج_غلاف_اقرأ": "read",
    "نص_إدخال_إخراج_غلاف_اكتب": "write",
    "نص_إدخال_إخراج_غلاف_اكتب_أسطراً": "writelines",
    "نص_إدخال_إخراج_غلاف_انتقل": "seek",
    "نص_إدخال_إخراج_غلاف_رقم_الملف": "fileno",
    "نص_إدخال_إخراج_غلاف_سطر_قراءة": "readline",
    "نص_إدخال_إخراج_غلاف_سطر_قراءة_2": "readlines",
    "نص_إدخال_إخراج_غلاف_ضع_الموضع": "tell",
    "نص_إدخال_إخراج_غلاف_قابل_للانتقال": "seekable",
    "نص_إدخال_إخراج_غلاف_قابل_للقراءة": "readable",
    "نص_إدخال_إخراج_غلاف_قابل_للكتابة": "writable",
    "نص_إدخال_إخراج_غلاف_هو_طرفية": "isatty",
    "نص_إدخال_إخراج_قابل_للانتقال": "seekable",
    "نص_إدخال_إخراج_قابل_للقراءة": "readable",
    "نص_إدخال_إخراج_قابل_للكتابة": "writable",
    "نص_إدخال_إخراج_هو_طرفية": "isatty",
    # === xml ===
    "نص_إلى_إكس_إم_إم": "toxml",
    "نص_إلى_إكس_إم_إم_جميل": "toprettyxml",
    "نص_احذف_ابن": "removeChild",
    "نص_احذف_بيانات": "deleteData",
    "نص_احصل_مستخدم_بيانات": "getUserData",
    "نص_احصل_واجهة": "getInterface",
    "نص_استبدل_ابن": "replaceChild",
    "نص_استبدل_بيانات": "replaceData",
    "نص_استبدل_كامل_نص": "replaceWholeText",
    "نص_استنسخ_عُقدة": "cloneNode",
    "نص_افصل_نص": "splitText",
    "نص_اكتب_إكس_إم_إم": "writexml",
    "نص_عيّن_مستخدم_بيانات": "setUserData",
    "نص_فكّ_الرابط": "unlink",
    "نص_له_ابن_عُقد": "hasChildNodes",
    "نص_نص_فرعي_بيانات": "substringData",
    "نص_هو_مدعوم": "isSupported",
    "نص_هو_نفس_عُقدة": "isSameNode",
    "نص_وحّد": "normalize",
    "نموذج_كائن_تنفيذ_احصل_واجهة": "getInterface",
    "نموذج_كائن_حدث_تدفق_امسح": "clear",
    "نموذج_كائن_حدث_تدفق_صفّر": "reset",
    # === tarfile ===
    "هو_أنبوب": "isfifo",
    # === fileinput ===
    "هو_إدخال_قياسي": "isstdin",
    "هو_السطر_الأول": "isfirstline",
    # === tarfile ===
    "هو_جهاز": "isdev",
    "هو_جهاز_حرفي": "ischr",
    "هو_جهاز_كتلي": "isblk",
    "هو_رابط_رمزي": "issym",
    "هو_رابط_صلب": "islnk",
    # === xml ===
    "هو_عنصر_محتوى": "isElementContent",
    "هو_فارغ": "isEmpty",
    # === tarfile ===
    "هو_متفرّق": "issparse",
    # === xml ===
    "هو_معرف_NS": "isIdNS",
    # === tarfile ===
    "هو_ملف_عادي": "isreg",
    # === unicodedata ===
    "هو_موحّد": "is_normalized",
    # === graphlib ===
    "هو_نشط": "is_active",
    # === xml ===
    "وسّع_عُقدة": "expandNode",
    # === tarfile ===
    "وقت_الاستخدام": "utime",
}


DF_PROPS = {
    # خصائص الأصناف
    # === difflib ===
    "B": "b",
    # === bz2 ===
    "BZ_2_فكّ_ضغط_غير_مستخدم_بيانات": "unused_data",
    "BZ_2_فكّ_ضغط_نهاية_الملف": "eof",
    "BZ_2_فكّ_ضغط_يحتاج_إدخال": "needs_input",
    "BZ_2_ملف_اسم": "name",
    "BZ_2_ملف_مغلق": "closed",
    "BZ_2_ملف_وضع": "mode",
    # === gettext ===
    "B_سحري": "BE_MAGIC",
    # === tarfile ===
    "EX_ملف_كائن_اسم": "name",
    "EX_ملف_كائن_خام": "raw",
    "EX_ملف_كائن_مغلق": "closed",
    "EX_ملف_كائن_وضع": "mode",
    "GID": "gid",
    # === gettext ===
    "LE_سحري": "LE_MAGIC",
    # === zipfile ===
    "PY_أرشيف_مضغوط_ملف_تعليق": "comment",
    "PY_أرشيف_مضغوط_ملف_مؤشر_ملف": "fp",
    # === tarfile ===
    "UID": "uid",
    # === xml ===
    "XML_شجرة_عناصر_عنصر_شجرة_سمة": "attrib",
    "XML_شجرة_عناصر_عنصر_شجرة_كيان": "entity",
    "XML_محلل_إصدار": "version",
    "XML_محلل_هدف": "target",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_ترميز_عُقدة": "NOTATION_NODE",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_تعليق_عُقدة": "COMMENT_NODE",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_سمة_عُقدة": "ATTRIBUTE_NODE",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_عنصر_عُقدة": "ELEMENT_NODE",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_كيان_عُقدة": "ENTITY_NODE",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_مستند_عُقدة": "DOCUMENT_NODE",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "XML_نموذج_كائن_DOM_صغير_عُقدة_نص_عُقدة": "TEXT_NODE",
    # === difflib ===
    "أ": "a",
    # === zipfile ===
    "أدنى_اقرأ_حجم": "MIN_READ_SIZE",
    "أرشيف_مضغوط_امتداد_ملف_مغلق": "closed",
    "أرشيف_مضغوط_معلومات_اسم_ملف": "filename",
    "أرشيف_مضغوط_معلومات_تاريخ_وقت": "date_time",
    "أرشيف_مضغوط_معلومات_تعليق": "comment",
    "أرشيف_مضغوط_ملف_تعليق": "comment",
    "أرشيف_مضغوط_ملف_مؤشر_ملف": "fp",
    "أصلي_اسم_ملف": "orig_filename",
    # === io ===
    "أغلق_الملف": "closefd",
    # === zipfile ===
    "أقصى_N": "MAX_N",
    "أقصى_انتقل_اقرأ": "MAX_SEEK_READ",
    "أنشئ_إصدار": "create_version",
    "أنشئ_نظام": "create_system",
    # === weakref ===
    "أنهِ_خروج": "atexit",
    # === io ===
    "إدخال_إخراج_أساس_مغلق": "closed",
    # === tarfile ===
    "إزاحة_بيانات": "offset_data",
    # === gettext ===
    "إصدارات": "VERSIONS",
    # === zipfile ===
    "إضافي": "extra",
    # === gettext ===
    "احصل_على_النص_سياق": "CONTEXT",
    # === tarfile ===
    "استخراج_رشّح": "extraction_filter",
    # === zipfile ===
    "استخرج_إصدار": "extract_version",
    # === xml ===
    "اسحب_نموذج_كائن_مستند": "document",
    # === tarfile ===
    "اسم_الرابط": "linkname",
    "اسم_المجموعة": "gname",
    "اسم_النظام": "uname",
    # === zipfile ===
    "اضغط_حجم": "compress_size",
    "اضغط_مستوى": "compress_level",
    "اضغط_نوع": "compress_type",
    # === tarfile ===
    "افتح_دالة": "OPEN_METH",
    # === xml ===
    "اقرأ_فقط_تسلسلي_مسمّى_عُقدة_خريطة_طول": "length",
    # === io ===
    "اكتب_عبر": "write_through",
    # === xml ===
    "المالك_عنصر": "ownerElement",
    # === io ===
    "بايتات_إدخال_إخراج_مغلق": "closed",
    # === xml ===
    "بلا_أبناء_أخير_ابن": "lastChild",
    "بلا_أبناء_أول_ابن": "firstChild",
    "بلا_أبناء_ابن_عُقد": "childNodes",
    "بلا_أبناء_سمات": "attributes",
    "بلا_بيانات_مسموح_خطأ_كود": "code",
    "بلا_تعديل_مسموح_خطأ_كود": "code",
    # === weakref ===
    "بمفاتيح_مرجع_مفتاح": "key",
    # === struct ===
    "بنية_حجم": "size",
    "بنية_نسّق": "format",
    # === codecs ===
    "بيانات_ترميز": "data_encoding",
    # === xml ===
    "بيانات_ج_قسم_أب_عُقدة": "parentNode",
    "بيانات_ج_قسم_أخير_ابن": "lastChild",
    "بيانات_ج_قسم_أول_ابن": "firstChild",
    "بيانات_ج_قسم_ابن_عُقد": "childNodes",
    "بيانات_ج_قسم_التالي_شقيق": "nextSibling",
    "بيانات_ج_قسم_السابق_شقيق": "previousSibling",
    "بيانات_ج_قسم_المالك_مستند": "ownerDocument",
    "بيانات_ج_قسم_بادئة": "prefix",
    "بيانات_ج_قسم_بيانات": "data",
    "بيانات_ج_قسم_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "بيانات_ج_قسم_ترميز_عُقدة": "NOTATION_NODE",
    "بيانات_ج_قسم_تعليق_عُقدة": "COMMENT_NODE",
    "بيانات_ج_قسم_سمات": "attributes",
    "بيانات_ج_قسم_سمة_عُقدة": "ATTRIBUTE_NODE",
    "بيانات_ج_قسم_طول": "length",
    "بيانات_ج_قسم_عنصر_عُقدة": "ELEMENT_NODE",
    "بيانات_ج_قسم_عُقدة_اسم": "nodeName",
    "بيانات_ج_قسم_عُقدة_قيمة": "nodeValue",
    "بيانات_ج_قسم_عُقدة_نوع": "nodeType",
    "بيانات_ج_قسم_كامل_نص": "wholeText",
    "بيانات_ج_قسم_كيان_عُقدة": "ENTITY_NODE",
    "بيانات_ج_قسم_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "بيانات_ج_قسم_محلي_اسم": "localName",
    "بيانات_ج_قسم_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "بيانات_ج_قسم_مستند_عُقدة": "DOCUMENT_NODE",
    "بيانات_ج_قسم_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "بيانات_ج_قسم_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "بيانات_ج_قسم_نص_عُقدة": "TEXT_NODE",
    "بيانات_ج_قسم_نطاق_اسم_URI": "namespaceURI",
    "بيانات_ج_قسم_هو_مسافة_بيضاء_في_عنصر_محتوى": "isWhitespaceInElementContent",
    # === unicodedata ===
    "بيانات_يونيكود_إصدار": "unidata_version",
    # === tarfile ===
    "تجاهل_أصفار": "ignore_zeros",
    # === xml ===
    "تحقق_خطأ_كود": "code",
    # === codecs ===
    "تدفق_قارئ_كاتب_ترميز": "encoding",
    # === xml ===
    "ترميز_أب_عُقدة": "parentNode",
    "ترميز_أخير_ابن": "lastChild",
    "ترميز_أول_ابن": "firstChild",
    "ترميز_ابن_عُقد": "childNodes",
    "ترميز_التالي_شقيق": "nextSibling",
    "ترميز_السابق_شقيق": "previousSibling",
    "ترميز_المالك_مستند": "ownerDocument",
    "ترميز_بادئة": "prefix",
    "ترميز_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "ترميز_ترميز_عُقدة": "NOTATION_NODE",
    "ترميز_تعليق_عُقدة": "COMMENT_NODE",
    "ترميز_سمات": "attributes",
    "ترميز_سمة_عُقدة": "ATTRIBUTE_NODE",
    "ترميز_عام_معرف": "publicId",
    "ترميز_عنصر_عُقدة": "ELEMENT_NODE",
    "ترميز_عُقدة_قيمة": "nodeValue",
    "ترميز_عُقدة_نوع": "nodeType",
    "ترميز_كيان_عُقدة": "ENTITY_NODE",
    "ترميز_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "ترميز_محلي_اسم": "localName",
    "ترميز_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "ترميز_مستند_عُقدة": "DOCUMENT_NODE",
    "ترميز_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "ترميز_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "ترميز_نص_عُقدة": "TEXT_NODE",
    "ترميز_نطاق_اسم_URI": "namespaceURI",
    "ترميز_نظام_معرف": "systemId",
    "تسلسل_هرمي_اطلب_خطأ_كود": "code",
    # === io ===
    "تصاعدي_سطر_جديد_مفكّك_سطر_جديد": "newlines",
    # === xml ===
    "تعليق_أب_عُقدة": "parentNode",
    "تعليق_أخير_ابن": "lastChild",
    "تعليق_أول_ابن": "firstChild",
    "تعليق_ابن_عُقد": "childNodes",
    "تعليق_التالي_شقيق": "nextSibling",
    "تعليق_السابق_شقيق": "previousSibling",
    "تعليق_المالك_مستند": "ownerDocument",
    "تعليق_بادئة": "prefix",
    "تعليق_بيانات": "data",
    "تعليق_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "تعليق_ترميز_عُقدة": "NOTATION_NODE",
    "تعليق_تعليق_عُقدة": "COMMENT_NODE",
    "تعليق_سمات": "attributes",
    "تعليق_سمة_عُقدة": "ATTRIBUTE_NODE",
    "تعليق_طول": "length",
    "تعليق_عنصر_عُقدة": "ELEMENT_NODE",
    "تعليق_عُقدة_اسم": "nodeName",
    "تعليق_عُقدة_قيمة": "nodeValue",
    "تعليق_عُقدة_نوع": "nodeType",
    "تعليق_كيان_عُقدة": "ENTITY_NODE",
    "تعليق_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "تعليق_محلي_اسم": "localName",
    "تعليق_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "تعليق_مستند_عُقدة": "DOCUMENT_NODE",
    "تعليق_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "تعليق_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "تعليق_نص_عُقدة": "TEXT_NODE",
    "تعليق_نطاق_اسم_URI": "namespaceURI",
    # === tarfile ===
    "تنسيق_pax_رؤوس": "pax_headers",
    # === xml ===
    "تنفيذ": "implementation",
    # === pickle ===
    "توزيع_جدول": "dispatch_table",
    # === array ===
    "حجم_العنصر": "itemsize",
    # === xml ===
    "حرف_بيانات_أب_عُقدة": "parentNode",
    "حرف_بيانات_أخير_ابن": "lastChild",
    "حرف_بيانات_أول_ابن": "firstChild",
    "حرف_بيانات_ابن_عُقد": "childNodes",
    "حرف_بيانات_التالي_شقيق": "nextSibling",
    "حرف_بيانات_السابق_شقيق": "previousSibling",
    "حرف_بيانات_المالك_مستند": "ownerDocument",
    "حرف_بيانات_بادئة": "prefix",
    "حرف_بيانات_بيانات": "data",
    "حرف_بيانات_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "حرف_بيانات_ترميز_عُقدة": "NOTATION_NODE",
    "حرف_بيانات_تعليق_عُقدة": "COMMENT_NODE",
    "حرف_بيانات_سمات": "attributes",
    "حرف_بيانات_سمة_عُقدة": "ATTRIBUTE_NODE",
    "حرف_بيانات_طول": "length",
    "حرف_بيانات_عنصر_عُقدة": "ELEMENT_NODE",
    "حرف_بيانات_عُقدة_قيمة": "nodeValue",
    "حرف_بيانات_كيان_عُقدة": "ENTITY_NODE",
    "حرف_بيانات_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "حرف_بيانات_محلي_اسم": "localName",
    "حرف_بيانات_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "حرف_بيانات_مستند_عُقدة": "DOCUMENT_NODE",
    "حرف_بيانات_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "حرف_بيانات_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "حرف_بيانات_نص_عُقدة": "TEXT_NODE",
    "حرف_بيانات_نطاق_اسم_URI": "namespaceURI",
    # === numbers ===
    "حقيقي_جزء_تخيلي": "imag",
    "حقيقي_حقيقي": "real",
    # === weakref ===
    "حيّ": "alive",
    # === zipfile ===
    "خارجي_سمة": "external_attr",
    # === io ===
    "خام_إدخال_إخراج_أساس_مغلق": "closed",
    # === xml ===
    "خطأ_مستند_خطأ_كود": "code",
    "خطأ_معالج": "errorHandler",
    # === zipfile ===
    "داخلي_سمة": "internal_attr",
    # === xml ===
    "داخلي_مجموعة_جزئية": "internalSubset",
    # === filecmp ===
    "دالة_خريطة": "methodmap",
    # === xml ===
    "ذيل": "tail",
    # === zipfile ===
    "رأس_إزاحة": "header_offset",
    # === tarfile ===
    "رقم_الجهاز_الثانوي": "devminor",
    "رقم_الجهاز_الرئيسي": "devmajor",
    # === array ===
    "رمز_النوع": "typecode",
    # === xml ===
    "سمة_أب_عُقدة": "parentNode",
    "سمة_أخير_ابن": "lastChild",
    "سمة_أول_ابن": "firstChild",
    "سمة_ابن_عُقد": "childNodes",
    "سمة_اسم": "name",
    "سمة_التالي_شقيق": "nextSibling",
    "سمة_السابق_شقيق": "previousSibling",
    "سمة_المالك_مستند": "ownerDocument",
    "سمة_بادئة": "prefix",
    "سمة_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "سمة_ترميز_عُقدة": "NOTATION_NODE",
    "سمة_تعليق_عُقدة": "COMMENT_NODE",
    "سمة_سمات": "attributes",
    "سمة_سمة_عُقدة": "ATTRIBUTE_NODE",
    "سمة_عنصر_عُقدة": "ELEMENT_NODE",
    "سمة_عُقدة_اسم": "nodeName",
    "سمة_عُقدة_قيمة": "nodeValue",
    "سمة_عُقدة_نوع": "nodeType",
    "سمة_قائمة_طول": "length",
    "سمة_قيمة": "value",
    "سمة_كيان_عُقدة": "ENTITY_NODE",
    "سمة_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "سمة_محلي_اسم": "localName",
    "سمة_مخطط_نوع": "schemaType",
    "سمة_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "سمة_مستند_عُقدة": "DOCUMENT_NODE",
    "سمة_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "سمة_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "سمة_نص_عُقدة": "TEXT_NODE",
    "سمة_نطاق_اسم_URI": "namespaceURI",
    "سمة_هو_معرف": "isId",
    # === contextvars ===
    "سياق_متغير_اسم": "name",
    # === tarfile ===
    "شريط_أرشيف_معلومات_إزاحة": "offset",
    "شريط_أرشيف_معلومات_اسم": "name",
    "شريط_أرشيف_معلومات_حجم": "size",
    "شريط_أرشيف_معلومات_نوع": "type",
    "شريط_أرشيف_معلومات_وضع": "mode",
    "شريط_أرشيف_معلومات_وقت_التعديل": "mtime",
    "شريط_أرشيف_ملف_أخطاء": "errors",
    "شريط_أرشيف_ملف_ترميز": "encoding",
    "شريط_أرشيف_ملف_تصحيح": "debug",
    "شريط_أرشيف_ملف_نسّق": "format",
    # === xml ===
    "صارم_خطأ_فحص": "strictErrorChecking",
    # === numbers ===
    "صحيح_بسط": "numerator",
    "صحيح_جزء_تخيلي": "imag",
    "صحيح_حقيقي": "real",
    "صحيح_مقام": "denominator",
    # === xml ===
    "صياغة_خطأ_كود": "code",
    # === gzip ===
    "ضغط_gzip_ملف_مغلق": "closed",
    "ضغط_gzip_ملف_وقت_التعديل": "mtime",
    # === lzma ===
    "ضغط_lzma_فكّ_ضغط_تحقق": "check",
    "ضغط_lzma_فكّ_ضغط_غير_مستخدم_بيانات": "unused_data",
    "ضغط_lzma_فكّ_ضغط_نهاية_الملف": "eof",
    "ضغط_lzma_فكّ_ضغط_يحتاج_إدخال": "needs_input",
    "ضغط_lzma_ملف_اسم": "name",
    "ضغط_lzma_ملف_مغلق": "closed",
    "ضغط_lzma_ملف_وضع": "mode",
    # === difflib ===
    "طابق_حجم": "size",
    # === zipfile ===
    "علامة_بتات": "flag_bits",
    # === xml ===
    "عنصر_أب_عُقدة": "parentNode",
    "عنصر_أخير_ابن": "lastChild",
    "عنصر_أول_ابن": "firstChild",
    "عنصر_ابن_عُقد": "childNodes",
    "عنصر_التالي_شقيق": "nextSibling",
    "عنصر_السابق_شقيق": "previousSibling",
    "عنصر_المالك_مستند": "ownerDocument",
    "عنصر_بادئة": "prefix",
    "عنصر_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "عنصر_ترميز_عُقدة": "NOTATION_NODE",
    "عنصر_تعليق_عُقدة": "COMMENT_NODE",
    "عنصر_سمات": "attributes",
    "عنصر_سمة_عُقدة": "ATTRIBUTE_NODE",
    "عنصر_عنصر_عُقدة": "ELEMENT_NODE",
    "عنصر_عُقدة_اسم": "nodeName",
    "عنصر_عُقدة_قيمة": "nodeValue",
    "عنصر_عُقدة_نوع": "nodeType",
    "عنصر_كيان_عُقدة": "ENTITY_NODE",
    "عنصر_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "عنصر_محلي_اسم": "localName",
    "عنصر_مخطط_نوع": "schemaType",
    "عنصر_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "عنصر_مستند_عُقدة": "DOCUMENT_NODE",
    "عنصر_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "عنصر_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "عنصر_معلومات_وسم_اسم": "tagName",
    "عنصر_نص": "text",
    "عنصر_نص_عُقدة": "TEXT_NODE",
    "عنصر_نطاق_اسم_URI": "namespaceURI",
    "عنصر_وسم": "tag",
    "عنصر_وسم_اسم": "tagName",
    "عُقدة_أب_عُقدة": "parentNode",
    "عُقدة_أخير_ابن": "lastChild",
    "عُقدة_أول_ابن": "firstChild",
    "عُقدة_أُعيد_تسميته": "NODE_RENAMED",
    "عُقدة_التالي_شقيق": "nextSibling",
    "عُقدة_السابق_شقيق": "previousSibling",
    "عُقدة_المالك_مستند": "ownerDocument",
    "عُقدة_بادئة": "prefix",
    "عُقدة_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "عُقدة_ترميز_عُقدة": "NOTATION_NODE",
    "عُقدة_تعليق_عُقدة": "COMMENT_NODE",
    "عُقدة_سمة_عُقدة": "ATTRIBUTE_NODE",
    "عُقدة_عنصر_عُقدة": "ELEMENT_NODE",
    "عُقدة_كيان_عُقدة": "ENTITY_NODE",
    "عُقدة_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "عُقدة_محذوف": "NODE_DELETED",
    "عُقدة_محلي_اسم": "localName",
    "عُقدة_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "عُقدة_مستند_عُقدة": "DOCUMENT_NODE",
    "عُقدة_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "عُقدة_مستورد": "NODE_IMPORTED",
    "عُقدة_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "عُقدة_مُستنسخ": "NODE_CLONED",
    "عُقدة_نص_عُقدة": "TEXT_NODE",
    "عُقدة_نطاق_اسم_URI": "namespaceURI",
    "غير_صالح_تعديل_خطأ_كود": "code",
    "غير_صالح_حالة_خطأ_كود": "code",
    "غير_صالح_حرف_خطأ_كود": "code",
    "غير_صالح_وصول_خطأ_كود": "code",
    # === zipfile ===
    "فحص_تكرار": "CRC",
    # === tarfile ===
    "فكّ_المرجع": "dereference",
    # === xml ===
    "فهرس_حجم_خطأ_كود": "code",
    # === contextvars ===
    "قديم_قيمة": "old_value",
    # === tarfile ===
    "كائن_ملف": "fileobject",
    # === gzip ===
    "كائن_ملفي": "myfileobj",
    # === xml ===
    "كيان_أب_عُقدة": "parentNode",
    "كيان_أخير_ابن": "lastChild",
    "كيان_أول_ابن": "firstChild",
    "كيان_إصدار": "version",
    "كيان_التالي_شقيق": "nextSibling",
    "كيان_السابق_شقيق": "previousSibling",
    "كيان_المالك_مستند": "ownerDocument",
    "كيان_بادئة": "prefix",
    "كيان_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "كيان_ترميز": "encoding",
    "كيان_ترميز_عُقدة": "NOTATION_NODE",
    "كيان_تعليق_عُقدة": "COMMENT_NODE",
    "كيان_سمات": "attributes",
    "كيان_سمة_عُقدة": "ATTRIBUTE_NODE",
    "كيان_عام_معرف": "publicId",
    "كيان_عنصر_عُقدة": "ELEMENT_NODE",
    "كيان_عُقدة_قيمة": "nodeValue",
    "كيان_عُقدة_نوع": "nodeType",
    "كيان_فعلي_ترميز": "actualEncoding",
    "كيان_كيان_عُقدة": "ENTITY_NODE",
    "كيان_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "كيان_محلي_اسم": "localName",
    "كيان_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "كيان_مستند_عُقدة": "DOCUMENT_NODE",
    "كيان_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "كيان_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "كيان_نص_عُقدة": "TEXT_NODE",
    "كيان_نطاق_اسم_URI": "namespaceURI",
    "كيان_نظام_معرف": "systemId",
    "لا_مدعوم_خطأ_كود": "code",
    "لا_موجود_خطأ_كود": "code",
    # === contextvars ===
    "متغير": "var",
    # === tarfile ===
    "متفرّق": "sparse",
    # === zipfile ===
    "مجلد_رئيسي": "volume",
    # === tarfile ===
    "مجموع_الفحص": "chksum",
    # === zipfile ===
    "محجوز": "reserved",
    # === xml ===
    "محلل_ساكس_2_نموذج_كائن_مستند": "document",
    # === io ===
    "مخزن_مؤقت": "buffer",
    # === numbers ===
    "مركّب_جزء_تخيلي": "imag",
    "مركّب_حقيقي": "real",
    # === tarfile ===
    "مسار": "path",
    "مسار_الرابط": "linkpath",
    # === xml ===
    "مستقل": "standalone",
    "مستند_URI": "documentURI",
    "مستند_أب_عُقدة": "parentNode",
    "مستند_أخير_ابن": "lastChild",
    "مستند_أول_ابن": "firstChild",
    "مستند_إصدار": "version",
    "مستند_ابن_عُقد": "childNodes",
    "مستند_التالي_شقيق": "nextSibling",
    "مستند_السابق_شقيق": "previousSibling",
    "مستند_المالك_مستند": "ownerDocument",
    "مستند_بادئة": "prefix",
    "مستند_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "مستند_ترميز": "encoding",
    "مستند_ترميز_عُقدة": "NOTATION_NODE",
    "مستند_تعليق_عُقدة": "COMMENT_NODE",
    "مستند_جزء_أب_عُقدة": "parentNode",
    "مستند_جزء_أخير_ابن": "lastChild",
    "مستند_جزء_أول_ابن": "firstChild",
    "مستند_جزء_التالي_شقيق": "nextSibling",
    "مستند_جزء_السابق_شقيق": "previousSibling",
    "مستند_جزء_المالك_مستند": "ownerDocument",
    "مستند_جزء_بادئة": "prefix",
    "مستند_جزء_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "مستند_جزء_ترميز_عُقدة": "NOTATION_NODE",
    "مستند_جزء_تعليق_عُقدة": "COMMENT_NODE",
    "مستند_جزء_سمات": "attributes",
    "مستند_جزء_سمة_عُقدة": "ATTRIBUTE_NODE",
    "مستند_جزء_عنصر_عُقدة": "ELEMENT_NODE",
    "مستند_جزء_عُقدة_اسم": "nodeName",
    "مستند_جزء_عُقدة_قيمة": "nodeValue",
    "مستند_جزء_عُقدة_نوع": "nodeType",
    "مستند_جزء_كيان_عُقدة": "ENTITY_NODE",
    "مستند_جزء_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "مستند_جزء_محلي_اسم": "localName",
    "مستند_جزء_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "مستند_جزء_مستند_عُقدة": "DOCUMENT_NODE",
    "مستند_جزء_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "مستند_جزء_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "مستند_جزء_نص_عُقدة": "TEXT_NODE",
    "مستند_جزء_نطاق_اسم_URI": "namespaceURI",
    "مستند_سمات": "attributes",
    "مستند_سمة_عُقدة": "ATTRIBUTE_NODE",
    "مستند_عنصر": "documentElement",
    "مستند_عنصر_عُقدة": "ELEMENT_NODE",
    "مستند_عُقدة_اسم": "nodeName",
    "مستند_عُقدة_قيمة": "nodeValue",
    "مستند_عُقدة_نوع": "nodeType",
    "مستند_فعلي_ترميز": "actualEncoding",
    "مستند_كيان_عُقدة": "ENTITY_NODE",
    "مستند_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "مستند_محلي_اسم": "localName",
    "مستند_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "مستند_مستند_عُقدة": "DOCUMENT_NODE",
    "مستند_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "مستند_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "مستند_نص_عُقدة": "TEXT_NODE",
    "مستند_نطاق_اسم_URI": "namespaceURI",
    "مستند_نوع_أب_عُقدة": "parentNode",
    "مستند_نوع_أخير_ابن": "lastChild",
    "مستند_نوع_أول_ابن": "firstChild",
    "مستند_نوع_ابن_عُقد": "childNodes",
    "مستند_نوع_اسم": "name",
    "مستند_نوع_التالي_شقيق": "nextSibling",
    "مستند_نوع_السابق_شقيق": "previousSibling",
    "مستند_نوع_المالك_مستند": "ownerDocument",
    "مستند_نوع_بادئة": "prefix",
    "مستند_نوع_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "مستند_نوع_ترميز_عُقدة": "NOTATION_NODE",
    "مستند_نوع_تعليق_عُقدة": "COMMENT_NODE",
    "مستند_نوع_سمات": "attributes",
    "مستند_نوع_سمة_عُقدة": "ATTRIBUTE_NODE",
    "مستند_نوع_عام_معرف": "publicId",
    "مستند_نوع_عنصر_عُقدة": "ELEMENT_NODE",
    "مستند_نوع_عُقدة_قيمة": "nodeValue",
    "مستند_نوع_عُقدة_نوع": "nodeType",
    "مستند_نوع_كيان_عُقدة": "ENTITY_NODE",
    "مستند_نوع_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "مستند_نوع_محلي_اسم": "localName",
    "مستند_نوع_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "مستند_نوع_مستند_عُقدة": "DOCUMENT_NODE",
    "مستند_نوع_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "مستند_نوع_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "مستند_نوع_نص_عُقدة": "TEXT_NODE",
    "مستند_نوع_نطاق_اسم_URI": "namespaceURI",
    "مستند_نوع_نظام_معرف": "systemId",
    # === tarfile ===
    "مستوى_الخطأ": "errorlevel",
    # === xml ===
    "معالجة_تعليمة_أب_عُقدة": "parentNode",
    "معالجة_تعليمة_أخير_ابن": "lastChild",
    "معالجة_تعليمة_أول_ابن": "firstChild",
    "معالجة_تعليمة_ابن_عُقد": "childNodes",
    "معالجة_تعليمة_التالي_شقيق": "nextSibling",
    "معالجة_تعليمة_السابق_شقيق": "previousSibling",
    "معالجة_تعليمة_المالك_مستند": "ownerDocument",
    "معالجة_تعليمة_بادئة": "prefix",
    "معالجة_تعليمة_بيانات": "data",
    "معالجة_تعليمة_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "معالجة_تعليمة_ترميز_عُقدة": "NOTATION_NODE",
    "معالجة_تعليمة_تعليق_عُقدة": "COMMENT_NODE",
    "معالجة_تعليمة_سمات": "attributes",
    "معالجة_تعليمة_سمة_عُقدة": "ATTRIBUTE_NODE",
    "معالجة_تعليمة_عنصر_عُقدة": "ELEMENT_NODE",
    "معالجة_تعليمة_عُقدة_اسم": "nodeName",
    "معالجة_تعليمة_عُقدة_قيمة": "nodeValue",
    "معالجة_تعليمة_عُقدة_نوع": "nodeType",
    "معالجة_تعليمة_كيان_عُقدة": "ENTITY_NODE",
    "معالجة_تعليمة_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "معالجة_تعليمة_محلي_اسم": "localName",
    "معالجة_تعليمة_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "معالجة_تعليمة_مستند_عُقدة": "DOCUMENT_NODE",
    "معالجة_تعليمة_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "معالجة_تعليمة_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "معالجة_تعليمة_نص_عُقدة": "TEXT_NODE",
    "معالجة_تعليمة_نطاق_اسم_URI": "namespaceURI",
    "معالجة_تعليمة_هدف": "target",
    # === tarfile ===
    "معلومات_شريط": "tarinfo",
    # === pickle ===
    "مفكّك_تحويل_ذاكرة_تحويل": "memo",
    # === io ===
    "ملف_إدخال_إخراج_مغلق": "closed",
    "ملف_إدخال_إخراج_وضع": "mode",
    # === codecs ===
    "ملف_ترميز": "file_encoding",
    # === zipfile ===
    "ملف_حجم": "file_size",
    # === tarfile ===
    "ملف_شريط_2": "tarfile",
    # === xml ===
    "مُتعرّف_عام_معرف": "publicId",
    "مُتعرّف_نظام_معرف": "systemId",
    "مُحدَّد": "specified",
    # === pickle ===
    "مُحوِّل_ثنائي": "bin",
    "مُحوِّل_ذاكرة_تحويل": "memo",
    "مُحوِّل_سريع": "fast",
    # === io ===
    "مُخزّن_مؤقتاً_إدخال_إخراج_أساس_مغلق": "closed",
    "مُخزّن_مؤقتاً_عشوائي_اسم": "name",
    "مُخزّن_مؤقتاً_عشوائي_خام": "raw",
    "مُخزّن_مؤقتاً_عشوائي_مغلق": "closed",
    "مُخزّن_مؤقتاً_عشوائي_وضع": "mode",
    "مُخزّن_مؤقتاً_قارئ_اسم": "name",
    "مُخزّن_مؤقتاً_قارئ_خام": "raw",
    "مُخزّن_مؤقتاً_قارئ_مغلق": "closed",
    "مُخزّن_مؤقتاً_قارئ_وضع": "mode",
    "مُخزّن_مؤقتاً_قراءة_كتابة_زوج_مغلق": "closed",
    "مُخزّن_مؤقتاً_كاتب_اسم": "name",
    "مُخزّن_مؤقتاً_كاتب_خام": "raw",
    "مُخزّن_مؤقتاً_كاتب_مغلق": "closed",
    "مُخزّن_مؤقتاً_كاتب_وضع": "mode",
    # === xml ===
    "مُستعمَل_سمة_خطأ_كود": "code",
    # === contextvars ===
    "ناقص": "MISSING",
    # === numbers ===
    "نسبي_بسط": "numerator",
    "نسبي_جزء_تخيلي": "imag",
    "نسبي_حقيقي": "real",
    "نسبي_مقام": "denominator",
    # === xml ===
    "نص_أب_عُقدة": "parentNode",
    "نص_أخير_ابن": "lastChild",
    "نص_أول_ابن": "firstChild",
    # === io ===
    "نص_إدخال_إخراج_أخطاء": "errors",
    "نص_إدخال_إخراج_أساس_أخطاء": "errors",
    "نص_إدخال_إخراج_أساس_ترميز": "encoding",
    "نص_إدخال_إخراج_أساس_سطر_جديد": "newlines",
    "نص_إدخال_إخراج_أساس_مغلق": "closed",
    "نص_إدخال_إخراج_ترميز": "encoding",
    "نص_إدخال_إخراج_سطر_تخزين_مؤقت": "line_buffering",
    "نص_إدخال_إخراج_سطر_جديد": "newlines",
    "نص_إدخال_إخراج_غلاف_أخطاء": "errors",
    "نص_إدخال_إخراج_غلاف_اسم": "name",
    "نص_إدخال_إخراج_غلاف_ترميز": "encoding",
    "نص_إدخال_إخراج_غلاف_سطر_تخزين_مؤقت": "line_buffering",
    "نص_إدخال_إخراج_غلاف_سطر_جديد": "newlines",
    "نص_إدخال_إخراج_غلاف_مغلق": "closed",
    "نص_إدخال_إخراج_مغلق": "closed",
    # === xml ===
    "نص_ابن_عُقد": "childNodes",
    "نص_التالي_شقيق": "nextSibling",
    "نص_السابق_شقيق": "previousSibling",
    "نص_المالك_مستند": "ownerDocument",
    "نص_بادئة": "prefix",
    "نص_بيانات": "data",
    "نص_بيانات_ج_قسم_عُقدة": "CDATA_SECTION_NODE",
    "نص_ترميز_عُقدة": "NOTATION_NODE",
    "نص_تعليق_عُقدة": "COMMENT_NODE",
    "نص_سمات": "attributes",
    "نص_سمة_عُقدة": "ATTRIBUTE_NODE",
    "نص_طول": "length",
    "نص_عنصر_عُقدة": "ELEMENT_NODE",
    "نص_عُقدة_اسم": "nodeName",
    "نص_عُقدة_قيمة": "nodeValue",
    "نص_عُقدة_نوع": "nodeType",
    "نص_كامل_نص": "wholeText",
    "نص_كيان_عُقدة": "ENTITY_NODE",
    "نص_كيان_مرجع_عُقدة": "ENTITY_REFERENCE_NODE",
    "نص_محلي_اسم": "localName",
    "نص_مستند_جزء_عُقدة": "DOCUMENT_FRAGMENT_NODE",
    "نص_مستند_عُقدة": "DOCUMENT_NODE",
    "نص_مستند_نوع_عُقدة": "DOCUMENT_TYPE_NODE",
    "نص_معالجة_تعليمة_عُقدة": "PROCESSING_INSTRUCTION_NODE",
    "نص_نص_عُقدة": "TEXT_NODE",
    "نص_نطاق_اسم_URI": "namespaceURI",
    "نص_نموذج_حجم_خطأ_كود": "code",
    "نص_هو_مسافة_بيضاء_في_عنصر_محتوى": "isWhitespaceInElementContent",
    "نطاق_اسم": "namespace",
    "نطاق_اسم_خطأ_كود": "code",
    "نوع_المستند": "doctype",
    # === codecs ===
    "نوع_مخزن_المحارف": "charbuffertype",
    # === xml ===
    "نوع_معلومات_اسم": "name",
}


DF_CONSTS = {
    # ثوابت تُكتب عارية
    # === stringprep ===
    "B1_عيّن": "stringprep.b1_set",
    "B3_استثناءات": "stringprep.b3_exceptions",
    # === dbm ===
    "DBM_خطأ": "dbm.error",
    # === locale ===
    "D_T_تنسيق": "locale.D_T_FMT",
    "D_تنسيق": "locale.D_FMT",
    # === xml ===
    "HTML_فارغ": "xml.etree.ElementTree.HTML_EMPTY",
    # === lzma ===
    "MF_BT_2": "lzma.MF_BT2",
    "MF_BT_3": "lzma.MF_BT3",
    # === tarfile ===
    "POSIX_سحري": "tarfile.POSIX_MAGIC",
    # === stat ===
    "SF_أضف_ذيلياً": "stat.SF_APPEND",
    "SF_بلا_بيانات": "stat.SF_DATALESS",
    "SF_بلا_رابط": "stat.SF_NOUNLINK",
    "SF_رابط_نير": "stat.SF_FIRMLINK",
    "SF_غير_قابل_للتعديل": "stat.SF_IMMUTABLE",
    "SF_قابل_للتعيين": "stat.SF_SETTABLE",
    "SF_لقطة": "stat.SF_SNAPSHOT",
    "SF_مؤرشَف": "stat.SF_ARCHIVED",
    "SF_مقيّد": "stat.SF_RESTRICTED",
    "ST_GID": "stat.ST_GID",
    "ST_حجم": "stat.ST_SIZE",
    "ST_عدد_الروابط": "stat.ST_NLINK",
    "ST_وقت_الإنشاء": "stat.ST_CTIME",
    "ST_وقت_التعديل": "stat.ST_MTIME",
    "ST_وقت_الوصول": "stat.ST_ATIME",
    # === locale ===
    "T_تنسيق": "locale.T_FMT",
    "T_تنسيق_ص_أو_م": "locale.T_FMT_AMPM",
    # === stat ===
    "UF_قابل_للتعيين": "stat.UF_SETTABLE",
    "UF_مخفي": "stat.UF_HIDDEN",
    # === xml ===
    "XHTML_نطاق_اسم": "xml.dom.XHTML_NAMESPACE",
    "XML_شجرة_عناصر_عنصر_شجرة_إصدار": "xml.etree.ElementTree.VERSION",
    "XML_محلل_ساكس_معالج_إصدار": "xml.sax.handler.version",
    "XML_نطاق_اسم": "xml.dom.XML_NAMESPACE",
    "XML_نموذج_كائن_اسحب_نموذج_كائن_أنهِ_عنصر": "xml.dom.pulldom.END_ELEMENT",
    "XML_نموذج_كائن_اسحب_نموذج_كائن_ابدأ_عنصر": "xml.dom.pulldom.START_ELEMENT",
    "XML_نموذج_كائن_اسحب_نموذج_كائن_تعليق": "xml.dom.pulldom.COMMENT",
    "XML_نموذج_كائن_اسحب_نموذج_كائن_معالجة_تعليمة": "xml.dom.pulldom.PROCESSING_INSTRUCTION",
    # === reprlib ===
    "أ_تمثيل": "reprlib.aRepr",
    # === xml ===
    "أحرف": "xml.dom.pulldom.CHARACTERS",
    # === pickle ===
    "أدخل_ثنائياً": "pickle.BINPUT",
    # === zipfile ===
    "أرشيف_مضغوط_64_إصدار": "zipfile.ZIP64_VERSION",
    "أرشيف_مضغوط_64_حدّ": "zipfile.ZIP64_LIMIT",
    "أرشيف_مضغوط_ضغط_zstandard": "zipfile.ZIP_ZSTANDARD",
    "أرشيف_مضغوط_عدد_الملفات_حدّ": "zipfile.ZIP_FILECOUNT_LIMIT",
    # === xml ===
    "أصلي_ترميز": "xml.parsers.expat.native_encoding",
    # === pickle ===
    "أقصى_حجم": "pickle.maxsize",
    # === xml ===
    "أنهِ_مستند": "xml.dom.pulldom.END_DOCUMENT",
    # === pickle ===
    "أوقف": "pickle.STOP",
    # === xml ===
    "إصدار_معلومات": "xml.parsers.expat.version_info",
    # === pickle ===
    "إطار": "pickle.FRAME",
    # === xml ===
    "إكس_إم_إم_إن_إس_نطاق_اسم": "xml.dom.XMLNS_NAMESPACE",
    "إكسبات_CAPI": "xml.parsers.expat.expat_CAPI",
    "إكسبات_إصدار": "xml.parsers.expat.EXPAT_VERSION",
    "ابدأ_مستند": "xml.dom.pulldom.START_DOCUMENT",
    # === pickle ===
    "ابنِ": "pickle.BUILD",
    "احصل_ثنائياً": "pickle.BINGET",
    "اختزل": "pickle.REDUCE",
    # === tarfile ===
    "اربط_رمزياً_استثناء": "tarfile.symlink_exception",
    # === pickle ===
    "اسحب": "pickle.POP",
    "اسحب_علامة": "pickle.POP_MARK",
    # === os ===
    "اسمح_ناقص": "os.path.ALLOW_MISSING",
    # === zipfile ===
    "افتراضي_إصدار": "zipfile.DEFAULT_VERSION",
    # === filecmp ===
    "افتراضي_تجاهل": "filecmp.DEFAULT_IGNORES",
    # === xml ===
    "افتراضي_حجم_المخزن": "xml.dom.pulldom.default_bufsize",
    "افتراضي_محلل_قائمة": "xml.sax.default_parser_list",
    # === io ===
    "افتراضي_مخزن_مؤقت_حجم": "io.DEFAULT_BUFFER_SIZE",
    # === gzip ===
    "اقرأ_مخزن_مؤقت_حجم": "gzip.READ_BUFFER_SIZE",
    # === pickle ===
    "التالي_مخزن_مؤقت": "pickle.NEXT_BUFFER",
    # === os ===
    "المجلد_الأب": "os.path.pardir",
    "المجلد_الحالي": "os.path.curdir",
    "المسار_الافتراضي": "os.path.defpath",
    # === pickle ===
    "امتداد_1": "pickle.EXT1",
    "امتداد_2": "pickle.EXT2",
    "امتداد_4": "pickle.EXT4",
    # === io ===
    "انتقل_أنهِ": "io.SEEK_END",
    "انتقل_حالي": "io.SEEK_CUR",
    "انتقل_عيّن": "io.SEEK_SET",
    # === pickle ===
    "بايت_مصفوفة_8": "pickle.BYTEARRAY8",
    "بايتات_أنواع": "pickle.bytes_types",
    "بايتات_ثنائية": "pickle.BINBYTES",
    "بايتات_ثنائية_8": "pickle.BINBYTES8",
    "بايكن_أضف_ذيلياً": "pickle.APPEND",
    "بايكن_أضف_ذيلياً_2": "pickle.APPENDS",
    "بايكن_أضف_عناصر": "pickle.ADDITEMS",
    "بايكن_احصل": "pickle.GET",
    "بايكن_بروتوكول": "pickle.PROTO",
    "بايكن_توزيع_جدول": "pickle.dispatch_table",
    "بايكن_خطأ": "pickle.FALSE",
    "بايكن_صحيح": "pickle.TRUE",
    "بايكن_ضع": "pickle.PUT",
    "بايكن_قائمة": "pickle.LIST",
    "بايكن_قاموس": "pickle.DICT",
    "بايكن_كائن": "pickle.OBJ",
    "بايكن_لا_شيء": "pickle.NONE",
    "بايكن_نص": "pickle.STRING",
    # === locale ===
    "بديل_أرقام": "locale.ALT_DIGITS",
    # === zipfile ===
    "بنية_أنهِ_أرشيف": "zipfile.structEndArchive",
    "بنية_أنهِ_أرشيف64": "zipfile.structEndArchive64",
    "بنية_أنهِ_أرشيف64_محدّد": "zipfile.structEndArchive64Locator",
    "بنية_مركزي_مجلد": "zipfile.structCentralDir",
    "بنية_ملف_رأس": "zipfile.structFileHeader",
    # === unicodedata ===
    "بيانات_يونيكود_إصدار_2": "unicodedata.unidata_version",
    # === lzma ===
    "تحقق_SHA_256": "lzma.CHECK_SHA256",
    "تحقق_معرف_أقصى": "lzma.CHECK_ID_MAX",
    # === plistlib ===
    "ترويسة_القائمة": "plistlib.PLISTHEADER",
    # === locale ===
    "تعبير_لا": "locale.NOEXPR",
    "تعبير_نعم": "locale.YESEXPR",
    # === plistlib ===
    "تنسيق_XML": "plistlib.FMT_XML",
    # === tarfile ===
    "تنسيق_gnu_أنواع": "tarfile.GNU_TYPES",
    "تنسيق_gnu_سحري": "tarfile.GNU_MAGIC",
    "تنسيق_pax_اسم_حقول": "tarfile.PAX_NAME_FIELDS",
    "تنسيق_pax_حقول": "tarfile.PAX_FIELDS",
    "تنسيق_pax_عدد_حقول": "tarfile.PAX_NUMBER_FIELDS",
    # === plistlib ===
    "تنسيق_ثنائي": "plistlib.FMT_BINARY",
    # === stringprep ===
    "توحيد22_خواص": "stringprep.c22_specials",
    "توحيد6_عيّن": "stringprep.c6_set",
    "توحيد7_عيّن": "stringprep.c7_set",
    "توحيد8_عيّن": "stringprep.c8_set",
    "توحيد9_عيّن": "stringprep.c9_set",
    # === os ===
    "جهاز_العدم": "os.path.devnull",
    # === zipfile ===
    "حجم_أنهِ_مئوي_مجلد": "zipfile.sizeEndCentDir",
    # === tarfile ===
    "حجم_السجل": "tarfile.RECORDSIZE",
    "حجم_الكتلة": "tarfile.BLOCKSIZE",
    # === filecmp ===
    "حجم_المخزن": "filecmp.BUFSIZE",
    # === zipfile ===
    "حجم_ملف_رأس": "zipfile.sizeFileHeader",
    # === locale ===
    "حرف_أقصى": "locale.CHAR_MAX",
    "حرف_الأساس": "locale.RADIXCHAR",
    # === pickle ===
    "خزّن_النتيجة": "pickle.MEMOIZE",
    "خطأ_جديد": "pickle.NEWFALSE",
    # === lzma ===
    "رشّح_ضغط_lzma_1": "lzma.FILTER_LZMA1",
    "رشّح_ضغط_lzma_2": "lzma.FILTER_LZMA2",
    # === array ===
    "رموز_النوع": "array.typecodes",
    # === xml ===
    "سمة_صنف_XML_نص": "xml.sax.handler.property_xml_string",
    "سمة_صنف_إعلان_معالج": "xml.sax.handler.property_declaration_handler",
    "سمة_صنف_تدويل_قاموس": "xml.sax.handler.property_interning_dict",
    "سمة_صنف_ترميز": "xml.sax.handler.property_encoding",
    "سمة_صنف_معجمي_معالج": "xml.sax.handler.property_lexical_handler",
    "سمة_صنف_نموذج_كائن_عُقدة": "xml.sax.handler.property_dom_node",
    # === tarfile ===
    "سولاريس_نوع_القرص": "tarfile.SOLARIS_XHDTYPE",
    # === pickle ===
    "شامل": "pickle.GLOBAL",
    # === locale ===
    "شهر_1": "locale.MON_1",
    "شهر_10": "locale.MON_10",
    "شهر_11": "locale.MON_11",
    "شهر_12": "locale.MON_12",
    "شهر_2": "locale.MON_2",
    "شهر_3": "locale.MON_3",
    "شهر_4": "locale.MON_4",
    "شهر_5": "locale.MON_5",
    "شهر_6": "locale.MON_6",
    "شهر_7": "locale.MON_7",
    "شهر_8": "locale.MON_8",
    "شهر_9": "locale.MON_9",
    "شهر_مختصر_1": "locale.ABMON_1",
    "شهر_مختصر_10": "locale.ABMON_10",
    "شهر_مختصر_11": "locale.ABMON_11",
    "شهر_مختصر_12": "locale.ABMON_12",
    "شهر_مختصر_2": "locale.ABMON_2",
    "شهر_مختصر_3": "locale.ABMON_3",
    "شهر_مختصر_4": "locale.ABMON_4",
    "شهر_مختصر_5": "locale.ABMON_5",
    "شهر_مختصر_6": "locale.ABMON_6",
    "شهر_مختصر_7": "locale.ABMON_7",
    "شهر_مختصر_8": "locale.ABMON_8",
    "شهر_مختصر_9": "locale.ABMON_9",
    "صباحاً_نص": "locale.AM_STR",
    # === pickle ===
    "صحيح_ثنائي": "pickle.BININT",
    "صحيح_ثنائي_1": "pickle.BININT1",
    "صحيح_ثنائي_2": "pickle.BININT2",
    "صحيح_جديد": "pickle.NEWTRUE",
    "صف": "pickle.TUPLE",
    "صف_1": "pickle.TUPLE1",
    "صف_2": "pickle.TUPLE2",
    "صف_3": "pickle.TUPLE3",
    # === zipfile ===
    "ضاغط_أسماء": "zipfile.compressor_names",
    "ضغط_bzip2": "zipfile.ZIP_BZIP2",
    "ضغط_bzip_2_إصدار": "zipfile.BZIP2_VERSION",
    # === gzip ===
    "ضغط_gzip_اقرأ": "gzip.READ",
    "ضغط_gzip_اكتب": "gzip.WRITE",
    # === zipfile ===
    "ضغط_lzma": "zipfile.ZIP_LZMA",
    "ضغط_lzma_إصدار": "zipfile.LZMA_VERSION",
    # === tarfile ===
    "طول_بادئة": "tarfile.LENGTH_PREFIX",
    "طول_وصلة": "tarfile.LENGTH_LINK",
    # === pickle ===
    "طويل": "pickle.LONG",
    "طويل_1": "pickle.LONG1",
    "طويل_4": "pickle.LONG4",
    "طويل_أدخل_ثنائياً": "pickle.LONG_BINPUT",
    "طويل_احصل_ثنائياً": "pickle.LONG_BINGET",
    "عائم": "pickle.FLOAT",
    "عائم_ثنائي": "pickle.BINFLOAT",
    # === tarfile ===
    "عادي_أنواع": "tarfile.REGULAR_TYPES",
    # === pickle ===
    "عدد_صحيح": "pickle.INT",
    # === locale ===
    "عصر": "locale.ERA",
    "عصر_D_T_تنسيق": "locale.ERA_D_T_FMT",
    "عصر_D_تنسيق": "locale.ERA_D_FMT",
    "عصر_T_تنسيق": "locale.ERA_T_FMT",
    # === pickle ===
    "علامة": "pickle.MARK",
    # === codecs ===
    "علامة_الترتيب": "codecs.BOM",
    "علامة_الترتيب_32_B": "codecs.BOM32_BE",
    "علامة_الترتيب_64_B": "codecs.BOM64_BE",
    "علامة_الترتيب_64_LE": "codecs.BOM64_LE",
    "علامة_الترتيب_UTF_8": "codecs.BOM_UTF8",
    # === pickle ===
    "عيّن_عناصر": "pickle.SETITEMS",
    "عيّن_عنصراً": "pickle.SETITEM",
    # === xml ===
    "غير_صالح_تعديل_خطأ": "xml.dom.INVALID_MODIFICATION_ERR",
    "غير_صالح_حالة_خطأ": "xml.dom.INVALID_STATE_ERR",
    # === pickle ===
    "فارغ_صف": "pickle.EMPTY_TUPLE",
    "فارغ_عيّن": "pickle.EMPTY_SET",
    "فارغ_قائمة": "pickle.EMPTY_LIST",
    "فارغ_قاموس": "pickle.EMPTY_DICT",
    # === locale ===
    "فاصل_الآلاف": "locale.THOUSEP",
    # === os ===
    "فاصل_المسارات": "os.path.pathsep",
    "فاصل_بديل": "os.path.altsep",
    # === plistlib ===
    "قائمة_نسّق_تنسيق_XML": "plistlib.PlistFormat.FMT_XML",
    "قائمة_نسّق_تنسيق_ثنائي": "plistlib.PlistFormat.FMT_BINARY",
    # === xml ===
    "قابل_للتجاهل_مسافة_بيضاء": "xml.dom.pulldom.IGNORABLE_WHITESPACE",
    # === pickle ===
    "قصير_بايتات_ثنائية": "pickle.SHORT_BINBYTES",
    "قصير_نص_ثنائي": "pickle.SHORT_BINSTRING",
    "قصير_يونيكود_ثنائي": "pickle.SHORT_BINUNICODE",
    "كائن_جديد": "pickle.NEWOBJ",
    "كائن_جديد_EX": "pickle.NEWOBJ_EX",
    "كرّر": "pickle.DUP",
    # === xml ===
    "كل_خصائص": "xml.sax.handler.all_properties",
    "كل_مزايا": "xml.sax.handler.all_features",
    # === pickle ===
    "للقراءة_فقط_مخزن_مؤقت": "pickle.READONLY_BUFFER",
    "متوافق_تنسيقات": "pickle.compatible_formats",
    "مجموعة_مجمّدة": "pickle.FROZENSET",
    # === locale ===
    "محلي_اسم_مستعار": "locale.locale_alias",
    "محلي_ترميز_اسم_مستعار": "locale.locale_encoding_alias",
    # === tarfile ===
    "مدعوم_أنواع": "tarfile.SUPPORTED_TYPES",
    # === xml ===
    "مزايا": "xml.parsers.expat.features",
    # === locale ===
    "مساءً_نص": "locale.PM_STR",
    # === pickle ===
    "معرف_دائم": "pickle.PERSID",
    "معرف_دائم_ثنائي": "pickle.BINPERSID",
    # === unicodedata ===
    "معيار_يونيكود_3_2_0": "unicodedata.ucd_3_2_0",
    # === pickle ===
    "مكدس_شامل": "pickle.STACK_GLOBAL",
    # === stat ===
    "ملف_سمة_أرشيف": "stat.FILE_ATTRIBUTE_ARCHIVE",
    "ملف_سمة_إعادة_تحليل_نقطة": "stat.FILE_ATTRIBUTE_REPARSE_POINT",
    "ملف_سمة_افتراضي": "stat.FILE_ATTRIBUTE_VIRTUAL",
    "ملف_سمة_بلا_امسح_الزيادة_بيانات": "stat.FILE_ATTRIBUTE_NO_SCRUB_DATA",
    "ملف_سمة_جهاز": "stat.FILE_ATTRIBUTE_DEVICE",
    "ملف_سمة_دون_اتصال": "stat.FILE_ATTRIBUTE_OFFLINE",
    "ملف_سمة_سلامة_تدفق": "stat.FILE_ATTRIBUTE_INTEGRITY_STREAM",
    "ملف_سمة_عادي": "stat.FILE_ATTRIBUTE_NORMAL",
    "ملف_سمة_لا_محتوى_مُفهرس": "stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED",
    "ملف_سمة_مؤقت": "stat.FILE_ATTRIBUTE_TEMPORARY",
    "ملف_سمة_متفرّق_ملف": "stat.FILE_ATTRIBUTE_SPARSE_FILE",
    "ملف_سمة_مجلد": "stat.FILE_ATTRIBUTE_DIRECTORY",
    "ملف_سمة_مشفّر": "stat.FILE_ATTRIBUTE_ENCRYPTED",
    "ملف_سمة_مضغوط": "stat.FILE_ATTRIBUTE_COMPRESSED",
    "ملف_سمة_نظام": "stat.FILE_ATTRIBUTE_SYSTEM",
    # === tarfile ===
    "ملف_شريط_إصدار": "tarfile.version",
    "ملف_شريط_ترميز": "tarfile.ENCODING",
    "ملف_شريط_نوع_المحتوى": "tarfile.CONTTYPE",
    # === xml ===
    "ميزة_تحقق": "xml.sax.handler.feature_validation",
    "ميزة_خارجي_GES": "xml.sax.handler.feature_external_ges",
    "ميزة_خارجي_وحدات_أساسية": "xml.sax.handler.feature_external_pes",
    "ميزة_نص_تدويل": "xml.sax.handler.feature_string_interning",
    "ميزة_نطاق_اسم_بادئات": "xml.sax.handler.feature_namespace_prefixes",
    "ميزة_نطاقات_أسماء": "xml.sax.handler.feature_namespaces",
    # === lzma ===
    "مُعدّ_مسبقاً_أقصى": "lzma.PRESET_EXTREME",
    # === pickle ===
    "نسخة": "pickle.INST",
    "نسّق_إصدار": "pickle.format_version",
    # === stat ===
    "نص_EN_FMT": "stat.S_ENFMT",
    "نص_IRWXG": "stat.S_IRWXG",
    "نص_IRWXU": "stat.S_IRWXU",
    # === zipfile ===
    "نص_أنهِ_أرشيف": "zipfile.stringEndArchive",
    "نص_أنهِ_أرشيف64": "zipfile.stringEndArchive64",
    "نص_أنهِ_أرشيف64_محدّد": "zipfile.stringEndArchive64Locator",
    # === xml ===
    "نص_أنواع": "xml.dom.minidom.StringTypes",
    # === locale ===
    "نص_العملة": "locale.CRNCYSTR",
    # === pickle ===
    "نص_ثنائي": "pickle.BINSTRING",
    # === zipfile ===
    "نص_مركزي_مجلد": "zipfile.stringCentralDir",
    "نص_ملف_رأس": "zipfile.stringFileHeader",
    # === stat ===
    "نص_نوع_أنبوب": "stat.S_IFIFO",
    "نص_نوع_جهاز_حرفي": "stat.S_IFCHR",
    "نص_نوع_جهاز_كتلي": "stat.S_IFBLK",
    "نص_نوع_رابط_صلب": "stat.S_IFLNK",
    "نص_نوع_مجلد": "stat.S_IFDIR",
    "نص_نوع_مقبس": "stat.S_IFSOCK",
    "نص_نوع_ملف_عادي": "stat.S_IFREG",
    "نص_هو_معرف_المجموعة": "stat.S_ISGID",
    "نص_هو_معرف_المستخدم": "stat.S_ISUID",
    "نص_هو_ناقل": "stat.S_ISVTX",
    # === os ===
    "نظام_تشغيل_مسار_فاصل": "os.path.sep",
    # === tarfile ===
    "نوع_OpenGL": "tarfile.XGLTYPE",
    "نوع_gnu_رابط_طويل": "tarfile.GNUTYPE_LONGLINK",
    "نوع_gnu_طويل_اسم": "tarfile.GNUTYPE_LONGNAME",
    "نوع_gnu_متفرّق": "tarfile.GNUTYPE_SPARSE",
    "نوع_الأنبوب": "tarfile.FIFOTYPE",
    "نوع_الرابط": "tarfile.LNKTYPE",
    "نوع_الرابط_الرمزي": "tarfile.SYMTYPE",
    "نوع_السجل": "tarfile.AREGTYPE",
    "نوع_القرص": "tarfile.XHDTYPE",
    "نوع_الكتلة": "tarfile.BLKTYPE",
    "نوع_المجلد": "tarfile.DIRTYPE",
    "نوع_المحرف": "tarfile.CHRTYPE",
    "نوع_الملف": "tarfile.REGTYPE",
    # === weakref ===
    "وكيل_أنواع": "weakref.ProxyTypes",
    # === locale ===
    "ويندوز_محلي": "locale.windows_locale",
    # === os ===
    "يدعم_يونيكود_أسماء_الملفات": "os.path.supports_unicode_filenames",
    # === locale ===
    "يوم_1": "locale.DAY_1",
    "يوم_2": "locale.DAY_2",
    "يوم_3": "locale.DAY_3",
    "يوم_4": "locale.DAY_4",
    "يوم_5": "locale.DAY_5",
    "يوم_6": "locale.DAY_6",
    "يوم_7": "locale.DAY_7",
    "يوم_مختصر_1": "locale.ABDAY_1",
    "يوم_مختصر_2": "locale.ABDAY_2",
    "يوم_مختصر_3": "locale.ABDAY_3",
    "يوم_مختصر_4": "locale.ABDAY_4",
    "يوم_مختصر_5": "locale.ABDAY_5",
    "يوم_مختصر_6": "locale.ABDAY_6",
    "يوم_مختصر_7": "locale.ABDAY_7",
    # === pickle ===
    "يونيكود": "pickle.UNICODE",
    "يونيكود_ثنائي": "pickle.BINUNICODE",
    "يونيكود_ثنائي_8": "pickle.BINUNICODE8",
}


# --- الاسم الواحد يمرّ مرة واحدة ---
_DF_TOKEN = re.compile(
    r"(?P<dot>\.)?"
    r"(?P<word>(?!\d)[\w\u064B-\u065F\u0670]+)"
    r"(?P<open>\s*\()?"
)

USER_NAMES = set()


def _df_replace(match):
    dot = match.group("dot")
    word = match.group("word")
    open_paren = match.group("open")

    if word in USER_NAMES:
        return match.group(0)

    if dot:
        if open_paren and word in DF_METHODS:
            return "." + DF_METHODS[word] + open_paren
        if word in DF_PROPS:
            return "." + DF_PROPS[word]
        return match.group(0)

    if word in DF_CONSTS:
        return DF_CONSTS[word]
    if word in DF_FUNCS:
        return DF_FUNCS[word] + (open_paren or "")
    return match.group(0)


def DF_SUBSTITUTE(text):
    """يترجم كلمات البيانات والملفات في نص واحد ويُرجع المترجم."""
    if not text:
        return text
    return _DF_TOKEN.sub(_df_replace, text)

IMPORT_NAME = "os"
IMPORT_MODULES = ["io", "codecs", "stat", "filecmp", "fileinput", "glob", "fnmatch", "os.path", "zipfile", "tarfile", "gzip", "bz2", "lzma", "pickle", "shelve", "dbm", "dbm.dumb", "marshal", "plistlib", "array", "struct", "bisect", "heapq", "queue", "types", "copy", "copyreg", "weakref", "numbers", "abc", "contextlib", "contextvars", "graphlib", "xml.dom", "xml.dom.minidom", "xml.dom.pulldom", "xml.sax", "xml.sax.handler", "xml.sax.saxutils", "xml.sax.xmlreader", "xml.etree.ElementTree", "xml.parsers.expat", "unicodedata", "difflib", "stringprep", "reprlib", "gettext", "locale"]
IMPORT_CHECK = r"(?:io|codecs|stat|filecmp|fileinput|glob|fnmatch|os\.path|zipfile|tarfile|gzip|bz2|lzma|pickle|shelve|dbm|dbm\.dumb|marshal|plistlib|array|struct|bisect|heapq|queue|types|copy|copyreg|weakref|numbers|abc|contextlib|contextvars|graphlib|xml\.dom|xml\.dom\.minidom|xml\.dom\.pulldom|xml\.sax|xml\.sax\.handler|xml\.sax\.saxutils|xml\.sax\.xmlreader|xml\.etree\.ElementTree|xml\.parsers\.expat|unicodedata|difflib|stringprep|reprlib|gettext|locale)\."
IMPORT_STATEMENT = "import io, codecs, stat, filecmp, fileinput, glob, fnmatch, os.path, zipfile, tarfile, gzip, bz2, lzma, pickle, shelve, dbm, dbm.dumb, marshal, plistlib, array, struct, bisect, heapq, queue, types, copy, copyreg, weakref, numbers, abc, contextlib, contextvars, graphlib, xml.dom, xml.dom.minidom, xml.dom.pulldom, xml.sax, xml.sax.handler, xml.sax.saxutils, xml.sax.xmlreader, xml.etree.ElementTree, xml.parsers.expat, unicodedata, difflib, stringprep, reprlib, gettext, locale"


DF_HELP = [
    "# datafiles — البيانات والملفات (io, zipfile, pickle, xml, os.path)",
    "اربط_مسارين(أ, ب)              - ربط مسارين",
    "حجم_ملف(مسار)                  - حجم ملف",
    "بحث_نمطي(نمط)                  - بحث عن ملفات",
    "ملف_مضغوط(مسار) / اعمل_أرشيفاً - ضغط zip",
    "أفرغ_بايكن(كائن) / حمّل_بايكن   - تسلسل pickle",
    "عنصر(اسم, صنف)                 - بناء عنصر XML",
    "حلل_شجرة(ملف)                  - تحليل XML",
    "مصفوفة(نوع) / احزم_بنية        - array / struct",
    "طابور() / كتلة_مصفوفات_ضعيفة   - queue / weakref",
]

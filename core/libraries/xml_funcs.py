"""
APL - XML Library Functions
Transpiles Arabic keywords to Python's xml.etree.ElementTree module.

Arabic keywords are grouped in four maps, exactly like every other APL library:

    XML_FUNCS      -> module level helpers  (اقرأ_إكس_إم_إل(مسار))
    XML_METHODS    -> methods called after a dot (الجذر.ابحث_عنصر("صنف"))
    XML_PROPS      -> element properties, no parentheses (العنصر.نص_العنصر)
    XML_CONSTANTS  -> bare constants (حدث_نهاية)

Runtime helpers (``_apl_xml_*``) live in ``core/apl_runner/main.py`` inside the
``_RUNTIME`` prologue, and every helper imports ``xml.etree.ElementTree``
lazily so a program that never touches XML pays nothing at startup.

NOTE: ``ضع_خاصية`` already belongs to the dataclasses library, so this library
spells the attribute setter ``عين_خاصية``. ``نسخ`` is a method alias in the
core language, and Element objects have no ``.copy``, so duplication goes
through the standalone helper ``انسخ_العنصر`` / ``نسخ_العنصر``.
"""

XML_FUNCS = {
    # === القراءة والتحليل (Parsing) ===
    "اقرأ_إكس_إم_إل": "_apl_xml_parse",
    "إكس_إم_إل_من_ملف": "_apl_xml_parse",
    "إكس_إم_إل_من_نص": "_apl_xml_fromstring",
    "من_نص_إكس_إم_إل": "_apl_xml_fromstring",
    "إكس_إم_إل_من_أسطر": "_apl_xml_fromstringlist",
    "اقرأ_إكس_إم_إل_آمن": "_apl_xml_safe_parse",
    "تحقق_من_عنصر": "_apl_xml_check",
    "خطأ_التحقق": "_apl_xml_check_message",

    # الصيغة الحرة (بدون نقطة) لدوال الخصائص: عين_خاصية(عنصر, اسم, قيمة)
    "اقرأ_خاصية": "_apl_xml_get",
    "عين_خاصية": "_apl_xml_set",
    "تضيف": "_apl_xml_append",
    "تحذف": "_apl_xml_remove",
    "تنسخ": "_apl_xml_copy",
    "تجد": "_apl_xml_find",
    "تجد_الكل": "_apl_xml_findall",
    "تجد_نص": "_apl_xml_findtext",
    "تفرغ": "_apl_xml_clear",
    "أعد_تسمية": "_apl_xml_set_tag",
    "عين_وسم": "_apl_xml_set_tag",
    "عين_خصائص": "_apl_xml_set_attrib",
    "غذِّ_نص_العنصر": "_apl_xml_set_text",
    "غذِّ_ذيل_العنصر": "_apl_xml_set_tail",

    # === الكتابة والتحويل (Serialization) ===
    "إكس_إم_إل_إلى_نص": "_apl_xml_tostring",
    "إلى_نص_إكس_إم_إل": "_apl_xml_tostring",
    "إكس_إم_إل_إلى_نص_خام": "_apl_xml_tostring_raw",
    "إكس_إم_إل_إلى_أسطر": "_apl_xml_tolist",
    "إكس_إم_إل_قياسي": "_apl_xml_canonicalize",
    "نسّق_إكس_إم_إل": "_apl_xml_pretty",
    "رتّب_الشجرة": "_apl_xml_indent",
    "أزل_المسافات": "_apl_xml_strip",
    "احفظ_إكس_إم_إل": "_apl_xml_save",
    "اطبع_إكس_إم_إل": "_apl_xml_dump",

    # === بناء الشجرة (Building) ===
    "عنصر_جديد": "_apl_xml_element",
    "عنصر": "_apl_xml_element",
    "عنصر_فرعي_جديد": "_apl_xml_subelement",
    "شجرة_إكس_إم_إل": "_apl_xml_tree",
    "شجرة": "_apl_xml_tree",
    "باني_الشجرة": "_apl_xml_treebuilder",
    "محلل_سحب": "_apl_xml_pull_parser",

    # === الفحص والتفتيش (Inspection) ===
    "عد_العناصر": "_apl_xml_count",
    "أبناء_مباشرون": "_apl_xml_children",
    "نص_كامل": "_apl_xml_text",
    "احسب_المسار": "_apl_xml_path",
    "عنصر_بالمعرف": "_apl_xml_by_id",
    "انسخ_العنصر": "_apl_xml_copy",
    "نسخ_العنصر": "_apl_xml_copy",

    # === أحداث العنصر (Element Events) ===
    # "ابدأ" محجوز لـ flask/fastapi/threading، لذا نستخدم "ابدأ_عنصر"
    "ابدأ_عنصر": "_apl_xml_event_start",
    "أنهِ": "_apl_xml_event_end",
    "أنهِ_عنصر": "_apl_xml_event_end",

    # === مساحات الأسماء (Namespaces) ===
    "مساحة_أسماء": "_apl_xml_namespace",
    "سجل_مساحة_أسماء": "_apl_xml_register_namespace",
}

XML_PATTERN = (
    r"(?<![\w.\u0600-\u06FF])("
    + "|".join(sorted(XML_FUNCS.keys(), key=len, reverse=True))
    + r")\s*\("
)

XML_METHODS = {
    # === البحث (Search) ===
    "ابحث_عنصر": "find",
    "ابحث_الكل": "findall",
    "ابحث_نص": "findtext",
    "كرر_بحث": "iterfind",
    "ابحث_شجرة": "find",
    "ابحث_كل_شجرة": "findall",
    "ابحث_نص_شجرة": "findtext",
    "جذر_الشجرة": "getroot",
    "كرر_الشجرة": "iter",
    "اكتب_الشجرة": "write",

    # === التكرار (Iteration) ===
    "كرر": "iter",
    "كرر_نصوص": "itertext",

    # === الخصائص (Attributes) ===
    "اقرأ_خاصية": "get",
    "عين_خاصية": "set",
    "أسماء_الخصائص": "keys",
    "عناصر_الخصائص": "items",

    # === التعديل (Mutation) ===
    "أضف_عنصر": "append",
    "أضف_عناصر": "extend",
    "أدرج_عنصر": "insert",
    "احذف_عنصر": "remove",
    "أفرغ_العنصر": "clear",
    "أنشئ_عنصر": "makeelement",
    # ملاحظة: indent و strip ليستا دالتين على العنصر في ElementTree،
    # لذا تستخدم الصيغة الحرة: رتّب_الشجرة(عنصر) و أزل_المسافات(عنصر)

    # === الباني (TreeBuilder) ===
    "ابدأ_وسم": "start",
    "أنهِ_وسم": "end",
    "غذِّ": "data",
    "غذِّ_نص": "data",
    "غذِّ_نص_العنصر": "data",
    "غذِّ_العنصر": "data",
    "تعليق_باني": "comment",
    "تعليمات_باني": "pi",

    # === المحلل التدريجي (XMLPullParser) ===
    "غذِّ_المحلل": "feed",
    "غذِّ_شجرة": "feed",
    "اقرأ_الأحداث": "read_events",
    "أحداث_المحلل": "read_events",
    "أغلق_المحلل": "close",
    "أغلق_الباني": "close",
    "أغلق_الشجرة": "close",

    # === مكررات (ElementTree) ===
    "كرر_شجرة": "iter",
    "كرر_بحث_شجرة": "iterfind",
    "اقرأ_نص_شجرة": "findtext",
}

XML_METHOD_PATTERN = (
    r"\.("
    + "|".join(sorted(XML_METHODS.keys(), key=len, reverse=True))
    + r")\s*\("
)

XML_PROPS = {
    "اسم_العنصر": "tag",
    "نص_العنصر": "text",
    "ذيل_العنصر": "tail",
    "خصائص_العنصر": "attrib",
}

XML_PROP_PATTERN = (
    r"\.("
    + "|".join(sorted(XML_PROPS.keys(), key=len, reverse=True))
    + r")(?![\w\u0600-\u06FF])"
)

# Event names used by محلل_سحب -> ET.XMLPullParser(events=[...])
XML_CONSTANTS = {
    "حدث_بداية": '"start"',
    "حدث_نهاية": '"end"',
    "حدث_بداية_مساحة": '"start-ns"',
    "حدث_نهاية_مساحة": '"end-ns"',
}

XML_CONSTANT_PATTERN = (
    r"(?<![\w.\u0600-\u06FF])("
    + "|".join(sorted(XML_CONSTANTS.keys(), key=len, reverse=True))
    + r")(?![\w\u0600-\u06FF])"
)

# Keyword arguments translated before "=" (see inline_replacer)
XML_KWARGS = {
    "عناصر_فارغة_قصيرة": "short_empty_elements",
    "إعادة_كتابة_البادئات": "rewrite_prefixes",
    "إزالة_المسافات_إكس_إم_إل": "strip_text",
    "أحداث": "events",
    "مساحة_افتراضية": "default_namespace",
    "بادئات_الخصائص_المؤهلة": "attribute_prefixes",
    "أسماء_مؤهلة_الوسوم": "qname_aware_tags",
    "أسماء_مؤهلة_الخصائص": "qname_aware_attrs",
    "استبعاد_الخصائص": "exclude_attrs",
    "استبعاد_الوسوم": "exclude_tags",
}

# Help text for CLI
XML_HELP = [
    "# xml — قراءة وبناء وتعديل ملفات XML",
    "اقرأ_إكس_إم_إل(مسار)          - تحليل ملف -> كائن شجرة (استخدم .جذر_الشجرة())",
    "إكس_إم_إل_من_نص(نص)            - تحليل نص -> العنصر الجذر",
    "إكس_إم_إل_إلى_نص(عنصر)         - تحويل الشجرة إلى نص منسّق",
    "احفظ_إكس_إم_إل(عنصر, مسار)     - كتابة الشجرة إلى ملف",
    "عنصر_جديد(وسم, خصائص)          - إنشاء عنصر",
    "عنصر_فرعي_جديد(أب, وسم)        - إضافة عنصر فرعي وإرجاعه",
    "# البحث والقراءة",
    "  عنصر.ابحث_عنصر(مسار)        - أول عنصر مطابق",
    "  عنصر.ابحث_الكل(مسار)        - كل العناصر المطابقة",
    "  عنصر.ابحث_نص(مسار)          - نص أول عنصر مطابق",
    "  عنصر.كرر(وسم)               - المرور على العناصر",
    "  عنصر.اقرأ_خاصية(اسم)        - قيمة خاصية",
    "# التعديل",
    "  عنصر.عين_خاصية(اسم, قيمة)   - تعيين خاصية",
    "  عنصر.أضف_عنصر(ابن)          - إضافة ابن",
    "  عنصر.احذف_عنصر(ابن)         - حذف ابن",
    "# الخصائص",
    "  عنصر.اسم_العنصر، عنصر.نص_العنصر، عنصر.ذيل_العنصر، عنصر.خصائص_العنصر",
    "# أدوات",
    "عد_العناصر(عنصر, وسم)          - عدّ العناصر",
    "نص_كامل(عنصر)                  - كل النصوص مدموجة",
    "احسب_المسار(الجذر, عنصر)       - مسار العنصر داخل الشجرة",
    "تحقق_من_عنصر(نص)               - هل الصياغة صحيحة؟",
]

# Import detection: every runtime helper imports xml.etree.ElementTree inside
# its own body (lazily), so no `import` line is injected into generated code —
# a program that never touches XML never imports the module at all.
IMPORT_NAME = "xml.etree.ElementTree"
IMPORT_CHECK = r"_apl_xml_"
IMPORT_STATEMENT = "import xml.etree.ElementTree as ET"

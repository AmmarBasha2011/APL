"""
APL - Archive & Compression Library
Transpiles Arabic keywords to Python's archive stack:

    zipfile  -> ملفات ZIP         (القراءة، الكتابة، الإضافة، الاستخراج)
    tarfile  -> ملفات TAR         (gz / bz2 / xz)
    gzip     -> ضغط سريع          (.gz)
    bz2      -> ضغط قوي           (.bz2)
    lzma     -> ضغط فائق          (.xz / .lzma)

Arabic keywords are grouped in four maps, exactly like every other APL library:

    ARCHIVE_FUNCS      -> module level helpers  (افتح_أرشيف("ملف.zip"))
    ARCHIVE_METHODS    -> methods after a dot   (أرشيف.اقرأ_عضو("تقرير.txt"))
    ARCHIVE_PROPS      -> properties, no parens (عضو.حجم_العضو)
    ARCHIVE_CONSTANTS  -> bare constants        (ضغط_افتراضي)

Runtime helpers (``_apl_zip_*`` / ``_apl_tar_*`` / ``_apl_gz_*``) live in
``core/runner/main.py`` inside the ``_RUNTIME`` prologue. Every helper
imports its module inside its own body, so a program that never touches an
archive imports nothing extra at startup.

NOTE: ``ضغط`` belongs to ``itertools`` (``itertools.compress``) and ``مستوى``
belongs to ``logging``, so this library never uses those bare names — it uses
``درجة_الضغط`` for ``compresslevel`` and ``ضغط_افتراضي`` for the ZIP method.
``هو_مجلد`` belongs to ``os``, so zip members use ``عضو_مجلد``.
"""

ARCHIVE_FUNCS = {
    # === فتح الأرشيف (Opening) ===
    "افتح_أرشيف": "_apl_zip_open",
    "أرشيف_جديد": "_apl_zip_open",
    "أرشيف_للقراءة": "_apl_zip_read_open",
    "افتح_أي_أرشيف": "_apl_archive_open",

    # === الفحص والسرد (Inspect / list) ===
    "افحص_أرشيف": "_apl_zip_is",
    "نوع_الأرشيف": "_apl_archive_detect",
    "قائمة_الأرشيف": "_apl_zip_names",
    "أسماء_الأرشيف": "_apl_zip_names",
    "عدد_الأعضاء": "_apl_zip_count",
    "داخل_الأرشيف": "_apl_zip_contains",
    "بيانات_عضو": "_apl_zip_info",
    "ملخص_الأرشيف": "_apl_zip_summary",
    "عرض_الأرشيف": "_apl_zip_print",
    "بيانات_الأرشيف": "_apl_zip_stats",
    "حجم_الأرشيف": "_apl_file_size",
    "حجم_غير_مضغوط": "_apl_zip_uncompressed",
    "حجم_بشري": "_apl_size_human",
    "نسبة_الضغط": "_apl_compression_ratio",

    # === الإنشاء والتعديل (Create / edit) ===
    "أنشئ_أرشيف": "_apl_zip_create",
    "أنشئ_أرشيف_من_مجلد": "_apl_zip_create",
    "أضف_للأرشيف": "_apl_zip_add",
    "احذف_من_الأرشيف": "_apl_zip_remove",
    "استخرج_الأرشيف": "_apl_zip_extract",

    # === قراءة محتوى الأعضاء (Read members) ===
    "نص_العضو": "_apl_zip_read",
    "اقرأ_من_الأرشيف": "_apl_zip_read",
    "بايتات_العضو": "_apl_zip_read_bytes",
    "معلومات_عضو": "_apl_zip_info",

    # === أرشيف TAR ===
    "افتح_طر": "_apl_tar_open",
    "أرشيف_طر": "_apl_tar_open",
    "افحص_طر": "_apl_tar_is",
    "أسماء_الطر": "_apl_tar_names",
    "أعضاء_الطر": "_apl_tar_members",
    "بيانات_عضو_طر": "_apl_tar_info",
    "أنشئ_طر": "_apl_tar_create",
    "أضف_للطر": "_apl_tar_add",
    "استخرج_طر": "_apl_tar_extract",
    "نص_من_الطر": "_apl_tar_read",

    # === الضغط المباشر للنصوص (gzip / bz2 / lzma) ===
    "ضغط_نص": "_apl_gzip_compress",
    "فك_ضغط_نص": "_apl_gzip_decompress",
    "ضغط_سريع": "_apl_gzip_compress",
    "فك_ضغط_سريع": "_apl_gzip_decompress",
    "ضغط_قوي": "_apl_bz2_compress",
    "فك_ضغط_قوي": "_apl_bz2_decompress",
    "ضغط_فائق": "_apl_lzma_compress",
    "فك_ضغط_فائق": "_apl_lzma_decompress",
    "ضغط_gz": "_apl_gzip_compress",
    "فك_ضغط_gz": "_apl_gzip_decompress",
    "ضغط_bz2": "_apl_bz2_compress",
    "فك_ضغط_bz2": "_apl_bz2_decompress",
    "ضغط_xz": "_apl_lzma_compress",
    "فك_ضغط_xz": "_apl_lzma_decompress",

    # === ملفات مضغوطة على القرص (single-file archives) ===
    "اقرأ_مضغوط": "_apl_gz_read_file",
    "اكتب_مضغوط": "_apl_gz_write_file",
    "ضغط_ملف": "_apl_gz_file",
    "فك_ملف_مضغوط": "_apl_gz_unfile",
    "اقرأ_bz2": "_apl_bz2_read_file",
    "اكتب_bz2": "_apl_bz2_write_file",
    "اقرأ_xz": "_apl_lzma_read_file",
    "اكتب_xz": "_apl_lzma_write_file",
}

ARCHIVE_PATTERN = (
    r"(?<![\w.\u0600-\u06FF])("
    + "|".join(sorted(ARCHIVE_FUNCS.keys(), key=len, reverse=True))
    + r")\s*\("
)

ARCHIVE_METHODS = {
    # === ZipFile ===
    "اقرأ_عضو": "read",
    "اكتب_عضو": "writestr",
    "افتح_عضو": "open",
    "أسماء_الأعضاء": "namelist",
    "سرد_الأعضاء": "infolist",
    "معلومات_عضو": "getinfo",
    "استخرج_عضو": "extract",
    "استخرج_الكل": "extractall",
    "أغلق_الأرشيف": "close",
    "عين_كلمة_السر": "setpassword",
    "افحص_السلامة": "testzip",

    # === TarFile ===
    "أسماء_أعضاء_الطر": "getnames",
    "أعضاء_الطر_كامل": "getmembers",
    "معلومات_عضو_طر": "getmember",
    "افتح_عضو_طر": "extractfile",
    "استخرج_عضو_طر": "extract",
    "استخرج_طر_الكل": "extractall",
    "أضف_ملف_للطر": "add",
    "أغلق_طر": "close",
    "سرد_طر": "list",
}

ARCHIVE_METHOD_PATTERN = (
    r"\.("
    + "|".join(sorted(ARCHIVE_METHODS.keys(), key=len, reverse=True))
    + r")\s*\("
)

ARCHIVE_PROPS = {
    # === ZipInfo ===
    "اسم_العضو": "filename",
    "حجم_العضو": "file_size",
    "حجم_مضغوط": "compress_size",
    "تاريخ_العضو": "date_time",
    "طريقة_الضغط": "compress_type",
    "تعليق_الأرشيف": "comment",
    # === TarInfo ===
    "اسم_الطر": "name",
    "مسار_الطر": "path",
    "حجم_الطر": "size",
    "وقت_الطر": "mtime",
    "نمط_الطر": "mode",
    "نوع_الطر": "type",
}

ARCHIVE_PROP_PATTERN = (
    r"\.("
    + "|".join(sorted(ARCHIVE_PROPS.keys(), key=len, reverse=True))
    + r")(?![\w\u0600-\u06FF])"
)

# Bare constants. ZIP_* are integers, while tar/gzip modes are Python string literals.
ARCHIVE_CONSTANTS = {
    "بدون_ضغط": "zipfile.ZIP_STORED",
    "ضغط_افتراضي": "zipfile.ZIP_DEFLATED",
    "ضغط_أرشيف_bz2": "zipfile.ZIP_BZIP2",
    "ضغط_أرشيف_lzma": "zipfile.ZIP_LZMA",
    "طر_بدون_ضغط": '"w"',
    "طر_مع_gz": '"w:gz"',
    "طر_مع_bz2": '"w:bz2"',
    "طر_مع_xz": '"w:xz"',
    "طر_اقرأ_تلقائي": '"r:*"',
    "أقصى_ضغط": "9",
    "أسرع_ضغط": "1",
}

ARCHIVE_CONSTANT_PATTERN = (
    r"(?<![\w.\u0600-\u06FF])("
    + "|".join(sorted(ARCHIVE_CONSTANTS.keys(), key=len, reverse=True))
    + r")(?![\w\u0600-\u06FF])"
)

# Keyword arguments translated before "=" (see inline_replacer)
ARCHIVE_KWARGS = {
    "درجة_الضغط": "compresslevel",
    "كلمة_السر": "pwd",
    "أعضاء": "members",
    "إلى_مجلد": "path",
}

# Help text for CLI
ARCHIVE_HELP = [
    "# archive — أرشيف ZIP و TAR والضغط (zipfile / tarfile / gzip / bz2 / lzma)",
    "أنشئ_أرشيف(مسار, عناصر)        - إنشاء أرشيف ZIP من ملفات أو مجلد",
    "قائمة_الأرشيف(مسار)            - أسماء كل الأعضاء",
    "استخرج_الأرشيف(مسار, إلى)      - استخراج آمن ضد الخروج عن المجلد",
    "أضف_للأرشيف(مسار, عناصر)       - إضافة ملفات لأرشيف موجود",
    "احذف_من_الأرشيف(مسار, أسماء)   - إعادة بناء الأرشيف بدون أعضاء",
    "نص_العضو(مسار, عضو)            - نص عضو داخل الأرشيف",
    "ملخص_الأرشيف(مسار)             - جدول الأعضاء والأحجام",
    "افحص_أرشيف(مسار)               - هل هو ZIP صالح؟",
    "# داخل الأرشيف",
    "  أرشيف.اقرأ_عضو(اسم)          - بايتات العضو",
    "  أرشيف.اكتب_عضو(اسم, بيانات)  - كتابة عضو جديد",
    "  أرشيف.أسماء_الأعضاء()        - قائمة الأسماء",
    "  أرشيف.سرد_الأعضاء()          - كائنات ZipInfo",
    "  أرشيف.استخرج_الكل(إلى)       - استخراج الكل",
    "  أرشيف.أغلق_الأرشيف()         - إغلاق",
    "# TAR",
    "أنشئ_طر(مسار, عناصر, طر_مع_gz) - إنشاء أرشيف tar.gz",
    "استخرج_طر(مسار, إلى)           - استخراج أرشيف tar",
    "# الضغط",
    "ضغط_نص(نص) / فك_ضغط_نص(بايتات) - gzip مباشر",
    "ضغط_قوي / ضغط_فائق            - bz2 / lzma",
    "اقرأ_مضغوط(مسار.gz)            - قراءة ملف مضغوط كاملاً",
    "حجم_بشري(عدد_البايتات)         - 1.4 MB بدل 1468006",
]

# Import detection. Helpers import their modules lazily inside their body, but
# bare constants expand to ``zipfile.ZIP_DEFLATED`` at transpile time, so the
# common import is emitted only for programs that actually use an archive.
IMPORT_NAME = "zipfile"
IMPORT_CHECK = r"zipfile\.|tarfile\.|gzip\.|bz2\.|lzma\."
IMPORT_STATEMENT = "import zipfile, tarfile, gzip, bz2, lzma"

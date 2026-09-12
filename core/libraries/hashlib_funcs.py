"""
APL - Hashlib Library Functions
Transpiles Arabic hashing keywords to Python hashlib module calls

NOTE: hashlib requires bytes, not strings. Use b"..." for byte literals
or .encode('utf-8') on string variables.
"""

HASHLIB_FUNCS = {
    # تجزئة (Hashing)
    "تجزئة_md5": "hashlib.md5",
    "تجزئة_sha1": "hashlib.sha1",
    "تجزئة_sha256": "hashlib.sha256",
    "تجزئة_sha512": "hashlib.sha512",
    
    # مختصرات (Shortcuts)
    "md5": "hashlib.md5",
    "sha256": "hashlib.sha256",
    
    # دوال (Functions)
    "اشتق_مفتاح": "hashlib.pbkdf2_hmac",
}

HASHLIB_PATTERN = r"(?<!\w)(" + "|".join(sorted(HASHLIB_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
HASHLIB_HELP = [
    "# تجزئة (Hashing) - تتطلب bytes وليس strings",
    "تجزئة_md5(بايتات)      - تجزئة MD5",
    "تجزئة_sha1(بايتات)     - تجزئة SHA1",
    "تجزئة_sha256(بايتات)   - تجزئة SHA256 (الأكثر استخداماً)",
    "تجزئة_sha512(بايتات)   - تجزئة SHA512",
    "# مختصرات (Shortcuts)",
    "md5(بايتات)            - تجزئة MD5",
    "sha256(بايتات)         - تجزئة SHA256",
    "# دوال (Functions)",
    "اشتق_مفتاح(خوارزمية, كلمة, ملح, تكرار) - اشتقاق مفتاح",
]

# Import detection
IMPORT_NAME = "hashlib"
IMPORT_CHECK = "hashlib\."
IMPORT_STATEMENT = "import hashlib"

# مكتبة التجزئة — `hashlib`

مكتبة التجزئة بالعربي، متوافقة مع Python hashlib:

**7 عنصراً عربياً** (الدوال: 7).

## الدوال (7)

| العربي | Python |
|--------|--------|
| `تجزئة_md5` | `hashlib.md5` |
| `تجزئة_sha1` | `hashlib.sha1` |
| `تجزئة_sha256` | `hashlib.sha256` |
| `تجزئة_sha512` | `hashlib.sha512` |
| `md5` | `hashlib.md5` |
| `sha256` | `hashlib.sha256` |
| `اشتق_مفتاح` | `hashlib.pbkdf2_hmac` |

## مثال

```apl
# SHA256 و MD5 و SHA1 — كلها دوال عربية
المتغير نتيجة = تجزئة_sha256(b"Hello World")
print("SHA256:", نتيجة.hexdigest())

المتغير نتيجة2 = تجزئة_md5(b"Hello World")
print("MD5:", نتيجة2.hexdigest())

المتغير نتيجة3 = تجزئة_sha1(b"Hello World")
print("SHA1:", نتيجة3.hexdigest())
```

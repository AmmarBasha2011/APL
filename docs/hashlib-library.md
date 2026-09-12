# مكتبة التجزئة — `hashlib`

مكتبة التجزئة بالعربي، متوافقة مع Python hashlib:

## تجزئة (Hashing)

| العربي | Python | الوصف |
|--------|--------|-------|
| `تجزئة_md5(بايتات)` | `hashlib.md5(بايتات)` | تجزئة MD5 |
| `تجزئة_sha1(بايتات)` | `hashlib.sha1(بايتات)` | تجزئة SHA1 |
| `تجزئة_sha256(بايتات)` | `hashlib.sha256(بايتات)` | تجزئة SHA256 (الأكثر استخداماً) |
| `تجزئة_sha512(بايتات)` | `hashlib.sha512(بايتات)` | تجزئة SHA512 |

## مختصرات (Shortcuts)

| العربي | Python | الوصف |
|--------|--------|-------|
| `md5(بايتات)` | `hashlib.md5(بايتات)` | تجزئة MD5 |
| `sha256(بايتات)` | `hashlib.sha256(بايتات)` | تجزئة SHA256 |

## دوال (Functions)

| العربي | Python | الوصف |
|--------|--------|-------|
| `اشتق_مفتاح(خوارزمية, كلمة, ملح, تكرار)` | `hashlib.pbkdf2_hmac(...)` | اشتقاق مفتاح |

## ملاحظة مهمة

hashlib تتطلب **bytes** وليس strings. استخدم `b"..."` للبايتات الحرفية:
```apl
النتيجة = تجزئة_sha256(b"Hello World")
```

أو استخدم `.encode('utf-8')` للمتغيرات:
```apl
المتغير نص = "Hello World"
النتيجة = تجزئة_sha256(نص.encode("utf-8"))
```

## مثال

```apl
# SHA256
النتيجة = تجزئة_sha256(b"Hello World")
print("SHA256:", النتيجة.hexdigest())

# MD5
النتيجة2 = تجزئة_md5(b"Hello World")
print("MD5:", النتيجة2.hexdigest())

# SHA1
النتيجة3 = تجزئة_sha1(b"Hello World")
print("SHA1:", النتيجة3.hexdigest())

# Shortcuts
print("sha256:", sha256(b"test").hexdigest())
```

# مكتبة فئات البيانات والتعدادات — `dataclasses` & `enum`

مكتبة dataclasses و enum و abc الكاملة بالعربي:

**51 عنصراً عربياً** (الدوال: 68).

## الدوال (51)

| العربي | Python |
|--------|--------|
| `فئة_بيانات` | `dataclasses.dataclass` |
| `حقل_بيانات` | `dataclasses.field` |
| `أنواع` | `dataclasses.fields` |
| `اسم_حقل` | `field.name` |
| `نوع_حقل` | `field.type` |
| `قيمة_افتراضية` | `field.default` |
| `مصنع_افتراضي` | `field.default_factory` |
| `اختر_تمثيل` | `field.repr` |
| `اختر_مقارنة` | `field.compare` |
| `اختر_تجزئة` | `field.hash` |
| `بيانات_وصفية` | `field.metadata` |
| `تهيئة` | `field.init` |
| `اختر_مفتاح` | `field.kw_only` |
| `اختر_اختيار` | `field.omit` |
| `استبدال_حقل` | `dataclasses.replace` |
| `تهيئة_بعد` | `__post_init__` |
| `MISSING` | `dataclasses.MISSING` |
| `اختر_النوع` | `type` |
| `Enum` | `enum.Enum` |
| `Flag` | `enum.Flag` |
| `IntFlag` | `enum.IntFlag` |
| `IntEnum` | `enum.IntEnum` |
| `StrEnum` | `enum.StrEnum` |
| `قيم` | `EnumType` |
| `EnumMeta` | `enum.EnumMeta` |
| `auto` | `enum.auto` |
| `فريد` | `enum.unique` |
| `عضو_تعداد` | `EnumMember` |
| `ABC` | `abc.ABC` |
| `ABCMeta` | `abc.ABCMeta` |
| `دالة_مجردة` | `abc.abstractmethod` |
| `خاصية_مجردة` | `abc.abstractproperty` |
| `static_method` | `staticmethod` |
| `class_method` | `classmethod` |
| `فتحة` | `__slots__` |
| `مفاتيح` | `__slots__` |
| `فئة_بيانات_مجمدة` | `frozen` |
| `اختر_فئة` | `type` |
| `فئة_الأم` | `super` |
| `أب_بيانات` | `super` |
| `نوع_بيانات` | `type` |
| `من_نوع_بيانات` | `isinstance` |
| `يملك` | `hasattr` |
| `احصل_خاصية` | `getattr` |
| `ضع_خاصية` | `setattr` |
| `احذف_خاصية` | `delattr` |
| `قابل_للنداء` | `callable` |
| `اختر_وثيقة` | `__doc__` |
| `اختر_اسم` | `__name__` |
| `اختر_وحدة` | `__module__` |
| `اختر_ملف` | `__file__` |

## مثال

```apl
@فئة_بيانات
صنف مستخدم:
    اسم: نص
    عمر: صحيح
    بريد: نص = ""

المتغير ح = مستخدم("عمار", 25, "a@b.c")
اطبع ح.اسم, ح.عمر

اطبع تحويل_لقاموس(ح)

المتغير ح2 = استبدال_حقل(ح, عمر=26)
اطبع "بعد الاستبدال:", ح2.عمر
```

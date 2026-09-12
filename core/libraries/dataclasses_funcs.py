"""
APL - Dataclasses & Enum Library
Full dataclasses and enum wrapper with Arabic keywords
"""

DATACLASSES_FUNCS = {
    # Dataclasses
    "dataclass": "dataclasses.dataclass",
    "فئة_بيانات": "dataclasses.dataclass",
    "DataClass": "dataclasses.dataclass",
    "أنشئ_فئة_بيانات": "dataclasses.dataclass",
    
    # خصائص Dataclass
    "حقول": "dataclasses.fields",
    "حقل": "dataclasses.field",
    "أنواع": "dataclasses.fields",
    "اسم_حقل": "field.name",
    "نوع_حقل": "field.type",
    "قيمة_افتراضية": "field.default",
    "مصنع_افتراضي": "field.default_factory",
    "اختر_تمثيل": "field.repr",
    "اختر_مقارنة": "field.compare",
    "اختر_تجزئة": "field.hash",
    "بيانات_وصفية": "field.metadata",
    "تهيئة": "field.init",
    "اختر_مفتاح": "field.kw_only",
    "اختر_اختيار": "field.omit",
    
    # دوال Dataclass
    "تحويل_لصف": "dataclasses.astuple",
    "تحويل_لقاموس": "dataclasses.asdict",
    "استبدال": "dataclasses.replace",
    "فحص_فئة_بيانات": "dataclasses.is_dataclass",
    "تهيئة_بعد": "__post_init__",
    
    # دوال مساعدة
    "MISSING": "dataclasses.MISSING",
    "اختر_النوع": "dataclasses.KW_ONLY",
    
    # Enum
    "تعداد": "enum.Enum",
    "Enum": "enum.Enum",
    "أنشئ_تعداد": "enum.Enum",
    "Flag": "enum.Flag",
    "IntFlag": "enum.IntFlag",
    "IntEnum": "enum.IntEnum",
    "StrEnum": "enum.StrEnum",
    
    # خصائص Enum
    "أسماء": "enum.Enum",
    "قيم": "EnumType",
    "EnumType": "enum.EnumType",
    "EnumMeta": "enum.EnumMeta",
    
    # دوال Enum
    "تلقائي": "enum.auto",
    "auto": "enum.auto",
    "فريد": "enum.unique",
    "عضو_تعداد": "EnumMember",
    
    # ABC
    "ABC": "abc.ABC",
    "ABCMeta": "abc.ABCMeta",
    "مجرد": "abc.ABC",
    "فئة_مجردة": "abc.ABC",
    "دالة_مجردة": "abc.abstractmethod",
    "abstract_method": "abc.abstractmethod",
    "خاصية_مجردة": "abc.abstractproperty",
    "static_method": "staticmethod",
    "class_method": "classmethod",
    
    # مفاتيح البيانات
    "فتحة": "__slots__",
    "مفاتيح": "__slots__",
    "فئة_بيانات_مجمدة": "frozen",
    
    # خصائص مفيدة
    "اختر_النوع": "type",
    "اختر_فئة": "type",
    "فئة_الأم": "super",
    "أب": "super",
    "نوع": "type",
    "من_نوع": "isinstance",
    "يملك": "hasattr",
    "احصل_خاصية": "getattr",
    "ضع_خاصية": "setattr",
    "احذف_خاصية": "delattr",
    "قابل_للنداء": "callable",
    "اختر_وثيقة": "__doc__",
    "اختر_اسم": "__name__",
    "اختر_وحدة": "__module__",
    "اختر_ملف": "__file__",
}

DATACLASSES_PATTERN = r"(?<!\w)(" + "|".join(sorted(DATACLASSES_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

DATACLASSES_HELP = [
    "# === Dataclasses ===",
    "@dataclass                - مُزيِّن فئة البيانات",
    "@فئة_بيانات              - مُزيِّن (عربي)",
    "حقول(فئة)                - حقول الفئة",
    "حقل(افتراضي, مقارنة)     - حقل مخصص",
    "تهيئة_بعد(ذات)           - بعد التهيئة",
    "تحويل_لصف(كائن)          - تحويل لصف",
    "تحويل_لقاموس(كائن)        - تحويل لقاموس",
    "استبدال(كائن, **تغييرات)  - استبدال قيم",
    "فحص_فئة_بيانات(كائن)     - هل فئة بيانات",
    "# === Enum ===",
    "تعداد                     - فئة تعداد",
    "Enum                      - فئة تعداد (إنجليزي)",
    "IntEnum                   - تعداد أعداد صحيحة",
    "IntFlag                   - تعداد أعلام أعداد",
    "Flag                      - تعداد أعلام",
    "StrEnum                   - تعداد نصوص",
    "تلقائي()                  - قيمة تلقائية",
    "auto()                    - قيمة تلقائية (إنجليزي)",
    "فريد                      - تعداد فريد",
    "# === ABC ===",
    "مجرد()                   - فئة مجردة",
    "ABC                       - فئة مجردة (إنجليزي)",
    "دالة_مجردة(دالة)         - دالة مجردة",
    "abstract_method(دالة)     - دالة مجردة (إنجليزي)",
    "# === Data keys ===",
    "فتحة = (...)              - __slots__",
    "مفاتيح = (...)            - __slots__",
    "# === Useful properties ===",
    "نوع(كائن)                - type",
    "من_نوع(كائن, نوع)        - isinstance",
    "يملك(كائن, اسم)          - hasattr",
    "احصل_خاصية(كائن, اسم)    - getattr",
    "ضع_خاصية(كائن, اسم, قيمة) - setattr",
    "فئة_الأم()               - super",
    "أب()                      - super",
]

IMPORT_NAME = "dataclasses"
IMPORT_CHECK = "(dataclasses\.|enum\.|abc\.)"
IMPORT_STATEMENT = "from dataclasses import dataclass, field, asdict, astuple, replace; from enum import Enum, IntEnum, IntFlag, Flag, auto, unique; from abc import ABC, abstractmethod"

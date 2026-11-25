"""مولّد تلقائياً — مكتبة sortedcontainers لـ APL.

قوائم وقواميس ومجموعات مرتبة من حزمة sortedcontainers.

كل الأسماء وُلّدت آلياً من معرّفات الحزمة الحقيقية sortedcontainers، وتُرجم كل اسم إلى مسار
Python كامل. كل عنصر يشير إلى كائن Python حقيقي فريد لا تغطّيه مكتبة أخرى،
والأسماء فريدة عبر كل مكتبات APL ونواة اللغة.
"""

import re

SORTEDCONTAINERS_FUNCS = {
    "مرتبات_قائمة_مرتبة_ريكورسيف_ريبر": "sortedcontainers.sortedlist.recursive_repr",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة": "sortedcontainers.sortedlist.SortedList",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_أدرج": "sortedcontainers.sortedlist.SortedList.insert",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_أضف": "sortedcontainers.sortedlist.SortedList.add",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_ألحق": "sortedcontainers.sortedlist.SortedList.append",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_احذف": "sortedcontainers.sortedlist.SortedList.remove",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_اسحب": "sortedcontainers.sortedlist.SortedList.pop",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_اعكس": "sortedcontainers.sortedlist.SortedList.reverse",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_امسح": "sortedcontainers.sortedlist.SortedList.clear",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_انسخ": "sortedcontainers.sortedlist.SortedList.copy",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_تجاهل": "sortedcontainers.sortedlist.SortedList.discard",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_تنصيف": "sortedcontainers.sortedlist.SortedList.bisect",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_تنصيف_يسار": "sortedcontainers.sortedlist.SortedList.bisect_left",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_تنصيف_يمين": "sortedcontainers.sortedlist.SortedList.bisect_right",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_حدّث": "sortedcontainers.sortedlist.SortedList.update",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_شريحة_تكرار": "sortedcontainers.sortedlist.SortedList.islice",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_عدد": "sortedcontainers.sortedlist.SortedList.count",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_فهرس": "sortedcontainers.sortedlist.SortedList.index",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_مدى_فهرسي": "sortedcontainers.sortedlist.SortedList.irange",
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_مدّد": "sortedcontainers.sortedlist.SortedList.extend",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة": "sortedcontainers.sortedlist.SortedKeyList",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_أضف": "sortedcontainers.sortedlist.SortedKeyList.add",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_احذف": "sortedcontainers.sortedlist.SortedKeyList.remove",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_امسح": "sortedcontainers.sortedlist.SortedKeyList.clear",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_انسخ": "sortedcontainers.sortedlist.SortedKeyList.copy",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_تجاهل": "sortedcontainers.sortedlist.SortedKeyList.discard",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_تنصيف": "sortedcontainers.sortedlist.SortedKeyList.bisect",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_تنصيف_مفتاح": "sortedcontainers.sortedlist.SortedKeyList.bisect_key",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_تنصيف_مفتاح_يسار": "sortedcontainers.sortedlist.SortedKeyList.bisect_key_left",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_تنصيف_مفتاح_يمين": "sortedcontainers.sortedlist.SortedKeyList.bisect_key_right",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_تنصيف_يسار": "sortedcontainers.sortedlist.SortedKeyList.bisect_left",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_تنصيف_يمين": "sortedcontainers.sortedlist.SortedKeyList.bisect_right",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_حدّث": "sortedcontainers.sortedlist.SortedKeyList.update",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_عدد": "sortedcontainers.sortedlist.SortedKeyList.count",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_فهرس": "sortedcontainers.sortedlist.SortedKeyList.index",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_مدى_فهرسي": "sortedcontainers.sortedlist.SortedKeyList.irange",
    "مرتبات_قائمة_مرتبة_مرتب_مفتاح_قائمة_مدى_فهرسي_مفتاح": "sortedcontainers.sortedlist.SortedKeyList.irange_key",
    "مرتبات_قائمة_مرتبة_يدينتيتي": "sortedcontainers.sortedlist.identity",
    "مرتبات_قاموس_مرتب_قاموس_مرتب": "sortedcontainers.sorteddict.SortedDict",
    "مرتبات_قاموس_مرتب_قاموس_مرتب_اسحب": "sortedcontainers.sorteddict.SortedDict.pop",
    "مرتبات_قاموس_مرتب_قاموس_مرتب_اسحب_عنصراً": "sortedcontainers.sorteddict.SortedDict.popitem",
    "مرتبات_قاموس_مرتب_قاموس_مرتب_امسح": "sortedcontainers.sorteddict.SortedDict.clear",
    "مرتبات_قاموس_مرتب_قاموس_مرتب_انسخ": "sortedcontainers.sorteddict.SortedDict.copy",
    "مرتبات_قاموس_مرتب_قاموس_مرتب_بيكيتيم": "sortedcontainers.sorteddict.SortedDict.peekitem",
    "مرتبات_قاموس_مرتب_قاموس_مرتب_حدّث": "sortedcontainers.sorteddict.SortedDict.update",
    "مرتبات_قاموس_مرتب_قاموس_مرتب_ضبط_افتراضي": "sortedcontainers.sorteddict.SortedDict.setdefault",
    "مرتبات_قاموس_مرتب_قاموس_مرتب_عناصر": "sortedcontainers.sorteddict.SortedDict.items",
    "مرتبات_قاموس_مرتب_قاموس_مرتب_فرومكيس": "sortedcontainers.sorteddict.SortedDict.fromkeys",
    "مرتبات_قاموس_مرتب_قاموس_مرتب_قيم": "sortedcontainers.sorteddict.SortedDict.values",
    "مرتبات_قاموس_مرتب_قاموس_مرتب_مفاتيح": "sortedcontainers.sorteddict.SortedDict.keys",
    "مرتبات_قاموس_مرتب_مرتب_عناصر_عرض": "sortedcontainers.sorteddict.SortedItemsView",
    "مرتبات_قاموس_مرتب_مرتب_قيم_عرض": "sortedcontainers.sorteddict.SortedValuesView",
    "مرتبات_قاموس_مرتب_مرتب_مفاتيح_عرض": "sortedcontainers.sorteddict.SortedKeysView",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة": "sortedcontainers.sortedset.SortedSet",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_أضف": "sortedcontainers.sortedset.SortedSet.add",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_اتحاد": "sortedcontainers.sortedset.SortedSet.union",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_احذف": "sortedcontainers.sortedset.SortedSet.remove",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_اسحب": "sortedcontainers.sortedset.SortedSet.pop",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_امسح": "sortedcontainers.sortedset.SortedSet.clear",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_انسخ": "sortedcontainers.sortedset.SortedSet.copy",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_تجاهل": "sortedcontainers.sortedset.SortedSet.discard",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_تقاطع": "sortedcontainers.sortedset.SortedSet.intersection",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_تقاطع_حدّث": "sortedcontainers.sortedset.SortedSet.intersection_update",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_حدّث": "sortedcontainers.sortedset.SortedSet.update",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_عدد": "sortedcontainers.sortedset.SortedSet.count",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_فرق": "sortedcontainers.sortedset.SortedSet.difference",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_فرق_حدّث": "sortedcontainers.sortedset.SortedSet.difference_update",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_متماثل_فرق": "sortedcontainers.sortedset.SortedSet.symmetric_difference",
    "مرتبات_مجموعة_مرتبة_مجموعة_مرتبة_متماثل_فرق_حدّث": "sortedcontainers.sortedset.SortedSet.symmetric_difference_update",
}

SORTEDCONTAINERS_CONSTS = {
    "مرتبات_قائمة_مرتبة_قائمة_مرتبة_افتراضي_LOAD_عامل": "sortedcontainers.sortedlist.SortedList.DEFAULT_LOAD_FACTOR",
}

IMPORT_MODULES = ['sortedcontainers', 'sortedcontainers.sorteddict', 'sortedcontainers.sortedlist', 'sortedcontainers.sortedset']
IMPORT_CHECK = r"(?<![\w.])(?:sortedcontainers)\."
IMPORT_STATEMENT = "import " + ", ".join(IMPORT_MODULES)

SORTEDCONTAINERS_HELP = [
    "# sortedcontainers - قوائم وقواميس ومجموعات مرتبة من حزمة sortedcontainers",
]

_SORTEDCONTAINERS_TOKEN = re.compile(
    r"(?P<dot>\.)?"
    r"(?P<word>(?!\d)[\w\u064B-\u065F\u0670]+)"
    r"(?P<open>\s*\()?"
)

USER_NAMES = set()


def _sortedcontainers_replace(match):
    dot = match.group("dot")
    word = match.group("word")
    open_paren = match.group("open")
    if word in USER_NAMES:
        return match.group(0)
    if dot:
        return match.group(0)
    if word in SORTEDCONTAINERS_CONSTS:
        return SORTEDCONTAINERS_CONSTS[word]
    if word in SORTEDCONTAINERS_FUNCS:
        return SORTEDCONTAINERS_FUNCS[word] + (open_paren or "")
    return match.group(0)


def SORTEDCONTAINERS_SUBSTITUTE(text):
    """يترجم كلمات المكتبة في نص واحد ويُرجع المترجم."""
    if not text:
        return text
    return _SORTEDCONTAINERS_TOKEN.sub(_sortedcontainers_replace, text)

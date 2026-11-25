"""مولّد تلقائياً — مكتبة cachetools لـ APL.

ذواكر مؤقتة بسياسات إخلاء متعددة من حزمة cachetools.

كل الأسماء وُلّدت آلياً من معرّفات الحزمة الحقيقية cachetools، وتُرجم كل اسم إلى مسار
Python كامل. كل عنصر يشير إلى كائن Python حقيقي فريد لا تغطّيه مكتبة أخرى،
والأسماء فريدة عبر كل مكتبات APL ونواة اللغة.
"""

import re

CACHETOOLS_FUNCS = {
    "كاش_تولز_FIFO_ذاكرة_مؤقتة": "cachetools.FIFOCache",
    "كاش_تولز_FIFO_ذاكرة_مؤقتة_اسحب_عنصراً": "cachetools.FIFOCache.popitem",
    "كاش_تولز_FIFO_ذاكرة_مؤقتة_امسح": "cachetools.FIFOCache.clear",
    "كاش_تولز_LFU_ذاكرة_مؤقتة": "cachetools.LFUCache",
    "كاش_تولز_LFU_ذاكرة_مؤقتة_اسحب_عنصراً": "cachetools.LFUCache.popitem",
    "كاش_تولز_LFU_ذاكرة_مؤقتة_امسح": "cachetools.LFUCache.clear",
    "كاش_تولز_LRU_ذاكرة_مؤقتة": "cachetools.LRUCache",
    "كاش_تولز_LRU_ذاكرة_مؤقتة_اسحب_عنصراً": "cachetools.LRUCache.popitem",
    "كاش_تولز_LRU_ذاكرة_مؤقتة_امسح": "cachetools.LRUCache.clear",
    "كاش_تولز_RR_ذاكرة_مؤقتة": "cachetools.RRCache",
    "كاش_تولز_RR_ذاكرة_مؤقتة_اسحب_عنصراً": "cachetools.RRCache.popitem",
    "كاش_تولز_RR_ذاكرة_مؤقتة_امسح": "cachetools.RRCache.clear",
    "كاش_تولز_TLRU_ذاكرة_مؤقتة": "cachetools.TLRUCache",
    "كاش_تولز_TLRU_ذاكرة_مؤقتة_اسحب_عنصراً": "cachetools.TLRUCache.popitem",
    "كاش_تولز_TLRU_ذاكرة_مؤقتة_امسح": "cachetools.TLRUCache.clear",
    "كاش_تولز_TLRU_ذاكرة_مؤقتة_انتهاء": "cachetools.TLRUCache.expire",
    "كاش_تولز_TTL_ذاكرة_مؤقتة": "cachetools.TTLCache",
    "كاش_تولز_TTL_ذاكرة_مؤقتة_اسحب_عنصراً": "cachetools.TTLCache.popitem",
    "كاش_تولز_TTL_ذاكرة_مؤقتة_امسح": "cachetools.TTLCache.clear",
    "كاش_تولز_TTL_ذاكرة_مؤقتة_انتهاء": "cachetools.TTLCache.expire",
    "كاش_تولز_ذاكرة_مؤقتة": "cachetools.Cache",
    "كاش_تولز_ذاكرة_مؤقتة_اسحب": "cachetools.Cache.pop",
    "كاش_تولز_ذاكرة_مؤقتة_امسح": "cachetools.Cache.clear",
    "كاش_تولز_ذاكرة_مؤقتة_جلب": "cachetools.Cache.get",
    "كاش_تولز_ذاكرة_مؤقتة_حجم_كائن": "cachetools.Cache.getsizeof",
    "كاش_تولز_ذاكرة_مؤقتة_ضبط_افتراضي": "cachetools.Cache.setdefault",
    "كاش_تولز_ذاكرة_مؤقتة_معلومات": "cachetools.CacheInfo",
    "كاش_تولز_طريقة_مخزّنة": "cachetools.cachedmethod",
    "كاش_تولز_فونك_الأقل_استخداماً_ذاكرة_مؤقتة": "cachetools.func.lfu_cache",
    "كاش_تولز_فونك_الأقل_حديثاً_ذاكرة_مؤقتة": "cachetools.func.lru_cache",
    "كاش_تولز_فونك_الأول_دخولاً_ذاكرة_مؤقتة": "cachetools.func.fifo_cache",
    "كاش_تولز_فونك_دوري_ذاكرة_مؤقتة": "cachetools.func.rr_cache",
    "كاش_تولز_فونك_مدة_حياة_ذاكرة_مؤقتة": "cachetools.func.ttl_cache",
    "كاش_تولز_مخزّن": "cachetools.cached",
    "كاش_تولز_مفاتيح_تيبيدميثودكي": "cachetools.keys.typedmethodkey",
    "كاش_تولز_مفاتيح_مفتاح_تجزئة": "cachetools.keys.hashkey",
    "كاش_تولز_مفاتيح_مفتاح_مكتوب": "cachetools.keys.typedkey",
    "كاش_تولز_مفاتيح_ميثودكي": "cachetools.keys.methodkey",
}

CACHETOOLS_CONSTS = {
}

IMPORT_MODULES = ['cachetools', 'cachetools.func', 'cachetools.keys']
IMPORT_CHECK = r"(?<![\w.])(?:cachetools)\."
IMPORT_STATEMENT = "import " + ", ".join(IMPORT_MODULES)

CACHETOOLS_HELP = [
    "# cachetools - ذواكر مؤقتة بسياسات إخلاء متعددة من حزمة cachetools",
]

_CACHETOOLS_TOKEN = re.compile(
    r"(?P<dot>\.)?"
    r"(?P<word>(?!\d)[\w\u064B-\u065F\u0670]+)"
    r"(?P<open>\s*\()?"
)

USER_NAMES = set()


def _cachetools_replace(match):
    dot = match.group("dot")
    word = match.group("word")
    open_paren = match.group("open")
    if word in USER_NAMES:
        return match.group(0)
    if dot:
        return match.group(0)
    if word in CACHETOOLS_CONSTS:
        return CACHETOOLS_CONSTS[word]
    if word in CACHETOOLS_FUNCS:
        return CACHETOOLS_FUNCS[word] + (open_paren or "")
    return match.group(0)


def CACHETOOLS_SUBSTITUTE(text):
    """يترجم كلمات المكتبة في نص واحد ويُرجع المترجم."""
    if not text:
        return text
    return _CACHETOOLS_TOKEN.sub(_cachetools_replace, text)

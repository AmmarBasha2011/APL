"""مولّد تلقائياً — مكتبة humanize لـ APL.

تحويل الأرقام والأزمنة والأحجام لصيغة مقروءة من حزمة humanize.

كل الأسماء وُلّدت آلياً من معرّفات الحزمة الحقيقية humanize، وتُرجم كل اسم إلى مسار
Python كامل. كل عنصر يشير إلى كائن Python حقيقي فريد لا تغطّيه مكتبة أخرى،
والأسماء فريدة عبر كل مكتبات APL ونواة اللغة.
"""

import re

HUMANIZE_FUNCS = {
    "هيومنايز_تعريب_ثاوساندس_سيباراتور": "humanize.i18n.thousands_separator",
    "هيومنايز_تعريب_جلب_ترجمة": "humanize.i18n.get_translation",
    "هيومنايز_تعريب_ديسيمال_سيباراتور": "humanize.i18n.decimal_separator",
    "هيومنايز_تعريب_عطّل": "humanize.i18n.deactivate",
    "هيومنايز_تعريب_فعّل": "humanize.i18n.activate",
    "هيومنايز_حجم_ملف_حجم_طبيعي": "humanize.filesize.naturalsize",
    "هيومنايز_رقم_ترتيبي": "humanize.number.ordinal",
    "هيومنايز_رقم_رقم_صحفي": "humanize.number.apnumber",
    "هيومنايز_رقم_رقم_كلمات": "humanize.number.intword",
    "هيومنايز_رقم_علمي": "humanize.number.scientific",
    "هيومنايز_رقم_فواصل_أرقام": "humanize.number.intcomma",
    "هيومنايز_رقم_قيّد": "humanize.number.clamp",
    "هيومنايز_رقم_كسري": "humanize.number.fractional",
    "هيومنايز_رقم_متري": "humanize.number.metric",
    "هيومنايز_ليستس_طبيعي_قائمة": "humanize.lists.natural_list",
    "هيومنايز_وقت_تاريخ_طبيعي": "humanize.time.naturaldate",
    "هيومنايز_وقت_فرق_دقيق": "humanize.time.precisedelta",
    "هيومنايز_وقت_فرق_طبيعي": "humanize.time.naturaldelta",
    "هيومنايز_وقت_وقت_طبيعي": "humanize.time.naturaltime",
    "هيومنايز_وقت_ونيت": "humanize.time.Unit",
    "هيومنايز_وقت_يوم_طبيعي": "humanize.time.naturalday",
}

HUMANIZE_CONSTS = {
    "هيومنايز_تعريب_TYPE_تشيكينج": "humanize.i18n.TYPE_CHECKING",
    "هيومنايز_رقم_TYPE_تشيكينج": "humanize.number.TYPE_CHECKING",
    "هيومنايز_ليستس_TYPE_تشيكينج": "humanize.lists.TYPE_CHECKING",
    "هيومنايز_وقت_TYPE_تشيكينج": "humanize.time.TYPE_CHECKING",
}

IMPORT_MODULES = ['humanize', 'humanize.filesize', 'humanize.i18n', 'humanize.lists', 'humanize.number', 'humanize.time']
IMPORT_CHECK = r"(?<![\w.])(?:humanize)\."
IMPORT_STATEMENT = "import " + ", ".join(IMPORT_MODULES)

HUMANIZE_HELP = [
    "# humanize - تحويل الأرقام والأزمنة والأحجام لصيغة مقروءة من حزمة humanize",
]

_HUMANIZE_TOKEN = re.compile(
    r"(?P<dot>\.)?"
    r"(?P<word>(?!\d)[\w\u064B-\u065F\u0670]+)"
    r"(?P<open>\s*\()?"
)

USER_NAMES = set()


def _humanize_replace(match):
    dot = match.group("dot")
    word = match.group("word")
    open_paren = match.group("open")
    if word in USER_NAMES:
        return match.group(0)
    if dot:
        return match.group(0)
    if word in HUMANIZE_CONSTS:
        return HUMANIZE_CONSTS[word]
    if word in HUMANIZE_FUNCS:
        return HUMANIZE_FUNCS[word] + (open_paren or "")
    return match.group(0)


def HUMANIZE_SUBSTITUTE(text):
    """يترجم كلمات المكتبة في نص واحد ويُرجع المترجم."""
    if not text:
        return text
    return _HUMANIZE_TOKEN.sub(_humanize_replace, text)

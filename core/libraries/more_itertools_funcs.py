"""مولّد تلقائياً — مكتبة more_itertools لـ APL.

أدوات التكرار الإضافية من حزمة more_itertools.

كل الأسماء وُلّدت آلياً من معرّفات الحزمة الحقيقية more_itertools، وتُرجم كل اسم إلى مسار
Python كامل. كل عنصر يشير إلى كائن Python حقيقي فريد لا تغطّيه مكتبة أخرى،
والأسماء فريدة عبر كل مكتبات APL ونواة اللغة.
"""

import re

MORE_ITERTOOLS_FUNCS = {
    "مور_إيتر_ريسيبيس_أول_صحيح": "more_itertools.recipes.first_true",
    "مور_إيتر_ريسيبيس_إحصاءات": "more_itertools.recipes.Stats",
    "مور_إيتر_ريسيبيس_استهلك": "more_itertools.recipes.consume",
    "مور_إيتر_ريسيبيس_الترتيب": "more_itertools.recipes.nth",
    "مور_إيتر_ريسيبيس_الترتيب_كومبيناتيون": "more_itertools.recipes.nth_combination",
    "مور_إيتر_ريسيبيس_التفاف": "more_itertools.recipes.convolve",
    "مور_إيتر_ريسيبيس_باتشيد": "more_itertools.recipes.batched",
    "مور_إيتر_ريسيبيس_بدّل": "more_itertools.recipes.transpose",
    "مور_إيتر_ريسيبيس_بريبيند": "more_itertools.recipes.prepend",
    "مور_إيتر_ريسيبيس_بيرويس": "more_itertools.recipes.pairwise",
    "مور_إيتر_ريسيبيس_تريبليويس": "more_itertools.recipes.triplewise",
    "مور_إيتر_ريسيبيس_تكرار_فهرس": "more_itertools.recipes.iter_index",
    "مور_إيتر_ريسيبيس_تكرار_يكسيبت": "more_itertools.recipes.iter_except",
    "مور_إيتر_ريسيبيس_توتيينت": "more_itertools.recipes.totient",
    "مور_إيتر_ريسيبيس_جداء_نقطي": "more_itertools.recipes.dotproduct",
    "مور_إيتر_ريسيبيس_جدولة": "more_itertools.recipes.tabulate",
    "مور_إيتر_ريسيبيس_جراوبير": "more_itertools.recipes.grouper",
    "مور_إيتر_ريسيبيس_حشو_لاشيء": "more_itertools.recipes.pad_none",
    "مور_إيتر_ريسيبيس_خذ": "more_itertools.recipes.take",
    "مور_إيتر_ريسيبيس_دورات": "more_itertools.recipes.ncycles",
    "مور_إيتر_ريسيبيس_ذيل": "more_itertools.recipes.tail",
    "مور_إيتر_ريسيبيس_راوندروبين": "more_itertools.recipes.roundrobin",
    "مور_إيتر_ريسيبيس_رونينج_أدنى": "more_itertools.recipes.running_min",
    "مور_إيتر_ريسيبيس_رونينج_أقصى": "more_itertools.recipes.running_max",
    "مور_إيتر_ريسيبيس_رونينج_إحصاءات": "more_itertools.recipes.running_statistics",
    "مور_إيتر_ريسيبيس_رونينج_متوسط": "more_itertools.recipes.running_mean",
    "مور_إيتر_ريسيبيس_رونينج_وسيط": "more_itertools.recipes.running_median",
    "مور_إيتر_ريسيبيس_ريبيتفونك": "more_itertools.recipes.repeatfunc",
    "مور_إيتر_ريسيبيس_ريشاب": "more_itertools.recipes.reshape",
    "مور_إيتر_ريسيبيس_سطّح": "more_itertools.recipes.flatten",
    "مور_إيتر_ريسيبيس_سوبسليسيس": "more_itertools.recipes.subslices",
    "مور_إيتر_ريسيبيس_ضرب_مصفوفات": "more_itertools.recipes.matmul",
    "مور_إيتر_ريسيبيس_عامل": "more_itertools.recipes.factor",
    "مور_إيتر_ريسيبيس_عشوائي_بيرموتاتيون": "more_itertools.recipes.random_permutation",
    "مور_إيتر_ريسيبيس_عشوائي_ديرانجيمينت": "more_itertools.recipes.random_derangement",
    "مور_إيتر_ريسيبيس_عشوائي_ضرب": "more_itertools.recipes.random_product",
    "مور_إيتر_ريسيبيس_عشوائي_كومبيناتيون": "more_itertools.recipes.random_combination",
    "مور_إيتر_ريسيبيس_عشوائي_كومبيناتيون_ويث_ريبلاسيمينت": "more_itertools.recipes.random_combination_with_replacement",
    "مور_إيتر_ريسيبيس_غربال": "more_itertools.recipes.sieve",
    "مور_إيتر_ريسيبيس_فريد": "more_itertools.recipes.unique",
    "مور_إيتر_ريسيبيس_فريد_جوستسين": "more_itertools.recipes.unique_justseen",
    "مور_إيتر_ريسيبيس_فريد_يفيرسين": "more_itertools.recipes.unique_everseen",
    "مور_إيتر_ريسيبيس_قبل_اند_بعد": "more_itertools.recipes.before_and_after",
    "مور_إيتر_ريسيبيس_قدّر": "more_itertools.recipes.quantify",
    "مور_إيتر_ريسيبيس_قسّم": "more_itertools.recipes.partition",
    "مور_إيتر_ريسيبيس_كثير_حدود_ديريفاتيف": "more_itertools.recipes.polynomial_derivative",
    "مور_إيتر_ريسيبيس_كثير_حدود_فروم_روتس": "more_itertools.recipes.polynomial_from_roots",
    "مور_إيتر_ريسيبيس_كثير_حدود_يفال": "more_itertools.recipes.polynomial_eval",
    "مور_إيتر_ريسيبيس_كل_يكوال": "more_itertools.recipes.all_equal",
    "مور_إيتر_ريسيبيس_لوبس": "more_itertools.recipes.loops",
    "مور_إيتر_ريسيبيس_مجموع_من_سكواريس": "more_itertools.recipes.sum_of_squares",
    "مور_إيتر_ريسيبيس_مجموعة_القوى": "more_itertools.recipes.powerset",
    "مور_إيتر_ريسيبيس_منزلق_نافذة": "more_itertools.recipes.sliding_window",
    "مور_إيتر_ريسيبيس_مولتينوميال": "more_itertools.recipes.multinomial",
    "مور_إيتر_ريسيبيس_هل_بريم": "more_itertools.recipes.is_prime",
    "مور_إيتر_مور_آخر": "more_itertools.more.last",
    "مور_إيتر_مور_أول": "more_itertools.more.first",
    "مور_إيتر_مور_ابورت_ثريد": "more_itertools.more.AbortThread",
    "مور_إيتر_مور_ادجاسينت": "more_itertools.more.adjacent",
    "مور_إيتر_مور_اربط_مابينجس": "more_itertools.more.join_mappings",
    "مور_إيتر_مور_ارجماكس": "more_itertools.more.argmax",
    "مور_إيتر_مور_ارجمين": "more_itertools.more.argmin",
    "مور_إيتر_مور_اضمم_برودكاست": "more_itertools.more.zip_broadcast",
    "مور_إيتر_مور_اضمم_وفسيت": "more_itertools.more.zip_offset",
    "مور_إيتر_مور_اطوِ": "more_itertools.more.collapse",
    "مور_إيتر_مور_الأطول_كومون_بريفيكس": "more_itertools.more.longest_common_prefix",
    "مور_إيتر_مور_الترتيب_بريم": "more_itertools.more.nth_prime",
    "مور_إيتر_مور_الترتيب_بيرموتاتيون": "more_itertools.more.nth_permutation",
    "مور_إيتر_مور_الترتيب_ضرب": "more_itertools.more.nth_product",
    "مور_إيتر_مور_الترتيب_كومبيناتيون_ويث_ريبلاسيمينت": "more_itertools.more.nth_combination_with_replacement",
    "مور_إيتر_مور_الترتيب_ور_آخر": "more_itertools.more.nth_or_last",
    "مور_إيتر_مور_اوتير_ضرب": "more_itertools.more.outer_product",
    "مور_إيتر_مور_باديد": "more_itertools.more.padded",
    "مور_إيتر_مور_بارتيال_ضرب": "more_itertools.more.partial_product",
    "مور_إيتر_مور_بارتيتيونس": "more_itertools.more.partitions",
    "مور_إيتر_مور_بالضبط_ن": "more_itertools.more.exactly_n",
    "مور_إيتر_مور_بوكيت": "more_itertools.more.bucket",
    "مور_إيتر_مور_بيرموتاتيون_فهرس": "more_itertools.more.permutation_index",
    "مور_إيتر_مور_تخلل": "more_itertools.more.intersperse",
    "مور_إيتر_مور_تدرّج": "more_itertools.more.stagger",
    "مور_إيتر_مور_تسلسل_عرض": "more_itertools.more.SequenceView",
    "مور_إيتر_مور_تشابك": "more_itertools.more.interleave",
    "مور_إيتر_مور_تشابك_الأطول": "more_itertools.more.interleave_longest",
    "مور_إيتر_مور_تشابك_راندوملي": "more_itertools.more.interleave_randomly",
    "مور_إيتر_مور_تشابك_يفينلي": "more_itertools.more.interleave_evenly",
    "مور_إيتر_مور_تكرار_سوبريس": "more_itertools.more.iter_suppress",
    "مور_إيتر_مور_جراوبي_ترانسفورم": "more_itertools.more.groupby_transform",
    "مور_إيتر_مور_جري_ضرب": "more_itertools.more.gray_product",
    "مور_إيتر_مور_خذ_طالما_ينكلوسيف": "more_itertools.more.takewhile_inclusive",
    "مور_إيتر_مور_دائماً_ريفيرسيبل": "more_itertools.more.always_reversible",
    "مور_إيتر_مور_دائماً_يتيرابل": "more_itertools.more.always_iterable",
    "مور_إيتر_مور_داوبليستارماب": "more_itertools.more.doublestarmap",
    "مور_إيتر_مور_دفت": "more_itertools.more.dft",
    "مور_إيتر_مور_دوبليكاتيس_جوستسين": "more_itertools.more.duplicates_justseen",
    "مور_إيتر_مور_دوبليكاتيس_يفيرسين": "more_itertools.more.duplicates_everseen",
    "مور_إيتر_مور_ديرانجيمينتس": "more_itertools.more.derangements",
    "مور_إيتر_مور_ديستريبوت": "more_itertools.more.distribute",
    "مور_إيتر_مور_ديفيد": "more_itertools.more.divide",
    "مور_إيتر_مور_رتّب_توجيثير": "more_itertools.more.sort_together",
    "مور_إيتر_مور_رد_نداء_تكرار": "more_itertools.more.callback_iter",
    "مور_إيتر_مور_رستريب": "more_itertools.more.rstrip",
    "مور_إيتر_مور_رلوكات": "more_itertools.more.rlocate",
    "مور_إيتر_مور_ريبلاك": "more_itertools.more.replace",
    "مور_إيتر_مور_ريس": "more_itertools.more.raise_",
    "مور_إيتر_مور_سبي": "more_itertools.more.spy",
    "مور_إيتر_مور_ستريب": "more_itertools.more.strip",
    "مور_إيتر_مور_ستريكتلي_ن": "more_itertools.more.strictly_n",
    "مور_إيتر_مور_سوبسترينجس": "more_itertools.more.substrings",
    "مور_إيتر_مور_سوبسترينجس_ينديكسيس": "more_itertools.more.substrings_indexes",
    "مور_إيتر_مور_سوبفاكتوريال": "more_itertools.more.subfactorial",
    "مور_إيتر_مور_سيد_يفيكت": "more_itertools.more.side_effect",
    "مور_إيتر_مور_سيركولار_شيفتس": "more_itertools.more.circular_shifts",
    "مور_إيتر_مور_سيرياليز": "more_itertools.more.serialize",
    "مور_إيتر_مور_سيرياليز_أغلق": "more_itertools.more.serialize.close",
    "مور_إيتر_مور_سيرياليز_ثرو": "more_itertools.more.serialize.throw",
    "مور_إيتر_مور_سيرياليز_سيند": "more_itertools.more.serialize.send",
    "مور_إيتر_مور_سيزيد_مكرر": "more_itertools.more.sized_iterator",
    "مور_إيتر_مور_سيكابل": "more_itertools.more.seekable",
    "مور_إيتر_مور_سيكابل_ابحث": "more_itertools.more.seekable.seek",
    "مور_إيتر_مور_سيكابل_اطّلع": "more_itertools.more.seekable.peek",
    "مور_إيتر_مور_سيكابل_ريلاتيف_ابحث": "more_itertools.more.seekable.relative_seek",
    "مور_إيتر_مور_سيكابل_يليمينتس": "more_itertools.more.seekable.elements",
    "مور_إيتر_مور_سينتشرونيزيد": "more_itertools.more.synchronized",
    "مور_إيتر_مور_شريحة_تكرار_يكستينديد": "more_itertools.more.islice_extended",
    "مور_إيتر_مور_شغّل_طول": "more_itertools.more.run_length",
    "مور_إيتر_مور_شغّل_طول_ديكود": "more_itertools.more.run_length.decode",
    "مور_إيتر_مور_شغّل_طول_ينكود": "more_itertools.more.run_length.encode",
    "مور_إيتر_مور_صفّي_طبّق": "more_itertools.more.filter_map",
    "مور_إيتر_مور_صفّي_يكسيبت": "more_itertools.more.filter_except",
    "مور_إيتر_مور_ضبط_بارتيتيونس": "more_itertools.more.set_partitions",
    "مور_إيتر_مور_ضرب_فهرس": "more_itertools.more.product_index",
    "مور_إيتر_مور_طبّق_ريدوك": "more_itertools.more.map_reduce",
    "مور_إيتر_مور_طبّق_يف": "more_itertools.more.map_if",
    "مور_إيتر_مور_طبّق_يكسيبت": "more_itertools.more.map_except",
    "مور_إيتر_مور_طول_تكرار": "more_itertools.more.ilen",
    "مور_إيتر_مور_عدد_دورة": "more_itertools.more.count_cycle",
    "مور_إيتر_مور_عشوائي_ورديريد_مدى": "more_itertools.more.random_ordered_range",
    "مور_إيتر_مور_عينة": "more_itertools.more.sample",
    "مور_إيتر_مور_فرق": "more_itertools.more.difference",
    "مور_إيتر_مور_فريد_إلى_يتش": "more_itertools.more.unique_to_each",
    "مور_إيتر_مور_فريد_ين_نافذة": "more_itertools.more.unique_in_window",
    "مور_إيتر_مور_فقط": "more_itertools.more.only",
    "مور_إيتر_مور_فك_الضم": "more_itertools.more.unzip",
    "مور_إيتر_مور_قابل_للاطلاع": "more_itertools.more.peekable",
    "مور_إيتر_مور_قابل_للاطلاع_اطّلع": "more_itertools.more.peekable.peek",
    "مور_إيتر_مور_قابل_للاطلاع_بريبيند": "more_itertools.more.peekable.prepend",
    "مور_إيتر_مور_قسّم_بعد": "more_itertools.more.split_after",
    "مور_إيتر_مور_قسّم_عند": "more_itertools.more.split_at",
    "مور_إيتر_مور_قسّم_قبل": "more_itertools.more.split_before",
    "مور_إيتر_مور_قسّم_وهين": "more_itertools.more.split_when",
    "مور_إيتر_مور_قسّم_ينتو": "more_itertools.more.split_into",
    "مور_إيتر_مور_قيمة_سلسلة": "more_itertools.more.value_chain",
    "مور_إيتر_مور_كاونتابل": "more_itertools.more.countable",
    "مور_إيتر_مور_كرر": "more_itertools.more.iterate",
    "مور_إيتر_مور_كرر_آخر": "more_itertools.more.repeat_last",
    "مور_إيتر_مور_كرر_يتش": "more_itertools.more.repeat_each",
    "مور_إيتر_مور_كل_فريد": "more_itertools.more.all_unique",
    "مور_إيتر_مور_كلاسيفي_فريد": "more_itertools.more.classify_unique",
    "مور_إيتر_مور_كومبيناتيون_فهرس": "more_itertools.more.combination_index",
    "مور_إيتر_مور_كومبيناتيون_ويث_ريبلاسيمينت_فهرس": "more_itertools.more.combination_with_replacement_index",
    "مور_إيتر_مور_كونسترينيد_باتشيس": "more_itertools.more.constrained_batches",
    "مور_إيتر_مور_كونسومير": "more_itertools.more.consumer",
    "مور_إيتر_مور_كونسيكوتيف_جراوبس": "more_itertools.more.consecutive_groups",
    "مور_إيتر_مور_كونكورينت_تي": "more_itertools.more.concurrent_tee",
    "مور_إيتر_مور_لستريب": "more_itertools.more.lstrip",
    "مور_إيتر_مور_لوكات": "more_itertools.more.locate",
    "مور_إيتر_مور_مارك_نهاية": "more_itertools.more.mark_ends",
    "مور_إيتر_مور_ماك_مزخرف": "more_itertools.more.make_decorator",
    "مور_إيتر_مور_مجموعة_القوى_من_سيتس": "more_itertools.more.powerset_of_sets",
    "مور_إيتر_مور_مشرّح": "more_itertools.more.sliced",
    "مور_إيتر_مور_مقطّع": "more_itertools.more.chunked",
    "مور_إيتر_مور_مقطّع_يفين": "more_itertools.more.chunked_even",
    "مور_إيتر_مور_مميز_تباديل": "more_itertools.more.distinct_permutations",
    "مور_إيتر_مور_مميز_توافيق": "more_itertools.more.distinct_combinations",
    "مور_إيتر_مور_مينماكس": "more_itertools.more.minmax",
    "مور_إيتر_مور_نوميريك_مدى": "more_itertools.more.numeric_range",
    "مور_إيتر_مور_نوميريك_مدى_عدد": "more_itertools.more.numeric_range.count",
    "مور_إيتر_مور_نوميريك_مدى_فهرس": "more_itertools.more.numeric_range.index",
    "مور_إيتر_مور_هل_مرتب": "more_itertools.more.is_sorted",
    "مور_إيتر_مور_واحد": "more_itertools.more.one",
    "مور_إيتر_مور_وقت_ليميتيد": "more_itertools.more.time_limited",
    "مور_إيتر_مور_ويث_تكرار": "more_itertools.more.with_iter",
    "مور_إيتر_مور_ويندويد": "more_itertools.more.windowed",
    "مور_إيتر_مور_ويندويد_كومبليت": "more_itertools.more.windowed_complete",
    "مور_إيتر_مور_يتشونكيد": "more_itertools.more.ichunked",
    "مور_إيتر_مور_يدفت": "more_itertools.more.idft",
    "مور_إيتر_مور_يكستراكت": "more_itertools.more.extract",
    "مور_إيتر_مور_يكوالس": "more_itertools.more.iequals",
}

MORE_ITERTOOLS_CONSTS = {
}

IMPORT_MODULES = ['more_itertools', 'more_itertools.more', 'more_itertools.recipes']
IMPORT_CHECK = r"(?<![\w.])(?:more_itertools)\."
IMPORT_STATEMENT = "import " + ", ".join(IMPORT_MODULES)

MORE_ITERTOOLS_HELP = [
    "# more_itertools - أدوات التكرار الإضافية من حزمة more_itertools",
]

_MORE_ITERTOOLS_TOKEN = re.compile(
    r"(?P<dot>\.)?"
    r"(?P<word>(?!\d)[\w\u064B-\u065F\u0670]+)"
    r"(?P<open>\s*\()?"
)

USER_NAMES = set()


def _more_itertools_replace(match):
    dot = match.group("dot")
    word = match.group("word")
    open_paren = match.group("open")
    if word in USER_NAMES:
        return match.group(0)
    if dot:
        return match.group(0)
    if word in MORE_ITERTOOLS_CONSTS:
        return MORE_ITERTOOLS_CONSTS[word]
    if word in MORE_ITERTOOLS_FUNCS:
        return MORE_ITERTOOLS_FUNCS[word] + (open_paren or "")
    return match.group(0)


def MORE_ITERTOOLS_SUBSTITUTE(text):
    """يترجم كلمات المكتبة في نص واحد ويُرجع المترجم."""
    if not text:
        return text
    return _MORE_ITERTOOLS_TOKEN.sub(_more_itertools_replace, text)

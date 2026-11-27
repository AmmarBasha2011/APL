"""مولّد تلقائياً — مكتبة optuna لـ APL.

تحسين المعلمات الفائقة.

كل الأسماء وُلّدت آلياً من معرّفات الحزمة الحقيقية optuna، وتُرجم كل اسم إلى مسار
Python كامل. كل عنصر يشير إلى كائن Python حقيقي فريد لا تغطّيه مكتبة أخرى،
والأسماء فريدة عبر كل مكتبات APL ونواة اللغة.
"""

import re

OPTUNA_FUNCS = {
    "أوبتونا_ارتيفاكتس_يكسيبتيونس_ارتيفاكت_نوت_فاوند": "optuna.artifacts.exceptions.ArtifactNotFound",
    "أوبتونا_تسجيل_إنشاء_افتراضي_فورماتير": "optuna.logging.create_default_formatter",
    "أوبتونا_تسجيل_جلب_فيربوسيتي": "optuna.logging.get_verbosity",
    "أوبتونا_تسجيل_جلب_لوجير": "optuna.logging.get_logger",
    "أوبتونا_تسجيل_ديسابل_افتراضي_هاندلير": "optuna.logging.disable_default_handler",
    "أوبتونا_تسجيل_ديسابل_بروباجاتيون": "optuna.logging.disable_propagation",
    "أوبتونا_تسجيل_ضبط_فيربوسيتي": "optuna.logging.set_verbosity",
    "أوبتونا_تسجيل_ينابل_افتراضي_هاندلير": "optuna.logging.enable_default_handler",
    "أوبتونا_تسجيل_ينابل_بروباجاتيون": "optuna.logging.enable_propagation",
    "أوبتونا_تيرميناتور_تيرميناتور_أساس_تيرميناتور": "optuna.terminator.terminator.BaseTerminator",
    "أوبتونا_تيرميناتور_تيرميناتور_أساس_تيرميناتور_شاولد_تيرمينات": "optuna.terminator.terminator.BaseTerminator.should_terminate",
    "أوبتونا_تيرميناتور_تيرميناتور_تيرميناتور": "optuna.terminator.terminator.Terminator",
    "أوبتونا_تيرميناتور_تيرميناتور_تيرميناتور_شاولد_تيرمينات": "optuna.terminator.terminator.Terminator.should_terminate",
    "أوبتونا_تيرميناتور_رد_نداء_تيرميناتور_رد_نداء": "optuna.terminator.callback.TerminatorCallback",
    "أوبتونا_تيرميناتور_وسيط_يروريفال_وسيط_خطأ_يفالواتور": "optuna.terminator.median_erroreval.MedianErrorEvaluator",
    "أوبتونا_تيرميناتور_وسيط_يروريفال_وسيط_خطأ_يفالواتور_يفالوات": "optuna.terminator.median_erroreval.MedianErrorEvaluator.evaluate",
    "أوبتونا_تيرميناتور_يروريفال_أساس_خطأ_يفالواتور": "optuna.terminator.erroreval.BaseErrorEvaluator",
    "أوبتونا_تيرميناتور_يروريفال_أساس_خطأ_يفالواتور_يفالوات": "optuna.terminator.erroreval.BaseErrorEvaluator.evaluate",
    "أوبتونا_تيرميناتور_يروريفال_ريبورت_كروس_فاليداتيون_سكوريس": "optuna.terminator.erroreval.report_cross_validation_scores",
    "أوبتونا_تيرميناتور_يروريفال_ستاتيك_خطأ_يفالواتور": "optuna.terminator.erroreval.StaticErrorEvaluator",
    "أوبتونا_تيرميناتور_يروريفال_ستاتيك_خطأ_يفالواتور_يفالوات": "optuna.terminator.erroreval.StaticErrorEvaluator.evaluate",
    "أوبتونا_تيرميناتور_يروريفال_كروس_فاليداتيون_خطأ_يفالواتور": "optuna.terminator.erroreval.CrossValidationErrorEvaluator",
    "أوبتونا_تيرميناتور_يروريفال_كروس_فاليداتيون_خطأ_يفالواتور_يفالوات": "optuna.terminator.erroreval.CrossValidationErrorEvaluator.evaluate",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يفالواتور_أساس_يمبروفيمينت_يفالواتور": "optuna.terminator.improvement.evaluator.BaseImprovementEvaluator",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يفالواتور_أساس_يمبروفيمينت_يفالواتور_يفالوات": "optuna.terminator.improvement.evaluator.BaseImprovementEvaluator.evaluate",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يفالواتور_بيست_قيمة_ستاجناتيون_يفالواتور": "optuna.terminator.improvement.evaluator.BestValueStagnationEvaluator",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يفالواتور_بيست_قيمة_ستاجناتيون_يفالواتور_يفالوات": "optuna.terminator.improvement.evaluator.BestValueStagnationEvaluator.evaluate",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يفالواتور_ريجريت_باوند_يفالواتور": "optuna.terminator.improvement.evaluator.RegretBoundEvaluator",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يفالواتور_ريجريت_باوند_يفالواتور_يفالوات": "optuna.terminator.improvement.evaluator.RegretBoundEvaluator.evaluate",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يمر_EMMR_يفالواتور": "optuna.terminator.improvement.emmr.EMMREvaluator",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يمر_EMMR_يفالواتور_يفالوات": "optuna.terminator.improvement.emmr.EMMREvaluator.evaluate",
    "أوبتونا_ديستريبوتيونس_أساس_ديستريبوتيون": "optuna.distributions.BaseDistribution",
    "أوبتونا_ديستريبوتيونس_أساس_ديستريبوتيون_إلى_يكستيرنال_ريبر": "optuna.distributions.BaseDistribution.to_external_repr",
    "أوبتونا_ديستريبوتيونس_أساس_ديستريبوتيون_إلى_ينتيرنال_ريبر": "optuna.distributions.BaseDistribution.to_internal_repr",
    "أوبتونا_ديستريبوتيونس_أساس_ديستريبوتيون_سينجل": "optuna.distributions.BaseDistribution.single",
    "أوبتونا_ديستريبوتيونس_تشيك_ديستريبوتيون_كومباتيبيليتي": "optuna.distributions.check_distribution_compatibility",
    "أوبتونا_ديستريبوتيونس_جسون_إلى_ديستريبوتيون": "optuna.distributions.json_to_distribution",
    "أوبتونا_ديستريبوتيونس_ديستريبوتيون_إلى_جسون": "optuna.distributions.distribution_to_json",
    "أوبتونا_ديستريبوتيونس_ديسكريت_ونيفورم_ديستريبوتيون": "optuna.distributions.DiscreteUniformDistribution",
    "أوبتونا_ديستريبوتيونس_سجل_ونيفورم_ديستريبوتيون": "optuna.distributions.LogUniformDistribution",
    "أوبتونا_ديستريبوتيونس_صحيح_ديستريبوتيون": "optuna.distributions.IntDistribution",
    "أوبتونا_ديستريبوتيونس_صحيح_ديستريبوتيون_إلى_يكستيرنال_ريبر": "optuna.distributions.IntDistribution.to_external_repr",
    "أوبتونا_ديستريبوتيونس_صحيح_ديستريبوتيون_إلى_ينتيرنال_ريبر": "optuna.distributions.IntDistribution.to_internal_repr",
    "أوبتونا_ديستريبوتيونس_صحيح_ديستريبوتيون_سينجل": "optuna.distributions.IntDistribution.single",
    "أوبتونا_ديستريبوتيونس_صحيح_سجل_ونيفورم_ديستريبوتيون": "optuna.distributions.IntLogUniformDistribution",
    "أوبتونا_ديستريبوتيونس_صحيح_ونيفورم_ديستريبوتيون": "optuna.distributions.IntUniformDistribution",
    "أوبتونا_ديستريبوتيونس_عشري_ديستريبوتيون": "optuna.distributions.FloatDistribution",
    "أوبتونا_ديستريبوتيونس_عشري_ديستريبوتيون_إلى_ينتيرنال_ريبر": "optuna.distributions.FloatDistribution.to_internal_repr",
    "أوبتونا_ديستريبوتيونس_عشري_ديستريبوتيون_سينجل": "optuna.distributions.FloatDistribution.single",
    "أوبتونا_ديستريبوتيونس_كاتيجوريكال_ديستريبوتيون": "optuna.distributions.CategoricalDistribution",
    "أوبتونا_ديستريبوتيونس_كاتيجوريكال_ديستريبوتيون_إلى_يكستيرنال_ريبر": "optuna.distributions.CategoricalDistribution.to_external_repr",
    "أوبتونا_ديستريبوتيونس_كاتيجوريكال_ديستريبوتيون_إلى_ينتيرنال_ريبر": "optuna.distributions.CategoricalDistribution.to_internal_repr",
    "أوبتونا_ديستريبوتيونس_كاتيجوريكال_ديستريبوتيون_سينجل": "optuna.distributions.CategoricalDistribution.single",
    "أوبتونا_ديستريبوتيونس_ونيفورم_ديستريبوتيون": "optuna.distributions.UniformDistribution",
    "أوبتونا_ستودي_ستودي_إنشاء_ستودي": "optuna.study.study.create_study",
    "أوبتونا_ستودي_ستودي_احذف_ستودي": "optuna.study.study.delete_study",
    "أوبتونا_ستودي_ستودي_انسخ_ستودي": "optuna.study.study.copy_study",
    "أوبتونا_ستودي_ستودي_جلب_كل_ستودي_سوماريس": "optuna.study.study.get_all_study_summaries",
    "أوبتونا_ستودي_ستودي_جلب_كل_ستودي_ناميس": "optuna.study.study.get_all_study_names",
    "أوبتونا_ستودي_ستودي_حمّل_ستودي": "optuna.study.study.load_study",
    "أوبتونا_ستودي_ستودي_ستودي": "optuna.study.study.Study",
    "أوبتونا_ستودي_ستودي_ستودي_أضف_تريال": "optuna.study.study.Study.add_trial",
    "أوبتونا_ستودي_ستودي_ستودي_أضف_تريالس": "optuna.study.study.Study.add_trials",
    "أوبتونا_ستودي_ستودي_ستودي_إيقاف": "optuna.study.study.Study.stop",
    "أوبتونا_ستودي_ستودي_ستودي_اسك": "optuna.study.study.Study.ask",
    "أوبتونا_ستودي_ستودي_ستودي_تريالس_داتافرام": "optuna.study.study.Study.trials_dataframe",
    "أوبتونا_ستودي_ستودي_ستودي_تيل": "optuna.study.study.Study.tell",
    "أوبتونا_ستودي_ستودي_ستودي_جلب_تريالس": "optuna.study.study.Study.get_trials",
    "أوبتونا_ستودي_ستودي_ستودي_ضبط_متري_ناميس": "optuna.study.study.Study.set_metric_names",
    "أوبتونا_ستودي_ستودي_ستودي_ضبط_وسير_اتر": "optuna.study.study.Study.set_user_attr",
    "أوبتونا_ستودي_ستودي_ستودي_وبتيميز": "optuna.study.study.Study.optimize",
    "أوبتونا_ستودي_ستودي_ستودي_ينكويوي_تريال": "optuna.study.study.Study.enqueue_trial",
    "أوبتونا_ستوراجيس_جلب_ستوراج": "optuna.storages.get_storage",
    "أوبتونا_سيرتش_سباك_تقاطع_تقاطع_سيرتش_سباك": "optuna.search_space.intersection.IntersectionSearchSpace",
    "أوبتونا_سيرتش_سباك_تقاطع_تقاطع_سيرتش_سباك_2": "optuna.search_space.intersection.intersection_search_space",
    "أوبتونا_سيرتش_سباك_تقاطع_تقاطع_سيرتش_سباك_كالكولات": "optuna.search_space.intersection.IntersectionSearchSpace.calculate",
    "أوبتونا_كلي_سيل_قيمة": "optuna.cli.CellValue",
    "أوبتونا_كلي_سيل_قيمة_جلب_نص": "optuna.cli.CellValue.get_string",
    "أوبتونا_كلي_سيل_قيمة_ويدث": "optuna.cli.CellValue.width",
    "أوبتونا_كلي_قيمة_نوع": "optuna.cli.ValueType",
    "أوبتونا_كلي_مين": "optuna.cli.main",
    "أوبتونا_يكسيبتيونس_CLI_وساج_خطأ": "optuna.exceptions.CLIUsageError",
    "أوبتونا_يكسيبتيونس_تريال_برونيد": "optuna.exceptions.TrialPruned",
    "أوبتونا_يكسيبتيونس_حدّث_فينيشيد_تريال_خطأ": "optuna.exceptions.UpdateFinishedTrialError",
    "أوبتونا_يكسيبتيونس_دوبليكاتيد_ستودي_خطأ": "optuna.exceptions.DuplicatedStudyError",
    "أوبتونا_يكسيبتيونس_ستوراج_ينتيرنال_خطأ": "optuna.exceptions.StorageInternalError",
    "أوبتونا_يكسيبتيونس_وبتونا_خطأ": "optuna.exceptions.OptunaError",
    "أوبتونا_يكسيبتيونس_يكسبيريمينتال_وارنينج": "optuna.exceptions.ExperimentalWarning",
    "أوبتونا_يمبورتانك_جلب_بارام_يمبورتانسيس": "optuna.importance.get_param_importances",
}

OPTUNA_CONSTS = {
    "أوبتونا_TYPE_تشيكينج": "optuna.TYPE_CHECKING",
    "أوبتونا_بروجريس_بار_TYPE_تشيكينج": "optuna.progress_bar.TYPE_CHECKING",
    "أوبتونا_برونيرس_TYPE_تشيكينج": "optuna.pruners.TYPE_CHECKING",
    "أوبتونا_تسجيل_DEBUG": "optuna.logging.DEBUG",
    "أوبتونا_تسجيل_ERROR": "optuna.logging.ERROR",
    "أوبتونا_تسجيل_FATAL": "optuna.logging.FATAL",
    "أوبتونا_تسجيل_INFO": "optuna.logging.INFO",
    "أوبتونا_تسجيل_WARN": "optuna.logging.WARN",
    "أوبتونا_تسجيل_كريتيكال": "optuna.logging.CRITICAL",
    "أوبتونا_تسجيل_وارنينج": "optuna.logging.WARNING",
    "أوبتونا_تيرميناتور_تيرميناتور_افتراضي_MIN_N_تريالس": "optuna.terminator.terminator.DEFAULT_MIN_N_TRIALS",
    "أوبتونا_تيرميناتور_رد_نداء_TYPE_تشيكينج": "optuna.terminator.callback.TYPE_CHECKING",
    "أوبتونا_تيرميناتور_وسيط_يروريفال_TYPE_تشيكينج": "optuna.terminator.median_erroreval.TYPE_CHECKING",
    "أوبتونا_تيرميناتور_يروريفال_TYPE_تشيكينج": "optuna.terminator.erroreval.TYPE_CHECKING",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يفالواتور_TYPE_تشيكينج": "optuna.terminator.improvement.evaluator.TYPE_CHECKING",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يفالواتور_افتراضي_MIN_N_تريالس": "optuna.terminator.improvement.evaluator.DEFAULT_MIN_N_TRIALS",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يفالواتور_افتراضي_TOP_تريالس_RATIO": "optuna.terminator.improvement.evaluator.DEFAULT_TOP_TRIALS_RATIO",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يمر_TYPE_تشيكينج": "optuna.terminator.improvement.emmr.TYPE_CHECKING",
    "أوبتونا_تيرميناتور_يمبروفيمينت_يمر_مارجين_FOR_نوماريكال_ستابيليتي": "optuna.terminator.improvement.emmr.MARGIN_FOR_NUMARICAL_STABILITY",
    "أوبتونا_ديستريبوتيونس_TYPE_تشيكينج": "optuna.distributions.TYPE_CHECKING",
    "أوبتونا_ستودي_ستودي_TYPE_تشيكينج": "optuna.study.study.TYPE_CHECKING",
    "أوبتونا_سيرتش_سباك_تقاطع_TYPE_تشيكينج": "optuna.search_space.intersection.TYPE_CHECKING",
    "أوبتونا_سيرتش_سباك_جمّع_ديكومبوسيد_TYPE_تشيكينج": "optuna.search_space.group_decomposed.TYPE_CHECKING",
    "أوبتونا_يمبورتانك_TYPE_تشيكينج": "optuna.importance.TYPE_CHECKING",
}

IMPORT_MODULES = ['optuna', 'optuna.artifacts.exceptions', 'optuna.cli', 'optuna.distributions', 'optuna.exceptions', 'optuna.importance', 'optuna.logging', 'optuna.progress_bar', 'optuna.pruners', 'optuna.search_space.group_decomposed', 'optuna.search_space.intersection', 'optuna.storages', 'optuna.study.study', 'optuna.terminator.callback', 'optuna.terminator.erroreval', 'optuna.terminator.improvement.emmr', 'optuna.terminator.improvement.evaluator', 'optuna.terminator.median_erroreval', 'optuna.terminator.terminator']
IMPORT_CHECK = r"(?<![\w.])(?:optuna)\."
IMPORT_STATEMENT = "import " + ", ".join(IMPORT_MODULES)

OPTUNA_HELP = [
    "# optuna - تحسين المعلمات الفائقة",
]

_OPTUNA_TOKEN = re.compile(
    r"(?P<dot>\.)?"
    r"(?P<word>(?!\d)[\w\u064B-\u065F\u0670]+)"
    r"(?P<open>\s*\()?"
)

USER_NAMES = set()


def _optuna_replace(match):
    dot = match.group("dot")
    word = match.group("word")
    open_paren = match.group("open")
    if word in USER_NAMES:
        return match.group(0)
    if dot:
        return match.group(0)
    if word in OPTUNA_CONSTS:
        return OPTUNA_CONSTS[word]
    if word in OPTUNA_FUNCS:
        return OPTUNA_FUNCS[word] + (open_paren or "")
    return match.group(0)


def OPTUNA_SUBSTITUTE(text):
    """يترجم كلمات المكتبة في نص واحد ويُرجع المترجم."""
    if not text:
        return text
    return _OPTUNA_TOKEN.sub(_optuna_replace, text)

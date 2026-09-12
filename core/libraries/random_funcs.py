"""
APL - Random Library Functions
Transpiles Arabic random keywords to Python random module calls
"""

RANDOM_FUNCS = {
    # أساسي
    "عشوائي_كسر": "random.random",
    "عشوائي_عائم": "random.uniform",
    "عشوائي_عدد": "random.randint",
    "عشوائي_خطوة": "random.randrange",
    "عشوائي": "random.choice",
    "عشوائي_أوزان": "random.choices",
    "عشوائي_عينة": "random.sample",
    "خلط": "random.shuffle",
    # توزيعات
    "عشوائي_طبيعي": "random.gauss",
    "عشوائي_متماثل": "random.normalvariate",
    "عشوائي_لوغ": "random.lognormvariate",
    "عشوائي_أسي": "random.expovariate",
    "عشوائي_فونميس": "random.vonmisesvariate",
    "عشوائي_جاما": "random.gammavariate",
    "عشوائي_بيتا": "random.betavariate",
    "عشوائي_باريتو": "random.paretovariate",
    "عشوائي_ويبول": "random.weibullvariate",
    # حالة
    "بذرة": "random.seed",
    "حالة_عشوائي": "random.getstate",
    "تعيين_حالة": "random.setstate",
}

RANDOM_PATTERN = r"(?<!\w)(" + "|".join(sorted(RANDOM_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
RANDOM_HELP = [
    "# عشوائي",
    "عشوائي_كسر            - random.random",
    "عشوائي_عائم           - random.uniform",
    "عشوائي_عدد            - random.randint",
    "عشوائي_خطوة           - random.randrange",
    "عشوائي               - random.choice",
    "عشوائي_أوزان          - random.choices",
    "عشوائي_عينة           - random.sample",
    "خلط                   - random.shuffle",
    "# توزيعات عشوائية",
    "عشوائي_طبيعي          - random.gauss",
    "عشوائي_متماثل         - random.normalvariate",
    "عشوائي_لوغ            - random.lognormvariate",
    "عشوائي_أسي            - random.expovariate",
    "عشوائي_فونميس        - random.vonmisesvariate",
    "عشوائي_جاما           - random.gammavariate",
    "عشوائي_بيتا           - random.betavariate",
    "عشوائي_باريتو         - random.paretovariate",
    "عشوائي_ويبول          - random.weibullvariate",
    "# حالة عشوائي",
    "بذرة                 - random.seed",
    "حالة_عشوائي           - random.getstate",
    "تعيين_حالة            - random.setstate",
]

# Import detection
IMPORT_NAME = "random"
IMPORT_CHECK = "random\."
IMPORT_STATEMENT = "import random"

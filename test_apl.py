import unittest
from apl import transpile

class TestAPL(unittest.TestCase):

    # ----- المتغير (Variable) -----
    def test_variable_string(self):
        code = 'المتغير اسم = "عمار"'
        self.assertEqual(transpile(code).strip(), 'اسم = "عمار"')

    def test_variable_number(self):
        code = "المتغير عمر = 25"
        self.assertEqual(transpile(code).strip(), "عمر = 25")

    def test_variable_expression(self):
        code = "المتغير ناتج = عمر + 5"
        self.assertEqual(transpile(code).strip(), "ناتج = عمر + 5")

    def test_indent_preserved(self):
        code = "    المتغير x = 5"
        self.assertEqual(transpile(code), "    x = 5")

    # ----- اطبع (Print) -----
    def test_print_string(self):
        code = 'اطبع "مرحبا"'
        self.assertEqual(transpile(code).strip(), 'print("مرحبا")')

    def test_print_variable(self):
        code = "اطبع(عمر)"
        self.assertEqual(transpile(code).strip(), "print(عمر)")

    def test_print_multi(self):
        code = 'اطبع "العمر:", ناتج'
        self.assertEqual(transpile(code).strip(), 'print("العمر:", ناتج)')

    # ----- ادخل (Input) -----
    def test_input_no_prompt(self):
        code = "المتغير x = ادخل()"
        self.assertEqual(transpile(code).strip(), "x = input()")

    def test_input_with_prompt(self):
        code = 'المتغير x = ادخل("الاسم: ")'
        self.assertEqual(transpile(code).strip(), 'x = input("الاسم: ")')

    # ----- لو / الا / الا لو (If/Else/Elif) -----
    def test_if(self):
        code = "لو x > 5:"
        self.assertEqual(transpile(code).strip(), "if x > 5:")

    def test_else(self):
        code = "الا:"
        self.assertEqual(transpile(code).strip(), "else:")

    def test_elif(self):
        code = "الا لو x == 5:"
        self.assertEqual(transpile(code).strip(), "elif x == 5:")

    def test_nested_if(self):
        code = ["المتغير x = 5", "لو x > 0:", '    اطبع "موجب"', "    الا:", '        اطبع "صفر أو سالب"']
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "x = 5")
        self.assertEqual(result[1].strip(), "if x > 0:")
        self.assertEqual(result[2].strip(), 'print("موجب")')
        self.assertEqual(result[3].strip(), "else:")

    # ----- طالما (While) -----
    def test_while(self):
        code = "طالما x < 10:"
        self.assertEqual(transpile(code).strip(), "while x < 10:")

    def test_while_with_body(self):
        code = ["المتغير x = 0", "طالما x < 3:", "    اطبع x", "    المتغير x = x + 1"]
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "x = 0")
        self.assertEqual(result[1].strip(), "while x < 3:")
        self.assertEqual(result[2].strip(), "print(x)")
        self.assertEqual(result[3].strip(), "x = x + 1")

    # ----- لكل (For) -----
    def test_for_in(self):
        code = "لكل i في نطاق(5):"
        self.assertEqual(transpile(code).strip(), "for i in range(5):")

    def test_for_in_list(self):
        code = 'لكل اسم في ["عمار", "علي"]:'
        result = transpile(code).strip()
        self.assertEqual(result, 'for اسم in ["عمار", "علي"]:')

    def test_for_with_body(self):
        code = ["لكل i في نطاق(3):", '    اطبع "رقم:", i']
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "for i in range(3):")
        self.assertEqual(result[1].strip(), 'print("رقم:", i)')

    # ----- دالة (Def) / ارجع (Return) -----
    def test_function_def(self):
        code = "دالة جمع(أ, ب):"
        self.assertEqual(transpile(code).strip(), "def جمع(أ, ب):")

    def test_function_with_body(self):
        code = ["دالة جمع(أ, ب):", "    ارجع أ + ب"]
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "def جمع(أ, ب):")
        self.assertEqual(result[1].strip(), "return أ + ب")

    def test_return_value(self):
        code = "ارجع أ + ب"
        self.assertEqual(transpile(code).strip(), "return أ + ب")

    def test_return_empty(self):
        code = "ارجع"
        self.assertEqual(transpile(code).strip(), "return")

    def test_full_function(self):
        code = [
            "دالة مضروب(ن):",
            "    لو ن <= 1:",
            "        ارجع 1",
            "    ارجع ن * مضروب(ن - 1)",
        ]
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "def مضروب(ن):")
        self.assertEqual(result[1].strip(), "if ن <= 1:")
        self.assertEqual(result[2].strip(), "return 1")
        self.assertEqual(result[3].strip(), "return ن * مضروب(ن - 1)")

    # ----- Type conversions -----
    def test_int_arabic(self):
        code = 'المتغير x = صحيح("5")'
        self.assertEqual(transpile(code).strip(), 'x = int("5")')

    def test_str_arabic(self):
        code = "المتغير x = نص(123)"
        self.assertEqual(transpile(code).strip(), "x = str(123)")

    def test_float_arabic(self):
        code = 'المتغير x = عشري("3.14")'
        self.assertEqual(transpile(code).strip(), 'x = float("3.14")')

    def test_bool_arabic(self):
        code = "المتغير x = منطق(1)"
        self.assertEqual(transpile(code).strip(), "x = bool(1)")

    def test_list_arabic(self):
        code = 'المتغير x = قائمة("abc")'
        self.assertEqual(transpile(code).strip(), 'x = list("abc")')

    def test_tuple_arabic(self):
        code = "المتغير x = مجموعة([1, 2, 3])"
        self.assertEqual(transpile(code).strip(), "x = tuple([1, 2, 3])")

    def test_set_arabic(self):
        code = "المتغير x = مصفوفة([1, 2, 2, 3])"
        self.assertEqual(transpile(code).strip(), "x = set([1, 2, 2, 3])")

    def test_dict_arabic(self):
        code = 'المتغير x = قاموس(اسم="عمار", عمر=25)'
        self.assertEqual(transpile(code).strip(), 'x = dict(اسم="عمار", عمر=25)')

    def test_type_in_print(self):
        code = 'اطبع نص(عمر)'
        self.assertEqual(transpile(code).strip(), 'print(str(عمر))')

    def test_type_in_expression(self):
        code = 'المتغير x = صحيح(ادخل("num: ")) + 5'
        self.assertEqual(transpile(code).strip(), 'x = int(input("num: ")) + 5')

    # ----- نطاق (range) / طول (len) -----
    def test_range(self):
        code = "المتغير x = نطاق(5)"
        self.assertEqual(transpile(code).strip(), "x = range(5)")

    def test_len(self):
        code = 'المتغير x = طول("مرحبا")'
        self.assertEqual(transpile(code).strip(), 'x = len("مرحبا")')

    def test_range_in_for(self):
        code = "لكل i في نطاق(طول(ق)):"
        result = transpile(code).strip()
        self.assertEqual(result, "for i in range(len(ق)):")

    # ----- Logical operators (و / أو / ليس) -----
    def test_and(self):
        code = "لو x > 0 و x < 10:"
        self.assertEqual(transpile(code).strip(), "if x > 0 and x < 10:")

    def test_or(self):
        code = "لو x == 0 أو y == 0:"
        self.assertEqual(transpile(code).strip(), "if x == 0 or y == 0:")

    def test_not(self):
        code = "لو ليس موجود:"
        self.assertEqual(transpile(code).strip(), "if not موجود:")

    def test_and_in_while(self):
        code = "طالما x > 0 و x < 10:"
        self.assertEqual(transpile(code).strip(), "while x > 0 and x < 10:")

    # ----- Constants (صواب / خطأ / لا_شيء) -----
    def test_true(self):
        code = "المتغير x = صواب"
        self.assertEqual(transpile(code).strip(), "x = True")

    def test_false(self):
        code = "المتغير x = خطأ"
        self.assertEqual(transpile(code).strip(), "x = False")

    def test_none(self):
        code = "المتغير x = لا_شيء"
        self.assertEqual(transpile(code).strip(), "x = None")

    def test_constants_in_condition(self):
        code = "المتغير x = صواب\nلو x:\n    اطبع x"
        result = transpile(code).split("\n")
        self.assertEqual(result[0].strip(), "x = True")
        self.assertEqual(result[1].strip(), "if x:")
        self.assertEqual(result[2].strip(), "print(x)")

    # ----- Edge cases -----
    def test_comment(self):
        code = "# تعليق"
        self.assertEqual(transpile(code).strip(), code)

    def test_empty_line(self):
        self.assertEqual(transpile(""), "")

    def test_python_passthrough(self):
        code = "print('hello')"
        self.assertEqual(transpile(code).strip(), code)

    def test_logical_in_variable(self):
        code = "المتغير x = أ و ب"
        self.assertEqual(transpile(code).strip(), "x = أ and ب")

    # ----- Break / Continue -----
    def test_break(self):
        code = "توقف"
        self.assertEqual(transpile(code).strip(), "break")

    def test_continue(self):
        code = "اكمل"
        self.assertEqual(transpile(code).strip(), "continue")

    def test_break_in_while(self):
        code = ["طالما صواب:", "    لو x > 10:", "        توقف"]
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "while True:")
        self.assertEqual(result[1].strip(), "if x > 10:")
        self.assertEqual(result[2].strip(), "break")

    # ----- Try / Except -----
    def test_try(self):
        code = "حاول:"
        self.assertEqual(transpile(code).strip(), "try:")

    def test_except(self):
        code = "إمسك:"
        self.assertEqual(transpile(code).strip(), "except:")

    def test_except_type(self):
        code = "إمسك ValueError:"
        self.assertEqual(transpile(code).strip(), "except ValueError:")

    def test_except_as(self):
        code = "إمسك ValueError مثل e:"
        self.assertEqual(transpile(code).strip(), "except ValueError as e:")

    def test_try_except(self):
        code = ["حاول:", "    المتغير x = صحيح(ادخل())", "إمسك ValueError:", "    اطبع 'رقم غير صحيح'"]

    # ----- Import -----
    def test_import(self):
        code = "استورد math"
        self.assertEqual(transpile(code).strip(), "import math")

    def test_import_as(self):
        code = "استورد math as m"
        self.assertEqual(transpile(code).strip(), "import math as m")

    def test_from_import(self):
        code = "من math استورد sqrt"
        self.assertEqual(transpile(code).strip(), "from math import sqrt")

    # ----- Math functions -----
    def test_abs(self):
        code = "المتغير x = مطلق(-5)"
        self.assertEqual(transpile(code).strip(), "x = abs(-5)")

    def test_pow(self):
        code = "المتغير x = قوة(2, 3)"
        self.assertEqual(transpile(code).strip(), "x = pow(2, 3)")

    def test_sqrt(self):
        code = "المتغير x = جذر(16)"
        result = transpile(code).strip()
        self.assertIn("x = math.sqrt(16)", result)

    def test_sqrt_auto_import(self):
        code = "المتغير x = جذر(16)"
        result = transpile(code)
        self.assertIn("import math", result)

    def test_max(self):
        code = "المتغير x = أكبر(1, 2, 3)"
        self.assertEqual(transpile(code).strip(), "x = max(1, 2, 3)")

    def test_min(self):
        code = "المتغير x = أصغر(1, 2, 3)"
        self.assertEqual(transpile(code).strip(), "x = min(1, 2, 3)")

    def test_round(self):
        code = "المتغير x = مقرب(3.7)"
        self.assertEqual(transpile(code).strip(), "x = round(3.7)")

    def test_sum(self):
        code = "المتغير x = مجموع([1, 2, 3])"
        self.assertEqual(transpile(code).strip(), "x = sum([1, 2, 3])")

    def test_sorted(self):
        code = "المتغير x = مفرز([3, 1, 2])"
        self.assertEqual(transpile(code).strip(), "x = sorted([3, 1, 2])")

    # ----- Method aliases -----
    def test_split(self):
        code = 'المتغير x = "أ ب ج".تقسيم(" ")'
        self.assertEqual(transpile(code).strip(), 'x = "أ ب ج".split(" ")')

    def test_append(self):
        code = "قائمة.أضف(5)"
        self.assertEqual(transpile(code).strip(), "قائمة.append(5)")

    def test_join(self):
        code = '" ".ضم(["أ", "ب"])'
        self.assertEqual(transpile(code).strip(), '" ".join(["أ", "ب"])')

    def test_pop(self):
        code = "قائمة.حذف()"
        self.assertEqual(transpile(code).strip(), "قائمة.pop()")

    def test_sort(self):
        code = "قائمة.فرز()"
        self.assertEqual(transpile(code).strip(), "قائمة.sort()")

    def test_reverse(self):
        code = "قائمة.عكس()"
        self.assertEqual(transpile(code).strip(), "قائمة.reverse()")

    def test_copy(self):
        code = "قائمة.نسخ()"
        self.assertEqual(transpile(code).strip(), "قائمة.copy()")

    def test_count(self):
        code = 'قائمة.عد(5)'
        self.assertEqual(transpile(code).strip(), 'قائمة.count(5)')

    def test_index(self):
        code = 'قائمة.بحث(5)'
        self.assertEqual(transpile(code).strip(), 'قائمة.index(5)')

    def test_remove(self):
        code = 'قائمة.أزل(5)'
        self.assertEqual(transpile(code).strip(), 'قائمة.remove(5)')

    def test_insert(self):
        code = 'قائمة.أدخل(0, 5)'
        self.assertEqual(transpile(code).strip(), 'قائمة.insert(0, 5)')

    def test_extend(self):
        code = 'قائمة.وسع([1, 2])'
        self.assertEqual(transpile(code).strip(), 'قائمة.extend([1, 2])')

    # ----- صنف (class) -----
    def test_class(self):
        code = "صنف شخص:"
        self.assertEqual(transpile(code).strip(), "class شخص:")

    def test_class_with_body(self):
        code = ["صنف شخص:", '    المتغير اسم = "عمار"', "    دالة __init__(ذات, ن):", "        ذات.اسم = ن"]
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "class شخص:")
        self.assertEqual(result[1].strip(), 'اسم = "عمار"')
        self.assertEqual(result[2].strip(), "def __init__(ذات, ن):")

    def test_pass(self):
        code = "تمرير"
        self.assertEqual(transpile(code).strip(), "pass")

    def test_class_with_pass(self):
        code = ["صنف فارغ:", "    تمرير"]
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "class فارغ:")
        self.assertEqual(result[1].strip(), "pass")

    # ----- خاص / عام (private / public) -----
    def test_private_var(self):
        code = "خاص المتغير x = 5"
        self.assertEqual(transpile(code).strip(), "__x = 5")

    def test_private_func(self):
        code = "خاص دالة اختباء():"
        self.assertEqual(transpile(code).strip(), "def __اختباء():")

    def test_public_var(self):
        code = "عام المتغير x = 5"
        self.assertEqual(transpile(code).strip(), "x = 5")

    def test_public_func(self):
        code = "عام دالة ظاهر():"
        self.assertEqual(transpile(code).strip(), "def ظاهر():")

    # ----- جسون / جسون_تحويل -----
    def test_json_parse(self):
        code = 'المتغير x = جسون(\'{"اسم": "عمار"}\')'
        result = transpile(code)
        self.assertIn('json.loads(', result)
        self.assertIn("import json", result)

    def test_json_dumps(self):
        code = 'المتغير x = جسون_تحويل({"اسم": "عمار"})'
        result = transpile(code)
        self.assertIn("json.dumps(", result)

    # ----- الساعة / التاريخ -----
    def test_datetime_now(self):
        code = "المتغير x = الساعة()"
        result = transpile(code)
        self.assertIn("datetime.datetime.now()", result)
        self.assertIn("import datetime", result)

    def test_date_today(self):
        code = "المتغير x = التاريخ()"
        result = transpile(code)
        self.assertIn("datetime.date.today()", result)

    # ----- فتح / اقرأ / اكتب / اغلق -----
    def test_open(self):
        code = 'المتغير f = فتح("test.txt", "w", ترميز="utf-8")'
        result = transpile(code).strip()
        self.assertEqual(result, 'f = open("test.txt", "w", encoding="utf-8")')

    def test_file_read(self):
        code = 'المتغير f = فتح("test.txt")\nالمتغير م = اقرأ(f)'
        result = transpile(code).split("\n")
        self.assertIn("_apl_read(f)", result[1].strip())

    def test_file_write(self):
        code = 'اكتب(f, "مرحبا")'
        self.assertIn("_apl_write(f,", transpile(code))

    def test_file_close(self):
        code = "اغلق(f)"
        self.assertIn("_apl_close(f)", transpile(code))

    # ----- طلب (HTTP request) -----
    def test_fetch(self):
        code = 'المتغير استجابة = طلب("https://example.com")'
        result = transpile(code)
        self.assertIn("_apl_fetch(", result)
        self.assertIn("urllib.request", result)

    # ----- احذف ملف / انشئ مجلد -----
    def test_delete_file(self):
        code = 'احذف ملف "test.txt"'
        result = transpile(code)
        self.assertIn('os.remove("test.txt")', result)
        self.assertIn("import os", result)

    def test_mkdir(self):
        code = 'انشئ مجلد "جديد"'
        result = transpile(code)
        self.assertIn('os.mkdir("جديد")', result)

    # ----- Arabic error message map -----
    def test_error_map_contains_keys(self):
        from apl import _get_error_ar
        e = ValueError("قيمة خاطئة")
        msg = _get_error_ar(e)
        self.assertIn("خطأ في القيمة", msg)

    def test_error_map_unknown(self):
        from apl import _get_error_ar
        e = RuntimeError("خطأ")
        msg = _get_error_ar(e)
        self.assertIn("خطأ في التشغيل", msg)

    def test_error_map_fallback(self):
        from apl import _get_error_ar
        e = Exception("خطأ عام")
        msg = _get_error_ar(e)
        self.assertIn("Exception", msg)

    # ----- Extra inline funcs edge cases -----
    def test_extra_funcs_in_expression(self):
        code = "المتغير x = جسون_تحويل(جسون(نص))"
        result = transpile(code)
        self.assertIn("json.dumps(json.loads(نص))", result)

    # ----- سهم (lambda) -----
    def test_lambda(self):
        code = "المتغير ضعف = سهم س: س * 2"
        result = transpile(code).strip()
        self.assertEqual(result, "ضعف = lambda س: س * 2")

    def test_lambda_multi_param(self):
        code = "المتغير جمع = سهم س, ص: س + ص"
        result = transpile(code).strip()
        self.assertEqual(result, "جمع = lambda س, ص: س + ص")

    # ----- Ternary (س إذا شرط والا ص) -----
    def test_ternary(self):
        code = "المتغير ن = 1 إذا صواب والا 0"
        result = transpile(code).strip()
        self.assertEqual(result, "ن = 1 if True else 0")

    def test_ternary_in_assign(self):
        code = "المتغير حالة = 'كبير' إذا عمر >= 18 والا 'صغير'"
        result = transpile(code).strip()
        self.assertIn("if", result)
        self.assertIn("else", result)

    # ----- حالة/قيمة/افتراضي (match/case) -----
    def test_match(self):
        code = "حالة اختيار:"
        self.assertEqual(transpile(code).strip(), "match اختيار:")

    def test_case_value(self):
        code = "قيمة 1:"
        self.assertEqual(transpile(code).strip(), "case 1:")

    def test_case_default(self):
        code = "افتراضي:"
        self.assertEqual(transpile(code).strip(), "case _:")

    def test_match_block(self):
        code = ["حالة اختيار:", "    قيمة 1:", '        اطبع "واحد"', "    قيمة 2:", '        اطبع "اثنان"', "    افتراضي:", '        اطبع "غير معروف"']
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "match اختيار:")
        self.assertEqual(result[1].strip(), "case 1:")
        self.assertEqual(result[3].strip(), "case 2:")
        self.assertEqual(result[5].strip(), "case _:")

    # ----- مع..مثل (with..as) -----
    def test_with_as(self):
        code = 'مع فتح("f.txt") مثل f:'
        result = transpile(code).strip()
        self.assertEqual(result, 'with open("f.txt") as f:')

    def test_with_as_encoding(self):
        code = 'مع فتح("f.txt", "w", ترميز="utf-8") مثل f:'
        result = transpile(code).strip()
        self.assertIn("with open(", result)
        self.assertIn("as f:", result)

    # ----- قاعدة (class alias) -----
    def test_qaeda(self):
        code = "قاعدة شخص:"
        self.assertEqual(transpile(code).strip(), "class شخص:")

    def test_qaeda_inherit(self):
        code = "قاعدة طالب(شخص):"
        self.assertEqual(transpile(code).strip(), "class طالب(شخص):")

    # ----- مولد (yield) -----
    def test_yield(self):
        code = "مولد س"
        self.assertEqual(transpile(code).strip(), "yield س")

    def test_yield_empty(self):
        code = "مولد"
        self.assertEqual(transpile(code).strip(), "yield")

    def test_yield_in_function(self):
        code = ["دالة مولد_ارقام():", "    المتغير i = 0", "    طالما i < 5:", "        مولد i", "        المتغير i = i + 1"]
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "def مولد_ارقام():")
        self.assertEqual(result[3].strip(), "yield i")

    # ----- حذف (del) -----
    def test_del(self):
        code = "حذف س"
        self.assertEqual(transpile(code).strip(), "del س")

    def test_del_item(self):
        code = "حذف قائمة[0]"
        self.assertEqual(transpile(code).strip(), "del قائمة[0]")

    # ----- أبدا (while True) -----
    def test_abda(self):
        code = "أبدا:"
        self.assertEqual(transpile(code).strip(), "while True:")

    def test_abda_with_body(self):
        code = ["أبدا:", "    اطبع 'حلقة'"]
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "while True:")
        self.assertEqual(result[1].strip(), "print('حلقة')")

    # ----- كل/أي/خريطة/فلترة/تجميع (all/any/map/filter/zip) -----
    def test_all_func(self):
        code = "المتغير x = كل([صواب, خطأ])"
        result = transpile(code).strip()
        self.assertEqual(result, "x = all([True, False])")

    def test_any_func(self):
        code = "المتغير x = أي([صواب, خطأ])"
        self.assertEqual(transpile(code).strip(), "x = any([True, False])")

    def test_map_func(self):
        code = "المتغير x = خريطة(دالة, قائمة)"
        self.assertEqual(transpile(code).strip(), "x = map(دالة, قائمة)")

    def test_filter_func(self):
        code = "المتغير x = فلترة(دالة, قائمة)"
        self.assertEqual(transpile(code).strip(), "x = filter(دالة, قائمة)")

    def test_zip_func(self):
        code = "المتغير x = تجميع(ق1, ق2)"
        self.assertEqual(transpile(code).strip(), "x = zip(ق1, ق2)")

    # ----- عشوائي (random.choice) -----
    def test_random_choice(self):
        code = 'المتغير x = عشوائي(["أ", "ب", "ج"])'
        result = transpile(code)
        self.assertIn("random.choice(", result)
        self.assertIn("import random", result)

    # ----- نوع (type) -----
    def test_type_func(self):
        code = "المتغير x = نوع(5)"
        self.assertEqual(transpile(code).strip(), "x = type(5)")

    # ----- عدد (enumerate) -----
    def test_enumerate_func(self):
        code = "لكل i, v في عدد(قائمة):"
        result = transpile(code).strip()
        self.assertEqual(result, "for i, v in enumerate(قائمة):")

    # ----- اطبع_بدون (print without newline) -----
    def test_print_no_newline(self):
        code = 'اطبع_بدون "مرحبا"'
        result = transpile(code).strip()
        self.assertEqual(result, 'print("مرحبا", end=\'\')')

    def test_print_no_newline_parens(self):
        code = 'اطبع_بدون("مرحبا")'
        result = transpile(code).strip()
        self.assertEqual(result, 'print("مرحبا", end=\'\')')


    # ----- String methods -----
    def test_replace(self):
        code = '"abc".استبدال("a", "z")'
        self.assertEqual(transpile(code).strip(), '"abc".replace("a", "z")')

    def test_upper(self):
        code = '"abc".علوي()'
        self.assertEqual(transpile(code).strip(), '"abc".upper()')

    def test_lower(self):
        code = '"ABC".سفلي()'
        self.assertEqual(transpile(code).strip(), '"ABC".lower()')

    def test_startswith(self):
        code = '"abc".بداية("a")'
        self.assertEqual(transpile(code).strip(), '"abc".startswith("a")')

    def test_endswith(self):
        code = '"abc".نهاية("c")'
        self.assertEqual(transpile(code).strip(), '"abc".endswith("c")')

    def test_strip(self):
        code = '" a ".تقليم()'
        self.assertEqual(transpile(code).strip(), '" a ".strip()')

    # ----- Set methods -----
    def test_union(self):
        code = "ق1.اتحاد(ق2)"
        self.assertEqual(transpile(code).strip(), "ق1.union(ق2)")

    def test_intersection(self):
        code = "ق1.تقاطع(ق2)"
        self.assertEqual(transpile(code).strip(), "ق1.intersection(ق2)")

    def test_difference(self):
        code = "ق1.فرق(ق2)"
        self.assertEqual(transpile(code).strip(), "ق1.difference(ق2)")

    # ----- في (in) -----
    def test_membership_in(self):
        code = "لو 5 في قائمة:"
        self.assertEqual(transpile(code).strip(), "if 5 in قائمة:")

    def test_membership_not_in(self):
        code = "لو 5 ليس في قائمة:"
        result = transpile(code).strip()
        self.assertEqual(result, "if 5 not in قائمة:")

    # ----- ط / ه (math.pi / math.e) -----
    def test_pi(self):
        code = "المتغير x = ط"
        result = transpile(code)
        self.assertIn("math.pi", result)
        self.assertIn("import math", result)

    def test_e(self):
        code = "المتغير x = ه"
        result = transpile(code)
        self.assertIn("math.e", result)

    # ----- انتظر / وقت (time.sleep / time.time) -----
    def test_sleep(self):
        code = "انتظر(1.5)"
        result = transpile(code)
        self.assertIn("time.sleep(1.5)", result)
        self.assertIn("import time", result)

    def test_time(self):
        code = "المتغير t = وقت()"
        result = transpile(code)
        self.assertIn("time.time()", result)

    # ----- تمثيل / ثنائي / سداسي / ترتيب / رمز -----
    def test_repr(self):
        code = "المتغير x = تمثيل('abc')"
        self.assertEqual(transpile(code).strip(), "x = repr('abc')")

    def test_bin(self):
        code = "المتغير x = ثنائي(10)"
        self.assertEqual(transpile(code).strip(), "x = bin(10)")

    def test_hex(self):
        code = "المتغير x = سداسي(255)"
        self.assertEqual(transpile(code).strip(), "x = hex(255)")

    def test_ord(self):
        code = "المتغير x = ترتيب('أ')"
        self.assertEqual(transpile(code).strip(), "x = ord('أ')")

    def test_chr(self):
        code = "المتغير x = رمز(65)"
        self.assertEqual(transpile(code).strip(), "x = chr(65)")

    # ----- اخرج (exit) -----
    def test_exit_stmt(self):
        code = "اخرج"
        self.assertEqual(transpile(code).strip(), "exit()")

    def test_exit_stmt_code(self):
        code = "اخرج 0"
        self.assertEqual(transpile(code).strip(), "exit(0)")

    def test_exit_inline(self):
        code = "اخرج(1)"
        self.assertEqual(transpile(code).strip(), "exit(1)")

    # ----- من (isinstance) -----
    def test_isinstance(self):
        code = "المتغير x = من(س, صحيح)"
        self.assertEqual(transpile(code).strip(), "x = isinstance(س, int)")

    # ----- تأكد (assert) -----
    def test_assert(self):
        code = "تأكد س > 0"
        self.assertEqual(transpile(code).strip(), "assert س > 0")

    def test_assert_message(self):
        code = "تأكد(س > 0, 'خطأ')"
        result = transpile(code).strip()
        self.assertIn("assert", result)

    def test_assert_with_parens(self):
        code = "تأكد(س > 0)"
        self.assertEqual(transpile(code).strip(), "assert س > 0")

    # ----- خاصية / محدد / محدد_حذف (decorators) -----
    def test_property(self):
        code = "خاصية"
        self.assertEqual(transpile(code).strip(), "@property")

    def test_setter(self):
        code = "محدد اسم"
        self.assertEqual(transpile(code).strip(), "@اسم.setter")

    def test_deleter(self):
        code = "محدد_حذف اسم"
        self.assertEqual(transpile(code).strip(), "@اسم.deleter")

    def test_property_with_function(self):
        code = ["خاصية", "دالة اسم(ذات):", "    ارجع ذات._اسم"]
        result = transpile("\n".join(code)).split("\n")
        self.assertEqual(result[0].strip(), "@property")
        self.assertEqual(result[1].strip(), "def اسم(ذات):")

    # ----- نسخ ملف / نقل ملف / حجم ملف / قائمة ملفات -----
    def test_copy_file(self):
        code = 'نسخ ملف "a.txt" إلى "b.txt"'
        result = transpile(code)
        self.assertIn("shutil.copy(", result)
        self.assertIn("import shutil", result)

    def test_move_file(self):
        code = 'نقل ملف "a.txt" إلى "b.txt"'
        result = transpile(code)
        self.assertIn("shutil.move(", result)

    def test_file_size(self):
        code = 'المتغير x = حجم_ملف("a.txt")'
        result = transpile(code).strip()
        self.assertIn("os.path.getsize(", result)

    def test_list_dir(self):
        code = 'المتغير x = قائمة_ملفات(".")'
        result = transpile(code).strip()
        self.assertIn("os.listdir(", result)

    # ----- Edge: في not breaking لكل -----
    def test_for_in_still_works(self):
        code = "لكل i في نطاق(5):"
        self.assertEqual(transpile(code).strip(), "for i in range(5):")


if __name__ == "__main__":
    unittest.main()

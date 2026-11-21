"""
APL - UnitTest Library
Full unittest wrapper with Arabic keywords
"""

UNITTEST_FUNCS = {
    # TestCase
    "حالة_اختبار": "unittest.TestCase",
    "أنشئ_اختبار": "unittest.TestCase",
    "حالة_اختبار": "unittest.TestCase",
    
    # Test fixtures
    "setUp": "setUp",
    "tearDown": "tearDown",
    "setUpClass": "setUpClass",
    "tearDownClass": "tearDownClass",
    
    # Assertions - مقارنات
    "assertEqual": "assertEqual",
    "assertNotEqual": "assertNotEqual",
    "assertTrue": "assertTrue",
    "assertFalse": "assertFalse",
    "assertIs": "assertIs",
    "assertIsNot": "assertIsNot",
    "assertIsNone": "assertIsNone",
    "assertIsNotNone": "assertIsNotNone",
    "assertIn": "assertIn",
    "assertNotIn": "assertNotIn",
    "assertIsInstance": "assertIsInstance",
    "assertNotIsInstance": "assertNotIsInstance",
    "assertRaises": "assertRaises",
    "assertRaisesRegex": "assertRaisesRegex",
    "assertWarns": "assertWarns",
    "assertWarnsRegex": "assertWarnsRegex",
    "assertLogs": "assertLogs",
    "assertAlmostEqual": "assertAlmostEqual",
    "assertNotAlmostEqual": "assertNotAlmostEqual",
    "assertGreater": "assertGreater",
    "assertGreaterEqual": "assertGreaterEqual",
    "assertLess": "assertLess",
    "assertLessEqual": "assertLessEqual",
    "assertRegex": "assertRegex",
    "assertNotRegex": "assertNotRegex",
    "assertCountEqual": "assertCountEqual",
    "assertMultiLineEqual": "assertMultiLineEqual",
    "assertSequenceEqual": "assertSequenceEqual",
    "assertListEqual": "assertListEqual",
    "assertTupleEqual": "assertTupleEqual",
    "assertSetEqual": "assertSetEqual",
    "assertDictEqual": "assertDictEqual",
    
    # Arabic aliases - تسميات عربية
    "ساوي": "assertEqual",
    "لا_ساوي": "assertNotEqual",
    "تأكيد": "assertTrue",
    "خطأ_اختبار": "assertFalse",
    "هو": "assertIs",
    "ليس": "assertIsNot",
    "لا_شيء": "assertIsNone",
    "ليس_لا_شيء": "assertIsNotNone",
    "في_اختبار": "assertIn",
    "ليس_في": "assertNotIn",
    "من_نوع": "assertIsInstance",
    "ليس_من_نوع": "assertNotIsInstance",
    "يرفع": "assertRaises",
    "يرفع_نمط": "assertRaisesRegex",
    "يحذر": "assertWarns",
    "يحذر_نمط": "assertWarnsRegex",
    "يسجل": "assertLogs",
    "تقريبا": "assertAlmostEqual",
    "ليس_تقريبا": "assertNotAlmostEqual",
    "أكبر_اختبار": "assertGreater",
    "أكبر_أو_يساوي": "assertGreaterEqual",
    "أصغر_اختبار": "assertLess",
    "أصغر_أو_يساوي": "assertLessEqual",
    "يطابق_نمط": "assertRegex",
    "لا_يطابق_نمط": "assertNotRegex",
    "نفس_العدد": "assertCountEqual",
    "نفس_السطر": "assertMultiLineEqual",
    "نفس_التسلسل": "assertSequenceEqual",
    "نفس_القائمة": "assertListEqual",
    "نفس_الصف": "assertTupleEqual",
    "نفس_المجموعة": "assertSetEqual",
    "نفس_القاموس": "assertDictEqual",
    
    # Test Suite
    "مجموعة_اختبارات": "unittest.TestSuite",
    "أضف_اختبار": "testSuite.addTest",
    
    # Test Runner
    "شغل_اختبارات": "unittest.TextTestRunner",
    "نفذ_اختبار": "testRunner.run",
    
    # Main
    "رئيسي": "unittest.main",
    
    # Skip
    "تخطى": "unittest.skip",
    "تخطى_إذا": "unittest.skipIf",
    "تخطى_ما_لم": "unittest.skipUnless",
    "فشل_متوقع": "unittest.expectedFailure",
    
    # Mock (if available)
    "mock": "unittest.mock",
    "Mock": "unittest.mock.Mock",
    "MagicMock": "unittest.mock.MagicMock",
    "تصحيح_اختبار": "unittest.mock.patch",
    "patch.object": "unittest.mock.patch.object",
}

UNITTEST_PATTERN = r"(?<![\w.\u0600-\u06FF])(" + "|".join(sorted(UNITTEST_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

UNITTEST_HELP = [
    "# === TestCase ===",
    "حالة_اختبار             - فئة حالة_اختبار",
    "أنشئ_اختبار             - إنشاء حالة_اختبار",
    "setUp                    - قبل كل حالة_اختبار",
    "tearDown                 - بعد كل حالة_اختبار",
    "# === Assertions ===",
    "ساوي(أ, ب)               - تأكد من المساواة",
    "لا_ساوي(أ, ب)            - تأكد من عدم المساواة",
    "صحيح(تعبير)             - تأكد من الصحة",
    "خطأ_اختبار(تعبير)              - تأكد من الخطأ",
    "لا_شيء(قيمة)            - تأكد من كونها None",
    "في_اختبار(عنصر, تسلسل)         - تأكد من الانتماء",
    "من_نوع(كائن, نوع)       - تأكد من النوع",
    "يرفع(استثناء, دالة)     - تأكد من رفع الاستثناء",
    "أكبر_اختبار(أ, ب)               - تأكد من أكبر_اختبار",
    "أصغر_اختبار(أ, ب)               - تأكد من أصغر_اختبار",
    "تقريبا(أ, ب)            - تأكد من التقريب",
    "يطابق_نمط(نص, نمط)      - تأكد من النمط",
]

IMPORT_NAME = "unittest"
IMPORT_CHECK = "unittest\."
IMPORT_STATEMENT = "import unittest"

# مكتبة الاختبارات — `unittest`

مكتبة unittest الكاملة بالعربي، اختبارات الوحدة:

**81 عنصراً عربياً** (الدوال: 84).

## الدوال (81)

| العربي | Python |
|--------|--------|
| `setUp` | `setUp` |
| `tearDown` | `tearDown` |
| `setUpClass` | `setUpClass` |
| `tearDownClass` | `tearDownClass` |
| `assertEqual` | `assertEqual` |
| `assertNotEqual` | `assertNotEqual` |
| `assertTrue` | `assertTrue` |
| `assertFalse` | `assertFalse` |
| `assertIs` | `assertIs` |
| `assertIsNot` | `assertIsNot` |
| `assertIsNone` | `assertIsNone` |
| `assertIsNotNone` | `assertIsNotNone` |
| `assertIn` | `assertIn` |
| `assertNotIn` | `assertNotIn` |
| `assertIsInstance` | `assertIsInstance` |
| `assertNotIsInstance` | `assertNotIsInstance` |
| `assertRaises` | `assertRaises` |
| `assertRaisesRegex` | `assertRaisesRegex` |
| `assertWarns` | `assertWarns` |
| `assertWarnsRegex` | `assertWarnsRegex` |
| `assertLogs` | `assertLogs` |
| `assertAlmostEqual` | `assertAlmostEqual` |
| `assertNotAlmostEqual` | `assertNotAlmostEqual` |
| `assertGreater` | `assertGreater` |
| `assertGreaterEqual` | `assertGreaterEqual` |
| `assertLess` | `assertLess` |
| `assertLessEqual` | `assertLessEqual` |
| `assertRegex` | `assertRegex` |
| `assertNotRegex` | `assertNotRegex` |
| `assertCountEqual` | `assertCountEqual` |
| `assertMultiLineEqual` | `assertMultiLineEqual` |
| `assertSequenceEqual` | `assertSequenceEqual` |
| `assertListEqual` | `assertListEqual` |
| `assertTupleEqual` | `assertTupleEqual` |
| `assertSetEqual` | `assertSetEqual` |
| `assertDictEqual` | `assertDictEqual` |
| `ساوي` | `assertEqual` |
| `لا_ساوي` | `assertNotEqual` |
| `تأكيد` | `assertTrue` |
| `خطأ_اختبار` | `assertFalse` |
| `هو` | `assertIs` |
| `ليس` | `assertIsNot` |
| `لا_شيء` | `assertIsNone` |
| `ليس_لا_شيء` | `assertIsNotNone` |
| `في_اختبار` | `assertIn` |
| `ليس_في` | `assertNotIn` |
| `من_نوع` | `assertIsInstance` |
| `ليس_من_نوع` | `assertNotIsInstance` |
| `يرفع` | `assertRaises` |
| `يرفع_نمط` | `assertRaisesRegex` |
| `يحذر` | `assertWarns` |
| `يحذر_نمط` | `assertWarnsRegex` |
| `يسجل` | `assertLogs` |
| `تقريبا` | `assertAlmostEqual` |
| `ليس_تقريبا` | `assertNotAlmostEqual` |
| `أكبر_اختبار` | `assertGreater` |
| `أكبر_أو_يساوي` | `assertGreaterEqual` |
| `أصغر_اختبار` | `assertLess` |
| `أصغر_أو_يساوي` | `assertLessEqual` |
| `يطابق_نمط` | `assertRegex` |
| `لا_يطابق_نمط` | `assertNotRegex` |
| `نفس_العدد` | `assertCountEqual` |
| `نفس_السطر` | `assertMultiLineEqual` |
| `نفس_التسلسل` | `assertSequenceEqual` |
| `نفس_القائمة` | `assertListEqual` |
| `نفس_الصف` | `assertTupleEqual` |
| `نفس_المجموعة` | `assertSetEqual` |
| `نفس_القاموس` | `assertDictEqual` |
| `أضف_اختبار` | `testSuite.addTest` |
| `شغل_اختبارات` | `unittest.TextTestRunner` |
| `نفذ_اختبار` | `testRunner.run` |
| `رئيسي` | `unittest.main` |
| `تخطى` | `unittest.skip` |
| `تخطى_إذا` | `unittest.skipIf` |
| `تخطى_ما_لم` | `unittest.skipUnless` |
| `فشل_متوقع` | `unittest.expectedFailure` |
| `mock` | `unittest.mock` |
| `Mock` | `unittest.mock.Mock` |
| `MagicMock` | `unittest.mock.MagicMock` |
| `تصحيح_اختبار` | `unittest.mock.patch` |
| `patch.object` | `unittest.mock.patch.object` |

## مثال

```apl
import unittest

صنف TestMath(unittest.TestCase):
    دالة setUp(ذات):
        ذات.س = 10
        ذات.ص = 20

    دالة test_جمع(ذات):
        ذات.assertEqual(ذات.س + ذات.ص, 30)

    دالة test_ضرب(ذات):
        ذات.assertEqual(ذات.س * ذات.ص, 200)

المتغير حزمة = unittest.TestLoader().loadTestsFromTestCase(TestMath)
unittest.TextTestRunner(verbosity=2).run(حزمة)
```

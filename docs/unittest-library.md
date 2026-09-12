# مكتبة الاختبارات — `unittest`

مكتبة unittest الكاملة بالعربي، اختبارات الوحدة:

## TestCase

| العربي | Python | الوصف |
|--------|--------|-------|
| `حالة_اختبار()` | `unittest.TestCase()` | فئة اختبار |
| `أنشئ_اختبار()` | `unittest.TestCase()` | إنشاء اختبار |
| `اختبار()` | `unittest.TestCase()` | اختبار |
| `setUp()` | `setUp()` | قبل كل اختبار |
| `tearDown()` | `tearDown()` | بعد كل اختبار |
| `setUpClass()` | `setUpClass()` | قبل الفئة |
| `tearDownClass()` | `tearDownClass()` | بعد الفئة |

## التأكيدات الأساسية (Basic Assertions)

| العربي | Python | الوصف |
|--------|--------|-------|
| `assertEqual(أ, ب)` | `assertEqual(أ, ب)` | تأكد من المساواة |
| `assertNotEqual(أ, ب)` | `assertNotEqual(أ, ب)` | تأكد من عدم المساواة |
| `assertTrue(تعبير)` | `assertTrue(تعبير)` | تأكد من الصحة |
| `assertFalse(تعبير)` | `assertFalse(تعبير)` | تأكد من الخطأ |
| `assertIs(أ, ب)` | `assertIs(أ, ب)` | تأكد من الهوية |
| `assertIsNot(أ, ب)` | `assertIsNot(أ, ب)` | تأكد من عدم الهوية |
| `assertIsNone(قيمة)` | `assertIsNone(قيمة)` | تأكد من None |
| `assertIsNotNone(قيمة)` | `assertIsNotNone(قيمة)` | تأكد من عدم None |
| `assertIn(عنصر, تسلسل)` | `assertIn(عنصر, تسلسل)` | تأكد من الانتماء |
| `assertNotIn(عنصر, تسلسل)` | `assertNotIn(عنصر, تسلسل)` | تأكد من عدم الانتماء |
| `assertIsInstance(كائن, نوع)` | `assertIsInstance(كائن, نوع)` | تأكد من النوع |
| `assertNotIsInstance(كائن, نوع)` | `assertNotIsInstance(كائن, نوع)` | تأكد من عدم النوع |
| `assertRaises(استثناء, دالة)` | `assertRaises(استثناء, دالة)` | تأكد من رفع الاستثناء |
| `assertRaisesRegex(استثناء, نمط, دالة)` | `assertRaisesRegex(استثناء, نمط, دالة)` | تأكد من رفع استثناء مع نمط |
| `assertWarns(تحذير, دالة)` | `assertWarns(تحذير, دالة)` | تأكد من التحذير |
| `assertLogs(مسجل, مستوى)` | `assertLogs(مسجل, مستوى)` | تأكد من السجلات |

## التأكيدات العددية (Numeric Assertions)

| العربي | Python | الوصف |
|--------|--------|-------|
| `assertAlmostEqual(أ, ب)` | `assertAlmostEqual(أ, ب)` | تأكد من التقريب |
| `assertNotAlmostEqual(أ, ب)` | `assertNotAlmostEqual(أ, ب)` | تأكد من عدم التقريب |
| `assertGreater(أ, ب)` | `assertGreater(أ, ب)` | تأكد من أكبر |
| `assertGreaterEqual(أ, ب)` | `assertGreaterEqual(أ, ب)` | تأكد من أكبر أو يساوي |
| `assertLess(أ, ب)` | `assertLess(أ, ب)` | تأكد من أصغر |
| `assertLessEqual(أ, ب)` | `assertLessEqual(أ, ب)` | تأكد من أصغر أو يساوي |

## التأكيدات النصية (String Assertions)

| العربي | Python | الوصف |
|--------|--------|-------|
| `assertRegex(نص, نمط)` | `assertRegex(نص, نمط)` | تأكد من النمط |
| `assertNotRegex(نص, نمط)` | `assertNotRegex(نص, نمط)` | تأكد من عدم النمط |
| `assertMultiLineEqual(أول, ثاني)` | `assertMultiLineEqual(أول, ثاني)` | تأكد من مساواة متعدد الأسطر |

## التأكيدات على المجموعات (Collection Assertions)

| العربي | Python | الوصف |
|--------|--------|-------|
| `assertCountEqual(أول, ثاني)` | `assertCountEqual(أول, ثاني)` | تأكد من نفس العدد |
| `assertSequenceEqual(أول, ثاني)` | `assertSequenceEqual(أول, ثاني)` | تأكد من نفس التسلسل |
| `assertListEqual(أول, ثاني)` | `assertListEqual(أول, ثاني)` | تأكد من نفس القائمة |
| `assertTupleEqual(أول, ثاني)` | `assertTupleEqual(أول, ثاني)` | تأكد من نفس الصف |
| `assertSetEqual(أول, ثاني)` | `assertSetEqual(أول, ثاني)` | تأكد من نفس المجموعة |
| `assertDictEqual(أول, ثاني)` | `assertDictEqual(أول, ثاني)` | تأكد من نفس القاموس |

## التسميات العربية (Arabic Aliases)

| العربي | Python |
|--------|--------|
| `ساوي(أ, ب)` | assertEqual |
| `لا_ساوي(أ, ب)` | assertNotEqual |
| `صحيح(تعبير)` | assertTrue |
| `خطأ(تعبير)` | assertFalse |
| `هو(أ, ب)` | assertIs |
| `ليس(أ, ب)` | assertIsNot |
| `لا_شيء(قيمة)` | assertIsNone |
| `ليس_لا_شيء(قيمة)` | assertIsNotNone |
| `في(عنصر, تسلسل)` | assertIn |
| `ليس_في(عنصر, تسلسل)` | assertNotIn |
| `من_نوع(كائن, نوع)` | assertIsInstance |
| `ليس_من_نوع(كائن, نوع)` | assertNotIsInstance |
| `يرفع(استثناء, دالة)` | assertRaises |
| `يحذر(تحذير, دالة)` | assertWarns |
| `يسجل(مسجل, مستوى)` | assertLogs |
| `تقريبا(أ, ب)` | assertAlmostEqual |
| `أكبر(أ, ب)` | assertGreater |
| `أصغر(أ, ب)` | assertLess |
| `أكبر_أو_يساوي(أ, ب)` | assertGreaterEqual |
| `أصغر_أو_يساوي(أ, ب)` | assertLessEqual |
| `يطابق_نمط(نص, نمط)` | assertRegex |
| `نفس_العدد(أول, ثاني)` | assertCountEqual |
| `نفس_القائمة(أول, ثاني)` | assertListEqual |
| `نفس_القاموس(أول, ثاني)` | assertDictEqual |

## Test Suite

| العربي | Python | الوصف |
|--------|--------|-------|
| `مجموعة_اختبارات()` | `unittest.TestSuite()` | إنشاء مجموعة اختبارات |
| `أضف_اختبار(اختبار)` | `testSuite.addTest(اختبار)` | إضافة اختبار |

## Test Runner

| العربي | Python | الوصف |
|--------|--------|-------|
| `شغل_اختبارات(مجموعة)` | `unittest.TextTestRunner().run(مجموعة)` | تشغيل الاختبارات |
| `نفذ(مجموعة)` | `testRunner.run(مجموعة)` | تنفيذ الاختبارات |
| `رئيسي()` | `unittest.main()` | الدالة الرئيسية |

## التخطي والتوقع

| العربي | Python | الوصف |
|--------|--------|-------|
| `تخطى(سبب)` | `unittest.skip(سبب)` | تخطي اختبار |
| `تخطى_إذا(شرط, سبب)` | `unittest.skipIf(شرط, سبب)` | تخطي إذا تحقق الشرط |
| `تخطى_ما_لم(شرط, سبب)` | `unittest.skipUnless(شرط, سبب)` | تخطي ما لم يتحقق الشرط |
| `فشل_متوقع()` | `unittest.expectedFailure` | فشل متوقع |

## Mock

| العربي | Python | الوصف |
|--------|--------|-------|
| `mock()` | `unittest.mock` | مكتبة الـ mock |
| `Mock()` | `unittest.mock.Mock()` | كائن mock |
| `MagicMock()` | `unittest.mock.MagicMock()` | كائن MagicMock |
| `patch(هدف)` | `unittest.mock.patch(هدف)` | تصحيح |
| `patch.object(هدف, خاصية)` | `unittest.mock.patch.object(هدف, خاصية)` | تصحيح كائن |

## مثال

```apl
class TestMath(حالة_اختبار):
    def setUp(self):
        self.x = 10
        self.y = 20

    def test_جمع(self):
        result = self.x + self.y
        ساوي(result, 30)

    def test_ضرب(self):
        result = self.x * self.y
        ساوي(result, 200)

    def test_أكبر(self):
        أكبر(self.y, self.x)

# تشغيل الاختبارات
رئيسي()
```

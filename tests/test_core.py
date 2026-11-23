"""Core contracts. No optional packages or network needed."""
import contextlib
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from core.apl_runner.main import transpile
from core.apl_runner.execution import Compilation, diagnostic


def cli(*args, **kwargs):
    return subprocess.run([sys.executable, str(ROOT / 'apl.py'), *args], capture_output=True, text=True, **kwargs)


class CompilerTests(unittest.TestCase):
    def test_malformed_stops_before_execution(self):
        result = cli('-c', 'اطبع "MUST_NOT_RUN"\nالمتغير س\nاطبع 2')
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn('MUST_NOT_RUN', result.stdout)
        self.assertIn('<command>:2:1', result.stderr)

    def test_multiline_literal_exact(self):
        value = 'first\nلو صحيح:\n2 + 3\n# اطبع\nدالة فيب(س):\n'
        code = transpile('المتغير س = """' + value + '"""')
        ns = {}
        exec(code, ns)
        self.assertEqual(ns['س'], value)

    def test_strings_comments_and_escaping(self):
        ns = {}
        exec(transpile('المتغير س = "اطبع \\\"لو\\\"; # نعم"\n# دالة فيب(س):\nالمتغير ص = r"a\\b"'), ns)
        self.assertEqual(ns['س'], 'اطبع "لو"; # نعم')
        self.assertEqual(ns['ص'], 'a\\b')

    def test_fstring_library_expression(self):
        result = cli('-c', 'المتغير س = 2.345\nاطبع f"قيمة {مقرب(س, 1)}"')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('2.3', result.stdout)

    def test_user_shadow_and_attached_conjunction(self):
        ns = {}
        exec(transpile('المتغير وسائط = [3]\nالمتغير جذر = lambda س: س + 1\nالمتغير ن = جذر(وسائط[0])'), ns)
        self.assertEqual(ns['ن'], 4)

    def test_nested_blocks_elif_recursion(self):
        result = cli('-c', 'دالة_عدد(ن):\n    لو ن < 1:\n        ارجع 0\n    والا_لو ن == 1:\n        ارجع 1\n    والا:\n        ارجع 1 + دالة_عدد(ن - 1)\nاطبع عدد(4)')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('4', result.stdout)

    def test_runtime_source_location_and_suggestion(self):
        result = cli('-c', 'المتغير العدد = 3\nاطبع العدذ')
        self.assertEqual(result.returncode, 1)
        self.assertIn('<command>:2:1', result.stderr)
        self.assertIn('هل تقصد: العدد', result.stderr)

    def test_check_has_no_side_effects(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'check.apl'
            path.write_text('raise RuntimeError("not executed")', encoding='utf-8')
            self.assertEqual(cli('check', str(path)).returncode, 0)

    def test_unterminated_string(self):
        result = cli('-c', 'المتغير س = """غير مغلق')
        self.assertEqual(result.returncode, 1)
        self.assertIn('APL-SyntaxError', result.stderr)

    def test_fold_equivalence(self):
        source = 'المتغير س = 2 + 3 * 4\nاطبع س\nاطبع "2 + 3"'
        normal = cli('-c', source)
        plain = cli('-c', source, env={**os.environ, 'APL_NO_FOLD': '1'})
        self.assertEqual(normal.stdout, plain.stdout)
        self.assertEqual(normal.returncode, 0)

    def test_parallel_context_does_not_leak(self):
        def compile_one(n):
            name = 'جذر' if n % 2 else 'قوة'
            ns = {}
            exec(transpile(f'المتغير {name} = lambda س: س + {n}\nالمتغير ن = {name}(2)'), ns)
            return ns['ن']
        with ThreadPoolExecutor(max_workers=6) as pool:
            self.assertEqual(list(pool.map(compile_one, range(30))), list(range(2, 32)))

    def test_repl_echo_and_state(self):
        result = cli('repl', input='المتغير س = 2\nس + 3\nexit\n')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('5', result.stdout)

    def test_multifile_argv_and_name(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'حساب.apl').write_text('دالة جمع(س, ص):\n    ارجع س + ص\n', encoding='utf-8')
            (root / 'main.apl').write_text('من حساب استورد جمع\nاستورد sys\nاطبع جمع(2, 3)\nاطبع __name__\nاطبع __file__\nاطبع sys.argv[1]', encoding='utf-8')
            result = cli('run', str(root / 'main.apl'), 'arg-value', cwd='/tmp')
            self.assertEqual(result.returncode, 0, result.stderr)
            for expected in ('5', '__main__', str(root / 'main.apl'), 'arg-value'):
                self.assertIn(expected, result.stdout)

    def test_package_relative_import(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'pkg').mkdir()
            (root / 'pkg/__init__.apl').write_text('from .values import answer\n', encoding='utf-8')
            (root / 'pkg/values.apl').write_text('answer = 42\n', encoding='utf-8')
            (root / 'main.apl').write_text('from pkg import answer\nاطبع answer', encoding='utf-8')
            result = cli('run', str(root / 'main.apl'))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('42', result.stdout)

    def test_core_words_and_attribute_bindings(self):
        result = cli('-c', 'صنف س:\n    دالة_إنشاء(ذات, أ):\n        ذات.أ = أ\n    دالة قيمة(ذات):\n        ارجع ذات.أ\nالمتغير ك = س(4)\nلو ك.قيمة() == 4 و 1 < 2:\n    اطبع "passed"')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('passed', result.stdout)

    def test_cache_invalidation_source_and_registry(self):
        from core.apl_runner import cache
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'program.apl'
            path.write_text('اطبع 1', encoding='utf-8')
            self.assertEqual(cli(str(path)).returncode, 0)
            self.assertIsNotNone(cache.load_cached(path, 'اطبع 1'))
            self.assertIsNone(cache.load_cached(path, 'اطبع 2'))
            path.write_text('المتغير س', encoding='utf-8')
            result = cli(str(path))
            self.assertEqual(result.returncode, 1)

    def test_taskbook(self):
        with tempfile.TemporaryDirectory() as temp:
            db = str(Path(temp) / 'tasks.db')
            main = str(ROOT / 'projects/taskbook/main.apl')
            self.assertEqual(cli('run', main, db, 'add', 'Test task').returncode, 0)
            self.assertIn('Test task', cli('run', main, db, 'list').stdout)
            self.assertEqual(cli('run', main, db, 'done', '1').returncode, 0)
            self.assertIn("'Test task', 1", cli('run', main, db, 'list').stdout)


if __name__ == '__main__':
    unittest.main()

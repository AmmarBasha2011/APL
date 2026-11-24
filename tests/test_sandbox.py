import os
import unittest
from playground.sandbox import command, run


class SandboxConfigTests(unittest.TestCase):
    def test_fail_closed_flags(self):
        args = command('test')
        for flag in ('--network=none', '--read-only', '--cap-drop=ALL',
                     '--security-opt=no-new-privileges:true', '--memory=128m',
                     '--pids-limit=32', '--user=65534:65534', '--pull=never'):
            self.assertIn(flag, args)
        self.assertNotIn('-v', args)
        self.assertNotIn('--privileged', args)

    def test_source_limit(self):
        with self.assertRaises(ValueError):
            run('x' * 16385)


@unittest.skipUnless(os.environ.get('APL_DOCKER_TESTS') == '1', 'requires built Docker image')
class SandboxIntegrationTests(unittest.TestCase):
    def test_arithmetic(self):
        result = run('اطبع 2 + 3')
        self.assertEqual(result['exit_code'], 0, result)
        self.assertIn('5', result['output'])

    def test_timeout(self):
        result = run('while True:\n    pass')
        self.assertTrue(result['status'] == 'timeout' or result['exit_code'] != 0, result)

    def test_output_cap(self):
        result = run('while True:\n    print("x" * 1000)')
        self.assertEqual(result['status'], 'output_limit', result)
        self.assertLessEqual(len(result['output'].encode()), 32768)

    def test_no_host_files(self):
        result = run('import os\nprint(os.path.exists("/host"))\nopen("/app/owned", "w")')
        self.assertNotEqual(result['exit_code'], 0, result)
        self.assertIn('False', result['output'])

    def test_no_network(self):
        result = run('import socket\nsocket.create_connection(("1.1.1.1", 80), timeout=1)')
        self.assertNotEqual(result['exit_code'], 0, result)

    def test_memory_limit(self):
        result = run('x = bytearray(512 * 1024 * 1024)')
        self.assertNotEqual(result['exit_code'], 0, result)

    def test_no_leftover_containers(self):
        import subprocess
        run('print(1)')
        result = subprocess.run(['docker', 'ps', '-aq', '--filter', 'name=apl-'], capture_output=True, text=True, check=True)
        self.assertFalse(result.stdout.strip())

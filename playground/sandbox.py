"""Fail-closed disposable Docker execution with bounded I/O and resources."""
import os
import selectors
import subprocess
import time
import uuid

IMAGE = 'apl-playground:local'
MAX_SOURCE = 16384
MAX_OUTPUT = 32768
TIMEOUT = 6


def command(name):
    return ['docker', 'run', '--rm', '--pull=never', '-i', '--name', name,
            '--network=none', '--read-only', '--cap-drop=ALL',
            '--security-opt=no-new-privileges:true', '--memory=128m',
            '--memory-swap=128m', '--cpus=0.5', '--pids-limit=32',
            '--ulimit', 'cpu=2:2', '--ulimit', 'nofile=64:64',
            '--ulimit', 'fsize=65536:65536', '--user=65534:65534',
            '--tmpfs', '/tmp:rw,noexec,nosuid,size=16m,mode=1777',
            '--log-driver=none', IMAGE]


def run(source):
    data = source.encode('utf-8')
    if len(data) > MAX_SOURCE:
        raise ValueError('Source exceeds 16 KiB')
    name = 'apl-' + uuid.uuid4().hex
    process, selector = None, selectors.DefaultSelector()
    output = bytearray()
    status = 'completed'
    try:
        process = subprocess.Popen(command(name), stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        os.set_blocking(process.stdout.fileno(), False)
        os.set_blocking(process.stdin.fileno(), False)
        selector.register(process.stdout, selectors.EVENT_READ, 'output')
        selector.register(process.stdin, selectors.EVENT_WRITE, 'input')
        pending = memoryview(data)
        deadline = time.monotonic() + TIMEOUT
        while selector.get_map():
            if time.monotonic() >= deadline:
                status = 'timeout'
                break
            for key, _ in selector.select(.05):
                if key.data == 'input':
                    try:
                        written = os.write(key.fd, pending) if pending else 0
                        pending = pending[written:]
                    except BrokenPipeError:
                        pending = memoryview(b'')
                    if not pending:
                        selector.unregister(key.fileobj)
                        process.stdin.close()
                else:
                    block = os.read(key.fd, 4096)
                    if not block:
                        selector.unregister(key.fileobj)
                        continue
                    available = MAX_OUTPUT - len(output)
                    output.extend(block[:available])
                    if len(block) > available:
                        status = 'output_limit'
                        break
            if status == 'output_limit':
                break
        if status == 'completed':
            try:
                process.wait(timeout=max(.1, deadline - time.monotonic()))
            except subprocess.TimeoutExpired:
                status = 'timeout'
        return {'status': status, 'exit_code': process.poll(),
                'output': output.decode('utf-8', 'replace')}
    finally:
        selector.close()
        # Kill by container name, not just the Docker client process: children
        # must not survive a timeout, disconnect or output flood.
        try:
            subprocess.run(['docker', 'rm', '-f', name], capture_output=True, timeout=10)
        except (OSError, subprocess.TimeoutExpired):
            pass
        if process:
            if process.poll() is None:
                process.kill()
            process.communicate(timeout=5)


def ready():
    subprocess.run(['docker', 'image', 'inspect', IMAGE], check=True,
                   capture_output=True, timeout=10)

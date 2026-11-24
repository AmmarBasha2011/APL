"""Runs ONLY inside the disposable no-network container."""
from pathlib import Path
import sys
sys.path.insert(0, '/app')
from core.apl_runner.cli import main
source = sys.stdin.buffer.read(16385)
if len(source) > 16384:
    raise SystemExit('Source exceeds 16 KiB')
raise SystemExit(main(['-c', source.decode('utf-8')]))

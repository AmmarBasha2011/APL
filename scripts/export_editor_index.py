#!/usr/bin/env python3
"""Generate the editor vocabulary from the shared registry (no target imports)."""
import json
import gzip
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from core.libraries.registry import symbols
out = ROOT / 'editors/vscode/completions.json.gz'
data = [{key: item[key] for key in ('name', 'target', 'library')} for item in symbols()]
text = gzip.compress((json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n').encode('utf-8'), mtime=0)
if '--check' in sys.argv:
    if not out.is_file() or out.read_bytes() != text:
        raise SystemExit('Editor index is stale: python scripts/export_editor_index.py')
else:
    out.write_bytes(text)
    print(f'Wrote {out}')

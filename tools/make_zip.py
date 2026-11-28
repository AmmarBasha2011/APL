#!/usr/bin/env python3
"""Zip a folder for a release, keeping what Info-ZIP on a CI runner loses.

    python tools/make_zip.py <folder> <out.zip> [--unix]

* Arabic file names are stored as UTF-8 and flagged as such, so Windows
  Explorer and unzip show them correctly.
* With --unix, the program files (apl, عمار, *.sh) get the executable bit.
  Build artifacts lose it on the way through upload/download.
"""
import stat
import sys
import zipfile
from pathlib import Path

folder, out = Path(sys.argv[1]), Path(sys.argv[2])
unix = "--unix" in sys.argv
EXEC_NAMES = {"apl", "عمار"}
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(folder.rglob("*")):
        rel = path.relative_to(folder).as_posix()
        if path.is_dir():
            continue
        info = zipfile.ZipInfo.from_file(path, rel)
        info.compress_type = zipfile.ZIP_DEFLATED
        mode = 0o644
        if unix and (path.name in EXEC_NAMES or path.suffix == ".sh"):
            mode = 0o755
        info.create_system = 3
        info.external_attr = (stat.S_IFREG | mode) << 16
        archive.writestr(info, path.read_bytes())
print("wrote", out)

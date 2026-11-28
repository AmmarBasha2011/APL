#!/usr/bin/env python3
"""Build the Linux installer: a .deb that installs APL like any other program.

    python tools/package_linux.py <package-folder> <version> <out-folder>

<package-folder> holds the built `apl` and the APL-Docs snapshot. The .deb puts
the program in /opt/apl, links `apl` and `عمار` into /usr/bin (so they are on
PATH), adds a menu entry with its own icon for each app, and registers the
.apl file type.
"""
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
package, version, out = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
deb_version = version.lstrip("v").replace("-", "~")
apps = json.loads((ROOT / "packaging" / "apps.json").read_text(encoding="utf-8"))
SIZES = [16, 24, 32, 48, 64, 128, 256, 512]

with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp) / "apl"
    opt = root / "opt" / "apl"
    opt.mkdir(parents=True)
    shutil.copy2(package / "apl", opt / "apl")
    (opt / "apl").chmod(0o755)
    shutil.copytree(package / "APL-Docs", opt / "APL-Docs")
    # On PATH.
    bin_dir = root / "usr" / "bin"
    bin_dir.mkdir(parents=True)
    os.symlink("/opt/apl/apl", bin_dir / "apl")
    os.symlink("/opt/apl/apl", bin_dir / "عمار")
    # Menu entries and icons.
    applications = root / "usr" / "share" / "applications"
    applications.mkdir(parents=True)
    names = ["apl"] + [a["id"] for a in apps]
    for name in names:
        for size in SIZES:
            target = root / "usr" / "share" / "icons" / "hicolor" / f"{size}x{size}" / "apps"
            target.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / "assets" / "icons" / name / f"{size}.png", target / f"apl-{name}.png")
    for app in apps:
        (applications / f"apl-{app['id']}.desktop").write_text(
            "[Desktop Entry]\nType=Application\nVersion=1.0\n"
            f"Name={app['name']}\nComment={app['comment']}\n"
            f"Exec=/opt/apl/apl {app['sub']}\nIcon=apl-{app['id']}\n"
            "Terminal=true\nCategories=Development;\nStartupNotify=false\n", encoding="utf-8")
    # .apl files open with APL.
    (applications / "apl-run.desktop").write_text(
        "[Desktop Entry]\nType=Application\nName=APL\nComment=Run an APL program\n"
        "Exec=/opt/apl/apl run %f\nIcon=apl-apl\nTerminal=true\nNoDisplay=true\n"
        "MimeType=text/x-apl;\n", encoding="utf-8")
    mime = root / "usr" / "share" / "mime" / "packages"
    mime.mkdir(parents=True)
    (mime / "apl.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">\n'
        '  <mime-type type="text/x-apl"><comment>APL program</comment>\n'
        '    <glob pattern="*.apl"/><icon name="apl-apl"/></mime-type>\n</mime-info>\n', encoding="utf-8")
    doc = root / "usr" / "share" / "doc" / "apl"
    doc.mkdir(parents=True)
    shutil.copy2(ROOT / "LICENSE", doc / "copyright")
    # Package metadata.
    debian = root / "DEBIAN"
    debian.mkdir()
    size_kb = sum(f.stat().st_size for f in root.rglob("*") if f.is_file()) // 1024
    (debian / "control").write_text(
        "Package: apl\n"
        f"Version: {deb_version}\n"
        "Section: devel\nPriority: optional\nArchitecture: amd64\n"
        "Maintainer: Ammar Elkhateeb <ammarbasha2011@users.noreply.github.com>\n"
        f"Installed-Size: {size_kb}\n"
        "Homepage: https://ammarbasha2011.github.io/APL/\n"
        "Description: APL, the Arabic programming language\n"
        " Write code in Arabic; it runs as clean Python. Includes the apl and\n"
        " عمار commands, plus Terminal, REPL, Libraries, Docs, Examples and\n"
        " Benchmark apps. Alpha release: expect bugs.\n", encoding="utf-8")
    script = ("#!/bin/sh\nset -e\n"
              "command -v update-mime-database >/dev/null 2>&1 && update-mime-database /usr/share/mime || true\n"
              "command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database -q || true\n"
              "command -v gtk-update-icon-cache >/dev/null 2>&1 && gtk-update-icon-cache -q -t /usr/share/icons/hicolor || true\n"
              "exit 0\n")
    for name in ("postinst", "postrm"):
        (debian / name).write_text(script, encoding="utf-8")
        (debian / name).chmod(0o755)
    out.mkdir(parents=True, exist_ok=True)
    target = out / f"APL-{version.lstrip('v')}-linux-amd64.deb"
    subprocess.run(["dpkg-deb", "--root-owner-group", "-Zxz", "--build", str(root), str(target)], check=True)
    print("wrote", target)

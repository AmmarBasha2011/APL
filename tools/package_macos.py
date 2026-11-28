#!/usr/bin/env python3
"""Build the macOS installer: a .pkg that installs APL and six apps.

    python tools/package_macos.py <package-folder> <version> <arch> <out-folder>

Run on a Mac (it needs iconutil and pkgbuild). The package installs:

* /usr/local/lib/apl/apl and the APL-Docs snapshot,
* `apl` and `عمار` in /usr/local/bin (already on PATH),
* /Applications/APL/APL Terminal.app, APL REPL.app, and so on. Each app opens
  Terminal and runs its tool, and has its own icon.

The package is not signed. The first time, right-click it and choose Open.
"""
import json
import os
import plistlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
package, version, arch, out = Path(sys.argv[1]), sys.argv[2], sys.argv[3], Path(sys.argv[4])
clean_version = version.lstrip("v")
apps = json.loads((ROOT / "packaging" / "apps.json").read_text(encoding="utf-8"))
LIB = "/usr/local/lib/apl"


def make_icns(name, target):
    with tempfile.TemporaryDirectory() as tmp:
        iconset = Path(tmp) / f"{name}.iconset"
        iconset.mkdir()
        source = ROOT / "assets" / "icons" / name
        pairs = {"icon_16x16.png": 16, "icon_16x16@2x.png": 32, "icon_32x32.png": 32,
                 "icon_32x32@2x.png": 64, "icon_128x128.png": 128, "icon_128x128@2x.png": 256,
                 "icon_256x256.png": 256, "icon_256x256@2x.png": 512, "icon_512x512.png": 512}
        for file_name, size in pairs.items():
            shutil.copy2(source / f"{size}.png", iconset / file_name)
        subprocess.run(["iconutil", "-c", "icns", str(iconset), "-o", str(target)], check=True)


with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp) / "root"
    lib = root / "usr" / "local" / "lib" / "apl"
    lib.mkdir(parents=True)
    shutil.copy2(package / "apl", lib / "apl")
    (lib / "apl").chmod(0o755)
    shutil.copytree(package / "APL-Docs", lib / "APL-Docs")
    make_icns("apl", lib / "apl.icns")
    bin_dir = root / "usr" / "local" / "bin"
    bin_dir.mkdir(parents=True)
    os.symlink(f"{LIB}/apl", bin_dir / "apl")
    os.symlink(f"{LIB}/apl", bin_dir / "عمار")
    group = root / "Applications" / "APL"
    group.mkdir(parents=True)
    for app in apps:
        bundle = group / f"{app['name']}.app"
        (bundle / "Contents" / "MacOS").mkdir(parents=True)
        (bundle / "Contents" / "Resources").mkdir(parents=True)
        make_icns(app["id"], bundle / "Contents" / "Resources" / f"{app['id']}.icns")
        launcher = bundle / "Contents" / "MacOS" / "launcher"
        launcher.write_text(
            "#!/bin/sh\n"
            f"/usr/bin/osascript -e 'tell application \"Terminal\" to do script \"{LIB}/apl {app['sub']}\"' "
            "-e 'tell application \"Terminal\" to activate'\n", encoding="utf-8")
        launcher.chmod(0o755)
        with open(bundle / "Contents" / "Info.plist", "wb") as handle:
            plistlib.dump({
                "CFBundleName": app["name"], "CFBundleDisplayName": app["name"],
                "CFBundleIdentifier": f"io.github.ammarbasha2011.apl.{app['id']}",
                "CFBundleVersion": clean_version, "CFBundleShortVersionString": clean_version.split("-")[0],
                "CFBundleExecutable": "launcher", "CFBundleIconFile": app["id"],
                "CFBundlePackageType": "APPL", "LSMinimumSystemVersion": "11.0",
                "NSHighResolutionCapable": True,
            }, handle)
    out.mkdir(parents=True, exist_ok=True)
    target = out / f"APL-{clean_version}-macos-{arch}.pkg"
    subprocess.run(["pkgbuild", "--root", str(root), "--identifier", "io.github.ammarbasha2011.apl",
                    "--version", clean_version.split("-")[0], "--install-location", "/", str(target)], check=True)
    print("wrote", target)

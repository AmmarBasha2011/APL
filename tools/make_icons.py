#!/usr/bin/env python3
"""Draw the APL logo and the six app icons from assets/logo.svg.

    python tools/make_icons.py

Needs Chrome (to draw the SVG) and Pillow (to write .ico and PNG sizes). The
results are committed under assets/, so builds don't need either. The logo and
the badges are original drawings made for this project.
"""
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image

ASSETS = Path(__file__).resolve().parents[1] / "assets"
LOGO = (ASSETS / "logo.svg").read_text(encoding="utf-8")
CHROME = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chrome")

BADGE_BG = '<circle cx="388" cy="388" r="92" fill="#06150f" stroke="#3ddc97" stroke-width="6"/>'
GLYPH = 'fill="none" stroke="#eaf6f0" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"'
BADGES = {
    "terminal": f'<path d="M352 358 L386 388 L352 418" {GLYPH}/><path d="M398 424 H430" {GLYPH}/>',
    "repl": '<path d="M366 350 L430 388 L366 426 Z" fill="#eaf6f0" stroke="#eaf6f0" stroke-width="10" stroke-linejoin="round"/>',
    "libraries": f'<rect x="350" y="352" width="26" height="72" rx="5" {GLYPH}/><rect x="388" y="352" width="26" height="72" rx="5" {GLYPH}/><path d="M424 358 L440 424" {GLYPH}/>',
    "docs": f'<path d="M352 358 H424 M352 388 H424 M352 418 H400" {GLYPH}/>',
    "examples": f'<path d="M372 352 C354 352 358 388 346 388 C358 388 354 424 372 424 M404 352 C422 352 418 388 430 388 C418 388 422 424 404 424" {GLYPH}/>',
    "benchmark": f'<path d="M346 420 A44 44 0 1 1 430 420" {GLYPH}/><path d="M388 410 L410 372" {GLYPH}/>',
}
SIZES = [16, 24, 32, 48, 64, 128, 256, 512]


def render(svg_text, size, out):
    with tempfile.TemporaryDirectory() as folder:
        source = Path(folder) / "i.svg"
        source.write_text(svg_text, encoding="utf-8")
        subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
                        "--hide-scrollbars", "--default-background-color=00000000",
                        f"--window-size=512,512", f"--screenshot={out}", source.as_uri()],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def save_sizes(big, name):
    folder = ASSETS / "icons" / name
    folder.mkdir(parents=True, exist_ok=True)
    image = Image.open(big).convert("RGBA")
    for size in SIZES:
        image.resize((size, size), Image.LANCZOS).save(folder / f"{size}.png")
    image.save(folder / f"{name}.ico", sizes=[(s, s) for s in (16, 24, 32, 48, 64, 128, 256)])


def main():
    (ASSETS / "icons").mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as folder:
        big = Path(folder) / "apl.png"
        render(LOGO, 512, big)
        save_sizes(big, "apl")
        for name, badge in BADGES.items():
            svg = LOGO.replace("</svg>", BADGE_BG + badge + "</svg>")
            big = Path(folder) / f"{name}.png"
            render(svg, 512, big)
            save_sizes(big, name)
    # Contact sheet for review.
    sheet = Image.new("RGBA", (6 * 276 + 276, 276), (20, 20, 20, 255))
    for index, name in enumerate(["apl"] + list(BADGES)):
        icon = Image.open(ASSETS / "icons" / name / "256.png")
        sheet.paste(icon, (index * 276 + 10, 10), icon)
    sheet.save(ASSETS / "icons" / "sheet.png")
    print("icons written to", ASSETS / "icons")


if __name__ == "__main__":
    main()

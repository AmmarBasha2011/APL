#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""update_landing_stats.py — تحديث أرقام صفحة الهبوط على gh-pages.

يحسب عدد المكتبات من core/libraries/registry.json وعدد الأمثلة من examples/*.apl
ويكتب stats.json في فرع gh-pages ويحدّث الأرقام الثابتة في index.html (وصف ميتا،
عدادات data-to، وعنوان قسم المكتبات). تُشغّله workflow Landing stats بعد كل دفع إلى main.

الاستخدام:
    python scripts/update_landing_stats.py <main_checkout> <ghpages_checkout>
"""

import glob
import json
import os
import re
import sys


def main() -> int:
    main_dir, site_dir = sys.argv[1], sys.argv[2]

    reg = json.load(open(os.path.join(main_dir, "core/libraries/registry.json"), encoding="utf-8"))
    libs = reg["libraries"] if isinstance(reg, dict) else reg
    n_libs = len(libs)
    names = [lib["name"] for lib in libs]

    n_examples = len(glob.glob(os.path.join(main_dir, "examples", "*.apl")))

    stats = {"libs": n_libs, "libNames": names, "examples": n_examples}
    with open(os.path.join(site_dir, "stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)
        f.write("\n")

    index_path = os.path.join(site_dir, "index.html")
    lines = open(index_path, encoding="utf-8").read().split("\n")
    for i, line in enumerate(lines):
        if "مكتبة مترجمة بالكامل" in line:
            lines[i] = re.sub(r'data-to="\d+"', f'data-to="{n_libs}"', line)
        elif "مثال جاهز، كلها مختبرة" in line:
            lines[i] = re.sub(r'data-to="\d+"', f'data-to="{n_examples}"', line)
        elif "<em>" in line and "مكتبة بالعربي" in line:
            lines[i] = re.sub(r"<em>\d+</em>", f"<em>{n_libs}</em>", line)
        elif 'name="description"' in line:
            lines[i] = re.sub(r"\d+ مكتبة و\d+ مثالاً", f"{n_libs} مكتبة و{n_examples} مثالاً", line)
    open(index_path, "w", encoding="utf-8").write("\n".join(lines))

    print(f"libs={n_libs} examples={n_examples} libNames={len(names)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

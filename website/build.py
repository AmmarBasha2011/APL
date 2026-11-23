#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""يبني موقع APL الثابت (عربي، RTL) من ملفات الريبو نفسها.

    python website/build.py          # يكتب الصفحات في website/
    python website/build.py --check  # يتأكد أن الصفحات المبنية محدّثة

لا يعتمد على أي حزمة خارجية ولا يحمّل أي موارد من الإنترنت.
الصفحات: index (الرئيسية) / docs (مرجع اللغة) / features (المميزات)
        / examples (الأمثلة) / libraries (المكتبات)
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO_URL = "https://github.com/AmmarBasha2011/APL"


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def version():
    m = re.search(r'__version__\s*=\s*"([\d.]+)"', read("core/apl_runner/main.py"))
    return m.group(1) if m else "?"


# ---------------------------------------------------------------- تلوين الكود
KEYWORDS = (
    "المتغير اطبع اطبع_بدون ادخل إذا لو سإذا الا والا طالما لكل في أبدا توقف "
    "استمر دالة ارجع صنف دالة_إنشاء ذات حاول إمسك أخيرا أخيراً مع مثل حالة قيمة "
    "افتراضي تمرير سهم و أو ليس صواب خطأ لا_شيء عام خاص خاصية محدد تأكد انتج "
    "استورد من"
).split()
KW_RE = re.compile(
    r"(?<![\w\u0600-\u06FF])(" + "|".join(sorted(map(re.escape, KEYWORDS), key=len, reverse=True))
    + r")(?![\w\u0600-\u06FF])")
TOKEN_RE = re.compile(
    r'(?P<c>#[^\n]*)|(?P<s>f?"""[\s\S]*?"""|f?"(?:\\.|[^"\\\n])*"|f?\'(?:\\.|[^\'\\\n])*\')'
    r'|(?P<n>(?<![\w\u0600-\u06FF])\d+(?:\.\d+)?)')


def highlight(code):
    out, pos = [], 0

    def kw(text):
        return KW_RE.sub(lambda m: '<span class="k">%s</span>' % m.group(1), html.escape(text))

    for m in TOKEN_RE.finditer(code):
        out.append(kw(code[pos:m.start()]))
        cls = m.lastgroup
        out.append('<span class="%s">%s</span>' % (cls, html.escape(m.group(0))))
        pos = m.end()
    out.append(kw(code[pos:]))
    return "".join(out)


def code_block(code, lang="apl"):
    code = code.rstrip("\n")
    body = highlight(code) if lang in ("apl", "") else html.escape(code)
    return ('<div class="code"><button class="copy" type="button" aria-label="نسخ الكود">نسخ</button>'
            '<pre dir="rtl"><code>%s</code></pre></div>' % body)


# ---------------------------------------------------------------- ماركداون مصغّر
def inline(text):
    parts = re.split(r"(`[^`]+`)", text)
    res = []
    for p in parts:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            res.append("<code>%s</code>" % html.escape(p[1:-1]))
        else:
            p = html.escape(p)
            p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
            p = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: link(m.group(1), m.group(2)), p)
            res.append(p)
    return "".join(res)


def link(label, href):
    href = html.unescape(href)
    if not re.match(r"https?://|#", href):
        href = REPO_URL + "/blob/main/docs/" + href.lstrip("./")
    return '<a href="%s">%s</a>' % (html.escape(href, quote=True), label)


def slug(text):
    s = re.sub(r"[^\w\u0600-\u06FF]+", "-", text).strip("-")
    return s or "section"


def md_to_html(md):
    lines = md.splitlines()
    out, toc, i = [], [], 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            lang = ln[3:].strip()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append(code_block("\n".join(buf), lang or "text"))
            continue
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
            head = [c.strip() for c in ln.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ['<div class="table-wrap"><table><thead><tr>']
            t += ["<th>%s</th>" % inline(h) for h in head]
            t.append("</tr></thead><tbody>")
            for r in rows:
                t.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", ln)
        if m:
            level, text = len(m.group(1)), m.group(2)
            sid = slug(text)
            if level == 2:
                toc.append((sid, re.sub(r"`", "", text)))
            out.append('<h%d id="%s">%s</h%d>' % (level, sid, inline(text), level))
            i += 1
            continue
        if re.match(r"^\s*[-*]\s+", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i]))
                i += 1
            out.append("<ul>" + "".join("<li>%s</li>" % inline(x) for x in items) + "</ul>")
            continue
        if ln.strip() in ("", "---"):
            i += 1
            continue
        buf = [ln]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(```|#|\||\s*[-*]\s)", lines[i]):
            buf.append(lines[i])
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(buf)))
    return "\n".join(out), toc


# ---------------------------------------------------------------- القالب
NAV = [("index.html", "الرئيسية"), ("docs.html", "مرجع اللغة"), ("features.html", "المميزات"),
       ("examples.html", "الأمثلة"), ("libraries.html", "المكتبات")]


def page(fname, title, body, side=""):
    nav = "".join('<a href="%s"%s>%s</a>' % (h, ' class="on" aria-current="page"' if h == fname else "", t)
                  for h, t in NAV)
    return """<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="APL: لغة برمجة كاملة بالعربي. اكتب بالعربي، وتتحول إلى Python وتعمل مباشرة.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">تخطَّ إلى المحتوى</a>
<header class="top"><div class="wrap bar">
<a class="brand" href="index.html"><span class="logo" aria-hidden="true">أ</span> APL</a>
<nav aria-label="التنقل الرئيسي">%(nav)s</nav>
<a class="gh" href="%(repo)s">GitHub</a>
</div></header>
<main id="main">
%(body)s
</main>
<footer><div class="wrap">
<p>APL v%(ver)s — لغة برمجة بالعربي. المصدر على <a href="%(repo)s">GitHub</a>. هذه الصفحات مبنية تلقائيا من ملفات المشروع بواسطة <code>website/build.py</code>.</p>
</div></footer>
<script src="app.js"></script>
</body>
</html>
""" % {"title": html.escape(title), "nav": nav, "body": body, "repo": REPO_URL, "ver": version()}


def doc_page(fname, title, md_file, intro):
    body_html, toc = md_to_html(read(md_file))
    body_html = re.sub(r"^<h1[^>]*>.*?</h1>\n?", "", body_html, count=1, flags=re.S)
    side = '<aside class="toc" aria-label="فهرس الصفحة"><strong>في هذه الصفحة</strong>%s</aside>' % "".join(
        '<a href="#%s">%s</a>' % (s, html.escape(t)) for s, t in toc)
    body = ('<div class="wrap doc"><div class="doc-head"><h1>%s</h1><p class="lead">%s</p></div>'
            '<div class="doc-grid">%s<article class="prose">%s</article></div></div>'
            % (html.escape(title), html.escape(intro), side, body_html))
    return page(fname, title + " — APL", body)


# ---------------------------------------------------------------- الصفحات
HERO_CODE = '''المتغير اسم = "عالم"
اطبع f"مرحبا يا {اسم}"

دالة فيب(ن):
    لو ن < 2:
        ارجع ن
    ارجع فيب(ن - 1) + فيب(ن - 2)

لكل س في نطاق(8):
    اطبع_بدون f"{فيب(س)} "
'''


def library_rows():
    rows = []
    for ln in read("README.md").splitlines():
        m = re.match(r"^\| `([^`]+)` \| (\d+) \| (.*) \|$", ln)
        if m:
            rows.append((m.group(1), int(m.group(2)), m.group(3)))
    return rows


def build_index():
    libs = library_rows()
    n_lib = len(libs)
    n_items = sum(r[1] for r in libs)
    n_ex = len([f for f in os.listdir(os.path.join(ROOT, "examples")) if f.endswith(".apl")])
    feats = [
        ("كلمات مفتاحية عربية", "اطبع، لو، دالة، صنف، حاول، حالة وغيرها. تقرأ الكود كما تقرأ الجملة."),
        ("تتحول إلى Python", "كل ما يعمل في Python متاح لك: مكتباته وأدواته وسرعته."),
        ("مكتبات بالعربي", "%d مكتبة بأسماء عربية، من الرياضيات والملفات إلى الويب والبيانات." % n_lib),
        ("أخطاء مفهومة", "رسائل الأخطاء مترجمة إلى العربية بدل نصوص Python الإنجليزية."),
        ("REPL تفاعلي", "جرّب الكود سطرا بسطر: <code>python apl.py repl</code>."),
        ("%d مثالا جاهزا" % n_ex, "برامج حقيقية مختبرة تغطي الخوارزميات والنصوص والملفات والويب."),
    ]
    cards = "".join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (t, d) for t, d in feats)
    body = """
<section class="hero"><div class="wrap hero-grid">
<div>
<p class="badge">الإصدار %(ver)s</p>
<h1>اكتب برنامجك<br>بلغتك العربية</h1>
<p class="lead">APL لغة برمجة كاملة بالعربي. تكتب الكود بالعربي، فيتحول تلقائيا إلى Python ويعمل مباشرة.</p>
<div class="cta"><a class="btn primary" href="#start">ابدأ الآن</a><a class="btn" href="examples.html">شاهد الأمثلة</a></div>
<ul class="stats"><li><b>%(n_lib)d</b> مكتبة</li><li><b>%(n_items)s</b> عنصر</li><li><b>%(n_ex)d</b> مثال</li></ul>
</div>
<div>%(hero)s<p class="hint">هذا المثال يطبع: مرحبا يا عالم، ثم أول ثمانية حدود من متتالية فيبوناتشي.</p></div>
</div></section>
<section class="wrap block"><h2>لماذا APL؟</h2><div class="cards">%(cards)s</div></section>
<section class="wrap block" id="start"><h2>ابدأ في دقيقة</h2>
<p>تحتاج Python 3.14 أو أحدث. لا شيء آخر.</p>
<ol class="steps">
<li><p>حمّل المشروع:</p>%(c1)s</li>
<li><p>شغّل مثالا جاهزا:</p>%(c2)s</li>
<li><p>أو جرّب الكود مباشرة:</p>%(c3)s</li>
</ol>
<p>ثم اقرأ <a href="docs.html">مرجع اللغة</a> وتصفّح <a href="examples.html">الأمثلة</a>.</p>
</section>
""" % {
        "ver": version(), "n_lib": n_lib, "n_items": format(n_items, ","), "n_ex": n_ex,
        "hero": code_block(HERO_CODE), "cards": cards,
        "c1": code_block("git clone %s.git\ncd APL" % REPO_URL, "text"),
        "c2": code_block("python apl.py examples/01-calculator.apl", "text"),
        "c3": code_block("python apl.py -c \"اطبع 'مرحباً'\"\npython apl.py repl", "text"),
    }
    return page("index.html", "APL — لغة برمجة بالعربي", body)


EXAMPLE_PICKS = [
    ("11-fibonacci", "متتالية فيبوناتشي", "دوال وحلقات وتكرار"),
    ("12-prime-check", "فحص الأعداد الأولية", "دوال وشروط وقوائم"),
    ("03-task-manager", "مدير المهام", "قواميس وقوائم وحلقات"),
    ("04-text-analyzer", "محلل النصوص", "معالجة النصوص"),
    ("06-search-sort", "البحث والفرز", "خوارزميات"),
    ("01-calculator", "آلة حاسبة", "إدخال وشروط متعددة"),
]


def build_examples():
    items = []
    for key, title, sub in EXAMPLE_PICKS:
        rel = "examples/%s.apl" % key
        if not os.path.exists(os.path.join(ROOT, rel)):
            continue
        src = read(rel)
        items.append('<article class="ex" id="%s"><div class="ex-head"><h2>%s</h2><p>%s</p></div>%s'
                     '<p class="src">الملف: <a href="%s/blob/main/%s"><code dir="ltr">%s</code></a></p></article>'
                     % (key, html.escape(title), html.escape(sub), code_block(src), REPO_URL, rel, rel))
    n_ex = len([f for f in os.listdir(os.path.join(ROOT, "examples")) if f.endswith(".apl")])
    demo = ""
    body = ('<div class="wrap doc"><div class="doc-head"><h1>الأمثلة</h1>'
            '<p class="lead">مختارات من %d مثالا جاهزا في مجلد <code>examples/</code>. كلها حقيقية ومختبرة في كل فحص.</p>%s</div>'
            '<div class="ex-list">%s</div>'
            '<p><a class="btn" href="%s/tree/main/examples">كل الأمثلة على GitHub</a></p></div>'
            % (n_ex, demo, "\n".join(items), REPO_URL))
    return page("examples.html", "الأمثلة — APL", body)


def build_libraries():
    libs = sorted(library_rows(), key=lambda r: -r[1])
    rows = "".join(
        '<tr><td><code dir="ltr">%s</code></td><td class="num">%s</td><td>%s</td></tr>'
        % (html.escape(n), format(c, ","), inline(d)) for n, c, d in libs)
    body = ('<div class="wrap doc"><div class="doc-head"><h1>المكتبات</h1>'
            '<p class="lead">%d مكتبة، مجموع عناصرها %s. لكل مكتبة ملف توثيق في <a href="%s/tree/main/docs">docs/</a>.</p></div>'
            '<input id="filter" class="filter" type="search" placeholder="ابحث عن مكتبة…" aria-label="ابحث عن مكتبة">'
            '<div class="table-wrap"><table id="libs"><thead><tr><th>المكتبة</th><th>العناصر</th><th>الوصف</th></tr></thead>'
            '<tbody>%s</tbody></table></div></div>'
            % (len(libs), format(sum(r[1] for r in libs), ","), REPO_URL, rows))
    return page("libraries.html", "المكتبات — APL", body)


def build_all():
    return {
        "index.html": build_index(),
        "docs.html": doc_page("docs.html", "مرجع اللغة", "docs/language-reference.md",
                              "كل الكلمات المفتاحية والتراكيب مع أمثلة قصيرة."),
        "features.html": doc_page("features.html", "مميزات اللغة", "docs/language-features.md",
                                  "التقاط الأخطاء، المطابقة، lambda، الوراثة وغيرها."),
        "examples.html": build_examples(),
        "libraries.html": build_libraries(),
    }


def main():
    pages = build_all()
    if "--check" in sys.argv:
        stale = [n for n, c in pages.items()
                 if not os.path.exists(os.path.join(HERE, n))
                 or open(os.path.join(HERE, n), encoding="utf-8").read() != c]
        if stale:
            print("صفحات قديمة، شغّل python website/build.py:", ", ".join(stale))
            sys.exit(1)
        print("✓ صفحات الموقع محدّثة")
        return
    for name, content in pages.items():
        with open(os.path.join(HERE, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
    print("تم بناء %d صفحات في website/" % len(pages))


if __name__ == "__main__":
    main()

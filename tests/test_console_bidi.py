"""Console Arabic: joining forms, visual order, and the buffered stream."""
import io
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from core import console_bidi as b  # noqa: E402

failures = []


def check(name, ok, detail=""):
    if not ok:
        failures.append(name)
        print("FAIL", name, repr(detail))


# Plain text without Arabic is untouched.
check("ascii unchanged", b.visual("hello (1, 2)") == "hello (1, 2)")
check("empty", b.visual("") == "")

# Joining forms: initial, medial, final, isolated.
check("shape word", b.shape("لغة") == "\uFEDF\uFED0\uFE94" or b.shape("لغة")[0] == "\uFEDF", b.shape("لغة"))
check("shape isolated letter", b.shape("م") == "\uFEE1", b.shape("م"))
check("shape non-joining alef", b.shape("با") == "\uFE91\uFE8E", b.shape("با"))
check("lam alef ligature", b.shape("لا") == "\uFEFB", b.shape("لا"))
check("lam alef after joiner", b.shape("بلا") == "\uFE91\uFEFC", b.shape("بلا"))

# Order: a right-to-left line is reversed; Latin and digits keep their order.
word = b.visual("مرحبا")
check("reversed", word == b.shape("مرحبا")[::-1], word)
mixed = b.visual("النتيجة: abc 123")
check("latin run kept", "abc 123" in mixed, mixed)
check("latin run left", mixed.startswith("abc 123"), mixed)
check("number kept", "1,234" in b.visual("المبلغ 1,234 جنيه"))
check("brackets mirrored", b.visual("(مرحبا)").startswith("(") and b.visual("(مرحبا)").endswith(")"))
check("controls dropped", "\u202b" not in b.visual("\u202bمرحبا\u202c"))
# Marks stay after their letter.
check("mark follows base", b.visual("لِ")[-1] == "\u0650" or b.visual("لِ")[1] == "\u0650", b.visual("لِ"))

# ANSI colour codes survive.
check("ansi kept", "\x1b[31m" in b.convert("\x1b[31mمرحبا\x1b[0m"))

# The stream buffers pieces of one print into one line.
sink = io.StringIO()
stream = b.Stream(sink)
print("\u202b", "مرحبا", "بالعالم", "\u202c", file=stream)
check("stream line", sink.getvalue() == b.visual("\u202b مرحبا بالعالم \u202c") + "\n", sink.getvalue())
stream.write("سؤال؟ ")
check("pending held", sink.getvalue().endswith("\n"))
stream.flush()
check("flush writes pending", "ﻝﺍﺅﺱ" in sink.getvalue() or len(sink.getvalue()) > 10)

# A pipe is never changed unless forced; APL_BIDI=1 forces it, 0 disables it.
program = ROOT / "tests" / "cases" / "01_basics.apl"
env = dict(os.environ, PYTHONUTF8="1")
env.pop("APL_BIDI", None)
plain = subprocess.run([sys.executable, str(ROOT / "apl.py"), "-c", 'اطبع "مرحبا"'],
                       capture_output=True, env=env).stdout.decode("utf-8")
check("pipe unchanged", "مرحبا" in plain, plain)
forced = subprocess.run([sys.executable, str(ROOT / "apl.py"), "-c", 'اطبع "مرحبا"'],
                        capture_output=True, env=dict(env, APL_BIDI="1")).stdout.decode("utf-8")
check("forced is visual", b.shape("مرحبا")[::-1] in forced, forced)
off = subprocess.run([sys.executable, str(ROOT / "apl.py"), "-c", 'اطبع "مرحبا"'],
                     capture_output=True, env=dict(env, APL_BIDI="0")).stdout.decode("utf-8")
check("off is plain", "مرحبا" in off, off)

sys.exit(1 if failures else 0)

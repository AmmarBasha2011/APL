import sys, os, io
from core.runner import regex_cache as re

# Install lazy library proxies BEFORE anything imports a library module. This is
# what removes the ~41 unconditional imports (and their ~1,956 regex compiles)
# from startup: a module is only executed when one of its Arabic keys is used.
from core.libraries import lazy as _apl_lazy
_apl_lazy.install()

from core.runner import _inline_replace
from core.runner.transpiler import transpile_line
from core.runner.patterns import _UDF_NAMES

def _build_reserved_keys():
    """Deprecated no-op.

    This used to import all 41 library modules and union their Arabic keys.
    The result was never read anywhere in the codebase, so it only cost startup
    time (~1,956 regex compiles). Kept for API compatibility; returns an empty
    set. Library loading is now lazy (see core.libraries.lazy).
    """
    return set()

from core.libraries.registry import ENTRIES, module, imports_for
LIBRARY_MODULES = [entry['module'] for entry in ENTRIES]
_RESERVED_KEYS = _build_reserved_keys()  # empty: unused, see docstring

# Constant folding on by default; APL_NO_FOLD=1 turns it off.
_APL_FOLD = os.environ.get("APL_NO_FOLD", "") not in ("1", "true", "yes")
_library_modules = {entry['name']: module(entry) for entry in ENTRIES}
globals().update({entry['module']: _library_modules[entry['name']] for entry in ENTRIES})

# Respect embedding applications and redirected/captured stdout.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.platform == "win32":
    import ctypes
    try:
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleOutputCP(65001)
        kernel32.SetConsoleCP(65001)
    except Exception:
        pass



_USER_NAME_PATTERNS = (
    r"^\s*(?:async\s+)?def\s+([^\s(:]+)",
    r"^\s*class\s+([^\s(:]+)",
    r"^\s*دالة\s+([^\s(]+)",
    r"^\s*دالة_([^\s(]+)\s*\(",
    r"^\s*صنف\s+([^\s(:]+)",
    r"^\s*(?:المتغير|عام\s+المتغير|خاص\s+المتغير)\s+([^\s=]+)",
    r"^\s*([\w\u0600-\u06FF]+)\s*=(?!=)",
    r"^\s*لكل\s+([^\s]+)\s+",
    r"^\s*من\s+([^\s]+)\s+استورد",
)


def _collect_user_names(source: str) -> set:
    """Names the program itself defines, so libraries never rewrite them."""
    names = set()
    for line in source.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        for pat in _USER_NAME_PATTERNS:
            m = re.match(pat, stripped)
            if m:
                names.add(m.group(1))
    for statement in source.splitlines():
        match = re.match(r"\s*من\s+\S+\s+استورد\s+(.+)", statement)
        if match:
            for name in match.group(1).split(','):
                names.add(name.strip().split()[-1])
    names.update(re.findall(r"(?:إمسك|امسك|except).*?(?:مثل|as)\s+([^\W\d]\w*)", source))
    return names

import threading
_COMPILE_LOCK = threading.RLock()


def transpile(source: str) -> str:
    # Legacy library tables hold per-compilation name state. Serialize their
    # use and reset on each invocation, including concurrent embedding calls.
    with _COMPILE_LOCK:
        return _transpile(source)


_DIGITS = {ord(c): str(i) for i, c in enumerate('٠١٢٣٤٥٦٧٨٩')}
_DIGITS.update({ord(c): str(i) for i, c in enumerate('۰۱۲۳۴۵۶۷۸۹')})


def _arabic_digits(source: str) -> str:
    """٠١٢٣ and ۰۱۲۳ are digits too.

    Literals are already replaced by placeholders when this runs, so text inside
    strings keeps its own spelling and only real code is normalised.
    """
    return source.translate(_DIGITS)


def _transpile(source: str) -> str:
    # "استورد "ملف.apl"" pulls another APL file into this program. It has to be
    # rewritten before literals are protected, because the path is a literal.
    # A trailing comment is allowed: without it the line fell through to
    # "import "ملف.apl"", which Python rejected as invalid syntax.
    source = re.sub(
        r"(?m)^([ \t]*)استورد[ \t]+[\"']([^\"']+\.apl)[\"'][ \t]*(?:#.*)?$",
        r'\1_apl_import_file("\2", globals())',
        source,
    )
    source = re.sub(
        r"(?m)^([ \t]*)استورد[ \t]+([^\s\"']+\.apl)[ \t]*(?:#.*)?$",
        r'\1_apl_import_file("\2", globals())',
        source,
    )
    from core.runner.source import protect, restore
    source, _literals, _origins = protect(source)
    source = _arabic_digits(source)
    from core.runner import inline_replacer as _ir
    _ir.USER_NAMES = _collect_user_names(source)
    # Pre-scan for user-defined function names so their call sites are protected
    # before any library pattern runs.
    _UDF_NAMES.clear()
    for _ln in source.split("\n"):
        _s = _ln.strip()
        if _s.startswith("دالة") and ("(" in _s) and not _s.startswith("#"):
            # "دالة_اسم(...)" -> the identifier is "دالة_اسم"
            # "دالة اسم(...)"  -> the identifier is "اسم"
            # "دالة_فيب(...)": the identifier is دالة_فيب -> protect "فيب" and re-add prefix
            # "دالة مربع(...)":  the identifier is مربع
            if _s.startswith("دالة_"):
                _m = re.match(r"^دالة_([^\s(:]+)", _s)
                # "دالة_إنشاء" is the CONSTRUCTOR keyword, not a user-defined
                # name: registering it made the pre-pass placeholder-ise the
                # constructor, so transpile_line never saw the keyword and
                # emitted "def إنشاء" instead of "def __init__".
                if _m and _m.group(1) not in ("def", "إنشاء", "إنشاء_فئة"):
                    _UDF_NAMES.add(_m.group(1))
            else:
                _m = re.match(r"^([^\s(:]+)", _s[4:].strip())
                if _m and _m.group(1) != "def":
                    _UDF_NAMES.add(_m.group(1))

    # Protect user-defined function names across the WHOLE source before any
    # library pattern can rewrite them.
    # A user-defined name shadows a library key of the same name inside this file.
    # Replace user-defined function names with ASCII placeholders so that no
    # library pattern (which may contain the same Arabic word) can match them.
    _udf_map = {}
    for _i, _nm in enumerate(sorted(_UDF_NAMES)):
        _tok = f"_APL_UDF_{_i}_"
        _udf_map[_tok] = _nm
        # Protect the name at BOTH call sites and definition sites.
        # A definition reads "دالة_اسم(نص):" where the name is directly glued to
        # the "دالة_" prefix, so a normal (?<!\w) guard skips every definition
        # and leaves `def دالة_اسم` unrenamed while calls became `اسم(...)`
        # (this silently broke example 49). Handle the glued case explicitly.
        # (a) glued to the definition/call keyword: "دالة_فيب(" and the
        #     recursive "ارجع دالة_فيب(". No negative lookbehind here — the
        #     preceding char is "_", which IS \w, so a (?<!\w) guard would
        #     block the very match we need. The name may be followed by "("
        #     (a call) or by "," / ")" (passed as a function reference, e.g.
        #     map(دالة_مربع, ...)) — cover both.
        source = re.sub(
            rf"(?<=دالة_){re.escape(_nm)}(?=\s*[\(,)]|$)", _tok, source
        )
        # (a2) decorator lines: "@دالة_مزخرفة" — the char before دالة_ is "@",
        #      so neither lookbehind above can match. Drop the prefix there.
        source = re.sub(rf"(@\s*)دالة_({re.escape(_nm)})", rf"\1\2", source)
        source = re.sub(
            rf"(?<=دالة_){re.escape(_nm)}(?=\s*[\(,)]|$)", _tok, source
        )
        # (b) ordinary call sites: "اطبع فيب(" and bare references such as a
        #     decorator line "@مزخرفة" (no parentheses at all).
        source = re.sub(
            rf"(?<![\w\u0600-\u06FF@]){re.escape(_nm)}(?=\s*[\(,)\s]|$)",
            _tok, source,
        )
    # "دالة_اسم(...)" -> "_APL_UDF_0_(...)" so the transpiler sees a plain call
    # token. A DEFINITION keeps its دالة_ prefix: without it, transpile_line
    # sees "_APL_UDF_0_(ن):" (no "دالة"/"def") and emits a bare tuple, not a
    # function. The def name is normalised in the restore step below.
    _lines = source.split("\n")
    # A definition: "دالة_<anything>(...):" at end of line. Match on the
    # ALREADY-substituted text too, because the placeholder has replaced the
    # name by this point: "دالة_فيب(ن):" -> "دالة__APL_UDF_0_(ن):".
    _is_def = re.compile(r"^\s*دالة_\S*\s*\(.*\)\s*:\s*$")
    for _i, _l in enumerate(_lines):
        if _is_def.match(_l):
            continue
        # Any "دالة_" immediately followed by the placeholder token, at line
        # start OR mid-line ("ارجع دالة__APL_UDF_0_(...)"), loses the prefix.
        _lines[_i] = re.sub(r"دالة_(?=_APL_UDF_)", "", _l)
    source = "\n".join(_lines)


    lines = source.split("\n")
    result = []
    _class_indent = None      # indent of the innermost open class body
    import core.runner.transpiler as _tp
    _tp._IN_MATCH = False
    _ir.USER_ATTRIBUTES = set(re.findall(r"ذات\.([^\W\d]\w*)\s*=(?!=)", source))
    _global_names = set(_ir.USER_NAMES)
    _scopes = []
    for _source_index, line in enumerate(lines):
        _indent = len(line) - len(line.lstrip())
        if line.strip() and not line.lstrip().startswith('#'):
            while _scopes and _indent <= _scopes[-1][0]:
                _scopes.pop()
        _local_names = set()
        _signature = re.match(r"\s*(?:دالة\s+|دالة_|def\s+)[^ (]+\((.*?)\)", line)
        if _signature:
            _local_names = {p.split(':')[0].split('=')[0].strip().lstrip('*')
                            for p in _signature.group(1).split(',') if p.strip()}
            _scopes.append((_indent, _local_names))
        _ir.USER_NAMES = _global_names | set().union(*(names for _, names in _scopes))
        # Comprehension, lambda and exception bindings are user identifiers too.
        for _binding in re.finditer(r"(?:لكل|for|مثل)\s+([^\W\d]\w*)|\(([^()]+)\)\s*=>", line):
            _ir.USER_NAMES.update((_binding.group(1) or _binding.group(2)).replace(' ', '').split(','))
        try:
            _out = transpile_line(line)
            result.append(" " * _indent + f"# apl-source:{_origins[_source_index]}")
            result.append(_out)
        except SyntaxError as e:
            e.lineno = _origins[_source_index]
            e.offset = _indent + 1
            raise
        # Track class bodies so a method named "دالة_س" becomes "س" (def س).
        # A comment or blank line inside a method must NOT end the class — only
        # a real statement dedented back to column 0 does. (An earlier flag
        # version mis-fired on example 49 and broke a top-level function.)
        _s = _out.strip()
        if re.match(r"^\s*class\s+\S", _out):
            _class_indent = _indent
        elif _class_indent is not None:
            if _s and not _s.startswith("#") and _indent <= _class_indent:
                _class_indent = None
            elif re.match(r"^\s+def\s+", _out) and _indent > _class_indent:
                # strip the دالة_ prefix on methods (recursion is not needed
                # inside a class body, and Python rejects Arabic def names)
                _out = re.sub(r"^(\s+def\s+)دالة_", r"\1", _out)
                result[-1] = _out
        # leaving any match body ends case-context for a following حالة
        if not _s or (_s and not _s.startswith(("case ", "if ")) and _indent == 0):
            _tp._IN_MATCH = False
    code = "\n".join(result)

    needs = imports_for(code)
    if needs:
        code = "\n".join(needs) + "\n\n" + code

    # Restore protected user-defined function names
    for _tok, _nm in _udf_map.items():
        code = code.replace(_tok, _nm)
    code = code.replace("_APL_UDF_", "")
    # Definitions whose name came from a placeholder must lose the دالة_
    # prefix (call sites use the bare name). Recursive top-level functions
    # keep it — a blanket strip broke 14 examples.
    if _udf_map:
        # A definition is emitted as `def دالة_اسم(...)` (recursion-safe: the
        # recursive call site kept the same prefix). Its call sites use the bare
        # `اسم`, so emit an alias right after each such definition instead of
        # renaming it — renaming broke recursion, an alias does not.
        _names = "|".join(re.escape(n) for n in _udf_map.values())
        # The alias must go AFTER the function body, not right after the def
        # line (that split the body and broke indentation).
        _lines = code.split("\n")
        _alias_at = []
        for _i, _l in enumerate(_lines):
            _m = re.match(rf"^(\s*)def\s+دالة_({_names})\b", _l)
            if not _m:
                continue
            _ind = len(_m.group(1))
            _j = _i + 1
            while _j < len(_lines):
                _nxt = _lines[_j]
                if not _nxt.strip() or _nxt.lstrip().startswith("#"):
                    _j += 1
                    continue
                _n_ind = len(_nxt) - len(_nxt.lstrip())
                if _n_ind <= _ind:
                    break
                _j += 1
            _alias_at.append((_j, f"{_m.group(1)}{_m.group(2)} = دالة_{_m.group(2)}"))
        for _pos, _txt in sorted(_alias_at, reverse=True):
            _lines.insert(_pos, _txt)
        code = "\n".join(_lines)

    # Constant folding on the generated Python: pure-literal arithmetic becomes a
    # literal, so e.g. 2 ** 100 costs nothing at run time.
    if _APL_FOLD:
        from core.runner.constfold import fold_code
        code = fold_code(code)

    code = restore(code, _literals)
    # Interpolation expressions are translated during restoration, so discover
    # imports once more after literals have been restored.
    return "\n".join(imports_for(code)) + "\n" + code


_AR_MESSAGES = (
    (r"^division by zero$", "قسمة على صفر"),
    (r"^integer division or modulo by zero$", "قسمة على صفر"),
    (r"^list index out of range$", "الفهرس خارج حدود القائمة"),
    (r"^tuple index out of range$", "الفهرس خارج حدود المجموعة"),
    (r"^string index out of range$", "الفهرس خارج حدود النص"),
    (r"^'([^']+)' object is not subscriptable$", r"'\1' مش ممكن يتفهرس بالأقواس"),
    (r"^'([^']+)' object is not iterable$", r"'\1' مش ممكن نلف عليه"),
    (r"^'([^']+)' object is not callable$", r"'\1' مش دالة"),
    (r"^'([^']+)' object has no attribute '([^']+)'$",
     r"'\1' ماعندوش الخاصية '\2'"),
    (r"^name '([^']+)' is not defined$", r"الاسم '\1' مش معرّف"),
    (r"^unsupported operand type\(s\) for (.+?): '([^']+)' and '([^']+)'$",
     r"عملية \1 مش مسموحة بين '\2' و'\3'"),
    (r'^can only concatenate str \(not "(.+?)"\) to str$',
     r"مش ممكن نجمع نص مع \1"),
    (r"^invalid literal for int\(\) with base 10: '(.+)'$", r"'\1' مش رقم صحيح"),
    (r"^could not convert string to float: '(.+)'$", r"'\1' مش رقم"),
    (r"^math domain error$", "القيمة خارج نطاق العملية الرياضية"),
    (r"^\[Errno 2\] No such file or directory: '(.+)'$", r"الملف مش موجود: '\1'"),
    (r"^\[Errno 13\] Permission denied: '(.+)'$", r"مفيش صلاحية للوصول: '\1'"),
    (r"^not enough values to unpack.*$", "عدد القيم أقل من المطلوب"),
    (r"^too many values to unpack.*$", "عدد القيم أكبر من المطلوب"),
    (r"^maximum recursion depth exceeded.*$", "الاستدعاء المتكرر أعمق من المسموح"),
    (r"^object of type '(.+?)' has no len\(\)$", r"'\1' ماعندهاش طول"),
    (r"^empty separator$", "الفاصل فاضي"),
)


def _ar_message(error):
    # ترجم أشهر رسائل بايثون، وغير المعروف يفضل زي ما هو
    import re as _re
    text = error.args[0] if error.args and isinstance(error.args[0], str) else str(error)
    for pattern, replacement in _AR_MESSAGES:
        if _re.match(pattern, text):
            return _re.sub(pattern, replacement, text)
    return text


_RUNTIME = """
import sys
import builtins
import pathlib
import zoneinfo
import decimal
import fractions
import string
import enum
import secrets
import getpass
import operator
import pprint

_apl_orig_print = getattr(builtins.print, '_apl_orig', builtins.print)

def _apl_passthrough_decorator(func):
    # Bare Arabic decorator with no call parentheses: returns func unchanged.
    return func

class _apl_db:
    # Placeholder for Flask-SQLAlchemy style db.* keys; a real app assigns its own.
    Model = None
    session = None
    add = None
    delete = None
    commit = None
    rollback = None
    close = None
    flush = None
    refresh = None
    query = None
    cr = None

_apl_flask_db = _apl_db
_apl_db.session = _apl_db
_apl_db_placeholder = _apl_db

def _apl_bytes_to_text(b):
    # Render bytes as a readable string (base64 payloads are ASCII-safe)
    try:
        return b.decode("utf-8")
    except (UnicodeDecodeError, AttributeError):
        return b.decode("latin-1")


# --- batch-2 library runtime helpers -------------------------------------
def _D(x):
    import decimal as _dc
    return x if isinstance(x, _dc.Decimal) else _dc.Decimal(str(x))

def _apl_decimal_add(a, b): return _D(a) + _D(b)
def _apl_decimal_sub(a, b): return _D(a) - _D(b)
def _apl_decimal_mul(a, b): return _D(a) * _D(b)
def _apl_decimal_div(a, b, places=10):
    import decimal as _dc
    q = _dc.Decimal(1).scaleb(-places)
    return (_D(a) / _D(b)).quantize(q)
def _apl_decimal_mod(a, b): return _D(a) % _D(b)
def _apl_decimal_pow(a, b): return _D(a) ** _D(b)
def _apl_decimal_sqrt(a): return _D(a).sqrt()
def _apl_decimal_cmp(a, b): return (_D(a) > _D(b)) - (_D(a) < _D(b))
def _apl_decimal_copy(a): return +_D(a)
def _apl_decimal_quantize(a, places=2):
    import decimal as _dc
    return _D(a).quantize(_dc.Decimal(1).scaleb(-places))
def _apl_decimal_fma(a, b, c): return _D(a) * _D(b) + _D(c)

def _apl_secret_int(low, high=None):
    import secrets as _sc
    if high is None:
        return _sc.randbelow(low)
    return _sc.randbelow(high - low) + low

def _apl_fraction_value(f): return float(f)
def _apl_fraction_recip(f):
    import fractions as _fr
    return _fr.Fraction(1, 1) / f

def _apl_zone_from_key(key): return zoneinfo.ZoneInfo(key)

def _apl_operator_all(iterable): return builtins.all(iterable)
def _apl_operator_any(iterable): return builtins.any(iterable)
def _apl_operator_invert(n): return ~n
def _apl_operator_pow(a, b): return a ** b

def _apl_json_load_file(path, encoding="utf-8"):
    import json as _j
    with open(path, "r", encoding=encoding) as f:
        return _j.load(f)

def _apl_json_dump_file(obj, path, encoding="utf-8", indent=2):
    import json as _j
    with open(path, "w", encoding=encoding) as f:
        return _j.dump(obj, f, ensure_ascii=False, indent=indent)

def _apl_ap_add_argument(parser, *args, **kwargs):
    return parser.add_argument(*args, **kwargs)

def _apl_ap_add_argument_group(parser, *args, **kwargs):
    return parser.add_argument_group(*args, **kwargs)

def _apl_ap_parse_args(parser, args=None, namespace=None):
    return parser.parse_args(args, namespace)

def _apl_ap_parse_known_args(parser, args=None, namespace=None):
    return parser.parse_known_args(args, namespace)

def _apl_ap_format_help(parser):
    return parser.format_help()

def _apl_ap_print_help(parser):
    return parser.print_help()

def _apl_ap_parser_copy(parser):
    return parser

def _apl_super_init(*args, **kwargs):
    # استدعاء_الأب(صنف_الأب, ذات, ...) invokes the parent's __init__ directly.
    # A plain super() cannot be used here: the zero-argument form needs the
    # __class__ closure cell, which is only available inside a class body.
    if args and isinstance(args[0], type) and len(args) > 1 and not isinstance(args[1], type):
        صنف_الأب, rest = args[0], args[2:]
    elif len(args) > 1 and isinstance(args[1], type):
        صنف_الأب, rest = args[1], args[2:]
    else:
        صنف_الأب, rest = None, args[1:] if args else ()
    if صنف_الأب is None:
        return object.__init__(args[0]) if args else None
    return صنف_الأب.__init__(args[1] if len(args) > 1 and args[0] is صنف_الأب else args[0], *rest, **kwargs)

def _apl_path_exists(p):
    return pathlib.Path(p).exists()

def _apl_path_unlink(p):
    return pathlib.Path(p).unlink()

def _APL_SELF(method, *args, **kwargs):
    # Standalone form of a method alias: علوي("x") -> "x".upper()
    if not args:
        return method
    obj, rest = args[0], args[1:]
    if rest and isinstance(rest[0], str) and method in (str.split, str.startswith, str.endswith, str.replace):
        return getattr(obj, method)(rest[0], *rest[1:], **kwargs)
    return getattr(obj, method)(*rest, **kwargs)

def _apl_has_arabic(v):
    return any('\\u0600' <= c <= '\\u06FF' or '\\u0750' <= c <= '\\u07FF' or '\\u08A0' <= c <= '\\u08FF' or '\\uFB50' <= c <= '\\uFDFF' for c in str(v))

def _apl_print(*args, **kwargs):
    if any(_apl_has_arabic(a) for a in args):
        _apl_orig_print('\\u202B', *args, '\\u202C', **kwargs)
    else:
        _apl_orig_print(*args, **kwargs)

_apl_print._apl_orig = _apl_orig_print
builtins.print = _apl_print

def _apl_input(prompt=""):
    # اقرأ سطر واحد من المستخدم
    try:
        return builtins.input(prompt)
    except EOFError:
        return ""


def _apl_import_file(path, target=None):
    # شغّل ملف APL تاني جوه نفس النطاق
    import pathlib
    candidate = pathlib.Path(path)
    if not candidate.is_absolute() and target is not None:
        base = pathlib.Path(target.get("__file__") or ".").parent
        if (base / candidate).is_file():
            candidate = base / candidate
    if not candidate.is_file():
        raise FileNotFoundError(path)
    from core.runner.execution import Compilation
    namespace = target if target is not None else {}
    namespace.setdefault("__name__", candidate.stem)
    namespace["__file__"] = str(candidate)
    compilation = Compilation(candidate.read_text(encoding="utf-8"), str(candidate))
    exec(compilation.code, namespace)
    return namespace


def _apl_ar_message(error):
    from core.runner.main import _ar_message as _translate
    return _translate(error)


class _apl_error(Exception):
    # The object bound by "امسك مثل خطأ:". It is a real exception (so re-raising
    # works) whose message is the Arabic text of the error it wraps.
    def __init__(self, error):
        self.original = error
        super().__init__(_apl_ar_message(error))

    def __getattr__(self, name):
        return getattr(self.__dict__.get("original"), name)


def _apl_exception(error):
    return _apl_error(error)


def _apl_error_text(error):
    # رسالة(خطأ) - النص العربي للخطأ الممسوك
    return _apl_ar_message(error)


_ERROR_AR = {
    "SyntaxError": "خطأ في الصياغة",
    "NameError": "خطأ: متغير غير معروف",
    "TypeError": "خطأ في نوع البيانات",
    "ValueError": "خطأ في القيمة",
    "IndexError": "خطأ: الفهرس خارج النطاق",
    "KeyError": "خطأ: المفتاح غير موجود",
    "ZeroDivisionError": "خطأ: القسمة على صفر",
    "FileNotFoundError": "خطأ: الملف غير موجود",
    "ImportError": "خطأ: استيراد فاشل",
    "AttributeError": "خطأ: الخاصية غير موجودة",
    "EOFError": "خطأ: لا توجد بيانات إدخال",
    "IndentationError": "خطأ: مشكلة في المسافات",
    "StopIteration": "تم التوقف",
    "RuntimeError": "خطأ في التشغيل",
    "PermissionError": "خطأ: صلاحية مرفوضة",
    "TimeoutError": "خطأ: انتهاء الوقت",
    "ConnectionError": "خطأ: فشل الاتصال",
    "OSError": "خطأ: نظام التشغيل",
    "OverflowError": "خطأ: تجاوز السعة",
    "RecursionError": "خطأ: استدعاء متكرر عميق",
    "ModuleNotFoundError": "خطأ: الوحدة غير موجودة",
    "AssertionError": "خطأ: التأكيد فشل",
    "JSONDecodeError": "خطأ: نص JSON غير صالح",
    "UnicodeDecodeError": "خطأ: ترميز النص غير مفهوم",
    "FileExistsError": "خطأ: الملف موجود بالفعل",
    "IsADirectoryError": "خطأ: ده مجلد مش ملف",
    "NotADirectoryError": "خطأ: ده ملف مش مجلد",
    "KeyboardInterrupt": "توقف بواسطة المستخدم",
}

_old_excepthook = sys.excepthook
def _apl_excepthook(typ, val, tb):
    name = _ERROR_AR.get(typ.__name__, typ.__name__)
    import traceback
    traceback.print_exception(typ, val, tb)
    sys.stderr.write(f"\\u202B{name}: {_apl_ar_message(val)}\\u202C\\n")
sys.excepthook = _apl_excepthook

def _apl_enum(name, spec, base=None):
    # تعداد("الحالة", "نشط، معطل، pending") -> a real enum class.
    # Members are numbered from 1 in the order given; the Arabic member names
    # are valid Python identifiers, so the class exposes them directly.
    import enum as _enum
    members = {}
    for i, raw in enumerate(str(spec).replace("\u060c", ",").split(","), 1):
        key = raw.strip()
        if not key:
            continue
        members[key] = i
    _base = base or _enum.Enum
    return _enum.Enum(name, members, type=_base) if _base is not _enum.Enum \
        else _enum.Enum(name, members)

def _apl_enum_value(cls, key):
    return cls[key].value

def _apl_enum_all_names(cls):
    return [m.name for m in cls]

def _apl_enum_all_values(cls):
    return [m.value for m in cls]

def _apl_enum_has_value(cls, v):
    return v in [m.value for m in cls]

def _apl_read(target, mode="r", encoding="utf-8"):
    # اقرأ(file) or اقرأ(open_handle)
    if hasattr(target, "read"):
        return target.read()
    with open(target, mode, encoding=encoding) as _f:
        return _f.read()

def _apl_write(target, s, mode="w", encoding="utf-8"):
    # اكتب(file, s) or اكتب(open_handle, s)
    if hasattr(target, "write"):
        return target.write(s)
    with open(target, mode, encoding=encoding) as _f:
        return _f.write(s)

def _apl_close(target=None):
    if target is not None and hasattr(target, "close"):
        return target.close()

def _apl_fetch(url):
    return urllib.request.urlopen(url).read().decode("utf-8")


# --- xml.etree.ElementTree helpers --------------------------------------
# Every helper imports the module lazily, so an APL program that never touches
# XML never pays for the ElementTree import.
def _apl_xml_et():
    import xml.etree.ElementTree as _ET
    return _ET

def _apl_xml_parse(source, parser=None):
    # اقرأ_إكس_إم_إل("ملف.xml") -> جذر الشجرة (ElementTree.parse)
    return _apl_xml_et().parse(source, parser=parser)

def _apl_xml_safe_parse(source, parser=None):
    # نفس القراءة لكن ترفض أي مرجع خارجي (حماية من هجمات XXE)
    return _apl_xml_et().parse(source, parser=_apl_xml_et().XMLParser())

def _apl_xml_fromstring(text, parser=None):
    return _apl_xml_et().fromstring(text, parser=parser)

def _apl_xml_fromstringlist(sequence, parser=None):
    return _apl_xml_et().fromstringlist(sequence, parser=parser)

def _apl_xml_tostring(element, encoding="unicode", **kwargs):
    # النص العربي يجب أن يبقى عربياً: encoding="unicode" افتراضياً
    return _apl_xml_et().tostring(element, encoding=encoding, **kwargs)

def _apl_xml_tostring_raw(element, encoding="utf-8", **kwargs):
    return _apl_xml_et().tostring(element, encoding=encoding, **kwargs)

def _apl_xml_tolist(element, encoding="unicode", **kwargs):
    # قائمة أجزاء النص (str افتراضياً، حتى يبقى العربي مقروءاً)
    return _apl_xml_et().tostringlist(element, encoding=encoding, **kwargs)

def _apl_xml_canonicalize(xml_data=None, **kwargs):
    return _apl_xml_et().canonicalize(xml_data, **kwargs)

def _apl_xml_save(element, path, encoding="utf-8", **kwargs):
    # احفظ_إكس_إم_إل(جذر, "ملف.xml") — يقبل Element أو ElementTree
    _t = _apl_xml_et()
    tree = element if isinstance(element, _t.ElementTree) else _t.ElementTree(element)
    tree.write(path, encoding=encoding, **kwargs)
    return path

def _apl_xml_dump(element, **kwargs):
    print(_apl_xml_tostring(element, **kwargs))
    return element

def _apl_xml_element(tag, attrib=None, **kwargs):
    return _apl_xml_et().Element(tag, attrib if attrib is not None else {}, **kwargs)

def _apl_xml_subelement(parent, tag, attrib=None, **kwargs):
    # SubElement ينشئ الابن ويضيفه للأب في خطوة واحدة (makeelement لا يضيف)
    return _apl_xml_et().SubElement(parent, tag, attrib if attrib is not None else {}, **kwargs)

def _apl_xml_tree(element=None, file=None):
    _t = _apl_xml_et()
    return _t.ElementTree(element) if element is not None else _t.ElementTree(file=file)

def _apl_xml_treebuilder(element_factory=None):
    _t = _apl_xml_et()
    return _t.TreeBuilder(element_factory=element_factory) if element_factory else _t.TreeBuilder()

def _apl_xml_pull_parser(events=None):
    _t = _apl_xml_et()
    return _t.XMLPullParser(events=events or ("end",))

def _apl_xml_children(element, tag=None):
    return list(element) if tag is None else list(element.findall(tag))

def _apl_xml_count(element, tag=None):
    return len(element) if tag is None else len(element.findall(tag))

def _apl_xml_text(element):
    return "".join(element.itertext())

def _apl_xml_path(root, element):
    # احسب_المسار(الجذر, العنصر) -> مسار مطلق بصيغة /أب/ابن
    index = {child: parent for parent in root.iter() for child in parent}

    def _segment(node):
        tag = node.tag if isinstance(node.tag, str) else str(node.tag)
        parent = index.get(node)
        siblings = [c for c in (list(parent) if parent is not None else []) if c.tag == node.tag]
        if len(siblings) <= 1:
            return tag
        return tag + "[" + str(siblings.index(node) + 1) + "]"

    parts = []
    node = element
    while node is not None:
        parts.append(_segment(node))
        node = index.get(node)
    # المسار يبدأ دائماً بالجذر: /طلاب/طالب[1]
    return "/" + "/".join(reversed(parts))

def _apl_xml_by_id(element, target):
    for node in element.iter():
        if node.get("id") == target:
            return node
    return None

def _apl_xml_copy(element):
    tmpl = element.makeelement(element.tag, dict(element.attrib))
    tmpl.text = element.text
    tmpl.tail = element.tail
    for child in element:
        tmpl.append(_apl_xml_copy(child))
    return tmpl

def _apl_xml_namespace(tag):
    if isinstance(tag, str) and tag.startswith("{"):
        end = tag.find("}")
        return tag[1:end] if end > 0 else ""
    return ""

def _apl_xml_register_namespace(prefix, uri):
    _apl_xml_et().register_namespace(prefix, uri)
    return prefix

def _apl_xml_get(element, key, default=None):
    # اقرأ_خاصية(عنصر, "الاسم") — الصيغة الحرة لعنصر.اقرأ_خاصية("الاسم")
    return element.get(key, default)

def _apl_xml_set(element, key, value):
    # عين_خاصية(عنصر, "الاسم", "قيمة") — الصيغة الحرة لعنصر.عين_خاصية(...)
    element.set(key, value)
    return element

def _apl_xml_find(element, path, namespaces=None):
    # الصيغة الحرة لعنصر.ابحث_عنصر: تجد(الجذر, "كتاب")
    return element.find(path, namespaces) if namespaces else element.find(path)

def _apl_xml_findall(element, path, namespaces=None):
    return element.findall(path, namespaces) if namespaces else element.findall(path)

def _apl_xml_findtext(element, path, default=None, namespaces=None):
    return element.findtext(path, default, namespaces)

def _apl_xml_append(parent, child):
    parent.append(child)
    return child

def _apl_xml_remove(parent, child):
    parent.remove(child)
    return parent

def _apl_xml_clear(element):
    element.clear()
    return element

def _apl_xml_set_text(element, text):
    element.text = text
    return element

def _apl_xml_set_tail(element, text):
    element.tail = text
    return element

def _apl_xml_event_start(tag, attrs):
    # باني.ابدأ("صنف", {"سعر": "2"}) — حدث بداية وسم للباني
    if hasattr(tag, "start"):
        return tag.start(tag, attrs)
    return (tag, attrs)

def _apl_xml_event_end(tag):
    # باني.أنهِ("صنف")
    if hasattr(tag, "end"):
        return tag.end(tag)
    return tag

def _apl_xml_indent(tree, space="  ", level=0):
    # رتّب_الشجرة(الجذر) — إخراج مُزاح بصرياً (ElementTree.indent من 3.9+)
    _t = _apl_xml_et()
    target = tree.getroot() if isinstance(tree, _t.ElementTree) else tree
    if hasattr(_t, "indent"):
        _t.indent(target, space=space, level=level)
    return tree

def _apl_xml_pretty(element, space="  "):
    # نسخة منسّقة من الشجرة (لا تعدّل الأصل) ثم إرجاع النص
    copy = _apl_xml_copy(element.getroot() if isinstance(element, _apl_xml_et().ElementTree) else element)
    _apl_xml_indent(copy, space)
    return _apl_xml_tostring(copy)

def _apl_xml_strip(element):
    # أزل_المسافات(عنصر) — حذف النصوص والذيل المكوّنة من مسافات فقط
    for node in element.iter():
        if node.text is not None and not node.text.strip():
            node.text = None
        if node.tail is not None and not node.tail.strip():
            node.tail = None
    return element

def _apl_xml_set_tag(element, tag):
    element.tag = tag
    return element

def _apl_xml_set_attrib(element, attrib):
    element.attrib.clear()
    element.attrib.update(attrib)
    return element

def _apl_xml_check(text, parser=None):
    # تحقق_من_عنصر(نص) -> صحيح/خطأ (مناسب للاستخدام مباشرة داخل لو)
    try:
        _apl_xml_et().fromstring(text, parser=parser)
        return True
    except Exception:
        return False

def _apl_xml_check_message(text, parser=None):
    # خطأ_التحقق(نص) -> رسالة الخطأ، أو نص فارغ إن كانت الصياغة صحيحة
    try:
        _apl_xml_et().fromstring(text, parser=parser)
        return ""
    except Exception as exc:
        return str(exc)

# --- archive / compression helpers (zipfile, tarfile, gzip, bz2, lzma) ------
# --- archive / compression helpers (zipfile, tarfile, gzip, bz2, lzma) ------
# Same rule as the XML helpers: each one imports its module inside its body so
# a program that never touches an archive pays nothing at startup.
def _apl_archive_bytes(data):
    if isinstance(data, str):
        return data.encode("utf-8")
    return data

def _apl_archive_text(data):
    if isinstance(data, (bytes, bytearray)):
        return bytes(data).decode("utf-8", "replace")
    return data

def _apl_archive_as_list(items):
    if items is None:
        return []
    if isinstance(items, (str, bytes)):
        return [items]
    return list(items)

def _apl_archive_safe_name(name):
    # رفض أي عضو يحاول الخروج عن مجلد الاستخراج (zip-slip)
    norm = str(name).replace("\\\\", "/")
    if norm.startswith("/") or (len(norm) > 1 and norm[1] == ":"):
        raise ValueError("عضو غير آمن (مسار مطلق): " + str(name))
    if ".." in norm.split("/"):
        raise ValueError("عضو غير آمن (خروج عن المجلد): " + str(name))
    return name

def _apl_file_size(path):
    import os
    return os.path.getsize(path)

def _apl_size_human(size, decimals=1):
    units = ["بايت", "ك.ب", "م.ب", "ج.ب", "ت.ب"]
    value = float(size)
    index = 0
    while value >= 1024 and index < len(units) - 1:
        value /= 1024.0
        index += 1
    if index == 0:
        return "%d بايت" % int(value)
    return ("%." + str(int(decimals)) + "f %s") % (value, units[index])

def _apl_compression_ratio(original, compressed):
    original = float(original)
    if original <= 0:
        return 0.0
    return round(float(compressed) / original * 100.0, 2)

# ---------- ZIP ----------
def _apl_zip_open(path, mode="r", compression=None, compresslevel=None):
    import zipfile
    kwargs = {}
    if mode[:1] in ("w", "x"):
        kwargs["compression"] = zipfile.ZIP_DEFLATED if compression is None else compression
    elif compression is not None:
        kwargs["compression"] = compression
    if compresslevel is not None:
        kwargs["compresslevel"] = compresslevel
    return zipfile.ZipFile(path, mode, **kwargs)

def _apl_zip_read_open(path, **kwargs):
    return _apl_zip_open(path, "r", **kwargs)

def _apl_zip_is(path):
    import zipfile
    return zipfile.is_zipfile(path)

def _apl_zip_names(path):
    import zipfile
    with zipfile.ZipFile(path) as archive:
        return archive.namelist()

def _apl_zip_count(path):
    return len(_apl_zip_names(path))

def _apl_zip_contains(path, member):
    return member in _apl_zip_names(path)

def _apl_zip_info(path, member):
    import zipfile
    with zipfile.ZipFile(path) as archive:
        return archive.getinfo(member)

def _apl_zip_read_bytes(path, member, pwd=None):
    import zipfile
    with zipfile.ZipFile(path) as archive:
        if pwd is not None:
            archive.setpassword(_apl_archive_bytes(pwd))
        return archive.read(member)

def _apl_zip_read(path, member, pwd=None):
    return _apl_archive_text(_apl_zip_read_bytes(path, member, pwd))

def _apl_zip_uncompressed(path):
    with_open = _apl_zip_open(path, "r")
    with with_open as archive:
        return sum(info.file_size for info in archive.infolist())

def _apl_zip_stats(path):
    with _apl_zip_open(path, "r") as archive:
        infos = archive.infolist()
        raw = sum(info.file_size for info in infos)
        packed = sum(info.compress_size for info in infos)
    return {
        "عدد_الأعضاء": len(infos),
        "الحجم_الأصلي": raw,
        "الحجم_المضغوط": packed,
        "نسبة_الضغط": _apl_compression_ratio(raw, packed),
        "الحجم_المقروء": _apl_size_human(packed),
    }

def _apl_zip_summary(path):
    with _apl_zip_open(path, "r") as archive:
        infos = archive.infolist()
        lines = []
        raw = 0
        packed = 0
        for info in infos:
            raw += info.file_size
            packed += info.compress_size
            lines.append(
                "%s  |  %s ← %s" % (
                    info.filename,
                    _apl_size_human(info.compress_size),
                    _apl_size_human(info.file_size),
                )
            )
        lines.append(
            "الإجمالي: %d عضواً | %s مضغوط من %s (%.2f%%)" % (
                len(infos), _apl_size_human(packed), _apl_size_human(raw),
                _apl_compression_ratio(raw, packed),
            )
        )
        return lines

def _apl_zip_print(path):
    lines = _apl_zip_summary(path)
    for line in lines:
        print(line)
    return lines

def _apl_zip_create(path, items=None, compresslevel=None):
    import os
    import zipfile
    entries = _apl_archive_as_list(items)
    kwargs = {"compression": zipfile.ZIP_DEFLATED}
    if compresslevel is not None:
        kwargs["compresslevel"] = compresslevel
    with zipfile.ZipFile(path, "w", **kwargs) as archive:
        for entry in entries:
            if os.path.isdir(entry):
                base = os.path.dirname(os.path.abspath(entry))
                for root, dirs, files in os.walk(entry):
                    dirs.sort()
                    for name in sorted(files):
                        full = os.path.join(root, name)
                        archive.write(full, os.path.relpath(full, base))
            elif os.path.exists(entry):
                archive.write(entry, os.path.basename(entry))
            else:
                raise FileNotFoundError("العنصر غير موجود: " + str(entry))
    return path

def _apl_zip_add(path, items, compresslevel=None):
    import os
    import zipfile
    entries = _apl_archive_as_list(items)
    kwargs = {}
    if compresslevel is not None:
        kwargs["compresslevel"] = compresslevel
    with zipfile.ZipFile(path, "a", **kwargs) as archive:
        for entry in entries:
            if os.path.isdir(entry):
                base = os.path.dirname(os.path.abspath(entry))
                for root, dirs, files in os.walk(entry):
                    dirs.sort()
                    for name in sorted(files):
                        full = os.path.join(root, name)
                        archive.write(full, os.path.relpath(full, base))
            elif os.path.exists(entry):
                archive.write(entry, os.path.basename(entry))
            else:
                raise FileNotFoundError("العنصر غير موجود: " + str(entry))
    return path

def _apl_zip_remove(path, members):
    import os
    import zipfile
    names = set(_apl_archive_as_list(members))
    temp = str(path) + ".tmp"
    with zipfile.ZipFile(path) as source:
        with zipfile.ZipFile(temp, "w", compression=zipfile.ZIP_DEFLATED) as target:
            for info in source.infolist():
                if info.filename in names:
                    continue
                target.writestr(info, source.read(info.filename))
    os.replace(temp, path)
    return sorted(names)

def _apl_zip_extract(path, dest=".", members=None, pwd=None):
    import os
    import zipfile
    names = members if members is not None else None
    if isinstance(names, (str, bytes)):
        names = [names]
    with zipfile.ZipFile(path) as archive:
        targets = list(names) if names is not None else archive.namelist()
        for name in targets:
            _apl_archive_safe_name(name)
        if pwd is not None:
            archive.setpassword(_apl_archive_bytes(pwd))
        os.makedirs(dest, exist_ok=True)
        archive.extractall(dest, members=names)
        return targets

# ---------- TAR ----------
def _apl_tar_open(path, mode="r:*"):
    import tarfile
    return tarfile.open(path, mode)

def _apl_tar_is(path):
    import tarfile
    return tarfile.is_tarfile(path)

def _apl_tar_names(path):
    import tarfile
    with tarfile.open(path, "r:*") as archive:
        return archive.getnames()

def _apl_tar_members(path):
    import tarfile
    with tarfile.open(path, "r:*") as archive:
        return archive.getmembers()

def _apl_tar_info(path, member):
    import tarfile
    with tarfile.open(path, "r:*") as archive:
        return archive.getmember(member)

def _apl_tar_read(path, member):
    import tarfile
    with tarfile.open(path, "r:*") as archive:
        handle = archive.extractfile(member)
        if handle is None:
            raise ValueError("العضو ليس ملفاً عادياً: " + str(member))
        return _apl_archive_text(handle.read())

def _apl_tar_create(path, items=None, mode="w:gz"):
    import os
    import tarfile
    entries = _apl_archive_as_list(items)
    with tarfile.open(path, mode) as archive:
        for entry in entries:
            if os.path.exists(entry):
                archive.add(entry, arcname=os.path.basename(entry))
            else:
                raise FileNotFoundError("العنصر غير موجود: " + str(entry))
    return path

def _apl_tar_add(path, items, mode="a"):
    import os
    import tarfile
    entries = _apl_archive_as_list(items)
    with tarfile.open(path, mode) as archive:
        for entry in entries:
            if os.path.exists(entry):
                archive.add(entry, arcname=os.path.basename(entry))
            else:
                raise FileNotFoundError("العنصر غير موجود: " + str(entry))
    return path

def _apl_tar_extract(path, dest=".", members=None):
    import os
    import tarfile
    names = members
    if isinstance(names, (str, bytes)):
        names = [names]
    with tarfile.open(path, "r:*") as archive:
        targets = list(names) if names is not None else archive.getnames()
        for name in targets:
            _apl_archive_safe_name(name)
        os.makedirs(dest, exist_ok=True)
        kwargs = {}
        try:
            import inspect
            if "filter" in inspect.signature(archive.extractall).parameters:
                kwargs["filter"] = "data"
        except Exception:
            kwargs = {}
        archive.extractall(dest, members=names, **kwargs)
        return targets

# ---------- gzip / bz2 / lzma ----------
def _apl_gzip_compress(data, compresslevel=9):
    import gzip
    return gzip.compress(_apl_archive_bytes(data), compresslevel=int(compresslevel))

def _apl_gzip_decompress(data):
    import gzip
    return _apl_archive_text(gzip.decompress(_apl_archive_bytes(data)))

def _apl_bz2_compress(data, compresslevel=9):
    import bz2
    return bz2.compress(_apl_archive_bytes(data), compresslevel=int(compresslevel))

def _apl_bz2_decompress(data):
    import bz2
    return _apl_archive_text(bz2.decompress(_apl_archive_bytes(data)))

def _apl_lzma_compress(data, compresslevel=None):
    import lzma
    preset = 6 if compresslevel is None else int(compresslevel)
    return lzma.compress(_apl_archive_bytes(data), preset=preset)

def _apl_lzma_decompress(data):
    import lzma
    return _apl_archive_text(lzma.decompress(_apl_archive_bytes(data)))

def _apl_gz_read_file(path):
    import gzip
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as handle:
        return handle.read()

def _apl_gz_write_file(path, text):
    import gzip
    with gzip.open(path, "wt", encoding="utf-8") as handle:
        handle.write(_apl_archive_text(text))
    return path

def _apl_gz_file(source, dest=None):
    import gzip
    import shutil
    target = dest or (str(source) + ".gz")
    with open(source, "rb") as reader, gzip.open(target, "wb") as writer:
        shutil.copyfileobj(reader, writer)
    return target

def _apl_gz_unfile(source, dest=None):
    import gzip
    import shutil
    target = dest or (str(source)[:-3] if str(source).endswith(".gz") else str(source) + ".out")
    with gzip.open(source, "rb") as reader, open(target, "wb") as writer:
        shutil.copyfileobj(reader, writer)
    return target

def _apl_bz2_read_file(path):
    import bz2
    with bz2.open(path, "rt", encoding="utf-8", errors="replace") as handle:
        return handle.read()

def _apl_bz2_write_file(path, text):
    import bz2
    with bz2.open(path, "wt", encoding="utf-8") as handle:
        handle.write(_apl_archive_text(text))
    return path

def _apl_lzma_read_file(path):
    import lzma
    with lzma.open(path, "rt", encoding="utf-8", errors="replace") as handle:
        return handle.read()

def _apl_lzma_write_file(path, text):
    import lzma
    with lzma.open(path, "wt", encoding="utf-8") as handle:
        handle.write(_apl_archive_text(text))
    return path

def _apl_archive_detect(path):
    import os
    import zipfile
    try:
        import tarfile
        if tarfile.is_tarfile(path):
            return "TAR"
    except Exception:
        pass
    if zipfile.is_zipfile(path):
        return "ZIP"
    lower = str(path).lower()
    for suffix, kind in ((".tar.gz", "TAR"), (".tgz", "TAR"), (".tar.bz2", "TAR"),
                         (".tar.xz", "TAR"), (".tar", "TAR"), (".gz", "GZIP"),
                         (".bz2", "BZ2"), (".xz", "XZ"), (".lzma", "LZMA"),
                         (".zip", "ZIP")):
        if lower.endswith(suffix):
            return kind
    return "غير معروف"

def _apl_archive_open(path, mode="r"):
    import zipfile
    if zipfile.is_zipfile(path):
        return zipfile.ZipFile(path, mode)
    import tarfile
    tar_mode = mode if mode not in ("r", "w") else ("r:*" if mode == "r" else "w:gz")
    return tarfile.open(path, tar_mode)

# --- network helpers (socket, ssl, email, smtp, imap, ftp) -------------------
# Same contract as the archive helpers: every import happens inside the body,
# so a program that never touches the network imports nothing here.
def _apl_net_close(conn):
    # أغلق_مقبس(م) works for a socket object and for a raw file descriptor.
    import socket
    if hasattr(conn, "close"):
        return conn.close()
    return socket.close(conn)

def _apl_net_bytes(data, encoding="utf-8"):
    # أرسل_بيانات("نص") is accepted just like bytes.
    if isinstance(data, str):
        return data.encode(encoding)
    return data

def _apl_net_text(data, encoding="utf-8"):
    if isinstance(data, (bytes, bytearray)):
        return bytes(data).decode(encoding, "replace")
    return data

def _apl_net_addr(address):
    # Accepts ("host", port), "host:port" or ["host", port] and returns a tuple.
    if isinstance(address, str):
        host, _, port = address.rpartition(":")
        return (host or "127.0.0.1", int(port))
    return tuple(address)

def _apl_net_send(conn, data):
    import socket
    sock = conn if hasattr(conn, "sendall") else socket.socket(fileno=conn)
    payload = _apl_net_bytes(data)
    sock.sendall(payload)
    return len(payload)

def _apl_net_recv(conn, size=4096):
    import socket
    sock = conn if hasattr(conn, "recv") else socket.socket(fileno=conn)
    return _apl_net_text(sock.recv(size))

def _apl_net_send_text(conn, data, encoding="utf-8"):
    payload = _apl_net_bytes(data, encoding)
    conn["socket"].sendall(payload) if isinstance(conn, dict) else conn.sendall(payload)
    return len(payload)

def _apl_ssl_context(cafile=None, capath=None, cadata=None, تحقق=True):
    # سياق_آمن_افتراضي() with an Arabic switch:
    #   سياق_آمن_افتراضي(تحقق = خطأ)  -> no certificate check (local testing)
    # The parameter name is Arabic on purpose: the call site already reads
    # `تحقق = خطأ`, so no keyword mapping is needed.
    import ssl
    context = ssl.create_default_context(cafile=cafile, capath=capath, cadata=cadata)
    if not تحقق:
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
    return context

def _apl_email_attach(message, data, filename=None, subtype=None, cid=None):
    # أضف_مرفقاً(بايتات, اسم_الملف = "...") without guessing the MIME type.
    import mimetypes
    import os
    if isinstance(data, str) and os.path.isfile(data):
        filename = filename or os.path.basename(data)
        with open(data, "rb") as handle:
            data = handle.read()
    guess_name = filename or "attachment.bin"
    mime, _ = mimetypes.guess_type(guess_name)
    maintype, _, sub = (mime or "application/octet-stream").partition("/")
    message.add_attachment(data, maintype=maintype, subtype=subtype or sub, filename=filename, cid=cid)
    return message

def _apl_email_body_list(message):
    # أجزاء_الرسالة(ر) -> قائمة الأجزاء المفكوكة، مفيدة لكل جزء في ...
    return list(message.walk())

def _apl_http_status(response):
    return int(response.status)

def _apl_http_text(response, encoding="utf-8"):
    return response.read().decode(encoding, "replace")

def _apl_http_json(response):
    import json
    return json.loads(_apl_http_text(response))
"""


def run_file(filepath: str):
    from core.runner.execution import execute_file
    execute_file(filepath)


def _get_error_ar(e: Exception) -> str:
    name = type(e).__name__
    ar_name = {
        "SyntaxError": "خطأ في الصياغة",
        "NameError": "خطأ: متغير غير معروف",
        "TypeError": "خطأ في نوع البيانات",
        "ValueError": "خطأ في القيمة",
        "IndexError": "خطأ: الفهرس خارج النطاق",
        "KeyError": "خطأ: المفتاح غير موجود",
        "ZeroDivisionError": "خطأ: القسمة على صفر",
        "FileNotFoundError": "خطأ: الملف غير موجود",
        "ImportError": "خطأ: استيراد فاشل",
        "AttributeError": "خطأ: الخاصية غير موجودة",
        "EOFError": "خطأ: لا توجد بيانات إدخال",
        "IndentationError": "خطأ: مشكلة في المسافات",
        "RuntimeError": "خطأ في التشغيل",
        "PermissionError": "خطأ: صلاحية مرفوضة",
        "OSError": "خطأ: نظام التشغيل",
        "ConnectionError": "خطأ: فشل الاتصال",
        "ModuleNotFoundError": "خطأ: الوحدة غير موجودة",
        "OverflowError": "خطأ: تجاوز السعة",
        "JSONDecodeError": "خطأ: نص JSON غير صالح",
        "UnicodeDecodeError": "خطأ: ترميز النص غير مفهوم",
        "FileExistsError": "خطأ: الملف موجود بالفعل",
        "IsADirectoryError": "خطأ: ده مجلد مش ملف",
        "NotADirectoryError": "خطأ: ده ملف مش مجلد",
    }.get(name, name)
    return f"{ar_name}: {_ar_message(e)}"


def transpile_to_code(source: str) -> str:
    return transpile(source)


def _library_folder_hint():
    """Where installed libraries live."""
    from core.libraries.registry import library_home
    return library_home()


def print_library_help():
    """Print the Arabic vocabulary of every installed library."""
    if not ENTRIES:
        print("مفيش مكتبات مثبتة، فمفيش كلمات إضافية تعرضها.")
        return
    for _entry in ENTRIES:
        _mod = _library_modules[_entry['name']]
        _lines = []
        for _attr in dir(_mod):
            if _attr.endswith('_HELP'):
                _value = getattr(_mod, _attr)
                if isinstance(_value, (list, tuple)):
                    _lines = list(_value)
                    break
        print(f"  # مكتبة {_entry['name']}")
        for _line in _lines:
            print(f"    {_line}")
        print()


def print_help():
    """Print help information"""
    print("APL - Ammar Programming Language")
    print("مبنية على Python - رخصة PSF-2.0 | https://www.python.org/psf/license/")
    print()
    print("الاستخدام:")
    print("  عمار شغل ملف.apl [وسائط]   تشغيل برنامج APL")
    print("  عمار فحص ملف.apl           فحص الصياغة بدون تشغيل")
    print("  عمار ترجمة ملف.apl         طباعة كود Python المترجم")
    print("  عمار طرفية                 موجه تفاعلي")
    print("  عمار -c '<كود>'            تنفيذ كود مباشرة")
    print("  عمار بناء ملف.apl          ملف تنفيذي مستقل للبرنامج")
    print("  عمار تتبع ملف.apl          عرض كل سطر بيتنفّذ")
    print("  عمار مصحح ملف.apl          مصحح خطوة بخطوة (--توقف 3,7)")
    print("  عمار تنسيق ملف.apl         تنسيق الكود (--كتابة يحفظ)")
    print("  عمار مسار ثبت              إضافة عمار للـ PATH")
    print("  عمار مشروع جديد <اسم>      مجلد مشروع جديد")
    print("  عمار مشروع تشغيل           تشغيل المشروع الحالي")
    print("  عمار مكتبة تحميل <اسم>     تحميل مكتبة")
    print("  عمار مكتبة قائمة           المكتبات المثبتة")
    print("  عمار نسخة                  رقم الإصدار")
    print("  عمار مساعدة                هذه المساعدة")
    print("  عمار مسح-الكاش             حذف الترجمات المخزنة")
    print()
    print("  python apl.py ملف.apl      نفس الأمر بدون التثبيت (لو مش مثبت)")
    print()
    print("Environment switches:")
    print("  APL_NO_CACHE=1   Disable the transpilation cache")
    print("  APL_NO_FOLD=1    Disable constant folding")
    print()
    print("ميزات اللغة:")
    print("  حاول: / امسك مثل خطأ: / أخيراً:   معالجة الأخطاء")
    print("  صنف اسم: + دالة_إنشاء(ذات, ...)   الأصناف والكائنات")
    print("  استورد \"ملف.apl\"                   استيراد ملف APL تاني")
    print("  اقرأ/اكتب/ادخل                    ملفات وإدخال من المستخدم")
    print("  (س) => س * 2                       دوال مختصرة")
    print("  [ع * 2 لكل ع في قائمة]             فهم القوائم")
    print("  \"أهلاً {الاسم}\"                      نص منسّق بالقيم")
    print("  عمار لوحده                         موجّه تفاعلي")
    print()
    print("Language keywords:")
    lang_cmds = [
        "المتغير x = y       - متغير",
        "اطبع / اطبع_بدون     - طباعة",
        "ادخل(...)            - إدخال",
        "لو / الا لو / الا    - شرط",
        "طالما شرط:           - while",
        "لكل x في y:          - for",
        "دالة / ارجع          - function / return",
        "سهم x, y: expr       - lambda",
        "مولد / توقف / اكمل   - yield / break / continue",
        "حاول / إمسك          - try / except",
        "تأكد(شرط)            - assert",
        "خاصية / محدد / محدد_حذف - property/setter/deleter",
        "صنف/قاعدة / تمرير    - class / pass",
        "خاص / عام            - private / public",
        "حالة / قيمة / افتراضي - match / case",
        "مع .. مثل            - with .. as",
        "حذف / أبدا           - del / while True",
        "استورد / من..استورد   - import",
        "فتح / اقرأ / اكتب / اغلق - ملفات",
        "طلب(url)             - HTTP",
        "من(س, نوع)           - isinstance",
        "صحيح/نص/عشري/منطق   - int/str/float/bool",
        "قائمة/مجموعة/مصفوفة/قاموس - list/tuple/set/dict",
        "نطاق/طول            - range/len",
        "عدد                  - enumerate",
        "ط/ه/تاو/لانهائي_موجب - pi/e/tau/inf",
        ".تقسيم/.أضف/.ضم     - .split/.append/.join",
        ".علوي/.سفلي/.تقليم  - .upper/.lower/.strip",
        ".استبدال/.بداية/.نهاية - .replace/.startswith/.endswith",
        ".اتحاد/.تقاطع/.فرق   - .union/.intersection/.difference",
        "و / أو / ليس / مثل / في - and/or/not/as/in",
        "صواب / خطأ / لا_شيء  - True / False / None",
    ]
    for cmd in lang_cmds:
        print(f"  {cmd}")
    
    print()
    if ENTRIES:
        print("المكتبات المثبتة:")
        print("  " + "، ".join(entry['name'] for entry in ENTRIES))
        print("  تفاصيل كل مكتبة: عمار مساعدة مكتبات")
    else:
        print("المكتبات: مفيش مكتبات مثبتة. اللغة نفسها مش محتاجة أي مكتبة.")
        print("  مجلد المكتبات: " + str(_library_folder_hint()))
    print()
    print("أمثلة:")
    print("  عمار شغل hello.apl")
    print("  عمار -c 'اطبع \"أهلاً بالعالم\"'")
    print("  عمار طرفية")


__version__ = "1.13"


def run_repl():
    """Run interactive REPL"""
    print("APL - لغة عمار البرمجية")
    print("الطرفية التفاعلية — اكتب خروج (أو Ctrl+D) للخروج")
    print("سطر بينتهي بـ ':' بيكمّل على أسطر لحد سطر فاضي.")
    print()

    # One shared namespace for the whole session, so variables survive between
    # lines (and the runtime prologue is executed only once).
    _namespace = {"__name__": "__console__"}
    exec(_RUNTIME, _namespace)
    from core.runner.interactive import configure, evaluate
    configure(_namespace)

    while True:
        try:
            line = input(">>> ")
        except EOFError:          # end of piped input / Ctrl+D
            print()
            break
        except KeyboardInterrupt:
            print("\nمع السلامة 👋")
            break

        if line.strip().lower() in ('exit', 'اخرج', 'quit', 'خروج', 'خ'):
            print("مع السلامة 👋")
            break
        if not line.strip():
            continue

        # A block header (ends with ":") keeps reading indented lines, so
        # `دالة س(ص):` + body works exactly like in a file.
        eof = False
        if line.rstrip().endswith(':'):
            block = [line]
            while True:
                try:
                    cont = input("... ")
                except EOFError:
                    eof = True
                    break
                except KeyboardInterrupt:
                    eof = True
                    print()
                    break
                if not cont.strip():
                    break
                block.append(cont)
            line = "\n".join(block)

        try:
            # Transpile and execute in the session namespace
            evaluate(line, _namespace)
        except KeyboardInterrupt:
            print("\nمع السلامة 👋")
            break
        except Exception as e:
            msg = _get_error_ar(e)
            print(f"\u202B{msg}\u202C", file=sys.stderr)
        if eof:
            print()
            break


def legacy_main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()
    
    if command in ('--clear-cache', 'clear-cache'):
        from core.runner import cache as _c
        n = _c.clear()
        print(f"\u202Bتم حذف {n} ملف ترجمة مخزّنة\u202C")
        return

    if command in ('help', '--help', '-h', '-?'):
        print_help()
        return

    if command in ('--version', '-v', 'version'):
        print(f"APL v{__version__} - Ammar Programming Language")
        return
    
    if command in ('repl', 'interactive', 'shell'):
        run_repl()
        return

    # Execute code directly: python apl.py -c "اطبع 'مرحباً'"
    if command in ('-c', '--code'):
        if len(sys.argv) < 3:
            print("Usage: python apl.py -c '<code>'")
            sys.exit(1)
        code = sys.argv[2]
        # Split by newlines and semicolons for multi-statement support
        lines = code.replace(';', '\n').split('\n')
        # go through transpile() so the library-import block is emitted.
        # Building the code line-by-line here skipped it, so
        # `apl.py -c "اطبع جذر(16)"` produced `math.sqrt(...)` with no
        # `import math` -> NameError.
        python_code = _RUNTIME + "\n" + transpile(code)
        try:
            exec(python_code, {})
        except Exception as e:
            msg = _get_error_ar(e)
            print(f"\u202B{msg}\u202C", file=sys.stderr)
            raise SystemExit(1)
        return

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Error: file '{filepath}' not found")
        sys.exit(1)

    run_file(filepath)


def main():
    from core.cli import main as cli_main
    return cli_main()


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        # `python apl.py help | head` closes the pipe early - exit quietly.
        try:
            sys.stdout.close()
        finally:
            os._exit(0)
    except KeyboardInterrupt:
        print()
        os._exit(130)

"""عمار - واجهة سطر الأوامر للغة APL.

الأوامر الأساسية:
    عمار شغل ملف.apl          تشغيل برنامج
    عمار فحص ملف.apl          فحص الصياغة بدون تشغيل
    عمار ترجمة ملف.apl        طباعة كود Python المترجم
    عمار طرفية                موجه تفاعلي (REPL)
    عمار نسخة                 رقم الإصدار
    عمار مساعدة               المساعدة الكاملة
    عمار مسح-الكاش            حذف الترجمات المخزنة

المشاريع:
    عمار مشروع جديد <اسم>     مجلد مشروع جديد جاهز للتشغيل
    عمار مشروع تشغيل          تشغيل المشروع اللي في المجلد الحالي

المكتبات:
    عمار مكتبة تحميل <اسم>    تحميل مكتبة إلى مجلد المكتبات
    عمار مكتبة قائمة          المكتبات المثبتة
    عمار مكتبة بحث <كلمة>     البحث في مكتبات APL
    عمار مكتبة حذف <اسم>      حذف مكتبة محمّلة
    عمار مكتبة قفل            إصدارات المكتبات المثبتة (lockfile)
    عمار مكتبة استعادة        تنزيل المكتبات المسجّلة في القفل بإصداراتها

التثبيت مابيسطّبش حزم Python لوحده. لو عايز تسطّبها مع المكتبة استخدم
--مع-الاعتمادات، وهيقولك بالظبط إيه اللي هيتسطّب قبل ما يبدأ.

الأسماء الإنجليزية (run, check, transpile, repl, version, help,
clear-cache, library) تعمل بنفس الطريقة.
"""
# APL - لغة عمار البرمجية
# Copyright (c) 2026 Ammar Elkhateeb (AmmarBasha2011)
# Distributed under the Python Software Foundation License Version 2 (PSF-2.0),
# the same license as Python. See LICENSE and NOTICE.

import difflib
import os
import re
import sys
from pathlib import Path

#: Arabic and English spellings for every command.
ALIASES = {
    'شغل': 'run', 'تشغيل': 'run', 'نفذ': 'run', 'نفّذ': 'run', 'شغّل': 'run',
    'فحص': 'check', 'تحقق': 'check', 'اختبر': 'check',
    'ترجمة': 'transpile', 'حوّل': 'transpile', 'حول': 'transpile',
    'طرفية': 'repl', 'تفاعلي': 'repl', 'موجه': 'repl',
    'نسخة': 'version', 'إصدار': 'version', 'اصدار': 'version',
    'مساعدة': 'help', 'دليل': 'help',
    'مسح-الكاش': 'clear-cache', 'نظف': 'clear-cache',
    'مكتبة': 'library', 'مكتبات': 'library',
    'مثال': 'example', 'أمثلة': 'example', 'امثلة': 'example',
    'تنسيق': 'format', 'نسّق': 'format', 'format': 'format',
    'مسار': 'path', 'المسار': 'path', 'path': 'path',
    'بناء': 'build', 'ابن': 'build', 'ابنِ': 'build', 'حزّم': 'build',
    'build': 'build', 'exe': 'build',
    'مشروع': 'project', 'مشاريع': 'project', 'project': 'project',
    'تتبع': 'trace', 'تتبّع': 'trace', 'trace': 'trace',
    'مصحح': 'debug', 'مصحّح': 'debug', 'debug': 'debug',
    # English spellings
    'run': 'run', 'check': 'check', 'transpile': 'transpile', 'repl': 'repl',
    'version': 'version', 'help': 'help', 'clear-cache': 'clear-cache',
    'library': 'library', 'example': 'example', 'project': 'project',
}

#: Sub-commands of `عمار مشروع`.
PROJECT_ALIASES = {
    'جديد': 'new', 'إنشاء': 'new', 'انشاء': 'new', 'اعمل': 'new',
    'تشغيل': 'run', 'شغل': 'run', 'نفذ': 'run',
    'new': 'new', 'init': 'new', 'create': 'new',
    'run': 'run', 'start': 'run',
}

#: Sub-commands of `عمار مكتبة`.
LIBRARY_ALIASES = {
    'تحميل': 'install', 'نزل': 'install', 'نزّل': 'install', 'ثبت': 'install',
    'قائمة': 'list', 'المثبتة': 'list',
    'الكل': 'list-all', 'متاح': 'list-all',
    'بحث': 'search', 'ابحث': 'search',
    'حذف': 'remove', 'إزالة': 'remove', 'ازالة': 'remove', 'امسح': 'remove',
    'قفل': 'lock', 'القفل': 'lock', 'إصدارات': 'lock',
    'استعادة': 'sync', 'زامن': 'sync', 'زامِن': 'sync',
    'install': 'install', 'download': 'install', 'add': 'install',
    'list': 'list', 'all': 'list-all', 'search': 'search', 'find': 'search',
    'remove': 'remove', 'uninstall': 'remove',
    'lock': 'lock', 'lockfile': 'lock', 'sync': 'sync', 'restore': 'sync',
}

#: Where `عمار مكتبة تحميل` fetches a library from.
DEFAULT_SOURCE = ('https://raw.githubusercontent.com/AmmarBasha2011/APL'
                  '/libraries/core/libraries/')
LIBRARY_SOURCE = os.environ.get('APL_LIBRARY_SOURCE', DEFAULT_SOURCE)


def _configure_console():
    """Arabic output on every platform, console or pipe.

    On Windows the default stream encoding is the ANSI code page, which cannot
    represent Arabic at all: printing the library list to a pipe raised
    UnicodeEncodeError. UTF-8 plus the 65001 code page fixes both the console
    and a redirect.
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding='utf-8', errors='replace')
        except (AttributeError, ValueError):
            pass
    # Piped input is UTF-8 everywhere, but a Windows pipe is decoded with the
    # ANSI code page, so an Arabic command (`م` in the stepper, a typed answer
    # to `ادخل`) arrived garbled and was rejected as unknown.
    try:
        if not sys.stdin.isatty():
            sys.stdin.reconfigure(encoding='utf-8', errors='replace')
    except (AttributeError, ValueError, OSError):
        pass
    if sys.platform == 'win32':
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleOutputCP(65001)
            ctypes.windll.kernel32.SetConsoleCP(65001)
        except Exception:
            pass


def _command(word):
    """Resolve a typed word to a command name, or None."""
    return ALIASES.get(word) or ALIASES.get(word.lower())


def _error(message):
    print(message, file=sys.stderr)
    return 1


def _catalog_by_name():
    from core.libraries.registry import CATALOG
    return {item['name']: item for item in CATALOG.values()}


def _library_folder():
    from core.libraries.registry import library_home
    return library_home()


def _size(kilobytes):
    return f'{kilobytes} ك.ب' if kilobytes < 1024 else f'{kilobytes / 1024:.1f} م.ب'


# --------------------------------------------------------------------------
# تشغيل وفحص وترجمة
# --------------------------------------------------------------------------

def _run(rest):
    if not rest:
        return _error('حدد الملف. مثال: عمار شغل برنامج.apl')
    file, args = rest[0], list(rest[1:])
    debug = '--debug' in args
    if debug:
        args.remove('--debug')
    from core.runner.execution import diagnostic, execute_file
    try:
        execute_file(file, args, debug)
    except OSError as error:
        print(diagnostic(error, filename=file), file=sys.stderr)
        return 1
    return 0


def _compile(file):
    """Compile a file, returning (source, compilation) or raising."""
    from core.runner.execution import Compilation
    source = Path(file).read_text(encoding='utf-8')
    return source, Compilation(source, file)


def _check(rest):
    if not rest:
        return _error('حدد الملف. مثال: عمار فحص برنامج.apl')
    file, source = rest[0], ''
    from core.runner.execution import diagnostic
    try:
        source, _ = _compile(file)
    except Exception as error:
        try:
            text = Path(file).read_text(encoding='utf-8')
        except OSError:
            text = ''
        for note in _lint(text, file):
            print(f'  تنبيه: {note}', file=sys.stderr)
        print(diagnostic(error, None, source, file), file=sys.stderr)
        return 1
    notes = _lint(source, file)
    print(f'سليم: {file}')
    for note in notes:
        print(f'  تنبيه: {note}')
    return 0


def _transpile(rest):
    if not rest:
        return _error('حدد الملف. مثال: عمار ترجمة برنامج.apl')
    file, source = rest[0], ''
    from core.runner.execution import diagnostic
    from core.runner.main import _RUNTIME
    try:
        source, compilation = _compile(file)
    except Exception as error:
        print(diagnostic(error, None, source, file), file=sys.stderr)
        return 1
    print(_RUNTIME + '\n' + compilation.python)
    return 0


def _execute_code(rest):
    if not rest:
        return _error('حدد الكود. مثال: عمار -c \'اطبع 1\'')
    source = rest[0]
    from core.runner.execution import Compilation, diagnostic, execute
    compilation = None
    try:
        compilation = Compilation(source, '<command>')
        execute(compilation, {'__name__': '__main__'})
    except Exception as error:
        print(diagnostic(error, compilation, source, '<command>'), file=sys.stderr)
        return 1
    return 0


# --------------------------------------------------------------------------
# المكتبات
# --------------------------------------------------------------------------

PROJECT_FILE = 'apl-project.json'

#: The starting program of `عمار مشروع جديد`.
PROJECT_PROGRAM = """# برنامج APL جديد
# شغّله بـ: عمار شغل main.apl

اطبع("أهلاً بالعالم!")
"""

PROJECT_README = """# {name}

مشروع {lang} مبني على لغة APL.

## التشغيل

```
عمار مشروع تشغيل      # من جوه المجلد ده
عمار شغل main.apl     # أو بالملف مباشرة
عمار فحص main.apl     # فحص الصياغة وتنبيهات التنسيق
```

## المكتبات

المكتبات بتتسطب مرة واحدة للجهاز كله (زي Python)، وبتتسجل في
`~/.apl/lock.json`:

```
عمار مكتبة تحميل <اسم>            # تثبيت
عمار مكتبة قفل                    # إيه المثبت وإصداره
عمار مكتبة استعادة                # رجّع نفس الإصدارات
```

المكتبات اللي المشروع ده محتاجها بتتكتب في `apl-project.json` تحت `libraries`.
"""

PROJECT_GITIGNORE = """__pycache__/
*.pyc
dist/
build/
.apl-cache/
"""


def _project_usage():
    print('الاستخدام: عمار مشروع [جديد|تشغيل]')
    print('  عمار مشروع جديد <اسم>   اعمل مجلد مشروع فيه main.apl و README')
    print('  عمار مشروع تشغيل        شغّل المشروع اللي في المجلد الحالي')
    return 0


def _project_new(name):
    """عمار مشروع جديد <اسم> - a folder that runs with one command."""
    import json
    name = name.strip().rstrip('/')
    if not name or name in ('.', '..'):
        return _error('حدد اسم المشروع. مثال: عمار مشروع جديد تجريبي')
    folder = Path(name)
    if folder.exists() and any(folder.iterdir()):
        return _error(f'المجلد {folder} موجود وفيه ملفات. اختار اسم تاني.')
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'main.apl').write_text(PROJECT_PROGRAM, encoding='utf-8')
    (folder / 'README.md').write_text(
        PROJECT_README.format(name=name, lang='APL'), encoding='utf-8')
    (folder / '.gitignore').write_text(PROJECT_GITIGNORE, encoding='utf-8')
    config = {
        'name': name,
        'version': '0.1.0',
        'entry': 'main.apl',
        'libraries': [],
    }
    (folder / PROJECT_FILE).write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'تم عمل مشروع {name} في {folder.resolve()}')
    print('  main.apl         البرنامج')
    print(f'  {PROJECT_FILE}   اسم المشروع والملف اللي بيتشغل')
    print('  README.md        طريقة التشغيل')
    print('  .gitignore')
    print()
    print(f'ابدأ بـ: cd {folder} ثم عمار مشروع تشغيل')
    return 0


def _project_run():
    """عمار مشروع تشغيل - run the entry file of the project in this folder."""
    import json
    path = Path(PROJECT_FILE)
    if not path.is_file():
        return _error(f'مفيش {PROJECT_FILE} هنا. اعمل مشروع: عمار مشروع جديد <اسم>')
    try:
        config = json.loads(path.read_text(encoding='utf-8'))
    except ValueError as error:
        return _error(f'{PROJECT_FILE} مش JSON سليم: {error}')
    entry = config.get('entry') or 'main.apl'
    if not Path(entry).is_file():
        return _error(f'الملف {entry} المذكور في {PROJECT_FILE} مش موجود.')
    libraries = [item for item in (config.get('libraries') or []) if isinstance(item, str)]
    if libraries:
        from core.libraries.registry import ENTRIES
        installed = {item['name'] for item in ENTRIES}
        missing = [item for item in libraries if item not in installed]
        if missing:
            print('محتاج مكتبات مش متسطبة: ' + '، '.join(missing))
            print('سطّبها بـ: ' + ' ثم '.join(
                f'عمار مكتبة تحميل {item}' for item in missing))
    return _run([entry])


def _project(rest):
    if not rest:
        return _project_run()
    action = PROJECT_ALIASES.get(rest[0]) or PROJECT_ALIASES.get(rest[0].lower())
    args = rest[1:]
    if action == 'new':
        if not args:
            return _error('حدد اسم المشروع. مثال: عمار مشروع جديد تجريبي')
        return _project_new(args[0])
    if action == 'run':
        return _project_run()
    return _project_usage()


def _library_usage():
    print('الاستخدام: عمار مكتبة [تحميل|قائمة|بحث|حذف]')
    print('  عمار مكتبة تحميل <اسم>            تحميل مكتبة من GitHub')
    print('  عمار مكتبة تحميل <مالك/ريبو>      تحميل من ريبو معيّن')
    print('  عمار مكتبة تحميل <رابط>           تحميل من رابط GitHub كامل')
    print('  عمار مكتبة قائمة                  المكتبات المثبتة')
    print('  عمار مكتبة بحث <كلمة>             البحث في المثبتة وعلى GitHub')
    print('  عمار مكتبة حذف <اسم>              حذف مكتبة مثبتة')
    print('  عمار مكتبة قفل                    إصدارات المكتبات المثبتة')
    print('  عمار مكتبة استعادة                تنزيل المكتبات المسجّلة في القفل')
    print('  عمار مكتبة تحميل <اسم> --مع-الاعتمادات  تسطّب حزم Python المطلوبة كمان')
    return 0


# --------------------------------------------------------------------------
# مدير الحزم: كل مكتبة ريبو GitHub مستقل فيه apl-library.json وكودها
# --------------------------------------------------------------------------

DEFAULT_OWNER = 'AmmarBasha2011'
DEFAULT_PREFIX = 'apl-'


def _split_source(spec):
    """Turn what the user typed into (owner, repo), or None for a local path.

    numpy                     -> AmmarBasha2011/apl-numpy
    someone/mylib             -> someone/mylib
    https://github.com/a/b    -> a/b
    ./مكتبتي  or /path/lib    -> None (installed from disk)
    """
    text = spec.strip().rstrip('/')
    if not text:
        return None
    if text.startswith(('http://', 'https://')):
        parts = [part for part in text.split('/') if part]
        if 'github.com' in parts:
            index = parts.index('github.com')
            rest = parts[index + 1:]
            if len(rest) >= 2:
                return rest[0], rest[1].removesuffix('.git')
        return None
    if Path(text).expanduser().is_dir():
        return None
    if text.count('/') == 1:
        owner, repo = text.split('/')
        return owner, repo.removesuffix('.git')
    return DEFAULT_OWNER, text if text.startswith(DEFAULT_PREFIX) else DEFAULT_PREFIX + text


def _download_tarball(owner, repo, refs=None):
    """Fetch a repository tarball; returns bytes, or None when not found."""
    import urllib.error
    import urllib.request
    for ref in (refs or ('HEAD', 'refs/heads/main', 'refs/heads/master')):
        url = f'https://codeload.github.com/{owner}/{repo}/tar.gz/{ref}'
        request = urllib.request.Request(url, headers={'User-Agent': 'APL-package-manager'})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code == 404:
                continue
            raise
        except (urllib.error.URLError, OSError) as error:
            raise RuntimeError(str(error)) from error
    return None


def _unpack(data, target):
    """Extract a GitHub tarball and return the folder holding the project."""
    import io
    import tarfile
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive:
        for member in archive.getmembers():
            parts = Path(member.name).parts
            if not parts or parts[0] in ('..', '/') or member.name.startswith('/'):
                raise ValueError('أرشيف غير آمن')
            if member.issym() or member.islnk():
                continue
            archive.extract(member, target)
    roots = [path for path in Path(target).iterdir() if path.is_dir()]
    return roots[0] if len(roots) == 1 else Path(target)


def _read_package(folder):
    """Read apl-library.json from a library folder, or None when absent."""
    import json
    path = Path(folder) / 'apl-library.json'
    if not path.is_file():
        return None
    try:
        meta = json.loads(path.read_text(encoding='utf-8'))
    except ValueError as error:
        raise ValueError(f'apl-library.json مش JSON سليم: {error}') from error
    if not isinstance(meta, dict):
        raise ValueError('apl-library.json لازم يكون كائن JSON')
    return meta


def _lock_path():
    """The lockfile: exactly what is installed, from where, at which version."""
    return Path.home() / '.apl' / 'lock.json'


def _read_lock():
    import json
    try:
        data = json.loads(_lock_path().read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def _write_lock(name, entry):
    import json
    data = _read_lock()
    if entry is None:
        data.pop(name, None)
    else:
        data[name] = entry
    path = _lock_path()
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + '\n',
                        encoding='utf-8')
    except OSError:
        pass


def _split_version(spec):
    """`numpy@1.0.0` and `numpy==1.0.0` both pin a version."""
    for marker in ('==', '@'):
        if marker in spec:
            name, _, version = spec.partition(marker)
            name, version = name.strip(), version.strip()
            if name and version:
                return name, version
    return spec.strip(), None


def _pip_command():
    """The command used to install a library's Python packages.

    APL_PIP_CMD overrides it, for a virtualenv's pip, uv, or a test stub.
    """
    import shlex
    override = os.environ.get('APL_PIP_CMD', '').strip()
    if override:
        # A Windows path keeps its backslashes: POSIX splitting would eat them
        # and pip would never start ("cannot find the file specified").
        parts = shlex.split(override, posix=(os.name != 'nt'))
        if os.name == 'nt':
            parts = [part[1:-1] if len(part) > 1 and part[0] == part[-1]
                     and part[0] in '"\'' else part for part in parts]
        return parts
    return [sys.executable, '-m', 'pip', 'install']


def _install_python_deps(requires):
    """Install a library's Python packages; True when they are in place."""
    import subprocess
    requires = [item for item in requires if isinstance(item, str) and item.strip()]
    if not requires:
        return True
    print('  بنسطّب حزم Python: ' + '، '.join(requires))
    try:
        result = subprocess.run(_pip_command() + requires, capture_output=True,
                                text=True, encoding='utf-8', errors='replace')
    except OSError as error:
        print(f'  تعذر تشغيل pip: {error}', file=sys.stderr)
        print('  سطّبها بنفسك: pip install ' + ' '.join(requires), file=sys.stderr)
        return False
    if result.returncode != 0:
        print('  فشل تثبيت حزم Python. المكتبة اتسطبت، بس محتاجة الحزم دي. '
              'جرّب: pip install ' + ' '.join(requires), file=sys.stderr)
        for line in (result.stderr or result.stdout or '').strip().splitlines()[-3:]:
            print('  ' + line, file=sys.stderr)
        return False
    print('  تم تثبيت حزم Python.')
    return True


def _install_from_folder(source, name_hint=None, origin=None, deps=False):
    """Copy one library folder into the library home, without running it."""
    import shutil
    from core.libraries import registry
    source = Path(source)
    meta = _read_package(source)
    if meta is None:
        return _error(f'مفيش apl-library.json في {source}، مش مكتبة APL.')
    name = (meta.get('name') or name_hint or source.name).strip()
    entry = meta.get('entry') or f'{name}_funcs.py'
    entry_path = source / entry
    if not entry_path.is_file():
        return _error(f'الملف {entry} المذكور في apl-library.json مش موجود في المكتبة.')
    try:
        compile(entry_path.read_text(encoding='utf-8'), str(entry_path), 'exec')
    except SyntaxError as error:
        return _error(f'كود المكتبة فيه خطأ صياغة: {error}')
    home = _library_folder()
    home.mkdir(parents=True, exist_ok=True)
    target = home / name
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns('.git', '__pycache__'))
    registry.refresh()
    version = meta.get('version') or '؟'
    _write_lock(name, {
        'version': meta.get('version'),
        'source': origin or str(source),
        'requires': meta.get('requires') or [],
        'libraries': meta.get('libraries') or [],
    })
    print(f'تم تثبيت مكتبة {name} ({version}) في {target}')
    title = meta.get('title')
    if title:
        print(f'  {title}')
    requires = meta.get('requires') or []
    if requires:
        print('  محتاجة من Python: ' + '، '.join(requires))
        if deps:
            _install_python_deps(requires)
        else:
            # Installing packages is the user's decision, not a side effect of
            # installing a library: say the command, or offer the flag.
            print('  لو مش متسطبة: pip install ' + ' '.join(
                requirement.split('>')[0].split('=')[0] for requirement in requires))
            print('  أو نزّلها مع المكتبة بـ: عمار مكتبة تحميل <الاسم> --مع-الاعتمادات')
    libraries = [name for name in (meta.get('libraries') or []) if isinstance(name, str)]
    if libraries:
        from core.libraries.registry import ENTRIES
        installed = {entry['name'] for entry in ENTRIES}
        missing = [name for name in libraries if name not in installed]
        if missing:
            print('  محتاجة مكتبات APL: ' + '، '.join(missing))
            print('  نزّلها بـ: ' + ' ثم '.join(
                f'عمار مكتبة تحميل {name}' for name in missing))
        else:
            print('  محتاجة مكتبات APL (مثبتة): ' + '، '.join(libraries))
    if origin:
        print(f'  المصدر: {origin}')
    requires = meta.get('requires') or []
    if requires:
        print('  تنبيه: المكتبة دي كود بيشتغل بصلاحياتك وقت الاستخدام، '
              'زي أي برنامج بتشغله. راجع كودها لو جاية من مصدر مش معروف.')
    else:
        print('  تنبيه: المكتبة دي كود بيشتغل بصلاحياتك وقت الاستخدام.')
    return 0


def _library_install(spec, deps=False):
    """عمار مكتبة تحميل <اسم|مالك/ريبو|رابط|مسار>"""
    import shutil
    import tempfile
    local = Path(spec).expanduser()
    if local.is_dir():
        return _install_from_folder(local, deps=deps)
    # A plain name: the shipped index says which repo it is, by library name or
    # by the real Python package it wraps.
    spec, version = _split_version(spec)
    if '/' not in spec and not spec.lower().startswith('http'):
        item = _index_match(spec.strip())
        if item and item.get('repo'):
            owner, _, repo = item['repo'].partition('/')
            if owner and repo:
                spec = item['repo']
    source = _split_source(spec)
    if source is None:
        return _error(f'مش عارف أجيب مكتبة من: {spec}')
    owner, repo = source
    origin = f'https://github.com/{owner}/{repo}'
    refs = None
    if version:
        # codeload wants the tag name itself, not refs/tags/... (a branch ref
        # works either way, a tag ref does not).
        refs = (f'v{version}', version)
    try:
        data = _download_tarball(owner, repo, refs)
    except RuntimeError as error:
        return _error(f'تعذر الاتصال بـ GitHub: {error}')
    if data is None:
        if version:
            return _error(f'مفيش إصدار {version} في {owner}/{repo}. '
                          'الإصدارات بتكون tags زي v1.0.0.')
        return _error(f'مفيش ريبو اسمه {owner}/{repo} على GitHub. '
                      'اتأكد من الاسم، أو استخدم مالك/ريبو.')
    workdir = Path(tempfile.mkdtemp(prefix='apl-lib-'))
    try:
        folder = _unpack(data, workdir)
        hint = repo[len(DEFAULT_PREFIX):] if repo.startswith(DEFAULT_PREFIX) else repo
        return _install_from_folder(folder, hint, origin, deps=deps)
    except ValueError as error:
        return _error(str(error))
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def _library_list(show_all):
    from core.libraries.registry import ENTRIES
    if not ENTRIES:
        print('مفيش مكتبات مثبتة.')
        print(f'مجلد المكتبات: {_library_folder()}')
        print('نزّل واحدة بـ: عمار مكتبة تحميل <اسم>')
        return 0
    print(f'المكتبات المثبتة ({len(ENTRIES)}):')
    for entry in ENTRIES:
        version = entry.get('version') or ''
        title = entry.get('title') or ''
        line = f'  {entry["name"]}'
        if version:
            line += f' {version}'
        if title:
            line += f' — {title}'
        print(line)
    print(f'مجلد المكتبات: {_library_folder()}')
    return 0


def _library_index():
    """The list of published libraries that ships with APL."""
    import json
    path = Path(__file__).resolve().parent.parent / 'data' / 'libraries.json'
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return []


def _index_match(word):
    """The published library a name refers to.

    A library answers to its own name and to the real Python package it wraps,
    so a user who knows the Python package can install the Arabic wrapper by
    that name.
    """
    needle = word.lower()
    for item in _library_index():
        names = [str(item.get('name') or '').lower(), str(item.get('package') or '').lower()]
        if needle in names:
            return item
    return None


def _library_search(word):
    """Search the shipped index and the installed packages, then GitHub."""
    import json
    import urllib.error
    import urllib.request
    from core.libraries.registry import ENTRIES
    needle = word.lower()
    hits = [entry for entry in ENTRIES
            if needle in ' '.join((entry['name'], entry.get('title') or '')).lower()]
    if hits:
        print(f'مثبتة عندك ({len(hits)}):')
        for entry in hits:
            print(f'  {entry["name"]} — {entry.get("title") or ""}')
    catalogue = [item for item in _library_index()
                 if needle in ' '.join((item.get('name', ''), item.get('title', ''),
                                        item.get('package') or '')).lower()]
    if catalogue:
        print(f'متاحة للتحميل ({len(catalogue)}):')
        for item in catalogue:
            print(f'  {item["name"]} — {item["repo"]}')
        print('نزّل واحدة بـ: عمار مكتبة تحميل <الاسم>')
        return 0
    url = ('https://api.github.com/search/repositories?q=' + word
           + f'+user:{DEFAULT_OWNER}+in:name&per_page=10')
    request = urllib.request.Request(url, headers={'User-Agent': 'APL-package-manager',
                                                   'Accept': 'application/vnd.github+json'})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode('utf-8'))
    except (urllib.error.URLError, OSError, ValueError):
        if not hits:
            print('مفيش نتائج محليًا، وتعذر البحث على GitHub دلوقتي.')
        return 0 if hits else 1
    found = payload.get('items') or []
    if not found:
        print(f'مفيش مكتبة على GitHub فيها: {word}')
        return 0 if hits else 1
    print(f'على GitHub ({len(found)}):')
    for item in found:
        name = item['name']
        if name.startswith(DEFAULT_PREFIX):
            name = name[len(DEFAULT_PREFIX):]
        print(f'  {name} — {item.get("description") or ""}')
    print('نزّل واحدة بـ: عمار مكتبة تحميل <الاسم>')
    return 0


def _library_lock():
    """عمار مكتبة قفل - what is installed, from where, at which version."""
    data = _read_lock()
    if not data:
        print('مفيش قفل لسه. القفل بيتكتب لوحده أول ما تنزّل مكتبة.')
        print(f'مكانه: {_lock_path()}')
        return 0
    from core.libraries import registry
    registry.refresh()
    home = _library_folder()
    installed = {entry['name']: entry for entry in registry.ENTRIES
                 if (home / entry['name']).is_dir()}
    print(f'قفل المكتبات ({len(data)}):')
    for name in sorted(data):
        entry = data[name] or {}
        version = entry.get('version') or 'أحدث نسخة'
        line = f'  {name} {version}'
        if name not in installed:
            line += ' (مش مثبتة دلوقتي)'
        source = entry.get('source')
        if source:
            line += f' — {source}'
        print(line)
        requires = entry.get('requires') or []
        if requires:
            print('    محتاجة من Python: ' + '، '.join(requires))
    print(f'مكان القفل: {_lock_path()}')
    print('رجّع كل حاجة زي ما هي بـ: عمار مكتبة استعادة')
    return 0


def _library_sync():
    """عمار مكتبة استعادة - reinstall everything in the lock at its version.

    The lockfile is what makes an install repeatable: another machine, or the
    same machine after a library folder is gone, gets the same versions back.
    """
    data = _read_lock()
    if not data:
        print('مفيش قفل. نزّل مكتبة الأول، وبعدها القفل هيتكتب لوحده.')
        return 0
    from core.libraries import registry
    registry.refresh()
    home = _library_folder()
    installed = {entry['name']: entry for entry in registry.ENTRIES
                 if (home / entry['name']).is_dir()}
    status = 0
    done, ok, skipped = 0, 0, 0
    for name in sorted(data):
        entry = data[name] or {}
        version = entry.get('version')
        have = installed.get(name)
        if have and (not version or have.get('version') == version):
            print(f'  {name} {version or ""} — متسطبة بالفعل')
            skipped += 1
            continue
        spec = f'{name}@{version}' if version else name
        print(f'  بننزّل {spec}…')
        code = _library_install(spec)
        done += 1
        if code == 0:
            ok += 1
        else:
            status = 1
    print(f'خلصنا: {ok} نزلت، {skipped} كانت موجودة'
          + (f'، {done - ok} فشلت' if done - ok else ''))
    return status


def _library_remove(name):
    import shutil
    from core.libraries import registry
    home = _library_folder()
    folder = home / name
    _write_lock(name, None)
    if folder.is_dir():
        shutil.rmtree(folder)
    else:
        files = list(home.glob(f'{name}_funcs.py')) if home.is_dir() else []
        if not files:
            return _error(f'مكتبة {name} مش مثبتة أصلاً.')
        for path in files:
            path.unlink()
    registry.refresh()
    print(f'تم حذف مكتبة {name}.')
    return 0


EXAMPLES_REPO = 'AmmarBasha2011/APL-Examples'
EXAMPLES_BRANCH = 'main'


def _examples_index(force=False):
    """The example list published in APL-Examples, cached for a day."""
    import json
    import time
    import urllib.error
    import urllib.request
    cache = _library_folder().parent / 'examples-index.json'
    if not force and cache.is_file() and time.time() - cache.stat().st_mtime < 86400:
        try:
            return json.loads(cache.read_text(encoding='utf-8'))
        except ValueError:
            pass
    url = (f'https://raw.githubusercontent.com/{EXAMPLES_REPO}/{EXAMPLES_BRANCH}/index.json')
    request = urllib.request.Request(url, headers={'User-Agent': 'APL-examples'})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))
    except (urllib.error.URLError, OSError, ValueError) as error:
        if cache.is_file():
            try:
                return json.loads(cache.read_text(encoding='utf-8'))
            except ValueError:
                pass
        raise RuntimeError(f'تعذر جلب قائمة الأمثلة: {error}') from error
    try:
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
    except OSError:
        pass
    return data


def _match_example(items, wanted):
    """Find one example by number, exact name, file name or part of the name."""
    wanted = str(wanted).strip()
    lowered = wanted.lower()
    for item in items:
        if str(item.get('number')) == wanted:
            return item
    for item in items:
        if str(item.get('number')).lstrip('0') == wanted.lstrip('0'):
            return item
    for item in items:
        if item.get('file', '').lower() == lowered or item.get('name', '').lower() == lowered:
            return item
    for item in items:
        if lowered in item.get('name', '').lower() or lowered in item.get('file', '').lower():
            return item
    return None


def _path(rest):
    """Add عمار to PATH, so it runs from any folder."""
    action = rest[0] if rest else 'عرض'
    if action in ('عرض', 'show'):
        print('عشان تشغّل "عمار" من أي مجلد، ضيف مجلد المشروع للـ PATH.')
        print('ويندوز: عمار مسار ثبت')
        print('لينكس/ماك: عمار مسار ثبت')
        return 0
    if action not in ('ثبت', 'install', 'اضف', 'أضف'):
        return _error('الاستخدام: عمار مسار [عرض|ثبت]')
    import os
    project = Path(__file__).resolve().parent.parent
    launcher = project / ('عمار.cmd' if os.name == 'nt' else 'عمار')
    if not launcher.is_file():
        return _error(f'مفيش ملف تشغيل في {project}')
    if os.name == 'nt':
        target = Path(os.environ.get('LOCALAPPDATA', Path.home())) / 'APL'
        target.mkdir(parents=True, exist_ok=True)
        wrapper = target / 'عمار.cmd'
        wrapper.write_text(f'@echo off\r\npython "{launcher}" %*\r\n', encoding='utf-8')
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0,
                                winreg.KEY_READ | winreg.KEY_WRITE) as key:
                current, _ = winreg.QueryValueEx(key, 'Path')
                parts = [item for item in current.split(';') if item]
                if str(target) not in parts:
                    parts.append(str(target))
                    winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, ';'.join(parts))
                    print(f'تمت إضافة {target} للـ PATH. افتح نافذة جديدة وجرب: عمار نسخة')
                else:
                    print(f'{target} موجود في الـ PATH بالفعل.')
        except OSError as error:
            return _error(f'تعذر تعديل الـ PATH: {error}')
        return 0
    bin_dir = Path.home() / '.local' / 'bin'
    bin_dir.mkdir(parents=True, exist_ok=True)
    link = bin_dir / 'عمار'
    try:
        if link.exists() or link.is_symlink():
            link.unlink()
        # A wrapper, not a symlink: the launcher finds apl.py next to itself, and
        # a symlink would point it at ~/.local/bin.
        link.write_text('#!/bin/sh\nexec python3 "' + str(project / 'apl.py') + '" "$@"\n',
                        encoding='utf-8')
        link.chmod(0o755)
    except OSError as error:
        return _error(f'تعذر إنشاء الملف: {error}')
    print(f'تم إنشاء {link}')
    if str(bin_dir) not in os.environ.get('PATH', ''):
        print(f'ضيف ده لملف ~/.profile:  export PATH="$HOME/.local/bin:$PATH"')
    print('جرب في تيرمنال جديد: عمار نسخة')
    return 0


def _format_text(source: str) -> str:
    """Reindent by structure, trim trailing spaces, squeeze blank lines."""
    lines = source.replace('\r\n', '\n').replace('\t', '    ').split('\n')
    result = []
    blanks = 0
    for line in lines:
        stripped = line.strip()
        if not stripped:
            blanks += 1
            if blanks <= 1:
                result.append('')
            continue
        blanks = 0
        depth = (len(line) - len(line.lstrip(' '))) // 4
        result.append('    ' * depth + stripped)
    while result and not result[-1]:
        result.pop()
    return '\n'.join(result) + '\n'


def _format(rest):
    if not rest:
        return _error('حدد الملف. مثال: عمار تنسيق برنامج.apl')
    write = '--كتابة' in rest or '--write' in rest
    files = [item for item in rest if not item.startswith('--')]
    if not files:
        return _error('حدد الملف. مثال: عمار تنسيق برنامج.apl')
    path = Path(files[0])
    if not path.is_file():
        return _error(f'الملف مش موجود: {path}')
    source = path.read_text(encoding='utf-8')
    formatted = _format_text(source)
    if write:
        if formatted != source:
            path.write_text(formatted, encoding='utf-8')
            print(f'تم تنسيق {path}')
        else:
            print(f'{path} منسّق أصلاً')
        return 0
    sys.stdout.write(formatted)
    return 0


def _lint(source: str, path: str) -> list:
    """Cheap, honest checks: they never claim the program is correct."""
    notes = []
    for number, line in enumerate(source.split('\n'), 1):
        if '\t' in line:
            notes.append(f'{path}:{number}: فيه تاب، استخدم مسافات')
        if line.rstrip() != line:
            notes.append(f'{path}:{number}: مسافات زيادة في آخر السطر')
        stripped = line.strip()
        if stripped.startswith('لو ') and re.search(r'(?<![=!<>])=(?!=)', stripped):
            notes.append(f'{path}:{number}: "=" جوه شرط، يمكن تقصد "=="')
        if stripped.startswith('#') and 'TODO' in stripped.upper():
            notes.append(f'{path}:{number}: TODO لسه موجود')
    return notes


#: How many examples a list prints before it summarizes the rest.
LIST_LIMIT = 40


def _search_examples(items, word):
    """Examples whose number, name, file or summary contains the word."""
    needle = str(word).strip().lower()
    if not needle:
        return []
    return [item for item in items
            if needle in ' '.join(str(item.get(key) or '') for key in
                                  ('number', 'name', 'file', 'summary')).lower()]


def _example_usage():
    print('الاستخدام: عمار مثال [حمل|جرب|قائمة] [الرقم أو الاسم]')
    print('  عمار مثال حمل <رقم/اسم>   تنزيل مثال في المجلد الحالي')
    print('  عمار مثال جرب <رقم/اسم>   تنزيل المثال وتشغيله')
    print('  عمار مثال قائمة           أول 40 مثال (وزيادة --الكل للكل)')
    print('  عمار مثال بحث <كلمة>      الأمثلة اللي اسمها أو وصفها فيه الكلمة')
    print(f'الأمثلة كلها في: https://github.com/{EXAMPLES_REPO}')
    return 0


def _example(rest):
    import urllib.error
    import urllib.request
    if not rest:
        return _example_usage()
    action = rest[0]
    aliases = {'حمل': 'get', 'نزل': 'get', 'تحميل': 'get', 'get': 'get', 'download': 'get',
               'جرب': 'try', 'شغل': 'try', 'شغّل': 'try', 'try': 'try', 'run': 'try',
               'قائمة': 'list', 'list': 'list',
               'بحث': 'search', 'ابحث': 'search', 'دوّر': 'search', 'search': 'search',
               'find': 'search'}
    action = aliases.get(action, action)
    try:
        items = _examples_index()
    except RuntimeError as error:
        return _error(str(error))
    if action == 'list':
        # The repository is thousands of examples now, so the list is a page,
        # not a wall: everything is still one flag away.
        everything = any(word in ('--الكل', '--all') for word in rest[1:])
        shown = items if everything else items[:LIST_LIMIT]
        print(f'الأمثلة ({len(items)}):' if everything
              else f'الأمثلة ({len(items)})، أول {len(shown)}:')
        for item in shown:
            print(f'  {item["number"]}. {item["name"]} — {item["summary"]}')
        if len(shown) < len(items):
            print(f'  … وفيه {len(items) - len(shown)} كمان. '
                  'شوفهم كلهم بـ: عمار مثال قائمة --الكل')
            print('  أو دوّر على حاجة معيّنة بـ: عمار مثال بحث <كلمة>')
        return 0
    if action == 'search':
        if len(rest) < 2:
            return _error('اكتب الكلمة اللي بتدوّر عليها. مثال: عمار مثال بحث مصفوفة')
        found = _search_examples(items, rest[1])
        if not found:
            return _error(f'مفيش مثال فيه: {rest[1]}')
        print(f'أمثلة فيها "{rest[1]}" ({len(found)}):')
        for item in found[:LIST_LIMIT]:
            print(f'  {item["number"]}. {item["name"]} — {item["summary"]}')
        if len(found) > LIST_LIMIT:
            print(f'  … وفيه {len(found) - LIST_LIMIT} كمان، جرّب كلمة أدق.')
        print('شغّل واحد بـ: عمار مثال جرب <الرقم>')
        return 0
    if action not in ('get', 'try'):
        return _example_usage()
    if len(rest) < 2:
        return _error('حدد رقم أو اسم المثال. مثال: عمار مثال حمل 1')
    item = _match_example(items, rest[1])
    if item is None:
        close = [entry['name'] for entry in items if rest[1].lower() in entry['name'].lower()][:3]
        hint = f' يمكن تقصد: {"، ".join(close)}' if close else ''
        return _error(f'مفيش مثال بالرقم أو الاسم ده: {rest[1]}.{hint}')
    url = (f'https://raw.githubusercontent.com/{EXAMPLES_REPO}/{EXAMPLES_BRANCH}/'
           f'examples/{item["file"]}')
    request = urllib.request.Request(url, headers={'User-Agent': 'APL-examples'})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()
    except (urllib.error.URLError, OSError) as error:
        return _error(f'تعذر تنزيل المثال: {error}')
    target = Path(item['file'])
    target.write_bytes(data)
    print(f'تم تنزيل المثال {item["number"]}. {item["name"]} في {target}')
    print(f'  {item["summary"]}')
    if action == 'try':
        print('--- التشغيل ---')
        return _run([str(target)])
    print(f'شغّله بـ: عمار شغل {target.name}')
    return 0


def _debug(rest, interactive):
    """عمار تتبع ملف.apl / عمار مصحح ملف.apl [--توقف 3,7]"""
    from core.runner.execution import Compilation
    from core.runner.main import _RUNTIME
    from core.runner.debugger import run as trace_run
    args = [item for item in rest if not item.startswith('-')]
    breakpoints = []
    index = 0
    while index < len(rest):
        item = rest[index]
        if item in ('--توقف', '--break') and index + 1 < len(rest):
            for piece in rest[index + 1].replace('،', ',').split(','):
                piece = piece.strip()
                if piece.isdigit():
                    breakpoints.append(int(piece))
            index += 2
            continue
        index += 1
    if not args:
        return _error('حدد الملف. مثال: عمار تتبع برنامج.apl')
    file = args[0]
    try:
        source = Path(file).read_text(encoding='utf-8')
    except OSError as error:
        return _error(f'مش قادر أقرا الملف: {error}')
    try:
        compilation = Compilation(source, file)
    except Exception as error:
        from core.runner.execution import diagnostic
        print(diagnostic(error, None, source, file), file=sys.stderr)
        return 1
    namespace = {'__name__': '__main__'}
    exec(compile(_RUNTIME, '<apl-runtime>', 'exec'), namespace)
    # Everything the runtime prologue put there is machinery, not the user's
    # program, so `متغيرات` shows only what the program itself created.
    hidden = frozenset(namespace)
    try:
        return trace_run(compilation, namespace, interactive=interactive,
                         breakpoints=breakpoints, source=source, hidden=hidden)
    except SystemExit:
        print('اتوقف المصحح.')
        return 0
    except Exception as error:
        from core.runner.execution import diagnostic
        print(diagnostic(error, compilation, source, file), file=sys.stderr)
        return 1


def _build(rest):
    """عمار بناء [ملف.apl] [--اسم اسم] — ملف تنفيذي مستقل.

    بلا ملف: يبني ملف تنفيذي للمفسّر نفسه. مع ملف: يبني ملف تنفيذي للبرنامج،
    ومصدر البرنامج بيكون جواه، فبيشتغل على أي جهاز من غير APL ومن غير بايثون.
    """
    import importlib.util
    script = Path(__file__).resolve().parent.parent / 'tools' / 'build_program.py'
    if not script.is_file():
        return _error('أمر بناء محتاج نسخة الريبو كاملة (مجلد tools).')
    spec = importlib.util.spec_from_file_location('apl_build_program', script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not rest:
        return _error('حدد الملف. مثال: عمار بناء برنامج.apl')
    name = None
    args = []
    index = 0
    while index < len(rest):
        item = rest[index]
        if item in ('--اسم', '--name') and index + 1 < len(rest):
            name = rest[index + 1]
            index += 2
            continue
        if not item.startswith('-'):
            args.append(item)
        index += 1
    if not args:
        return _error('حدد الملف. مثال: عمار بناء برنامج.apl')
    target = Path(args[0])
    if not target.is_file():
        return _error(f'مفيش ملف اسمه {target}')
    print(f'بيبني ملف تنفيذي من {target}… (بياخد دقيقة تقريبًا)')
    outcome = module.build(target, name=name)
    if not outcome.get('ok'):
        if outcome.get('needs'):
            print('بناء ملف تنفيذي محتاج PyInstaller. ثبّته بـ: pip install pyinstaller',
                  file=sys.stderr)
        return _error(outcome.get('error') or 'البناء فشل')
    size = outcome.get('size') or 0
    print(f'تم: {outcome["path"]} ({size // 1024} كيلوبايت)')
    print('  الملف ده بيشتغل لوحده على أي جهاز، من غير APL ومن غير بايثون.')
    return 0


def _library(rest):
    if not rest:
        return _library_usage()
    action = LIBRARY_ALIASES.get(rest[0]) or LIBRARY_ALIASES.get(rest[0].lower())
    args = rest[1:]
    if action in ('install', 'remove', 'search'):
        deps = False
        plain = []
        for item in args:
            if item in ('--مع-الاعتمادات', '--with-deps', '--تبعيات'):
                deps = True
            elif item in ('--بدون-تبعيات', '--no-deps'):
                deps = False
            elif not item.startswith('-'):
                plain.append(item)
        if not plain:
            return _error(f'حدد اسم المكتبة. مثال: عمار مكتبة {rest[0]} numpy')
        if action == 'install':
            return _library_install(plain[0], deps=deps)
        return {'remove': _library_remove, 'search': _library_search}[action](plain[0])
    if action in ('list', 'list-all'):
        return _library_list(action == 'list-all')
    if action == 'lock':
        return _library_lock()
    if action == 'sync':
        return _library_sync()
    return _library_usage()


# --------------------------------------------------------------------------

def main(argv=None):
    """نقطة الدخول: يقرأ الأمر وينفذه ويرجع رمز الخروج."""
    _configure_console()
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        if sys.stdin.isatty():
            from core.runner.main import run_repl
            run_repl()
            return 0
        from core.runner.main import print_help
        print_help()
        return 0
    first = argv.pop(0)
    if first in ('-h', '--help', '-?'):
        from core.runner.main import print_help
        print_help()
        return 0
    if first in ('--version', '-v'):
        first = 'نسخة'
    if first in ('-c', '--code'):
        return _execute_code(argv)
    command = _command(first)
    if command is None:
        if first.endswith('.apl') or Path(first).is_file():
            return _run([first, *argv])
        return _error(f'أمر غير معروف: {first}. اكتب: عمار مساعدة')
    if command == 'run':
        return _run(argv)
    if command == 'check':
        return _check(argv)
    if command == 'transpile':
        return _transpile(argv)
    if command == 'repl':
        from core.runner.main import run_repl
        run_repl()
        return 0
    if command == 'version':
        from core.runner.main import __version__
        print(f'APL v{__version__} - لغة عمار البرمجية')
        return 0
    if command == 'help':
        from core.runner.main import print_help, print_library_help
        if argv and argv[0] in ('مكتبات', 'libraries'):
            print_library_help()
        else:
            print_help()
        return 0
    if command == 'clear-cache':
        from core.runner.cache import clear, default_roots, project_root
        # An optional path (a program or a folder) names where to look; without
        # one, the current folder and the project root are searched.
        roots = None
        if argv:
            target = Path(argv[0])
            if target.is_file():
                target = target.parent
            if not target.exists():
                return _error(f'مفيش مسار بالاسم ده: {argv[0]}')
            roots = [target]
            found = project_root(target)
            if found is not None and found != target.resolve():
                roots.append(found)
        print(f'تم حذف {clear(roots=roots)} ملف ترجمة مخزنة')
        return 0
    if command == 'library':
        return _library(argv)
    if command == 'project':
        return _project(argv)
    if command == 'example':
        return _example(argv)
    if command == 'format':
        return _format(argv)
    if command == 'path':
        return _path(argv)
    if command == 'build':
        return _build(argv)
    if command == 'trace':
        return _debug(argv, interactive=False)
    if command == 'debug':
        return _debug(argv, interactive=True)
    return _error(f'أمر غير معروف: {first}')


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        sys.stdout.close()
    except KeyboardInterrupt:
        print()
        raise SystemExit(130)

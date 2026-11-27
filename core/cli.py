"""عمار - واجهة سطر الأوامر للغة APL.

الأوامر الأساسية:
    عمار شغل ملف.apl          تشغيل برنامج
    عمار فحص ملف.apl          فحص الصياغة بدون تشغيل
    عمار ترجمة ملف.apl        طباعة كود Python المترجم
    عمار طرفية                موجه تفاعلي (REPL)
    عمار نسخة                 رقم الإصدار
    عمار مساعدة               المساعدة الكاملة
    عمار مسح-الكاش            حذف الترجمات المخزنة

المكتبات:
    عمار مكتبة تحميل <اسم>    تحميل مكتبة إلى مجلد المكتبات
    عمار مكتبة قائمة          المكتبات المثبتة
    عمار مكتبة بحث <كلمة>     البحث في مكتبات APL
    عمار مكتبة حذف <اسم>      حذف مكتبة محمّلة

الأسماء الإنجليزية (run, check, transpile, repl, version, help,
clear-cache, library) تعمل بنفس الطريقة.
"""
# APL - لغة عمار البرمجية
# Copyright (c) 2026 Ammar Elkhateeb (AmmarBasha2011)
# Distributed under the Python Software Foundation License Version 2 (PSF-2.0),
# the same license as Python. See LICENSE and NOTICE.

import difflib
import os
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
    # English spellings
    'run': 'run', 'check': 'check', 'transpile': 'transpile', 'repl': 'repl',
    'version': 'version', 'help': 'help', 'clear-cache': 'clear-cache',
    'library': 'library',
}

#: Sub-commands of `عمار مكتبة`.
LIBRARY_ALIASES = {
    'تحميل': 'install', 'نزل': 'install', 'نزّل': 'install', 'ثبت': 'install',
    'قائمة': 'list', 'المثبتة': 'list',
    'الكل': 'list-all', 'متاح': 'list-all',
    'بحث': 'search', 'ابحث': 'search',
    'حذف': 'remove', 'إزالة': 'remove', 'ازالة': 'remove', 'امسح': 'remove',
    'install': 'install', 'download': 'install', 'add': 'install',
    'list': 'list', 'all': 'list-all', 'search': 'search', 'find': 'search',
    'remove': 'remove', 'uninstall': 'remove',
}

#: Where `عمار مكتبة تحميل` fetches a library from.
DEFAULT_SOURCE = ('https://raw.githubusercontent.com/AmmarBasha2011/APL'
                  '/libraries/core/libraries/')
LIBRARY_SOURCE = os.environ.get('APL_LIBRARY_SOURCE', DEFAULT_SOURCE)


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
        print(diagnostic(error, None, source, file), file=sys.stderr)
        return 1
    print(f'سليم: {file}')
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

def _library_usage():
    print('الاستخدام: عمار مكتبة [تحميل|قائمة|بحث|حذف]')
    print('  عمار مكتبة تحميل <اسم>    تحميل مكتبة')
    print('  عمار مكتبة قائمة [الكل]   المكتبات المثبتة أو كل المكتبات')
    print('  عمار مكتبة بحث <كلمة>     البحث في المكتبات')
    print('  عمار مكتبة حذف <اسم>      حذف مكتبة محمّلة')
    return 0


def _library_install(name):
    import urllib.error
    import urllib.request
    from core.libraries import registry
    item = _catalog_by_name().get(name)
    if item is None:
        names = sorted(_catalog_by_name())
        close = difflib.get_close_matches(name, names, n=3)
        hint = f' هل تقصد: {"، ".join(close)}؟' if close else ''
        return _error(f'مكتبة غير معروفة: {name}.{hint}')
    if item['bundled']:
        print(f'مكتبة {name} جزء من APL ومثبتة بالفعل.')
        return 0
    folder = _library_folder()
    target = folder / (item['module'] + '.py')
    url = LIBRARY_SOURCE + item['module'] + '.py'
    request = urllib.request.Request(url, headers={'User-Agent': 'APL-library-manager'})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()
    except urllib.error.HTTPError as error:
        return _error(f'تعذر تحميل {name} من المكتبة المركزية ({error.code}).')
    except (urllib.error.URLError, OSError) as error:
        return _error(f'تعذر الاتصال بمصدر المكتبات: {error}')
    try:
        compile(data, url, 'exec')
    except SyntaxError as error:
        return _error(f'ملف المكتبة تالف: {error}')
    folder.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    try:
        registry.module(dict(item, bundled=False))
    except Exception as error:
        target.unlink(missing_ok=True)
        return _error(f'المكتبة اتحملت بس مش بتشتغل: {error}')
    registry.refresh()
    print(f'تم تحميل مكتبة {name} ({_size(item["size_kb"])}) إلى {target}')
    if item.get('package'):
        print(f'المكتبة دي بتستخدم حزمة Python اسمها {item["package"]}.')
        print(f'لو مش مثبتة: pip install {item["package"]}')
    return 0


def _library_list(show_all):
    from core.libraries.registry import (CATALOG, bundled_modules,
                                        downloaded_modules)
    by_module = CATALOG
    bundled = sorted(item['name'] for item in by_module.values() if item['bundled'])
    downloaded = sorted(item['name'] for item in by_module.values()
                        if not item['bundled'] and item['module'] in downloaded_modules())
    available = sorted(item['name'] for item in by_module.values()
                       if not item['bundled'] and item['module'] not in downloaded_modules())
    print(f'مثبتة مع APL ({len(bundled)}): {"، ".join(bundled)}')
    print(f'محمّلة ({len(downloaded)}): {"، ".join(downloaded) if downloaded else "لا شيء"}')
    print(f'متاحة للتحميل ({len(available)}) — المجلد: {_library_folder()}')
    if show_all:
        print('، '.join(available))
    else:
        print('اعرض الأسماء بـ: عمار مكتبة قائمة الكل')
    return 0


def _library_search(word):
    from core.libraries.registry import CATALOG, downloaded_modules
    hits = []
    for item in CATALOG.values():
        haystack = ' '.join((item['name'], item['module'], item.get('title') or ''))
        if word.lower() in haystack.lower():
            state = ('مثبتة' if item['bundled'] else
                     'محمّلة' if item['module'] in downloaded_modules() else 'متاحة')
            hits.append(f'  {item["name"]} — {state} — {item.get("title") or ""}')
    if not hits:
        return _error(f'مفيش مكتبة فيها: {word}')
    print(f'نتائج البحث عن "{word}" ({len(hits)}):')
    print('\n'.join(hits))
    return 0


def _library_remove(name):
    from core.libraries import registry
    item = _catalog_by_name().get(name)
    if item is None:
        return _error(f'مكتبة غير معروفة: {name}')
    if item['bundled']:
        return _error(f'مكتبة {name} جزء من APL، مش ممكن تتحذف.')
    target = _library_folder() / (item['module'] + '.py')
    if not target.is_file():
        return _error(f'مكتبة {name} مش محمّلة أصلاً.')
    target.unlink()
    registry.refresh()
    print(f'تم حذف مكتبة {name}.')
    return 0


def _library(rest):
    if not rest:
        return _library_usage()
    action = LIBRARY_ALIASES.get(rest[0]) or LIBRARY_ALIASES.get(rest[0].lower())
    args = rest[1:]
    if action in ('install', 'remove', 'search'):
        if not args:
            return _error(f'حدد اسم المكتبة. مثال: عمار مكتبة {rest[0]} numpy')
        return {'install': _library_install, 'remove': _library_remove,
                'search': _library_search}[action](args[0])
    if action in ('list', 'list-all'):
        return _library_list(action == 'list-all')
    return _library_usage()


# --------------------------------------------------------------------------

def main(argv=None):
    """نقطة الدخول: يقرأ الأمر وينفذه ويرجع رمز الخروج."""
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
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
        from core.runner.cache import clear
        print(f'تم حذف {clear()} ملف ترجمة مخزنة')
        return 0
    if command == 'library':
        return _library(argv)
    return _error(f'أمر غير معروف: {first}')


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        sys.stdout.close()
    except KeyboardInterrupt:
        print()
        raise SystemExit(130)

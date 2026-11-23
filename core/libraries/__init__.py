"""APL library compatibility API, backed by the unified registry."""
from .registry import ENTRIES, module

LIBRARIES = {entry['name']: module(entry) for entry in ENTRIES}
globals().update({entry['module']: LIBRARIES[entry['name']] for entry in ENTRIES})

def get_all_funcs():
    """Return a dict of {pattern_name: (funcs_dict, pattern, import_info)}"""
    result = {}
    for name, mod in LIBRARIES.items():
        pattern_name = name.upper() + "_PATTERN"
        result[name] = {
            "funcs": getattr(mod, name.upper() + "_FUNCS"),
            "pattern": getattr(mod, pattern_name),
            "import_name": mod.IMPORT_NAME,
            "import_check": mod.IMPORT_CHECK,
            "import_statement": mod.IMPORT_STATEMENT,
        }
    return result

def get_all_help():
    """Return help text lines for all libraries"""
    lines = []
    for name, mod in LIBRARIES.items():
        lines.append(f"# {name} library")
        for help_line in mod.HELP:
            lines.append(help_line)
        lines.append("")
    return lines


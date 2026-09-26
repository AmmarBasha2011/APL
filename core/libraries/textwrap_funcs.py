"""
APL - textwrap Library Functions
Transpiles Arabic keywords to Python textwrap module
"""

TEXTWRAP_FUNCS = {
    "التفاف_نص": "textwrap.fill",
    "الالتفاف_نص": "textwrap.fill",
    "التفاف_سطر": "textwrap.wrap",
    "الالتفاف_سطر": "textwrap.wrap",
    "اختصار_نص": "textwrap.shorten",
    "إزالة_التفافات": "textwrap.dedent",
    "إزاحة_نص": "textwrap.indent",
    "محاذاة_نص": "textwrap.fill",
    "حزم_النص": "textwrap.fill",
}

TEXTWRAP_PATTERN = r"(?<!\w)(" + "|".join(sorted(TEXTWRAP_FUNCS.keys(), key=len, reverse=True)) + r")\s*\("

# Help text for CLI
TEXTWRAP_HELP = [
    "# textwrap - تنسيق النصوص",
    "التفاف_نص(نص, 40)              - لف النص على عرض 40 حرف",
    "الالتفاف_نص(نص, 40)            - نفس الدالة (اسم بديل)",
    "التفاف_سطر(نص, 40)             - لف وإرجاع قائمة أسطر",
    "اختصار_نص(نص, 60)              - اختصار مع ... في النهاية",
    "إزالة_التفافات(نص)             - إزالة المسافات البادئة",
    "إزاحة_نص(نص, '  ')             - إضافة مسافة بادئة لكل سطر",
]

# Import detection
IMPORT_NAME = "textwrap"
IMPORT_CHECK = r"textwrap\."
IMPORT_STATEMENT = "import textwrap"

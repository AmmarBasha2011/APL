"""Trace and step through an APL program, in APL terms.

The interpreter runs Python, but a user thinks in APL lines, so both tools here
work on the APL source: the trace prints the APL line that is about to run, and
the stepper stops on it, never on the generated Python.

    عمار تتبع ملف.apl        print every APL line as it runs (no input needed)
    عمار مصحح ملف.apl        stop before each line and wait for a command

Commands in the stepper:

    (Enter) or س   خطوة — run this line, stop before the next
    ك or c         كمّل — run to the end, or to the next breakpoint
    م or v         متغيرات — print the program's variables
    خ or q         خروج — stop here

Breakpoints are APL line numbers: `عمار مصحح ملف.apl --توقف 12,20`.
"""
from __future__ import annotations

import sys

from core.runner.source import MARKER, source_line  # noqa: F401  (MARKER re-exported)


def line_map(python_code: str) -> dict:
    """Generated Python line → APL line, built once per program.

    `source_line` scans from the top on every call, which is fine for an error
    and far too slow for a traceback on every executed line.
    """
    mapping = {}
    current = 1
    for number, line in enumerate(python_code.splitlines(), 1):
        match = MARKER.match(line)
        if match:
            current = int(match.group(1))
        mapping[number] = current
    return mapping


def _apl_line(mapping: dict, generated: int) -> int:
    return mapping.get(generated, mapping.get(generated - 1, 1))


def _variables(namespace: dict, hidden=frozenset()) -> str:
    visible = {name: value for name, value in namespace.items()
               if not name.startswith('_') and name not in hidden}
    if not visible:
        return '  (مفيش متغيرات لسه)'
    lines = []
    for name in sorted(visible):
        text = repr(visible[name])
        if len(text) > 70:
            text = text[:67] + '…'
        lines.append(f'  {name} = {text}')
    return '\n'.join(lines)


def run(compilation, namespace: dict, interactive: bool = False,
        breakpoints=(), out=None, source: str | None = None,
        hidden=frozenset()) -> int:
    """Run one compiled program, tracing or stepping through its APL lines."""
    out = out or sys.stdout
    filename = compilation.filename
    mapping = line_map(compilation.python)
    lines = (source if source is not None else compilation.source).split('\n')
    stops = set(breakpoints)
    state = {'last': None, 'continue': not interactive, 'quit': False}

    def show(apl_line: int) -> None:
        text = lines[apl_line - 1].strip() if 0 < apl_line <= len(lines) else ''
        print(f'{apl_line:>4}: {text}', file=out, flush=True)

    def ask(apl_line: int) -> None:
        show(apl_line)
        while True:
            try:
                answer = input('(خطوة/كمّل/متغيرات/خروج) ').strip()
            except EOFError:
                state['continue'] = True
                return
            if answer in ('', 'س', 's'):
                return
            if answer in ('ك', 'c'):
                state['continue'] = True
                return
            if answer in ('م', 'v'):
                print(_variables(namespace, hidden), file=out, flush=True)
                continue
            if answer in ('خ', 'q'):
                state['quit'] = True
                return
            print('  أوامر: خطوة (Enter)، كمّل (ك)، متغيرات (م)، خروج (خ)', file=out)

    def tracer(frame, event, arg):
        if frame.f_code.co_filename != filename:
            return None
        if event == 'line':
            apl_line = _apl_line(mapping, frame.f_lineno)
            if apl_line != state['last']:
                state['last'] = apl_line
                if interactive:
                    if not state['continue'] or apl_line in stops:
                        state['continue'] = False
                        ask(apl_line)
                else:
                    show(apl_line)
            if state['quit']:
                raise SystemExit(130)
        return tracer

    previous = sys.gettrace()
    sys.settrace(tracer)
    try:
        exec(compilation.code, namespace)
    finally:
        sys.settrace(previous)
    return 0

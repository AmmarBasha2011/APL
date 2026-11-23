"""REPL evaluation and optional standard-library line editing."""
import ast
import atexit
from pathlib import Path


def configure(namespace):
    try:
        import readline
        import rlcompleter
        history = Path.home() / '.apl_history'
        try:
            readline.read_history_file(str(history))
        except OSError:
            pass
        readline.set_history_length(1000)
        readline.set_completer(rlcompleter.Completer(namespace).complete)
        readline.parse_and_bind('tab: complete')

        def save():
            try:
                readline.write_history_file(str(history))
                history.chmod(0o600)
            except OSError:
                pass
        atexit.register(save)
    except ImportError:
        pass  # Windows/minimal Python: evaluation still works.


def evaluate(source, namespace):
    from core.apl_runner.main import transpile
    tree = ast.parse(transpile(source), filename='<repl>', mode='exec')
    expression = tree.body.pop() if tree.body and isinstance(tree.body[-1], ast.Expr) else None
    exec(compile(tree, '<repl>', 'exec'), namespace)
    if expression:
        value = eval(compile(ast.Expression(expression.value), '<repl>', 'eval'), namespace)
        if value is not None:
            print(repr(value))

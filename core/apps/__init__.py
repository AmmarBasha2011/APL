"""APL companion apps: Terminal, Docs, Libraries, Examples and Benchmark.

Each one is a small program that ships inside the same executable as the
language and starts with `عمار <اسم>`. They use only the standard library.
"""


def launch(name, argv):
    """Start a companion app by name. Returns an exit code."""
    if name == "terminal":
        from core.apps import terminal
        return terminal.run(argv)
    if name == "docs":
        from core.apps import docs
        return docs.run(argv)
    if name == "libraries":
        from core.apps import docs
        return docs.run(argv, libraries=True)
    if name == "examples":
        from core.apps import examples
        return examples.run(argv)
    if name == "benchmark":
        from core.apps import bench
        return bench.run(argv)
    raise ValueError(name)

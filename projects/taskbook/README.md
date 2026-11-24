# Taskbook

A small multi-file SQLite application. `main.apl` handles CLI commands;
`storage.apl` owns persistence. No external packages are needed.

From the repository root after `pip install .`:

```sh
apl run projects/taskbook/main.apl /tmp/tasks.db add 'Read the guide'
apl run projects/taskbook/main.apl /tmp/tasks.db list
apl run projects/taskbook/main.apl /tmp/tasks.db done 1
apl run projects/taskbook/main.apl /tmp/tasks.db list
```

The database path is explicit. The application creates that file; remove it
when finished. SQL values use parameters. See `tests/test_core.py::test_taskbook`
for the add/list/done persistence test. Names and imports demonstrate APL's
Python-backed module model; this is not a remote package manager.

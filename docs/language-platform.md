# Language platform

This PR keeps the Python backend and existing aliases. It does not publish a
package, extension or website, and does not change the license.

## Install and run

Python 3.14 or newer:

```sh
python -m venv .venv
. .venv/bin/activate
pip install .
apl --version
apl run projects/taskbook/main.apl /tmp/tasks.db add 'Learn APL'
apl run projects/taskbook/main.apl /tmp/tasks.db list
apl run projects/taskbook/main.apl /tmp/tasks.db done 1
apl check projects/taskbook/main.apl
apl transpile projects/taskbook/main.apl > /tmp/program.py
```

The core has no third-party dependencies. Optional groups are available with
`pip install '.[web]'`, `'.[science]'` and `'.[bots]'`. The repository's pinned
`requirements.txt` remains the full test/development environment. Installing
an optional group does not promise support for every generated external API.

`python apl.py FILE` and `python apl.py -c CODE` still work. `apl run FILE ARGS`
sets `sys.argv`, `__name__ = '__main__'` and `__file__`. Local imports resolve
`module.apl` and packages with `__init__.apl`, including relative imports inside
packages, using ordinary Python import caching and cycles semantics. Python
imports remain available. Run projects you trust: APL is not a restricted
language or a sandbox on your own computer.

`check` compiles without executing source. Diagnostics contain a stable
`APL-ExceptionType` prefix, file, source line and a source-column anchor.
For rewritten statements the caret is deliberately at the first source token,
not a claimed exact Python-token offset. `run --debug FILE` also shows the
Python traceback. Generated code includes source markers, so imports, aliases
and multiline literals do not shift normal diagnostic source lines.

The legacy global replacement state is protected by a compilation lock and
reset per compilation. This provides correctness, not parallel compilation
speed. Optimizations run before literal restoration. Malformed declarations
now abort before any program statement runs. F-string expressions retain
legacy Arabic replacement support; arbitrary modern Python f-string nesting
is not a newly promised feature in this change.

## Library registration

`core/libraries/registry.json` is the ordered registration source. It drives
`LIBRARIES`, lazy module names, generated-library substitution, Python import
insertion and the editor vocabulary export. Existing `*_funcs.py` tables remain
the source of Arabic spellings and Python targets. Per-library token Bloom filters avoid loading large generated tables for
unrelated words. False positives only cause an extra load; they never alter
lookup results. Regenerate filters after vocabulary changes. Compatibility regexes for
older small libraries remain in the inline engine; migrating those regexes is
not necessary to add another generated library.

To add a generated library: add its `*_funcs.py`, then one JSON entry with its
public `*_SUBSTITUTE` name and import metadata. There is no need to edit four
registration lists. Core syntax, declared variables, function parameters and
user-assigned attributes take precedence over generated-library vocabulary.
Unknown API signatures stay null in the normalized symbol API. We do not
invent signatures or load optional packages just to fill completion metadata.

```sh
python scripts/update_registry_filters.py
python scripts/export_editor_index.py
python scripts/export_editor_index.py --check
```

The checked-in editor index is compressed to avoid a huge source file. It is a
generated artifact, not a second editable vocabulary. Large vocabulary indexes
can use noticeable editor memory; completion is limited to 100 matching items.

## VS Code and REPL

Open `editors/vscode` in VS Code and use an Extension Development Host (F5), or
package locally with `npx @vscode/vsce package`. Do not publish without the
owner's separate approval. Install `apl` first, or set `apl.executable` to its
absolute path. Syntax and snippets work offline; completion/hover use the
shared generated index. Saved-file diagnostics call `apl check`, never run a
program. Executable launch is disabled in untrusted workspaces. This is a small
extension, not a full LSP server or a promise of semantic/type completion.

`apl repl` retains variables, echoes expression results and supports standard
readline history/completion when readline is available. History is stored at
`~/.apl_history`; do not type secrets into a code history. No history support is
required on platforms without readline.

## Local playground and isolation

```sh
docker build -f playground/Dockerfile -t apl-playground:local .
python -m playground.server
# Open http://127.0.0.1:8765
APL_DOCKER_TESTS=1 python -m unittest discover -s tests -p test_sandbox.py -v
```

The service binds only 127.0.0.1, checks Host and Origin, and has no CORS access.
It is for local development. Do not expose it to the internet or forward its
port. Public hosting needs a separate security review, authentication, quotas,
a hardened runtime/VM boundary and an abuse/patching plan. Docker containers
share the host kernel and are not a claim of VM-grade protection against
hostile multi-tenant code. Keep Docker and the host patched. The server needs
Docker-daemon access, so run it only under a local account you trust.

Each run uses a new disposable container: no host mounts, no environment
secrets, no network, read-only image, non-root UID, dropped capabilities,
no-new-privileges, Docker's default seccomp, 128 MiB memory/swap cap, 0.5 CPU,
2-second CPU limit, 32 processes, a 16 MiB /tmp and file limits. Source is capped
at 16 KiB; combined stdout/stderr is capped at 32 KiB and wall time at 6 seconds.
The container is removed on every exit path. External packages are not included
in the worker image. There is no fallback to server-side `exec`. Without Docker
or a built image the server refuses to start. The browser uses textContent for
output and a restrictive content security policy.

The Docker job exercises execution, infinite loops, output floods, network
failure, read-only files, memory exhaustion and container cleanup. These tests
are a regression gate, not an independent security audit.

## Tests

```sh
python -m unittest discover -s tests -v
node --test editors/vscode/test/*.test.js
python scripts/export_editor_index.py --check
python test_examples.py
python scripts/check_libraries.py
python scripts/check_repo.py
python -m build
```

The language-platform workflow also installs the wheel in a clean environment
and runs the multi-file SQLite taskbook. Existing repository checks are kept.

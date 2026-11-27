"""Source-spanning literal protection and source-map markers."""
import re
import uuid

MARKER = re.compile(r"^\s*# apl-source:(\d+)\s*$")


def protect(source):
    """Hide literals/comments before any keyword or library substitution.

    Literal spelling is restored only after optimization. F-string expressions
    use Python syntax, as before; no substitutions happen inside a literal.
    """
    prefix = "_APL_LITERAL_" + uuid.uuid4().hex + "_"
    values, out, origins = {}, [], [1]
    i, line = 0, 1
    while i < len(source):
        ch = source[i]
        if ch == '#':
            end = source.find('\n', i)
            if end < 0:
                end = len(source)
            # Retain a comment marker so comment-only lines remain comments.
            key = prefix + str(len(values)) + '_END_'
            values[key] = source[i:end]
            out.append('# ' + key)
            i = end
            continue
        if ch in "\"'":
            quote = ch * (3 if source.startswith(ch * 3, i) else 1)
            j = i + len(quote)
            while j < len(source):
                if source[j] == '\\':
                    j += 2
                    continue
                if source.startswith(quote, j):
                    j += len(quote)
                    break
                if source[j] == '\n' and len(quote) == 1:
                    raise SyntaxError('unterminated string literal', ('<apl>', line, 1, source.splitlines()[line - 1]))
                j += 1
            else:
                raise SyntaxError('unterminated string literal', ('<apl>', line, 1, source.splitlines()[line - 1]))
            # Prefix letters already emitted belong to the literal too.
            before = ''.join(out)
            match = re.search(r'(?<!\w)([rRuUbBfF]{1,2})$', before)
            literal_prefix = ''
            if match:
                literal_prefix = match.group(1)
                joined = before[:-len(literal_prefix)]
                out = [joined]
            key = prefix + str(len(values)) + '_END_'
            literal = source[i:j]
            values[key] = literal_prefix + literal
            out.append(key)
            line += literal.count('\n')
            i = j
            continue
        out.append(ch)
        if ch == '\n':
            line += 1
            origins.append(line)
        i += 1
    return ''.join(out), values, origins


def restore(code, values):
    for key, literal in values.items():
        if re.match(r"(?i)^f[\"']", literal):
            from core.runner.inline_replacer import _inline_replace
            literal = _inline_replace(literal)
        code = code.replace('# ' + key, literal) if literal.startswith('#') else code.replace(key, literal)
    return code


def source_line(code, generated_line):
    current = 1
    for line in code.splitlines()[:generated_line]:
        match = MARKER.match(line)
        if match:
            current = int(match.group(1))
    return current

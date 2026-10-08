#!/usr/bin/env python3
"""Check that the text shared by the OWGTM CP/CPS documents is identical.

Shared text is delimited in each document by HTML comments:

    <!-- common:begin ID -->
    ...
    <!-- common:end ID -->

The script compares every block ID present in more than one document and
exits with status 1 if any block differs, is unbalanced, or is duplicated.

Usage:
    python3 tools/check_common_sections.py OWGTMTLSCPS.md OWGTMSMIMECPS.md

With --include TEMPLATE SOURCE OUTPUT it instead expands the placeholders
<!-- common:include ID --> of TEMPLATE with the blocks of SOURCE.
"""
import difflib
import re
import sys

BLOCK = re.compile(r'<!-- common:begin (\S+) -->\n(.*?)<!-- common:end \1 -->', re.S)


def blocks(path):
    text = open(path, encoding='utf-8').read()
    begins = re.findall(r'<!-- common:begin (\S+) -->', text)
    ends = re.findall(r'<!-- common:end (\S+) -->', text)
    errors = []
    if begins != ends:
        errors.append(f'{path}: unbalanced common markers')
    dups = sorted({b for b in begins if begins.count(b) > 1})
    if dups:
        errors.append(f'{path}: duplicated blocks {dups}')
    return {m.group(1): m.group(2) for m in BLOCK.finditer(text)}, errors


def check(paths):
    found, errors = {}, []
    for p in paths:
        b, e = blocks(p)
        found[p] = b
        errors += e
    ids = sorted({i for b in found.values() for i in b})
    compared = 0
    for i in ids:
        holders = [p for p in paths if i in found[p]]
        if len(holders) < 2:
            errors.append(f'block {i} only in {holders[0]}')
            continue
        ref = holders[0]
        for p in holders[1:]:
            compared += 1
            if found[p][i] != found[ref][i]:
                diff = difflib.unified_diff(found[ref][i].splitlines(), found[p][i].splitlines(),
                                            ref, p, lineterm='', n=1)
                errors.append(f'block {i} differs:\n' + '\n'.join(diff))
    for e in errors:
        print('ERROR:', e)
    print(f'{len(ids)} common blocks, {compared} comparisons, {len(errors)} errors')
    return 1 if errors else 0


def include(template, source, output):
    src, errors = blocks(source)
    if errors:
        sys.exit('\n'.join(errors))
    text = open(template, encoding='utf-8').read()

    def repl(m):
        i = m.group(1)
        if i not in src:
            sys.exit(f'block {i} not found in {source}')
        return f'<!-- common:begin {i} -->\n{src[i]}<!-- common:end {i} -->'

    open(output, 'w', encoding='utf-8').write(re.sub(r'<!-- common:include (\S+) -->', repl, text))


if __name__ == '__main__':
    if len(sys.argv) == 5 and sys.argv[1] == '--include':
        include(*sys.argv[2:])
    elif len(sys.argv) >= 3:
        sys.exit(check(sys.argv[1:]))
    else:
        sys.exit(__doc__)

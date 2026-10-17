#!/usr/bin/env python3
"""Parse S1 (sanskrit/raw_etexts .../rAmAyaNam/baroda_alt.md) into per-chapter
files text/chPP.CCC.md with lines 'PP.CCC.V[x] | text'.
Usage: parse_baroda_alt.py SOURCE OUTDIR [--dry]
Text is copied unchanged (NFC, trailing spaces trimmed). Never retype verses."""
import re, sys, json, unicodedata
from collections import OrderedDict
src, out = sys.argv[1], sys.argv[2]
dry = '--dry' in sys.argv
DIG = {ord(c): str(i) for i, c in enumerate('०१२३४५६७८९')}
num = lambda s: int(s.translate(DIG))
ID = re.compile(r'^([१२३४५६७])\.([०-९]{3})\.([०-९]{3})\s(.*)$')
chapters = OrderedDict()   # (k,s) -> list of [verse, text, orphan?]
issues = []
last = None
for n, raw in enumerate(open(src, encoding='utf8'), 1):
    line = unicodedata.normalize('NFC', raw.rstrip('\n')).strip()
    if not line:
        continue
    m = ID.match(line)
    if m:
        k, s, v, t = num(m[1]), num(m[2]), num(m[3]), m[4].strip()
        chapters.setdefault((k, s), []).append([v, t, n, False])
        last = (k, s)
    else:  # fragment without an ID: keep in order, flag
        chapters[last].append([chapters[last][-1][0], line, n, True])
meta = []
for (k, s), rows in chapters.items():
    lines, i = [], 0
    byverse = OrderedDict()
    for r in rows:
        byverse.setdefault(r[0], []).append(r)
    for v, rs in byverse.items():
        for j, r in enumerate(rs):
            letter = '' if len(rs) == 1 else 'abcdefgh'[j]
            lid = f'{k:02d}.{s:03d}.{v}{letter}'
            lines.append(f'{lid} | {r[1]}')
            if r[3]:
                issues.append((lid, 'source line %d has no verse ID; kept as its own line in source order' % r[2]))
    meta.append((k, s, len(byverse), len(lines)))
    if not dry:
        open(f'{out}/ch{k:02d}.{s:03d}.md', 'w', encoding='utf8').write('\n'.join(lines) + '\n')
json.dump({'chapters': meta, 'issues': issues}, open(f'{out}/../parse_report.json' if not dry else '/dev/null', 'w'))
print(len(meta), 'chapters', sum(m[2] for m in meta), 'verses', sum(m[3] for m in meta), 'lines', len(issues), 'orphans')

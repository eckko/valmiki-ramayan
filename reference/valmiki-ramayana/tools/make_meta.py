#!/usr/bin/env python3
"""Write toc.md and STATUS.md from parse_report.json (run after parse_baroda_alt.py)."""
import json
r = json.load(open('parse_report.json'))
D = '०१२३४५६७८९'
dn = lambda n: ''.join(D[int(c)] for c in str(n))
K = {1:('बालकाण्डम्','Bālakāṇḍa','Book of the Boyhood'),2:('अयोध्याकाण्डम्','Ayodhyākāṇḍa','Book of Ayodhyā'),
     3:('अरण्यकाण्डम्','Araṇyakāṇḍa','Book of the Forest'),4:('किष्किन्धाकाण्डम्','Kiṣkindhākāṇḍa','Book of Kiṣkindhā'),
     5:('सुन्दरकाण्डम्','Sundarakāṇḍa','Book of Beauty'),6:('युद्धकाण्डम्','Yuddhakāṇḍa','Book of the War'),
     7:('उत्तरकाण्डम्','Uttarakāṇḍa','Final Book')}
CE = {1:76,2:111,3:71,4:66,5:66,6:116,7:100}
by = {}
for k,s,v,l in r['chapters']: by.setdefault(k,[]).append((s,v,l))
tv = sum(v for _,_,v,_ in r['chapters']); tl = sum(l for _,_,_,l in r['chapters'])
o = ['# Vālmīki Rāmāyaṇa (वाल्मीकिरामायणम्): Baroda Critical Edition','',
 '- Author / compiler: Vālmīki (tradition: ādikavi, first poet); this is the text as reconstructed by the Baroda Critical Edition, which leaves out passages the manuscripts show to be later additions',
 '- Subject and purpose of the book: the story of Rāma, told in 7 kāṇḍas; the text itself opens with Vālmīki asking Nārada for a man of all virtues (inferred from the opening verses)',
 '- Base edition: The Vālmīki-Rāmāyaṇa, Critical Edition, 7 vols, ed. G. H. Bhatt, P. L. Vaidya et al., Oriental Institute, Baroda, 1960-1975, as typed in S1 (see sources.md)',
 '- Mapping: part = kāṇḍa (01-07), chapter = sarga (3-digit), verse = śloka number as in the source; each verse is written on 2 or more lines (a, b, c...)',
 f'- Totals: 7 parts, {len(r["chapters"])} chapters, {tv} verses, {tl} lines extracted (traditional verse count: unknown; sarga counts per kāṇḍa match the Critical Edition: 76, 111, 71, 66, 66, 116, 100)',
 '- Titles: the Critical Edition prints no sarga titles and S1 has none, so the Sanskrit name column holds only "सर्गः N" and purposes are left empty rather than invented. Chapter titles are a later stage.','']
st = ['# Status: valmiki-ramayana','','Updated: 2026-10-17 on branch docs/2026-10-17/version-1. Base source: S1 (all chapters).','',
 '| Part | Chapter | Sanskrit lines | Source | Hindi | English | Check | Notes |','|---|---|---|---|---|---|---|---|']
for k in sorted(by):
    sk,iast,en = K[k]
    o += [f'## Part {k:02d}: {sk} ({iast}, {en})','',f'Purpose: not stated in source ({len(by[k])} sargas).','',
          '| Part | Chapter | Sanskrit name | English name | Purpose | Verses (extracted) | Verses (traditional) | File | Status |','|---|---|---|---|---|---|---|---|---|']
    for s,v,l in by[k]:
        o.append(f'| {k:02d} | {s:03d} | सर्गः {dn(s)} | Sarga {s} | | {v} | unknown | text/ch{k:02d}.{s:03d}.md | extracted |')
        st.append(f'| {k:02d} | {s:03d} | {l} | S1 | -- | -- | pass | |')
    o.append('')
st += ['','## Next','- Await owner confirmation of the chapter map and edition scope (toc.md).','- Translations (Hindi, English) not yet sought; Sanskrit first.','- Cross-check against S2 (baroda/ folder, kāṇḍas 1-6) not done at verse level: S2 is sandhi-split and laid out differently, so line counts do not compare. A word-level comparison is the next check.']
open('toc.md','w',encoding='utf8').write('\n'.join(o)+'\n'); open('STATUS.md','w',encoding='utf8').write('\n'.join(st)+'\n')
iss = ['# Issues: valmiki-ramayana','','| Line ID | Kind | What | Source(s) | Suggested check |','|---|---|---|---|---|']
for lid,msg in r['issues']: iss.append(f'| {lid} | other | {msg} | S1 | compare with Baroda print edition |')
iss += ['| 07.026.31b | possible-typo | double space inside the line in S1 | S1 | check against print edition |',
 '| all | other | S1 has no daṇḍa (।) or verse-end mark (॥) on any line; the Sanskrit lines are the source\'s bare pādas | S1 | S2 keeps । and ॥ and could supply them in a later stage |',
 '| all | possible-typo | the Vedic accent mark ॑ (U+0951) occurs 1,717 times in 332 chapter files of S1, usually at the end of a pāda before a pause; kept as in the source | S1 | check against print edition and S2 |',
 '| all | order | verses with 3 or 4 lines (588 and 5 verses) and 82 one-line verses exist in S1; these are the source\'s own line counts, kept as is | S1 | compare with Baroda print |']
open('ISSUES.md','w',encoding='utf8').write('\n'.join(iss)+'\n')

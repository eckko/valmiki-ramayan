# Issues: valmiki-ramayana

| Line ID | Kind | What | Source(s) | Suggested check |
|---|---|---|---|---|
| 02.048.36c | other | source line 6831 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 02.073.17c | other | source line 8112 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 02.088.27c | other | source line 8946 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 02.098.70b | other | source line 9643 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 02.099.17c | other | source line 9681 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 02.099.18b | other | source line 9683 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 02.099.19b | other | source line 9686 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 02.108.25b | other | source line 10156 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 02.108.25d | other | source line 10158 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 03.021.26b | other | source line 11624 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 03.044.33c | other | source line 12928 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 04.040.47c | other | source line 17225 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 05.039.8b | other | source line 21857 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 05.045.1c | other | source line 22138 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 06.097.31b | other | source line 31291 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 07.011.41b | other | source line 33459 has no verse ID; kept as its own line in source order | S1 | compare with Baroda print edition |
| 07.026.31b | possible-typo | double space inside the line in S1 | S1 | check against print edition |
| all | other | S1 has no daṇḍa (।) or verse-end mark (॥) on any line; the Sanskrit lines are the source's bare pādas | S1 | S2 keeps । and ॥ and could supply them in a later stage |
| all | possible-typo | the Vedic accent mark ॑ (U+0951) occurs 1,717 times in 332 chapter files of S1, usually at the end of a pāda before a pause; kept as in the source | S1 | check against print edition and S2 |
| all | order | verses with 3 or 4 lines (588 and 5 verses) and 82 one-line verses exist in S1; these are the source's own line counts, kept as is | S1 | compare with Baroda print |

## Word check and AI proofreading (2026-10-17, stage 2)
Checks that ran: stray-character scan, typo-candidate scan (rare token one akshara from a frequent token), metre outliers, AI reading of the flagged lines plus a fixed-seed sample. Second edition: not available, skipped. The text in `text/` is unchanged.

| Check | Flagged | AI read | Proposals |
|---|---|---|---|
| stray characters | 3 | 3 | 3 error (anusvara plus visarga, e.g. 01.073.13b, 02.047.19a, 07.068.8a) |
| typo candidates | 482 | 482 | 52 error, 3 unsure |
| metre outliers (not 15-17 / 22-26 aksharas) | 691 | 691 | 38 error, 3 unsure |
| ordinary-line sample | 246 | 246 | 8 error, 2 unsure |

- Sample error rate: 8 of 246 ordinary lines (3.3%) have a typing error by the AI reading. That is about 1,200 lines in 38,054 if the sample is representative (rough range 1.4% to 6.3%). Lines nobody read are not verified.
- Proposals are in `checks/proposals.tsv` (109 rows) and `checks/PROOFREAD.md`. Each is a candidate to check against the printed edition; none has been applied.
- Two kinds of proposal are layout faults of S1, not wrong aksharas: a last word split onto its own line (for example 02.048.36c, 02.073.17c, 04.040.47c, 06.097.31, 07.011.41) and a stray space inside a word. The 16 ID-less fragments already logged above are of this kind.
- Typos noticed by agents in context lines outside their items, not yet in proposals.tsv: 07.035.38a (प्रांषुं), 07.073.12b (प्र्पग्रहो), 06.088.59a (सर्वबूतानां).
- Not covered by any check: errors that form another valid word, and lines outside the flagged and sampled sets. S1 has no daṇḍas, so the structure check's "truncated?" flags (7) are all false alarms.

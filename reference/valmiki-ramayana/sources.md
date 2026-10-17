# Sources: valmiki-ramayana

| ID | Name | URL | Edition / editor / year | Script | Licence | Covers | Fetched how | Quality note | Role |
|---|---|---|---|---|---|---|---|---|---|
| S1 | `baroda_alt.md` in sanskrit/raw_etexts | https://github.com/sanskrit/raw_etexts/blob/d0754ea9d5b68d74f5fed4783543ad1814e45e07/purANam/vaiShNavam/rAmAyaNam/baroda_alt.md | Baroda Critical Edition (Oriental Institute, Baroda, 1960-1975); typist and exact provenance not stated in the repo (the repo's other Baroda copy is labelled Tokunaga/Smith e-text lineage by sanskritdocuments.org) | Devanagari, sandhi joined | unknown (repo has no licence file; recorded for the owner to decide) | all 7 kāṇḍas, 606 sargas, 18,761 verse numbers | `git clone --depth 1` of sanskrit/raw_etexts; file sha256 `af69a5e960727daf8dd53fb4e79d8d77cf1a557ec649c5a02efe9e7ab3fe5162` (5,272,257 bytes, commit d0754ea, 2026-10-13) | sarga counts equal the Critical Edition (76, 111, 71, 66, 66, 116, 100); no daṇḍas; 16 ID-less fragments; repo says some files are non-proofread | primary |
| S2 | `baroda/` folder in the same repo | https://github.com/sanskrit/raw_etexts/tree/d0754ea9d5b68d74f5fed4783543ad1814e45e07/purANam/vaiShNavam/rAmAyaNam/baroda | Baroda Critical Edition, sandhi-split reading text | Devanagari, words split | unknown | kāṇḍas 1-6 only (no Uttarakāṇḍa) | same clone | split words and nasal spelling differ from S1, so only a word-level comparison is meaningful | cross-check (not yet done) |

## Not used, and why
- `goraxapuram/` in the same repo: Gita Press (vulgate) text, which includes later additions; not what was asked.
- imradhe/ramayanam and AshuVj/Valmiki_Ramayan_Dataset: both follow the vulgate sarga counts (77/119/75/67/68/131) from the IIT Kanpur / Gita Press text; not the critical text.
- GRETIL / TITUS / Sanskrit Library TEI (Bālakāṇḍa only) / sanskritdocuments mirror / archive.org scans of the 7 printed volumes: not reachable from the shell (HTTP refused). The sanskritdocuments mirror is the same Baroda edition (Tokunaga's e-text); if you want an independent S3 for cross-checking, download its files and add them to the repo.

## Notes on conversion
No script conversion: S1 is already Devanagari. `tools/parse_baroda_alt.py` splits S1 by the `K.SSS.VVV` prefix into `text/chKK.SSS.md`; the prefix numbers become the ID (`KK.SSS.V`), repeated verse numbers get line letters a, b, c in source order, and text is copied unchanged (NFC, outer spaces trimmed).

## Decisions for the owner
- Scope: the Critical Edition includes the Uttarakāṇḍa (100 sargas) and the opening of the Bālakāṇḍa; many scholars consider both later than the core. They are extracted as part of the edition, in their own files, so they are easy to drop.
- Licence of S1 is unknown.

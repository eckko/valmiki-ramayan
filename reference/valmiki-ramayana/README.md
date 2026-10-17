# Vālmīki Rāmāyaṇa (Baroda Critical Edition): raw extracted source bank

Stage 1 (extraction) of a pipeline: verify, review, fix, proofread come next. This folder holds the raw text, not a finished edition. Nothing here has been proofread.

Read, in order: FORMAT.md (file and line format), toc.md (structure), STATUS.md (what is done), sources.md (where text came from), ISSUES.md (known doubts).

Rules for anyone editing here:
- Text lines come only from sources listed in sources.md; never from memory.
- Do not rename files or change line IDs of finished chapters.
- Record every doubt in ISSUES.md; fix text only in a later, explicit proofreading stage.
- Run `python3 reference/tools/check_extraction.py reference/valmiki-ramayana` before every commit.
- Branch pattern: `docs/YYYY-MM-DD/version-N`; push new branches only; the owner merges.

Layout: one file per sarga, `text/chKK.SSS.md` (KK = kāṇḍa 01-07, SSS = sarga). `tools/parse_baroda_alt.py` rebuilds the text from S1; `tools/make_meta.py` rebuilds toc.md, STATUS.md and ISSUES.md.

How to continue: open STATUS.md, take the first chapter not marked extracted, follow the skill `/extract-vedic-book-web` (or the steps in FORMAT.md and sources.md if the skill is not available).

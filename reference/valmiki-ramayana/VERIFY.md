# Verify log: valmiki-ramayana

Dated log of stage 2 (`/verify-vedic-book-reference`). Append only.

## 2026-10-17, branch docs/2026-10-17/version-1
- Inventory: `inventory.py` asked 4 questions; all were false positives (latin-text files are this folder's own scripts and the shared `reference/tools/check_extraction.py`; toc.md exists in the book folder). Base is the Devanagari `text/` from S1 (Baroda Critical Edition). Owner confirmed repo eckko/valmiki-ramayan.
- Structure: 7 parts, 606 chapters, 18,761 verse numbers, no gaps, no toc mismatches. The 7 "TRUNCATED?" flags are false alarms: S1 has no daṇḍas on any line (ISSUES.md).
- check_extraction.py: 0 errors, 1 warning (double space ch07.026 line 64).
- word_check.py: 173,946 tokens; 3 stray, 482 typo candidates, 691 metre outliers. Second edition: not available, skipped.
- Proofreading: 24 packs of 1,422 items (3 stray, 482 typo?, 691 metre, 246 sample), each read by a separate agent on the strongest model (fable). All answered. 109 proposals (101 error, 8 unsure). Sample error rate 8/246 = 3.3%. Summary in ISSUES.md. `text/` unchanged.

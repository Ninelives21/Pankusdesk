# MAC pages delta — 28 Aug 2026

This delta adds the R25 Matrices and Calculus subject framework using the current College Design Lock v2 architecture.

## Added

- `college/1-1/matrices-calculus/`
  - subject home
  - official R25 syllabus page
  - Unit I–V shells
  - subject-wide PYQ scaffold
  - class-log shell
  - syllabus/topic/coverage/source-lock KB data
  - Unit I–V human-readable scaffold notes
  - MAC-specific verifier
- `styles/new/pages/syllabus.css` — shared syllabus-page styling

## Updated

- `college/1-1/semester.json` — enables the Matrices and Calculus subject card/navbar link.
- `college/1-1/basic-electrical-engineering/r25-syllabus.html` — points BEE at the new shared syllabus stylesheet.
- `college/1-1/basic-electrical-engineering/kb/data/topics.json` — three small wording cleanups in Unit II so the Design Lock v2 global verifier passes; no BEE scope/source changes.

## Publication state

All five MAC units intentionally remain `scaffold`. The official R25 syllabus is mapped to 43 stable syllabus atoms/topic IDs, but no prescribed-textbook/lecture source corpus was supplied with this build. Detailed theory is therefore not invented.

## Apply

From the directory containing the extracted `mac-pages-delta` folder:

```bash
rsync -avhn mac-pages-delta/ /path/to/Pankusdesk/
rsync -avh mac-pages-delta/ /path/to/Pankusdesk/
```

Do not add `--delete`.

## Verify

From the Pankusdesk repository root:

```bash
python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py
python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py
python3 scripts/tools/verify_college.py
```

Expected result: all three PASS.

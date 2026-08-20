# Basic Electrical Engineering KB — 25ES1EE101 · R25

This is the **content / evidence layer** for the BEE subject in Panku’s Desk. It is designed so the eventual subject page and BEE Expert can be generated from source-grounded material without repeatedly rereading hundreds of screenshots.

## Non-negotiable source rules

1. **R25 is the syllabus authority.** A supplied source cannot add a new core syllabus topic by itself.
2. **No phantom knowledge.** Every knowledge record has `source_refs` that resolve through the source manifest/index.
3. **No silent repair.** If a source is ambiguous or appears mislabeled, the ambiguity is recorded (not silently corrected). See the SFU/ELCB caution in Unit V.
4. **Preserve supplied extras.** Material supplied but outside R25 is retained in `notes/supporting-outside-r25.md`, not thrown away and not promoted to core.
5. **Gap material is explicit.** Swinburne’s test, synchronous-impedance regulation, synchronous-motor principle and ELCB are marked `core-gap-filled` and cite the approved verification sources.
6. **Copyright boundary.** Commercial textbook PNGs are not stored in the public workspace. Book references point to printed page + source image filename so the physical book can be used.

## Files

- `data/syllabus.json` — atomised official R25 scope.
- `data/topics.json` — machine-readable knowledge records used by future pages/AI.
- `data/coverage-audit.json` — each R25 atom → topic(s) → sources.
- `data/source-manifest.json` — exact input archives/files, hashes and gap sources.
- `data/book-index.json` — every captured textbook page/image accounted for.
- `data/lecture-index.json` — every supplied lecture transcript accounted for.
- `data/supplementary-pdf-index.json` — all 97 pages of the extra PDF accounted for.
- `notes/unit-1.md` … `unit-5.md` — human-readable unit knowledge.
- `notes/formulas-methods.md` — source-grounded formula index.
- `notes/source-reference-map.md` — page/image/lecture source map.
- `notes/source-accounting.md` — corpus completeness audit.
- `notes/coverage-audit.md` — human-readable R25 coverage result.
- `notes/supporting-outside-r25.md` — supplied material deliberately kept outside core.
- `tools/verify_kb.py` — deterministic integrity checks.

## Status labels

- `core` — directly within an R25 syllabus atom.
- `supporting` — source-supplied material useful to understand core, but not a separate R25 atom.
- `core-gap-filled` — R25-required material absent/ambiguous in the main supplied corpus and filled from the approved gap sources.

## Next layer

The future BEE subject UI should read the JSON/Markdown in this folder and present five unit cards, Learn, Formula & Method, Worked Example references, Exam Questions and Common Confusions. PYQs can be added later as a new provenance layer without altering the source-locked theory corpus.

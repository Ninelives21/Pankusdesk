# Unit Build Checklist

Use this checklist for every new college unit, regardless of subject or semester.

## A. Start

- [ ] Read `college/COLLEGE_BUILD_STANDARD.md`.
- [ ] Read `college/REFERENCE_IMPLEMENTATION.md`.
- [ ] Inspect the latest workspace, not an old delta/chat reconstruction.
- [ ] Inspect target `subject.json`, target unit status, generic renderers, and current schemas.

## B. Source intake

- [ ] Inventory official syllabus/regulation source.
- [ ] Inventory prescribed textbook pages/figures/questions.
- [ ] Inventory supplied lectures/transcripts.
- [ ] Inventory class notes/daily material.
- [ ] Inventory supplementary sources.
- [ ] Record known missing files/lecture numbers/anomalies exactly.

## C. Syllabus and gaps

- [ ] Atomise the official unit syllabus.
- [ ] Map every atom to real source references.
- [ ] Mark unsupported required material as `SOURCE_GAP`.
- [ ] Obtain explicit approval before using outside gap sources.
- [ ] Record approved gap sources/provenance.

## D. Cumulative theory

- [ ] Build/update stable topic IDs.
- [ ] Set each topic to `core`, `supporting`, or `core-gap-filled` correctly.
- [ ] Consolidate overlapping textbook/lecture/class explanations.
- [ ] Remove duplication.
- [ ] Write theory as theory—no source/workflow commentary.
- [ ] Add formulas/methods/cautions only when source-backed/useful.
- [ ] Add section/topic provenance.
- [ ] Synchronize human-readable `unit-N.md` where used.

## E. Self-checks and practice

- [ ] Keep generated self-checks distinct from official textbook questions.
- [ ] Audit all prescribed chapter-end questions for the unit.
- [ ] Preserve official question wording.
- [ ] Never invent unsupported answers.
- [ ] Flag source gaps/discrepancies explicitly.
- [ ] Give each question a stable ID/anchor.
- [ ] Link “Practice from the prescribed book” to exact question anchors.

## F. Figures

- [ ] Audit which figures are actually needed before cropping/redrawing.
- [ ] Put theory figures in `assets/book/uN/theory/`.
- [ ] Put question/example figures in `assets/book/uN/examples/`.
- [ ] Follow `college/NOTEBOOK_REDRAW_STYLE.md`.
- [ ] Verify topology/labels/values against source.
- [ ] Use descriptive alt text.
- [ ] Add exact insertion anchors in topic data.
- [ ] Record intrinsic width/height when available.
- [ ] Do not expose internal capture filenames in student UI.

## G. Daily class notes (when supplied)

- [ ] Preserve dated verbatim record separately.
- [ ] Map dated record to stable topic IDs.
- [ ] Integrate only useful new theory into cumulative topics.
- [ ] Preserve lecturer emphasis/assignments in the correct structured layer.
- [ ] Flag contradictions instead of silently reconciling them.
- [ ] Link calendar → dated log → cumulative topics.
- [ ] Add quiet class-history links where useful.
- [ ] Do not commit raw notebook photographs under website assets.

## H. UI/architecture

- [ ] Reuse generic `subject-unit.js` / `unit-questions.js` / `class-log.js` architecture.
- [ ] Do not create subject-specific duplicate renderers without an approved architectural reason.
- [ ] Keep HTML pages as lightweight data-driven shells.
- [ ] Preserve left-nav independent scroll and active-topic navigation.
- [ ] Preserve Practice links below TOC.
- [ ] Preserve end-of-unit practice CTA.
- [ ] Keep Detailed sources quiet/collapsed.
- [ ] Verify desktop/tablet/mobile rendering.

## I. PYQs

- [ ] Keep PYQs subject-wide by default.
- [ ] Do not invent PYQ content/year/marks.
- [ ] Add unit/topic mappings only when confident.

## J. Verification

- [ ] Parse all changed JSON.
- [ ] Syntax-check changed JavaScript/Python.
- [ ] Run subject-specific verifier.
- [ ] Run `python3 scripts/tools/verify_college.py`.
- [ ] Resolve errors rather than suppressing checks.
- [ ] Confirm all ready-unit assets/links exist.
- [ ] Confirm student-facing prose contains no build/source commentary.

## K. Publish/handoff

- [ ] Change `publicationStatus` to `ready` only after verification.
- [ ] Generate a minimal delta.
- [ ] List every changed/added file.
- [ ] Provide unzip command.
- [ ] Provide `rsync -avhn` dry run.
- [ ] Provide real `rsync -avh` command.
- [ ] Provide `git status` command.
- [ ] Provide verifier command(s).

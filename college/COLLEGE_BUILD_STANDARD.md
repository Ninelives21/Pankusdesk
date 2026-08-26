# PankusDesk College Build Standard

**Status:** Normative project contract  
**Canonical reference implementation:** Semester 1.1 → Basic Electrical Engineering → Unit I  
**Reference workspace generation:** the current BEE Unit-I architecture represented by `redo(8)` when this standard was created.

This document defines the default build contract for every college unit, subject, and semester in PankusDesk. If a future implementation choice is ambiguous, follow the current BEE Unit-I reference implementation unless the user explicitly changes the standard.

## 1. Non-negotiable design principles

1. **Source-locked academics.** Core academic content must come from supplied sources or explicitly approved gap sources. Never fill a source gap silently from model memory.
2. **Official syllabus defines scope.** The current regulation/syllabus determines what belongs in the core course. Textbooks, lectures, class notes, and supplementary sources support that scope; they do not redefine it.
3. **One cumulative study version.** The unit page is a consolidated, de-duplicated theory notebook. Do not create parallel textbook notes, lecture notes, and class notes on the main unit page.
4. **Chronology is preserved separately.** Dated class logs preserve what happened on a specific day. They are not substitutes for the cumulative unit page.
5. **Provenance stays in the backend.** Student-facing theory should teach the subject, not narrate how the notes were built.
6. **Generic renderers first.** Shared scripts/styles serve all subjects and semesters. Extend generic data/schema support before creating subject-specific rendering code.
7. **No fake completeness.** Incomplete units remain `scaffold`. A unit becomes `ready` only after academic coverage, assets, links, and verification pass.
8. **Deterministic verification.** “Done” means both human QA and verifier PASS, not merely that the page looks complete.

## 2. The four-layer model

Keep these layers distinct:

1. **Source material** — syllabus, prescribed textbook, supplied lectures, class notes, supplementary material, approved gap sources.
2. **Archival/provenance record** — source IDs, page indexes, lecture indexes, class-log records, source manifests, coverage audits.
3. **Cumulative knowledge** — `kb/data/topics.json`, containing the best current study version.
4. **Student-facing pages** — generic renderers presenting clean theory, practice, class logs, and PYQs.

Do not leak archival language into theory prose.

## 3. Mandatory source workflow

Before writing a new unit:

1. Inspect the latest workspace and the target subject's `subject.json`.
2. Inventory every supplied source relevant to the unit.
3. Extract the official syllabus and atomise the unit into small syllabus requirements.
4. Map every syllabus atom to one or more source references.
5. Record a true missing requirement as `SOURCE_GAP`; do not guess.
6. Use outside material only after explicit approval, then record it as an approved gap source.
7. Preserve known source anomalies and missing lecture numbers exactly. Never invent sequence items to make numbering look complete.

### Source hierarchy

Use this default authority order:

1. Official current syllabus/regulation — defines required scope.
2. Prescribed textbook — primary theory/figure/chapter-question source.
3. Supplied lecture/class material — explanations, emphasis, methods, examples.
4. Supplied supplementary material — supporting material only; cannot redefine syllabus.
5. Explicitly approved gap source — fills a syllabus-required hole when needed.

## 4. Topic status rules

Allowed topic statuses:

- `core` — directly within the official syllabus.
- `supporting` — useful supplied material that helps the course but is not separately named by the official syllabus.
- `core-gap-filled` — official syllabus content filled from an explicitly approved source because the primary supplied corpus lacked it.

Do not promote useful extra material to official syllabus status.

## 5. Cumulative unit-note rules

The canonical rendered theory lives in `kb/data/topics.json`.

Each topic should contain, where relevant:

- stable topic ID
- unit number
- title
- status
- concise `intro`
- quick-recall `learn` points
- detailed `sections`
- formulas
- problem-solving method
- cautions
- prescribed-book practice links
- generated self-checks
- provenance (`source_refs`)
- optional class history

### Prose standard

The main unit page must read as **actual theory notes**.

Write directly:

- “A DC circuit carries direct current…”
- “Network elements may be classified…”
- “An ideal inductor…”

Do not write source/workflow commentary such as:

- “The class notes say…”
- “The 24 August class grouped…”
- “The textbook says…”
- “The prescribed textbook defines…”
- “The lecture explains…”
- “The source material gives…”
- “At the level needed here…”
- “R25 Unit I does not require…”
- “This page retains…”
- “We include…”

Scope and provenance belong in metadata, syllabus pages, or source sections—not in ordinary theory prose.

### De-duplication rule

If textbook, lecture, and class notes cover the same idea, write the concept once and attach all appropriate source references. Do not append repeated source-specific versions.

## 6. Section-level provenance

Every topic must have non-empty `source_refs`. Detailed sections should also have `source_refs` whenever practical.

A source reference must resolve through the subject's configured source collections or indexes. Never invent a reference ID.

`book_refs` may retain printed-page/capture bookkeeping internally. Internal capture filenames are not student-facing content.

## 7. Human-readable Markdown companion

Maintain `kb/notes/unit-N.md` as a readable companion where the subject workflow uses it.

The rendered JSON is canonical when the live page is data-driven. Never overwrite newer JSON merely because an older Markdown companion differs. When editing a unit, keep the Markdown synchronized where practical.

## 8. Generated self-checks vs official questions

Keep these distinct:

- `self_checks` in `topics.json` are generated study/revision prompts.
- `textbook-questions.json` stores official prescribed-textbook chapter-end questions.
- PYQs are a separate subject-wide layer.

Never present a generated self-check as an official textbook or university question.

## 9. Prescribed-textbook question workflow

Official chapter-end questions belong to the corresponding unit and are rendered through the generic unit-question renderer.

Rules:

1. Preserve supplied textbook question wording.
2. Use stable IDs such as `u1-sa-01` / `u1-es-01` or another consistent unit-scoped convention.
3. Practice links from theory should use stable question anchors.
4. PankusDesk-created answers must not be called official textbook solutions unless official solutions were actually supplied.
5. If the book supplies only a final answer, store it as a check, not as proof that the full derivation came from the book.
6. If a printed result conflicts with a source-backed derivation, flag the discrepancy explicitly.
7. If the source set cannot support the answer, retain the question with `status: source-gap` rather than filling it from model memory.

## 10. PYQ architecture

Use one subject-wide `pyqs.html` page unless the architecture is explicitly changed.

Do not invent PYQs, years, marks, or exam metadata. Unit/topic mappings should be added only when confident.

## 11. Daily class-log workflow

The permanent daily workflow is:

**raw intake → verbatim dated record → topic mapping → selective integration into cumulative notes**

### Dated record

Store a dated entry under:

`<subject>/kb/class-log/YYYY-MM-DD/entry.json`

and, where retained:

`<subject>/kb/class-log/YYYY-MM-DD/raw.md`

The dated record preserves notebook wording faithfully. It may normalize line wrapping/markup, but must not silently rewrite the student's/lecturer's meaning. If handwriting is unreadable, mark it as illegible rather than guessing.

### Calendar index

The semester calendar index lives under the semester data layer (currently `college/<semester>/data/class-log.json`). Calendar entries link to the generic class-log shell with a date query.

### Bidirectional linking

Calendar → dated class log → cumulative unit topic.

Where useful, cumulative topics may contain quiet `class_history` links back to dated class logs.

### Integration rule

For each daily class item:

- already covered adequately → do not duplicate
- useful new detail → integrate into the existing cumulative topic
- lecturer-specific emphasis → retain as structured class emphasis where appropriate
- assignment/example → route to the appropriate structured layer
- contradiction → preserve verbatim in class log and flag; do not silently replace the cumulative theory

### Raw notebook images

Original notebook photographs are **intake/archive material**, not normal website assets. Do not commit them under `assets/class/**/raw/`.

Retain only useful derived/redrawn class visuals in the site when needed.

## 12. Figure-selection policy

Do not bulk-copy every textbook figure.

Capture/redraw a figure only if it has a concrete role in:

- cumulative theory, or
- a worked example/question actually represented in the site.

Keep asset roles separate:

`assets/book/uN/theory/` — figures supporting cumulative theory  
`assets/book/uN/examples/` — figures required by textbook questions/examples

Class-derived figures remain under a separate class asset path.

## 13. Figure data and accessibility

A rendered theory figure should normally include:

- `src`
- descriptive `alt`
- caption
- printed page where applicable
- intrinsic `width` / `height` when known
- exact insertion anchor (`after` paragraph/bullet)

Alt text must describe the technical content. Never use meaningless alt text such as “image”, “figure”, or only the filename/figure number.

Internal capture filenames must not be shown in normal student-facing UI.

## 14. Notebook Redraw Style

All redraws must follow `college/NOTEBOOK_REDRAW_STYLE.md`.

Key non-negotiable rule: **all visible text in a redraw uses the same handwriting-style visual language.** Do not mix handwritten labels with textbook/serif/sans-serif print captions.

Scientific/source fidelity outranks aesthetics.

## 15. Shared renderer architecture

Current generic renderers include:

- `scripts/new/subject-unit.js`
- `scripts/new/unit-questions.js`
- `scripts/new/class-log.js`
- semester/calendar/shared navigation renderers

Current shared page styles include:

- `styles/new/pages/unit.css`
- `styles/new/pages/practice.css`
- `styles/new/pages/class-log.css`
- related semester/calendar/subject styles

Do not create `chemistry-unit.js`, `physics-unit.js`, etc. just because a new subject is easier to hard-code. Add a generic optional data field/renderer capability first.

If a genuinely new architecture is required, explain it before changing the shared contract.

## 16. Lightweight HTML shells

Unit, textbook-question, and class-log pages should remain lightweight shells that point to subject metadata and shared renderers.

Do not duplicate full note HTML per unit/date when the generic renderer can generate it from data.

## 17. Publication status

Allowed unit publication states:

- `ready`
- `scaffold`

A scaffold may expose the official syllabus boundary and a reserved destination, but must not fake completed theory.

Set a unit to `ready` only after:

- all required syllabus atoms are covered or explicitly resolved
- topic provenance exists
- required assets resolve
- practice links resolve
- student prose has been audited
- visual QA is complete
- verifier passes

## 18. Verification contract

Run both:

1. any subject-specific verifier (for source-corpus invariants), and
2. `scripts/tools/verify_college.py` (for cross-subject architectural invariants).

Do not weaken a verifier merely to make an error disappear. Fix the underlying data or explicitly change the standard.

## 19. Stop conditions

Stop and report rather than guessing when:

- official syllabus is unavailable/ambiguous
- prescribed-textbook page/figure is missing
- figure identity cannot be verified
- a lecture appears to be missing
- required syllabus content is unsupported
- authoritative supplied sources materially conflict
- numerical source results conflict
- question needs unsupplied material
- PYQ mapping is uncertain
- current workspace schema differs materially from this contract

## 20. Standard unit-build sequence

1. Read this standard and `REFERENCE_IMPLEMENTATION.md`.
2. Inspect latest workspace and target subject metadata.
3. Inventory sources.
4. Atomise official syllabus.
5. Audit source coverage and gaps.
6. Obtain approval for any required gap sources.
7. Build/update cumulative topics.
8. Consolidate lecture/class material without duplication.
9. Audit student-facing prose for theory-note style.
10. Build/verify prescribed-textbook questions.
11. Audit required figures.
12. Redraw figures using Notebook Redraw Style.
13. Add descriptive alt text and exact anchors.
14. Link theory practice to stable question anchors.
15. Add dated class-log integration when supplied.
16. Maintain subject-wide PYQ layer separately.
17. Run visual QA.
18. Run subject verifier.
19. Run generic college verifier.
20. Only then mark `publicationStatus: ready` and hand off a minimal delta.

## 21. Artifact handoff convention

Prefer a minimal delta rather than a whole workspace.

Always provide:

```bash
unzip <delta>.zip
rsync -avhn "<delta-folder>/" "Pankusdesk/"
rsync -avh "<delta-folder>/" "Pankusdesk/"
cd Pankusdesk
git status
```

When relevant, also provide the exact verifier command.

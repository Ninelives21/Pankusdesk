# PankusDesk College Build Standard — Design Lock v2

**Status:** Normative project contract  
**Design lock:** v2 · 28 Aug 2026  
**Canonical reference implementation:** Semester 1.1 → Basic Electrical Engineering → Unit I  
**Reference workspace:** the latest Unit-I-complete workspace supplied with this design-lock update.

This document defines the default build contract for every future college unit, subject and semester in PankusDesk/PadhaiSpace. If a future implementation choice is ambiguous, follow the finished BEE Unit I implementation and the files listed in `REFERENCE_IMPLEMENTATION.md` unless the user explicitly changes the standard.

---

## 1. Non-negotiable principles

1. **Official syllabus defines scope.** The current regulation/syllabus determines what is core. Textbooks, lectures, class notes and supplementary sources support that scope; they do not redefine it.
2. **The prescribed textbook is the primary notes source.** For a textbook-led unit, do not reduce the book to a thin summary. Preserve its sequence, terminology, definitions, equations, derivations, explanatory steps and useful worked-example calculation lines as closely as practical. Correct only grammar, punctuation, obvious typographical errors and clearly accidental formatting defects unless the user asks for a conceptual rewrite.
3. **Every example must be fully worked.** Every textbook example, class example, PankusDesk-added example and solved practice/PYQ example must appear in a dropdown and contain the complete reproducible working, not merely the question and final answer. Show every substantive row operation, algebraic transformation, substitution, iteration or calculation needed to reach the result. If a source omits intermediate working and PankusDesk supplies it, keep the completion faithful to the source result and label any genuinely source-external clarification when needed.
4. **The complete example question stays visible before opening the dropdown.** The example title and the full problem statement (including matrices, equations, given values and subparts) must be visible in the closed state. Opening the `+` reveals the solution only; the hidden portion must begin with the solution/working, never with information needed to know what is being solved.
5. **Multi-part questions and answers are visually separated.** Whenever a question, example, answer, solution, PYQ or self-check contains labelled subparts such as `(i)`, `(ii)`, `(iii)` or `(a)`, `(b)`, `(c)`, render each subpart on its own line rather than running the parts together inline. In a revealed solution, each subpart must also appear as a clearly separate solution block with its own part label and visual boundary; use the shared alternating panel treatment unless a subject requires a stronger semantic distinction. This is a global presentation rule across all subjects and practice layers.
6. **One cumulative study version.** The unit page is the best current, de-duplicated semester notebook. Do not create parallel “textbook notes”, “lecture notes” and “class notes” pages for the same theory.
7. **Class chronology is preserved separately.** A dated class log records what happened on a particular date. Useful material is then integrated at the correct conceptual point in the cumulative unit page.
8. **Class-note material must remain visibly identifiable.** Integrated class-note sections use the dedicated class-note visual treatment and date/source label, but their prose states the content directly; it must not narrate the note-building workflow.
9. **Explanations are separated from source notes.** PankusDesk-authored plain-language teaching material belongs in the blue explanation accordion (`Understand this diagram` / explanation dropdown), not mixed into textbook or class-note prose as though it came from the source.
10. **Provenance stays in data.** Student-facing theory teaches the subject. Source IDs, capture filenames, ingestion commentary and build decisions live in metadata/audits, not ordinary theory prose.
11. **Source discrepancies are never silently repaired.** Preserve the source-backed statement/result and flag the discrepancy explicitly. A clarification accordion may explain the standard relationship, but it must not rewrite the source unnoticed.
12. **Generic architecture first.** Shared renderers/styles serve all subjects and semesters. Extend the generic schema/renderer before creating subject-specific duplicate code.
13. **Figures are part of the teaching flow.** Every production figure is placed at the text it explains. No “all figures at the end” dump and no unanchored fallback in a ready unit.
14. **Technical redraw accuracy outranks appearance.** All NRS work follows `NOTEBOOK_REDRAW_STYLE.md`, including the mandatory semantic-verification gate.
15. **Mathematics is rendered, not improvised.** Use MathJax/LaTeX in student-facing data. Fractions use `\dfrac`, not `\frac`.
16. **No fake completeness.** Incomplete units remain `scaffold`. A unit becomes `ready` only after academic, visual, practice, class-log/link and verifier checks pass.
17. **Done means reproducibly verified.** Human QA + subject verifier + generic college verifier are required.
18. **Every fully solved problem ends with an explicit final answer.** After the complete working, show the final answer/result as a visually distinct bold line whenever the problem has a determinate result. Keep any printed-textbook answer check or provenance note separate from that final-answer line. This applies globally to textbook questions, worked examples, class examples, PYQs and other solved practice.
19. **Textbook problem sets stay in textbook position.** When an in-scope prescribed-textbook problem/exercise set appears immediately after a theory section, the cumulative unit page must reference/link that exact set at the same logical point in the teaching flow, in addition to the persistent Textbook Questions navigation link.
20. **Inline textbook-practice links must be visually prominent.** A prescribed-book problem-set reference embedded in the theory flow is a major study action, not a footnote. Render it as a large, high-contrast callout with a clearly readable heading and an obvious clickable practice row. Use the shared dark-primary practice-callout treatment across subjects so students can immediately distinguish “stop and practise this set” from surrounding theory and class-note content.

---

## 2. The five-layer model

Keep these concerns distinct:

1. **Source material** — official syllabus, prescribed textbook, supplied lectures, handwritten class notes, supplementary documents, approved gap sources.
2. **Archival/provenance record** — source manifests, page/lecture indexes, class-log source IDs, coverage audits, anomaly notes.
3. **Cumulative knowledge** — `kb/data/topics.json`, the canonical rendered study content.
4. **Chronological class record** — `kb/class-log/YYYY-MM-DD/entry.json` plus optional `raw.md`.
5. **Student-facing shells/renderers** — unit, questions, class-log, syllabus, calendar and PYQ pages rendered from shared code.

The layers may link to one another, but they must not collapse into one another.

---

## 3. Source authority and source lock

### 3.1 Default authority order

1. Official current syllabus/regulation — defines required scope.
2. Prescribed textbook — canonical core theory, figure and chapter-question source.
3. Supplied lecturer/class material — emphasis, explanation, notation, worked methods and class-specific additions.
4. Supplied supplementary material — supporting evidence only.
5. Explicitly approved gap source — used only to fill an unresolved syllabus requirement.

### 3.2 Mandatory intake workflow

Before writing or extending a unit:

1. Inspect the **latest workspace**, never reconstruct the design from an old chat delta.
2. Read the target `subject.json`, current schemas and this design lock.
3. Inventory all supplied sources relevant to the unit.
4. Atomise the official syllabus into small requirements.
5. Map every requirement to real source IDs.
6. Mark a genuine unsupported requirement as `SOURCE_GAP`.
7. Obtain explicit approval before using an outside source to fill a gap.
8. Preserve missing lecture numbers, source anomalies and inconsistent results exactly in provenance/audit records.

Never manufacture a source ID, page, lecture or exam record to make the corpus look complete.

---

## 4. Topic and publication status

### 4.1 Topic status

Allowed topic statuses:

- `core` — directly within the official syllabus.
- `supporting` — useful supplied material that supports the course but is not separately named by the official syllabus.
- `core-gap-filled` — required syllabus material filled from an explicitly approved source because the primary supplied corpus lacked it.

### 4.2 Unit publication status

Allowed unit publication states:

- `ready`
- `scaffold`

A scaffold may expose the syllabus boundary and a reserved destination, but must not imitate finished notes.

---

## 5. Canonical cumulative unit-note contract

The live theory is data-driven from:

`<subject>/kb/data/topics.json`

A topic should contain, where relevant:

- stable `id`
- `unit`
- `title`
- `status`
- concise `intro`
- `learn` quick-recall points
- detailed `sections`
- `formulas`
- `method`
- `cautions`
- prescribed-textbook `practice` anchors
- generated `self_checks`
- topic/section `source_refs`
- `book_refs`
- optional `class_history`

### 5.1 Textbook-as-notes rule

For prescribed-textbook theory:

- preserve the textbook's conceptual sequence;
- keep definitions and terminology recognisable;
- keep equations and derivations in the body where they occur;
- keep useful worked-example calculation lines in context;
- do not replace a detailed explanation with a terse model-generated summary;
- do not silently modernise unusual notation or “correct” a printed inconsistency.

PankusDesk additions such as Quick recall, Check yourself, explanation accordions, navigation, formula consolidation, method boxes and cautions are **additive study aids**, not substitutes for the primary notes.

### 5.2 Direct-prose rule

The main unit page must read like subject notes.

Write:

- “A voltage source maintains…”
- “The current in an inductor…”
- “A practical current source…”

Do not write workflow narration such as:

- “Priyanka’s notes say…”
- “The textbook says…”
- “The lecture explains…”
- “The supplied source shows…”
- “We retained…”
- “This page includes…”
- “R25 requires…”

The **class-note source label itself is allowed and intentional**; source-management prose inside the teaching paragraph is not.

### 5.3 De-duplication rule

If textbook, lecture and class notes overlap, teach the concept once in the best location and attach all appropriate provenance. An integrated class-note panel may remain when it represents lecturer-specific wording, notation, emphasis or a useful visual; it must not simply duplicate the surrounding textbook paragraph.

---

## 6. Mathematics and notation

1. Use MathJax-compatible delimiters: `\(...\)` and `\[...\]`.
2. **All authored fractions use `\dfrac`.** `\frac` is not allowed in ready-unit student-facing topic data.
3. Preserve source variable names and subscripts unless a user-approved correction is being made.
4. Do not let code-generation escapes corrupt LaTeX (`\rho`, `\varphi`, etc.). Check for control characters after programmatic edits.
5. If a source equation appears wrong, preserve/flag it rather than silently substituting a standard formula.

---

## 7. Section types and class-note integration

### 7.1 Ordinary section

An ordinary section is part of the cumulative textbook-led theory and normally has:

- `heading`
- `scope`
- `paragraphs` and/or `bullets`
- `source_refs`
- optional `book_refs`
- optional figures

### 7.2 Integrated class-note section

Use:

```json
{
  "kind": "class-note",
  "source_label": "Priyanka’s class notes · 27 Aug 2026"
}
```

The renderer gives this a visibly separate class-note treatment. Use it when class material adds real value at that point in the topic.

Rules:

- place it beside the concept it belongs to;
- keep the date/source label visible;
- write content directly, without “Priyanka’s notes…” narration;
- include the class source ID in `source_refs`;
- class-derived figures in cumulative topics use `kind: "class-note"`;
- do not dump a whole day's notes at the end of the unit.

### 7.3 Ambiguous handwriting

If a reading is uncertain, ask the user. A user-confirmed reading becomes the authoritative transcription for that class record and should be documented in `transcription_policy` / `source_notes` where useful.

---

## 8. Explanation accordions — the teaching layer

Use a blue explanation dropdown when source material is correct but too terse, symbol-heavy or easy to misunderstand.

Data lives at section level:

```json
{
  "accordions": [
    {
      "title": "Ideal and Practical Voltage",
      "paragraphs": ["..."],
      "bullets": ["..."]
    }
  ],
  "accordion_recap": ["..."]
}
```

The shared renderer presents these under **Understand this diagram**.

Rules:

1. Explanation prose is PankusDesk-authored and intentionally visually separate from the source notes.
2. Explain in plain language before introducing more abstraction.
3. Decode equations and symbols line by line when that is the actual stumbling block.
4. Keep the explanation concise enough for study use, but do not be so terse that it fails to explain the confusing step.
5. Use source-backed facts; do not invent new syllabus content.
6. If an explanation corrects or contrasts a questionable printed expression, make the distinction explicit rather than silently replacing the source.
7. Multiple related accordions may be used in one section; the UI behaves as an accordion, not an always-open essay.

Canonical Unit-I examples include:

- **How to read the energy-source classification**
- **Ideal and Practical Voltage**
- **Ideal and Practical Current**

---

## 9. Figure contract: content, placement and accessibility

### 9.1 Asset roles

Textbook theory figures:

`assets/book/uN/theory/`

Textbook question/example figures:

`assets/book/uN/examples/`

Class-derived redraws:

`assets/class/YYYY-MM-DD/figures/`

Raw notebook photographs remain source/intake material and are not normal website assets.

### 9.2 Every ready-unit figure must be explicitly placed

A ready-unit figure must have either:

- an `after` anchor, or
- a `grid` placement.

Do not rely on renderer fallback placement.

Supported anchor concepts are:

- `before-paragraph`
- `paragraph`
- `bullet`
- `end` only when the source genuinely places the figure after the whole section

### 9.3 CSS Grid placement

For textbook-like side-by-side placement, use `grid` metadata:

```json
{
  "grid": {
    "start": 4,
    "end": 6,
    "side": "right",
    "size": "small"
  }
}
```

Design Lock v2 layout rule:

- side-by-side textbook rows use **CSS Grid, not floats**;
- default desktop text/image split is **50/50** (`1fr 1fr`);
- `side` follows the source layout where meaningful;
- full-width figures remain full-width;
- mobile collapses to one column;
- image labels must remain readable at normal web size.

### 9.4 Source-placement audit

Before a unit is ready, compare each used textbook figure with the actual source page and place it beside the corresponding text. Unit I's figure-placement audit is the reference standard.

### 9.5 Figure metadata

A production figure normally carries:

- `src`
- descriptive `alt`
- caption
- printed `page` where applicable
- intrinsic `width` / `height`
- `size`
- placement metadata
- `kind: "class-note"` for class-derived cumulative figures

Alt text describes the electrical/scientific content, not merely the filename or figure number.

---

## 10. Notebook Redraw Style (NRS)

All redraws follow `college/NOTEBOOK_REDRAW_STYLE.md`.

Design Lock v2 adds a mandatory semantic gate:

**understand/confirm meaning-bearing details → draw → visually verify those same details**

For technical drawings, arrow direction, polarity, dot/cross convention, source orientation, graph axes, topology and spatial relationships are academic content. A beautiful redraw with one of these wrong is a failed redraw.

Never use a textbook/reference image to override the actual class-note source. Reference material may clarify standard symbol shape only after the source meaning is understood.

---

## 11. Dated class-log workflow

Permanent workflow:

**raw intake → faithful dated record → topic mapping → NRS derivation where useful → cumulative integration → calendar link**

### 11.1 Dated record

Store:

`<subject>/kb/class-log/YYYY-MM-DD/entry.json`

and, where retained:

`<subject>/kb/class-log/YYYY-MM-DD/raw.md`

`entry.json` preserves the page sequence using structured blocks such as headings, lines, paragraphs, bullets, equations and figures.

### 11.2 Calendar index

The semester index is:

`college/<semester>/data/class-log.json`

A dated class entry links to the generic subject shell:

`class-log.html?date=YYYY-MM-DD`

The calendar, dated log and cumulative topic must resolve bidirectionally where mappings exist.

### 11.3 Integration policy

For each class item:

- already covered adequately → do not duplicate;
- useful new detail → integrate into the existing topic;
- lecturer-specific notation/emphasis → keep in a class-note section;
- confusing sketch → redraw in NRS after semantic confirmation;
- two adjacent sketches that clearly form one concept may be combined in one class redraw when explicitly understood/approved;
- contradiction → preserve in class log and flag; do not silently reconcile;
- assignment/question → route to the appropriate practice layer.

### 11.4 Raw source handling

Do not commit raw notebook photographs under `assets/class/**/raw/`. Production assets are clean derived redraws only.

---

## 12. Human-readable Markdown companion

Where used, maintain:

`kb/notes/unit-N.md`

It is a readable companion, not the rendering authority. `topics.json` is canonical for the live unit page. Never overwrite newer JSON from an older Markdown copy.

---

## 13. Self-checks, textbook questions and PYQs

Keep three layers distinct:

- `self_checks` — generated revision prompts in `topics.json`;
- `textbook-questions.json` — official prescribed-textbook chapter-end questions, with PankusDesk study answers where source-backed;
- `pyqs.html` / PYQ data — previous university examination questions.

Never label a generated question as textbook/PYQ material.

### 13.1 Textbook question rules

1. Preserve official question wording.
2. Use stable unit-scoped IDs/anchors.
3. Link theory practice rows to exact anchors.
4. PankusDesk answers are not “official textbook solutions” unless official solutions were supplied.
5. A book final answer may be stored as a check, not falsely cited as the derivation source.
6. Preserve/flag printed discrepancies.
7. For any labelled multi-part question, store/render the subparts structurally so every part appears on its own line in the closed question view.
8. For any multi-part solution or answer, render each part as a clearly separate labelled panel rather than one uninterrupted stream of working.
9. End every fully worked solution with a clearly separated **bold final answer/result** whenever a determinate final result exists; keep `book_check` or other source metadata separate.
10. Reference each in-scope textbook problem/exercise set on the theory page at the same logical point where the book places it, linking to the exact question-group anchor.
11. If sources cannot support an answer, keep `status: "source-gap"` instead of filling from memory.

### 13.2 PYQ rules

Use a subject-wide PYQ layer by default. Never invent year, marks, wording or mappings.

---

## 14. Shared renderer architecture

Current generic college renderers include:

- `scripts/new/subject-unit.js`
- `scripts/new/unit-questions.js`
- `scripts/new/class-log.js`
- `scripts/new/calendar.js`
- shared semester/subject/navigation renderers

Unit I demonstrates that the generic unit renderer supports:

- lightweight HTML shells;
- topic navigation and active tracking;
- Quick recall;
- Check yourself accordions;
- textbook practice links;
- class-history links;
- integrated class-note panels;
- blue explanation accordions;
- MathJax;
- explicitly anchored figures;
- CSS-Grid text/figure rows;
- full-width figure rows;
- quiet provenance/reference footer.

Do not fork subject-specific renderers just to avoid extending generic data structures.

---

## 15. Lightweight shells

Unit, class-log and question HTML files remain small shells that declare the subject/unit context and load shared renderers/styles. Do not copy full theory HTML into every shell.

---

## 16. Source/reference resolution

Every topic and detailed section has non-empty `source_refs`. References must resolve through collections configured in `subject.json → unitRenderer.sources`.

`book_refs` may hold printed page/capture bookkeeping internally. Internal capture filenames are not normal student-facing content.

Class-note sections must include their corresponding `CLASS-...` source reference.

---

## 17. Verification contract

Run:

1. subject-specific verifier (source-corpus invariants), and
2. `python3 scripts/tools/verify_college.py` (cross-subject architecture).

Design Lock v2 generic verification covers, among other things:

- unit/topic status and shells;
- topic/section provenance;
- configured source-reference resolution;
- figure assets, alt text and explicit placement;
- figure Grid ranges;
- class-note labels/source references;
- explanation-accordion structure;
- textbook practice anchors;
- class-log mappings/assets/calendar links;
- absence of raw notebook binaries in website class assets;
- no `\frac` in ready-unit topic content;
- no student-facing source/build meta-commentary.

Do not weaken verification merely to make an error disappear. Fix data or explicitly change the design lock.

---

## 18. Stop conditions

Stop and report rather than guessing when:

- official syllabus is unavailable or ambiguous;
- prescribed textbook page/figure is missing;
- a figure's technical meaning cannot be verified;
- handwriting is ambiguous and materially changes meaning;
- a lecture/source sequence item appears missing;
- required syllabus content is unsupported;
- supplied authoritative sources materially conflict;
- a numerical result/equation conflicts with another authoritative source;
- a question needs unsupplied material;
- a PYQ mapping is uncertain;
- current data/schema materially differs from this contract.

---

## 19. Standard build sequence

1. Read this file, `REFERENCE_IMPLEMENTATION.md`, `NOTEBOOK_REDRAW_STYLE.md` and `UNIT_BUILD_CHECKLIST.md`.
2. Inspect the latest workspace and target subject metadata.
3. Inventory/lock sources.
4. Atomise syllabus and audit source coverage.
5. Resolve/approve gaps.
6. Build textbook-faithful cumulative topics.
7. Integrate supplied lecture/class material without duplication.
8. Add NRS visuals only after semantic verification.
9. Place every figure at the corresponding text using explicit anchor/Grid metadata.
10. Add explanation accordions where a source is too terse to learn from easily.
11. Build/verify prescribed textbook questions.
12. Maintain dated class logs and calendar links.
13. Audit student-facing prose and all LaTeX (`\dfrac`).
14. Synchronize `unit-N.md` where applicable.
15. Run visual QA.
16. Run subject verifier.
17. Run generic college verifier.
18. Mark `publicationStatus: ready` only after the unit satisfies the completion checklist.

---

## 20. Design-lock maintenance

The following files form one contract and must be updated together when architecture changes:

```text
college/
├── COLLEGE_BUILD_STANDARD.md
├── REFERENCE_IMPLEMENTATION.md
├── NOTEBOOK_REDRAW_STYLE.md
├── UNIT_BUILD_CHECKLIST.md
└── schemas/
    ├── subject.schema.json
    ├── topics.schema.json
    ├── textbook-questions.schema.json
    └── class-log.schema.json

scripts/
└── tools/
    └── verify_college.py
```

Do not update only the prose spec while leaving schemas/verifier behind.

---

## 21. Handoff convention

Prefer a minimal delta ZIP with **one top-level folder** so extraction is predictable.

Always provide dry-run before real sync. Do not use `--delete` for a delta.

Typical handoff:

```bash
cd ~/Downloads
unzip -q "<delta>.zip"
rsync -avhn "<delta>/" "/actual/path/to/Pankusdesk/"
rsync -avh  "<delta>/" "/actual/path/to/Pankusdesk/"
cd "/actual/path/to/Pankusdesk"
git status
python3 scripts/tools/verify_college.py
```

If the destination path is not known, do not invent it.

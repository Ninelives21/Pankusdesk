# PankusDesk College Build Standard — Design Lock v2

**Status:** Normative project contract  
**Design lock:** v2 · amended 2 Sep 2026 for the three-page unit split  
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
6. **Each unit has three study pages.** Use a textbook-led **Text** page, a **Textbook Questions** page, and a chronological **Class Notes** page. Do not mix class-note prose into the textbook-led Text page.
7. **Class chronology is preserved on the unit Class Notes page.** Dated entries remain separate and are reached directly from the calendar by date anchor.
8. **Class-note material stays in the class-note layer.** Its grammar may be cleaned for readability, but its equations, examples, diagrams, notation and teacher emphasis remain source-faithful and are not silently rewritten into textbook theory.
9. **Explanations are separated from source notes.** PankusDesk-authored plain-language teaching material belongs in the blue explanation accordion (`Understand this diagram` / explanation dropdown), not mixed into textbook or class-note prose as though it came from the source.
10. **Provenance stays in data.** Student-facing theory teaches the subject. Source IDs, capture filenames, ingestion commentary and build decisions live in metadata/audits, not ordinary theory prose.
11. **Source discrepancies are never silently repaired.** Awkward grammar and wording may be cleaned for readability, but source content that affects meaning—numbers, signs, equations, matrices, conditions, figure values, labels, topology, or a disagreement between a question and its printed solution—must be checked against the source. If a source/textbook discrepancy is independently verified, PankusDesk must explicitly state what the source prints and what conflicts. A verified **source/textbook discrepancy** uses one shared project-wide amber/gold semantic treatment across every subject and semester: highlight the question/example number or heading in the established MAC golden style (and the affected subpart label when applicable) and show the entire discrepancy explanation inside the matching amber/gold note treatment. Where a mathematically corrected result is presented, explain why the correction is justified; where textbook fidelity requires retaining the printed solution, say which source version that solution follows. Amber/gold is reserved for verified content discrepancies that affect meaning; never use it for grammar, spelling, punctuation, wording clean-up or ordinary editorial notes.
12. **Generic architecture first.** Shared renderers/styles serve all subjects and semesters. Extend the generic schema/renderer before creating subject-specific duplicate code.
13. **Figures are part of the teaching flow.** Every production figure is placed at the text it explains. No “all figures at the end” dump and no unanchored fallback in a ready unit.
14. **Technical redraw accuracy outranks appearance.** All NRS work follows `NOTEBOOK_REDRAW_STYLE.md`, including the mandatory semantic-verification gate.
15. **Mathematics is rendered, not improvised.** Use MathJax/LaTeX in student-facing data. Fractions use `\dfrac`, not `\frac`.
16. **No fake completeness.** Incomplete units remain `scaffold`. A unit becomes `ready` only after academic, visual, practice, class-log/link and verifier checks pass.
17. **Done means reproducibly verified.** Human QA + subject verifier + generic college verifier are required.
18. **Every fully solved problem ends with an explicit final answer.** After the complete working, show the final answer/result as a visually distinct bold line whenever the problem has a determinate result. Keep any printed-textbook answer check or provenance note separate from that final-answer line. This applies globally to textbook questions, worked examples, class examples, PYQs and other solved practice.
19. **Textbook problem sets stay in textbook position.** When an in-scope prescribed-textbook problem/exercise set appears immediately after a theory section, the cumulative unit page must reference/link that exact set at the same logical point in the teaching flow, in addition to the persistent Textbook Questions navigation link.
20. **Inline textbook-practice links must be visually prominent.** A prescribed-book problem-set reference embedded in the theory flow is a major study action, not a footnote. Render it as a large, high-contrast callout with a clearly readable heading and an obvious clickable practice row. Use the shared dark-primary practice-callout treatment across subjects so students can immediately distinguish “stop and practise this set” from surrounding theory and class-note content.
21. **No unnecessary nested scrollbars in study content.** Ordinary theory, class-note prose, equations, examples and explanation panels must expand naturally with the page and must not create their own vertical scroll regions. A local vertical scrollbar is permitted only for a deliberately bounded navigation/modal panel that genuinely needs independent scrolling. Wide mathematics/tables may use horizontal overflow on narrow screens, but the companion vertical axis must be hidden so MathJax or line-height rounding cannot produce stray vertical scrollbars.

---

## 2. The five-layer model

Keep these concerns distinct:

1. **Source material** — official syllabus, prescribed textbook, supplied lectures, handwritten class notes, supplementary documents, approved gap sources.
2. **Archival/provenance record** — source manifests, page/lecture indexes, class-log source IDs, coverage audits, anomaly notes.
3. **Textbook-led cumulative knowledge** — `kb/data/topics.json`, the canonical rendered Text page; class-note material is not mixed into this layer.
4. **Chronological class record** — `kb/class-log/YYYY-MM-DD/entry.json` plus optional `raw.md`, rendered together on the unit Class Notes page.
5. **Student-facing shells/renderers** — unit Text, Textbook Questions, Unit Class Notes, syllabus, calendar and PYQ pages rendered from shared code.

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

If textbook, lecture and class notes overlap, keep the Text page textbook-led and keep the class lesson on the dated Class Notes page. Do not reconcile overlap by merging source voices into one paragraph.

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
- optional semantic `tables` when a source-backed comparison or correspondence is clearer in rows and columns
- `source_refs`
- optional `book_refs`
- optional figures


Use `tables` for genuine comparisons/correspondences, not to fake page layout. Keep the source terminology and sequence intact; do not invent new categories merely to make a table look fuller.

### 7.2 Dedicated Unit Class Notes page

The student-facing class record is rendered chronologically from `kb/class-log/YYYY-MM-DD/entry.json` on:

`unit-N-class-notes.html#YYYY-MM-DD`

Rules:

- keep dates in chronological order with a date-based left navigation;
- keep a very brief description beside each date in the nav;
- lightly correct grammar, punctuation and awkward English without changing technical meaning;
- place NRS redraws with the dated material they explain;
- if a later date adds side notes onto an earlier notebook page, record the new additions without reproducing the earlier lesson in full;
- keep class-note source IDs in the dated entry/source manifest, not in textbook theory topics.

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

**raw intake → faithful dated record → light grammar cleanup → NRS derivation where useful → dedicated Unit Class Notes page → calendar link**

### 11.1 Dated record

Store:

`<subject>/kb/class-log/YYYY-MM-DD/entry.json`

and, where retained:

`<subject>/kb/class-log/YYYY-MM-DD/raw.md`

`entry.json` preserves the page sequence using structured blocks such as headings, lines, paragraphs, bullets, equations and figures.

### 11.2 Calendar index

The semester index is:

`college/<semester>/data/class-log.json`

A dated class entry links to its anchor on the unit Class Notes page:

`unit-N-class-notes.html#YYYY-MM-DD`

The calendar, dated entry and Unit Class Notes page must resolve consistently. Legacy `class-log.html?date=` shells may remain for backward compatibility, but new calendar links use the unit page.

### 11.3 Integration policy

For each class item:

- keep the dated lesson on the dedicated Unit Class Notes page, even when it overlaps the textbook;
- do not inject class-note prose or figures into the Text page;
- if a later date repeats an older notebook page with only side-note additions, record only the new dated additions instead of duplicating the older lesson;
- lightly fix grammar and awkward English without changing equations, examples or technical meaning;
- confusing sketch → redraw in NRS after semantic confirmation;
- two adjacent sketches that clearly form one concept may be combined in one class redraw when explicitly understood/approved;
- contradiction → preserve it in the class-note/source layer; do not silently rewrite the textbook layer;
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

1. Preserve the mathematical content and intent of the official question, but lightly clean awkward grammar, punctuation and wording when that improves readability without changing the mathematics.
2. When the source/textbook contains a verified content discrepancy, store it structurally (for example `math_mismatch` or `discrepancy`) rather than burying it in ordinary notes. Use the same shared project-wide MAC golden treatment everywhere: render the question/example number or heading in solid amber/gold; for multipart questions also highlight only the affected part label(s); render the entire discrepancy explanation in the matching amber/gold note box. This applies to mathematical mismatches and other source inconsistencies that change meaning, such as a figure value changing between a question and its solution. Do not apply this state to language/editorial clean-up.
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
- `scripts/new/class-log.js` (legacy/direct dated shell)
- `scripts/new/unit-class-notes.js`
- `scripts/new/unit-resource-nav.js`
- `scripts/new/calendar.js`
- shared semester/subject/navigation renderers

Unit I demonstrates that the generic unit renderer supports:

- lightweight HTML shells;
- topic navigation and active tracking;
- Quick recall;
- Check yourself accordions;
- textbook practice links;
- unit-level Text / Questions / Class Notes navigation;
- chronological dated class-note rendering;
- blue explanation accordions;
- MathJax;
- explicitly anchored figures;
- CSS-Grid text/figure rows;
- full-width figure rows;
- quiet provenance/reference footer.

Do not fork subject-specific renderers just to avoid extending generic data structures.

---

## 15. Lightweight shells

Unit Text, Textbook Questions and Unit Class Notes HTML files remain small shells that declare the subject/unit context and load shared renderers/styles. Legacy single-date class-log shells may remain for backward compatibility.

---

## 16. Source/reference resolution

Every topic and detailed section has non-empty `source_refs`. References must resolve through collections configured in `subject.json → unitRenderer.sources`.

`book_refs` may hold printed page/capture bookkeeping internally. Internal capture filenames are not normal student-facing content.

Class-note source IDs resolve through the dated class-log/source-manifest layer; ready-unit Text topics should not contain `kind: "class-note"` sections.

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
- configured Unit Class Notes shells and dated class-log/source references;
- explanation-accordion structure;
- textbook practice anchors;
- dated class-note assets, Unit Class Notes anchors and calendar links;
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
7. Keep supplied class material in dated Unit Class Notes entries; keep textbook theory source-clean.
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

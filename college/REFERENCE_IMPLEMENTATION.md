# College Reference Implementation — Design Lock v2

**Canonical implementation:** Semester 1.1 → Basic Electrical Engineering → Unit I  
**State:** Unit I refactored to Text · Questions · Class Notes on 2 Sep 2026

This file is the worked architectural reference for future units. Copy the **pattern**, not BEE-specific content or counts.

---

## 1. Why Unit I is canonical

Unit I now demonstrates the complete intended workflow:

**official syllabus → prescribed textbook-led Text page → exact figure placement → Textbook Questions → dated Unit Class Notes → NRS redraws → calendar anchors → verification**

It includes four dated class records (24 Aug, 27 Aug, 31 Aug and 1 Sep), NRS redraws where needed, a separate chronological Unit I Class Notes page, source-backed textbook questions, CSS-Grid figure placement, semantic study tables, and the plain-language explanation layer.

---

## 2. Primary reference files

### Subject contract

`college/1-1/basic-electrical-engineering/subject.json`

Demonstrates:

- subject identity/regulation/semester;
- `ready` vs `scaffold` units;
- paths to topics, syllabus and coverage;
- configurable source collections under `unitRenderer.sources`;
- prescribed-textbook question configuration;
- subject-wide PYQ configuration.

### Canonical cumulative theory

`college/1-1/basic-electrical-engineering/kb/data/topics.json`

This is the live rendering authority.

Unit I demonstrates:

- stable topic IDs;
- `core`, `supporting`, `core-gap-filled`;
- textbook-led detailed prose rather than thin summaries;
- equations/derivations in situ;
- `learn`, formulas, methods, cautions and self-checks;
- topic + section provenance;
- physical-book references;
- stable practice anchors;
- no embedded class-note sections in the Text data;
- unit-level Text / Questions / Class Notes navigation;
- explanation accordions;
- explicit figure placement using `after` or `grid` metadata.

### Human-readable companion

`college/1-1/basic-electrical-engineering/kb/notes/unit-1.md`

Keep it synchronized where practical, but do not treat it as more authoritative than the current JSON.

---

## 3. Unit page renderer reference

`college/1-1/basic-electrical-engineering/unit-1.html`  
`scripts/new/subject-unit.js`

The generic unit renderer demonstrates:

- lightweight page shell;
- syllabus boundary/context;
- independent topic navigation and active-topic tracking;
- Quick recall;
- Check yourself accordions;
- detailed theory sections;
- textbook-led detailed sections only; dated class material is rendered by the separate Unit Class Notes renderer;
- section explanation accordions via `accordions`;
- optional `accordion_recap`;
- semantic comparison tables via section-level `tables`;
- MathJax rendering;
- textbook/class figure captions and descriptive alt text;
- full-width figure rows;
- side-by-side text/figure Grid rows;
- prescribed-textbook practice links;
- class-history links;
- end-of-unit practice CTA;
- quiet source/provenance footer.

### Important renderer data shapes

#### Unit Class Notes configuration

```json
{
  "classNotes": {
    "hrefPattern": "unit-{unit}-class-notes.html",
    "availableUnits": [1],
    "sourceManifest": "kb/data/source-manifest.json",
    "collection": "class_sources"
  }
}
```

The unit class-notes renderer loads dated entries from the configured class-source collection and builds a date-based left navigation.

#### Explanation accordion

```json
{
  "accordions": [
    {
      "title": "Ideal and Practical Voltage",
      "paragraphs": ["..."],
      "bullets": ["..."]
    }
  ]
}
```

The renderer places these in the visually separate **Understand this diagram** teaching box.

#### Semantic comparison table

Use a section-level table when the source itself presents corresponding quantities or a compact comparison is clearer than prose. The Unit I electrical–magnetic–mechanical analogy is the reference pattern.

```json
{
  "tables": [
    {
      "headers": ["Electrical system", "Magnetic system", "Mechanical system"],
      "rows": [
        ["EMF", "MMF", "Torque"],
        ["Current", "Flux", "Speed"],
        ["Resistance", "Reluctance", "Friction"]
      ]
    }
  ]
}
```

The renderer emits a real HTML table with column headers and responsive horizontal scrolling on narrow screens. Do not use tables as a substitute for CSS layout.

#### Side-by-side figure Grid

```json
{
  "src": "college/1-1/basic-electrical-engineering/assets/book/u1/theory/f1-6.png",
  "alt": "...",
  "grid": {
    "start": 4,
    "end": 6,
    "side": "right",
    "size": "small"
  }
}
```

Design Lock v2 uses CSS Grid with a 50/50 desktop text/image split for side-by-side rows and one-column mobile collapse.

---

## 4. Textbook-as-notes reference

Audit/reference files:

`college/1-1/basic-electrical-engineering/kb/audits/unit-1-v5-source-policy.md`  
`college/1-1/basic-electrical-engineering/kb/audits/unit-1-v5-verification.md`

The Unit-I core is intentionally textbook-faithful:

- textbook sequence retained;
- explanatory prose retained rather than aggressively summarized;
- equations and derivations rendered where they occur;
- useful worked-example calculation lines retained;
- source anomalies preserved/flagged;
- PankusDesk aids remain additive.

This is the model for future prescribed-textbook-led units.

---

## 5. Figure placement reference

Audits:

`college/1-1/basic-electrical-engineering/kb/audits/unit-1-v5.4-grid-figure-audit.md`  
`college/1-1/basic-electrical-engineering/kb/audits/unit-1-v5.5-grid-50-50.md`

Unit I establishes these rules:

1. Every used figure is explicitly positioned.
2. No ready-unit figure relies on an unanchored fallback.
3. Source pages are visually checked before placement.
4. A figure that belongs beside several paragraphs uses a `grid.start`–`grid.end` range.
5. Side-by-side layout uses CSS Grid, not floats.
6. Desktop side-by-side rows are 50/50 text/image.
7. Full-width source figures remain full-width.
8. Mobile collapses to one column.
9. Technical labels must remain readable.

Theory figures:

`assets/book/u1/theory/`

Question/example figures:

`assets/book/u1/examples/`

Class-derived figures:

`assets/class/YYYY-MM-DD/figures/`

---

## 6. Class-notes page reference

### 24 Aug 2026

`kb/class-log/2026-08-24/entry.json`  
`kb/class-log/2026-08-24/raw.md`

Demonstrates a dated class record preserved on the Unit I Class Notes page without being embedded into textbook theory.

### 27 Aug 2026

`kb/class-log/2026-08-27/entry.json`  
`kb/class-log/2026-08-27/raw.md`  
`kb/audits/unit-1-2026-08-27-class-integration.md`

Demonstrates the mature class workflow:

- 3 notebook pages preserved in order;
- user-confirmed ambiguous readings recorded;
- 7 NRS redraws produced and integrated;
- two adjacent ideal-voltage sketches combined into one approved conceptual redraw;
- class figures placed in `assets/class/2026-08-27/figures/`;
- the dated lesson remains on the Unit I Class Notes page; textbook theory remains source-clean;
- malformed image-generation text is not allowed onto the site; correct mathematics is rendered separately in MathJax when necessary;
- class-note wording may be lightly cleaned for study without changing the source meaning.

Canonical explanation titles currently include:

- **How to read the energy-source classification**
- **Ideal and Practical Voltage**
- **Ideal and Practical Current**

These demonstrate the rule that explanation prose is separate from source notes.

### 31 Aug 2026

`kb/class-log/2026-08-31/entry.json`  
`kb/class-log/2026-08-31/raw.md`  
`kb/audits/unit-1-2026-08-31-class-integration.md`

Demonstrates later-semester consolidation after the basic Unit I page is already mature:

- one class date maps into more than one cumulative topic (`u1-sources` and `u1-rlc`);
- dependent-source notation is integrated beside the existing textbook dependent-source section, not appended as a duplicate lecture block;
- a semantic study table defines every equation term and maps two notation systems used on the same page;
- the blue **Understanding the four dependent sources** accordion adds intuition without rewriting source prose;
- resistance, inductance and capacitance class material is split and placed beside the corresponding R/L/C textbook sections;
- the previously planned **In simple words — what these equations mean** inductance accordion is used as a teaching bridge;
- no duplicate class redraw is created where the existing prescribed-textbook figures already carry the needed technical symbols;
- source-form differences are recorded in the backend audit instead of being silently reconciled in source prose.

---

### 1 Sep 2026

`kb/class-log/2026-09-01/entry.json`  
`kb/class-log/2026-09-01/raw.md`

Demonstrates the new chronological class-notes model: an updated network-element tree, R/L/C energy additions, and the nodes/branches/closed-loops example. Repeated 31 August base text is not duplicated; only the genuinely new 1 September additions are recorded.

---

## 7. Calendar/class-log reference

Semester calendar index:

`college/1-1/data/class-log.json`

Generic calendar renderer:

`scripts/new/calendar.js`

Unit I class-notes shell/renderer:

`college/1-1/basic-electrical-engineering/unit-1-class-notes.html`  
`scripts/new/unit-class-notes.js`

The reference link chain is:

**calendar date → Unit I Class Notes date anchor → dated `entry.json`**

The Text page is textbook-led and does not embed Priyanka's class-note sections. The 24 Aug, 27 Aug, 31 Aug and 1 Sep BEE entries are the working examples.

---

## 8. NRS reference

`college/NOTEBOOK_REDRAW_STYLE.md`

NRS v1.1 under Design Lock v2 adds the mandatory technical safeguard:

**semantic audit → user confirmation when required → generation → visual semantic audit**

Figure 1.8 / current-source work established why this is mandatory: arrow direction, polarity, dot/cross convention, graph axes and connectivity can change academic meaning even when the image looks polished.

---

## 9. Prescribed-textbook questions

`college/1-1/basic-electrical-engineering/kb/data/textbook-questions.json`  
`college/1-1/basic-electrical-engineering/unit-1-questions.html`  
`scripts/new/unit-questions.js`

Demonstrates:

- official chapter-end wording;
- stable IDs/anchors;
- source-backed PankusDesk study answers;
- source-gap status instead of invented answers;
- steps, equations, tables, result, notes and book checks;
- answer figures with descriptive alt text;
- theory → exact question-anchor links.

Generated `self_checks` remain a different layer.

---

## 10. Provenance/source-accounting reference

`kb/data/source-manifest.json`  
`kb/data/book-index.json`  
`kb/data/lecture-index.json`  
`kb/data/supplementary-pdf-index.json`  
`kb/data/coverage-audit.json`  
`kb/tools/verify_kb.py`

`subject.json → unitRenderer.sources` is the generic resolver contract. All topic/section source references must resolve through these configured collections.

---

## 11. Mathematics reference

Unit I establishes:

- MathJax/LaTeX in body content;
- `\dfrac` for fractions;
- source notation preserved unless explicitly corrected;
- no Python/control-character corruption of symbols such as `\rho`;
- equations rendered as text data rather than baked into UI markup when possible.

---

## 12. What to copy

Copy:

- the architecture;
- source-lock workflow;
- textbook-as-notes treatment;
- topic/section provenance;
- class-note integration pattern;
- explanation-accordion layer;
- figure asset roles;
- explicit Grid/anchor placement;
- NRS semantic gate;
- dated class-log/calendar chain;
- question/PYQ separation;
- `\dfrac`/MathJax discipline;
- verification-before-ready workflow.

---

## 13. What not to copy as universal facts

Do not hard-code into another subject:

- BEE source IDs (`TB-P...`, `CLASS-U1...`, etc.);
- BEE topic counts;
- BEE figure numbers;
- BEE gap sources;
- BEE textbook-question grouping;
- BEE lecture/capture counts;
- dates 24/27/31 Aug;
- number of class redraws;
- exact explanation titles.

Those are examples, not schema constants.

---

## 14. Decision rule

When uncertain:

1. Read `COLLEGE_BUILD_STANDARD.md`.
2. Inspect the finished Unit-I data/rendering in the **latest workspace**.
3. Read the relevant schema.
4. Extend generic data/renderer capability only when the new subject genuinely needs it.
5. Update the design-lock documents + schemas + generic verifier together if the architecture changes.
6. Never reconstruct a design decision from stale chat memory when the workspace can answer it.

## Shared study UI reference

The canonical common presentation layer is:

```text
scripts/new/study-ui.js
styles/new/study-ui.css
```

All college subjects and semesters consume this layer for accordions, example question/solution structure, MathJax/LaTeX handling, study-tip boxes and baseline figures. Subject renderers are data/layout adapters only; they must not fork these common behaviours.

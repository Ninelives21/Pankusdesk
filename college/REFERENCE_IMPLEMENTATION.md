# College Reference Implementation

## Canonical reference

The canonical implementation pattern is:

**Semester 1.1 → Basic Electrical Engineering → Unit I**

When a future unit/subject design decision is ambiguous, inspect these current files before inventing a new structure.

## Primary reference files

### Subject metadata

`college/1-1/basic-electrical-engineering/subject.json`

Demonstrates:

- subject identity and regulation
- unit metadata
- `ready` vs `scaffold`
- paths to topics/syllabus/coverage
- configurable provenance/source collections
- unit-question configuration
- subject-wide PYQ configuration

### Cumulative theory data

`college/1-1/basic-electrical-engineering/kb/data/topics.json`

Demonstrates:

- stable topic IDs
- `core`, `supporting`, `core-gap-filled`
- quick recall (`learn`)
- coherent theory sections
- section-level provenance
- formulas/methods/cautions
- exact figure insertion anchors
- descriptive alt text/captions
- prescribed-book practice anchors
- generated self-checks
- quiet class-history links

### Human-readable notes

`college/1-1/basic-electrical-engineering/kb/notes/unit-1.md`

Companion to the rendered JSON. The data-driven JSON remains canonical for the live unit page.

### Unit shell + renderer

`college/1-1/basic-electrical-engineering/unit-1.html`  
`scripts/new/subject-unit.js`  
`styles/new/pages/unit.css`

Demonstrates the shared data-driven unit-page architecture:

- lightweight HTML shell
- official syllabus boundary
- sticky/independently scrollable topic navigation
- active-topic tracking
- practice links beneath TOC
- end-of-unit practice CTA
- quick recall
- self-check accordions
- detailed theory
- anchored figures
- quiet detailed sources

### Prescribed-textbook questions

`college/1-1/basic-electrical-engineering/kb/data/textbook-questions.json`  
`college/1-1/basic-electrical-engineering/unit-1-questions.html`  
`scripts/new/unit-questions.js`  
`styles/new/pages/practice.css`

Demonstrates:

- official chapter-end question grouping
- stable question IDs/anchors
- source-backed PankusDesk answers
- source-gap questions without invented answers
- tables/equations/steps/results/notes/book checks
- question/example figures
- direct links from unit theory practice rows

### Class-log system

`college/1-1/basic-electrical-engineering/class-log.html`  
`college/1-1/basic-electrical-engineering/kb/class-log/2026-08-24/entry.json`  
`college/1-1/basic-electrical-engineering/kb/class-log/2026-08-24/raw.md`  
`college/1-1/data/class-log.json`  
`scripts/new/class-log.js`  
`styles/new/pages/class-log.css`

Demonstrates:

- calendar → dated class page
- verbatim chronological record
- mapped cumulative topics
- derived class figures
- return links to cumulative unit notes/calendar
- separation of chronology from polished theory

### Provenance and verification

`college/1-1/basic-electrical-engineering/kb/data/source-manifest.json`  
`college/1-1/basic-electrical-engineering/kb/data/book-index.json`  
`college/1-1/basic-electrical-engineering/kb/data/lecture-index.json`  
`college/1-1/basic-electrical-engineering/kb/data/coverage-audit.json`  
`college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`

Demonstrates the source-accounting layer and subject-specific invariants.

## Asset reference pattern

Theory figures:

`college/1-1/basic-electrical-engineering/assets/book/u1/theory/`

Question/example figures:

`college/1-1/basic-electrical-engineering/assets/book/u1/examples/`

Future units should normally use the same `uN/theory` and `uN/examples` role separation.

## What to copy as a pattern

Copy the **architecture**, not BEE-specific content:

- shared renderers
- data-driven shells
- unit publication status
- topic/provenance structure
- class-log separation
- question/PYQ separation
- figure-role folders
- alt-text discipline
- stable practice anchors
- source-gap discipline
- verification-before-ready workflow

## What NOT to copy as universal requirements

Do not hard-code these BEE-specific facts into another subject:

- number of units
- number of topics
- BEE source IDs (`TB-P...`, `LEC-U...`, etc.)
- BEE textbook capture/transcript counts
- BEE gap-topic IDs
- BEE chapter question grouping
- BEE figure numbering
- BEE syllabus atom counts

Each subject derives those values from its own actual sources.

## Non-canonical working artifacts

A working/optimization copy such as:

`assets/book/u1/theory/optimized/`  
`assets/book/u1/theory/optimized.zip`

is **not** part of the intended architecture. Treat such folders/files as temporary asset-processing artifacts unless the user explicitly adopts them as production structure.

## Decision rule for future work

When uncertain:

1. Read `college/COLLEGE_BUILD_STANDARD.md`.
2. Inspect these reference files in the latest workspace.
3. Extend the generic schema/renderer only when necessary.
4. Do not reconstruct design decisions from chat memory alone.

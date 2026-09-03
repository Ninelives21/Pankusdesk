# Matrices and Calculus KB

Course: **25BS1MT101 · Matrices and Calculus · R25 · Semester 1.1**

This subject follows the college Design Lock v2 architecture.

## Current state

- **Unit I — Matrices:** source-backed and `ready`
- **Unit II — Eigenvalues, Eigenvectors and Quadratic Forms:** source-backed and `ready`
- **Units III–V:** remain explicit `scaffold` / source-gap units
- **Unit I textbook practice:** R25-filtered Grewal questions with printed Appendix 3 answer checks where available
- **Unit I class notes:** five dated notebook sets live on a dedicated `unit-1-class-notes.html` page; they are no longer mixed into textbook theory

## Unit I three-page study structure

1. `unit-1.html` — prescribed Grewal text/theory and textbook worked examples
2. `unit-1-questions.html` — textbook questions and PankusDesk solutions
3. `unit-1-class-notes.html` — Priyanka's chronological class notes with a date/topic left navigation

## Unit I source map

- Grewal pp. **37–44** — rank, elementary transformations, Gauss–Jordan inverse, normal form
- Grewal pp. **47–58** — matrix solution of systems, consistency, homogeneous and non-homogeneous systems
- Grewal pp. **1066–1068** — Gauss–Seidel
- Practice pages: **44, 49, 57–58, 85–88, 1072**
- Printed answer checks: **1380–1383, 1440**

Nearby material that is not part of R25 Unit I is deliberately not promoted into the notes/practice bank (for example partition-method inverse, Cramer-only exercises, Unit-II eigenvalue/quadratic-form questions, Jacobi-only questions, and relaxation methods).

## Class-note source map

- **25 Aug 2026** — rank and normal/canonical form; two normal-form examples
- **28 Aug 2026** — Gauss–Jordan procedure; three inverse examples
- **29 Aug 2026** — systems, consistency, homogeneous and non-homogeneous equations
- **1 Sep 2026** — Gauss-elimination / row-rank method; consistency and parameter examples
- **2 Sep 2026** — further row-rank examples, including homogeneous and four-variable systems

Class notes remain date-faithful. Where a notebook calculation contains a visible slip or stops before a result, the dedicated class-notes page labels an independent verification rather than silently rewriting the class record.

## Primary files

- `data/syllabus.json` — official R25 unit scope
- `data/topics.json` — stable topic IDs and textbook/source-backed unit theory
- `data/textbook-questions.json` — R25-filtered Grewal practice bank
- `data/book-index.json` — physical-book page provenance
- `data/coverage-audit.json` — current coverage/source-gap audit
- `data/source-manifest.json` — provenance/source lock
- `data/kb-status.json` — current status counts
- `class-log/YYYY-MM-DD/entry.json` — dated class-note records rendered by the dedicated class-notes page
- `notes/unit-N.md` — human-readable unit companions
- `tools/verify_kb.py` — subject verifier

Raw commercial textbook scans and raw notebook photographs remain intake/provenance material and are **not** copied into the public workspace.

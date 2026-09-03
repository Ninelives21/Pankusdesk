# MAC Unit I — textbook/class-notes separation audit — 3 September 2026

## Goal

- Keep the Unit I Text page textbook-led and free of embedded dated class-note sections.
- Keep textbook questions on their dedicated page.
- Move Priyanka's dated notes to one chronological Unit I Class Notes page with date/topic navigation.

## Class-note sections removed from `topics.json`

- `u1-rank-echelon` — **Rank — class-note view** (CLASS-U1-2026-08-25)
- `u1-inverse-gauss-jordan` — **Gauss–Jordan method — class-note view** (CLASS-U1-2026-08-28)
- `u1-rank-normal` — **Normal form — class-note view** (CLASS-U1-2026-08-25)
- `u1-linear-systems` — **System of linear equations — class-note view** (CLASS-U1-2026-08-29)
- `u1-linear-systems` — **Gauss-elimination terminology — class-note view** (CLASS-U1-2026-09-01)
- `u1-non-homogeneous-systems` — **Consistency — class-note view** (CLASS-U1-2026-08-29)
- `u1-non-homogeneous-systems` — **Gauss-elimination / Row-rank method — class examples** (CLASS-U1-2026-09-01)
- `u1-homogeneous-systems` — **Homogeneous systems — class-note view** (CLASS-U1-2026-08-29)
- `u1-homogeneous-systems` — **Homogeneous systems by Row-rank method — class examples** (CLASS-U1-2026-09-01)

**Total removed from theory: 9 class-note sections.**

No textbook/syllabus section was removed. Topic-level `CLASS-U1-*` references and `class_history` rows were removed from Unit I theory topics; textbook/syllabus provenance remains intact.

## Dedicated dated records

- 25 Aug 2026 — notebook pp. 1–5
- 28 Aug 2026 — notebook pp. 6–10
- 29 Aug 2026 — notebook pp. 11–12
- 1 Sep 2026 — notebook pp. 13–18
- 2 Sep 2026 — notebook pp. 19–21

Notebook numbering is continuous from p. 1 through p. 21.

## Duplicate-reconciliation rule

- If class notes repeat textbook theory, the textbook version remains on **Text** and the class version remains only on **Priyanka's Class Notes**.
- If a later class repeats a method but adds a new worked example or side note, the later date is retained because it is new class material.
- Raw notebook errors are not promoted into textbook theory. The class page preserves the class context and labels independent verification separately.

## Verified notebook issues surfaced on the class page

- 1 Sep p.14: `2 < 4` corrected in a verification note to `2 < 3`; infinite-solution conclusion unchanged.
- 1 Sep p.16: `R2 - 2R1` row entry corrected in a verification note; rank/trivial-solution conclusion unchanged.
- 1 Sep p.18: supplied page stops mid-solution; verified `λ = 1, -9` solution families are labelled as independent completion.
- 2 Sep p.19: class work stops before full parameter solution; verified one-parameter family is labelled as independent completion.
- 2 Sep p.20: displayed row is the negative of the annotated row operation; solution family is unchanged.
- 2 Sep p.21: later handwritten arithmetic does not solve the original four-variable system; verified unique solution is `(2, 1, -1, 3)`.

## Unit II safeguard

Unit II theory was not refactored. Existing `math_mismatch` flags for Grewal Examples 2.43, 2.53 and 2.54 remain in place and continue to use the amber worked-example renderer.

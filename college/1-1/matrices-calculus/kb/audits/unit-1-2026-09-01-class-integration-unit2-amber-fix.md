# MAC 1 Sep class integration + Unit II amber renderer fix — 2026-09-01

## Inputs

- Latest workspace: `redo(20260901-145308).zip`
- Class-note source: `mac_1stSept.zip`, notebook pp. 13–18
- Prescribed-book verification: Grewal §2.10, especially pp. 50–56
- Prior Unit-II amber fix used only as a reference; changes were merged into the latest workspace rather than overwriting newer renderer/schema additions.

## Unit I class-note integration

- Added permanent dated class log at `kb/class-log/2026-09-01/`.
- Added calendar entry and source-manifest provenance.
- Added the lecturer terminology **Gauss-elimination method (Row-rank method)** to Unit I without inventing a new R25 syllabus atom.
- Mapped the method to Grewal §2.10 consistency/rank procedure.
- Added verified class examples to the cumulative non-homogeneous and homogeneous topics.
- Example 5 is the same problem as Grewal Example 2.34 (pp. 51–52).
- Preserved two notebook slips transparently: p.14 compares rank 2 with 4 instead of 3; p.16 writes -3 where `R2-2R1` gives -2. Both conclusions remain correct.
- Notebook p.18 stops mid-working. The dated record stops with it; the cumulative page clearly labels the completion as an independent verification. Verified result: `lambda = 1` or `lambda = -9`, with nullspace ratios `(1,-1,2)` and `(-3,-9,2)` respectively.

## Unit II amber fix

- Added first-class `math_mismatch` support to worked-example accordions in the generic theory renderer.
- Preserved the latest workspace's study-table renderer and schema additions; the old delta was not copied wholesale.
- Added visible amber badges + open-state amber notes for Examples 2.43, 2.53 and 2.54.
- Removed only the duplicate generic caution strings for those three examples.

## Verification

Run:

- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`
- `python3 scripts/tools/verify_college.py college/1-1/matrices-calculus`

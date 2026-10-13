# BEE semester PYQs — three-year solved build

Date: 2026-10-13

## Source workspace

Latest user-supplied `redo.zip` for this task.

## Paper sources locked

1. 2023–24: VNR R22, subject code `22ES1EE101`, **Basic Electrical and Electronics Engineering**, January 2024 Regular Examinations, common to CSE/IT/CyS/DS. Extracted from the user-supplied `2023-24 I Semester.rar`.
2. 2024–25: VNR R22, subject code `22ES1EE101`, **Basic Electrical and Electronics Engineering**, January 2025 Regular/Supplementary Examinations, common to CSE/IT/CyS/DS. Extracted from the user-supplied `2024-25 I Semester.rar`.
3. 2025–26: VNR R25, subject code `25ES1EE101`, **Basic Electrical Engineering**, January 2026 Regular Examinations, common to CSE and IT. This is the current R25 paper.

The R22 papers are preserved as complete historical papers. Their electronics questions are solved but explicitly marked as outside the current `25ES1EE101` R25 syllabus. They are not promoted into current R25 unit teaching content.

## UI / architecture

- Reused the existing subject-level `pyqs.html` destination.
- Added data-driven `kb/data/pyqs.json` and shared `scripts/new/pyqs.js` renderer.
- No separate page per year: `pyqs.html` uses `?year=YYYY-YY`.
- Default with no query string is `2025-26`.
- Added previous/current/next year navigation at the top, modelled on the existing unit-neighbour navigation pattern.
- All 45 paper questions are accordion items; multi-part official questions retain their subparts inside the same accordion.
- The five source-paper circuit figures are now represented by explicit PYQ image placeholders, using zero-padded target filenames (`q01.png`, `q02.png`, `q01b.png`) and preserving year/question/source-page provenance. The source-paper PDFs remain available for faithful redraws.
- Each paper provides a local source-PDF link.
- Updated the existing BEE index study-tool card to `Semester PYQs · Solved`.
- Removed the non-functional `Page & figure references` and `Formula & method sheet` cards from the BEE index for now; they can be added back when a concrete study workflow needs them.

## Answering / source rules

- Current R25 answers were aligned to the current PankusDesk R25 unit content and prescribed-textbook conventions.
- Approved gap treatment is retained where needed, especially synchronous-impedance regulation.
- Historical R22 electronics answers are clearly marked as historical/outside current R25.
- No old-paper electronics content was inserted into the canonical R25 unit Text pages.

## Numerical checks performed

- 2023–24 Q1: `I_50Ω = 1 A` downward.
- 2023–24 Q2: `I_4Ω = 30/7 A ≈ 4.286 A` downward.
- 2023–24 Q4: `R = 25 Ω`, `C ≈ 58.36 µF`, `pf ≈ 0.417` leading.
- 2024–25 Q1(b): `R_ab ≈ 142.32 Ω`.
- 2024–25 Q2: `I_7Ω = 55/26 A ≈ 2.115 A` downward.
- 2024–25 Q4: `I ≈ 8.52 A`, `pf ≈ 0.298` leading, `V_L ≈ 80.3 V`, `V_C ≈ 271.2 V`, `P ≈ 508 W`, `Q ≈ -1.626 kVAR`, `S ≈ 1.704 kVA`.
- 2024–25 Q5(b): DC shunt-motor speed `≈ 626 rpm`.
- 2024–25 Q6(b): secondary emf `450 V`; `B_max ≈ 1.014 T`.
- 2024–25 Q7(a): synchronous speed `1500 rpm`; rotor speed at 4% slip `1440 rpm`.
- 2025–26 Q2: `V_Th = 32 V`, `R_Th = 8 Ω`.

## Verification performed

- `pyqs.json` parses successfully.
- Exactly 15 official question accordions per year, 45 total.
- Every question has a non-empty answer.
- All source-paper paths referenced by `pyqs.json` exist.
- Exactly five question-image entries are placeholders; each has a zero-padded target filename and source-paper page metadata.
- Legacy extracted circuit PNGs from the previous build remain physically present in the workspace but are no longer referenced by the PYQ data/renderer.
- Mathematical delimiter scan: balanced `\\(...\\)` and `\\[...\\]`.
- JSON control-character scan: no unexpected control characters.
- `scripts/new/pyqs.js`: `node --check` passes.

Further repository-level verifier results are recorded in the handoff after packaging.
- BEE KB verifier: PASS.
- Global College verifier: PASS.
- Headless Chromium screenshot pass was attempted but Chromium did not complete within the execution window; no browser-visual PASS is claimed.

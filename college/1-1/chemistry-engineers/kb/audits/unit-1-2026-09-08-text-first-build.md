# Chemistry Unit I — text-first build audit

Date: 2026-09-08

## Sources used
- Official VNR VJIET R25 Chemistry for Engineers Unit I syllabus (course 25BS1CH101).
- Supplied Jain & Jain `Engineering Chemistry` Unit-I captures: textbook pp. 1–54 plus analytical-chemistry appendix pp. 1415–1418.

## Build choices
- R25 syllabus defines scope; out-of-scope chapter material is not pulled into the unit merely because it appears in Chapter 1.
- Relevant source tables are represented semantically with the shared `<table>` renderer.
- Chemistry formulae and equations are authored for MathJax/LaTeX; fractions use `\\dfrac`.
- Textbook diagrams are intentionally not embedded yet. Each retained figure is a structured placeholder carrying textbook figure number, figure name and textbook page number.
- The generic figure schema/renderer now supports explicit figure placeholders, so placeholders are not represented as broken `<img>` elements.

## Explicit source gaps / partial coverage
- R25 requires Microfiltration (MF), Ultrafiltration (UF) and Nanofiltration (NF), including advantages and applications. These were not found in the supplied Jain & Jain Unit-I pages; no outside theory was invented.
- The supplied textbook gives potable-water specifications, but the page does not identify them specifically as WHO values. They are therefore not relabelled as WHO specifications.
- The supplied pages support EDTA complexometric chemistry, EBT, pH and colour change, but do not present a single standalone water-hardness-by-EDTA laboratory procedure matching the R25 wording. This remains partial until an approved source/class/lab source is supplied.

## Figure placeholders retained
- Fig. 1 — Scale and sludge in boilers — p. 7
- Fig. 6 — Acidic or cation exchange resin (sulphonate form) — p. 17
- Fig. 7 — Basic or anion exchange resin (hydroxide form) — p. 18
- Fig. 8 — Demineralisation of water — p. 19
- Fig. 9 — Regeneration of mixed-bed ion exchanger — p. 20
- Fig. 10 — Sand filter — p. 21
- Fig. 11 — Chlorinator — p. 23
- Fig. 12 — Break-point chlorination curve — p. 24
- Fig. 14 — Flow diagram of drinking water treatment plant — p. 25
- Fig. 17 — Reverse osmosis cell — p. 27

## Verification
- `python3 scripts/tools/verify_college.py` — PASS after adding the generic `draft` publication state used for a visible but explicitly incomplete unit.

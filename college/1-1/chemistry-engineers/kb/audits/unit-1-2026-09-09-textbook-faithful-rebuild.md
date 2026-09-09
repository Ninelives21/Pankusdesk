# Chemistry Unit I — textbook-faithful rebuild (2026-09-09)

## Build intent

Unit I was rewritten so the student-facing theory follows the supplied Jain & Jain textbook much more closely in sequence, terminology, technical detail, calculations and treatment steps. It is deliberately not a short summary. The wording is a faithful paraphrase rather than a transcription.

## Rendering rules retained

- Tables remain structured data rendered as semantic HTML `<table>` elements by the shared unit renderer.
- Chemical equations and mathematical expressions are stored as MathJax/LaTeX strings.
- Figures remain placeholders for the later image pass. Every placeholder states textbook figure number, figure name and printed textbook page.
- Textbook-only topics outside the R25 Unit-I scope are not pulled into the student page merely because they occur between required sections.

## Important correction from the first draft

The supplied textbook **does contain the full water-hardness EDTA procedure** on printed pages 33–35: principle, EBT/pH-10 end point, preparation of solutions, EDTA standardisation, titration for total hardness, boiling/titration for permanent hardness, formulas for total/permanent/temporary hardness, and advantages. The earlier draft incorrectly marked this as only partial coverage. It is now treated as covered.

## Remaining source limitations

1. R25 explicitly asks for WHO potable-water specifications. The supplied textbook gives drinking-water specifications but does not explicitly identify those values as WHO values; the page therefore does not relabel them.
2. R25 asks for MF, UF and NF membrane types, advantages and applications. Those subsections were not found in the supplied Unit-I textbook pages and remain a source gap.

## Figure placeholders retained

- Fig. 1 — Scale and sludge in boilers — p.7
- Fig. 6 — Acidic or cation exchange resin (sulphonate form) — p.17
- Fig. 7 — Basic or anion exchange resin (hydroxide form) — p.18
- Fig. 8 — Demineralisation of water — p.19
- Fig. 9 — Regeneration of mixed-bed ion exchanger — p.20
- Fig. 10 — Sand filter — p.21
- Fig. 11 — Chlorinator — p.23
- Fig. 12 — Break-point chlorination curve — p.24
- Fig. 14 — Flow diagram of drinking water treatment plant — p.25
- Fig. 17 — Reverse osmosis cell — p.27

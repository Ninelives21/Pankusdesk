# WS 1 — college worksheet integration

## Scope and source

User-confirmed label: **WS 1**. The supplied `MAC WORK SHEET.pdf` is retained byte-for-byte at `worksheets/ws-1.pdf`, SHA-256 `ad5bfc80fcb54ac48318d7c9b8c680e5b7bb65462f232e24d002d9938172d044`.

All 15 PDF pages were visually inspected to recover mathematics absent from text extraction. The bank contains 272 section-numbered entries: Unit I 44, Unit II 24, Unit III 52, Unit IV 67, Unit V 85. Repeated source questions remain separate entries. Per-group PDF page references are stored in the bank. The original source title does not identify a worksheet number; WS 1 is the user's organisational label.

The subject resource card links to a shared worksheet adapter. Future worksheets are registered in `worksheets/index.json`; each supplies its own bank and globally unique anchors. Question and solution dropdowns, mathematics and interaction use `PankuStudyUI`. Only the number text in Unit III–IV cards is amber; no question prose or answer card receives an amber background.

The worked answers are PankusDesk-authored, not attributed as verbatim textbook or class-note solutions. The supplied class/textbook sources informed the earlier Unit III–IV review, but each worksheet assertion is independently assessed. Canonical topic JSON, unit publication states, class records and existing figures are unchanged. Curve answers give analytical traces; no new/replacement technical drawings are generated under the figure freeze.

## Source issues retained in the relevant answers

- Unit I: Short Q7 asks for k although its matrix uses x; Gauss–Seidel Q3 prints a chain of equalities. The likely intended linear system is explicitly labelled. Original matrices are preserved; rank and inverse computations use exact arithmetic.
- Unit II: Long Q4 is not diagonalizable: its repeated eigenvalue has insufficient independent eigenvectors. Cayley–Hamilton still provides its inverse, power and polynomial reduction.
- Unit III: Rolle Q3 fails endpoint equality; LMVT Q3 fails differentiability at zero; Rolle Q10 lacks an operator. LMVT Q9 has a reversed logarithm; Q12 repeats its lower-bound denominator in the upper bound. Domain omissions and the CMVT Q6 endpoint are explained. Curve Q7 repeats Q6 and stays unchanged.
- Unit IV: Short Q2's function is undefined at the requested point; Short Q8 lacks its origin value/axis cases. Product optimisation answers state sign assumptions, and Lagrange Q6's requested minimum is distinguished from its interior maximum. Euler Q1's additional mixed-derivative identity is false and a counterexample plus correct derivative are shown. The implicit derivative logarithm notation is clarified.
- Unit V: Several differentials conflict with variable-dependent bounds; labelled intended orders and regions are given rather than silently replacing the source. Short Q5 has crossed inner bounds and is reversed as a difference of regions. The polar Q3 printed target has incorrect scaling. Ambiguous crescent/common-area descriptions have their region assumptions stated. Triple Q1 has an incompatible order and a divergent natural intended integral; Q7 lacks a lower z-bound; Q14 diverges at the origin. Triple Q13's reversed limits retain their negative sign.

## Validation

- `python3 scripts/tools/verify_mac_worksheet.py`: source hash, all 272 entries, all original section counts, sequential numbers, nonempty working/results and unique group/question anchors.
- JSON parsed and validated against `college/schemas/worksheet.schema.json`; new JavaScript syntax checked.
- All three baseline college/BEE/MAC validators pass; unit publication states remain unchanged.
- Exact symbolic calculations verified matrix inverses by AA⁻¹=I, eigenvector/modal identities by AP=PD, all eight matrix polynomial reductions against direct matrix evaluation, and quadratic-form transformations by PᵀP=I and PᵀAP=D. Selected Unit III–IV derivatives, series, Jacobians and extrema have 16 additional independent symbolic checks. Unit V iterated evaluations record their successive antiderivatives; manually transformed/singular cases include explicit domain reasoning.
- Local Chromium checks at 1440px and 390px cover card navigation, WS selection, 272 dropdowns, 119 amber numbers, original PDF, exclusive group accordions, direct question anchors, mathematics and horizontal overflow. A routed `github.io/Pankusdesk/` browser check verifies base-path resolution. Screenshots reviewed locally; not a claim of hosted-preview acceptance.
- The Vercel static-output build includes the new HTML, JSON, shared adapter/CSS and unchanged PDF. The final PR handoff records the actual preview URL/commit and any pending deployed checks.

## Merge gate

Provide 2–4 unchecked, clickable manual acceptance checks in the PR description and chat. Do not auto-merge. Do not change Chemistry PR #24.

# MAC Unit V textbook integration — 3 November 2026

Base: main at `3498dd4167f9ab282f2dbba92f81bc038a415c18` (merged PR #30).

## Sources and completeness

- `Mac-unit5_01.zip`: 24 photographs, capture suffixes 1–24, printed pp. 315–338.
- `Mac-unit5_02.zip`: 26 photographs, suffixes 25–50, printed pp. 339–364.
- All 50 printed page identities were checked, including the chapter opening p. 315 and final page p. 364. There are no missing or duplicate pages in that range. Native filenames say `Mac-unit4`; their academic content is Chapter 7 / R25 Unit V, so filenames are retained only as provenance.
- `mac-unit5-source-captures.json` records archive identities, page/capture correspondence and SHA-256 hashes. The source manifest records both archive hashes. Full-page photographs are not published.
- `mac_book_answers.zip` could not be transferred: it exceeds the executor tool's 32 MiB limit. This integration **does not claim a comparison with that appendix**. It must be split into files under 30 MB before that additional cross-check can be performed. Existing Units I–II printed-answer checks remain unchanged.
- The new book packet's exact edition remains unconfirmed; no replacement edition citation has been invented.

## Included theory

All nine R25 Unit V atoms now have detailed textbook-led theory: Cartesian and polar double integrals, Cartesian order changes, Cartesian-to-polar substitution, triple integrals, spherical/cylindrical substitution, areas and volumes. Core theory follows §§7.1–7.7; later in-scope Examples 7.59–7.61 are placed with order changes. Notes remain grouped by the existing stable syllabus-topic IDs. The existing appendix formulas are retained; only their obsolete “chapter not supplied” statements are removed.

There are **38 example dropdowns** with complete visible questions, reproducible working and bold final results. The book prints “Example 7.15” both for the polar integral on p. 321 and the parabolas on p. 323; the polar example has a disambiguated title and stable `tb-example-7-15-polar` anchor. The missing numbering is not invented. Examples 7.33–7.34 are separately labelled supporting general substitutions, rather than being presented as the named R25 polar transformation.

There are **37 ROS assets**, including source-combined panels: all supplied relevant diagrams in §§7.1–7.7 and Examples 7.59–7.61. The images are original-pixel crops, losslessly encoded; no lines, arrows, labels or colours were redrawn. Each was compared visually with the source, including review of crop boundaries, and checked for pixel equality. Coordinates and input/output hashes are in `mac-unit5-ros-figures.json`. Known printed figure errors remain in the pixels and are explained beside the affected working. Chapter 7 references Figs. 8.27/8.28 on other pages; those two coordinate diagrams were **not supplied**, and no substitutes are invented.

## Question-page scope

`unit-5-questions.html` contains **104 questions across six exercise groups**. Original numbering, duplicate printed questions and labelled subparts are retained. Multiple-choice options have separate lines/anchors. Q7.1.15 has explicit sketch-construction guides and exact region limits; the source supplies no exercise sketch to extract as ROS, so no substitute drawing is invented. Every question has working and an explicit result or an explicit conditional/source-ambiguity outcome. Questions are PankusDesk solutions, not purported printed textbook solutions.

| Set | Included questions | Treatment |
| --- | --- | --- |
| 7.1 | 1–18, including both parts of 15 | Complete supplied double-integral set; polar order-change part 15(ii) labelled supporting |
| 7.2 | 1–8 | Complete supplied plane-area set |
| 7.3 | 1–11 | Complete supplied triple-integral set; duplicate Q3/Q5 retained |
| 7.4 | 1–26, 28 | All area/volume/integral questions; Q27 is mass, outside current R25; general substitutions Q5/Q6 labelled supporting |
| 7.9 | 5, 9–18 | All in-scope double-integral/order-change questions; Q1–4 elliptic integrals and Q6–8 error functions excluded |
| 7.10 | 1–3, 7–8, 11–29, 32–33, 41–43 | All in-scope objective questions plus supporting Gaussian/Jacobian applications; original gaps correspond to excluded material |

Excluded theory/problem sets concern curved-surface area, mass, centres of gravity/pressure, moments/products of inertia, Beta/Gamma/Dirichlet methods, elliptic integrals and error-function theory. These are not R25 Unit V syllabus atoms. In 7.10 the excluded questions are 4–6, 9–10, 30–31 and 34–40. A supplied double-integral question is not excluded merely because it occurs after an out-of-syllabus section.

The six practice callouts are inserted at their corresponding theory sections. Unit V is enabled in the shared Textbook Questions navigation. Class Notes remains unavailable because no Unit V class packet has been supplied. Units I–IV theory/questions, dated and undated class records, worksheet solutions, existing figures and unrelated subjects are preserved.

## Verified discrepancies and source uncertainty

Amber is reserved for checked printed mathematical discrepancies. Important examples:

- Ex. 7.1, 7.6, 7.7, 7.20, 7.21 and several exercise headers print differential orders incompatible with their variable bounds. The bounds and accompanying working are retained with explicitly corrected differential orders.
- Ex. 7.5/Fig. 7.7, Ex. 7.10/Fig. 7.12, Ex. 7.15/Fig. 7.18, Ex. 7.25/Fig. 7.27, Ex. 7.26/Fig. 7.28, Ex. 7.29/Fig. 7.31, Ex. 7.35/Fig. 7.36, Ex. 7.59/Fig. 7.54 and Ex. 7.61/Fig. 7.56 have equation/coordinate/axis-label slips; ROS retains their pixels.
- Ex. 7.11 has an incorrect intermediate denominator; Ex. 7.14 substitutes b² where a² belongs in its prose; Ex. 7.23 omits an antiderivative minus sign.
- Ex. 7.18: the final printed `19/2` must be **19/9**; the verified result is `(8/3)ln 2 − 19/9`.
- Ex. 7.26: `0<α<π` includes an undefined tanα and negative printed volume; acute-angle and absolute-value interpretations are explicit.
- Ex. 7.27: the printed equation is a **sphere**, but its solution is for `z=16−x²−y²`. Both readings are preserved; the displayed closed form follows only the explicitly labelled paraboloid. The rectangle also needs `a²+b²≤16` for nonnegative height throughout.
- Ex. 7.31: an absolute cosine is needed in the intermediate radial result. Ex. 7.34: printed **2/945** should be **16/945**; its boundary notes also incorrectly fix u=0 along whole edges.
- Ex. 7.59: the self-referential inner lower limit x is invalid; the worked solution and diagram clearly use the triangle `0≤x≤y≤π/2`. Its conditional correction is explicit. Ex. 7.60 has a wrong sign in an intermediate boundary line.
- Problems 7.1 Q2 prints a² in a cubic endpoint contribution; Q4's printed positive answer disagrees with its downward-oriented radial limits.
- Problems 7.3 Q9: as printed, the outer z interval reaches π, making `√(4−z²)` non-real. A clearly labelled change of y/z order yields a conditional **16/3**, not an unqualified correction.
- Problems 7.4 Q1 has a self-referential inner limit; a quarter-disk interpretation is explicit. Q9's whole-ball answer must be **π²a²**, rather than the printed **π²a³/8**. Q21 repeats the same parabola twice, so no finite base is determined; **569/140** is conditional on replacing one by `y=x²`. Q26's area scales as a², not a³.
- Problems 7.10 Q11 repeats dx in its differentials. Q16 and Q17 genuinely diverge under their explicitly stated interpretations; no finite answer is invented.
- **Transcription uncertainty, not a verified textbook error:** Problems 7.10 Q23, p. 364. The first relation appears as “y+x²” but its sign is unclear in the photograph. A close-up is needed. The value **3/56** is explicitly conditional on `y=x²`; this item has no verified-error amber state.

These annotations distinguish verified corrections, intended regions justified by source working, and interpretations that still need confirmation. Mathematical verification cannot establish an unreadable symbol's identity.

## Validation and remaining gates

- Required college, BEE and MAC validators: PASS.
- `kb/tools/verify_unit5.py`: PASS; exact source/question/example/asset accounting and I–IV data preservation.
- `kb/tools/check_unit5_calculus.py`: **141 exact independent calculations PASS**, including alternative-coordinate checks, Jacobians, improper integrals and conditional interpretations. This does not replace source transcription review or an appendix comparison.
- Modified JSON parsing, subject/question-bank schemas, Python compilation and JavaScript syntax: PASS.
- Strict topics schema: **32 pre-existing errors, unchanged from main; zero new errors**. The legacy errors are not suppressed or weakened.
- Chromium at 1440 px and 390 px: Unit V Text/questions, MAC index and Unit IV regression checked. No Unit V MathJax errors or document overflow; dropdowns, all 37 assets, six set links, multipart solutions, deep links and `/Pankusdesk/` base path checked.
- Pre-existing limitation: the unchanged Unit II Text page has document overflow at 390 px. It is recorded separately; no Unit II data/CSS changes were made here.
- Vercel static build: PASS, below the 350 MiB limit. Hosted preview acceptance is a user check, not claimed as an agent browser test.

Unit V remains **draft pending final review**, with complete supplied R25 theory coverage. The subject now has **39/43 covered theory atoms**; the four Unit III gaps remain. Unit III/IV partial textbook exercise banks are unchanged by this Unit V release. No PR is merged automatically.

For follow-up, provide the answer appendix in ZIPs under 30 MB, a clearer crop of p. 364 Q23, and optionally the edition title/copyright and Figs. 8.27/8.28. These limits must remain explicit in the PR handoff.

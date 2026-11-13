# End Sem intake and solution review

Four distinct full-length papers, all two pages, are represented once each. Labels use the printed examination session rather than the misleading filename year. PDF identities/checksums, original branches, subject codes, marks, unit order, question wording, source pages and answer references are in `end-sem-papers.json`.

- January 2026 R25 Chemistry for Engineers, 25BS1CH101 (includes IT).
- January 2025 R22 Chemistry for Engineers, 22BS1CH102 (includes IT).
- January 2024 R22 Chemistry for Engineers, 22BS1CH102 (includes IT).
- January 2025 R22 Engineering Chemistry, 22BS1CH101 (ME).

Each paper has five 2-mark Part A questions and ten Part B alternatives, grouped into five OR pairs. All 60 dropdown questions and 87 marked answer parts are answered. Historical units are preserved; R22 polymer/corrosion unit numbering is not relabelled as R25. Repeated questions across distinct papers remain. Questions from supporting banks are not presented as examination papers.

## Answer review

Answers use the supplied college/senior notes and their existing checked Mid 2 working where applicable. Structured blocks keep source references in JSON and teaching content in the student answer. Short answers are focused; essays include the requested definitions, processes, comparisons, reactions and applications. The comparison of biodegradable lubricants needs general materials knowledge beyond the supplied lubricant descriptions; that limited fallback is recorded in its answer data. These are study solutions, not official VNR marking keys.

Independent rational-arithmetic checks (course integer molar masses; all values as CaCO3):

| Paper / question | Temporary ppm | Permanent ppm | Total ppm |
| --- | ---: | ---: | ---: |
| Jan 2026 / 1(a) | 53.62 | 29.98 | 83.60 |
| Jan 2024 / 1(a) | 20.00 | 15.00 | 35.00 |
| Jan 2025 ME / 1(b) | 125.00 | 150.00 | 275.00 |

The two papers listing MgCO3 are interpreted using the intended carbonate-hardness convention, stated in the answer. Suspended material is excluded. Atom/charge balances were reviewed for the corrosion, fuel-cell, electrolysis, coagulation, resin, polymerisation and coal-analysis equations. Ultimate-analysis oxygen by difference accounts for the reporting basis and ash/moisture; the balanced Kjeldahl liberation equation contains two water molecules.

## Figures and source ambiguities

Existing approved images are reused unchanged for water treatment, SHE, corrosion/protection, PEM electrolysis/fuel cells, Fischer–Tropsch, STM and methanol cells. One original-pixel Bakelite network crop is added; the full network is retained and source pixels are compared against the embedded image. No PDF or full scanned page is published. Figure mappings, hashes and crop bounds are in `end-sem-source-figures.json` and the existing figure manifests.

Known source issues remain explicit:

- **Missing CO-analyser apparatus drawing:** January 2026 Q9(b) has a complete written operating explanation but still lacks a verified supplied apparatus figure. No substitute is generated under the drawing freeze.
- The supplied SHE image wrongly labels mercury. Its answer explicitly identifies platinised platinum as the active surface.
- The oxide-film drawing uses schematic “MO”; its answer gives a balanced metal-specific reaction.
- The old notes label circulating fluidised cracking as moving-bed/fluid-bed. January 2024 Q6(a) follows that course treatment; it does not pretend to depict a separate true moving-bed apparatus.
- January 2025 ME Q9(a) prints “Glass, Fibre and aramid”. The answer covers the standard glass-, carbon- and aramid-fibre groups; this ambiguity is retained in JSON.
- Free chlorine from bleaching powder gives faster initial disinfection than chloramine; chloramine's advantage is persistence. These are distinguished instead of equating persistence with stronger immediate action.

## Validation

`verify_chemistry_endsem.py` gates all four paper identities, 60 questions/87 answer parts, choices, marks, source/page bounds, numerical results, exact image hashes, required placements, nested answer parts, anchors, navigation and card replacement. The required college/BEE/MAC validators and the existing Chemistry bank/Mid 2/figure/answer/revision verifiers pass. Browser checks open every question at desktop and phone widths and check MathJax, decoded images, responsive scrolling, paper selection, full-card click, Back to top, legacy PYQ redirection and the GitHub Pages `/Pankusdesk/` prefix. Screenshots are retained outside the repository.

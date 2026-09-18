# BEE Unit I — Exercise 1.7.4 SIMPLER integration

Date: 2026-09-18

## Source workspace

Latest user-supplied `redo.zip`, extracted and inspected before editing.

## Source/resource check

No outside source was used. The existing Exercise 1.7.4 compact solution and Figures 1.49 through 1.49(d) were used as the source basis.

Visual/semantic checks performed before writing the explainer:

- Figure 1.49: top-right 2 ohm + 1 ohm and bottom-right 3 ohm + 5 ohm are genuine series pairs because their shared corner nodes have no other branches.
- Figure 1.49(a): upper delta is `a-b-c` with 6, 12 and 3 ohms; lower delta is `d-e-f` with 10, 4 and 8 ohms. The 8 ohm `b-d` and 2 ohm `c-e` branches are outside the deltas.
- Figure 1.49(b): upper-star values shown are 0.857, 3.43 and 1.714 ohms; lower-star values are 1.818, 1.455 and 3.636 ohms.
- Figure 1.49(c): two centre-to-centre branches shown are 13.25 and 5.169 ohms.
- Figure 1.49(d): their parallel equivalent is shown as 3.718 ohms, leading to 12.211 ohms and 1.638 A.

## Existing source discrepancy preserved

The compact printed sentence identifies the lower delta as `d,c,f`, while the actual labelled circuit is `d,e,f`. The existing amber discrepancy remains unchanged. The SIMPLER follows the drawing and explicitly says `d,e,f`.

## Change made

Added a nested `SIMPLER` explainer to Exercise 1.7.4 in `kb/data/topics.json`, positioned after the opening paragraph. Mirrored the walkthrough into cumulative `kb/notes/unit-1.md`.

The explainer teaches:

1. why the initial 2+1 and 3+5 combinations are series;
2. how to identify the upper `a-b-c` and lower `d-e-f` deltas;
3. which 8 ohm and 2 ohm branches remain outside the transformations;
4. all six Delta → Star calculations;
5. why the transformed network creates two series routes between the star centres;
6. why 13.25 ohms and 5.169 ohms are parallel;
7. the 3.718 ohm parallel reduction;
8. the final series sum to 12.211 ohms using the textbook's rounded displayed values; and
9. source current `I = 20/12.211 = 1.638 A`.

No textbook figure, compact source solution, or printed final answer was overwritten.

## Verification to perform

- JSON parse
- LaTeX/control-character scan on added content
- arithmetic verification
- BEE KB verifier
- global College verifier
- delta ZIP integrity/test-unzip

## Verification performed

- `topics.json` parse and target explainer structure: PASS.
- Added-content control-character scan: PASS.
- Arithmetic check: upper-star values, lower-star values, centre-to-centre series routes, parallel reduction, total equivalent resistance and source current all recomputed independently and consistent with the textbook reduction. Exact unrounded values give `R_eq = 12.211565... ohm` and `I = 1.637791... A`; the textbook's displayed `12.211 ohm` follows its rounded intermediate figures, and its final `1.638 A` is consistent.
- BEE KB verifier: PASS.
- Global College verifier: PASS.
- Delta ZIP integrity/test-unzip: pending packaging step below.

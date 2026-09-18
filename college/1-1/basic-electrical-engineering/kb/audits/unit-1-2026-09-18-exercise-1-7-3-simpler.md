# BEE Unit I — Exercise 1.7.3 SIMPLER integration

Date: 2026-09-18

## Source workspace

Latest available user-supplied `redo.zip`, extracted and inspected before editing. This workspace contains Exercise 1.7.3 and Figures 1.48 through 1.48(d), plus the established nested SIMPLER mechanism used by earlier worked examples.

## Source/resource check

No outside source was used. The existing Exercise 1.7.3 compact solution and its five supplied NRS textbook redraws were the basis for the explainer.

The figures were visually checked before writing the explainer:

- Figure 1.48: 12 V source across nodes `a` and `d`; left delta `a-b-c` contains 3 ohm (`a-b`), 2 ohm (`a-c`) and 1 ohm (`b-c`); 4 ohm joins `b-d`; 5 ohm joins `c-d`.
- Figure 1.48(a): the `a-b-c` delta is replaced by star arms `R_a`, `R_b`, `R_c`; the original 4 ohm and 5 ohm branches remain.
- Figure 1.48(b): substituted star values are 1 ohm, 0.5 ohm and 0.33 ohm.
- Figure 1.48(c): the drawing visibly labels the upper reduced branch `4.55 ohm` and the lower branch `5.33 ohm`.
- Figure 1.48(d): the later reduction uses 2.44 ohm, then 3.44 ohm, and shows 3.49 A source current.

## Verified discrepancy

Figure 1.48(b) makes the upper series branch `0.5 + 4 = 4.50 ohm`, not `4.55 ohm`. The exact lower branch is `1/3 + 5 = 16/3 ohm`. Using the correct upper value:

- `(9/2) || (16/3) = 144/59 = 2.440677... ohm`;
- total `R_eq = 1 + 144/59 = 203/59 = 3.440677... ohm`;
- source current `i = 12/(203/59) = 708/203 = 3.48768... A`, which rounds to `3.49 A`.

Thus the later 2.44 ohm, 3.44 ohm and 3.49 A values are consistent with 4.50 ohm. The source figure is preserved and the mismatch is flagged rather than silently redrawn.

## Change made

Added a nested `SIMPLER` explainer to Exercise 1.7.3 in `kb/data/topics.json`, positioned after the opening Delta-to-Star solution sentence.

The explainer explicitly teaches:

1. how to identify the `a-b-c` delta in the bridge;
2. which 4 ohm and 5 ohm branches are outside the selected delta and remain untouched;
3. why converting this particular delta creates useful series branches;
4. how to name `R_ab`, `R_ac`, `R_bc` before applying the Delta → Star rule;
5. how each star-arm numerator is chosen from the two delta sides touching its terminal;
6. the calculations `R_a=1 ohm`, `R_b=0.5 ohm`, `R_c=1/3 ohm`;
7. why `0.5 + 4` and `0.33 + 5` are series after conversion;
8. why the two resulting centre-to-`d` branches are parallel;
9. why the remaining 1 ohm is then in series with that parallel equivalent; and
10. how the final source current follows from Ohm's law only after the network has been reduced to one equivalent resistance.

Added a `Figure arithmetic discrepancy` amber note to the exercise and updated the Figure 1.48(c) alt text so accessibility text does not state the visible `4.55 ohm` typo as correct arithmetic.

Mirrored the same explanatory material and discrepancy note into cumulative `kb/notes/unit-1.md`.

No textbook figure, compact source solution, printed value, or final answer was overwritten.

## Verification to perform

- JSON parse
- LaTeX/control-character scan on changed content
- exact arithmetic check for the star conversion and final reduction
- BEE KB verifier
- global College verifier
- delta ZIP integrity/test-unzip

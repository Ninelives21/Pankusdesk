# BEE Unit I — Exercise 1.7.1 SIMPLER integration

Date: 2026-09-18

## Source workspace

Latest user-supplied `redo.zip`, extracted and inspected before editing. The current workspace already contains Exercise 1.7.1, Figure 1.46, the Star/Delta theory section, and the established nested SIMPLER mechanism used by earlier worked examples.

## Source/resource check

No outside source was needed. The existing Exercise 1.7.1 entry, Figure 1.46 and the immediately preceding Delta → Star derivation were used as the content basis.

Figure 1.46 was visually checked before writing the explainer:

- delta terminals are A, B and C;
- A–B branch is 25 ohms;
- B–C branch is 15 ohms;
- C–A branch is 10 ohms;
- the equivalent star retains A, B and C as external terminals;
- star arms are labelled `R_A`, `R_B`, `R_C` toward a new internal centre node.

## Change made

Added a nested `SIMPLER` explainer to Exercise 1.7.1 in `kb/data/topics.json`, immediately after the compact `Solution:` line.

The explainer follows the PankusDesk hand-holding pattern and explicitly explains:

1. how to recognize the left network as a delta and the right network as a star;
2. how to name the delta resistors from their terminal pairs (`R_ab=25 ohms`, `R_bc=15 ohms`, `R_ca=10 ohms`);
3. that the star centre is a new internal junction and not terminal C;
4. the Delta → Star rule in words before using the formula;
5. why the denominator is always `25+15+10=50`;
6. how to choose the numerator for each star arm by looking for the two delta resistors touching the same external terminal;
7. the calculations giving `R_a=5 ohms`, `R_b=7.5 ohms`, `R_c=3 ohms`; and
8. an A–B terminal-pair sanity check showing both the delta and star present `12.5 ohms`, reinforcing what “equivalent” means.

Mirrored the same explanatory material into the cumulative `kb/notes/unit-1.md` under Exercise 1.7.1.

No textbook figure, compact source solution, printed values, derivation, or final answer was altered.

## Verification performed

- Figure 1.46 semantic inspection: PASS
- Delta → Star arithmetic for all three arms: PASS
- A–B equivalence sanity check: PASS
- `topics.json` JSON parse: PASS
- added-content LaTeX/control-character scan: PASS
- BEE `verify_kb.py`: PASS
- global College verifier: PASS

Final verifier results are reported in the handoff and should supersede the pending lines above.

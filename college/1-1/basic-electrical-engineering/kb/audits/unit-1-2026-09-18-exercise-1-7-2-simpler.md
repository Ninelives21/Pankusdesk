# BEE Unit I — Exercise 1.7.2 SIMPLER integration

Date: 2026-09-18

## Source workspace

Latest user-supplied `redo.zip`, extracted and inspected before editing. The current workspace already contains Exercise 1.7.2 and Figures 1.47 through 1.47(e), as well as the established Star/Delta and nested SIMPLER implementation.

## Source/resource check

No outside source was needed. The existing textbook exercise text, its six NRS textbook-figure redraws, and the immediately preceding Star ↔ Delta theory/formulas were used as the basis.

Figures 1.47–1.47(e) were visually checked before writing the explainer. The verified progression is:

- original star at node d: 10 ohms to a, 20 ohms to b, 5 ohms to c;
- unchanged external branches: 12.5 ohms a–c, 15 ohms c–b, 30 ohms a–b;
- converted delta: 17.5 ohms a–c, 70 ohms a–b, 35 ohms c–b;
- parallel reductions: 12.5 || 17.5 = 7.2916... ohms, 15 || 35 = 10.5 ohms, 70 || 30 = 21 ohms;
- series path: 7.29 + 10.5 = 17.79 ohms using the textbook's displayed rounding;
- final parallel reduction: 17.79 || 21 ≈ 9.63 ohms;
- source current: 120 / 9.63 ≈ 12.46 A.

## Change made

Added a nested `SIMPLER` explainer to Exercise 1.7.2 in `kb/data/topics.json`, placed after the opening solution sentence.

The explainer follows the PankusDesk hand-holding pattern and explicitly explains:

1. why the objective is first to find the equivalent resistance seen by the 120 V source;
2. why the original bridge cannot immediately be reduced by ordinary series/parallel rules;
3. how to identify the 5/10/20-ohm star from the fact that all three meet at node d;
4. that 12.5, 15 and 30 ohms lie outside the converted star;
5. why this particular Star → Delta conversion is useful: it creates three parallel pairs;
6. how the Star → Delta denominator is chosen using the third/opposite star arm;
7. all three conversion calculations;
8. the node-based reason for each parallel and series reduction;
9. the final 9.63-ohm equivalent and 12.46-A source current; and
10. the effect of carrying unrounded intermediate values through the calculation.

Mirrored the same explanatory content into cumulative `kb/notes/unit-1.md` under Exercise 1.7.2.

No textbook wording, figures, compact calculations, or printed final answer was altered.

## Verification performed

- Figures 1.47–1.47(e) semantic/topology inspection: PASS
- Star → Delta arithmetic: PASS
- three parallel reductions: PASS
- final series/parallel reduction and source-current arithmetic: PASS
- `topics.json` JSON parse: PASS
- added-content LaTeX/control-character scan: PASS
- BEE `verify_kb.py`: PASS
- global College verifier: PASS

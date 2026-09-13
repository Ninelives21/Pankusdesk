# BEE Unit I — Exercise 1.5.8 SIMPLER integration

Date: 2026-09-13

## Source workspace

Cumulative working workspace derived from `/mnt/data/re.zip`, preserving the earlier 2026-09-13 Kirchhoff problem-solving guide and the Exercise 1.5.4, Exercise 1.5.6 and Exercise 1.5.7 SIMPLER integrations.

## Change

Added a `SIMPLER` explainer to textbook Exercise 1.5.8 in `kb/data/topics.json`.

The explainer applies the same Kirchhoff problem-solving sequence used in the general guide:

- read the source polarities, resistance values, current arrow and node labels before writing an equation;
- recognize that this is a single series loop, so the same current flows through both resistors;
- use the shown downward current reference to walk clockwise and assign every KVL sign explicitly;
- solve the loop equation to obtain `I = 4 A` and interpret the positive sign as confirmation of the shown direction;
- calculate the 5 Ω resistor drop as `20 V`;
- define `Vab = Va - Vb` and evaluate it cleanly by moving from `b` to `a` through the 8 V source and 5 Ω resistor;
- verify `Vab = 28 V` again using the alternate left/top path;
- substitute the solved current back into the complete KVL loop as a consistency check.

No textbook question, compact solution, figure, source value, polarity, current arrow, node label or final answer was changed.

## Verification performed

- JSON parse: PASS
- `college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`: PASS
- `scripts/tools/verify_college.py`: PASS
- Added Exercise 1.5.8 explainer mathematical/control-character scan: PASS
- Delta ZIP test-unzip: performed after packaging

No browser visual-render check was performed for this change.

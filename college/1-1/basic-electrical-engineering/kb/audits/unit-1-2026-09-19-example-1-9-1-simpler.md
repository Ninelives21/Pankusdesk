# BEE Unit I — Example 1.9.1 SIMPLER integration

Date: 2026-09-19

## Source workspace

Latest user-supplied `redo.zip`, extracted and inspected before editing.

## Source/resource check

No outside source was used. The existing Example 1.9.1 compact solution and Figures 1.56, 1.57(a), 1.57(b) and 1.57(c) were used as the source basis.

Visual/semantic checks performed before writing the explainer:

- Figure 1.56: the 4 ohm resistor is the load directly between terminals `a` and `b`; the 20 V source is drawn as an independent voltage source with `+` at the top and `-` at the bottom.
- Figure 1.57(a): after the 4 ohm load is removed and the 20 V source is shorted, 5 ohms and 15 ohms share the same two end nodes and are therefore parallel; the resulting 3.75 ohm block lies in series with 2 ohms and 3 ohms as seen from `a-b`.
- Figure 1.57(b): with the load removed and the 20 V source restored, the branches ending at open terminals `a` and `b` carry zero current, so the 2 ohm and 3 ohm resistors have zero voltage drop and `Vab = Vxy`.
- The only closed conducting loop for the open-circuit-voltage calculation contains the 20 V source, 5 ohms and 15 ohms, giving 1 A and `Vth = 15 V`.
- Figure 1.57(c): the original left network is replaced by `Vth = 15 V` in series with `Rth = 8.75 ohm`, feeding the original `RL = 4 ohm` load.

## Change made

Added a nested `SIMPLER` explainer to Example 1.9.1 in `kb/data/topics.json` and mirrored the walkthrough into cumulative `kb/notes/unit-1.md`.

The explainer explicitly teaches:

1. how to identify the 4 ohm resistor as the load from terminals `a-b`;
2. how the circular source symbol and polarity marks identify the 20 V independent voltage source;
3. why an ideal independent voltage source is shorted while finding `Rth`;
4. why 5 ohms and 15 ohms become parallel after that short;
5. why the reduced 3.75 ohm block is in series with 2 ohms and 3 ohms as seen from the load terminals;
6. why no current flows through 2 ohms and 3 ohms while finding `Vth`;
7. why zero current through those resistors makes `Vab = Vxy`;
8. how the remaining 20 V / (5 + 15) loop gives `I = 1 A` and `Vth = 15 V`;
9. what the Thevenin replacement buys us; and
10. a simple physical sanity check on the final load current.

The compact textbook solution, figures and printed final answer were not overwritten.

## Numerical note preserved

`15 / 12.75 = 1.176470... A`. The compact source solution prints `1.17 A`; the SIMPLER states the calculator value and explicitly notes that the textbook prints `1.17 A`, while preserving the printed compact final answer.

## Verification performed

- `topics.json` parse and target explainer structure: PASS.
- Added-content control-character/LaTeX delimiter scan: PASS.
- Arithmetic verification: PASS. Recomputed `5 || 15 = 3.75 ohm`, `Rth = 8.75 ohm`, open-circuit loop current `I = 1 A`, `Vth = 15 V`, and `15 / 12.75 = 1.176470... A`.
- BEE KB verifier: PASS.
- Global College verifier: PASS.
- Delta ZIP integrity/test-unzip: pending packaging step.

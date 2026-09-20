# BEE Unit I — Exercise 1.8.1 SIMPLER integration

Date: 2026-09-20

## Source workspace

Latest user-supplied `redo.zip` attached for this task.

## Source/resource check

No outside source was used. The existing Exercise 1.8.1 compact solution and NRS redraws Figure 1.50 and Figure 1.50(a)–(c) were used as the source basis.

Visual/semantic checks performed before writing the explainer:

- Figure 1.50: the target 2-ohm resistor is directly between nodes A and B; the circuit contains a 10 V independent voltage source, a 2 A independent current source with upward arrow, and a 20 V independent voltage source.
- Figure 1.50(a): with the 10 V source active, the 2 A source is open-circuited and the 20 V source is short-circuited. The 3-ohm branch is therefore open; the 2-ohm and 5-ohm resistors are series, and that 7-ohm path is parallel with 20 ohms.
- Figure 1.50(b): with the 2 A source active, both voltage sources are short-circuited. The 10-ohm and 20-ohm resistors are parallel; their equivalent is in series with the 2-ohm resistor; the 2 A source injects current upward into node B.
- Figure 1.50(c): with the 20 V source active, the 10 V source is short-circuited and the 2 A source is open-circuited. The 3-ohm branch is open; the 10-ohm and 20-ohm resistors are parallel; current through the 2-ohm resistor is from B to A.
- The existing amber discrepancy note was preserved: the printed source-deactivation wording conflicts with Figures 1.50(a) and (c), and the printed `i3 = -1.434 A` conflicts with the preceding `20/13.66 = 1.464 A` and the printed total `-1.708 A`.

## Change made

Added a nested `SIMPLER` explainer to Exercise 1.8.1 in `kb/data/topics.json` and mirrored the walkthrough into cumulative `kb/notes/unit-1.md`.

The explainer explicitly teaches:

1. how to identify the three independent sources from their symbols;
2. why the 2-ohm A-B branch is the response being tracked;
3. why an ideal voltage source becomes a short circuit and an ideal current source becomes an open circuit when deactivated;
4. how the circuit topology changes in each one-source case;
5. why the 2-ohm and 5-ohm resistors are series in the 10 V-source case;
6. why 20 ohms is parallel with that 7-ohm path;
7. how current division gives `i1`;
8. why `10 || 20` appears in the 2 A-source and 20 V-source cases;
9. why the 2 A source pushes current into node B and makes `i2` flow from B to A;
10. why the 20 V source also makes the 2-ohm current flow from B to A;
11. why the three responses must be added algebraically with direction signs;
12. why the final negative result means the actual current is B to A; and
13. a sanity check comparing the one positive contribution against the two larger negative contributions.

The compact textbook solution, figures and existing amber discrepancy note were not overwritten.

## Arithmetic verification

Using the displayed rounded textbook intermediates:

- `20 || (2 + 5) = 140/27 = 5.185... ohm` -> displayed as `5.18 ohm`.
- `10 + 5.18 = 15.18 ohm`.
- `10/15.18 = 0.65876... A` -> displayed as `0.658 A`.
- `0.658 x 20/27 = 0.4874... A`; using the unrounded upstream current gives about `0.488 A`, consistent with the printed `0.4879 A`.
- `10 || 20 = 200/30 = 6.666... ohm`.
- `2 + 6.66 = 8.66 ohm`.
- `2 x 5/(5 + 8.66) = 0.732... A`.
- `20/(5 + 2 + 6.66) = 20/13.66 = 1.464... A`.
- `0.4879 - 0.732 - 1.464 = -1.7081 A`.
- `(-1.708)(2) = -3.416 V`.

## Verification performed

- `topics.json` parse and target explainer structure: PASS.
- Added-content control-character scan: PASS.
- Added-content display-math delimiter scan: PASS.
- Arithmetic independently recomputed; the SIMPLER follows the textbook's displayed rounded values while preserving the existing printed discrepancy.
- BEE KB verifier: PASS.
- Global College verifier: PASS.
- Delta ZIP integrity/test-unzip: recorded after packaging below.

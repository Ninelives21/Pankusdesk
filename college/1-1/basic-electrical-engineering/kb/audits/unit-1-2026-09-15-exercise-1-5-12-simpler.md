# BEE Unit I — Exercise 1.5.12 SIMPLER integration

Date: 2026-09-15

## Source workspace

Latest user-supplied `/mnt/data/re.zip`, extracted and inspected before editing. The current workspace already contains Exercise 1.5.12, Figure 1.39, and the established nested SIMPLER mechanism used by neighbouring Kirchhoff worked examples.

## Source/resource check

No outside source was needed for the walkthrough. The existing Exercise 1.5.12 entry and Figure 1.39 were the source basis.

Figure 1.39 was visually checked before writing the explainer:

- nodes `a`, `b`, `c`, `d` are labelled;
- a 5 V circular voltage source is on the left, `+` at the top and `−` at the bottom;
- current `i1` is drawn upward in the left branch and therefore through the 2 ohm resistor from `b` to `c`;
- current `i2` is drawn downward through the central 8 ohm branch from `c` to `a`;
- the right branch is labelled `i1-i2` downward;
- the 2 ohm resistor has `+` at `b` and `−` at `c`;
- the 8 ohm resistor has `+` at `c` and `−` at `a`;
- the 4 ohm resistor has `+` at `c` and `−` at `d`;
- a 3 V circular voltage source is on the right, `+` at node `d` and `−` at node `a`.

## Verified source discrepancy

The compact source solution writes the right-loop equation as

`8 i2 - 4(i1-i2) + 3 = 0`.

That sign is inconsistent with the polarity actually drawn in Figure 1.39. Traversing the stated loop `a -> c -> d -> a` crosses the 3 V source from its `+` terminal at `d` to its `−` terminal at `a`, so the source contribution is a 3 V drop:

`8 i2 - 4(i1-i2) - 3 = 0`.

The corrected simultaneous equations are therefore

`2 i1 + 8 i2 = 5`

and

`-4 i1 + 12 i2 = 3`.

They give

- `i1 = 9/14 A ≈ 0.643 A`;
- `i2 = 13/28 A ≈ 0.464 A`;
- right-branch current `i1-i2 = 5/28 A ≈ 0.179 A`;
- `V1 = 9/7 V ≈ 1.286 V`;
- `V2 = 26/7 V ≈ 3.714 V`;
- `V3 = 5/7 V ≈ 0.714 V`.

A node-voltage check confirms the correction: with node `a = 0 V`, the two fixed sources require `Vb = 5 V` and `Vd = 3 V`; the corrected resistor drops give `Vc = 26/7 V`, and `Vc - V3 = 3 V`, exactly matching the right source.

The compact printed working and printed final answer are preserved for source fidelity. An amber discrepancy note identifies the sign problem; the SIMPLER walkthrough uses the corrected equation and values.

## Change made

Added a nested `SIMPLER` explainer to Exercise 1.5.12 in `kb/data/topics.json`, immediately after `Solution:`.

The explainer follows the hand-holding SIMPLER pattern and explicitly explains:

1. how the circular source symbol tells the student these are independent voltage sources;
2. how to read the `+/-` source polarities before writing KVL;
3. why the right branch is `i1-i2` from KCL at node `c`;
4. how the resistor polarity marks correspond to the assumed current directions;
5. every sign in the left-loop KVL equation;
6. why the 3 V term in the right loop is `-3`, using the visible `+/-` marks rather than memorisation;
7. the corrected simultaneous-equation solution;
8. the resistor voltages; and
9. a node-voltage sanity check.

No source figure, current arrow, source polarity, resistor value, compact source working, or printed final answer was overwritten.

## Verification performed

- Figure 1.39 semantic inspection: PASS
- corrected KCL/KVL equations checked independently: PASS
- exact current solution checked: PASS
- resistor-voltage values checked: PASS
- node-voltage consistency check against both independent sources: PASS
- `topics.json` JSON parse: PASS
- added Exercise 1.5.12 SIMPLER/discrepancy control-character scan: PASS
- BEE `verify_kb.py`: PASS
- global `verify_college.py`: PASS

No browser visual-render PASS is claimed unless separately recorded in the handoff.

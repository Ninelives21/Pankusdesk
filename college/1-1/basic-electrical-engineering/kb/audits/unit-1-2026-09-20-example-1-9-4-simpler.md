# BEE Unit I — Example 1.9.4 SIMPLER integration

Date: 2026-09-20

## Source workspace

Latest user-supplied `redo.zip` available in this BEE 7 sequence, with the immediately preceding Example 1.9.3 SIMPLER delta applied first so cumulative work was not regressed.

## Source/resource check

No outside source was used. The existing Example 1.9.4 compact solution and Figures 1.62 and 1.63(a)–(e) were used as the source basis.

Visual/semantic checks performed before writing the explainer:

- Figure 1.62: `R_L` is the load directly between terminals `a` and `b`; the 2 A current source and 12 ohm resistor share the same two nodes and are in parallel.
- Figure 1.63(a): source transformation gives `V = IR = 2 x 12 = 24 V` with the same 12 ohm resistance; the upward current-source arrow corresponds to a voltage source positive at the top.
- Figure 1.63(c): with `R_L` removed, the 1 ohm output branch ends open at `a`, so its current is zero and its voltage drop is zero; the active internal loop is the 32 V source, 4 ohms, 12 ohms and 24 V source.
- The 32 V and 24 V sources oppose in that loop, giving `(32 - 24)/(4 + 12) = 0.5 A`.
- The 12 ohm drop is `6 V`; adding that to the 24 V source level gives `Vth = 30 V`. Cross-check from the other side gives `32 - (0.5 x 4) = 30 V`.
- Figure 1.63(d): after both independent voltage sources are shorted, 4 ohms and 12 ohms share the same two nodes and are parallel; their 3 ohm equivalent is in series with 1 ohm, giving `Rth = 4 ohm`.
- Figure 1.63(e): the same `Vth = 30 V`, `Rth = 4 ohm` equivalent is reused for both load values.

## Change made

Added a nested `SIMPLER` explainer to Example 1.9.4 in `kb/data/topics.json` and mirrored the walkthrough into cumulative `kb/notes/unit-1.md`.

The explainer explicitly teaches:

1. how to identify `R_L` as the load from terminals `a-b`;
2. why the current-source/12-ohm pair is eligible for source transformation;
3. how `V = IR = 24 V` is obtained and how the current arrow fixes the voltage-source polarity;
4. why the 1-ohm branch carries zero current while finding `Vth`;
5. why the 32 V and 24 V sources subtract in the internal loop;
6. how `Vth = 30 V` can be obtained and independently cross-checked from either side;
7. why 4 ohms and 12 ohms become parallel after the voltage sources are shorted;
8. why the 1-ohm resistor is then in series with that parallel equivalent;
9. what the Thevenin replacement buys us for multiple load values; and
10. a sanity check showing that doubling total resistance halves the load current.

The compact textbook solution and figures were not overwritten.

## Verification performed

- `topics.json` parse and target explainer structure: PASS.
- Added-content control-character/LaTeX delimiter scan: PASS.
- Arithmetic verification performed manually: `2 x 12 = 24 V`, `(32 - 24)/(4 + 12) = 0.5 A`, `0.5 x 12 = 6 V`, `24 + 6 = 30 V`, `4 || 12 = 3 ohm`, `Rth = 4 ohm`, `30/(4 + 6) = 3 A`, `30/(4 + 16) = 1.5 A`.
- BEE KB verifier: PASS.
- Global College verifier: PASS.
- Delta ZIP integrity/test-unzip: PASS (exactly one top-level folder; three intended files).

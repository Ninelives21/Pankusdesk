# BEE Unit I — Example 1.9.3 SIMPLER audit — 2026-09-20

## Source workspace

Latest supplied workspace: `redo.zip`, extracted to this working tree.

## Scope of change

Added a hand-holding `SIMPLER` explainer for textbook Example 1.9.3 only. No textbook figures, compact source solution, discrepancy block, navigation, shared UI, styles, or unrelated topics were changed.

## Technical interpretation verified

- The 2-ohm branch between `a` and `b` is the load because the question asks for its current.
- For `R_th`, the 12 V ideal source is shorted. This makes the source's left and right nodes one common node.
- Therefore `4 ohm` and `6 ohm` share the same two end nodes and are parallel; `3 ohm` and `5 ohm` also share the same two end nodes and are parallel.
- `4 || 6 = 2.4 ohm`; `3 || 5 = 1.875 ohm`; therefore `R_th = 4.275 ohm`.
- With the load removed and source restored, the upper branch current is `12/(4+6)=1.2 A` and the lower branch current is `12/(3+5)=1.5 A`.
- From the same left positive node, the drop to `a` is `1.2*4=4.8 V` and the drop to `b` is `1.5*3=4.5 V`.
- Hence `V_ab = V_a - V_b = -0.3 V`; equivalently `V_ba = +0.3 V`.
- The load-current magnitude is `0.3/(4.275+2)=0.047808... A`, approximately `47.8 mA`, and conventional current flows from `b` to `a`.

## Existing source discrepancy preserved

The existing amber discrepancy remains unchanged. It records that the printed solution labels `1.5*3=4.5 V` as a drop across 4 ohms even though it is the 3-ohm drop, and that the printed Thevenin-equivalent treatment uses the magnitude `0.3 V` after obtaining `V_ab=-0.3 V` without preserving the corresponding current direction.

## Files modified

- `college/1-1/basic-electrical-engineering/kb/data/topics.json`
- `college/1-1/basic-electrical-engineering/kb/notes/unit-1.md`
- `college/1-1/basic-electrical-engineering/kb/audits/unit-1-2026-09-20-example-1-9-3-simpler.md`

## Verification

See handoff for the commands actually run and their results.

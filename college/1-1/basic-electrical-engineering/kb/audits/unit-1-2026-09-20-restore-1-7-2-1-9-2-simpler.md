# BEE Unit I — combined SIMPLER restoration for 1.7.2 and 1.9.2

## Source workspace

Latest user-supplied `redo.zip` for this restoration task. This workspace remained the code source of truth.

## Restoration basis

- Example 1.9.2: restored the previously authored SIMPLER content exactly from the earlier 1.9.2 delta available in this session, then merged it into the latest workspace rather than replacing newer files wholesale.
- Exercise 1.7.2: the earlier standalone delta was not available in the active filesystem. The SIMPLER was restored from the established project handoff/context and re-checked against the current Exercise 1.7.2 solution and Figures 1.47(a)–(e) in the latest workspace.

## Exercise 1.7.2 restored content

The restored SIMPLER explains why the 5-ohm, 10-ohm and 20-ohm star centred at node `d` is selected: converting it to a delta creates resistors directly across the existing 12.5-ohm, 15-ohm and 30-ohm branches, producing three immediate parallel reductions. It then shows:

- `R_ac = 17.5 ohm`
- `R_ab = 70 ohm`
- `R_bc = 35 ohm`
- `12.5 || 17.5 ≈ 7.29 ohm`
- `15 || 35 = 10.5 ohm`
- `70 || 30 = 21 ohm`
- `7.29 + 10.5 = 17.79 ohm`
- `17.79 || 21 ≈ 9.63 ohm`
- `i = 120 / 9.63 ≈ 12.46 A`

## Example 1.9.2 restored content

Restored the previously authored walkthrough covering load identification, voltage-source deactivation, `(8+2) || 20`, the meaning of `I1 = -0.8 A`, `Vth = 16 V`, reuse of one Thevenin equivalent for both load values, and the printed `1.65 A` versus ordinary rounding to `1.66 A` note.

## Files modified

- `college/1-1/basic-electrical-engineering/kb/data/topics.json`
- `college/1-1/basic-electrical-engineering/kb/notes/unit-1.md`
- `college/1-1/basic-electrical-engineering/kb/audits/unit-1-2026-09-20-restore-1-7-2-1-9-2-simpler.md`

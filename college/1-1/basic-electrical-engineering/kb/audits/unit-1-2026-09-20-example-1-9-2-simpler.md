# BEE Unit I — Example 1.9.2 SIMPLER integration

## Source workspace

Latest user-supplied `redo.zip` for the 2026-09-20 task.

## Source basis

No outside source was used. The existing Example 1.9.2 compact solution and Figures 1.58 and 1.59(a)–(d) in the current workspace were used as the source basis.

## Change

Added a nested `SIMPLER` explainer to Example 1.9.2 in `kb/data/topics.json` and mirrored the walkthrough into cumulative `kb/notes/unit-1.md`.

The explainer explicitly covers:

- how to identify `R` as the load from terminals `a-b`;
- why the 8 V and 32 V ideal independent voltage sources become short circuits while finding `Rth`;
- why 2 ohms and 8 ohms are series after deactivation, and why their 10-ohm equivalent is parallel with 20 ohms;
- why opening the load makes the terminal load current zero while an internal source-resistor loop still carries current;
- the KVL origin and physical meaning of the textbook result `I1 = -0.8 A`;
- how the signed current gives `Vth = 16 V`;
- why one Thevenin equivalent can then be reused for both `R = 3 ohm` and `R = 8 ohm`;
- sanity checks on polarity and the reduction of current when the load resistance increases.

## Arithmetic/source note

Recomputed independently:

- `(8 + 2) || 20 = 10 || 20 = 20/3 = 6.666... ohm`, consistent with the textbook's `6.66 ohm`;
- `(8 - 32)/(8 + 2 + 20) = -24/30 = -0.8 A`;
- `32 + (-0.8)(20) = 16 V`;
- `16/(6.66 + 3) = 1.656314... A`;
- `16/(6.66 + 8) = 1.091405... A`.

The textbook prints `1.65 A` for the 3-ohm load. That printed value is preserved in the compact textbook solution. The SIMPLER notes that ordinary two-decimal rounding of the displayed values gives `1.66 A`, rather than silently rewriting the source.

## Files modified

- `college/1-1/basic-electrical-engineering/kb/data/topics.json`
- `college/1-1/basic-electrical-engineering/kb/notes/unit-1.md`
- `college/1-1/basic-electrical-engineering/kb/audits/unit-1-2026-09-20-example-1-9-2-simpler.md`

## Verification performed

- JSON parse of `kb/data/topics.json`: PASS.
- Added-content LaTeX/control-character scan: PASS.
- Arithmetic recomputation: PASS.
- BEE KB verifier: PASS.
- Global College verifier for BEE: PASS.
- Delta ZIP integrity and test-unzip: performed after packaging.

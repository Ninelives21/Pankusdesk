# BEE Unit V Short Notes — page flow and figure integration audit
Date: 2026-10-16

## Source workspace
Latest lean `redo.zip` supplied in the task.

## Scope
Unit V Short Notes only. No binary assets were edited or generated.

## Changes
- Moved Figure 4.14 into the domestic-installation supply-path explanation and added a note for reading the layout.
- Expanded wiring visuals to the canonical textbook set used by the in-scope notes: Figures 4.15, 4.16, 4.17 and 4.18, each placed in its matching wiring-method study group.
- Kept Figure 4.23 out of the SFU teaching flow because its current-balance/search-coil mechanism conflicts with the preceding switch-plus-fuse definition. The discrepancy remains explicitly cautioned rather than being silently presented as an SFU mechanism.
- Moved Figure 4.24 into the MCB explanation and added Figure 4.25 beside the bimetal overload explanation.
- Added Figure 4.26 to the explanation of why earthing is needed; moved Figure 4.29 to pipe earthing and Figure 4.30 to plate earthing.
- Moved Figure 4.31 into lead-acid construction, Figure 4.32 into the voltage characteristic and Figure 4.33 into the capacity characteristic.
- Moved Figure 5.44 into the UPS block/roles explanation and connected the diagram to normal-mains and mains-failure operation.
- Removed or softened student-facing source/editorial phrases such as “as stated in the source”, “source examples”, and “for R25” where they were not part of the teaching content.
- Preserved the verified SFU and plate-earthing discrepancies as cautions because they are genuine source issues.

## Figure identities used
- Figure 4.14 — Lay-out of wiring in domestic installations — p. 201
- Figure 4.15 — Cleat wiring — p. 202
- Figure 4.16 — Capping and casing wiring — p. 202
- Figure 4.17 — TRS/CTS wiring — p. 203
- Figure 4.18 — Conduit wiring — p. 203
- Figure 4.24 — Miniature Circuit Breaker (MCB) — p. 206
- Figure 4.25 — Bimetal under normal and abnormal conditions — p. 207
- Figure 4.26 — Effect of not earthing and earthing — p. 208
- Figure 4.29 — Pipe earthing — p. 210
- Figure 4.30 — Plate earthing — p. 210
- Figure 4.31 — Lead-acid battery — p. 211
- Figure 4.32 — Variation in voltage during charging and discharging — p. 213
- Figure 4.33 — Capacity versus discharge characteristics — p. 213
- Figure 5.44 — UPS block diagram — p. 243

## Deliberate non-recommendations
- Figure 4.23 is not promoted as the SFU teaching figure because the source page is internally inconsistent.
- No invented ELCB figure was introduced. The R25 ELCB gap is adequately covered in text from the approved government sources; a diagram was not fabricated merely to fill space.

## Verification
- `short-notes.json` parsed successfully.
- `node --check scripts/new/unit-short-notes.js` passed.
- BEE KB verifier passed: `BEE KB VERIFY: PASS`.
- All Unit-V card-level diagram arrays are empty; every retained/recommended figure is placed inside the study group it explains.
- The lean workspace intentionally omits binary assets, so visual pixel-level inspection of the final redraws was not possible in this pass.

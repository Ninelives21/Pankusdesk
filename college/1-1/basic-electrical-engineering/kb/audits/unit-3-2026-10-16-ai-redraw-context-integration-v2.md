# Unit III Short Notes — AI redraw context integration v2 — 2026-10-16

## Scope
Rework the four active Unit III redraws so each appears immediately inside the concept it explains, with enough surrounding text to decode the labels and understand why the drawing is present.

## Changes
- Figure 3.31 is now embedded inside the construction explanation and is read outside-to-inside: yoke/poles/field system -> armature -> commutator -> brushes.
- Figure 3.26 is now embedded directly in the simple-loop explanation. The notes identify N/S, ABCD, slip rings, brushes, external load R, and explicitly explain M and N as the two external load-side terminals used to state current direction.
- Figure 3.29 is now embedded directly in the commutation explanation and connects coil-emf reversal with simultaneous commutator contact reversal.
- Figure 3.35 is now embedded directly in the EMF-equation derivation and defines one pole pitch before using it to obtain t = 60/(NP).
- Student-facing captions and teaching notes were rewritten as note content rather than implementation/source commentary. Backend figure/page/redraw provenance fields remain available but are not displayed as commentary while the image loads normally.
- The generic Short Notes renderer now permits diagrams inside a study group, allowing explanatory text -> relevant figure -> derivation/formula rather than collecting unrelated figures at the end of the card.

## Verification
- short-notes.json parses successfully.
- scripts/new/unit-short-notes.js passes `node --check`.
- BEE KB verifier: PASS.
- Confirmed the four diagrams are no longer duplicated at card level and are each attached to the intended study group.

## Asset note
The lean workspace intentionally omits binary assets. The four image files themselves were not changed in this pass; the change concerns their placement and the explanatory note text around them.

# Unit IV Short Notes — page-flow and figure integration audit

Date: 2026-10-16

## Scope
Reviewed all seven AI-generated Unit IV Short Notes topics in the latest lean workspace. The pass focused on making figures part of the teaching flow, removing student-facing editorial/source commentary, and improving figure recommendations without inventing textbook figures or technical labels.

## Changes
- Three-phase induction motor construction: moved Figure 4.2 into the phase-wound-rotor explanation and Figure 4.4 into the squirrel-cage explanation; added teaching notes that decode why slip rings permit external resistance and why cage bars do not.
- Induction-motor principle: moved Figure 4.6 beside rotating-magnetic-field theory and added Figure 4.7 beside rotor-torque production.
- Torque-slip characteristics: added Figure 4.8 beside the physical torque explanation and moved Figure 4.9 beside the curve-reading sequence.
- Synchronous generator: added Figure 4.10 as the energy-conversion overview, kept Figure 4.11 with construction, and added Figure 4.12 with the explanation of alternating sinusoidal emf.
- Synchronous-impedance method: added a separate educational OCC/SCC recommendation based on the approved Unit-IV gap sources. The placeholder includes a NPTEL search query and a constrained NRS fallback prompt. It is not represented as a textbook figure.
- Synchronous motor: added a separate educational magnetic-locking recommendation based on the approved NPTEL source. The placeholder includes a search query and constrained NRS fallback prompt. It is not represented as textbook material.
- Stepper motor: moved Figure 4.13 into the variable-reluctance phase-group explanation and linked A-AA, B-BB and C-CC directly to the step sequence.
- Removed student-facing wording such as “R25 types”, “unit source”, “intentionally limited”, and “exam sequence” where it read as editorial/implementation commentary.

## Figure policy
Textbook figure identities, page references and filenames come from the canonical Unit-IV topic data:
- Figure 4.2 — Phase-wound rotor — p. 187
- Figure 4.4 — Squirrel-cage rotor — p. 188
- Figure 4.6 — Production of rotating magnetic field — p. 189
- Figure 4.7 — Stator and rotor fluxes — p. 189
- Figure 4.8 — Stator and rotor fluxes producing torque — p. 195
- Figure 4.9 — Torque-slip characteristics — p. 196
- Figure 4.10 — Synchronous-generator block diagram — p. 197
- Figure 4.11 — Cross-sectional view of synchronous machine — p. 198
- Figure 4.12 — Sinusoidal generated voltage — p. 198
- Figure 4.13 — Cross-sectional view of stepper motor — p. 199

The synchronous-impedance and synchronous-motor study diagrams are PankusDesk educational recommendations because the supplied prescribed-textbook Chapter 4 pages do not contain those R25 topics. Their provenance remains in source_refs.

## Verification
See handoff for commands/results actually run on the packaged workspace.

## Verification results
- `short-notes.json` parsed successfully.
- `node --check scripts/new/unit-short-notes.js` passed.
- BEE KB verifier passed: `BEE KB VERIFY: PASS`.
- Confirmed all Unit-IV figures/recommendations are attached inside the relevant study group rather than left as detached card-level diagrams.
- The lean workspace intentionally omits binary image assets; this pass changes note flow and recommendations only.

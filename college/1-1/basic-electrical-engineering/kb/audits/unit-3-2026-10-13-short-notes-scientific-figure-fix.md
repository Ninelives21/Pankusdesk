# Unit III Short Notes — scientific + figure-alignment fix

Date: 2026-10-13

## Source workspace
Latest user-supplied `redo.zip` for this task.

## Source material inspected
- R25 BEE Unit III scope already mapped in the workspace.
- Prescribed V. Ramesh Babu Chapter 3 source pages from the supplied `unit_3.zip`, especially pp. 149–151, 161–167, 172–173 and 179–183.
- Teacher-shared Unit III SE1 notes already embedded in the workspace; these remain unchanged.
- Solved PYQ emphasis already mapped in `kb/data/pyqs.json`.
- Swinburne gap mapping in `kb/data/source-manifest.json` and `kb/data/topics.json`; the approved institutional lab-manual cross-check identifies IARE Fig. 4.1 as a Swinburne test circuit.

## Changes made
Only the AI-generated Unit III continuation was edited.

### Transformer losses and efficiency
- Expanded the efficiency derivation so it can be reconstructed in an exam.
- Kept the section figure-free because no textbook figure materially improves the short-note objective.

### DC machine construction
- Retained Figure 3.31.
- Restored the exact textbook caption: `Basic Construction of a DC Machine`.
- Added a short teaching note explaining the intended use of the figure.

### DC generator principle and EMF equation
- Explicitly separated the alternating-emf/slip-ring stage from the split-ring commutator stage.
- Retained Figure 3.26 only for the simple-loop/slip-ring stage.
- Added Figure 3.29 `Action of Commutator` for the unidirectional-output explanation.
- Reworked the EMF derivation to follow the textbook's one-pole-pitch route so it aligns with Figure 3.35.
- Changed `terminal generated emf` to `generated armature emf`.
- Added a source-caution note for the page-161 left-hand/right-hand rule wording mismatch.

### DC motor principle and back EMF
- Added Figure 3.42 `Fleming’s Left Hand Rule` for the motor-principle stage.
- Retained Figure 3.44 with its exact caption `Back Emf`.
- Added the source dot/cross current-direction convention to the notes and Figure 3.44 teaching note.

### Separately excited DC motor load characteristics
- Retained Figures 3.52, 3.53 and 3.54 with exact textbook captions.
- Removed speed-regulation formula/text from the short notes because it is outside the explicit R25 atom and the source page contains a prose/formula denominator mismatch.

### Speed control
- Retained Figures 3.56 and 3.58 with exact textbook captions.
- Reworded the armature method to match the textbook implementation: a series control rheostat reduces effective armature voltage.

### Swinburne’s test
- Clarified the no-load test/readings/loss-separation/efficiency-prediction sequence.
- Added a non-textbook educational-diagram placeholder because the prescribed Chapter 3 scan has no matching Swinburne figure.
- Placeholder includes:
  - expected PankusDesk asset path;
  - Google Images search string targeting the approved IARE Fig. 4.1 circuit;
  - fallback AI-generation prompt with a semantic-fidelity warning.
- No Swinburne image asset was generated in this pass.

## Renderer change
`unit-short-notes.js` now supports optional figure-QA metadata:
- `teaching_note`
- `source_label`
- `target_path`
- `search_query`
- `ai_prompt`

These fields are only shown when supplied. Existing textbook-figure placeholders remain compatible.

## Shared-asset policy
No textbook figure was renamed, moved or altered. Existing canonical textbook filenames remain stable. New textbook recommendations use the existing shared Unit III theory path. The Swinburne placeholder points to a separate PankusDesk educational-asset path because no prescribed-textbook figure exists for that topic.

## Verification performed
See handoff for commands/results. Browser visual verification is only claimed if separately recorded after this file was written.

# MAC Unit I — 4 September 2026 shared study UI refactor

## Requested changes

1. Clarify the Gauss–Seidel stopping rule directly after Step 4 using a visibly separate PankusDesk explanatory box.
2. Make class examples use the same accordion pattern as the shared BEE/unit examples: title + complete question visible when closed; opening the same card reveals the solution. No separate clickable “Solution” row.
3. Make the common drawing/LaTeX/accordion look and behaviour project-wide rather than subject-specific.

## Implementation

- Added the 4 September `PankusDesk tip — When do I stop iterating?` block to the dated MAC entry.
- Added shared `scripts/new/study-ui.js` and `styles/new/study-ui.css`.
- Refactored `subject-unit.js`, `unit-class-notes.js`, `unit-questions.js` and legacy/direct `class-log.js` to reuse the shared text/MathJax/figure/accordion layer where applicable.
- Updated all current BEE and MAC unit/question/class-note/class-log shells that use these renderers to load the shared UI layer.
- Extended the class-log schema for the explicit `pankusdesk-tip` block.
- Updated the College Build Standard, Reference Implementation, Notebook Redraw Style and Unit Build Checklist.
- Extended the generic college verifier to require the shared UI layer on study-content shells.

## Verification

- MAC KB VERIFY: PASS
- BEE KB VERIFY: PASS
- COLLEGE VERIFY: PASS

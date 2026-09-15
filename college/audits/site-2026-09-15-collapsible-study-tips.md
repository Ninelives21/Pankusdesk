# PankusDesk shared study-tip dropdown change — 15 September 2026

## Scope

Changed the shared blue `PankusDesk tip` component in `scripts/new/study-ui.js` and `styles/new/study-ui.css` from an always-open advisory box to a collapsed `<details>` dropdown.

## Reason

Blue explanatory/context boxes are useful but can make class-note pages unnecessarily long. The shared component now keeps the label and title visible in the closed state, shows the established `+` affordance, and reveals the detailed content only when opened.

## Global behaviour

Because both `class-log.js` and `unit-class-notes.js` already call `PankuStudyUI.renderTip()`, this shared change propagates to existing and future `pankusdesk-tip` blocks across subjects/semesters without subject-specific renderer forks.

## Design-lock update

Updated `college/COLLEGE_BUILD_STANDARD.md` and `college/REFERENCE_IMPLEMENTATION.md` so future builds preserve this behaviour.

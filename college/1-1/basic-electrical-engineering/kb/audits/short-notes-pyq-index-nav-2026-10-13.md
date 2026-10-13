# BEE indexed navigation pass — 2026-10-13

## Scope

Added the same indexed left-navigation pattern used by unit Text pages to:

- all five Unit Short Notes pages, through the shared `unit-short-notes.js` renderer;
- `pyqs.html`, through the shared `pyqs.js` renderer.

The change is renderer-driven, so no per-unit Short Notes HTML shells needed individual edits.

## Behaviour

- The new sidebar is sticky on desktop and becomes an in-flow index on narrower screens.
- The site-wide Back to top control is placed at the top of the indexed sidebar, matching existing unit-page behaviour.
- The active index entry follows the visible section through `IntersectionObserver`.
- Clicking an index entry updates the URL hash and smoothly scrolls to the selected section.
- Existing deep links continue to work.

### Short Notes indexing

- Teacher-only units index every supplied teacher-note page.
- Mixed Unit III groups teacher-note pages and AI-generated completion topics separately while using one continuous navigation index.
- AI-only Units IV and V index every generated short-note topic.
- The old in-content jump-link blocks and the duplicate bottom Back to top text link are no longer rendered.

### PYQ indexing

- Each paper indexes Part A and Units I–V in the left sidebar.
- The currently selected year query parameter is preserved in section links.
- Year-to-year paper navigation remains unchanged.

## Verification performed

- `node --check` passed for `study-ui.js`, `navbar.js`, `unit-short-notes.js`, and `pyqs.js`.
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py` — PASS.
- `python3 scripts/tools/verify_college.py college/1-1/basic-electrical-engineering` — PASS.
- A headless Chromium screenshot attempt did not complete within the execution window, so browser visual verification is not claimed.

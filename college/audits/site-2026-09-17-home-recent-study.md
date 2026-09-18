# Site audit — homepage Recently Studied automation — 2026-09-17

## Source workspace

Latest user-supplied `re.zip` received 2026-09-17.

## Change

The root homepage no longer contains manually maintained recent-study cards.

`scripts/new/home.js` now reads the current semester calendar/class log from:

`college/<semester-id>/data/class-log.json`

It selects the latest linked dated class-note entry for each distinct subject, sorts by date descending, and renders up to three cards. Each card links directly to the dated class-note anchor already stored in the calendar entry.

If fewer than three subjects have linked class notes, fewer cards are rendered; stale unlinked entries are not used as filler.

As a result, adding a new dated class note and updating the canonical semester class log automatically updates the homepage. No separate homepage edit is required.

## Current expected homepage output from the supplied workspace

1. 16 September — Matrices and Calculus — Unit II — link to `unit-2-class-notes.html#2026-09-16`
2. 11 September — Basic Electrical Engineering — Unit I — link to `unit-1-class-notes.html#2026-09-11`

No third card is rendered because no third subject currently has a linked dated class-note entry in the canonical semester log.

## Verification performed

- `node --check scripts/new/home.js` — PASS
- `python3 scripts/tools/verify_college.py` — `COLLEGE VERIFY: PASS`
- Confirmed the selection algorithm returns the two expected latest distinct linked subjects above.
- Confirmed the old static 12 August homepage cards were removed from `index.html`.

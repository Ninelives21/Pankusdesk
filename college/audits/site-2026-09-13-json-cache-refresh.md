# PankusDesk — JSON cache refresh hardening

Date: 2026-09-13

## Source workspace

User-supplied latest workspace: `/mnt/data/re.zip`.

## Problem addressed

GitHub Pages could successfully deploy a new cumulative `topics.json`, while a browser normal refresh could continue to render an older cached JSON response. A hard refresh exposed the newly deployed content, confirming that the repository/deployment was current but the browser-side data fetch could be stale.

## Change

Updated every mutable JSON loader in the shared `scripts/new/` application layer to fetch JSON with:

```js
fetch(url, { cache: 'no-store' })
```

or the equivalent `path` form.

Files changed:

- `scripts/new/subject-unit.js`
- `scripts/new/subject-home.js`
- `scripts/new/semester-home.js`
- `scripts/new/unit-questions.js`
- `scripts/new/unit-class-notes.js`
- `scripts/new/calendar.js`
- `scripts/new/semester-context.js`

`navbar.js` was intentionally left unchanged because its fetch is for the shared HTML navbar fragment, not mutable JSON study data.

## Intended behaviour

Normal page loads/reloads now re-request mutable JSON instead of satisfying those requests from the browser HTTP cache. Static assets such as images, CSS, JavaScript, and the navbar HTML retain their existing caching behaviour.

This is a global PankusDesk infrastructure change and is not specific to BEE.

## Verification performed

- Enumerated all `fetch()` calls under `scripts/new/`.
- Confirmed all JSON-loading fetches now specify `cache: 'no-store'`.
- Confirmed the only remaining plain fetch is `scripts/new/navbar.js` for `navbar_new.html`.
- `node --check` passed for all seven modified JavaScript files.
- `python scripts/tools/verify_college.py`: PASS.

No browser visual-render pass is claimed.

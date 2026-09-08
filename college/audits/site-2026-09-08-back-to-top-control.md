# Site-wide Back to top control — 2026-09-08

- Added one shared Back to top control in `scripts/new/navbar.js`; no subject/unit-specific copies.
- On long study pages with `.unit-toc` or `.class-notes-toc`, the control is mounted as the first item at the top of the left navigation and stays sticky within that navigation on desktop.
- On narrower layouts (where the left navigation stops being sticky) the same control becomes a compact floating bottom-right action after the user scrolls down.
- On pages without a supported left navigation, the same shared control appears as a floating bottom-right action after scrolling.
- Smooth scrolling respects `prefers-reduced-motion`.
- Styling is shared through `styles/new/navbar.css`, which is already loaded by every current college HTML shell.

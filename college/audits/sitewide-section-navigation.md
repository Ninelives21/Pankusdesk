# Shared current-reading navigation

## User-visible contract

Every same-document contents menu highlights the section currently being read. The current section changes when the next linked target crosses a reading line 20% down the viewport (clamped to 96–180 pixels). A long section retains selection until the next linked section reaches that line. Nested sections select the most recently reached target, and a short final section can become selected at the bottom of a scrollable page.

The tracker marks matching links with `aria-current="location"`, `is-current-section` and the existing `is-active` compatibility class. It never changes the URL, hash, history, content visibility, or the reading viewport on scroll. Click handlers retain the existing page-specific routing, answer opening, hidden-paper selection, smooth scrolling and mobile collapse behaviour. Links to another pathname/query/origin and links marked `aria-current="page"` are not reading-location links.

## Central integration and coverage

`scripts/new/navbar.js` imports `section-navigation.js` once through the shared site entry point. The new component discovers semantic `nav` elements and existing contents containers, matching their anchors to existing content IDs. All 80 full browsing pages in this checkout load that navbar entry point and `styles/new/navbar.css`. No individual HTML page or page builder needs a new script tag. The remaining HTML files are fragments or a legacy redirect, not additional independent navigation layouts. Resources on an external legacy site are not part of this checkout.

The implementation ignores global headers/footers, breadcrumbs, return-to-top controls, disabled links, malformed fragments, invisible targets and descendants of closed answer disclosures. Fragment-only links are matched to the current document even when the page uses a site-root `<base>`; absolute and relative links must match the actual pathname and query, including the GitHub Pages `/Pankusdesk/` prefix.

Shared renderer adapters now request `window.PankuSectionNav?.refresh()` instead of maintaining competing `aria-current="location"` loops or intersection observers. Adapters retain their navigation and content-loading responsibilities. `PankuStudyUI.initIndexedNav` still provides its click handling and compatible `setActive` entry point; `setActive` schedules a reading-position refresh and its old local observer is now null. The unrelated textbook lazy-figure observer remains unchanged.

For a future custom layout, use a semantic `nav` with same-document anchor links, or add `data-section-nav` to its contents container. Use `data-section-nav="off"` to explicitly exclude a menu. The shared stylesheet defines the current-section treatment once; existing layout and mobile styles remain in place.

## Dynamic content and mobile behaviour

One passive scroll listener schedules a single animation-frame update. Target/link discovery is cached between DOM changes. Mutation, body resize, image load, font readiness, answer disclosure, viewport resize, history navigation and renderer refresh requests update the selection after layout changes. No model, API, dependency or runtime service is introduced.

The tracker expands nested unit/topic disclosures inside a contents menu so the active entry is reachable. It does not open an outer mobile Contents panel. It scrolls only an independently scrollable contents container when necessary, not the page. Same-target duplicate links in a menu share the reading-location highlight; unrelated page-navigation state is preserved.

## Verification

`python3 scripts/tools/check_section_navigation_browser.py --screenshots <scratch-directory>` starts an ephemeral loopback server for this checkout and runs installed Playwright/Chromium. It checks the shared bootstrap/style coverage, long/nested/hidden/dynamically loaded sections, expansion-driven layout changes, a short last section, exclusion of other pages/queries, unchanged scroll URL/history, native click/Back/Forward, nested group opening and preservation of a collapsed outer menu. It also verifies real teacher notes, textbook topics, dated and supplied notes, MAC/PPS worksheets, PPS exam questions, source notes, filtered Chemistry banks and institutional documents at desktop and phone widths, plus a simulated GitHub Pages prefix. Existing college/BEE/MAC and relevant Chemistry validators remain applicable.

Browser tests do not certify academic content. No source content, diagrams, publication states, page HTML, deployment settings or links are changed by this feature.

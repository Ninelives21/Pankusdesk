/* One scroll tracker for same-document contents menus, loaded by the shared navbar. */
(function () {
'use strict';
if (window.PankuSectionNav) return;
const ROOTS = 'nav, [data-section-nav], .end-sem-nav, .study-index-nav, .class-notes-toc, .unit-toc, .source-notes-nav, .worksheet-nav, .programming-nav';
const EXCLUDED = '#navbar-new, header, footer, .breadcrumbs, .breadcrumb, [aria-label="Breadcrumb"], [data-section-nav="off"]';
const RETURN_LINKS = '.back-to-top-control, .document-back-top, .source-notes-top, [aria-disabled="true"], [download]';
let groups = [];
let dirty = true;
let frame = 0;

function schedule(rebuild = false) {
    dirty ||= rebuild;
    if (!frame) frame = requestAnimationFrame(update);
}

function entry(link) {
    if (link.matches(RETURN_LINKS) || link.getAttribute('aria-current') === 'page') return null;
    const raw = link.getAttribute('href');
    if (!raw) return null;
    try {
        // A <base href="/"> must not redirect a fragment-only contents link to home.
        const url = new URL(raw, raw.startsWith('#') ? location.href : document.baseURI);
        if (url.origin !== location.origin || url.pathname !== location.pathname || url.search !== location.search) return null;
        const id = link.dataset.indexTarget || decodeURIComponent(url.hash.slice(1));
        const target = id && document.getElementById(id);
        if (!target || target === document.body || target === document.documentElement) return null;
        if (/^(?:document|exam|page|worksheet)-top$/.test(id)) return null;
        return { link, target, id };
    } catch (_) { return null; }
}

function collect() {
    // Prefer the innermost semantic menu; don't register an enclosing aside twice.
    const roots = [...document.querySelectorAll(ROOTS)].filter(root =>
        !root.closest(EXCLUDED) && !root.querySelector(ROOTS));
    const previous = new Map(groups.map(group => [group.root, group.current]));
    const oldLinks = new Set(groups.flatMap(group => group.items.map(item => item.link)));
    groups = roots.map(root => ({ root, current: previous.get(root), items: [...root.querySelectorAll('a[href]')].map(entry).filter(Boolean) }))
        .filter(group => group.items.length);
    for (const group of groups) {
        group.root.setAttribute('data-section-nav', '');
        for (const item of group.items) oldLinks.delete(item.link);
    }
    for (const link of oldLinks) clear(link);
    dirty = false;
}

function clear(link) {
    link.classList.remove('is-current-section', 'is-active');
    if (link.getAttribute('aria-current') === 'location') link.removeAttribute('aria-current');
}

function visible(target) {
    if (!target.isConnected || target.closest('[hidden], [inert]')) return false;
    // Closed answer descendants can still expose stale rectangles in some browsers.
    for (let parent = target.parentElement; parent; parent = parent.parentElement) {
        if (parent.tagName === 'DETAILS' && !parent.open && !parent.querySelector(':scope > summary')?.contains(target)) return false;
    }
    return target.getClientRects().length > 0 && getComputedStyle(target).visibility !== 'hidden';
}

function showInMenu(item, root) {
    // Open nested units/topic groups, never the outer mobile Contents disclosure.
    for (let parent = item.link.parentElement; parent && parent !== root; parent = parent.parentElement) {
        if (parent.tagName === 'DETAILS' && !parent.open) parent.open = true;
    }
    if (!item.link.getClientRects().length) return;
    for (let parent = item.link.parentElement; parent; parent = parent.parentElement) {
        const style = getComputedStyle(parent);
        if (/(auto|scroll)/.test(style.overflowY) && parent.scrollHeight > parent.clientHeight) {
            const box = parent.getBoundingClientRect();
            const linkBox = item.link.getBoundingClientRect();
            if (linkBox.top < box.top + 8) parent.scrollTop -= box.top + 8 - linkBox.top;
            else if (linkBox.bottom > box.bottom - 8) parent.scrollTop += linkBox.bottom - box.bottom + 8;
            break;
        }
        if (parent === document.body) break;
    }
}

function update() {
    frame = 0;
    if (dirty) collect();
    // The heading changes selection at a stable reading line below the site header.
    const line = Math.max(96, Math.min(180, innerHeight * 0.2));
    const atEnd = scrollY > 0 && scrollY + innerHeight >= document.documentElement.scrollHeight - 2;
    for (const group of groups) {
        const positioned = group.items.filter(item => visible(item.target)).map(item => ({ ...item, box: item.target.getBoundingClientRect() }));
        positioned.sort((a, b) => a.box.top - b.box.top || (a.target === b.target ? 0 : a.target.compareDocumentPosition(b.target) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1));
        const passed = positioned.filter(item => item.box.top <= line);
        let selected = passed.at(-1) || positioned.find(item => item.box.top < innerHeight);
        if (atEnd) selected = positioned.filter(item => item.box.top < innerHeight && item.box.bottom > 0).at(-1) || selected;
        for (const item of group.items) {
            const active = selected && item.target === selected.target;
            if (active) {
                if (!item.link.classList.contains('is-current-section')) item.link.classList.add('is-current-section');
                if (!item.link.classList.contains('is-active')) item.link.classList.add('is-active');
                if (item.link.getAttribute('aria-current') !== 'location') item.link.setAttribute('aria-current', 'location');
            } else clear(item.link);
        }
        if (selected && group.current !== selected.link) {
            group.current = selected.link;
            showInMenu(selected, group.root);
        } else if (!selected) group.current = null;
    }
}

window.PankuSectionNav = { refresh: () => schedule(true) };
function start() {
    new MutationObserver(records => {
        // Ignore our own highlight classes, but notice renderer visibility classes.
        const meaningful = records.some(record => {
            if (record.attributeName !== 'class' || record.target.tagName !== 'A') return true;
            const withoutHighlight = value => (value || '').split(/\s+/)
                .filter(name => name && !['is-active', 'is-current-section'].includes(name)).sort().join(' ');
            return withoutHighlight(record.oldValue) !== withoutHighlight(record.target.getAttribute('class'));
        });
        if (meaningful) schedule(true);
    }).observe(document.body, {
        childList: true, subtree: true, attributes: true, attributeOldValue: true,
        attributeFilter: ['hidden', 'inert', 'open', 'href', 'id', 'style', 'class'],
    });
    if ('ResizeObserver' in window) new ResizeObserver(() => schedule()).observe(document.body);
    addEventListener('scroll', () => schedule(), { passive: true });
    addEventListener('resize', () => schedule());
    addEventListener('hashchange', () => schedule(true));
    addEventListener('popstate', () => schedule(true));
    addEventListener('pageshow', () => schedule(true));
    document.addEventListener('toggle', () => schedule(), true);
    document.addEventListener('load', () => schedule(), true);
    // Run after each renderer's click handler, without altering navigation/history.
    document.addEventListener('click', () => schedule(), true);
    document.fonts?.ready.then(() => schedule());
    schedule(true);
}
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
else start();
})();

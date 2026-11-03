(function () {
  'use strict';
  const root = document.querySelector('.end-sem-content');
  if (!root || !window.PankuStudyUI) return;
  const ui = window.PankuStudyUI;
  const navGroups = [...document.querySelectorAll('.source-nav-group')];
  navGroups.forEach(group => group.addEventListener('toggle', () => {
    if (group.open) navGroups.forEach(other => { if (other !== group) other.open = false; });
  }));
  function revealCurrentTopic() {
    let currentLink = null;
    navGroups.forEach(group => {
      group.querySelectorAll('a').forEach(link => {
        const current = Boolean(location.hash) && link.hash === location.hash;
        if (current) {
          group.open = true;
          link.setAttribute('aria-current', 'location');
          currentLink = link;
        } else link.removeAttribute('aria-current');
      });
    });
    if (currentLink) requestAnimationFrame(() => {
      const nav = currentLink.closest('.end-sem-nav');
      const linkBox = currentLink.getBoundingClientRect();
      const navBox = nav.getBoundingClientRect();
      if (linkBox.top < navBox.top + 12) nav.scrollTop += linkBox.top - navBox.top - 12;
      else if (linkBox.bottom > navBox.bottom - 12) nav.scrollTop += linkBox.bottom - navBox.bottom + 12;
    });
  }
  revealCurrentTopic();
  window.addEventListener('hashchange', revealCurrentTopic);
  ui.initAccordions(root);
  // A lossless source panel may need its native size for small labels.
  root.querySelectorAll('.source-visual img').forEach(img => {
    const link = document.createElement('a');
    link.href = img.src;
    link.target = '_blank';
    link.rel = 'noopener';
    link.setAttribute('aria-label', `Open full-size image: ${img.alt}`);
    img.replaceWith(link);
    link.append(img);
  });
  ui.typesetMath(root).then(() => {
    if (location.hash) document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView();
  }).catch(() => {
    const notice = document.createElement('p');
    notice.setAttribute('role', 'status');
    notice.textContent = 'Equation rendering is unavailable. Reload to retry; the source notes and original images remain available.';
    root.prepend(notice);
  });
})();

/* Source-backed, undated slide notes; common figures and examples use PankuStudyUI. */
(function () {
'use strict';
const content = document.getElementById('source-notes-content');
const nav = document.getElementById('source-notes-nav');
const menu = document.querySelector('.source-notes-nav');
const source = document.body.dataset.sourceNotes;
if (!content || !nav || !source) return;
const ui = window.PankuStudyUI;
const esc = ui.escapeHtml;
const narrow = window.matchMedia('(max-width: 760px)');
function fitMenu() { menu.open = !narrow.matches; }
fitMenu();
narrow.addEventListener('change', fitMenu);
function revealHash() {
	let id;
	try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
	const target = document.getElementById(id);
	if (!target || !content.contains(target)) return;
	if (target.matches('details')) target.open = true;
	nav.querySelectorAll('a').forEach(link => {
		if (link.hash === location.hash) link.setAttribute('aria-current', 'location');
		else link.removeAttribute('aria-current');
	});
	requestAnimationFrame(() => target.scrollIntoView({ block: 'start' }));
}
nav.addEventListener('click', event => {
	if (!event.target.closest('a')) return;
	if (narrow.matches) menu.open = false;
	// Re-selecting the current problem should reopen it after manual closure.
	if (event.target.closest('a').hash === location.hash) revealHash();
});
window.addEventListener('hashchange', revealHash);
fetch(new URL(source, document.baseURI))
	.then(response => { if (!response.ok) throw new Error('Notes could not be loaded.'); return response.json(); })
	.then(data => {
		nav.innerHTML = `<a href="${esc(location.pathname)}#" class="source-notes-top">Back to top ↑</a>` + data.sections.map(section =>
			`<a class="source-notes-heading" href="${esc(location.pathname)}#${esc(section.id)}">${esc(section.title)}</a>` +
			(section.examples || []).map(item => `<a class="source-notes-child" href="${esc(location.pathname)}#${esc(item.id)}">${esc(item.nav_title || item.title)}</a>`).join('')
		).join('');
		content.innerHTML = data.sections.map(section => `<section class="source-notes-section" id="${esc(section.id)}">
			<h2>${esc(section.title)}</h2>
			${(section.paragraphs || []).map(text => `<p>${ui.formatText(text)}</p>`).join('')}
			${(section.figures || []).map(figure => ui.renderFigure(figure)).join('')}
			${ui.renderAccordionGroup({label: 'Worked projection problems', isExampleGroup: true, items: section.examples || []})}
		</section>`).join('');
		content.querySelectorAll('figure').forEach(figure => {
			const img = figure.querySelector('img');
			if (!img) return;
			const link = document.createElement('a');
			link.href = img.src;
			link.target = '_blank';
			link.rel = 'noopener';
			link.className = 'source-notes-image-link';
			link.textContent = 'Open image at original size ↗';
			link.setAttribute('aria-label', `Open image at original size: ${img.alt}`);
			figure.append(link);
			img.addEventListener('error', () => {
				const error = document.createElement('p');
				error.textContent = 'This image could not be loaded. Please use the original PDF linked above.';
				figure.append(error);
			}, {once: true});
		});
		ui.initAccordions(content);
		content.setAttribute('data-notes-ready', '');
		revealHash();
		ui.typesetMath(content).catch(() => {});
	})
	.catch(error => { content.textContent = `${error.message} You can still open the original PDF above.`; });
}());

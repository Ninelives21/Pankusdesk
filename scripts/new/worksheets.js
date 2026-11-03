/* College worksheet adapter. Shared study UI owns accordions, indexed navigation and mathematics. */
(function () {
'use strict';
document.addEventListener('DOMContentLoaded', init);
async function init() {
	const page = document.querySelector('[data-worksheet-index]');
	if (!page) return;
	const ui = window.PankuStudyUI;
	const escape = ui.escapeHtml;
	const nav = page.querySelector('[data-worksheet-nav]');
	const content = page.querySelector('[data-worksheet-content]');
	try {
		const indexUrl = new URL(page.dataset.worksheetIndex, document.baseURI);
		const indexResponse = await fetch(indexUrl, { cache: 'no-store' });
		if (!indexResponse.ok) throw new Error(`Worksheet index returned ${indexResponse.status}`);
		const index = await indexResponse.json();
		const worksheetId = new URLSearchParams(location.search).get('worksheet') || page.dataset.worksheetId;
		const entry = index.worksheets.find(item => item.id === worksheetId);
		if (!entry) throw new Error('This worksheet is not registered.');
		const sheetUrl = new URL(entry.href, indexUrl);
		const sheetResponse = await fetch(sheetUrl, { cache: 'no-store' });
		if (!sheetResponse.ok) throw new Error(`Worksheet returned ${sheetResponse.status}`);
		const sheet = await sheetResponse.json();
		const title = entry.title || sheet.title;
		page.querySelector('h1').textContent = title;
		page.querySelector('[data-worksheet-breadcrumb]').textContent = title;
		document.title = `${title} · MAC · Panku's Desk`;
		const pagePath = location.pathname + location.search;
		const units = [...new Set(sheet.groups.map(group => group.unit))];
		const roman = ['','I','II','III','IV','V'];
		nav.innerHTML = units.map(unit => `<section class="worksheet-nav-unit" aria-labelledby="worksheet-nav-unit-${unit}">
			<h3 id="worksheet-nav-unit-${unit}">Unit ${escape(roman[unit] || unit)}</h3>
			${sheet.groups.filter(group => group.unit === unit).map(group => `<a class="study-index-link" data-index-target="${escape(group.id)}" href="${escape(pagePath)}#${escape(group.id)}">${escape(group.title)}</a>`).join('')}
		</section>`).join('');
		content.innerHTML = `<section id="${escape(sheet.id)}">
			<p>${escape(sheet.source.note)}</p>
			<p><a href="${escape(new URL(sheet.source.href, sheetUrl).href)}">Open original worksheet PDF ↗</a></p>
			<p class="worksheet-legend">Amber question numbers identify Unit III and Unit IV questions. Numbering restarts in each original question set.</p>
			${sheet.groups.map(group => `<section class="worksheet-group${[3,4].includes(group.unit) ? ' worksheet-group--focus' : ''}" id="${escape(group.id)}"><h2>Unit ${escape(roman[group.unit] || group.unit)} · ${escape(group.title)}</h2>${ui.renderAccordionGroup({label:'Questions',isExampleGroup:true,items:group.questions.map(question => ({...question,title:`Q${question.number}`}))})}</section>`).join('')}
		</section>`;
		ui.initAccordions(content);
		const indexedNav = ui.initIndexedNav(page, { navSelector: '[data-worksheet-nav]' });
		// Long question sets can span many viewports. Keep their nav item active
		// while reading inside the section, including direct links to an answer.
		const sections = Array.from(content.querySelectorAll('.worksheet-group'));
		let scrollFrame = null;
		function syncActiveSection() {
			scrollFrame = null;
			const current = sections.filter(section => section.getBoundingClientRect().top <= 150).at(-1) || sections[0];
			if (current) indexedNav?.setActive(current.id);
		}
		window.addEventListener('scroll', () => {
			if (scrollFrame === null) scrollFrame = requestAnimationFrame(syncActiveSection);
		}, { passive: true });
		const contentsPanel = page.querySelector('.worksheet-nav');
		if (window.matchMedia('(max-width: 700px)').matches) contentsPanel.open = false;
		nav.addEventListener('click', event => {
			const link = event.target.closest('.study-index-link');
			if (link && window.matchMedia('(max-width: 700px)').matches) {
				contentsPanel.open = false;
				requestAnimationFrame(() => document.getElementById(link.dataset.indexTarget)?.scrollIntoView({ block: 'start' }));
			}
		});
		function reveal() {
			let id;
			try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
			const target = id && document.getElementById(id);
			if (!target || !content.contains(target)) return;
			if (target.matches('details')) target.open = true;
			const group = target.closest('.worksheet-group');
			if (group) indexedNav?.setActive(group.id);
			target.scrollIntoView({block:'start'});
		}
		window.addEventListener('hashchange', reveal);
		try { await ui.typesetMath(content); }
		catch (error) {
			console.error('Worksheet mathematics:', error);
			const notice = document.createElement('p');
			notice.className = 'worksheet-notice';
			notice.textContent = 'Mathematics could not be typeset. Reload when online; the question text and solutions remain available.';
			content.prepend(notice);
		}
		reveal();
		page.dataset.worksheetReady = 'true';
	} catch (error) {
		console.error('Worksheets:',error);
		nav.textContent = 'Contents unavailable.';
		content.textContent = 'This worksheet could not be loaded. Please return to MAC study resources or reload to try again.';
	}
}
})();

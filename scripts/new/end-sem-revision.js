(function () {
	'use strict';
	const root = document.querySelector('[data-revision]');
	if (!root) return;
	const ui = window.PankuStudyUI;
	const text = value => ui.formatText(value);
	const paragraphs = values => (values || []).map(value => `<p>${text(value)}</p>`).join('');
	async function load() {
		const response = await fetch(root.dataset.revision);
		if (!response.ok) throw new Error('Revision notes could not be loaded.');
		const data = await response.json();
		const nav = document.querySelector('[data-revision-nav]');
		nav.innerHTML = data.sections.map(section => `<a href="${ui.escapeHtml(location.pathname + location.search)}#${ui.escapeHtml(section.id)}">${text(section.title)}</a>`).join('');
		root.innerHTML = `<p class="revision-status">${text(data.intro)}</p>` + data.sections.map(section => {
			const tables = (section.tables || []).map(table => `<div class="revision-table"><table><caption>${text(table.caption)}</caption><thead><tr>${table.headers.map(h => `<th scope="col">${text(h)}</th>`).join('')}</tr></thead><tbody>${table.rows.map(row => `<tr>${row.map(cell => `<td>${text(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`).join('');
			const questions = (section.question_groups || []).map(group => `<h3>${text(group.title)}</h3><ol class="revision-questions">${group.items.map(item => `<li id="${ui.escapeHtml(item.id)}" value="${Number(item.number)}">${paragraphs(item.paragraphs)}</li>`).join('')}</ol>`).join('');
			return `<section class="revision-section" id="${ui.escapeHtml(section.id)}"><h2>${text(section.title)}</h2>${paragraphs(section.paragraphs)}${tables}${(section.figures || []).map(figure => ui.renderFigure(figure)).join('')}${(section.formulas || []).map(formula => `<div class="revision-equation">${text(formula)}</div>`).join('')}${(section.notes || []).map(note => `<aside class="revision-note">${text(note)}</aside>`).join('')}${ui.renderAccordionGroup({label: 'Supplied numerical problems', isExampleGroup: true, items: section.examples || []})}${questions}</section>`;
		}).join('');
		ui.initAccordions(root);
		await ui.typesetMath(root);
		// Sections arrive asynchronously; restore deep links after they exist.
		if (location.hash) document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView();
	}
	load().catch(error => {
		const message = document.createElement('p');
		message.setAttribute('role', 'alert');
		message.textContent = `${error.message} Please reload this page. If equations are unavailable, the notes remain readable below.`;
		root.prepend(message);
	});
})();

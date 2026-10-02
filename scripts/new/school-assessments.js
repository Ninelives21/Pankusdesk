(function () {
'use strict';

function escapeHtml(value) {
	return String(value ?? '')
		.replaceAll('&', '&amp;')
		.replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;')
		.replaceAll("'", '&#039;');
}

function renderScan(image, alt, kind) {
	if (!image?.src) return '';
	const width = Number(image.width);
	const height = Number(image.height);
	const dimensions = Number.isFinite(width) && Number.isFinite(height)
		? ` width="${width}" height="${height}"`
		: '';
	return `<img class="school-scan school-scan--${kind}" src="${escapeHtml(image.src)}" alt="${escapeHtml(alt)}" loading="lazy" decoding="async"${dimensions}>`;
}

function renderItem(item, group) {
	const qAlt = `${group.topic}, Example ${item.example}, textbook page ${item.bookPage}: question.`;
	const sAlt = `${group.topic}, Example ${item.example}, textbook page ${item.bookPage}: worked textbook solution.`;
	return `
		<article class="school-question-card" id="${escapeHtml(item.id)}">
			<div class="school-question-meta">
				<span class="school-example-badge">Example ${escapeHtml(item.example)}</span>
				<span>Book p. ${escapeHtml(item.bookPage)}</span>
			</div>
			<div class="school-question-scan" aria-label="Question">
				${(item.questionImages || []).map(img => renderScan(img, qAlt, 'question')).join('')}
			</div>
			<details class="school-solution">
				<summary>
					<span>Show textbook solution</span>
					<span class="school-solution-toggle" aria-hidden="true">+</span>
				</summary>
				<div class="school-solution-body">
					${(item.solutionImages || []).map((img, index) => renderScan(img, `${sAlt} Part ${index + 1}.`, 'solution')).join('') || '<p class="school-scan-missing">Solution crop unavailable in source.</p>'}
				</div>
			</details>
		</article>`;
}

function renderGroup(group) {
	return `
		<details class="school-range" id="${escapeHtml(group.id)}">
			<summary class="school-range-summary">
				<span>
					<strong>${escapeHtml(group.label)}</strong>
					<small>${escapeHtml(group.topic)}</small>
				</span>
				<span class="school-range-count">${escapeHtml(group.count)} ${group.count === 1 ? 'question' : 'questions'}</span>
			</summary>
			<div class="school-range-body">
				${group.note ? `<p class="school-range-note">${escapeHtml(group.note)}</p>` : ''}
				<div class="school-question-list">
					${(group.items || []).map(item => renderItem(item, group)).join('')}
				</div>
			</div>
		</details>`;
}

function renderUnit(unit) {
	const count = (unit.groups || []).reduce((sum, group) => sum + Number(group.count || 0), 0);
	return `
		<section class="section school-unit" id="se1-unit-${escapeHtml(unit.number)}">
			<div class="section-heading-row school-unit-heading">
				<div>
					<div class="eyebrow">SE 1 · Unit ${escapeHtml(unit.number)}</div>
					<div class="section-title">${escapeHtml(unit.title)}</div>
				</div>
				<span class="school-unit-count">${count} questions</span>
			</div>
			<div class="school-range-list">
				${(unit.groups || []).map(renderGroup).join('')}
			</div>
		</section>`;
}

function renderPage(data) {
	const a = data.assessment || {};
	const units = Array.isArray(data.units) ? data.units : [];
	const total = units.reduce((sum, unit) => sum + (unit.groups || []).reduce((s, g) => s + Number(g.count || 0), 0), 0);
	const ranges = units.reduce((sum, unit) => sum + (unit.groups || []).length, 0);
	const ref = a.reference || {};
	return `
		<div class="breadcrumbs">
			<a href="index.html">Panku's Desk</a><span>›</span>
			<a href="college/1-1/index.html">Semester 1.1</a><span>›</span>
			<a href="college/1-1/basic-electrical-engineering/index.html">BEE</a><span>›</span>
			<span>School &amp; Exam Guidance</span>
		</div>

		<section class="school-hero" id="se1-2026">
			<div>
				<div class="school-source-badge">${escapeHtml(a.label || 'School recommended')}</div>
				<div class="eyebrow">Basic Electrical Engineering · ${escapeHtml(a.timing || 'Assessment preparation')}</div>
				<h1>${escapeHtml(a.title || 'SE 1 · Recommended Questions')}</h1>
				<p>${escapeHtml(a.description || '')}</p>
				<div class="school-hero-stats" aria-label="Question-set summary">
					<div><strong>${total}</strong><span>worked examples</span></div>
					<div><strong>${units.length}</strong><span>units</span></div>
					<div><strong>${ranges}</strong><span>school-listed blocks</span></div>
				</div>
			</div>
			<aside class="school-reference-card">
				<div class="tool-label">Reference used for solutions</div>
				<strong>${escapeHtml(ref.title || '')}</strong>
				<p>${escapeHtml(ref.edition || '')} · ${escapeHtml(ref.author || '')}</p>
				<p>${escapeHtml(ref.publisher || '')}</p>
				<p class="school-isbn">ISBN ${escapeHtml(ref.isbn || '')}</p>
			</aside>
		</section>

		<section class="school-guidance-note" aria-label="How this list was mapped">
			<strong>How the school sheet is represented here</strong>
			<p>${escapeHtml(a.interpretationNote || '')}</p>
		</section>

		<nav class="school-unit-jump" aria-label="Jump to SE 1 unit">
			${units.map(unit => {
				const count = (unit.groups || []).reduce((sum, group) => sum + Number(group.count || 0), 0);
				return `<a href="#se1-unit-${escapeHtml(unit.number)}"><span>Unit ${escapeHtml(unit.number)}</span><small>${count}</small></a>`;
			}).join('')}
		</nav>

		${units.map(renderUnit).join('')}
		<a class="back-to-top" href="#se1-2026">Back to SE 1 top ↑</a>`;
}

async function init() {
	const main = document.querySelector('.school-assessment-page');
	if (!main) return;
	const path = main.dataset.schoolJson;
	if (!path) return;
	try {
		const response = await fetch(path);
		if (!response.ok) throw new Error(`HTTP ${response.status}`);
		const data = await response.json();
		main.innerHTML = renderPage(data);
		if (window.location.hash) {
			requestAnimationFrame(() => document.querySelector(window.location.hash)?.scrollIntoView());
		}
	} catch (error) {
		main.innerHTML = `<div class="school-error">Could not load the school-recommended question set. ${escapeHtml(error.message)}</div>`;
	}
}

document.addEventListener('DOMContentLoaded', init);
})();

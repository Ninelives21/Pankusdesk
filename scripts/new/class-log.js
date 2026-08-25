(function () {
'use strict';

document.addEventListener('DOMContentLoaded', initClassLog);

async function initClassLog() {
	const page = document.querySelector('.class-log-page[data-subject-json]');
	if (!page) return;

	try {
		const date = new URLSearchParams(window.location.search).get('date');
		if (!/^\d{4}-\d{2}-\d{2}$/.test(date || '')) {
			throw new Error('A valid class-log date is required.');
		}

		const subjectUrl = new URL(page.dataset.subjectJson, document.baseURI);
		const subject = await fetchJson(subjectUrl.href);
		const entryUrl = new URL(`kb/class-log/${date}/entry.json`, subjectUrl);
		const entry = await fetchJson(entryUrl.href);
		renderPage(page, subject, subjectUrl, entry);
	} catch (error) {
		console.error('Class log failed to load:', error);
		page.innerHTML = `<div class="class-log-error">Class log could not be loaded.${error?.message ? ` ${escapeHtml(error.message)}` : ''}</div>`;
	}
}

function renderPage(page, subject, subjectUrl, entry) {
	const unitNumber = Number(entry.unit?.number || 0);
	const unitLabel = toRoman(unitNumber);
	const unitHref = unitNumber ? new URL(`unit-${unitNumber}.html`, subjectUrl).href : new URL('./index.html', subjectUrl).href;
	const subjectHome = new URL('./index.html', subjectUrl).href;
	const semesterHome = new URL('../index.html', subjectUrl).href;
	const siteHome = new URL('index.html', document.baseURI).href;
	const calendarHref = new URL(`college/calendar.html?semester=${encodeURIComponent(subject.semester || '')}&date=${encodeURIComponent(entry.date)}`, document.baseURI).href;
	const semesterLabel = String(subject.semester || '').replace('-', '.');

	document.title = `${entry.date_label || entry.date} · ${subject.shortName || subject.name} Class Log · Panku's Desk`;

	page.innerHTML = `
		<div class="breadcrumbs">
			<a href="${escapeHtml(siteHome)}">Panku's Desk</a><span>›</span>
			<a href="${escapeHtml(semesterHome)}">Semester ${escapeHtml(semesterLabel)}</a><span>›</span>
			<a href="${escapeHtml(subjectHome)}">${escapeHtml(subject.shortName || subject.name)}</a><span>›</span>
			<span>${escapeHtml(entry.date_label || entry.date)}</span>
		</div>

		<section class="class-log-hero">
			<div>
				<div class="eyebrow">${escapeHtml(subject.name)} · Unit ${escapeHtml(unitLabel)}</div>
				<h1>${escapeHtml(entry.date_label || entry.date)}</h1>
				<p class="class-log-title">${escapeHtml(entry.title || 'Class notes')}</p>
				<p class="class-log-summary">${escapeHtml(entry.summary || '')}</p>
			</div>
			<div class="class-log-hero-actions">
				<a href="${escapeHtml(calendarHref)}">← Back to calendar</a>
				<a href="${escapeHtml(unitHref)}">Open cumulative Unit ${escapeHtml(unitLabel)} notes →</a>
			</div>
		</section>

		<section class="class-log-map panel">
			<div class="class-log-kicker">Mapped into the cumulative unit</div>
			<h2>Topics covered</h2>
			<div class="class-log-topic-links">
				${(entry.mapped_topics || []).map(topic => `<a href="${escapeHtml(new URL(topic.href, subjectUrl).href)}"><span>${escapeHtml(topic.label)}</span><span aria-hidden="true">→</span></a>`).join('')}
			</div>
		</section>

		<section class="class-log-record">
			<div class="class-log-record-heading">
				<div>
					<div class="class-log-kicker">Permanent daily record</div>
					<h2>Verbatim notebook transcription</h2>
				</div>
				<span class="verbatim-badge">Wording preserved</span>
			</div>
			<p class="transcription-policy">${escapeHtml(entry.transcription_policy || '')}</p>
			<div class="class-log-pages">
				${(entry.pages || []).map(renderNotebookPage).join('')}
			</div>
		</section>

		${(entry.source_notes || []).length ? `
			<section class="class-log-source-note panel">
				<div class="class-log-kicker">Source discipline</div>
				<h2>How this dated record is used</h2>
				<ul>${entry.source_notes.map(note => `<li>${escapeHtml(note)}</li>`).join('')}</ul>
			</section>
		` : ''}

	`;
}

function renderNotebookPage(item) {
	return `
		<article class="class-log-notebook-page">
			<header>
				<span>Notebook page ${escapeHtml(item.page)}</span>
				<h3>${escapeHtml(item.heading || '')}</h3>
			</header>
			<div class="verbatim-copy">${renderBlocks(item.blocks || [])}</div>
		</article>
	`;
}

function renderBlocks(blocks) {
	let html = '';
	let bullets = [];
	const flush = () => {
		if (!bullets.length) return;
		html += `<ul>${bullets.join('')}</ul>`;
		bullets = [];
	};

	for (const block of blocks) {
		if (block.type === 'bullet') {
			bullets.push(`<li>${escapeHtml(block.text)}</li>`);
			continue;
		}
		flush();
		switch (block.type) {
			case 'heading': html += `<h4>${escapeHtml(block.text)}</h4>`; break;
			case 'subheading': html += `<h5>${escapeHtml(block.text)}</h5>`; break;
			case 'equation': html += `<div class="verbatim-equation">${formatText(block.text)}</div>`; break;
			case 'figure': html += renderClassFigure(block); break;
			case 'line': html += `<p class="verbatim-line">${formatText(block.text)}</p>`; break;
			default: html += `<p>${formatText(block.text || '')}</p>`;
		}
	}
	flush();
	return html;
}

function renderClassFigure(figure) {
	if (!figure?.src || !figure?.alt) return '';
	const width = Number(figure.width);
	const height = Number(figure.height);
	const dimensions = Number.isFinite(width) && Number.isFinite(height) ? ` width="${width}" height="${height}"` : '';
	return `
		<figure class="class-note-visual">
			<img src="${escapeHtml(figure.src)}" alt="${escapeHtml(figure.alt)}" loading="lazy" decoding="async"${dimensions}>
			${figure.caption ? `<figcaption>${escapeHtml(figure.caption)}</figcaption>` : ''}
		</figure>
	`;
}

async function fetchJson(url) {
	const response = await fetch(url);
	if (!response.ok) throw new Error(`${url} returned ${response.status}`);
	return response.json();
}

function formatText(value) {
	return escapeHtml(value).replace(/\b([A-Za-z][A-Za-z0-9]*)_\{?([A-Za-z0-9]+)\}?/g, '$1<sub>$2</sub>');
}

function toRoman(value) {
	const numerals = [[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']];
	let number = Number(value), result = '';
	for (const [amount, numeral] of numerals) while (number >= amount) { result += numeral; number -= amount; }
	return result || String(value || '');
}

function escapeHtml(value) {
	return String(value ?? '')
		.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;').replaceAll("'", '&#039;');
}
})();

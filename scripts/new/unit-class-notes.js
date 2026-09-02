(function () {
'use strict';

document.addEventListener('DOMContentLoaded', () => initUnitClassNotes());

async function initUnitClassNotes() {
	const page = document.querySelector('.unit-class-notes-page[data-unit][data-subject-json]');
	if (!page) return;

	try {
		const unitNumber = Number(page.dataset.unit);
		const subjectUrl = new URL(page.dataset.subjectJson, document.baseURI);
		const subject = await fetchJson(subjectUrl.href);
		const unitMeta = (subject.units || []).find(unit => Number(unit.number) === unitNumber);
		if (!unitMeta) throw new Error(`Unit ${unitNumber} is not defined.`);

		const cfg = subject.classNotes || {};
		const manifestPath = cfg.sourceManifest || 'kb/data/source-manifest.json';
		const manifest = await fetchJson(new URL(manifestPath, subjectUrl).href);
		const collectionName = cfg.collection || 'class_sources';
		const sources = (manifest?.[collectionName] || [])
			.filter(item => Number(item.unit) === unitNumber && item.entry)
			.sort((a, b) => String(a.date).localeCompare(String(b.date)));
		if (!sources.length) throw new Error(`No class-note entries are available for Unit ${unitNumber}.`);

		const entries = await Promise.all(sources.map(async source => ({
			source,
			entry: await fetchJson(new URL(source.entry, subjectUrl).href),
		})));

		renderPage(page, subject, subjectUrl, unitMeta, entries);
		setupDateNavigation(page);
		try {
			await typesetMath(page);
		} catch (mathError) {
			console.warn('Math typesetting failed; leaving LaTeX source visible.', mathError);
		}
		revealHashTarget(page);
	} catch (error) {
		console.error('Unit class notes failed to load:', error);
		page.innerHTML = `<div class="class-notes-error">Class notes could not be loaded.${error?.message ? ` ${escapeHtml(error.message)}` : ''}</div>`;
	}
}

function renderPage(page, subject, subjectUrl, unitMeta, entries) {
	const unitNumber = Number(unitMeta.number);
	const unitLabel = toRoman(unitNumber);
	const subjectHome = new URL('./index.html', subjectUrl).href;
	const semesterHome = new URL('../index.html', subjectUrl).href;
	const siteHome = new URL('index.html', document.baseURI).href;
	const semesterLabel = String(subject.semester || '').replace('-', '.');
	const resourceNav = window.PankuUnitResourceNav?.render?.({
		subject,
		subjectUrl,
		unitNumber,
		active: 'class-notes',
	}) || '';

	document.title = `Unit ${unitLabel} Class Notes · ${subject.shortName || subject.name} · Panku's Desk`;

	page.innerHTML = `
		<div class="breadcrumbs">
			<a href="${escapeHtml(siteHome)}">Panku's Desk</a><span>›</span>
			<a href="${escapeHtml(semesterHome)}">Semester ${escapeHtml(semesterLabel)}</a><span>›</span>
			<a href="${escapeHtml(subjectHome)}">${escapeHtml(subject.shortName || subject.name)}</a><span>›</span>
			<span>Unit ${escapeHtml(unitLabel)} Class Notes</span>
		</div>

		<section class="class-notes-hero">
			<div class="eyebrow">${escapeHtml(subject.name)} · Unit ${escapeHtml(unitLabel)}</div>
			<h1>Priyanka's Class Notes</h1>
			<p>${escapeHtml(unitMeta.title)}</p>
			<p class="class-notes-policy">Notebook order and meaning are preserved; grammar and awkward English are lightly cleaned for study. Redraws reproduce the teacher's diagrams without adding new theory.</p>
		</section>

		${resourceNav}

		<div class="class-notes-layout section">
			<aside class="class-notes-toc" aria-label="Class-note dates">
				<div class="toc-label">By date</div>
				<nav id="class-notes-date-nav">
					${entries.map(({ source, entry }) => `
						<a class="class-notes-date-link" href="#${escapeHtml(entry.date)}">
							<strong>${escapeHtml(shortDate(entry.date))}</strong>
							<span>${escapeHtml(source.nav_label || entry.nav_summary || entry.title || '')}</span>
						</a>
					`).join('')}
				</nav>
			</aside>

			<section class="class-notes-content" aria-label="Dated class notes">
				${entries.map(({ entry }) => renderEntry(entry)).join('')}
			</section>
		</div>
	`;
}

function renderEntry(entry) {
	return `
		<article class="class-notes-entry" id="${escapeHtml(entry.date)}">
			<header class="class-notes-entry-header">
				<div class="class-notes-date">${escapeHtml(entry.date_label || formatIsoDate(entry.date))}</div>
				<h2>${escapeHtml(entry.title || 'Class notes')}</h2>
				${entry.summary ? `<p>${escapeHtml(entry.summary)}</p>` : ''}
			</header>
			<div class="class-notes-pages">
				${(entry.pages || []).map(renderNotebookPage).join('')}
			</div>
		</article>
	`;
}

function renderNotebookPage(item) {
	return `
		<section class="class-notes-page-block">
			${item.heading ? `<h3>${escapeHtml(item.heading)}</h3>` : ''}
			<div class="class-notes-copy">${renderBlocks(item.blocks || [])}</div>
		</section>
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
			bullets.push(`<li>${formatText(block.text)}</li>`);
			continue;
		}
		flush();
		switch (block.type) {
			case 'heading': html += `<h4>${formatText(block.text)}</h4>`; break;
			case 'subheading': html += `<h5>${formatText(block.text)}</h5>`; break;
			case 'equation': html += `<div class="class-notes-equation">${formatText(block.text)}</div>`; break;
			case 'figure': html += renderClassFigure(block); break;
			case 'line': html += `<p class="class-notes-line">${formatText(block.text)}</p>`; break;
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
	const size = ['symbol','small','medium','large'].includes(figure.size) ? ` class-note-visual--${figure.size}` : 'class-note-visual--medium';
	return `
		<figure class="class-note-visual ${size}">
			<img src="${escapeHtml(figure.src)}" alt="${escapeHtml(figure.alt)}" loading="lazy" decoding="async"${dimensions}>
			${figure.caption ? `<figcaption>${escapeHtml(figure.caption)}</figcaption>` : ''}
		</figure>
	`;
}

function setupDateNavigation(page) {
	const links = Array.from(page.querySelectorAll('.class-notes-date-link'));
	const sections = links.map(link => document.getElementById(link.getAttribute('href')?.slice(1) || '')).filter(Boolean);
	if (!links.length || !sections.length) return;

	const setActive = id => {
		links.forEach(link => {
			const active = link.getAttribute('href') === `#${id}`;
			link.classList.toggle('is-active', active);
			if (active) link.setAttribute('aria-current', 'location');
			else link.removeAttribute('aria-current');
		});
	};

	const observer = new IntersectionObserver(entries => {
		const visible = entries.filter(entry => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
		if (visible[0]?.target?.id) setActive(visible[0].target.id);
	}, { rootMargin: '-18% 0px -68% 0px', threshold: [0, 0.01, 0.15] });
	sections.forEach(section => observer.observe(section));

	links.forEach(link => link.addEventListener('click', event => {
		const id = link.getAttribute('href')?.slice(1);
		const target = id ? document.getElementById(id) : null;
		if (!target) return;
		event.preventDefault();
		history.replaceState(null, '', `#${id}`);
		setActive(id);
		target.scrollIntoView({ behavior: 'smooth', block: 'start' });
	}));
}

function revealHashTarget(page) {
	const id = decodeURIComponent(window.location.hash.slice(1));
	if (!id) return;
	const target = page.querySelector(`#${cssEscape(id)}`);
	if (!target) return;
	requestAnimationFrame(() => target.scrollIntoView({ block: 'start' }));
}

function cssEscape(value) {
	if (window.CSS?.escape) return window.CSS.escape(value);
	return String(value).replace(/[^A-Za-z0-9_-]/g, '\\$&');
}

async function fetchJson(url) {
	const response = await fetch(url);
	if (!response.ok) throw new Error(`${url} returned ${response.status}`);
	return response.json();
}

function shortDate(value) {
	const match = String(value || '').match(/^(\d{4})-(\d{2})-(\d{2})$/);
	if (!match) return String(value || '');
	const [, , month, day] = match;
	const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
	return `${Number(day)} ${months[Number(month) - 1] || month}`;
}

function formatIsoDate(value) {
	const match = String(value || '').match(/^(\d{4})-(\d{2})-(\d{2})$/);
	if (!match) return String(value || '');
	const [, year, month, day] = match;
	const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
	return `${Number(day)} ${months[Number(month) - 1] || month} ${year}`;
}

function formatText(value) {
	const input = String(value ?? '');
	const mathPattern = /(\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))/g;
	let result = '';
	let lastIndex = 0;
	let match;
	while ((match = mathPattern.exec(input)) !== null) {
		result += formatPlainText(input.slice(lastIndex, match.index));
		result += escapeHtml(match[0]);
		lastIndex = match.index + match[0].length;
	}
	result += formatPlainText(input.slice(lastIndex));
	return result;
}

function formatPlainText(value) {
	return escapeHtml(value).replace(/\b([A-Za-z][A-Za-z0-9]*)_\{?([A-Za-z0-9]+)\}?/g, '$1<sub>$2</sub>');
}

let mathJaxPromise = null;
async function typesetMath(root) {
	if (!root || !/[\\][(\[]/.test(root.textContent || '')) return;
	await ensureMathJax();
	if (window.MathJax?.typesetPromise) await window.MathJax.typesetPromise([root]);
}
function ensureMathJax() {
	if (window.MathJax?.typesetPromise) return Promise.resolve(window.MathJax);
	if (mathJaxPromise) return mathJaxPromise;
	mathJaxPromise = new Promise((resolve, reject) => {
		window.MathJax = { tex: { inlineMath: [['\\(', '\\)']], displayMath: [['\\[', '\\]']], processEscapes: true }, options: { skipHtmlTags: ['script','noscript','style','textarea','pre','code'] } };
		const script = document.createElement('script');
		script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
		script.async = true;
		script.onload = () => resolve(window.MathJax);
		script.onerror = () => reject(new Error('MathJax could not be loaded.'));
		document.head.appendChild(script);
	});
	return mathJaxPromise;
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

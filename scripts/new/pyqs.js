(function () {
'use strict';

document.addEventListener('DOMContentLoaded', () => initPyqs());

async function initPyqs() {
	const page = document.querySelector('.practice-page[data-pyq-bank]');
	if (!page) return;

	try {
		const subjectUrl = new URL(page.dataset.subjectJson, document.baseURI);
		const subject = await fetchJson(subjectUrl.href);
		const bankPath = page.dataset.pyqBank || subject.practice?.pyqs?.data;
		if (!bankPath) throw new Error('No PYQ data source is configured for this subject.');
		const bank = await fetchJson(new URL(bankPath, subjectUrl).href);

		const years = Array.isArray(bank.years) ? bank.years : [];
		if (!years.length) throw new Error('No previous-year papers are available.');

		const requested = new URLSearchParams(window.location.search).get('year');
		const latest = bank.latest_year || years[years.length - 1]?.id;
		const year = years.find(item => item.id === requested) || years.find(item => item.id === latest) || years[years.length - 1];
		if (!year) throw new Error('The selected paper could not be found.');

		renderPage(page, subject, subjectUrl, bank, years, year);
		await typesetMath(page);
		initAccordions(page);
		revealHashTarget(page);
	} catch (error) {
		console.error('PYQ page load failed:', error);
		page.innerHTML = `<div class="practice-error">Previous-year questions could not be loaded.${error?.message ? ` ${escapeHtml(error.message)}` : ''}</div>`;
	}
}

function renderPage(page, subject, subjectUrl, bank, years, year) {
	const subjectHome = new URL('./index.html', subjectUrl).href;
	const sourcePaper = year.source_paper ? new URL(year.source_paper, subjectUrl).href : null;
	const questionCount = (year.groups || []).reduce((sum, group) => sum + (group.questions || []).length, 0);
	const currentIndex = years.findIndex(item => item.id === year.id);
	const currentPath = `${window.location.pathname}?year=${encodeURIComponent(year.id)}`;

	document.title = `${year.label || year.id} Semester PYQs · ${subject.shortName || subject.name} · Panku's Desk`;

	page.innerHTML = `
		<div class="breadcrumbs">
			<a href="index.html">Panku's Desk</a><span>›</span>
			<a href="college/1-1/index.html">Semester 1.1</a><span>›</span>
			<a href="${escapeHtml(subjectHome)}">${escapeHtml(subject.shortName || subject.name)}</a><span>›</span>
			<span>Semester PYQs</span>
		</div>

		<section class="practice-hero pyq-hero">
			<div class="eyebrow">${escapeHtml(subject.name)} · Solved semester papers</div>
			<h1>${escapeHtml(year.label || year.id)} PYQs</h1>
			<p>${escapeHtml(year.exam || 'Official semester examination paper')} · ${escapeHtml(year.course_code || '')} · ${escapeHtml(year.course_title || subject.name)}</p>
			<div class="practice-stats" aria-label="Paper summary">
				${stat(questionCount, 'question accordions')}
				${stat(year.regulation || subject.regulation, 'regulation')}
				${stat((year.groups || []).length, 'paper sections')}
			</div>
			<div class="practice-hero-actions">
				<a href="${escapeHtml(subjectHome)}">← Back to BEE</a>
				${sourcePaper ? `<a href="${escapeHtml(sourcePaper)}" target="_blank" rel="noopener">View source paper ↗</a>` : ''}
			</div>
		</section>

		${renderYearNav(years, currentIndex, getCurrentPaperUrl())}

		<section class="practice-source-note pyq-paper-note">
			<div class="practice-source-kicker">Paper provenance</div>
			<strong>${escapeHtml(year.course_code || '')} · ${escapeHtml(year.course_title || '')}</strong>
			<p>${escapeHtml(year.source_note || '')}</p>
			<p><strong>Answer provenance:</strong> Official questions are preserved from the paper; the worked answers are PankusDesk-generated solutions aligned to the locked BEE source base.</p>
			${year.branches ? `<p><strong>Branches:</strong> ${escapeHtml(year.branches)}</p>` : ''}
		</section>

		${renderJumpNav(year.groups || [], currentPath)}

		<div class="question-topic-list pyq-question-groups">
			${(year.groups || []).map(group => renderGroup(group, subjectUrl, year)).join('')}
		</div>
	`;
}

function renderYearNav(years, currentIndex, paperUrl) {
	const previous = currentIndex > 0 ? years[currentIndex - 1] : null;
	const current = years[currentIndex];
	const next = currentIndex >= 0 && currentIndex < years.length - 1 ? years[currentIndex + 1] : null;
	return `
		<nav class="pyq-year-nav" aria-label="Semester paper navigation">
			<div class="pyq-year-slot pyq-year-slot-prev">
				${previous ? yearLink(previous, 'Previous paper', '←', '', paperUrl) : '<span class="pyq-year-empty" aria-hidden="true"></span>'}
			</div>
			<div class="pyq-year-current" aria-current="page">
				<span class="pyq-year-kicker">Current paper</span>
				<strong>${escapeHtml(current?.label || current?.id || '')}</strong>
			</div>
			<div class="pyq-year-slot pyq-year-slot-next">
				${next ? yearLink(next, 'Next paper', '', '→', paperUrl) : '<span class="pyq-year-empty" aria-hidden="true"></span>'}
			</div>
		</nav>
	`;
}

function yearLink(year, kicker, prefix, suffix, paperUrl) {
	const href = `${paperUrl}?year=${encodeURIComponent(year.id)}`;
	return `
		<a class="pyq-year-link" href="${escapeHtml(href)}">
			<span class="pyq-year-kicker">${escapeHtml(kicker)}</span>
			<strong>${escapeHtml(prefix)}${prefix ? ' ' : ''}${escapeHtml(year.label || year.id)}${suffix ? ` ${escapeHtml(suffix)}` : ''}</strong>
		</a>
	`;
}

function getCurrentPaperUrl() {
	const url = new URL(window.location.href);
	url.search = '';
	url.hash = '';
	return url.href;
}

function renderJumpNav(groups, currentPath) {
	if (!groups.length) return '';
	return `
		<nav class="question-set-jump" aria-label="Jump to paper section">
			<div class="question-set-jump-heading">Jump to section</div>
			<div class="question-set-jump-links">
				${groups.map(group => `<a href="${escapeHtml(currentPath)}#${escapeHtml(group.id)}"><span>${escapeHtml(group.title)}</span><small>${(group.questions || []).length}</small></a>`).join('')}
			</div>
		</nav>
	`;
}

function renderGroup(group, subjectUrl, year) {
	return `
		<section class="section question-group" id="${escapeHtml(group.id)}">
			<div class="section-heading-row question-group-heading">
				<div>
					<div class="section-title">${escapeHtml(group.title)}</div>
					<div class="section-note">${escapeHtml(group.note || 'Open a question to reveal the worked answer.')}</div>
				</div>
				<span class="question-count">${(group.questions || []).length} questions</span>
			</div>
			<div class="chapter-question-list">
				${(group.questions || []).map(question => renderQuestion(question, subjectUrl, year)).join('')}
			</div>
		</section>
	`;
}

function renderQuestion(question, subjectUrl, year) {
	const answerId = `answer-${question.id}`;
	const outside = question.r25_scope === 'outside-current-r25';
	const prompt = renderQuestionPrompt(question);
	return `
		<article class="chapter-question pyq-question ${outside ? 'pyq-outside-r25' : ''}" id="question-${escapeHtml(question.id)}">
			<button class="chapter-question-toggle" type="button" aria-expanded="false" aria-controls="${escapeHtml(answerId)}">
				<span class="chapter-question-number">${formatQuestionNumber(question.number)}</span>
				<span class="chapter-question-copy">
					<span class="chapter-question-text">${prompt}</span>
					<span class="pyq-question-meta-row">
						<span class="pyq-marks">${escapeHtml(question.marks || '')}</span>
						${question.r25_mapping ? `<span class="pyq-topic-tag">${escapeHtml(question.r25_mapping)}</span>` : ''}
						${outside ? '<span class="pyq-scope-tag is-outside">Historical R22 · outside current R25</span>' : '<span class="pyq-scope-tag">Current R25 overlap</span>'}
					</span>
					${renderQuestionFigures(question.figures || [], subjectUrl, year)}
				</span>
				<span class="chapter-question-icon" aria-hidden="true">+</span>
			</button>
			<div class="chapter-question-answer" id="${escapeHtml(answerId)}" hidden>
				<div class="answer-label">Worked answer</div>
				${outside ? '<aside class="pyq-scope-note" role="note"><strong>Historical syllabus note:</strong> This question belongs to the older R22 BEEE paper and is outside the current 25ES1EE101 R25 syllabus. It is solved here to keep the official paper complete.</aside>' : ''}
				${renderAnswer(question.answer || {})}
			</div>
		</article>
	`;
}

function renderQuestionPrompt(question) {
	const parts = Array.isArray(question.question_parts) ? question.question_parts : [];
	if (!parts.length) return formatText(question.question || '');
	const lead = question.question_lead || question.question || '';
	return `
		${lead ? `<span class="chapter-question-lead">${formatText(lead)}</span>` : ''}
		<span class="chapter-question-parts">
			${parts.map(part => `
				<span class="chapter-question-part">
					<span class="chapter-question-part-label">${escapeHtml(part.label || '')}</span>
					<span class="chapter-question-part-content">${formatText(part.content || '')}</span>
				</span>
			`).join('')}
		</span>
	`;
}

function getPyqPlaceholderFilename(figure) {
	const target = typeof figure?.target_src === 'string' && figure.target_src.trim()
		? figure.target_src.trim()
		: (typeof figure?.src === 'string' ? figure.src.trim() : '');
	if (!target) return '';
	const clean = target.split('?')[0].split('#')[0];
	if (clean.startsWith('placeholder://')) {
		const token = clean.slice('placeholder://'.length).replace(/^\/+/, '');
		return token ? `${token}.png` : '';
	}
	const parts = clean.split('/').filter(Boolean);
	return parts.length ? parts[parts.length - 1] : '';
}

function renderQuestionFigures(figures, subjectUrl, year) {
	if (!figures.length) return '';
	return `
		<span class="pyq-question-figures">
			${figures.map(figure => {
				if (figure?.placeholder) {
					const yearLabel = year?.label || year?.id || 'PYQ';
					const questionLabel = figure.question_label || 'Question figure';
					const description = figure.description ? `<span class="pyq-figure-placeholder-description">${formatText(figure.description)}</span>` : '';
					const sourcePage = figure.source_page ? `Source paper p. ${figure.source_page}` : 'Source paper page to be confirmed';
					const filename = getPyqPlaceholderFilename(figure);
					const filenameLine = filename ? `<span class="pyq-figure-placeholder-filename">Expected filename: <code>${escapeHtml(filename)}</code></span>` : '';
					return `
						<span class="pyq-question-figure pyq-figure-placeholder" role="note" aria-label="${escapeHtml(`${yearLabel} ${questionLabel} image placeholder`)}">
							<span class="pyq-figure-placeholder-kicker">PYQ image placeholder</span>
							<span class="pyq-figure-placeholder-title">${escapeHtml(yearLabel)} · ${escapeHtml(questionLabel)}</span>
							${description}
							<span class="pyq-figure-placeholder-page">${escapeHtml(sourcePage)}</span>
							${filenameLine}
						</span>
					`;
				}
				if (!figure?.src) return '';
				const src = new URL(figure.src, subjectUrl).href;
				return `<span class="pyq-question-figure"><img src="${escapeHtml(src)}" alt="${escapeHtml(figure.alt || '')}" loading="lazy" />${figure.caption ? `<span>${escapeHtml(figure.caption)}</span>` : ''}</span>`;
			}).join('')}
		</span>
	`;
}

function renderAnswer(answer) {
	const pieces = [];
	for (const paragraph of answer.paragraphs || []) pieces.push(`<p>${formatText(paragraph)}</p>`);
	if (answer.parts?.length) pieces.push(`<div class="answer-part-list">${answer.parts.map(renderAnswerPart).join('')}</div>`);
	pieces.push(renderAnswerBody(answer));
	return pieces.join('') || '<p>No answer has been added yet.</p>';
}

function renderAnswerPart(part, index) {
	return `
		<section class="answer-part" aria-label="Solution ${escapeHtml(part.label || String(index + 1))}">
			<div class="answer-part-heading">Part ${escapeHtml(part.label || String(index + 1))}</div>
			${(part.paragraphs || []).map(paragraph => `<p>${formatText(paragraph)}</p>`).join('')}
			${renderAnswerBody(part)}
		</section>
	`;
}

function renderAnswerBody(answer) {
	const pieces = [];
	if (answer.figures?.length) pieces.push(`<div class="answer-figures">${answer.figures.map(renderAnswerFigure).join('')}</div>`);
	if (answer.diagram) pieces.push(`<pre class="answer-diagram">${escapeHtml(answer.diagram)}</pre>`);
	if (answer.bullets?.length) pieces.push(`<ul>${answer.bullets.map(item => `<li>${formatText(item)}</li>`).join('')}</ul>`);
	if (answer.table) pieces.push(renderTable(answer.table));
	for (const paragraph of answer.paragraphs_after || []) pieces.push(`<p>${formatText(paragraph)}</p>`);
	if (answer.equations?.length) pieces.push(`<div class="answer-equations">${answer.equations.map(eq => `<div>${formatText(eq)}</div>`).join('')}</div>`);
	if (answer.steps?.length) pieces.push(`<ol class="answer-steps">${answer.steps.map(step => `<li>${formatText(step)}</li>`).join('')}</ol>`);
	if (answer.result) pieces.push(`<div class="answer-result"><strong class="answer-result-label">Final answer:</strong> <strong class="answer-result-value">${formatText(answer.result)}</strong></div>`);
	if (answer.book_check) pieces.push(`<div class="book-check">${formatText(answer.book_check)}</div>`);
	if (answer.note) pieces.push(`<div class="answer-note">${formatText(answer.note)}</div>`);
	return pieces.join('');
}

function renderAnswerFigure(figure) {
	return window.PankuStudyUI?.renderFigure?.(figure, { className: 'study-figure answer-figure' }) || '';
}

function renderTable(table) {
	return `
		<div class="answer-table-wrap">
			<table class="answer-table">
				${table.headers?.length ? `<thead><tr>${table.headers.map(h => `<th>${formatText(h)}</th>`).join('')}</tr></thead>` : ''}
				<tbody>${(table.rows || []).map(row => `<tr>${row.map(cell => `<td>${formatText(cell)}</td>`).join('')}</tr>`).join('')}</tbody>
			</table>
		</div>
	`;
}

function stat(value, label) {
	if (value === undefined || value === null || value === '') return '';
	return `<div><strong>${escapeHtml(value)}</strong><span>${escapeHtml(label)}</span></div>`;
}

function initAccordions(page) {
	page.querySelectorAll('.chapter-question-toggle').forEach(button => {
		button.addEventListener('click', () => {
			const card = button.closest('.chapter-question');
			const answer = card?.querySelector('.chapter-question-answer');
			if (!answer) return;
			const willOpen = button.getAttribute('aria-expanded') !== 'true';
			const group = card.closest('.chapter-question-list');
			group?.querySelectorAll('.chapter-question-toggle[aria-expanded="true"]').forEach(other => {
				if (other === button) return;
				other.setAttribute('aria-expanded', 'false');
				const otherAnswer = other.closest('.chapter-question')?.querySelector('.chapter-question-answer');
				if (otherAnswer) otherAnswer.hidden = true;
			});
			button.setAttribute('aria-expanded', String(willOpen));
			answer.hidden = !willOpen;
			if (willOpen) typesetMath(answer);
		});
	});
}

function revealHashTarget(page) {
	if (!window.location.hash) return;
	const targetId = decodeURIComponent(window.location.hash.slice(1));
	const target = document.getElementById(targetId);
	if (!target || !page.contains(target)) return;
	const card = target.classList.contains('chapter-question') ? target : target.closest('.chapter-question');
	if (card) {
		const button = card.querySelector('.chapter-question-toggle');
		const answer = card.querySelector('.chapter-question-answer');
		if (button && answer) {
			button.setAttribute('aria-expanded', 'true');
			answer.hidden = false;
			typesetMath(answer);
		}
	}
	requestAnimationFrame(() => target.scrollIntoView({ behavior: 'smooth', block: 'start' }));
}

function formatQuestionNumber(value) {
	const text = String(value ?? '');
	return /^[a-z]$/i.test(text) ? `${text})` : `Q${text}`;
}

async function fetchJson(url) {
	const response = await fetch(url, { cache: 'no-store' });
	if (!response.ok) throw new Error(`${url} returned ${response.status}`);
	return response.json();
}

function formatText(value) { return window.PankuStudyUI?.formatText?.(value) ?? escapeHtml(value); }
async function typesetMath(root) { return window.PankuStudyUI?.typesetMath?.(root); }

function escapeHtml(value) {
	return String(value ?? '')
		.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;').replaceAll("'", '&#039;');
}
})();

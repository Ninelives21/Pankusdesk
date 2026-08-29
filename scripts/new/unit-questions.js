(function () {
'use strict';

document.addEventListener('DOMContentLoaded', () => initUnitQuestions());

async function initUnitQuestions() {
	const page = document.querySelector('.practice-page[data-unit]');
	if (!page) return;

	try {
		const unitNumber = Number(page.dataset.unit);
		const subjectUrl = new URL(page.dataset.subjectJson, document.baseURI);
		const subject = await fetchJson(subjectUrl.href);
		const unitMeta = subject.units.find(unit => Number(unit.number) === unitNumber);
		if (!unitMeta) throw new Error(`Unit ${unitNumber} is not defined.`);

		const bankPath = subject.practice?.unitQuestions?.data;
		if (!bankPath) throw new Error('No textbook-question data source is configured for this subject.');
		const bank = await fetchJson(new URL(bankPath, subjectUrl).href);
		const unitBank = bank.units?.[String(unitNumber)];
		if (!unitBank) throw new Error(`No textbook-question bank is available for Unit ${unitNumber}.`);

		renderPage(page, subject, subjectUrl, unitMeta, unitBank, { ...(bank.source || {}), ...(unitBank.source || {}) });
		await typesetMath(page);
		initAccordions(page);
		revealHashTarget(page);
	} catch (error) {
		console.error('Unit textbook questions load failed:', error);
		page.innerHTML = `<div class="practice-error">Textbook questions could not be loaded.${error?.message ? ` ${escapeHtml(error.message)}` : ''}</div>`;
	}
}

function renderPage(page, subject, subjectUrl, unitMeta, unitBank, source) {
	const unitLabel = toRoman(Number(unitMeta.number));
	const subjectHome = new URL('./index.html', subjectUrl).href;
	const unitHome = new URL(`unit-${unitMeta.number}.html`, subjectUrl).href;
	const pyqHref = subject.practice?.pyqs?.href ? new URL(subject.practice.pyqs.href, subjectUrl).href : null;
	const summary = unitBank.summary || {};

	const pageTitle = unitBank.page_title || 'Chapter-end Questions';
	const pageDescription = unitBank.page_description || `All official review questions from the prescribed textbook chapter, with answers consolidated from the source-backed Unit ${unitLabel} notes.`;
	document.title = `Unit ${unitLabel} ${pageTitle} · ${subject.shortName || subject.name} · Panku's Desk`;

	page.innerHTML = `
		<div class="breadcrumbs">
			<a href="index.html">Panku's Desk</a><span>›</span>
			<a href="${escapeHtml(subjectHome)}">${escapeHtml(subject.shortName || subject.name)}</a><span>›</span>
			<a href="${escapeHtml(unitHome)}">Unit ${escapeHtml(unitLabel)}</a><span>›</span>
			<span>Textbook Questions</span>
		</div>

		<section class="practice-hero">
			<div class="eyebrow">${escapeHtml(subject.name)} · Unit ${escapeHtml(unitLabel)}</div>
			<h1>${escapeHtml(pageTitle)}</h1>
			<p>${escapeHtml(pageDescription)}</p>
			<div class="practice-stats" aria-label="Question-bank summary">
				${Array.isArray(summary.stats) ? summary.stats.map(item => stat(item.value, item.label)).join('') : `${stat(summary.official_question_count, 'official questions')}${stat(summary.short_answer_count, '2-mark')}${stat(summary.essay_count, '6-mark')}`}
			</div>
			<div class="practice-hero-actions">
				<a href="${escapeHtml(unitHome)}">← Back to Unit ${escapeHtml(unitLabel)} notes</a>
				${pyqHref ? `<a href="${escapeHtml(pyqHref)}">Browse ${escapeHtml(subject.practice.pyqs.label || 'PYQs')} →</a>` : ''}
			</div>
		</section>

		<section class="practice-source-note">
			<strong>${escapeHtml(source.title || 'Prescribed textbook')}${source.chapter ? ` · ${escapeHtml(source.chapter)}` : ''}${source.review_pages?.length ? ` · ${escapeHtml(formatReviewPages(source.review_pages))}` : ''}</strong>
			<p>${escapeHtml(unitBank.scope_note || source.note || '')}</p>
		</section>

		${(unitBank.groups || []).map(group => renderGroup(group)).join('') || '<div class="practice-empty">No chapter-end questions are available for this unit yet.</div>'}
	`;
}

function stat(value, label) {
	if (value === undefined || value === null) return '';
	return `<div><strong>${escapeHtml(value)}</strong><span>${escapeHtml(label)}</span></div>`;
}

function renderGroup(group) {
	return `
		<section class="section question-group" id="${escapeHtml(group.id)}">
			<div class="section-heading-row question-group-heading">
				<div>
					<div class="section-title">${escapeHtml(group.title)}</div>
					<div class="section-note">${escapeHtml(group.note || 'Click a question to reveal the answer.')}</div>
				</div>
				<span class="question-count">${(group.questions || []).length} questions</span>
			</div>
			<div class="chapter-question-list">
				${(group.questions || []).map(question => renderQuestion(question)).join('')}
			</div>
		</section>
	`;
}

function renderQuestion(question) {
	const answerId = `answer-${question.id}`;
	const isGap = question.answer?.status === 'source-gap';
	return `
		<article class="chapter-question ${isGap ? 'question-source-gap' : ''}" id="question-${escapeHtml(question.id)}">
			<button class="chapter-question-toggle" type="button" aria-expanded="false" aria-controls="${escapeHtml(answerId)}">
				<span class="chapter-question-number">Q${escapeHtml(question.number)}</span>
				<span class="chapter-question-copy">
					<span class="chapter-question-text">${formatText(question.question)}</span>
					<span class="chapter-question-meta">Book p. ${escapeHtml(question.book_page)}${question.r25_scope === 'outside-current-r25' ? ' · outside current R25 Unit I scope' : ''}</span>
				</span>
				<span class="chapter-question-icon" aria-hidden="true">+</span>
			</button>
			<div class="chapter-question-answer" id="${escapeHtml(answerId)}" hidden>
				<div class="answer-label">${isGap ? 'Source note' : 'Answer'}</div>
				${renderAnswer(question.answer || {})}
			</div>
		</article>
	`;
}

function renderAnswer(answer) {
	const pieces = [];
	for (const paragraph of answer.paragraphs || []) pieces.push(`<p>${formatText(paragraph)}</p>`);
	if (answer.figures?.length) pieces.push(`<div class="answer-figures">${answer.figures.map(renderAnswerFigure).join('')}</div>`);
	if (answer.diagram) pieces.push(`<div class="answer-diagram">${formatText(answer.diagram)}</div>`);
	if (answer.bullets?.length) pieces.push(`<ul>${answer.bullets.map(item => `<li>${formatText(item)}</li>`).join('')}</ul>`);
	if (answer.table) pieces.push(renderTable(answer.table));
	for (const paragraph of answer.paragraphs_after || []) pieces.push(`<p>${formatText(paragraph)}</p>`);
	if (answer.equations?.length) pieces.push(`<div class="answer-equations">${answer.equations.map(eq => `<div>${formatText(eq)}</div>`).join('')}</div>`);
	if (answer.steps?.length) pieces.push(`<ol class="answer-steps">${answer.steps.map(step => `<li>${formatText(step)}</li>`).join('')}</ol>`);
	if (answer.result) pieces.push(`<div class="answer-result"><strong>Result:</strong> ${formatText(answer.result)}</div>`);
	if (answer.book_check) pieces.push(`<div class="book-check">${formatText(answer.book_check)}</div>`);
	if (answer.note) pieces.push(`<div class="answer-note">${formatText(answer.note)}</div>`);
	return pieces.join('') || '<p>No answer has been added yet.</p>';
}

function renderAnswerFigure(figure) {
	if (!figure?.src || !figure?.alt) return '';
	const width = Number(figure.width);
	const height = Number(figure.height);
	const dimensions = Number.isFinite(width) && Number.isFinite(height)
		? ` width="${width}" height="${height}"`
		: '';
	const caption = figure.caption ? `<span>${escapeHtml(figure.caption)}</span>` : '';
	const page = figure.page ? `<span class="answer-figure-page">Book p. ${escapeHtml(figure.page)}</span>` : '';

	return `
		<figure class="answer-figure">
			<img src="${escapeHtml(figure.src)}" alt="${escapeHtml(figure.alt)}" loading="lazy" decoding="async"${dimensions}>
			${caption || page ? `<figcaption>${caption}${page}</figcaption>` : ''}
		</figure>
	`;
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
		});
	});
}

function revealHashTarget(page) {
	if (!window.location.hash) return;
	const targetId = decodeURIComponent(window.location.hash.slice(1));
	const target = document.getElementById(targetId);
	if (!target || !page.contains(target)) return;

	const card = target.classList.contains('chapter-question')
		? target
		: target.closest('.chapter-question');
	if (card) {
		const button = card.querySelector('.chapter-question-toggle');
		const answer = card.querySelector('.chapter-question-answer');
		if (button && answer) {
			button.setAttribute('aria-expanded', 'true');
			answer.hidden = false;
		}
	}

	requestAnimationFrame(() => target.scrollIntoView({ behavior: 'smooth', block: 'start' }));
}

function formatReviewPages(pages) {
	const values = (pages || []).map(Number).filter(Number.isFinite).sort((a, b) => a - b);
	if (!values.length) return '';
	if (values.length === 1) return `p. ${values[0]}`;
	let sequential = true;
	for (let i = 1; i < values.length; i += 1) {
		if (values[i] !== values[i - 1] + 1) { sequential = false; break; }
	}
	return sequential ? `pp. ${values[0]}–${values[values.length - 1]}` : `pp. ${values.join(', ')}`;
}

async function fetchJson(url) {
	const response = await fetch(url);
	if (!response.ok) throw new Error(`${url} returned ${response.status}`);
	return response.json();
}


function formatText(value) {
	const input = String(value ?? '');
	const mathPattern = /(\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))/g;
	let result = '';
	let lastIndex = 0;
	let match;
	while ((match = mathPattern.exec(input)) !== null) {
		result += escapeHtml(input.slice(lastIndex, match.index));
		result += escapeHtml(match[0]);
		lastIndex = match.index + match[0].length;
	}
	result += escapeHtml(input.slice(lastIndex));
	return result;
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
		window.MathJax = {
			tex: { inlineMath: [['\\(', '\\)']], displayMath: [['\\[', '\\]']], processEscapes: true },
			options: { skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'] },
		};
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
	return result || String(value);
}

function escapeHtml(value) {
	return String(value ?? '')
		.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;').replaceAll("'", '&#039;');
}
})();

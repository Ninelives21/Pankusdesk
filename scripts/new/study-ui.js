(function () {
'use strict';

let mathJaxPromise = null;

function escapeHtml(value) {
	return String(value ?? '')
		.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;').replaceAll("'", '&#039;');
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

function normalizeMismatch(value) {
	if (!value || typeof value !== 'object' || !String(value.message || '').trim()) return null;
	return { label: String(value.label || 'Math mismatch'), message: String(value.message) };
}

function renderMismatch(mismatch) {
	return `
		<aside class="study-mismatch-note" role="note" aria-label="${escapeHtml(mismatch.label)}">
			<div class="study-mismatch-note-label">${escapeHtml(mismatch.label)}</div>
			<div class="study-mismatch-note-text">${formatText(mismatch.message)}</div>
		</aside>`;
}

function renderFigure(figure, options = {}) {
	if (!figure?.src || !figure?.alt) return '';
	const width = Number(figure.width);
	const height = Number(figure.height);
	const dimensions = Number.isFinite(width) && Number.isFinite(height) ? ` width="${width}" height="${height}"` : '';
	const className = options.className || 'study-figure';
	const extraClass = options.extraClass ? ` ${options.extraClass}` : '';
	const captionParts = [];
	if (figure.caption) captionParts.push(`<span>${escapeHtml(figure.caption)}</span>`);
	if (figure.page) captionParts.push(`<span class="study-figure-page">Book p. ${escapeHtml(figure.page)}</span>`);
	return `
		<figure class="${escapeHtml(className)}${extraClass}">
			<img src="${escapeHtml(figure.src)}" alt="${escapeHtml(figure.alt)}" loading="lazy" decoding="async"${dimensions}>
			${captionParts.length ? `<figcaption>${captionParts.join('')}</figcaption>` : ''}
		</figure>`;
}

function splitQuestionAndSolution(item) {
	const explicit = item.question_paragraphs ?? item.questionParagraphs ?? [];
	const paragraphs = item.paragraphs ?? [];
	if (Array.isArray(explicit) && explicit.length) return { question: explicit, solution: paragraphs };
	const solutionIndex = paragraphs.findIndex(paragraph => /^\s*Solution\b/i.test(String(paragraph)));
	if (solutionIndex > 0) return { question: paragraphs.slice(0, solutionIndex), solution: paragraphs.slice(solutionIndex) };
	if (solutionIndex === 0) return { question: [], solution: paragraphs };
	if (paragraphs.length) return { question: [paragraphs[0]], solution: paragraphs.slice(1) };
	return { question: [], solution: [] };
}

function renderAccordionGroup(config = {}) {
	const items = Array.isArray(config.items) ? config.items : [];
	if (!items.length) return '';
	const label = config.label || 'More detail';
	const isExampleGroup = config.isExampleGroup ?? /example|question/i.test(label);
	return `
		<div class="study-accordion${isExampleGroup ? ' study-accordion--examples' : ''}" aria-label="${escapeHtml(label)}">
			<div class="study-accordion-label">${escapeHtml(label)}</div>
			${items.map(item => renderAccordionItem(item, { isExampleGroup })).join('')}
		</div>`;
}

function renderAccordionItem(item, options = {}) {
	const isExample = options.isExampleGroup || (item.question_paragraphs ?? item.questionParagraphs)?.length;
	const mismatch = normalizeMismatch(item.math_mismatch ?? item.discrepancy);
	if (!isExample) {
		return `
			<details class="study-accordion-item${mismatch ? ' has-math-mismatch' : ''}">
				<summary>
					<span class="study-accordion-summary-title">${formatText(item.title || '')}</span>
					<span class="study-accordion-toggle" aria-hidden="true">+</span>
				</summary>
				<div class="study-accordion-content">
					${(item.paragraphs || []).map(p => `<p>${formatText(p)}</p>`).join('')}
					${(item.bullets || []).length ? `<ul>${item.bullets.map(b => `<li>${formatText(b)}</li>`).join('')}</ul>` : ''}
					${mismatch ? renderMismatch(mismatch) : ''}
				</div>
			</details>`;
	}

	const split = splitQuestionAndSolution(item);
	return `
		<details class="study-accordion-item study-accordion-item--example${mismatch ? ' has-math-mismatch' : ''}">
			<summary>
				<span class="study-example-summary-copy">
					<span class="study-example-title-row">
						<span class="study-example-title">${formatText(item.title || '')}</span>
						${mismatch ? `<span class="study-mismatch-badge">${escapeHtml(mismatch.label)}</span>` : ''}
					</span>
					${split.question.length ? `<span class="study-example-question">${split.question.map(p => `<span>${formatText(p)}</span>`).join('')}</span>` : ''}
				</span>
				<span class="study-accordion-toggle" aria-hidden="true">+</span>
			</summary>
			<div class="study-accordion-content study-example-solution">
				<div class="study-solution-label">Solution</div>
				${(item.figures || []).map(fig => renderFigure(fig)).join('')}
				${split.solution.map(p => `<p>${formatText(p)}</p>`).join('')}
				${(item.bullets || []).length ? `<ul>${item.bullets.map(b => `<li>${formatText(b)}</li>`).join('')}</ul>` : ''}
				${mismatch ? renderMismatch(mismatch) : ''}
				${item.final_answer ? `<div class="study-final-answer"><strong>Final answer:</strong> <strong>${formatText(item.final_answer)}</strong></div>` : ''}
			</div>
		</details>`;
}

function renderTip(block) {
	const title = block?.title || 'PankusDesk tip';
	const paragraphs = Array.isArray(block?.paragraphs) ? block.paragraphs : [];
	const bullets = Array.isArray(block?.bullets) ? block.bullets : [];
	return `
		<aside class="study-tip" role="note">
			<div class="study-tip-label">${escapeHtml(block?.label || 'PankusDesk tip')}</div>
			<h5>${formatText(title)}</h5>
			${paragraphs.map(p => `<p>${formatText(p)}</p>`).join('')}
			${bullets.length ? `<ul>${bullets.map(b => `<li>${formatText(b)}</li>`).join('')}</ul>` : ''}
			${block?.example ? `<div class="study-tip-example">${formatText(block.example)}</div>` : ''}
		</aside>`;
}

function initAccordions(root = document) {
	root.querySelectorAll('.study-accordion').forEach(group => {
		const detailsItems = Array.from(group.querySelectorAll(':scope > .study-accordion-item'));
		detailsItems.forEach(details => details.addEventListener('toggle', () => {
			if (!details.open) return;
			detailsItems.forEach(other => { if (other !== details) other.open = false; });
		}));
	});
}

window.PankuStudyUI = {
	escapeHtml,
	formatText,
	typesetMath,
	renderFigure,
	renderAccordionGroup,
	renderTip,
	initAccordions,
};
})();

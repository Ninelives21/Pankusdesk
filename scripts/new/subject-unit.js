document.addEventListener('DOMContentLoaded', () => {
	initSubjectUnitPage();
});

async function initSubjectUnitPage() {
	const page = document.querySelector('.subject-unit-page');
	if (!page) return;

	const unitNumber = Number(page.dataset.unit);
	const subjectJsonUrl = page.dataset.subjectJson;

	try {
		if (!unitNumber || !subjectJsonUrl) {
			throw new Error('Unit page configuration is incomplete.');
		}

		const subjectUrl = new URL(subjectJsonUrl, document.baseURI);
		const subject = await fetchJson(subjectUrl.href);
		const unitMeta = subject.units?.find(unit => Number(unit.number) === unitNumber);

		if (!unitMeta) {
			throw new Error(`Unit ${unitNumber} is not defined in subject.json.`);
		}

		const syllabusUrl = resolveSubjectUrl(subjectUrl, subject.syllabus);
		const syllabus = await fetchJson(syllabusUrl);
		const syllabusUnit = syllabus.units?.find(unit => Number(unit.unit) === unitNumber);

		if (!syllabusUnit) {
			throw new Error(`Unit ${unitNumber} is not defined in the syllabus data.`);
		}

		const context = createPageContext(page, subject, subjectUrl, unitMeta, syllabusUnit);
		renderBaseShell(context);

		if (unitMeta.publicationStatus !== 'ready') {
			renderScaffold(context);
			return;
		}

		const topicsUrl = resolveSubjectUrl(subjectUrl, subject.kb);
		const [topics, sourceCollections] = await Promise.all([
			fetchJson(topicsUrl),
			loadSourceCollections(subject, subjectUrl),
		]);

		const unitTopics = topics.filter(topic => Number(topic.unit) === unitNumber);
		if (!unitTopics.length) {
			throw new Error(`No published study topics were found for Unit ${unitNumber}.`);
		}

		renderReadyUnit(context, unitTopics, sourceCollections);
		setupTopicNavigation(unitTopics);
		try {
			await typesetMath(page);
		} catch (mathError) {
			console.warn('Math typesetting failed; leaving LaTeX source visible.', mathError);
		}
	} catch (error) {
		console.error('Subject unit page load failed:', error);
		renderPageError(page, error);
	}
}

function createPageContext(page, subject, subjectUrl, unitMeta, syllabusUnit) {
	const unitLabel = toRoman(Number(unitMeta.number));
	const subjectHomeUrl = new URL('./index.html', subjectUrl).href;
	const semesterHomeUrl = new URL('../index.html', subjectUrl).href;
	const siteHomeUrl = new URL('index.html', document.baseURI).href;
	const syllabusPage = subject.unitRenderer?.syllabusPage;
	const syllabusPageUrl = syllabusPage ? resolveSubjectUrl(subjectUrl, syllabusPage) : null;
	const syllabusUnitUrl = syllabusPageUrl ? `${syllabusPageUrl}#unit-${unitMeta.number}` : null;

	return {
		page,
		subject,
		subjectUrl,
		unitMeta,
		syllabusUnit,
		unitLabel,
		subjectHomeUrl,
		semesterHomeUrl,
		siteHomeUrl,
		syllabusPageUrl,
		syllabusUnitUrl,
	};
}

function renderBaseShell(context) {
	const { page, subject, unitMeta, unitLabel, siteHomeUrl, semesterHomeUrl, subjectHomeUrl } = context;
	const semesterLabel = String(subject.semester ?? '').replace('-', '.');

	document.title = `Unit ${unitLabel} · ${subject.name} · Panku's Desk`;

	page.innerHTML = `
		<div class="breadcrumbs">
			<a href="${escapeHtml(siteHomeUrl)}">Panku's Desk</a>
			<span>›</span>
			<a href="${escapeHtml(semesterHomeUrl)}">Semester ${escapeHtml(semesterLabel)}</a>
			<span>›</span>
			<a href="${escapeHtml(subjectHomeUrl)}">${escapeHtml(subject.shortName || subject.name)}</a>
			<span>›</span>
			<span>Unit ${escapeHtml(unitLabel)}</span>
		</div>
		<div id="unit-page-body"></div>
	`;
}

function renderScaffold(context) {
	const { subject, unitMeta, syllabusUnit, unitLabel, subjectHomeUrl, syllabusUnitUrl } = context;
	const body = document.getElementById('unit-page-body');
	if (!body) return;

	body.innerHTML = `
		${renderUnitHero(context, [])}
		<section class="unit-template-card">
			<div class="note-kicker">Official ${escapeHtml(subject.regulation)} scope</div>
			<h2>${escapeHtml(unitMeta.title)}</h2>
			<ul class="unit-template-scope">
				${syllabusUnit.atoms.map(atom => `<li>${formatText(atom)}</li>`).join('')}
			</ul>
			<p class="unit-template-note">The page is reserved and linked now. Full consolidated study notes will replace this scaffold when this unit is published.</p>
			<div class="unit-template-actions">
				${syllabusUnitUrl ? `<a href="${escapeHtml(syllabusUnitUrl)}">Open Unit ${escapeHtml(unitLabel)} in ${escapeHtml(subject.regulation)} syllabus →</a>` : ''}
				<a href="${escapeHtml(subjectHomeUrl)}">Back to ${escapeHtml(subject.shortName || subject.name)} →</a>
			</div>
		</section>
	`;
}

function renderReadyUnit(context, unitTopics, sourceCollections) {
	const body = document.getElementById('unit-page-body');
	if (!body) return;

	body.innerHTML = `
		${renderUnitHero(context, unitTopics)}
		${renderSyllabusBoundary(context)}
		<div class="unit-layout section">
			<aside class="unit-toc" aria-label="Unit ${escapeHtml(context.unitLabel)} topic navigation">
				<div class="toc-label">On this page</div>
				<nav id="unit-topic-nav"></nav>
				${renderPracticeNav(context)}
			</aside>

			<section class="unit-content" aria-label="Unit ${escapeHtml(context.unitLabel)} study notes">
				<div id="unit-topic-list"></div>
				${renderEndOfUnitPractice(context)}
			</section>
		</div>
	`;

	renderTopicNav(unitTopics);
	renderTopicNotes(unitTopics, context, sourceCollections);
	setupSelfCheckAccordions();
	setupExplanationAccordions();
}

function renderUnitHero(context, unitTopics) {
	const { subject, unitMeta, unitLabel, syllabusUnit, syllabusUnitUrl } = context;
	const isReady = unitMeta.publicationStatus === 'ready';
	const coreCount = unitTopics.filter(topic => topic.status === 'core').length;
	const regulation = escapeHtml(subject.regulation || 'Syllabus');

	return `
		<section class="unit-hero">
			<div>
				<div class="eyebrow">
					${escapeHtml(subject.name)}
					${syllabusUnitUrl ? ` · <a class="regulation-inline-link" href="${escapeHtml(syllabusUnitUrl)}">${regulation} ↗</a>` : ` · ${regulation}`}
				</div>
				<h1>Unit ${escapeHtml(unitLabel)}</h1>
				<p class="unit-subtitle">${escapeHtml(unitMeta.title)}</p>
				<p class="unit-description">${isReady
					? 'Complete study notes for the unit, organised for day-to-day revision and problem solving.'
					: 'This destination is in place now; the full consolidated study notes will be populated here next.'}</p>
			</div>

			${isReady ? `
				<div class="unit-hero-stats" aria-label="Unit ${escapeHtml(unitLabel)} coverage summary">
					<div><strong>${unitTopics.length}</strong><span>study topics</span></div>
					<div><strong>${syllabusUnit.atoms.length}</strong><span>${regulation} syllabus points</span></div>
					<div><strong>${coreCount}</strong><span>core topics</span></div>
				</div>
			` : ''}
		</section>
	`;
}

function renderSyllabusBoundary(context) {
	const { subject, syllabusUnit, syllabusUnitUrl } = context;
	return `
		<section class="unit-boundary section">
			<details>
				<summary>
					<span>
						<strong>Official ${escapeHtml(subject.regulation)} syllabus for this unit</strong>
						<span>${syllabusUnit.atoms.length} required syllabus points</span>
					</span>
					<span class="details-plus" aria-hidden="true">+</span>
				</summary>
				${syllabusUnitUrl ? `<div class="syllabus-source-row"><a href="${escapeHtml(syllabusUnitUrl)}">Open the ${escapeHtml(subject.shortName || subject.name)} ${escapeHtml(subject.regulation)} syllabus →</a></div>` : ''}
				<ol class="syllabus-atom-list">
					${syllabusUnit.atoms.map(atom => `<li>${formatText(atom)}</li>`).join('')}
				</ol>
			</details>
		</section>
	`;
}

function getPracticeLinks(context) {
	const practice = context.subject.practice ?? {};
	const links = [];
	const unitQuestions = practice.unitQuestions;
	const unitNumber = Number(context.unitMeta.number);
	const availableUnits = unitQuestions?.availableUnits ?? [];

	if (unitQuestions?.hrefPattern && availableUnits.map(Number).includes(unitNumber)) {
		const href = unitQuestions.hrefPattern.replace('{unit}', String(unitNumber));
		links.push({
			kind: 'unit-questions',
			label: unitQuestions.label || 'Textbook Questions',
			description: unitQuestions.description || '',
			href: new URL(href, context.subjectUrl).href,
			primary: true,
		});
	}

	if (practice.pyqs?.href) {
		links.push({
			kind: 'pyqs',
			label: practice.pyqs.label || 'PYQs',
			description: practice.pyqs.description || '',
			href: new URL(practice.pyqs.href, context.subjectUrl).href,
			primary: false,
		});
	}

	return links;
}

function renderPracticeNav(context) {
	const links = getPracticeLinks(context);
	if (!links.length) return '';
	return `
		<div class="toc-practice">
			<div class="toc-label">Practice</div>
			${links.map(link => `
				<a class="toc-practice-link" href="${escapeHtml(link.href)}">
					<span>${escapeHtml(link.label)}</span>
					<span aria-hidden="true">→</span>
				</a>
			`).join('')}
		</div>
	`;
}

function renderEndOfUnitPractice(context) {
	const links = getPracticeLinks(context);
	if (!links.length) return '';
	const primary = links.find(link => link.primary) ?? links[0];
	const secondary = links.filter(link => link !== primary);
	return `
		<section class="end-unit-practice" aria-label="End of unit practice">
			<div>
				<div class="note-kicker">Finished Unit ${escapeHtml(context.unitLabel)}?</div>
				<h2>Put the unit into practice</h2>
				<p>Move from the notes into source-backed practice while the ideas are still fresh.</p>
			</div>
			<div class="end-unit-actions">
				<a class="end-unit-primary" href="${escapeHtml(primary.href)}">Practice ${escapeHtml(primary.label)} →</a>
				${secondary.map(link => `<a class="end-unit-secondary" href="${escapeHtml(link.href)}">Browse ${escapeHtml(link.label)} →</a>`).join('')}
			</div>
		</section>
	`;
}

function renderTopicNav(unitTopics) {
	const nav = document.getElementById('unit-topic-nav');
	if (!nav) return;

	nav.innerHTML = unitTopics
		.map((topic, index) => `
			<a class="unit-toc-link" href="#${escapeHtml(topic.id)}">
				<span class="toc-index">${String(index + 1).padStart(2, '0')}</span>
				<span>${escapeHtml(topic.title)}</span>
			</a>
		`)
		.join('');
}

function renderTopicNotes(unitTopics, context, sourceCollections) {
	const list = document.getElementById('unit-topic-list');
	if (!list) return;

	list.innerHTML = unitTopics
		.map((topic, index) => renderTopic(topic, index, context, sourceCollections))
		.join('');
}

function renderTopic(topic, index, context, sourceCollections) {
	const isSupporting = topic.status === 'supporting';
	const statusLabel = isSupporting ? 'Supporting topic' : `${context.subject.regulation} core`;

	return `
		<article class="topic-note ${isSupporting ? 'supporting' : ''}" id="${escapeHtml(topic.id)}">
			<header class="topic-note-header">
				<div>
					<div class="topic-index">${String(index + 1).padStart(2, '0')}</div>
					<h2>${escapeHtml(topic.title)}</h2>
				</div>
				<span class="topic-status ${escapeHtml(topic.status)}"${isSupporting ? ' title="Useful supplied course material; not separately named as a syllabus item."' : ''}>${escapeHtml(statusLabel)}</span>
			</header>

			${renderTopicIntro(topic.intro)}
			${renderQuickRecall(topic.learn ?? [])}
			${renderSelfChecks(topic.self_checks ?? topic.questions ?? [], topic.id)}
			${renderSections(topic.sections ?? [], context)}
			${renderFormulas(topic.formulas ?? [])}
			${renderMethod(topic.method ?? [])}
			${renderCautions(topic.cautions ?? [])}
			${renderPractice(topic.practice ?? [], context)}
			${renderClassHistory(topic.class_history ?? [])}
			${renderReferenceFooter(topic, context, sourceCollections)}
		</article>
	`;
}

function renderTopicIntro(value) {
	if (!value) return '';
	return `<p class="topic-intro">${formatText(value)}</p>`;
}

function renderQuickRecall(items) {
	if (!items.length) return '';
	return `
		<section class="quick-recall" aria-label="Quick recall">
			<div class="note-kicker">Quick recall</div>
			<ul>${items.map(item => `<li>${formatText(item)}</li>`).join('')}</ul>
		</section>
	`;
}

function renderSections(sections, context) {
	if (!sections.length) return '';
	return `<div class="topic-sections">${sections.map(section => renderSection(section, context)).join('')}</div>`;
}

function renderSection(section, context) {
	const isClassNote = section.kind === 'class-note';
	const className = isClassNote ? 'note-section class-note-section' : 'note-section';
	const sourceLabel = isClassNote
		? `<div class="class-note-source-label">${escapeHtml(section.source_label || 'Priyanka\'s class notes')}</div>`
		: '';

	return `
		<section class="${className}">
			${sourceLabel}
			<div class="note-section-heading"><h3>${formatText(section.heading)}</h3></div>
			${renderSectionContent(section, context)}
		</section>
	`;
}

function renderSectionContent(section, context) {
	const figures = section.figures ?? [];
	const sideFigures = figures.filter(figure => figure.grid && Number.isInteger(Number(figure.grid.start)));
	const ordinaryFigures = figures.filter(figure => !figure.grid);

	const figuresAt = (hook, index) => ordinaryFigures
		.filter(figure => figure.after?.type === hook && Number(figure.after?.index) === index)
		.map(renderTextbookFigureRow)
		.join('');

	const sideFiguresStartingAt = index => sideFigures
		.filter(figure => Number(figure.grid.start) === index);

	let html = '';
	const paragraphs = section.paragraphs ?? [];

	for (let index = 0; index < paragraphs.length; index += 1) {
		const startingFigures = sideFiguresStartingAt(index);
		if (startingFigures.length) {
			const endIndex = Math.max(index, ...startingFigures.map(figure => Number(figure.grid.end ?? figure.grid.start)));
			const textHtml = paragraphs
				.slice(index, endIndex + 1)
				.map(paragraph => `<p>${formatText(paragraph)}</p>`)
				.join('');
			html += renderTextFigureGrid(textHtml, startingFigures);
			index = endIndex;
			continue;
		}

		html += figuresAt('before-paragraph', index);
		html += `<p>${formatText(paragraphs[index])}</p>`;
		html += figuresAt('paragraph', index);
	}

	const bullets = section.bullets ?? [];
	let bulletBuffer = [];
	const flushBullets = () => {
		if (!bulletBuffer.length) return;
		html += `<ul>${bulletBuffer.join('')}</ul>`;
		bulletBuffer = [];
	};

	bullets.forEach((item, index) => {
		bulletBuffer.push(`<li>${formatText(item)}</li>`);
		const anchoredFigures = figuresAt('bullet', index);
		if (anchoredFigures) {
			flushBullets();
			html += anchoredFigures;
		}
	});
	flushBullets();

	html += renderStudyTables(section.tables ?? []);
	html += renderExplanationAccordions(section.accordions ?? [], section.accordion_recap ?? [], section.accordion_label || 'Understand this diagram');

	const explicitlyEnded = ordinaryFigures
		.filter(figure => figure.after?.type === 'end')
		.map(renderTextbookFigureRow)
		.join('');
	html += explicitlyEnded;

	const anchored = new Set(
		figures
			.filter(figure => figure.after?.type || figure.grid)
			.map(figure => figure.src)
	);
	html += figures
		.filter(figure => !anchored.has(figure.src))
		.map(renderTextbookFigureRow)
		.join('');

	// Keep prescribed-textbook problem sets at the same logical point as the book.
	html += renderPractice(section.practice ?? [], context);

	return html;
}

function renderTextFigureGrid(textHtml, figures) {
	if (!figures.length) return textHtml;
	const lead = figures[0];
	const side = lead.grid?.side === 'left' ? 'left' : 'right';
	const size = lead.grid?.size || lead.size || 'medium';
	const figureHtml = figures.map(renderTextbookFigure).join('');
	const text = `<div class="textbook-grid-text">${textHtml}</div>`;
	const visual = `<div class="textbook-grid-visual">${figureHtml}</div>`;

	return `
		<div class="textbook-grid-row textbook-grid-row--side textbook-grid-row--${escapeHtml(side)} textbook-grid-row--${escapeHtml(size)}">
			${side === 'left' ? `${visual}${text}` : `${text}${visual}`}
		</div>
	`;
}

function renderTextbookFigureRow(figure) {
	const size = figure.size || 'medium';
	return `
		<div class="textbook-grid-row textbook-grid-row--full textbook-grid-row--${escapeHtml(size)}">
			<div class="textbook-grid-visual">${renderTextbookFigure(figure)}</div>
		</div>
	`;
}

function renderStudyTables(tables) {
	if (!tables.length) return '';

	return tables.map(table => {
		const headers = table.headers ?? [];
		const rows = table.rows ?? [];
		if (!headers.length || !rows.length) return '';

		return `
			<div class="study-table-wrap">
				<table class="study-table">
					${table.caption ? `<caption>${formatText(table.caption)}</caption>` : ''}
					<thead>
						<tr>${headers.map(header => `<th scope="col">${formatText(header)}</th>`).join('')}</tr>
					</thead>
					<tbody>
						${rows.map(row => `<tr>${row.map(cell => `<td>${renderStudyTableCell(cell)}</td>`).join('')}</tr>`).join('')}
					</tbody>
				</table>
			</div>
		`;
	}).join('');
}


function renderStudyTableCell(cell) {
	if (cell && typeof cell === 'object' && cell.type === 'image') {
		const src = escapeHtml(cell.src);
		const alt = escapeHtml(cell.alt || '');
		const width = Number(cell.width) || 160;
		const height = Number(cell.height) || width;
		const sizeClass = cell.size ? ` study-table-image--${escapeHtml(cell.size)}` : '';
		return `<img class="study-table-image${sizeClass}" src="${src}" alt="${alt}" width="${width}" height="${height}" loading="lazy">`;
	}
	return formatText(cell);
}

function renderExplanationAccordions(items, recapItems = [], label = 'Understand this diagram') {
	if (!items.length && !recapItems.length) return '';

	const isExampleGroup = /example/i.test(label);
	const accordionHtml = items.length ? `
		<div class="explanation-accordion${isExampleGroup ? ' explanation-accordion--examples' : ''}" aria-label="${escapeHtml(label)}">
			<div class="explanation-accordion-label">${escapeHtml(label)}</div>
			${items.map(item => renderExplanationAccordionItem(item, isExampleGroup)).join('')}
		</div>
	` : '';

	const recapHtml = recapItems.length ? `
		<div class="diagram-quick-recall">
			<div class="diagram-quick-recall-title">Quick way to read the diagram</div>
			<ul>${recapItems.map(item => `<li>${formatText(item)}</li>`).join('')}</ul>
		</div>
	` : '';

	return accordionHtml + recapHtml;
}

function renderExplanationAccordionItem(item, isExampleGroup) {
	if (!isExampleGroup) {
		return `
			<details class="explanation-accordion-item">
				<summary>
					<span>${formatText(item.title)}</span>
					<span class="explanation-accordion-toggle" aria-hidden="true">+</span>
				</summary>
				<div class="explanation-accordion-content">
					${(item.paragraphs ?? []).map(paragraph => `<p>${formatText(paragraph)}</p>`).join('')}
					${(item.bullets ?? []).length ? `<ul>${item.bullets.map(bullet => `<li>${formatText(bullet)}</li>`).join('')}</ul>` : ''}
				</div>
			</details>
		`;
	}

	const { questionParagraphs, solutionParagraphs } = splitExampleQuestionAndSolution(item);
	return `
		<details class="explanation-accordion-item explanation-accordion-item--example">
			<summary>
				<span class="example-summary-copy">
					<span class="example-summary-title">${formatText(item.title)}</span>
					${questionParagraphs.length ? `<span class="example-summary-question">${questionParagraphs.map(paragraph => `<span class="example-question-paragraph">${formatText(paragraph)}</span>`).join('')}</span>` : ''}
				</span>
				<span class="explanation-accordion-toggle" aria-hidden="true">+</span>
			</summary>
			<div class="explanation-accordion-content example-solution-content">
				${solutionParagraphs.map(paragraph => `<p>${formatText(paragraph)}</p>`).join('')}
				${(item.bullets ?? []).length ? `<ul>${item.bullets.map(bullet => `<li>${formatText(bullet)}</li>`).join('')}</ul>` : ''}
				${item.final_answer ? `<div class="example-final-answer"><strong>Final answer:</strong> <strong>${formatText(item.final_answer)}</strong></div>` : ''}
			</div>
		</details>
	`;
}

function splitExampleQuestionAndSolution(item) {
	const paragraphs = item.paragraphs ?? [];
	const explicitQuestion = item.question_paragraphs ?? item.questionParagraphs ?? [];
	if (explicitQuestion.length) {
		return { questionParagraphs: explicitQuestion, solutionParagraphs: paragraphs };
	}

	const solutionIndex = paragraphs.findIndex(paragraph => /^\s*Solution\b/i.test(String(paragraph)));
	if (solutionIndex > 0) {
		return {
			questionParagraphs: paragraphs.slice(0, solutionIndex),
			solutionParagraphs: paragraphs.slice(solutionIndex),
		};
	}

	if (solutionIndex === 0) {
		return { questionParagraphs: [], solutionParagraphs: paragraphs };
	}

	if (paragraphs.length) {
		return {
			questionParagraphs: [paragraphs[0]],
			solutionParagraphs: paragraphs.slice(1),
		};
	}

	return { questionParagraphs: [], solutionParagraphs: [] };
}

function setupExplanationAccordions() {
	const groups = Array.from(document.querySelectorAll('.explanation-accordion'));
	groups.forEach(group => {
		const detailsItems = Array.from(group.querySelectorAll('.explanation-accordion-item'));
		detailsItems.forEach(details => {
			details.addEventListener('toggle', () => {
				if (!details.open) return;
				detailsItems.forEach(other => {
					if (other !== details) other.open = false;
				});
			});
		});
	});
}

function renderTextbookFigure(figure) {
	if (!figure?.src || !figure?.alt) return '';
	const width = Number(figure.width);
	const height = Number(figure.height);
	const dimensions = Number.isFinite(width) && Number.isFinite(height)
		? ` width="${width}" height="${height}"`
		: '';
	const caption = figure.caption ? `<span>${escapeHtml(figure.caption)}</span>` : '';
	const page = figure.page ? `<span class="textbook-figure-page">Book p. ${escapeHtml(figure.page)}</span>` : '';
	const kindClass = figure.kind === 'class-note' ? ' class-note-figure' : '';

	return `
		<figure class="textbook-figure${kindClass}">
			<img src="${escapeHtml(figure.src)}" alt="${escapeHtml(figure.alt)}" loading="lazy" decoding="async"${dimensions}>
			${caption || page ? `<figcaption>${caption}${page}</figcaption>` : ''}
		</figure>
	`;
}

function renderSelfChecks(checks, topicId) {
	if (!checks.length) return '';

	const safeTopicId = String(topicId || 'topic').replace(/[^A-Za-z0-9_-]/g, '-');

	return `
		<section class="self-check-block" aria-label="Check yourself">
			<div class="self-check-heading">
				<div class="study-box-title">Check yourself</div>
				<span>Try the question first, then click it to reveal the answer.</span>
			</div>
			<div class="self-check-list">
				${checks.map((check, index) => {
					const questionId = `self-check-${safeTopicId}-${index + 1}-question`;
					const answerId = `self-check-${safeTopicId}-${index + 1}-answer`;
					return `
						<div class="self-check-item">
							<button
								type="button"
								class="self-check-question-button"
								id="${escapeHtml(questionId)}"
								aria-expanded="false"
								aria-controls="${escapeHtml(answerId)}"
							>
								<span class="self-check-number">Q${index + 1}</span>
								<span class="self-check-question">${formatText(check.question)}</span>
								<span class="self-check-toggle" aria-hidden="true">+</span>
							</button>
							<div
								class="self-check-answer"
								id="${escapeHtml(answerId)}"
								role="region"
								aria-labelledby="${escapeHtml(questionId)}"
								hidden
							>
								<div class="answer-label">Answer</div>
								<p>${formatText(check.answer)}</p>
							</div>
						</div>
					`;
				}).join('')}
			</div>
		</section>
	`;
}

function setupSelfCheckAccordions() {
	const buttons = Array.from(document.querySelectorAll('.self-check-question-button'));
	if (!buttons.length) return;

	buttons.forEach(button => {
		button.addEventListener('click', () => {
			const item = button.closest('.self-check-item');
			const list = button.closest('.self-check-list');
			const answerId = button.getAttribute('aria-controls');
			const answer = answerId ? document.getElementById(answerId) : null;
			if (!item || !answer) return;

			const willOpen = button.getAttribute('aria-expanded') !== 'true';

			// Behave as a real accordion: opening one answer closes the other
			// answers in the same topic's Check yourself block.
			if (willOpen && list) {
				list.querySelectorAll('.self-check-question-button[aria-expanded="true"]').forEach(openButton => {
					if (openButton === button) return;
					const openAnswerId = openButton.getAttribute('aria-controls');
					const openAnswer = openAnswerId ? document.getElementById(openAnswerId) : null;
					openButton.setAttribute('aria-expanded', 'false');
					openButton.closest('.self-check-item')?.classList.remove('is-open');
					if (openAnswer) openAnswer.hidden = true;
				});
			}

			button.setAttribute('aria-expanded', String(willOpen));
			item.classList.toggle('is-open', willOpen);
			answer.hidden = !willOpen;
		});
	});
}

function renderFormulas(formulas) {
	if (!formulas.length) return '';
	return `
		<section class="study-box formula-box">
			<div class="study-box-title">Key formulas</div>
			<div class="formula-list">${formulas.map(formula => `<div class="formula-line">${formatText(formula)}</div>`).join('')}</div>
		</section>
	`;
}

function renderMethod(steps) {
	if (!steps.length) return '';
	return `
		<section class="study-box method-box">
			<div class="study-box-title">Problem-solving method</div>
			<ol class="method-list">${steps.map(step => `<li>${formatText(step)}</li>`).join('')}</ol>
		</section>
	`;
}

function renderCautions(cautions) {
	if (!cautions.length) return '';
	return `
		<aside class="topic-cautions">
			<div class="study-box-title">Important note</div>
			${cautions.map(caution => `<p>${formatText(caution)}</p>`).join('')}
		</aside>
	`;
}

function renderPractice(practice, context) {
	if (!practice.length) return '';
	const questionLink = getPracticeLinks(context).find(link => link.kind === 'unit-questions');

	return `
		<section class="study-box practice-box">
			<div class="study-box-title">Practice from the prescribed book</div>
			<div class="practice-list">
				${practice.map(item => {
					const href = questionLink && item.group_anchor
						? `${questionLink.href}#${encodeURIComponent(item.group_anchor)}`
						: questionLink && item.anchor
							? `${questionLink.href}#question-${encodeURIComponent(item.anchor)}`
							: questionLink?.href || null;
					const content = `
						<span class="practice-page">p. ${escapeHtml(item.book_page)}</span>
						<span class="practice-type">${escapeHtml(item.type)}</span>
						<span class="practice-items">${escapeHtml(item.items)}</span>
						${href ? '<span class="practice-arrow" aria-hidden="true">→</span>' : ''}
					`;
					return href
						? `<a class="practice-item" href="${escapeHtml(href)}">${content}</a>`
						: `<div class="practice-item">${content}</div>`;
				}).join('')}
			</div>
		</section>
	`;
}

function renderClassHistory(items) {
	if (!items.length) return '';
	return `
		<section class="class-history" aria-label="Class history">
			<div class="study-box-title">Covered in class</div>
			<div class="class-history-links">
				${items.map(item => `
					<a href="${escapeHtml(item.href)}">
						<span>${escapeHtml(item.label || item.date)}</span>
						<span aria-hidden="true">→</span>
					</a>
				`).join('')}
			</div>
		</section>
	`;
}

function renderReferenceFooter(topic, context, sourceCollections) {
	const sourceRefs = topic.source_refs ?? [];
	if (!sourceRefs.length) return '';

	return `
		<footer class="topic-reference-footer">
			${renderSources(sourceRefs, context, sourceCollections)}
		</footer>
	`;
}

function renderSources(sourceRefs, context, sourceCollections) {
	if (!sourceRefs.length) return '';
	const sources = sourceRefs.map(ref => resolveSource(ref, context, sourceCollections));

	return `
		<details class="topic-sources">
			<summary>
				<span>Detailed sources · ${sources.length}</span>
				<span class="details-plus" aria-hidden="true">+</span>
			</summary>
			<ul class="source-list">
				${sources.map(source => `
					<li class="source-item">
						<span class="source-kind">${escapeHtml(source.kind)}</span>
						${source.href
							? `<a class="source-detail source-link" href="${escapeHtml(source.href)}"${isExternalUrl(source.href) ? ' target="_blank" rel="noopener"' : ''}>${escapeHtml(source.detail)} ↗</a>`
							: `<span class="source-detail">${escapeHtml(source.detail)}</span>`}
					</li>
				`).join('')}
			</ul>
		</details>
	`;
}

async function loadSourceCollections(subject, subjectUrl) {
	const definitions = subject.unitRenderer?.sources ?? [];
	if (!definitions.length) return [];

	const cache = new Map();
	const collections = [];

	for (const definition of definitions) {
		const url = resolveSubjectUrl(subjectUrl, definition.path);
		if (!cache.has(url)) cache.set(url, fetchJson(url));
		const data = await cache.get(url);
		const records = definition.collection ? getByPath(data, definition.collection) : data;
		collections.push({ definition, records: Array.isArray(records) ? records : [] });
	}

	return collections;
}

function resolveSource(ref, context, sourceCollections) {
	for (const collection of sourceCollections) {
		const { definition, records } = collection;
		const idField = definition.idField || 'source_id';
		const record = records.find(item => String(item?.[idField]) === String(ref));
		if (record) return formatSourceRecord(record, definition, context);
	}
	return { kind: 'Source', detail: ref };
}

function formatSourceRecord(record, definition, context) {
	const kind = definition.kind || 'Source';

	switch (definition.format) {
		case 'syllabus':
			return {
				kind,
				detail: record.document_pages
					? `Official ${context.subject.regulation} specification · document pp. ${record.document_pages}`
					: record.file || record.source_id || record.id,
				href: context.syllabusPageUrl && record.unit
					? `${context.syllabusPageUrl}#unit-${record.unit}`
					: context.syllabusPageUrl,
			};

		case 'book-page':
			return {
				kind,
				detail: `Textbook p. ${record.printed_page}`,
			};

		case 'lecture':
			return {
				kind,
				detail: `${record.unit ? `U${record.unit}-` : ''}${record.lecture_number != null ? String(record.lecture_number).padStart(2, '0') : ''}${record.file ? ` · ${cleanFileTitle(record.file)}` : ''}`,
			};

		case 'pdf-page':
			return { kind, detail: record.pdf_page != null ? `PDF p. ${record.pdf_page}` : record.file || record.source_id || record.id };

		case 'class-log':
			return {
				kind,
				detail: record.date ? `${formatIsoDate(record.date)} · ${record.title || 'Class notes'}` : record.title || record.id,
				href: record.href ? new URL(record.href, context.subjectUrl).href : null,
			};

		case 'external':
			return {
				kind,
				detail: record.lecture || record.topic || record.location || record.title || record.file || record.id,
				href: record.url || null,
			};

		default:
			return {
				kind,
				detail: record.detail || record.title || record.name || record.topic || record.file || record.source_id || record.id,
				href: record.url || record.href || null,
			};
	}
}

function setupTopicNavigation(unitTopics) {
	const nav = document.getElementById('unit-topic-nav');
	if (!nav) return;

	const links = Array.from(nav.querySelectorAll('.unit-toc-link'));
	const sections = unitTopics.map(topic => document.getElementById(topic.id)).filter(Boolean);
	if (!links.length || !sections.length) return;

	const setActive = id => {
		links.forEach(link => {
			const active = link.getAttribute('href') === `#${id}`;
			link.classList.toggle('is-active', active);
			if (active) link.setAttribute('aria-current', 'location');
			else link.removeAttribute('aria-current');
		});
	};

	links.forEach(link => {
		link.addEventListener('click', event => {
			const id = link.getAttribute('href')?.slice(1);
			const target = id ? document.getElementById(id) : null;
			if (!target) return;

			event.preventDefault();
			setActive(id);
			history.replaceState(null, '', `#${id}`);
			target.scrollIntoView({ behavior: 'smooth', block: 'start' });
		});
	});

	const observer = new IntersectionObserver(entries => {
		const visible = entries
			.filter(entry => entry.isIntersecting)
			.sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
		if (visible[0]?.target?.id) setActive(visible[0].target.id);
	}, {
		rootMargin: '-18% 0px -68% 0px',
		threshold: [0, 0.01, 0.15],
	});

	sections.forEach(section => observer.observe(section));

	const initialId = window.location.hash.slice(1);
	if (initialId && document.getElementById(initialId)) {
		setActive(initialId);
		requestAnimationFrame(() => document.getElementById(initialId)?.scrollIntoView({ block: 'start' }));
	} else {
		setActive(sections[0].id);
	}
}

function renderPageError(page, error) {
	page.innerHTML = `
		<div class="unit-error">
			The unit page could not be loaded. Open the site through Live Server or GitHub Pages so its JSON files can be fetched.
			${error?.message ? `<div class="unit-error-detail">${escapeHtml(error.message)}</div>` : ''}
		</div>
	`;
}

async function fetchJson(url) {
	if (!url) throw new Error('Missing JSON source URL.');
	const response = await fetch(url);
	if (!response.ok) throw new Error(`${url} returned ${response.status}`);
	return response.json();
}

function resolveSubjectUrl(subjectUrl, relativePath) {
	if (!relativePath) throw new Error('Missing subject resource path.');
	return new URL(relativePath, subjectUrl).href;
}

function getByPath(value, path) {
	return String(path).split('.').reduce((current, key) => current?.[key], value);
}

function cleanFileTitle(filename) {
	return String(filename)
		.replace(/\.[^.]+$/i, '')
		.replace(/^\d+_/, '')
		.replaceAll('_', ' ');
}

function formatIsoDate(value) {
	const match = String(value || '').match(/^(\d{4})-(\d{2})-(\d{2})$/);
	if (!match) return String(value || '');
	const [, year, month, day] = match;
	const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
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
	return escapeHtml(value)
		.replace(/\b([A-Za-z][A-Za-z0-9]*)_\{?([A-Za-z0-9]+)\}?/g, '$1<sub>$2</sub>');
}

let mathJaxPromise = null;

async function typesetMath(root) {
	if (!root || !/[\\][(\[]/.test(root.textContent || '')) return;
	await ensureMathJax();
	if (window.MathJax?.typesetPromise) {
		await window.MathJax.typesetPromise([root]);
	}
}

function ensureMathJax() {
	if (window.MathJax?.typesetPromise) return Promise.resolve(window.MathJax);
	if (mathJaxPromise) return mathJaxPromise;

	mathJaxPromise = new Promise((resolve, reject) => {
		window.MathJax = {
			tex: {
				inlineMath: [['\\\(', '\\\)']],
				displayMath: [['\\\[', '\\\]']],
				processEscapes: true,
			},
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
	const numerals = [
		[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
		[100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],
		[10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I'],
	];
	let number = Number(value);
	let result = '';
	for (const [amount, numeral] of numerals) {
		while (number >= amount) {
			result += numeral;
			number -= amount;
		}
	}
	return result || String(value);
}

function isExternalUrl(value) {
	try {
		return new URL(value).origin !== window.location.origin;
	} catch {
		return false;
	}
}

function escapeHtml(value) {
	return String(value ?? '')
		.replaceAll('&', '&amp;')
		.replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;')
		.replaceAll("'", '&#039;');
}

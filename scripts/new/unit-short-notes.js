(function () {
'use strict';

document.addEventListener('DOMContentLoaded', () => initUnitShortNotes());

async function initUnitShortNotes() {
	const page = document.querySelector('.unit-short-notes-page[data-unit][data-subject-json]');
	if (!page) return;

	try {
		const unitNumber = Number(page.dataset.unit);
		const subjectUrl = new URL(page.dataset.subjectJson, document.baseURI);
		const subject = await fetchJson(subjectUrl.href);
		const unitMeta = (subject.units || []).find(unit => Number(unit.number) === unitNumber);
		if (!unitMeta) throw new Error(`Unit ${unitNumber} is not defined.`);

		const cfg = subject.shortNotes || {};
		if (!cfg.data) throw new Error('No short-notes data source is configured for this subject.');
		const bank = await fetchJson(new URL(cfg.data, subjectUrl).href);
		const unitNotes = bank?.units?.[String(unitNumber)];
		if (!unitNotes) throw new Error(`No short notes are available for Unit ${unitNumber}.`);

		renderPage(page, subject, subjectUrl, unitMeta, unitNotes, bank);
		window.PankuStudyUI?.initIndexedNav?.(page);
		wireDiagramFallbacks(page);
		try {
			await window.PankuStudyUI?.typesetMath?.(page);
		} catch (mathError) {
			console.warn('Math typesetting failed; leaving LaTeX source visible.', mathError);
		}
		revealHashTarget(page);
	} catch (error) {
		console.error('Unit short notes failed to load:', error);
		page.innerHTML = `<div class="short-notes-error">Short notes could not be loaded.${error?.message ? ` ${escapeHtml(error.message)}` : ''}</div>`;
	}
}

function renderPage(page, subject, subjectUrl, unitMeta, unitNotes, bank) {
	const unitNumber = Number(unitMeta.number);
	const unitLabel = toRoman(unitNumber);
	const subjectHome = new URL('./index.html', subjectUrl).href;
	const semesterHome = new URL('../index.html', subjectUrl).href;
	const siteHome = new URL('index.html', document.baseURI).href;
	const semesterLabel = String(subject.semester || '').replace('-', '.');
	const resourceNav = window.PankuUnitResourceNav?.render?.({ subject, subjectUrl, unitNumber, active: 'short-notes' }) || '';

	document.title = `Unit ${unitLabel} Short Notes · ${subject.shortName || subject.name} · Panku's Desk`;

	page.innerHTML = `
		<div class="breadcrumbs">
			<a href="${escapeHtml(siteHome)}">Panku's Desk</a><span>›</span>
			<a href="${escapeHtml(semesterHome)}">Semester ${escapeHtml(semesterLabel)}</a><span>›</span>
			<a href="${escapeHtml(subjectHome)}">${escapeHtml(subject.shortName || subject.name)}</a><span>›</span>
			<span>Unit ${escapeHtml(unitLabel)} Short Notes</span>
		</div>

		<section class="short-notes-hero">
			<div class="eyebrow">${escapeHtml(subject.name)} · Unit ${escapeHtml(unitLabel)}</div>
			<h1>Short Notes</h1>
			<p>${escapeHtml(unitMeta.title)}</p>
			<p class="short-notes-policy">Teacher-shared pages are preserved as supplied. Any PankusDesk completion is visibly marked <strong>AI-generated</strong> and is tuned to the R25 syllabus and in-scope semester PYQs.</p>
		</section>

		${resourceNav}
		${renderProvenanceSummary(unitNotes)}
		<div class="study-index-layout section short-notes-index-layout">
			${renderShortNotesIndex(unitNotes)}
			<div class="study-index-content short-notes-index-content">
				${unitNotes.teacher ? renderTeacherSection(unitNotes.teacher) : ''}
				${unitNotes.ai_boundary ? renderAiBoundary(unitNotes.ai_boundary) : ''}
				${renderAiSectionGroup(unitNotes, bank)}
			</div>
		</div>
	`;
}

function renderShortNotesIndex(unitNotes) {
	const teacherPages = Array.isArray(unitNotes.teacher?.pages) ? unitNotes.teacher.pages : [];
	const aiSections = Array.isArray(unitNotes.ai_sections) ? unitNotes.ai_sections : [];
	if (!teacherPages.length && !aiSections.length) return '';

	let offset = 0;
	const renderLinks = items => items.map(item => {
		offset += 1;
		return `<a class="study-index-link" data-index-target="${escapeHtml(item.id)}" href="${escapeHtml(buildShortNotesHashHref(item.id))}">
			<span class="study-index-number">${String(offset).padStart(2, '0')}</span>
			<span>${escapeHtml(item.title)}</span>
		</a>`;
	}).join('');

	const teacherItems = teacherPages.map(item => ({
		id: `teacher-page-${Number(item.number)}`,
		title: item.title || `Teacher note page ${Number(item.number)}`,
	}));
	const aiItems = aiSections.map(item => ({ id: item.id, title: item.title || 'AI-generated note' }));
	const mixed = teacherItems.length && aiItems.length;

	return `<aside class="study-index-toc" aria-label="Short notes topic navigation">
		<div class="study-index-label">On this page</div>
		<div class="study-index-nav">
			${teacherItems.length ? `<div class="study-index-group">${mixed ? '<div class="study-index-group-label">Teacher notes</div>' : ''}<nav>${renderLinks(teacherItems)}</nav></div>` : ''}
			${aiItems.length ? `<div class="study-index-group">${mixed ? '<div class="study-index-group-label">AI-generated</div>' : ''}<nav>${renderLinks(aiItems)}</nav></div>` : ''}
		</div>
	</aside>`;
}

function buildShortNotesHashHref(id) {
	const url = new URL(window.location.href);
	url.hash = id;
	return `${url.pathname}${url.search}${url.hash}`;
}

function renderProvenanceSummary(unitNotes) {
	const mode = unitNotes.mode || 'ai';
	if (mode === 'teacher') {
		return `<section class="short-notes-provenance is-teacher" aria-label="Short notes provenance">
			<span class="short-notes-provenance-badge">Teacher-shared</span>
			<p>This unit contains the SE1 revision notes shared by Priyanka's BEE teacher.</p>
		</section>`;
	}
	if (mode === 'mixed') {
		return `<section class="short-notes-provenance is-mixed" aria-label="Short notes provenance">
			<span class="short-notes-provenance-badge">Teacher + AI</span>
			<p>The teacher-shared pages appear first. Only the uncovered R25 portion is completed below, with every generated topic marked AI-generated.</p>
		</section>`;
	}
	return `<section class="short-notes-provenance is-ai" aria-label="Short notes provenance">
		<span class="short-notes-provenance-badge">AI-generated</span>
		<p>${escapeHtml(unitNotes.ai_intro || 'These revision notes are AI-generated for the R25 syllabus.')}</p>
	</section>`;
}

function renderTeacherSection(teacher) {
	const pdfHref = teacher.pdf ? new URL(teacher.pdf, document.baseURI).href : '';
	const pages = Array.isArray(teacher.pages) ? teacher.pages : [];
	return `
		<section class="short-notes-teacher section" aria-labelledby="teacher-notes-heading">
			<header class="short-notes-section-header">
				<div>
					<div class="short-notes-source-badge is-teacher">Teacher-shared</div>
					<h2 id="teacher-notes-heading">${escapeHtml(teacher.heading || 'Teacher Notes')}</h2>
					<p><strong>${escapeHtml(teacher.label || '')}</strong></p>
					<p>${escapeHtml(teacher.description || '')}</p>
				</div>
				${pdfHref ? `<a class="short-notes-pdf-link" href="${escapeHtml(pdfHref)}" target="_blank" rel="noopener">View original PDF ↗</a>` : ''}
			</header>
			<div class="teacher-note-pages">${pages.map((item, index) => renderTeacherPage(item, index)).join('')}</div>
		</section>
	`;
}

function renderTeacherPage(item, index) {
	const src = item.src ? new URL(item.src, document.baseURI).href : '';
	if (!src) return '';
	return `<figure class="teacher-note-page" id="teacher-page-${Number(item.number)}">
		<a class="teacher-note-image-link" href="${escapeHtml(src)}" target="_blank" rel="noopener" aria-label="Open teacher note page ${Number(item.number)} at full size">
			<img src="${escapeHtml(src)}" alt="${escapeHtml(item.alt || item.title || 'Teacher-shared BEE notes')}" ${index === 0 ? 'fetchpriority="high"' : 'loading="lazy"'} decoding="async">
		</a>
		<figcaption><span>Page ${Number(item.number)}</span><strong>${escapeHtml(item.title || '')}</strong></figcaption>
	</figure>`;
}

function renderAiBoundary(boundary) {
	return `<section class="short-notes-ai-boundary" role="note" aria-label="Teacher notes end and AI-generated notes begin">
		<div class="short-notes-ai-boundary-kicker">AI-generated continuation begins below</div>
		<h2>${escapeHtml(boundary.title || 'Teacher-shared notes end here')}</h2>
		<p>${escapeHtml(boundary.text || '')}</p>
	</section>`;
}

function renderAiSectionGroup(unitNotes) {
	const sections = Array.isArray(unitNotes.ai_sections) ? unitNotes.ai_sections : [];
	if (!sections.length) return '';
	const heading = unitNotes.mode === 'mixed' ? 'AI-generated completion' : 'AI-generated short notes';
	return `<section class="short-notes-ai section" aria-labelledby="ai-notes-heading">
		<header class="short-notes-section-header">
			<div>
				<div class="short-notes-source-badge is-ai">AI-generated</div>
				<h2 id="ai-notes-heading">${escapeHtml(heading)}</h2>
				<p>Revision notes for the uncovered R25 material, with extra emphasis where the supplied semester papers repeatedly test a topic.</p>
			</div>
		</header>
		<div class="short-notes-ai-list">${sections.map(renderAiCard).join('')}</div>
	</section>`;
}

function renderAiCard(item) {
	const paragraphs = Array.isArray(item.paragraphs) ? item.paragraphs : [];
	const bullets = Array.isArray(item.bullets) ? item.bullets : [];
	const derivation = Array.isArray(item.derivation) ? item.derivation : [];
	const formulae = Array.isArray(item.formulae) ? item.formulae : [];
	const pyqFocus = Array.isArray(item.pyq_focus) ? item.pyq_focus : [];
	const diagrams = Array.isArray(item.diagrams) ? item.diagrams : [];
	const studyGroups = Array.isArray(item.study_groups) ? item.study_groups : [];
	return `<article class="short-note-card" id="${escapeHtml(item.id || '')}">
		<header class="short-note-card-header">
			<div><span class="short-note-ai-badge">AI-generated</span><h3>${escapeHtml(item.title || '')}</h3></div>
		</header>
		<div class="short-note-card-body">
			${pyqFocus.length ? renderPyqFocus(pyqFocus) : ''}
			${paragraphs.map(text => `<p>${escapeHtml(text)}</p>`).join('')}
			${bullets.length ? `<ul>${bullets.map(text => `<li>${escapeHtml(text)}</li>`).join('')}</ul>` : ''}
			${studyGroups.length ? renderStudyGroups(studyGroups) : ''}
			${derivation.length ? renderDerivation(derivation) : ''}
			${item.table ? renderTable(item.table) : ''}
			${formulae.length ? `<div class="short-note-formulas">${formulae.map(renderFormula).join('')}</div>` : ''}
			${diagrams.length ? `<div class="short-note-diagram-grid">${diagrams.map(renderDiagram).join('')}</div>` : ''}
			${item.caution ? `<div class="short-note-caution"><strong>Source caution</strong><p>${escapeHtml(item.caution)}</p></div>` : ''}
			${item.key_point ? `<div class="short-note-key-point"><strong>Key point</strong><p>${escapeHtml(item.key_point)}</p></div>` : ''}
		</div>
	</article>`;
}

function renderPyqFocus(items) {
	return `<div class="short-note-pyq-focus"><div class="short-note-mini-label">PYQ focus</div><ul>${items.map(text => `<li>${escapeHtml(text)}</li>`).join('')}</ul></div>`;
}

function renderStudyGroups(groups) {
	return `<div class="short-note-study-groups" aria-label="Detailed revision notes">${groups.map((group, index) => renderStudyGroup(group, index)).join('')}</div>`;
}

function renderStudyGroup(group, index) {
	const paragraphs = Array.isArray(group?.paragraphs) ? group.paragraphs : [];
	const bullets = Array.isArray(group?.bullets) ? group.bullets : [];
	const steps = Array.isArray(group?.steps) ? group.steps : [];
	const formulae = Array.isArray(group?.formulae) ? group.formulae : [];
	return `<section class="short-note-study-group">
		<h4><span class="short-note-study-number">${index + 1}</span>${escapeHtml(group?.heading || 'Revision point')}</h4>
		${paragraphs.map(text => `<p>${escapeHtml(text)}</p>`).join('')}
		${bullets.length ? `<ul>${bullets.map(text => `<li>${escapeHtml(text)}</li>`).join('')}</ul>` : ''}
		${steps.length ? `<ol class="short-note-study-steps">${steps.map(text => `<li>${escapeHtml(text)}</li>`).join('')}</ol>` : ''}
		${formulae.length ? `<div class="short-note-formulas is-compact">${formulae.map(renderFormula).join('')}</div>` : ''}
	</section>`;
}

function renderDerivation(items) {
	return `<div class="short-note-derivation"><div class="short-note-mini-label">Derivation / method</div><ol>${items.map(text => `<li>${escapeHtml(text)}</li>`).join('')}</ol></div>`;
}

function renderTable(table) {
	const headers = Array.isArray(table?.headers) ? table.headers : [];
	const rows = Array.isArray(table?.rows) ? table.rows : [];
	if (!headers.length || !rows.length) return '';
	return `<div class="short-note-table-wrap"><table class="short-note-table"><thead><tr>${headers.map(cell => `<th>${escapeHtml(cell)}</th>`).join('')}</tr></thead><tbody>${rows.map(row => `<tr>${row.map(cell => `<td>${escapeHtml(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
}

function renderFormula(formula) {
	if (!formula?.latex) return '';
	return `<div class="short-note-formula">
		${formula.label ? `<div class="short-note-formula-label">${escapeHtml(formula.label)}</div>` : ''}
		<div class="short-note-formula-math">\\[${escapeHtml(formula.latex)}\\]</div>
	</div>`;
}

function renderDiagram(item) {
	const src = item.src ? new URL(item.src, document.baseURI).href : '';
	const figure = item.figure || 'Figure';
	const title = item.title || 'Diagram';
	const placeholderKicker = item.placeholder_label || (item.source_label ? 'Educational diagram placeholder' : 'Image placeholder');
	const teachingNote = item.teaching_note ? `<div class="short-note-diagram-note">${escapeHtml(item.teaching_note)}</div>` : '';
	const sourceLabel = item.source_label ? `<div class="short-note-diagram-source">${escapeHtml(item.source_label)}</div>` : '';
	const targetPath = item.target_path ? `<span>Save as: <code>${escapeHtml(item.target_path)}</code></span>` : '';
	const searchQuery = item.search_query ? `<div class="short-note-diagram-search"><strong>Google Images search</strong><code>${escapeHtml(item.search_query)}</code></div>` : '';
	const aiPrompt = item.ai_prompt ? `<details class="short-note-diagram-ai-prompt"><summary>If image search fails: AI-generation prompt</summary><p>${escapeHtml(item.ai_prompt)}</p></details>` : '';
	return `<figure class="short-note-diagram" data-diagram-fallback>
		<div class="short-note-diagram-media">
			${src ? `<img src="${escapeHtml(src)}" alt="${escapeHtml(item.alt || `${figure} · ${title}`)}" loading="lazy" decoding="async">` : ''}
			<div class="short-note-diagram-placeholder" ${src ? 'hidden' : ''}>
				<div class="short-note-diagram-kicker">${escapeHtml(placeholderKicker)}</div>
				<strong>${escapeHtml(figure)} · ${escapeHtml(title)}</strong>
				${sourceLabel}
				${item.page ? `<span>Textbook p. ${Number(item.page)}</span>` : ''}
				${item.filename ? `<span>Rename image to: <code>${escapeHtml(item.filename)}</code></span>` : ''}
				${targetPath}
				${searchQuery}
				${aiPrompt}
			</div>
		</div>
		${teachingNote}
		<figcaption>${escapeHtml(item.caption || `${figure} · ${title}${item.page ? ` · p. ${Number(item.page)}` : ''}`)}</figcaption>
	</figure>`;
}

function wireDiagramFallbacks(page) {
	page.querySelectorAll('[data-diagram-fallback]').forEach(figure => {
		const img = figure.querySelector('img');
		const placeholder = figure.querySelector('.short-note-diagram-placeholder');
		if (!img || !placeholder) return;
		const fail = () => { img.hidden = true; placeholder.hidden = false; figure.classList.add('is-placeholder'); };
		img.addEventListener('error', fail, { once: true });
		if (img.complete && !img.naturalWidth) fail();
	});
}

function revealHashTarget(page) {
	if (!window.location.hash) return;
	requestAnimationFrame(() => {
		const id = decodeURIComponent(window.location.hash.slice(1));
		const target = page.querySelector(`#${cssEscape(id)}`);
		if (target) target.scrollIntoView({ block: 'start' });
	});
}

function cssEscape(value) {
	if (window.CSS?.escape) return window.CSS.escape(value);
	return String(value).replace(/[^a-zA-Z0-9_-]/g, '\\$&');
}

async function fetchJson(url) {
	const response = await fetch(url, { cache: 'no-store' });
	if (!response.ok) throw new Error(`${response.status} ${response.statusText}`);
	return response.json();
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

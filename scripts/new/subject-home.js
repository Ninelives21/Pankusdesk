(function () {
document.addEventListener('DOMContentLoaded', () => {
	initSubjectHome();
});

async function initSubjectHome() {
	const page = document.querySelector('.subject-page');
	if (!page) return;

	try {
		const subjectUrl = new URL(page.dataset.subjectJson, document.baseURI);
		const syllabusUrl = new URL(page.dataset.syllabusJson, document.baseURI);
		const kbStatusUrl = new URL(page.dataset.kbStatusJson, document.baseURI);

		const [subject, syllabus, kbStatus] = await Promise.all([
			fetchJson(subjectUrl.href),
			fetchJson(syllabusUrl.href),
			fetchJson(kbStatusUrl.href),
		]);

		renderSubjectIdentity(subject);
		renderKbStatus(subject, kbStatus);
		renderUnits(subject, syllabus, kbStatus, subjectUrl);
		renderPracticeLinks(subject, subjectUrl);
	} catch (error) {
		console.error('Subject page load failed:', error);
		const grid = document.querySelector('[data-unit-grid]');
		if (grid) {
			grid.innerHTML = '<div class="unit-error">Subject metadata could not be loaded. Open this page through Live Server or GitHub Pages so the JSON files can be fetched.</div>';
		}
	}
}

async function fetchJson(url) {
	if (!url) throw new Error('Missing JSON source URL.');
	const response = await fetch(url);
	if (!response.ok) throw new Error(`${url} returned ${response.status}`);
	return response.json();
}

function renderSubjectIdentity(subject) {
	setText('[data-subject-name]', subject.name);
	setText('[data-subject-code]', subject.code);
	setText('[data-subject-credits]', `${subject.credits} credits`);
}

function renderKbStatus(subject, kbStatus) {
	setText('[data-unit-count]', subject.units.length);
	setText('[data-r25-count]', kbStatus.r25_atom_count);
	setText('[data-gap-count]', kbStatus.gap_filled_topic_ids.length);
	const sourceGaps = Number(kbStatus.source_gap_count ?? 0);
	setText('[data-kb-label]', sourceGaps === 0 ? `${subject.regulation} coverage checked` : `${sourceGaps} source gaps`);
}

function renderUnits(subject, syllabus, kbStatus, subjectUrl) {
	const grid = document.querySelector('[data-unit-grid]');
	if (!grid) return;

	const syllabusByUnit = new Map(syllabus.units.map(unit => [Number(unit.unit), unit]));
	const supplementedUnits = new Set(
		(kbStatus.gap_filled_topic_ids ?? [])
			.map(topicId => Number(topicId.match(/^u(\d+)-/)?.[1]))
			.filter(Number.isFinite),
	);

	grid.innerHTML = subject.units.map(unit => {
		const syllabusUnit = syllabusByUnit.get(Number(unit.number));
		const atoms = syllabusUnit?.atoms ?? [];
		const preview = buildAtomPreview(atoms);
		const hasSupplement = supplementedUnits.has(Number(unit.number));
		const href = new URL(`unit-${unit.number}.html`, subjectUrl).href;
		return `
			<a class="unit-card" href="${escapeHtml(href)}">
				<div class="unit-card-top">
					<div class="unit-number">Unit ${unit.number}</div>
					${hasSupplement ? '<span class="unit-badge">Supplemented source</span>' : ''}
				</div>
				<h2>${escapeHtml(unit.title)}</h2>
				<p class="unit-topic-preview">${escapeHtml(preview)}</p>
				<div class="unit-card-footer">
					<span>${atoms.length} ${escapeHtml(subject.regulation)} syllabus points</span>
					<strong>Open unit →</strong>
				</div>
			</a>
		`;
	}).join('');
}

function renderPracticeLinks(subject, subjectUrl) {
	const pyqLink = document.querySelector('[data-pyq-link]');
	const pyq = subject.practice?.pyqs;
	if (pyqLink && pyq?.href) {
		pyqLink.href = new URL(pyq.href, subjectUrl).href;
	}
}

function buildAtomPreview(atoms) {
	if (!atoms.length) return 'Unit syllabus metadata unavailable.';
	const visible = atoms.slice(0, 5);
	const remaining = atoms.length - visible.length;
	return visible.join(' · ') + (remaining > 0 ? ` · +${remaining} more` : '');
}

function setText(selector, value) {
	const element = document.querySelector(selector);
	if (element && value !== undefined && value !== null) element.textContent = value;
}

function escapeHtml(value) {
	return String(value ?? '')
		.replaceAll('&', '&amp;')
		.replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;')
		.replaceAll("'", '&#039;');
}
})();

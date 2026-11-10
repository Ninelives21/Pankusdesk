(function () {
'use strict';

document.addEventListener('DOMContentLoaded', initSubjectHome);

async function initSubjectHome() {
	const page = document.querySelector('.subject-home');
	if (!page) return;
	// Resource-only subjects use the same card markup without a textbook KB.
	if (!page.dataset.subjectJson) {
		page.dataset.homeReady = 'true';
		revealFragment(page);
		return;
	}
	try {
		const subjectUrl = new URL(page.dataset.subjectJson, document.baseURI);
		const response = await fetch(subjectUrl.href, { cache: 'no-store' });
		if (!response.ok) throw new Error(`Subject metadata returned ${response.status}`);
		const subject = await response.json();
		for (const [selector, value] of [['[data-subject-name]', subject.name], ['[data-subject-code]', subject.code], ['[data-subject-credits]', subject.credits == null ? null : `${subject.credits} credits`]]) {
			const target = page.querySelector(selector);
			if (target && value != null) target.textContent = value;
		}
		renderStudyResources(subject, subjectUrl);
		renderTextbookUnits(subject, subjectUrl);
		page.dataset.homeReady = 'true';
		revealFragment(page);
	} catch (error) {
		console.error('Subject page load failed:', error);
		page.querySelectorAll('[data-study-resources], [data-unit-grid]').forEach(target => {
			target.innerHTML = '<p class="unit-error" role="alert">Study links could not be loaded. Please reload the page.</p>';
		});
	}
}

function revealFragment(page) {
	if (!location.hash) return;
	let id;
	try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
	const target = document.getElementById(id);
	if (target && page.contains(target)) requestAnimationFrame(() => target.scrollIntoView({ block: 'start' }));
}

function renderTextbookUnits(subject, subjectUrl) {
	const list = document.querySelector('[data-unit-grid]');
	if (!list) return;
	const questions = subject.practice?.unitQuestions;
	const questionUnits = new Set((questions?.availableUnits || []).map(Number));
	list.innerHTML = (subject.units || []).map(unit => {
		const unitHref = new URL(`unit-${unit.number}.html`, subjectUrl).href;
		const state = unit.publicationStatus;
		const stateText = state === 'ready' ? 'Text available' : state === 'draft' ? 'Text in progress' : 'Text not added yet';
		const questionHref = questionUnits.has(Number(unit.number)) && questions?.hrefPattern
			? new URL(questions.hrefPattern.replace('{unit}', unit.number), subjectUrl).href : null;
		return `<div class="textbook-unit-row">
			<div class="textbook-unit-copy"><span class="unit-number">Unit ${escapeHtml(unit.number)}</span>
				<h3>${escapeHtml(unit.title)}</h3><span class="textbook-unit-state">${stateText}</span></div>
			<div class="textbook-unit-actions">
				<a href="${escapeHtml(unitHref)}" aria-label="${state === 'scaffold' ? 'View outline' : 'Read textbook notes'}: Unit ${escapeHtml(unit.number)} · ${escapeHtml(unit.title)}">${state === 'scaffold' ? 'View outline' : 'Read notes'} →</a>
				${questionHref ? `<a href="${escapeHtml(questionHref)}" aria-label="Textbook questions: Unit ${escapeHtml(unit.number)} · ${escapeHtml(unit.title)}">Book questions →</a>` : ''}
			</div>
		</div>`;
	}).join('');
}

// Use the established configuration, including the grouped Chemistry revision
// entries. No metadata migration is needed, including for unmerged content PRs.
function resourceKind(entry) {
	if (entry.practiceKey === 'pyqs') return 'pyqs';
	if (entry.practiceKey === 'schoolGuidance') return 'question-sets';
	if (entry.unitResources || /end.sem|revision/i.test(entry.title || '')) return 'revision';
	if (/worksheet/i.test(entry.href || '')) return 'worksheets';
	return 'other';
}

function isAvailable(resource) {
	return Boolean(resource.href) && resource.status !== 'scaffold'
		&& !/not\s+(?:yet\s+)?(?:added|available|integrated)|coming soon/i.test(resource.state || '');
}

function unitLink(unit, subject, href, state) {
	const metadata = subject.units?.find(item => Number(item.number) === Number(unit.number));
	const title = metadata?.title || unit.title || '';
	return `<li class="resource-unit-item">
		<a href="${escapeHtml(href)}"><span class="resource-unit-number">Unit ${escapeHtml(unit.number)}</span><span>${escapeHtml(title)}</span><span aria-hidden="true">→</span></a>
		${state ? `<small>${escapeHtml(state)}</small>` : ''}
	</li>`;
}

function renderStudyResources(subject, subjectUrl) {
	const grid = document.querySelector('[data-study-resources]');
	if (!grid) return;
	const cards = [];
	const classNotes = subject.classNotes;
	if (classNotes?.hrefPattern && classNotes.availableUnits?.length) {
		const numbers = [...classNotes.availableUnits].map(Number).sort((a, b) => a - b);
		cards.push({ order: 0, html: `<article class="study-tool-card resource-hub-card" data-resource-kind="class-notes">
			<div class="tool-label">College learning</div><h3>Class Notes</h3>
			<p>${escapeHtml(classNotes.label || 'Class notes')} · Organised by unit.</p>
			<ul class="resource-unit-links">${numbers.map(number => unitLink({ number }, subject,
				new URL(classNotes.hrefPattern.replace('{unit}', number), subjectUrl).href)).join('')}</ul>
		</article>` });
	}
	const order = { revision: 1, pyqs: 2, worksheets: 3, 'question-sets': 4, other: 5 };
	for (const entry of subject.studyResources || []) {
		const kind = resourceKind(entry);
		if (Array.isArray(entry.unitResources)) {
			const available = entry.unitResources.filter(isAvailable);
			if (!available.length) continue;
			const pending = entry.unitResources.filter(unit => !isAvailable(unit));
			cards.push({ order: order[kind], html: `<article class="study-tool-card resource-hub-card" id="${escapeHtml(entry.id || 'unit-revision')}" data-resource-kind="${kind}">
				<div class="tool-label">Revision</div><h3>${escapeHtml(entry.title)}</h3><p>${escapeHtml(entry.description || '')}</p>
				<ul class="resource-unit-links">${available.map(unit => unitLink(unit, subject, new URL(unit.href, subjectUrl).href, unit.state)).join('')}</ul>
				${pending.length ? `<p class="resource-availability">Not added yet: ${pending.map(unit => `Unit ${escapeHtml(unit.number)}`).join(', ')}.</p>` : ''}
			</article>` });
			continue;
		}
		const resource = { ...subject.practice?.[entry.practiceKey], ...entry };
		if (!isAvailable(resource)) continue;
		cards.push({ order: order[kind], html: renderResourceCard(resource, subjectUrl, kind) });
	}
	cards.sort((a, b) => a.order - b.order);
	grid.classList.toggle('study-tool-grid-single', cards.length === 1);
	grid.innerHTML = cards.map(card => card.html).join('') || '<p class="resource-availability">College and exam resources have not been added yet.</p>';
}

function renderResourceCard(resource, subjectUrl, kind) {
	const href = new URL(resource.href, subjectUrl).href;
	return `<article class="study-tool-card resource-hub-card" data-resource-kind="${kind}">
		<div class="tool-label">${escapeHtml(resource.label || '')}</div><h3>${escapeHtml(resource.title)}</h3>
		${resource.description ? `<p>${escapeHtml(resource.description)}</p>` : ''}
		${resource.state ? `<span class="tool-state">${escapeHtml(resource.state)}</span>` : ''}
		<a class="resource-open-link" href="${escapeHtml(href)}">${escapeHtml(resource.action || 'Open resource')} →</a>
	</article>`;
}

function escapeHtml(value) {
	return String(value ?? '').replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;').replaceAll("'", '&#039;');
}
}());

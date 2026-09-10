(function () {
'use strict';

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

function unitIsAvailable(values, unitNumber) {
	return Array.isArray(values) && values.map(Number).includes(Number(unitNumber));
}

function getNeighbourUnits(subject, unitNumber) {
	const units = Array.isArray(subject?.units)
		? subject.units
			.filter(unit => Number.isInteger(Number(unit?.number)) && Number(unit.number) > 0)
			.slice()
			.sort((a, b) => Number(a.number) - Number(b.number))
		: [];
	const index = units.findIndex(unit => Number(unit.number) === Number(unitNumber));
	if (index < 0) return { previous: null, next: null };
	return {
		previous: index > 0 ? units[index - 1] : null,
		next: index < units.length - 1 ? units[index + 1] : null,
	};
}

function renderNeighbourLink(unit, direction, subjectUrl) {
	if (!unit) return '';
	const number = Number(unit.number);
	const unitLabel = toRoman(number);
	const title = String(unit.title || '').trim();
	const prefix = direction === 'previous' ? '← ' : '';
	const suffix = direction === 'next' ? ' →' : '';
	return `
		<a class="unit-neighbour-link is-${escapeHtml(direction)}" href="${escapeHtml(new URL(`unit-${number}.html`, subjectUrl).href)}" aria-label="${escapeHtml(`${direction === 'previous' ? 'Previous' : 'Next'} unit: Unit ${unitLabel}${title ? `, ${title}` : ''}`)}">
			<span class="unit-neighbour-kicker">${escapeHtml(direction === 'previous' ? 'Previous unit' : 'Next unit')}</span>
			<span class="unit-neighbour-main">${escapeHtml(`${prefix}Unit ${unitLabel}${suffix}`)}</span>
			${title ? `<span class="unit-neighbour-title">${escapeHtml(title)}</span>` : ''}
		</a>
	`;
}

function render({ subject, subjectUrl, unitNumber, active = 'text' }) {
	if (!subject || !subjectUrl || !unitNumber) return '';
	const unitLabel = toRoman(Number(unitNumber));
	const links = [
		{
			key: 'text',
			label: 'Text',
			href: new URL(`unit-${unitNumber}.html`, subjectUrl).href,
		},
	];

	const q = subject.practice?.unitQuestions;
	const questionsAvailable = Boolean(q?.hrefPattern && unitIsAvailable(q.availableUnits, unitNumber));
	links.push({
		key: 'questions',
		label: q?.label || 'Textbook Questions',
		href: questionsAvailable
			? new URL(q.hrefPattern.replace('{unit}', String(unitNumber)), subjectUrl).href
			: '#',
		dummy: !questionsAvailable,
	});

	const c = subject.classNotes;
	const classNotesAvailable = Boolean(c?.hrefPattern && unitIsAvailable(c.availableUnits, unitNumber));
	links.push({
		key: 'class-notes',
		label: c?.label || "Priyanka's Class Notes",
		href: classNotesAvailable
			? new URL(c.hrefPattern.replace('{unit}', String(unitNumber)), subjectUrl).href
			: '#',
		dummy: !classNotesAvailable,
	});

	const neighbours = getNeighbourUnits(subject, unitNumber);
	const hasNeighbourLinks = Boolean(neighbours.previous || neighbours.next);

	return `
		<div class="unit-navigation-stack">
			<nav class="unit-resource-nav" aria-label="Unit ${escapeHtml(unitLabel)} study pages">
				${links.map(link => `
					<a class="unit-resource-link${active === link.key ? ' is-active' : ''}${link.dummy ? ' is-dummy' : ''}" href="${escapeHtml(link.href)}"${active === link.key ? ' aria-current="page"' : ''}${link.dummy ? ' aria-disabled="true" title="Page not added yet"' : ''}>
						${escapeHtml(link.label)}
					</a>
				`).join('')}
			</nav>
			${hasNeighbourLinks ? `
				<nav class="unit-neighbour-nav" aria-label="Move between ${escapeHtml(subject.shortName || subject.name || 'subject')} units">
					${renderNeighbourLink(neighbours.previous, 'previous', subjectUrl)}
					${renderNeighbourLink(neighbours.next, 'next', subjectUrl)}
				</nav>
			` : ''}
		</div>
	`;
}

window.PankuUnitResourceNav = { render };
})();

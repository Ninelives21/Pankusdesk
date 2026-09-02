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
	if (q?.hrefPattern && unitIsAvailable(q.availableUnits, unitNumber)) {
		links.push({
			key: 'questions',
			label: q.label || 'Textbook Questions',
			href: new URL(q.hrefPattern.replace('{unit}', String(unitNumber)), subjectUrl).href,
		});
	}

	const c = subject.classNotes;
	if (c?.hrefPattern && unitIsAvailable(c.availableUnits, unitNumber)) {
		links.push({
			key: 'class-notes',
			label: c.label || "Priyanka's Class Notes",
			href: new URL(c.hrefPattern.replace('{unit}', String(unitNumber)), subjectUrl).href,
		});
	}

	if (links.length < 2) return '';
	return `
		<nav class="unit-resource-nav" aria-label="Unit ${escapeHtml(unitLabel)} study pages">
			${links.map(link => `
				<a class="unit-resource-link${active === link.key ? ' is-active' : ''}" href="${escapeHtml(link.href)}"${active === link.key ? ' aria-current="page"' : ''}>
					${escapeHtml(link.label)}
				</a>
			`).join('')}
		</nav>
	`;
}

window.PankuUnitResourceNav = { render };
})();

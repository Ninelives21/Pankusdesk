let semesterContextModule;
let semesterIndex;

document.addEventListener('DOMContentLoaded', async () => {
	try {
		semesterContextModule = await import('./semester-context.js');
		semesterIndex = await semesterContextModule.loadSemesterIndex();

		buildSemesterJourney(semesterIndex);

		const context = await semesterContextModule.resolveSemesterContext();
		renderSelectedSemester(context);

		window.addEventListener('pankusdesk:semester-change', event => {
			renderSelectedSemester(event.detail);
		});
	} catch (error) {
		console.error('Landing page semester context error:', error);
	}
});

function buildSemesterJourney(index) {
	const container = document.getElementById('semester-journey');
	if (!container) return;

	const availableById = new Map(
		index.semesters.map(semester => [semester.id, semester]),
	);

	container.innerHTML = Array.from({ length: 4 }, (_, yearOffset) => {
		const year = yearOffset + 1;
		const semesterIds = [`${year}-1`, `${year}-2`];

		const cards = semesterIds
			.map(id => semesterCardHtml(id, availableById.get(id)))
			.join('');

		return `
			<div class="year-column">
				<h3>Year ${year}</h3>
				${cards}
			</div>
		`;
	}).join('');

	container.querySelectorAll('[data-semester-id]').forEach(button => {
		button.addEventListener('click', async () => {
			await semesterContextModule.selectSemester(
				button.dataset.semesterId,
			);
		});
	});
}

function semesterCardHtml(id, semester) {
	if (!semester) {
		return `
			<div class="semester-card disabled">
				<span>${escapeHtml(displaySemesterId(id))}</span>
				<small>R25 not available</small>
			</div>
		`;
	}

	return `
		<button
			class="semester-card semester-card-button"
			type="button"
			data-semester-id="${escapeHtml(id)}"
		>
			<span>${escapeHtml(displaySemesterId(id))}</span>
			<small>Available</small>
		</button>
	`;
}

function renderSelectedSemester(context) {
	const { semesterSummary, semesterData } = context;

	document.querySelectorAll('[data-semester-id]').forEach(card => {
		card.classList.toggle(
			'active',
			card.dataset.semesterId === semesterSummary.id,
		);

		const label = card.querySelector('small');
		if (label) {
			label.textContent =
				card.dataset.semesterId === semesterSummary.id
					? 'Selected'
					: 'Available';
		}
	});

	setText('selected-semester-eyebrow', semesterEyebrow(semesterSummary));
	setText('selected-semester-title', semesterSummary.label);

	const subjectList = document.getElementById('selected-semester-subjects');
	if (subjectList) {
		const theory = semesterData.courses.filter(
			course => course.category === 'theory',
		);

		const practicalCount = semesterData.courses.filter(
			course => course.category === 'lab' || course.category === 'workshop',
		).length;

		subjectList.innerHTML = theory
			.map(course => `<span>${escapeHtml(course.name)}</span>`)
			.join('');

		if (practicalCount) {
			subjectList.insertAdjacentHTML(
				'beforeend',
				'<span>Labs &amp; Workshops</span>',
			);
		}
	}

	const openLink = document.getElementById('selected-semester-open');
	const unavailable = document.getElementById('selected-semester-unavailable');
	const dashboardRoute = semesterSummary.routes?.dashboard;

	if (openLink) {
		openLink.hidden = !dashboardRoute;
		if (dashboardRoute) openLink.href = dashboardRoute;
	}

	if (unavailable) {
		unavailable.hidden = Boolean(dashboardRoute);
	}

	updateRecentStudyContext(semesterSummary.id);
}

function updateRecentStudyContext(semesterId) {
	const recentContent = document.getElementById('recent-study-content');
	const recentEmpty = document.getElementById('recent-study-empty');

	if (!recentContent || !recentEmpty) return;

	const hasCurrentLog = semesterId === '1-1';
	recentContent.hidden = !hasCurrentLog;
	recentEmpty.hidden = hasCurrentLog;
}

function semesterEyebrow(semester) {
	const term = semester.id.endsWith('-1') ? 1 : 2;
	return `Year ${semester.year} · Semester ${term}`;
}

function displaySemesterId(id) {
	return id.replace('-', '.');
}

function setText(id, value) {
	const element = document.getElementById(id);
	if (element) element.textContent = value;
}

function escapeHtml(value) {
	return String(value)
		.replaceAll('&', '&amp;')
		.replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;')
		.replaceAll("'", '&#039;');
}

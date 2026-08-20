(function () {
document.addEventListener(
	'DOMContentLoaded',
	async () => {
		try {
			const semesterContextModule =
				await import(
					'./semester-context.js'
				);

			const context =
				await semesterContextModule
					.resolveCurrentSemesterContext();

			buildSemesterJourney(
				context.semesterIndex,
				context.currentAcademicSemesterId,
			);

			renderCurrentSemester(
				context,
			);
		} catch (error) {
			console.error(
				'Landing page semester context error:',
				error,
			);
		}
	},
);


function buildSemesterJourney(
	index,
	currentSemesterId,
) {
	const container =
		document.getElementById(
			'semester-journey',
		);

	if (!container) return;

	const availableById =
		new Map(
			index.semesters.map(
				semester => [
					semester.id,
					semester,
				],
			),
		);

	container.innerHTML =
		Array.from(
			{ length: 4 },
			(_, yearOffset) => {
				const year =
					yearOffset + 1;

				const semesterIds = [
					`${year}-1`,
					`${year}-2`,
				];

				const cards =
					semesterIds
						.map(id =>
							semesterCardHtml(
								id,
								availableById.get(id),
								currentSemesterId,
							),
						)
						.join('');

				return `
					<div class="year-column">
						<h3>Year ${year}</h3>
						${cards}
					</div>
				`;
			},
		).join('');
}


function semesterCardHtml(
	id,
	semester,
	currentSemesterId,
) {
	if (!semester) {
		return `
			<div class="semester-card disabled">
				<span>
					${escapeHtml(
						displaySemesterId(id),
					)}
				</span>

				<small>
					R25 not available
				</small>
			</div>
		`;
	}

	const isCurrent =
		id === currentSemesterId;

	const dashboardRoute =
		semester.routes?.dashboard;

	if (dashboardRoute) {
		return `
			<a
				class="semester-card ${
					isCurrent ? 'active' : ''
				}"
				href="${escapeHtml(
					dashboardRoute,
				)}"
			>
				<span>
					${escapeHtml(
						displaySemesterId(id),
					)}
				</span>

				<small>
					${isCurrent
						? 'Current'
						: 'Available'}
				</small>
			</a>
		`;
	}

	return `
		<div
			class="semester-card disabled ${
				isCurrent ? 'active' : ''
			}"
		>
			<span>
				${escapeHtml(
					displaySemesterId(id),
				)}
			</span>

			<small>
				${isCurrent
					? 'Current · page not built'
					: 'R25 available'}
			</small>
		</div>
	`;
}


function renderCurrentSemester(context) {
	const {
		currentAcademicSemesterId,
		currentSemesterSummary,
		currentSemesterData,
	} = context;

	if (
		!currentAcademicSemesterId ||
		!currentSemesterSummary ||
		!currentSemesterData
	) {
		renderBetweenSemesters();
		return;
	}

	setText(
		'current-semester-eyebrow',
		semesterEyebrow(
			currentSemesterSummary,
		),
	);

	setText(
		'current-semester-title',
		currentSemesterSummary.label,
	);

	const subjectList =
		document.getElementById(
			'current-semester-subjects',
		);

	if (subjectList) {
		const theory =
			currentSemesterData.courses.filter(
				course =>
					course.category ===
					'theory',
			);

		const practicalCount =
			currentSemesterData.courses.filter(
				course =>
					course.category ===
						'lab' ||
					course.category ===
						'workshop',
			).length;

		subjectList.innerHTML =
			theory
				.map(
					course =>
						`<span>${escapeHtml(
							course.name,
						)}</span>`,
				)
				.join('');

		if (practicalCount) {
			subjectList.insertAdjacentHTML(
				'beforeend',
				'<span>Labs &amp; Workshops</span>',
			);
		}
	}

	const openLink =
		document.getElementById(
			'current-semester-open',
		);

	const unavailable =
		document.getElementById(
			'current-semester-unavailable',
		);

	const dashboardRoute =
		currentSemesterSummary
			.routes
			?.dashboard;

	if (openLink) {
		openLink.hidden =
			!dashboardRoute;

		if (dashboardRoute) {
			openLink.href =
				dashboardRoute;
		}
	}

	if (unavailable) {
		unavailable.hidden =
			Boolean(
				dashboardRoute,
			);
	}

	updateRecentStudyContext(
		currentAcademicSemesterId,
	);
}


function renderBetweenSemesters() {
	setText(
		'current-semester-eyebrow',
		'Academic calendar',
	);

	setText(
		'current-semester-title',
		'Between semesters',
	);

	const subjectList =
		document.getElementById(
			'current-semester-subjects',
		);

	if (subjectList) {
		subjectList.innerHTML =
			'<span>No semester is currently in session.</span>';
	}

	const openLink =
		document.getElementById(
			'current-semester-open',
		);

	const unavailable =
		document.getElementById(
			'current-semester-unavailable',
		);

	if (openLink) {
		openLink.hidden = true;
	}

	if (unavailable) {
		unavailable.hidden = false;
		unavailable.textContent =
			'Semester break';
	}

	updateRecentStudyContext(
		null,
	);
}


function updateRecentStudyContext(
	semesterId,
) {
	const recentContent =
		document.getElementById(
			'recent-study-content',
		);

	const recentEmpty =
		document.getElementById(
			'recent-study-empty',
		);

	if (
		!recentContent ||
		!recentEmpty
	) {
		return;
	}

	const hasCurrentLog =
		semesterId === '1-1';

	recentContent.hidden =
		!hasCurrentLog;

	recentEmpty.hidden =
		hasCurrentLog;
}


function semesterEyebrow(
	semester,
) {
	const term =
		semester.id.endsWith('-1')
			? 1
			: 2;

	return (
		`Year ${semester.year} · Semester ${term}`
	);
}


function displaySemesterId(id) {
	return id.replace('-', '.');
}


function setText(
	id,
	value,
) {
	const element =
		document.getElementById(id);

	if (element) {
		element.textContent =
			value;
	}
}


function escapeHtml(value) {
	return String(value)
		.replaceAll('&', '&amp;')
		.replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;')
		.replaceAll("'", '&#039;');
}
})();

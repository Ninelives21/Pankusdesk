let semesterContextModule;

document.addEventListener('DOMContentLoaded', async () => {
	const mount = document.getElementById('navbar-new');
	if (!mount) return;

	try {
		const response = await fetch('navbar_new.html');

		if (!response.ok) {
			throw new Error(`Navbar load failed: ${response.status}`);
		}

		mount.innerHTML = await response.text();

		semesterContextModule = await import('./semester-context.js');

		await configureSemesterNavigation();

		initMobileNav();
		initDropdowns();
		highlightCurrentNav();

		window.addEventListener(
			'pankusdesk:semester-change',
			async event => {
				await configureSemesterNavigation(event.detail);
			},
		);
	} catch (error) {
		console.error('Navbar error:', error);
	}
});

async function configureSemesterNavigation(context = null) {
	const resolvedContext =
		context ?? (await semesterContextModule.resolveSemesterContext());

	const { semesterSummary, semesterData } = resolvedContext;

	updateCurrentSemesterLink(semesterSummary);
	updateSemesterUtilityLinks(semesterSummary);
	buildSubjectDropdown(semesterSummary, semesterData);
}

function updateCurrentSemesterLink(semester) {
	const link = document.getElementById('current-semester-link');
	if (!link) return;

	link.textContent = semester.label;
	link.href = semester.routes?.dashboard ?? 'index.html#four-year-journey';
}

function updateSemesterUtilityLinks(semester) {
	const calendarLink = document.getElementById('calendar-nav-link');
	const progressLink = document.getElementById('progress-nav-link');

	if (calendarLink) {
		calendarLink.href = `college/calendar.html?semester=${encodeURIComponent(semester.id)}`;
		calendarLink.hidden = false;
	}

	setOptionalNavLink(
		progressLink,
		semester.routes?.progress,
	);
}

function setOptionalNavLink(link, route) {
	if (!link) return;

	if (route) {
		link.href = route;
		link.hidden = false;
		return;
	}

	link.hidden = true;
}

function buildSubjectDropdown(semesterSummary, semesterData) {
	const menu = document.getElementById('subject-dropdown-menu');
	if (!menu) return;

	const visibleCourses = semesterData.courses.filter(
		course => course.showInNavbar !== false,
	);

	const theoryCourses = visibleCourses.filter(
		course => course.category === 'theory',
	);

	const practicalCourses = visibleCourses.filter(
		course => course.category === 'lab' || course.category === 'workshop',
	);

	const linksEnabled = Boolean(semesterSummary.routes?.dashboard);

	const theoryHtml = theoryCourses
		.map(course => subjectItemHtml(semesterData.id, course, linksEnabled))
		.join('');

	let practicalHtml = '';

	if (practicalCourses.length) {
		practicalHtml = `
			<div class="dropdown-divider" aria-hidden="true"></div>

			<div class="nav-dropdown-group-label">
				Labs &amp; Workshops
			</div>

			${practicalCourses
				.map(course => subjectItemHtml(semesterData.id, course, linksEnabled))
				.join('')}
		`;
	}

	menu.innerHTML = theoryHtml + practicalHtml;
}

function subjectItemHtml(semesterId, course, linksEnabled) {
	if (!linksEnabled) {
		return `
			<span class="nav-dropdown-unavailable">
				${escapeHtml(course.name)}
			</span>
		`;
	}

	return `
		<a href="college/${escapeHtml(semesterId)}/${escapeHtml(course.slug)}/index.html">
			${escapeHtml(course.name)}
		</a>
	`;
}

function initMobileNav() {
	const toggle = document.querySelector('.nav-toggle');
	const links = document.querySelector('.navbar-links');

	if (!toggle || !links) return;

	toggle.addEventListener('click', () => {
		const open = links.classList.toggle('open');
		toggle.setAttribute('aria-expanded', String(open));
	});

	links.querySelectorAll('a').forEach(link => {
		link.addEventListener('click', () => {
			links.classList.remove('open');
			toggle.setAttribute('aria-expanded', 'false');
		});
	});
}

function initDropdowns() {
	document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
		const button = dropdown.querySelector('.nav-dropdown-button');
		if (!button) return;

		button.addEventListener('click', event => {
			event.stopPropagation();

			document.querySelectorAll('.nav-dropdown.open').forEach(other => {
				if (other !== dropdown) {
					other.classList.remove('open');
					other
						.querySelector('.nav-dropdown-button')
						?.setAttribute('aria-expanded', 'false');
				}
			});

			const open = dropdown.classList.toggle('open');
			button.setAttribute('aria-expanded', String(open));
		});
	});

	document.addEventListener('click', () => {
		document.querySelectorAll('.nav-dropdown.open').forEach(dropdown => {
			dropdown.classList.remove('open');
			dropdown
				.querySelector('.nav-dropdown-button')
				?.setAttribute('aria-expanded', 'false');
		});
	});
}

function highlightCurrentNav() {
	const path = window.location.pathname;
	let key = 'home';

	if (/\/college\/[^/]+\/progress(?:\.html)?$/.test(path)) {
		key = 'progress';
	} else if (/\/college\/calendar(?:\.html)?$/.test(path)) {
		key = 'calendar';
	} else if (path.includes('/college/')) {
		key = 'semester';
	}

	document.querySelector(`[data-nav="${key}"]`)?.classList.add('active');
}

function escapeHtml(value) {
	return String(value)
		.replaceAll('&', '&amp;')
		.replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;')
		.replaceAll("'", '&#039;');
}

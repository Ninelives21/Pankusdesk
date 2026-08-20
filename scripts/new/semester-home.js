(function () {
document.addEventListener('DOMContentLoaded', () => {
	initSemesterHome();
});

async function initSemesterHome() {
	const page = document.querySelector('.semester-page');
	if (!page) return;

	try {
		const semesterUrl = new URL(page.dataset.semesterJson, document.baseURI);
		const semester = await fetchJson(semesterUrl.href);
		renderSemesterIdentity(semester);
		renderCourses(semester);
		renderCalendarLinks(semester);
		await renderToday(semester, semesterUrl);
	} catch (error) {
		console.error('Semester page load failed:', error);
		renderSemesterError(error);
	}
}

function renderSemesterIdentity(semester) {
	document.querySelectorAll('[data-semester-label]').forEach(element => {
		element.textContent = semester.label;
	});
	setText('[data-semester-eyebrow]', `Year ${semester.year} · Semester ${semester.semesterNumber}`);
	setText('[data-regulation]', semester.regulation);
	setText('[data-total-credits]', semester.totalCredits);
	document.title = `${semester.label} · Panku's Desk`;
}

function renderCourses(semester) {
	const subjectGrid = document.getElementById('semester-subject-grid');
	const labList = document.getElementById('semester-lab-list');
	const theory = semester.courses.filter(course => course.category === 'theory');
	const practical = semester.courses.filter(course => course.category === 'lab' || course.category === 'workshop');

	if (subjectGrid) {
		subjectGrid.innerHTML = theory.map(course => subjectCardHtml(course)).join('');
	}

	if (labList) {
		labList.innerHTML = practical.map(course => `
			<div class="lab-item">
				<div>
					<div class="subject-code">${escapeHtml(course.code)}</div>
					<h3>${escapeHtml(course.name)}</h3>
				</div>
				<span>${escapeHtml(course.credits)} credit${Number(course.credits) === 1 ? '' : 's'}</span>
			</div>
		`).join('');
	}
}

function subjectCardHtml(course) {
	const body = `
		<div class="subject-code">${escapeHtml(course.code)}</div>
		<h2>${escapeHtml(course.name)}</h2>
		<div class="subject-card-footer">
			<span>${escapeHtml(course.credits)} credits</span>
			<span>${course.page ? 'Open subject →' : 'Coming soon'}</span>
		</div>
	`;

	if (course.page) {
		return `<a class="subject-card" href="${escapeHtml(course.page)}">${body}</a>`;
	}

	return `<article class="subject-card subject-card--unavailable" aria-label="${escapeHtml(course.name)} — coming soon">${body}</article>`;
}

function renderCalendarLinks(semester) {
	const href = `college/calendar.html?semester=${encodeURIComponent(semester.id)}`;
	document.querySelectorAll('[data-calendar-link]').forEach(link => {
		link.href = href;
	});
}

async function renderToday(semester, semesterUrl) {
	const panel = document.getElementById('semester-today-panel');
	if (!panel) return;

	const timetablePath = semester.calendar?.timetable;
	if (!timetablePath) {
		panel.innerHTML = '<div class="semester-empty">No timetable is connected to this semester yet.</div>';
		return;
	}

	const timetableUrl = new URL(timetablePath, document.baseURI);
	const timetable = await fetchJson(timetableUrl.href);
	const now = new Date();
	const dayName = now.toLocaleDateString('en-US', { weekday: 'long' });
	const dateLabel = now.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });
	const entries = timetable.days?.[dayName] ?? [];
	const periodsById = new Map((timetable.periods ?? []).map(period => [Number(period.id), period]));

	panel.innerHTML = `
		<div class="today-date">
			<div class="eyebrow">${escapeHtml(dayName)}</div>
			<h2>${escapeHtml(dateLabel)}</h2>
		</div>
		<div class="today-list">
			${entries.length ? entries.map(entry => renderTodayEntry(entry, periodsById)).join('') : '<div class="semester-empty">No classes scheduled today.</div>'}
		</div>
	`;
}

function renderTodayEntry(entry, periodsById) {
	const ids = entry.periods ?? [];
	const first = periodsById.get(Number(ids[0]));
	const last = periodsById.get(Number(ids[ids.length - 1]));
	const time = first && last ? `${formatClock(first.start)}–${formatClock(last.end)}` : '';
	return `
		<div class="today-item">
			<div class="today-time">${escapeHtml(time)}</div>
			<div>
				<strong>${escapeHtml(entry.name)}</strong>
				<span>${escapeHtml(entry.code)}</span>
			</div>
		</div>
	`;
}

function formatClock(value) {
	if (!value) return '';
	const [hourString, minute] = value.split(':');
	const hour = Number(hourString);
	const suffix = hour >= 12 ? 'PM' : 'AM';
	const displayHour = hour % 12 || 12;
	return `${displayHour}:${minute} ${suffix}`;
}

function renderSemesterError(error) {
	const subjectGrid = document.getElementById('semester-subject-grid');
	if (subjectGrid) {
		subjectGrid.innerHTML = `<div class="semester-error">Semester metadata could not be loaded.${error?.message ? ` ${escapeHtml(error.message)}` : ''}</div>`;
	}
}

async function fetchJson(url) {
	const response = await fetch(url);
	if (!response.ok) throw new Error(`${url} returned ${response.status}`);
	return response.json();
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

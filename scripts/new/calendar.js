import { resolveSemesterContext } from './semester-context.js';

document.addEventListener('DOMContentLoaded', initCalendar);

async function initCalendar() {
	const grid = document.getElementById('calendar-grid');

	if (!grid) {
		return;
	}

	const state = {
		currentMonth: new Date(),
		selectedDate: null,

		semesterId: null,
		semesterSummary: null,
		semesterData: null,

		academicCalendar: null,
		timetable: null,
		holidays: null,
		classLog: {},
	};

	try {
		const context = await resolveSemesterContext();

		state.semesterId = context.semesterData.id;
		state.semesterSummary = context.semesterSummary;
		state.semesterData = context.semesterData;
		state.academicCalendar = context.academicCalendar;

		const resources = await loadCalendarResources(
			state.semesterId,
			context.semesterData.calendar ?? {},
		);

		state.timetable = resources.timetable;
		state.holidays = resources.holidays;
		state.classLog = resources.classLog;

		console.info('Calendar resources:', {
			semesterId: state.semesterId,
			timetableLoaded: Boolean(state.timetable),
			holidaysLoaded: Boolean(state.holidays),
			classLogDates: Object.keys(state.classLog ?? {}),
		});

		configurePage(state);
		setupMonthControls(state);
		setupTimetableModal(state);
		selectInitialDate(state);
	} catch (error) {
		console.error('Calendar failed to load:', error);

		grid.innerHTML = `
			<div class="calendar-load-error">
				Calendar data could not be loaded.
				Check the browser Console for the exact error.
			</div>
		`;
	}
}

/* ====================================================================== */
/* Data loading                                                           */
/* ====================================================================== */

async function loadCalendarResources(semesterId, declared) {
	const standardBase = `college/${semesterId}/data`;

	const timetable = await loadFirstAvailable(
		[declared.timetable, `${standardBase}/timetable.json`],
		null,
	);

	const holidays = await loadFirstAvailable(
		[declared.holidays, `${standardBase}/holidays.json`],
		null,
	);

	const classLog = await loadFirstAvailable(
		[declared.classLog, `${standardBase}/class-log.json`],
		{},
	);

	return {
		timetable,
		holidays,
		classLog: classLog ?? {},
	};
}

async function loadFirstAvailable(paths, fallback) {
	const tried = new Set();

	for (const path of paths) {
		if (!path || tried.has(path)) {
			continue;
		}

		tried.add(path);

		try {
			return await loadJson(path);
		} catch (error) {
			console.warn(`Calendar resource unavailable: ${path}`, error);
		}
	}

	return fallback;
}

async function loadJson(path) {
	const response = await fetch(path);

	if (!response.ok) {
		throw new Error(`Could not load ${path}: ${response.status}`);
	}

	return response.json();
}

/* ====================================================================== */
/* Page setup                                                             */
/* ====================================================================== */

function configurePage(state) {
	const label = state.semesterData.label;

	const dashboardRoute = state.semesterSummary.routes?.dashboard;

	document.title = `${label} Calendar · Panku's Desk`;

	setText('calendar-semester-eyebrow', label);

	setText('calendar-month-subtitle', label);

	setText('weekly-timetable-semester', label);

	setText('timetable-modal-title', `${label} Timetable`);

	const breadcrumb = document.getElementById('calendar-semester-breadcrumb');

	if (breadcrumb) {
		breadcrumb.textContent = label;

		breadcrumb.href = dashboardRoute ?? 'index.html#four-year-journey';
	}

	const dashboard = document.getElementById('calendar-dashboard-link');

	if (dashboard) {
		dashboard.href = dashboardRoute ?? 'index.html#four-year-journey';

		dashboard.textContent = dashboardRoute
			? 'Semester dashboard →'
			: 'Back to semesters →';
	}

	configureTimetablePanel(state);
	configureSourceNote(state);
}

function configureTimetablePanel(state) {
	const panel = document.getElementById('weekly-timetable-panel');

	const copy = document.getElementById('weekly-timetable-copy');

	if (!panel) {
		return;
	}

	if (!state.timetable) {
		panel.hidden = true;
		return;
	}

	panel.hidden = false;

	if (copy) {
		const from = formatLongDate(state.timetable.effectiveFrom);

		const to = state.timetable.effectiveTo
			? ` to ${formatLongDate(state.timetable.effectiveTo)}`
			: '';

		copy.textContent = `Official class timetable effective ${from}${to}.`;
	}
}

function configureSourceNote(state) {
	const note = document.getElementById('calendar-source-note');

	if (!note) {
		return;
	}

	const hasAcademicCalendar = Boolean(
		state.academicCalendar?.semesters?.[state.semesterId],
	);

	if (hasAcademicCalendar && state.timetable) {
		note.innerHTML = `
			<strong>Calendar scope:</strong>
			Official academic-calendar events are combined
			with this semester's timetable, holidays and class log.
		`;

		return;
	}

	if (hasAcademicCalendar) {
		note.innerHTML = `
			<strong>Calendar scope:</strong>
			Official academic-calendar events are available
			for this semester. Timetable and class-log data
			can be added later.
		`;

		return;
	}

	note.innerHTML = `
		<strong>Calendar scope:</strong>
		Academic-calendar dates for this semester
		have not been added yet.
	`;
}

/* ====================================================================== */
/* Month navigation                                                       */
/* ====================================================================== */

function setupMonthControls(state) {
	document.getElementById('calendar-prev')?.addEventListener('click', () => {
		state.currentMonth = new Date(
			state.currentMonth.getFullYear(),

			state.currentMonth.getMonth() - 1,

			1,
		);

		renderCalendar(state);
	});

	document.getElementById('calendar-next')?.addEventListener('click', () => {
		state.currentMonth = new Date(
			state.currentMonth.getFullYear(),

			state.currentMonth.getMonth() + 1,

			1,
		);

		renderCalendar(state);
	});
}

/* ====================================================================== */
/* Initial date                                                           */
/* ====================================================================== */

function selectInitialDate(state) {
	const today = new Date();

	const semester = state.academicCalendar?.semesters?.[state.semesterId];

	let initial = today;

	if (semester?.semesterPeriod?.start && semester?.semesterPeriod?.end) {
		const start = parseLocalDate(semester.semesterPeriod.start);

		const end = parseLocalDate(semester.semesterPeriod.end);

		if (today < start) {
			initial = start;
		}

		if (today > end) {
			initial = end;
		}
	} else if (state.timetable?.effectiveFrom) {
		initial = parseLocalDate(state.timetable.effectiveFrom);
	}

	state.currentMonth = new Date(initial.getFullYear(), initial.getMonth(), 1);

	state.selectedDate = toIsoDate(initial);

	renderCalendar(state);
	renderDayDetail(initial, state);
}

/* ====================================================================== */
/* Calendar rendering                                                     */
/* ====================================================================== */

function renderCalendar(state) {
	const grid = document.getElementById('calendar-grid');

	const title = document.getElementById('calendar-month-title');

	if (!grid || !title) {
		return;
	}

	const year = state.currentMonth.getFullYear();

	const month = state.currentMonth.getMonth();

	title.textContent = state.currentMonth.toLocaleDateString('en-IN', {
		month: 'long',
		year: 'numeric',
	});

	grid.innerHTML = '';

	const first = new Date(year, month, 1);

	const last = new Date(year, month + 1, 0);

	/*
		JavaScript:
		Sunday = 0

		Calendar:
		Monday = first column
	*/
	const leading = (first.getDay() + 6) % 7;

	for (let i = 0; i < leading; i++) {
		const empty = document.createElement('div');

		empty.className = 'calendar-day calendar-day-empty';

		grid.appendChild(empty);
	}

	for (let day = 1; day <= last.getDate(); day++) {
		const date = new Date(year, month, day);

		grid.appendChild(createDayCell(date, state));
	}
}

/* ====================================================================== */
/* Individual date cell                                                   */
/* ====================================================================== */

function createDayCell(date, state) {
	const iso = toIsoDate(date);

	const holiday = getHolidayInfo(date, state.holidays);

	const academic = getAcademicInfo(
		date,
		state.academicCalendar,
		state.semesterId,
	);

	const notes = getNotesForDate(iso, state.classLog);

	const scheduled = getScheduleForDate(
		date,
		state.timetable,
		holiday,
		academic,
	);

	const button = document.createElement('button');

	button.type = 'button';

	button.className = 'calendar-day';

	if (holiday.isHoliday) {
		button.classList.add('is-holiday');
	}

	if (academic.events.length) {
		button.classList.add('has-academic-event');
	}

	if (notes.length) {
		button.classList.add('has-notes');
	}

	if (scheduled.length) {
		button.classList.add('has-schedule');
	}

	if (isSameDate(date, new Date())) {
		button.classList.add('is-today');
	}

	if (state.selectedDate === iso) {
		button.classList.add('is-selected');
	}

	const tags = [];

	/*
		These are deliberately independent.

		A day may show:

		Registration
		6 classes
		3 notes

		or:

		Holiday
		2 notes

		etc.
	*/

	if (academic.events.length) {
		tags.push(`
			<span
				class="
					calendar-day-tag
					academic-tag
				"
			>
				${escapeHtml(shortAcademicLabel(academic.events[0]))}
			</span>
		`);
	}

	if (holiday.isHoliday) {
		tags.push(`
			<span
				class="
					calendar-day-tag
					holiday-tag
				"
			>
				${escapeHtml(shortHolidayLabel(holiday.label))}
			</span>
		`);
	}

	if (scheduled.length) {
		const classCount = countScheduledPeriods(scheduled);

		tags.push(`
			<span
				class="
					calendar-day-tag
					class-tag
				"
			>
				${classCount}
				class${classCount === 1 ? '' : 'es'}
			</span>
		`);
	}

	if (notes.length) {
		tags.push(`
			<span
				class="
					calendar-day-tag
					notes-tag
				"
			>
				${notes.length}
				note${notes.length === 1 ? '' : 's'}
			</span>
		`);
	}

	button.innerHTML = `
		<div
			class="calendar-day-top"
		>
			<span
				class="calendar-day-number"
			>
				${date.getDate()}
			</span>

			${
				notes.length
					? `
						<span
							class="
								calendar-note-marker
							"
							title="
								Class notes added
							"
						></span>
					`
					: ''
			}
		</div>

		<div
			class="calendar-day-body"
		>
			${tags.join('')}
		</div>
	`;

	button.addEventListener('click', () => {
		state.selectedDate = iso;

		renderCalendar(state);

		renderDayDetail(date, state);
	});

	return button;
}

/*
	A timetable item may occupy more than one period.

	Example:
	Engineering Drawing periods [1,2,3]

	That represents THREE scheduled class periods,
	not one.
*/
function countScheduledPeriods(schedule) {
	return schedule.reduce((total, item) => {
		const count = item.periods?.length ?? 1;

		return total + count;
	}, 0);
}

/* ====================================================================== */
/* Selected date panel                                                    */
/* ====================================================================== */

function renderDayDetail(date, state) {
	const title = document.getElementById('day-detail-title');

	const status = document.getElementById('day-detail-status');

	const content = document.getElementById('day-detail-content');

	if (!title || !status || !content) {
		return;
	}

	const iso = toIsoDate(date);

	const holiday = getHolidayInfo(date, state.holidays);

	const academic = getAcademicInfo(
		date,
		state.academicCalendar,
		state.semesterId,
	);

	const notes = getNotesForDate(iso, state.classLog);

	const scheduled = getScheduleForDate(
		date,
		state.timetable,
		holiday,
		academic,
	);

	title.textContent = date.toLocaleDateString('en-IN', {
		weekday: 'long',
		day: 'numeric',
		month: 'long',
		year: 'numeric',
	});

	const statusParts = [];

	if (academic.events.length) {
		statusParts.push(shortAcademicLabel(academic.events[0]));
	}

	if (holiday.isHoliday) {
		statusParts.push(`Holiday · ${holiday.label}`);
	}

	if (scheduled.length) {
		const classCount = countScheduledPeriods(scheduled);

		statusParts.push(`${classCount} class${classCount === 1 ? '' : 'es'}`);
	}

	if (notes.length) {
		statusParts.push(`${notes.length} note${notes.length === 1 ? '' : 's'}`);
	}

	status.innerHTML = statusParts.length
		? `
				<span
					class="
						detail-pill
						scheduled-detail-pill
					"
				>
					${escapeHtml(statusParts.join(' · '))}
				</span>
			`
		: '';

	let html = '';

	if (academic.events.length) {
		html += `
			<div
				class="
					day-detail-section
				"
			>
				<h3>
					Academic calendar
				</h3>

				<div
					class="
						academic-event-list
					"
				>
					${academic.events.map(renderAcademicEvent).join('')}
				</div>
			</div>
		`;
	}

	if (notes.length) {
		html += `
			<div
				class="
					day-detail-section
				"
			>
				<h3>
					What was taught
				</h3>

				<div
					class="
						class-log-list
					"
				>
					${notes.map(renderClassLogItem).join('')}
				</div>
			</div>
		`;
	}

	if (scheduled.length) {
		html += `
			<div
				class="
					day-detail-section
				"
			>
				<h3>
					Scheduled classes
				</h3>

				<div
					class="
						day-schedule-list
					"
				>
					${scheduled.map(item => renderScheduleItem(item, state.timetable)).join('')}
				</div>
			</div>
		`;
	}

	if (!academic.events.length && !notes.length && !scheduled.length) {
		html = `
			<p
				class="calendar-empty"
			>
				No academic events,
				scheduled classes or
				class notes for this date.
			</p>
		`;
	}

	if (!notes.length && scheduled.length) {
		html += `
			<div
				class="
					calendar-note-prompt
				"
			>
				No class summary has
				been added yet.
			</div>
		`;
	}

	content.innerHTML = html;
}

/* ====================================================================== */
/* Class log                                                              */
/* ====================================================================== */

function getNotesForDate(iso, classLog) {
	if (!classLog) {
		return [];
	}

	/*
		Format currently used:

		{
			"2026-08-12": [...]
		}
	*/
	if (Array.isArray(classLog[iso])) {
		return classLog[iso];
	}

	/*
		Also support:

		{
			"days": {
				"2026-08-12": [...]
			}
		}
	*/
	if (Array.isArray(classLog.days?.[iso])) {
		return classLog.days[iso];
	}

	return [];
}

/* ====================================================================== */
/* Timetable                                                              */
/* ====================================================================== */

function getScheduleForDate(date, timetable, holiday, academic) {
	if (!timetable?.days) {
		return [];
	}

	const iso = toIsoDate(date);

	if (timetable.effectiveFrom && iso < timetable.effectiveFrom) {
		return [];
	}

	if (timetable.effectiveTo && iso > timetable.effectiveTo) {
		return [];
	}

	if (!academic.isInstructionalDate) {
		return [];
	}

	if (academic.suppressRegularClasses) {
		return [];
	}

	if (holiday.isHoliday) {
		return [];
	}

	const dayName = getDayName(date);

	return timetable.days[dayName] || [];
}

/* ====================================================================== */
/* Academic calendar                                                      */
/* ====================================================================== */

function getAcademicInfo(date, academicCalendar, semesterId) {
	if (!academicCalendar) {
		return {
			events: [],
			isInstructionalDate: true,
			suppressRegularClasses: false,
		};
	}

	const iso = toIsoDate(date);

	const semester = academicCalendar.semesters?.[semesterId];

	const classPeriod = semester?.classPeriod;

	const isInstructionalDate = Boolean(
		classPeriod?.start &&
		classPeriod?.end &&
		iso >= classPeriod.start &&
		iso <= classPeriod.end,
	);

	const events = (academicCalendar.events || []).filter(
		event =>
			event.start <= iso &&
			event.end >= iso &&
			(!event.semesterId || event.semesterId === semesterId),
	);

	return {
		events,

		isInstructionalDate,

		suppressRegularClasses:
			events.some(event => event.suppressRegularClasses) ||
			!isInstructionalDate,
	};
}

/* ====================================================================== */
/* Holidays                                                               */
/* ====================================================================== */

function getHolidayInfo(date, holidays) {
	const iso = toIsoDate(date);

	const data = holidays ?? {};

	const exception = (data.exceptions || []).find(item => item.date === iso);

	if (exception?.workingDay) {
		return {
			isHoliday: false,
			label: null,
		};
	}

	if (data.dates?.[iso]) {
		return {
			isHoliday: true,
			label: data.dates[iso],
		};
	}

	const dayName = getDayName(date);

	if (dayName === 'Sunday') {
		return {
			isHoliday: true,
			label: 'Sunday',
		};
	}

	if (dayName === 'Saturday' && isNthSaturday(date, [2, 4])) {
		return {
			isHoliday: true,
			label: nthSaturdayLabel(date),
		};
	}

	return {
		isHoliday: false,
		label: null,
	};
}

/* ====================================================================== */
/* Day detail renderers                                                   */
/* ====================================================================== */

function renderClassLogItem(note) {
	const subject = escapeHtml(note.subject || 'Class');

	const summary = escapeHtml(note.summary || '');

	const link = note.link
		? `
				<a
					class="
						class-log-link
					"
					href="${escapeHtml(note.link)}"
				>
					Open notes →
				</a>
			`
		: '';

	return `
		<article
			class="class-log-item"
		>
			<div
				class="
					class-log-subject
				"
			>
				${subject}
			</div>

			<div
				class="
					class-log-summary
				"
			>
				${summary}
			</div>

			${link}
		</article>
	`;
}

function renderScheduleItem(item, timetable) {
	const periods = item.periods || [];

	if (!periods.length) {
		return '';
	}

	const firstPeriod = Math.min(...periods);

	const lastPeriod = Math.max(...periods);

	const start =
		timetable?.periods?.find(period => period.id === firstPeriod)?.start || '';

	const end =
		timetable?.periods?.find(period => period.id === lastPeriod)?.end || '';

	return `
		<div
			class="
				day-schedule-item
			"
		>
			<div
				class="
					day-schedule-time
				"
			>
				${formatTime(start)}
				–
				${formatTime(end)}
			</div>

			<div>
				<div
					class="
						day-schedule-code
					"
				>
					${escapeHtml(item.code || '')}
				</div>

				<div
					class="
						day-schedule-name
					"
				>
					${escapeHtml(item.name || '')}
				</div>
			</div>
		</div>
	`;
}

function renderAcademicEvent(event) {
	const dateText =
		event.start === event.end
			? formatShortDate(event.start)
			: `${formatShortDate(event.start)}–${formatShortDate(event.end)}`;

	return `
		<article
			class="
				academic-event-item
			"
		>
			<div
				class="
					academic-event-title
				"
			>
				${escapeHtml(event.title)}
			</div>

			<div
				class="
					academic-event-date
				"
			>
				${escapeHtml(dateText)}
			</div>
		</article>
	`;
}

/* ====================================================================== */
/* Weekly timetable modal                                                 */
/* ====================================================================== */

function setupTimetableModal(state) {
	if (!state.timetable) {
		return;
	}

	const openButton = document.getElementById('show-weekly-timetable');

	const closeButton = document.getElementById('close-timetable-modal');

	const backdrop = document.getElementById('timetable-modal');

	const mount = document.getElementById('weekly-timetable-table');

	if (!openButton || !closeButton || !backdrop || !mount) {
		return;
	}

	mount.innerHTML = buildWeeklyTimetable(state.timetable);

	const open = () => {
		backdrop.hidden = false;

		document.body.classList.add('modal-open');
	};

	const close = () => {
		backdrop.hidden = true;

		document.body.classList.remove('modal-open');
	};

	openButton.addEventListener('click', open);

	closeButton.addEventListener('click', close);

	backdrop.addEventListener('click', event => {
		if (event.target === backdrop) {
			close();
		}
	});

	document.addEventListener('keydown', event => {
		if (event.key === 'Escape' && !backdrop.hidden) {
			close();
		}
	});
}

function buildWeeklyTimetable(timetable) {
	if (!timetable?.periods || !timetable?.days) {
		return `
			<p
				class="
					calendar-empty
				"
			>
				Weekly timetable is
				not available yet.
			</p>
		`;
	}

	const days = [
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday',
	];

	const headers = timetable.periods
		.map(
			period => `
					<th>
						${period.id}

						<small>
							${formatTime(period.start)}
							–
							${formatTime(period.end)}
						</small>
					</th>
				`,
		)
		.join('');

	const rows = days
		.map(day => {
			const cells = timetable.periods
				.map(period => {
					const match = (timetable.days[day] || []).find(item =>
						(item.periods || []).includes(period.id),
					);

					if (!match) {
						return '<td>—</td>';
					}

					if (Math.min(...match.periods) !== period.id) {
						return '';
					}

					const span = match.periods.length;

					return `
										<td
											${span > 1 ? `colspan="${span}"` : ''}
										>
											<strong>
												${escapeHtml(match.code || '')}
											</strong>
										</td>
									`;
				})
				.join('');

			return `
						<tr>
							<th>
								${day}
							</th>

							${cells}
						</tr>
					`;
		})
		.join('');

	return `
		<div
			class="
				weekly-table-wrap
			"
		>
			<table
				class="
					weekly-timetable
				"
			>
				<thead>
					<tr>
						<th>
							Day
						</th>

						${headers}
					</tr>
				</thead>

				<tbody>
					${rows}
				</tbody>
			</table>
		</div>
	`;
}

/* ====================================================================== */
/* Labels                                                                 */
/* ====================================================================== */

function shortAcademicLabel(event) {
	const labels = {
		assessment: 'Assessment',

		exam: 'Sessional',

		'exam-period': 'Exam period',

		see: 'SEE',

		break: 'Break',

		registration: 'Registration',

		meeting: 'Meeting',

		feedback: 'Feedback',

		deadline: 'Deadline',

		'practical-exam': 'Practical',

		survey: 'Survey',

		milestone: 'Academic',
	};

	return labels[event?.type] || 'Academic';
}

function shortHolidayLabel(label) {
	if (!label) {
		return 'Holiday';
	}

	if (['Sunday', '2nd Saturday', '4th Saturday'].includes(label)) {
		return label;
	}

	return 'Holiday';
}

/* ====================================================================== */
/* Saturday helpers                                                       */
/* ====================================================================== */

function isNthSaturday(date, nthValues) {
	const occurrence = Math.floor((date.getDate() - 1) / 7) + 1;

	return nthValues.includes(occurrence);
}

function nthSaturdayLabel(date) {
	const occurrence = Math.floor((date.getDate() - 1) / 7) + 1;

	return occurrence === 2 ? '2nd Saturday' : '4th Saturday';
}

/* ====================================================================== */
/* Generic utilities                                                      */
/* ====================================================================== */

function setText(id, value) {
	const element = document.getElementById(id);

	if (element) {
		element.textContent = value;
	}
}

function parseLocalDate(iso) {
	const [year, month, day] = iso.split('-').map(Number);

	return new Date(year, month - 1, day);
}

function toIsoDate(date) {
	const year = date.getFullYear();

	const month = String(date.getMonth() + 1).padStart(2, '0');

	const day = String(date.getDate()).padStart(2, '0');

	return `${year}-${month}-${day}`;
}

function getDayName(date) {
	return date.toLocaleDateString('en-US', {
		weekday: 'long',
	});
}

function isSameDate(a, b) {
	return (
		a.getFullYear() === b.getFullYear() &&
		a.getMonth() === b.getMonth() &&
		a.getDate() === b.getDate()
	);
}

function formatTime(value) {
	if (!value) {
		return '';
	}

	const [hour, minute] = value.split(':').map(Number);

	return new Date(2000, 0, 1, hour, minute)
		.toLocaleTimeString('en-IN', {
			hour: 'numeric',

			minute: '2-digit',

			hour12: true,
		})
		.replace(' ', '');
}

function formatShortDate(iso) {
	return parseLocalDate(iso).toLocaleDateString('en-IN', {
		day: 'numeric',

		month: 'short',
	});
}

function formatLongDate(iso) {
	if (!iso) {
		return '';
	}

	return parseLocalDate(iso).toLocaleDateString('en-IN', {
		day: 'numeric',

		month: 'long',

		year: 'numeric',
	});
}

function escapeHtml(value) {
	return String(value ?? '')
		.replaceAll('&', '&amp;')
		.replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;')
		.replaceAll("'", '&#039;');
}

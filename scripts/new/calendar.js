document.addEventListener('DOMContentLoaded', async () => {
	const grid = document.getElementById('calendar-grid');
	if (!grid) return;

	const state = {
		currentMonth: new Date(2026, 7, 1),
		selectedDate: null,
		timetable: null,
		holidays: null,
		classLog: null,
	};

	try {
		const [timetable, holidays, classLog] = await Promise.all([
			loadJson('college/1-1/data/timetable.json'),
			loadJson('college/1-1/data/holidays.json'),
			loadJson('college/1-1/data/class-log.json'),
		]);

		state.timetable = timetable;
		state.holidays = holidays;
		state.classLog = classLog;

		setupControls(state);
		renderCalendar(state);
		selectInitialDate(state);
		setupTimetableModal(state);
	} catch (error) {
		console.error(error);

		grid.innerHTML = `
			<div class="calendar-load-error">
				Calendar data could not be loaded. If you opened the page directly as a local file,
				run it through a local web server (for example VS Code Live Server) so the JSON files can load.
			</div>
		`;
	}
});

async function loadJson(path) {
	const response = await fetch(path);

	if (!response.ok) {
		throw new Error(`Could not load ${path}: ${response.status}`);
	}

	return response.json();
}

function setupControls(state) {
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

function renderCalendar(state) {
	const grid = document.getElementById('calendar-grid');
	const title = document.getElementById('calendar-month-title');

	if (!grid || !title) return;

	const year = state.currentMonth.getFullYear();
	const month = state.currentMonth.getMonth();

	title.textContent = state.currentMonth.toLocaleDateString('en-IN', {
		month: 'long',
		year: 'numeric',
	});

	grid.innerHTML = '';

	const first = new Date(year, month, 1);
	const last = new Date(year, month + 1, 0);

	// JavaScript uses Sunday = 0.
	// This calendar begins with Monday.
	const leading = (first.getDay() + 6) % 7;

	for (let i = 0; i < leading; i++) {
		const filler = document.createElement('div');
		filler.className = 'calendar-day calendar-day-empty';
		grid.appendChild(filler);
	}

	for (let day = 1; day <= last.getDate(); day++) {
		const date = new Date(year, month, day);
		grid.appendChild(createDayCell(date, state));
	}
}

function createDayCell(date, state) {
	const iso = toIsoDate(date);
	const dayName = getDayName(date);
	const holiday = getHolidayInfo(date, state.holidays);
	const notes = state.classLog[iso] || [];
	const scheduled = getScheduleForDate(date, state.timetable, holiday);
	const isToday = isSameDate(date, new Date());

	const button = document.createElement('button');

	button.type = 'button';
	button.className = 'calendar-day';

	if (holiday.isHoliday) {
		button.classList.add('is-holiday');
	}

	if (notes.length) {
		button.classList.add('has-notes');
	}

	if (scheduled.length) {
		button.classList.add('has-schedule');
	}

	if (isToday) {
		button.classList.add('is-today');
	}

	if (state.selectedDate === iso) {
		button.classList.add('is-selected');
	}

	const indicators = [];

	if (holiday.isHoliday) {
		indicators.push(
			`<span class="calendar-day-tag holiday-tag">
				${escapeHtml(shortHolidayLabel(holiday.label))}
			</span>`,
		);
	} else if (notes.length) {
		indicators.push(
			`<span class="calendar-day-tag notes-tag">
				${notes.length} note${notes.length === 1 ? '' : 's'}
			</span>`,
		);
	} else if (scheduled.length) {
		indicators.push(
			`<span class="calendar-day-tag class-tag">
				${scheduled.length} class${scheduled.length === 1 ? '' : 'es'}
			</span>`,
		);
	}

	button.innerHTML = `
		<div class="calendar-day-top">
			<span class="calendar-day-number">
				${date.getDate()}
			</span>

			${
				notes.length
					? '<span class="calendar-note-marker" title="Class notes added"></span>'
					: ''
			}
		</div>

		<div class="calendar-day-body">
			${indicators.join('')}
		</div>
	`;

	button.setAttribute(
		'aria-label',
		`${dayName}, ${date.toLocaleDateString('en-IN', {
			day: 'numeric',
			month: 'long',
			year: 'numeric',
		})}`,
	);

	button.addEventListener('click', () => {
		state.selectedDate = iso;

		renderCalendar(state);
		renderDayDetail(date, state);
	});

	return button;
}

function selectInitialDate(state) {
	const today = new Date();
	const timetableStart = parseLocalDate(state.timetable.effectiveFrom);

	let initial;

	if (today.getFullYear() === 2026 && today >= timetableStart) {
		initial = today;
	} else {
		initial = timetableStart;
	}

	state.currentMonth = new Date(initial.getFullYear(), initial.getMonth(), 1);

	state.selectedDate = toIsoDate(initial);

	renderCalendar(state);
	renderDayDetail(initial, state);
}

function renderDayDetail(date, state) {
	const title = document.getElementById('day-detail-title');
	const status = document.getElementById('day-detail-status');
	const content = document.getElementById('day-detail-content');

	if (!title || !status || !content) return;

	const iso = toIsoDate(date);
	const holiday = getHolidayInfo(date, state.holidays);

	const schedule = getScheduleForDate(date, state.timetable, holiday);

	const notes = state.classLog[iso] || [];

	title.textContent = date.toLocaleDateString('en-IN', {
		weekday: 'long',
		day: 'numeric',
		month: 'long',
		year: 'numeric',
	});

	if (holiday.isHoliday) {
		status.innerHTML = `
			<span class="detail-pill holiday-detail-pill">
				Holiday · ${escapeHtml(holiday.label)}
			</span>
		`;
	} else if (schedule.length) {
		status.innerHTML = `
			<span class="detail-pill scheduled-detail-pill">
				${schedule.length}
				scheduled block${schedule.length === 1 ? '' : 's'}
			</span>
		`;
	} else {
		status.innerHTML = '';
	}

	let html = '';

	if (notes.length) {
		html += `
			<div class="day-detail-section">
				<h3>What was taught</h3>

				<div class="class-log-list">
					${notes.map(note => renderClassLogItem(note)).join('')}
				</div>
			</div>
		`;
	}

	if (!holiday.isHoliday && schedule.length) {
		html += `
			<div class="day-detail-section">
				<h3>Scheduled</h3>

				<div class="day-schedule-list">
					${schedule.map(item => renderScheduleItem(item, state.timetable)).join('')}
				</div>
			</div>
		`;
	}

	if (holiday.isHoliday) {
		html += `
			<p class="calendar-empty">
				No regular classes are generated for this date.
			</p>
		`;
	} else if (!schedule.length && !notes.length) {
		html += `
			<p class="calendar-empty">
				No regular timetable entries or class notes
				for this date.
			</p>
		`;
	}

	if (!notes.length && schedule.length) {
		html += `
			<div class="calendar-note-prompt">
				No class summary has been added yet.
			</div>
		`;
	}

	content.innerHTML = html;
}

function renderClassLogItem(note) {
	const subject = escapeHtml(note.subject || 'Class');

	const summary = escapeHtml(note.summary || '');

	const link = note.link;

	const action = link
		? `
			<a
				class="class-log-link"
				href="${escapeHtml(link)}"
			>
				Open notes →
			</a>
		`
		: `
			<span class="class-log-link pending">
				Subject notes link will be added when
				that page exists.
			</span>
		`;

	return `
		<article class="class-log-item">
			<div class="class-log-subject">
				${subject}
			</div>

			<div class="class-log-summary">
				${summary}
			</div>

			${action}
		</article>
	`;
}

function renderScheduleItem(item, timetable) {
	const firstPeriod = Math.min(...item.periods);
	const lastPeriod = Math.max(...item.periods);

	const start =
		timetable.periods.find(period => period.id === firstPeriod)?.start || '';

	const end =
		timetable.periods.find(period => period.id === lastPeriod)?.end || '';

	return `
		<div class="day-schedule-item">
			<div class="day-schedule-time">
				${formatTime(start)}–${formatTime(end)}
			</div>

			<div>
				<div class="day-schedule-code">
					${escapeHtml(item.code)}
				</div>

				<div class="day-schedule-name">
					${escapeHtml(item.name)}
				</div>
			</div>
		</div>
	`;
}

function getScheduleForDate(date, timetable, holiday) {
	if (!timetable) return [];

	if (date < parseLocalDate(timetable.effectiveFrom)) {
		return [];
	}

	if (holiday?.isHoliday) {
		return [];
	}

	const dayName = getDayName(date);

	return timetable.days[dayName] || [];
}

function getHolidayInfo(date, holidays) {
	const iso = toIsoDate(date);

	const exception = (holidays.exceptions || []).find(item => item.date === iso);

	if (exception?.workingDay) {
		return {
			isHoliday: false,
			label: null,
			note: exception.note || '',
		};
	}

	if (holidays.dates?.[iso]) {
		return {
			isHoliday: true,
			label: holidays.dates[iso],
			note: '',
		};
	}

	const dayName = getDayName(date);

	if (dayName === 'Sunday') {
		return {
			isHoliday: true,
			label: 'Sunday',
			note: '',
		};
	}

	if (dayName === 'Saturday' && isNthSaturday(date, [2, 4])) {
		return {
			isHoliday: true,
			label: nthSaturdayLabel(date),
			note: '',
		};
	}

	return {
		isHoliday: false,
		label: null,
		note: '',
	};
}

function isNthSaturday(date, nthValues) {
	const occurrence = Math.floor((date.getDate() - 1) / 7) + 1;

	return nthValues.includes(occurrence);
}

function nthSaturdayLabel(date) {
	const occurrence = Math.floor((date.getDate() - 1) / 7) + 1;

	return occurrence === 2 ? '2nd Saturday' : '4th Saturday';
}

function shortHolidayLabel(label) {
	if (!label) {
		return 'Holiday';
	}

	if (
		label === '2nd Saturday' ||
		label === '4th Saturday' ||
		label === 'Sunday'
	) {
		return label;
	}

	return 'Holiday';
}

function setupTimetableModal(state) {
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
	const days = [
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday',
	];

	const rows = days
		.map(day => {
			const periodCells = timetable.periods
				.map(period => {
					const match = (timetable.days[day] || []).find(item =>
						item.periods.includes(period.id),
					);

					if (!match) {
						return '<td>—</td>';
					}

					const isStart = Math.min(...match.periods) === period.id;

					if (!isStart) {
						return '';
					}

					const span = match.periods.length;

					return `
							<td
								${span > 1 ? `colspan="${span}"` : ''}
							>
								<strong>
									${escapeHtml(match.code)}
								</strong>
							</td>
						`;
				})
				.join('');

			return `
				<tr>
					<th>${day}</th>
					${periodCells}
				</tr>
			`;
		})
		.join('');

	const headers = timetable.periods
		.map(
			period => `
				<th>
					${period.id}

					<small>
						${formatTime(period.start)}–
						${formatTime(period.end)}
					</small>
				</th>
			`,
		)
		.join('');

	return `
		<div class="weekly-table-wrap">
			<table class="weekly-timetable">
				<thead>
					<tr>
						<th>Day</th>
						${headers}
					</tr>
				</thead>

				<tbody>
					${rows}
				</tbody>
			</table>
		</div>

		<p class="weekly-table-footnote">
			Lunch: 12:00 PM–12:40 PM ·
			Effective from
			${formatReadableDate(timetable.effectiveFrom)}
		</p>
	`;
}

function formatTime(value) {
	if (!value) {
		return '';
	}

	const [hour, minute] = value.split(':').map(Number);

	const date = new Date(2000, 0, 1, hour, minute);

	return date
		.toLocaleTimeString('en-IN', {
			hour: 'numeric',
			minute: '2-digit',
			hour12: true,
		})
		.replace(' ', '');
}

function formatReadableDate(iso) {
	return parseLocalDate(iso).toLocaleDateString('en-IN', {
		day: '2-digit',
		month: 'long',
		year: 'numeric',
	});
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

function escapeHtml(value) {
	return String(value)
		.replaceAll('&', '&amp;')
		.replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;')
		.replaceAll("'", '&#039;');
}

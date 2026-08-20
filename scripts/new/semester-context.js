export async function resolveSemesterContext(date = new Date()) {
	const semesterIndex = await loadSemesterIndex();
	const academicCalendar = await loadAcademicCalendar(semesterIndex);

	const currentAcademicSemesterId =
		getCurrentAcademicSemesterId(academicCalendar, date);

	const viewedSemesterId =
		getViewedSemesterId(semesterIndex);

	const activeSemesterId =
		viewedSemesterId ??
		currentAcademicSemesterId ??
		getFallbackSemesterId(
			semesterIndex,
			academicCalendar,
			date,
		);

	const semesterSummary =
		findSemester(
			semesterIndex,
			activeSemesterId,
		);

	if (!semesterSummary) {
		throw new Error(
			'No R25 semester metadata is available.',
		);
	}

	const semesterData =
		await loadSemesterData(
			semesterSummary,
		);

	const currentSemesterSummary =
		currentAcademicSemesterId
			? findSemester(
					semesterIndex,
					currentAcademicSemesterId,
				)
			: null;

	const currentSemesterData =
		currentSemesterSummary
			? await loadSemesterData(
					currentSemesterSummary,
				)
			: null;

	return {
		semesterIndex,
		academicCalendar,

		// Objective academic state.
		currentAcademicSemesterId,
		currentSemesterSummary,
		currentSemesterData,

		// Temporary browsing state, taken ONLY from the URL.
		viewedSemesterId,

		// Context the current page should use.
		activeSemesterId,
		semesterSummary,
		semesterData,
	};
}


export async function resolveCurrentSemesterContext(
	date = new Date(),
) {
	const semesterIndex =
		await loadSemesterIndex();

	const academicCalendar =
		await loadAcademicCalendar(
			semesterIndex,
		);

	const currentAcademicSemesterId =
		getCurrentAcademicSemesterId(
			academicCalendar,
			date,
		);

	const currentSemesterSummary =
		currentAcademicSemesterId
			? findSemester(
					semesterIndex,
					currentAcademicSemesterId,
				)
			: null;

	const currentSemesterData =
		currentSemesterSummary
			? await loadSemesterData(
					currentSemesterSummary,
				)
			: null;

	return {
		semesterIndex,
		academicCalendar,
		currentAcademicSemesterId,
		currentSemesterSummary,
		currentSemesterData,
	};
}


export async function loadSemesterIndex() {
	return loadJson(
		'college/semesters.json',
	);
}


export async function loadSemesterData(
	semesterSummary,
) {
	return loadJson(
		semesterSummary.data,
	);
}


export async function loadAcademicCalendar(
	semesterIndex = null,
) {
	const index =
		semesterIndex ??
		(await loadSemesterIndex());

	if (!index.academicCalendar) {
		return null;
	}

	return loadJson(
		index.academicCalendar,
	);
}


export function getCurrentAcademicSemesterId(
	academicCalendar,
	date = new Date(),
) {
	if (!academicCalendar?.semesters) {
		return null;
	}

	const iso =
		toIsoDate(date);

	for (
		const [
			semesterId,
			semester,
		] of Object.entries(
			academicCalendar.semesters,
		)
	) {
		const period =
			semester.semesterPeriod;

		if (
			!period?.start ||
			!period?.end
		) {
			continue;
		}

		if (
			iso >= period.start &&
			iso <= period.end
		) {
			return semesterId;
		}
	}

	return null;
}


export function getViewedSemesterId(
	semesterIndex,
) {
	const fromQuery =
		semesterIdFromQuery();

	if (
		fromQuery &&
		findSemester(
			semesterIndex,
			fromQuery,
		)
	) {
		return fromQuery;
	}

	const fromPath =
		semesterIdFromPath();

	if (
		fromPath &&
		findSemester(
			semesterIndex,
			fromPath,
		)
	) {
		return fromPath;
	}

	return null;
}


function getFallbackSemesterId(
	semesterIndex,
	academicCalendar,
	date,
) {
	const iso =
		toIsoDate(date);

	/*
		During a semester break there is genuinely no
		"current semester".

		For navigation context only, prefer the next
		semester whose official period has not begun yet.
	*/
	const upcoming =
		semesterIndex.semesters
			.map(semester => ({
				semester,
				period:
					academicCalendar
						?.semesters
						?.[semester.id]
						?.semesterPeriod,
			}))
			.filter(
				item =>
					item.period?.start &&
					item.period.start > iso,
			)
			.sort(
				(a, b) =>
					a.period.start.localeCompare(
						b.period.start,
					),
			);

	if (upcoming.length) {
		return upcoming[0].semester.id;
	}

	const previous =
		semesterIndex.semesters
			.map(semester => ({
				semester,
				period:
					academicCalendar
						?.semesters
						?.[semester.id]
						?.semesterPeriod,
			}))
			.filter(
				item =>
					item.period?.end &&
					item.period.end < iso,
			)
			.sort(
				(a, b) =>
					b.period.end.localeCompare(
						a.period.end,
					),
			);

	if (previous.length) {
		return previous[0].semester.id;
	}

	return (
		semesterIndex.semesters[0]?.id ??
		null
	);
}


function semesterIdFromQuery() {
	const params =
		new URLSearchParams(
			window.location.search,
		);

	return params.get('semester');
}


function semesterIdFromPath() {
	const match =
		window.location.pathname.match(
			/\/college\/(\d+-\d+)(?:\/|$)/,
		);

	return match
		? decodeURIComponent(
				match[1],
			)
		: null;
}


function findSemester(
	semesterIndex,
	semesterId,
) {
	return semesterIndex.semesters.find(
		semester =>
			semester.id === semesterId,
	);
}


function toIsoDate(date) {
	const year =
		date.getFullYear();

	const month =
		String(
			date.getMonth() + 1,
		).padStart(2, '0');

	const day =
		String(
			date.getDate(),
		).padStart(2, '0');

	return `${year}-${month}-${day}`;
}


async function loadJson(path) {
	const response =
		await fetch(path);

	if (!response.ok) {
		throw new Error(
			`Could not load ${path}: ${response.status}`,
		);
	}

	return response.json();
}

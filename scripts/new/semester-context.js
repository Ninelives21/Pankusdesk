export async function resolveSemesterContext() {
	const semesterIndex = await loadJson('college/semesters.json');
	const academicCalendar = await loadAcademicCalendar(semesterIndex);
	const semesterId = resolveSemesterId(semesterIndex, academicCalendar);
	const semesterSummary = findSemester(semesterIndex, semesterId);

	if (!semesterSummary) {
		throw new Error('No R25 semester metadata is available.');
	}

	const semesterData = await loadJson(semesterSummary.data);

	return {
		semesterIndex,
		semesterSummary,
		semesterData,
		academicCalendar,
		currentAcademicSemesterId:
			getCurrentAcademicSemesterId(academicCalendar),
	};
}

export async function selectSemester(semesterId) {
	const semesterIndex = await loadJson('college/semesters.json');
	const academicCalendar = await loadAcademicCalendar(semesterIndex);
	const semesterSummary = findSemester(semesterIndex, semesterId);

	if (!semesterSummary) {
		throw new Error(`Semester "${semesterId}" is not available in R25 metadata.`);
	}

	const semesterData = await loadJson(semesterSummary.data);

	const detail = {
		semesterIndex,
		semesterSummary,
		semesterData,
		academicCalendar,
		currentAcademicSemesterId:
			getCurrentAcademicSemesterId(academicCalendar),
	};

	window.dispatchEvent(
		new CustomEvent('pankusdesk:semester-change', { detail }),
	);

	return detail;
}

export async function loadSemesterIndex() {
	return loadJson('college/semesters.json');
}

export async function loadSemesterData(semesterSummary) {
	return loadJson(semesterSummary.data);
}

export async function loadAcademicCalendar(semesterIndex = null) {
	const index = semesterIndex ?? (await loadSemesterIndex());

	if (!index.academicCalendar) {
		return null;
	}

	return loadJson(index.academicCalendar);
}

export function getCurrentAcademicSemesterId(
	academicCalendar,
	date = new Date(),
) {
	if (!academicCalendar?.semesters) {
		return null;
	}

	const iso = toIsoDate(date);

	for (const [semesterId, semester] of Object.entries(
		academicCalendar.semesters,
	)) {
		const period = semester.semesterPeriod;
		if (!period?.start || !period?.end) continue;

		if (iso >= period.start && iso <= period.end) {
			return semesterId;
		}
	}

	return null;
}

function resolveSemesterId(semesterIndex, academicCalendar) {
	const fromQuery = semesterIdFromQuery();

	if (fromQuery && findSemester(semesterIndex, fromQuery)) {
		return fromQuery;
	}

	const fromUrl = semesterIdFromPath();

	if (fromUrl && findSemester(semesterIndex, fromUrl)) {
		return fromUrl;
	}

	const currentByDate =
		getCurrentAcademicSemesterId(academicCalendar);

	if (currentByDate && findSemester(semesterIndex, currentByDate)) {
		return currentByDate;
	}

	return semesterIndex.semesters[0]?.id ?? null;
}

function semesterIdFromQuery() {
	const params = new URLSearchParams(window.location.search);
	return params.get('semester');
}

function semesterIdFromPath() {
	const match = window.location.pathname.match(/\/college\/([^/]+)\//);
	return match ? decodeURIComponent(match[1]) : null;
}

function findSemester(semesterIndex, semesterId) {
	return semesterIndex.semesters.find(
		semester => semester.id === semesterId,
	);
}

function toIsoDate(date) {
	const year = date.getFullYear();
	const month = String(date.getMonth() + 1).padStart(2, '0');
	const day = String(date.getDate()).padStart(2, '0');

	return `${year}-${month}-${day}`;
}

async function loadJson(path) {
	const response = await fetch(path);

	if (!response.ok) {
		throw new Error(`Could not load ${path}: ${response.status}`);
	}

	return response.json();
}

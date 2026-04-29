document.addEventListener('DOMContentLoaded', function () {
	let pathToRoot = getRootPath();
	fetch(pathToRoot + 'navbar.html')
		.then(response => response.text())
		.then(data => {
			document.querySelector('nav').innerHTML = data;
			updatePaths(pathToRoot);
			highlightActivePage();
		});
});

function getRootPath() {
	let depth = window.location.pathname.split('/').length - 3;
	let pathToRoot = '';
	for (let i = 0; i < depth; i++) {
		pathToRoot += '../';
	}
	return pathToRoot;
}

function updatePaths(pathToRoot) {
	// Update icon paths
	const icons = document.querySelectorAll('.navbar-icons img');
	icons.forEach(icon => {
		icon.src = pathToRoot + icon.getAttribute('src');
	});

	// Update link paths
	const links = document.querySelectorAll('.navbar-icons a');
	links.forEach(link => {
		//alert(link);
		let href = link.getAttribute('href');
		link.setAttribute('href', pathToRoot + href);
	});

	// Update logo path
	const logo = document.querySelector('.logo img');
	if (logo) {
		logo.src = pathToRoot + logo.getAttribute('src');
	}

	const logoLink = document.querySelector('.logo a');
	if (logoLink) {
		//alert('here');
		logoLink.setAttribute('href', pathToRoot + 'index.html');
	}
}

function highlightActivePage() {
	const path = window.location.pathname;
	const page = path.split('/').pop().split('.')[0];

	const iconMap = {
		index: 'home-icon',
		study_material: 'study-material-icon',
		study: 'study-icon',
		question_builder: 'question-builder-icon',
		daily_planner: 'daily-planner-icon',
		calendar: 'calendar-icon',
		activity_log: 'activity-log-icon',
		languages: 'languages-icon',
	};

	const activeIconId = iconMap[page];
	if (activeIconId) {
		document.getElementById(activeIconId).classList.add('active');
	}
}

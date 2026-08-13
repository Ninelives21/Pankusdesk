document.addEventListener('DOMContentLoaded', async () => {
	const mount = document.getElementById('navbar-new');
	if (!mount) return;

	const root = getRootPrefix();

	try {
		const response = await fetch(root + 'navbar_new.html');
		if (!response.ok) throw new Error(`Navbar load failed: ${response.status}`);

		mount.innerHTML = await response.text();

		rewriteNavbarPaths(root);
		initMobileNav();
		initDropdowns();
		highlightCurrentNav();
	} catch (error) {
		console.error(error);
	}
});

function getRootPrefix() {
	const explicitRoot = document.body.dataset.root;
	if (explicitRoot !== undefined) return explicitRoot;

	const pathname = window.location.pathname;
	const marker = '/Pankusdesk/';
	const markerIndex = pathname.indexOf(marker);

	if (markerIndex !== -1) {
		const afterRepo = pathname.slice(markerIndex + marker.length);
		const segments = afterRepo.split('/').filter(Boolean);
		const fileIsPresent = segments.length && segments[segments.length - 1].includes('.');
		const depth = fileIsPresent ? Math.max(0, segments.length - 1) : segments.length;
		return '../'.repeat(depth);
	}

	return '';
}

function rewriteNavbarPaths(root) {
	document
		.querySelectorAll('#navbar-new a[href]')
		.forEach(link => {
			const href = link.getAttribute('href');

			if (
				!href ||
				href.startsWith('#') ||
				href.startsWith('http://') ||
				href.startsWith('https://') ||
				href.startsWith('mailto:')
			) {
				return;
			}

			link.setAttribute('href', root + href);
		});
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
					other.querySelector('.nav-dropdown-button')?.setAttribute('aria-expanded', 'false');
				}
			});

			const open = dropdown.classList.toggle('open');
			button.setAttribute('aria-expanded', String(open));
		});
	});

	document.addEventListener('click', () => {
		document.querySelectorAll('.nav-dropdown.open').forEach(dropdown => {
			dropdown.classList.remove('open');
			dropdown.querySelector('.nav-dropdown-button')?.setAttribute('aria-expanded', 'false');
		});
	});
}

function highlightCurrentNav() {
	const path = window.location.pathname;

	let key = 'home';

	if (path.includes('/college/1-1/calendar')) {
		key = 'calendar';
	} else if (path.includes('/college/1-1/')) {
		key = 'semester';
	} else if (path.endsWith('/index_old.html')) {
		key = 'archive';
	}

	document.querySelector(`[data-nav="${key}"]`)?.classList.add('active');
}

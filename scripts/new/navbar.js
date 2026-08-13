document.addEventListener('DOMContentLoaded', async () => {
	const mount = document.getElementById('navbar-new');
	if (!mount) return;

	try {
		const response = await fetch('navbar_new.html');

		if (!response.ok) {
			throw new Error(`Navbar load failed: ${response.status}`);
		}

		mount.innerHTML = await response.text();

		initMobileNav();
		initDropdowns();
		highlightCurrentNav();
	} catch (error) {
		console.error('Navbar error:', error);
	}
});

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

	if (path.includes('/college/1-1/calendar')) {
		key = 'calendar';
	} else if (path.includes('/college/1-1/')) {
		key = 'semester';
	} else if (path.endsWith('/index_old.html')) {
		key = 'archive';
	}

	document.querySelector(`[data-nav="${key}"]`)?.classList.add('active');
}

(function () {
	'use strict';

	// The site-root base must not send an in-page return link to the homepage.
	document.querySelectorAll('.end-sem-nav a[href^="#"]').forEach(link => {
		link.href = window.location.pathname + window.location.search + link.getAttribute('href');
	});
})();

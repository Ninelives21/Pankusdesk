const coll = document.getElementsByClassName('accordion-button');
let i;

for (i = 0; i < coll.length; i++) {
	coll[i].addEventListener('click', function () {
		this.classList.toggle('active');
		var content = this.nextElementSibling;
		if (content.style.display === 'block') {
			content.style.display = 'none';
		} else {
			content.style.display = 'block';
		}
	});
}

// Function to make all accordion sections open on certain pages
function openAllAccordions() {
	for (i = 0; i < coll.length; i++) {
		coll[i].classList.add('active');
		var content = coll[i].nextElementSibling;
		content.style.display = 'block';
		content.classList.add('accordion-open');
	}
}

// Call this function on pages where all accordion sections should be open
// document.addEventListener('DOMContentLoaded', function () {
// 	if (window.location.pathname.endsWith('specific-page.html')) {
// 		// Adjust this condition to match your page
// 		openAllAccordions();
// 	}
// });

function openAccordionFromHash() {
	const hash = window.location.hash;

	if (!hash) return;

	const target = document.querySelector(hash);
	if (!target) return;

	const accordionContent = target.closest('.accordion-content');
	const accordionItem = target.closest('.accordion-item');
	const accordionButton = accordionItem?.querySelector('.accordion-button');

	if (accordionContent) {
		accordionContent.style.display = 'block';
		accordionContent.classList.add('accordion-open');
	}

	if (accordionButton) {
		accordionButton.classList.add('active');
	}

	setTimeout(() => {
		target.scrollIntoView({ behavior: 'smooth', block: 'start' });
	}, 150);
}

document.addEventListener('DOMContentLoaded', openAccordionFromHash);
window.addEventListener('hashchange', openAccordionFromHash);

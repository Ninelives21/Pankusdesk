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

// ---------------------------------------------
//  ACCORDION SYSTEM (Supports Nested Accordions)
//  Smooth Animation + Scoped Toggle
// ---------------------------------------------

document.addEventListener('DOMContentLoaded', function () {
	const allAccordions = document.querySelectorAll('.accordion');

	allAccordions.forEach(accordion => {
		const buttons = accordion.querySelectorAll('.accordion-button');

		buttons.forEach(btn => {
			let content = btn.nextElementSibling;

			// Prepare content for smooth animation
			content.style.maxHeight = '0px';
			content.style.overflow = 'hidden';
			content.style.transition = 'max-height 0.35s ease';

			btn.addEventListener('click', function () {
				this.classList.toggle('active');

				if (content.style.maxHeight === '0px') {
					// OPEN
					content.style.display = 'block';
					content.style.maxHeight = content.scrollHeight + 'px';
					content.classList.add('accordion-open');
				} else {
					// CLOSE
					content.style.maxHeight = '0px';
					setTimeout(() => {
						content.style.display = 'none';
					}, 350);
					content.classList.remove('accordion-open');
				}
			});
		});
	});
});

// -------------------------------------------------
// OPEN ALL ACCORDIONS ON SPECIFIC PAGES
// -------------------------------------------------

function openAllAccordions() {
	const allButtons = document.querySelectorAll('.accordion-button');

	allButtons.forEach(btn => {
		let content = btn.nextElementSibling;

		btn.classList.add('active');
		content.style.display = 'block';
		content.style.maxHeight = content.scrollHeight + 'px';
		content.classList.add('accordion-open');
	});
}

// Example usage:
// document.addEventListener("DOMContentLoaded", function () {
//     if (window.location.pathname.includes("resonance_page.html")) {
//         openAllAccordions();
//     }
// });

(function () {
'use strict';
document.addEventListener('DOMContentLoaded', async () => {
 const page = document.querySelector('.institutional-document');
 if (!page) return;
 const contents = page.querySelector('.document-contents');
 const narrow = matchMedia('(max-width: 800px)');
 const setContents = () => { contents.open = !narrow.matches; };
 setContents();
 narrow.addEventListener('change', setContents);
 contents.addEventListener('click', event => {
  const link = event.target.closest('a');
  if (!link) return;
  const url = new URL(link.href);
  const target = document.getElementById(decodeURIComponent(url.hash.slice(1)));
  if (!target) return;
  event.preventDefault();
  contents.querySelectorAll('[aria-current]').forEach(item => item.removeAttribute('aria-current'));
  link.setAttribute('aria-current', 'location');
  if (narrow.matches) contents.open = false;
  history.pushState(null, '', url.hash);
  target.scrollIntoView({ behavior: 'instant', block: 'start' });
 });
 try {
  await window.PankuStudyUI?.typesetMath?.(page);
 } catch (error) {
  console.warn('Document mathematics could not be typeset:', error);
 }
 if (location.hash) document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView({ behavior: 'instant', block: 'start' });
 page.dataset.documentReady = 'true';
});
})();

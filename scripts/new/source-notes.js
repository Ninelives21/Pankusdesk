(function () {
  'use strict';
  const root = document.querySelector('.end-sem-content');
  if (!root || !window.PankuStudyUI) return;
  const ui = window.PankuStudyUI;
  ui.initAccordions(root);
  // A lossless source panel may need its native size for small labels.
  root.querySelectorAll('.source-visual img').forEach(img => {
    const link = document.createElement('a');
    link.href = img.src;
    link.target = '_blank';
    link.rel = 'noopener';
    link.setAttribute('aria-label', `Open full-size image: ${img.alt}`);
    img.replaceWith(link);
    link.append(img);
  });
  ui.typesetMath(root).then(() => {
    if (location.hash) document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView();
  }).catch(() => {
    const notice = document.createElement('p');
    notice.setAttribute('role', 'status');
    notice.textContent = 'Equation rendering is unavailable. Reload to retry; the source notes and original images remain available.';
    root.prepend(notice);
  });
})();

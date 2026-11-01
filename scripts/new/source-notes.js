(function () {
  'use strict';
  const root = document.querySelector('.end-sem-content');
  if (!root || !window.PankuStudyUI) return;
  const ui = window.PankuStudyUI;
  const navGroups = [...document.querySelectorAll('.source-nav-group')];
  navGroups.forEach(group => group.addEventListener('toggle', () => {
    if (group.open) navGroups.forEach(other => { if (other !== group) other.open = false; });
  }));
  function revealCurrentTopic() {
    let currentLink = null;
    navGroups.forEach(group => {
      group.querySelectorAll('a').forEach(link => {
        const current = Boolean(location.hash) && link.hash === location.hash;
        if (current) {
          group.open = true;
          link.setAttribute('aria-current', 'location');
          currentLink = link;
        } else link.removeAttribute('aria-current');
      });
    });
    if (currentLink) requestAnimationFrame(() => {
      const nav = currentLink.closest('.end-sem-nav');
      const linkBox = currentLink.getBoundingClientRect();
      const navBox = nav.getBoundingClientRect();
      if (linkBox.top < navBox.top + 12) nav.scrollTop += linkBox.top - navBox.top - 12;
      else if (linkBox.bottom > navBox.bottom - 12) nav.scrollTop += linkBox.bottom - navBox.bottom + 12;
    });
  }
  revealCurrentTopic();
  window.addEventListener('hashchange', revealCurrentTopic);
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

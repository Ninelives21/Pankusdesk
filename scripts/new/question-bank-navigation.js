(function () {
'use strict';
const bankPath = 'college/1-1/chemistry-engineers/question-banks.html';
function fragment() {
 try { return decodeURIComponent(location.hash.slice(1)); } catch (_) { return ''; }
}
document.addEventListener('DOMContentLoaded', () => {
 if (document.body.dataset.questionBankOrigin) {
  let migration;
  async function redirectMovedQuestion() {
   const id = fragment();
   if (!id) return;
   try {
    migration ||= fetch(new URL('college/1-1/chemistry-engineers/revision/question-bank-relocation.json', document.baseURI)).then(response => {
     if (!response.ok) throw new Error('Question relocation record could not be loaded.');
     return response.json();
    });
    const record = (await migration).units[document.body.dataset.questionBankOrigin];
    if (record?.ids.includes(id)) location.replace(new URL(`${bankPath}#${encodeURIComponent(id)}`, document.baseURI).href);
   } catch (error) { console.warn('Use the question bank link on this notes page:', error); }
  }
  redirectMovedQuestion();
  addEventListener('hashchange', redirectMovedQuestion);
  return;
 }
 if (!document.body.dataset.questionBank) return;
 const units = [...document.querySelectorAll('[data-bank-unit-section]')];
 const links = [...document.querySelectorAll('[data-bank-unit]')];
 const status = document.getElementById('bank-view-status');
 const ui = window.PankuStudyUI;
 ui?.initAccordions?.(document.querySelector('.document-body'));
 document.querySelectorAll('.source-visual img').forEach(img => {
  if (img.closest('a')) return;
  const link = document.createElement('a');link.href = img.src;link.target = '_blank';link.rel = 'noopener';
  link.setAttribute('aria-label', `Open full-size image: ${img.alt}`);img.replaceWith(link);link.append(img);
 });
 const defaultUnit = document.body.dataset.bankDefault || '1';
 const allId = document.body.dataset.bankAllId || 'all-units';
 let currentUnit = defaultUnit;
 function select(id, scroll = false) {
  const target = id ? document.getElementById(id) : null;
  const allView = [allId, 'existing-answers', 'source-questions-pending'].includes(id);
  const unit = id === 'document-top' ? currentUnit : allView ? 'all' : target?.closest('[data-bank-unit-section]')?.dataset.bankUnitSection || defaultUnit;
  currentUnit = unit;
  units.forEach(section => { section.hidden = unit !== 'all' && section.dataset.bankUnitSection !== unit; });
  links.forEach(link => {
   if (link.dataset.bankUnit === unit) link.setAttribute('aria-current', 'location');
   else link.removeAttribute('aria-current');
  });
  const selected = units.find(section => section.dataset.bankUnitSection === unit);
  status.textContent = unit === 'all' ? (document.body.dataset.bankAllLabel || 'Consolidated view · all five units') : selected?.dataset.bankTitle ? `Viewing ${selected.dataset.bankTitle}` : `Viewing Unit ${unit}`;
  let parent = target;
  while (parent) {
   if (parent.tagName === 'DETAILS') parent.open = true;
   parent = parent.parentElement;
  }
  if (scroll && target) requestAnimationFrame(() => target.scrollIntoView({behavior: 'instant', block: 'start'}));
  document.body.dataset.bankReady = 'true';
 }
 // Select the unit before the shared Contents handler scrolls to its target.
 document.querySelector('.document-contents').addEventListener('click', event => {
  const link = event.target.closest('[data-bank-unit]');
  if (link) select(new URL(link.href).hash.slice(1));
 }, true);
 addEventListener('hashchange', () => select(fragment(), true));
 addEventListener('popstate', () => select(fragment(), true));
 select(fragment());
});
})();

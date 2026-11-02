/* College worksheet adapter. Question/solution accordions and mathematics use the shared study UI. */
(function () {
'use strict';
document.addEventListener('DOMContentLoaded', init);
async function init() {
 const page = document.querySelector('[data-worksheet-index]');
 if (!page) return;
 const ui = window.PankuStudyUI;
 const escape = ui.escapeHtml;
 try {
  const indexUrl = new URL(page.dataset.worksheetIndex, document.baseURI);
  const response = await fetch(indexUrl);
  if (!response.ok) throw new Error(`Worksheet index returned ${response.status}`);
  const index = await response.json();
  const sheets = await Promise.all(index.worksheets.map(async entry => {
   const url = new URL(entry.href, indexUrl);
   const response = await fetch(url);
   if (!response.ok) throw new Error(`${entry.label} returned ${response.status}`);
   return { ...await response.json(), url };
  }));
  const nav = page.querySelector('[data-worksheet-nav]');
  const content = page.querySelector('[data-worksheet-content]');
  nav.innerHTML = sheets.map(sheet => `<a class="worksheet-link" href="${escape(location.pathname + location.search)}#${escape(sheet.id)}" data-worksheet="${escape(sheet.id)}">${escape(sheet.label)}</a>`).join('');
  let selected;
  async function select(sheet) {
   if (selected === sheet.id) return;
   selected = sheet.id;
   nav.querySelectorAll('[data-worksheet]').forEach(link => {
    if (link.dataset.worksheet === selected) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
   });
   content.innerHTML = `<section id="${escape(sheet.id)}"><h2>${escape(sheet.title)}</h2><p>${escape(sheet.source.note)}</p><p><a href="${escape(new URL(sheet.source.href, sheet.url).href)}">Open original worksheet PDF ↗</a></p><p class="worksheet-legend">Amber question numbers identify Unit III and Unit IV questions. Numbering restarts in each original question set.</p><nav class="worksheet-groups" aria-label="Question sets">${sheet.groups.map(group => `<a href="${escape(location.pathname + location.search)}#${escape(group.id)}">Unit ${group.unit} · ${escape(group.title)}</a>`).join('')}</nav>${sheet.groups.map(group => `<section class="worksheet-group${[3,4].includes(group.unit) ? ' worksheet-group--focus' : ''}" id="${escape(group.id)}"><h3>Unit ${group.unit} · ${escape(group.title)}</h3>${ui.renderAccordionGroup({label:'Questions',isExampleGroup:true,items:group.questions.map(q => ({...q,title:`Q${q.number}`}))})}</section>`).join('')}</section>`;
   ui.initAccordions(content);
   try { await ui.typesetMath(content); }
   catch (error) {
    console.error('Worksheet mathematics:',error);
    const notice = document.createElement('p');
    notice.className = 'worksheet-notice';
    notice.textContent = 'Mathematics could not be typeset. Reload when online; the question text and solutions remain available.';
    content.prepend(notice);
   }
  }
  async function reveal() {
   const id = decodeURIComponent(location.hash.slice(1));
   const sheet = sheets.find(sheet => sheet.id === id || sheet.groups.some(group => group.id === id || group.questions.some(q => q.id === id))) || sheets[0];
   if (!sheet) { content.textContent = 'No worksheets have been added yet.'; return; }
   await select(sheet);
   const target = id && document.getElementById(id);
   if (target && content.contains(target)) {
    if (target.matches('details')) target.open = true;
    target.scrollIntoView({block:'start'});
   }
  }
  nav.addEventListener('click', event => {
   const link = event.target.closest('[data-worksheet]');
   if (!link) return;
   event.preventDefault();
   history.pushState(null,'',link.href);
   reveal();
  });
  window.addEventListener('hashchange', reveal);
  await reveal();
 } catch (error) {
  console.error('Worksheets:',error);
  page.querySelector('[data-worksheet-content]').textContent = 'Worksheets could not be loaded. Please reload to try again.';
 }
}
})();

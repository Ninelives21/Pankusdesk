(function () {
'use strict';
const esc = value => String(value ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
async function json(path) {
 const response = await fetch(new URL(path, document.baseURI));
 if (!response.ok) throw new Error(`Resource metadata returned ${response.status}`);
 return response.json();
}
function card(resource, root) {
 const href = resource.href ? new URL(resource.href, root).href : '';
 return `<article class="study-tool-card"${resource.id ? ` id="${esc(resource.id)}"` : ''}><div class="tool-label">${esc(resource.label || 'Study resource')}</div><h3>${href ? `<a class="subject-card-link" href="${esc(href)}">${esc(resource.title)}</a>` : esc(resource.title)}</h3><p>${esc(resource.description)}</p>${resource.state ? `<span class="tool-state">${esc(resource.state)}</span>` : ''}${resource.links || ''}${resource.items ? `<ul class="subject-resource-links">${resource.items.map(item => `<li><a href="${esc(new URL(item.href,root))}">${esc(item.title)}</a></li>`).join('')}</ul>` : ''}${href ? `<span class="tool-action" aria-hidden="true">${esc(resource.action || 'Open resource')} →</span>` : ''}</article>`;
}
function unitLinks(config, subject, root) {
 return (config.availableUnits || []).map(number => {
  const unit = subject.units.find(item => Number(item.number) === Number(number));
  const href = new URL(config.hrefPattern.replace('{unit}', number), root);
  return `<li><a href="${esc(href)}">Unit ${number} · ${esc(unit?.title || '')}</a></li>`;
 }).join('');
}
document.addEventListener('DOMContentLoaded', async () => {
 const page = document.querySelector('.subject-home');
 if (!page) return;
 const targets = ['questions','notes'];
 try {
  const [extra, subject] = await Promise.all([json(page.dataset.indexResourcesJson), page.dataset.subjectJson ? json(page.dataset.subjectJson) : Promise.resolve(null)]);
  const root = new URL(page.dataset.indexResourcesJson, document.baseURI);
  const questions = [...extra.questions], notes = [...extra.notes];
  if (subject) {
   const identity = document.createElement('p');
   identity.className = 'subject-identity';
   identity.textContent = `${subject.code} · ${subject.credits} credits`;
   page.querySelector('h1').after(identity);
  }
  if (subject) {
   for (const entry of subject.studyResources || []) {
    const resource = {...subject.practice?.[entry.practiceKey], ...entry};
    if (entry.unitResources) {
     notes.push({...resource, links:`<ul class="subject-resource-links">${entry.unitResources.filter(unit => unit.href).map(unit => `<li><a href="${esc(new URL(unit.href, root))}">Unit ${unit.number} · ${esc(subject.units.find(item => item.number === unit.number)?.title || unit.title || '')}</a>${unit.state ? ` <small>${esc(unit.state)}</small>` : ''}</li>`).join('')}</ul>`});
    } else if (resource.href || resource.state) {
     const isQuestion = !!entry.practiceKey || /worksheet/i.test(entry.title);
     (isQuestion ? questions : notes).push(resource);
    }
   }
   const classes = subject.classNotes;
   if (classes?.availableUnits?.length) notes.unshift({title:classes.label,description:classes.description,label:'Class notes',links:`<ul class="subject-resource-links">${unitLinks(classes,subject,root)}</ul>`});
   const bookQuestions = subject.practice?.unitQuestions;
   if (bookQuestions?.availableUnits?.length) questions.push({title:'Textbook Questions',description:bookQuestions.description,label:'Textbook practice',links:`<ul class="subject-resource-links">${unitLinks(bookQuestions,subject,root)}</ul>`});
   notes.push({title:'Textbook Notes',label:'Textbook reference',description:'Existing textbook-led pages, organised by unit. Publication states are shown as recorded; draft and scaffold pages are still in progress.',links:`<ul class="subject-resource-links" id="subject-unit-grid">${subject.units.map(unit => `<li><a href="${esc(new URL(`unit-${unit.number}.html`,root))}">Unit ${unit.number} · ${esc(unit.title)}</a> <small>${esc(unit.publicationStatus)}</small></li>`).join('')}</ul>`});
  }
  for (const [key,resources] of [['questions',questions],['notes',notes]]) {
   page.querySelector(`[data-${key}]`).innerHTML = resources.length ? resources.map(resource => card(resource,root)).join('') : `<p class="subject-empty">No ${key} have been added for this subject yet.</p>`;
  }
  page.dataset.homeReady = 'true';
  const aliases = {'school-guidance-title':'questions','textbook-study':'subject-unit-grid'};
  const hash = decodeURIComponent(location.hash.slice(1));
  document.getElementById(aliases[hash] || hash)?.scrollIntoView();
 } catch (error) {
  console.error('Subject resources could not be loaded:',error);
  for (const key of targets) page.querySelector(`[data-${key}]`).innerHTML = '<p class="unit-error">Resources could not be loaded. Please reload this page or try again later.</p>';
 }
});
})();

/* Data adapter for C worksheets. Shared study UI owns the question accordions. */
(function () {
'use strict';
document.addEventListener('DOMContentLoaded', async () => {
 const page=document.querySelector('[data-programming-worksheet]'); if(!page) return;
 const ui=window.PankuStudyUI, escape=ui.escapeHtml;
 const content=page.querySelector('[data-programming-content]'), nav=page.querySelector('[data-programming-nav]');
 try {
  const response=await fetch(new URL(page.dataset.programmingWorksheet,document.baseURI),{cache:'no-store'});
  if(!response.ok) throw new Error(`Worksheet returned ${response.status}`);
  const bank=await response.json();
  const path=location.pathname+location.search;
  const numbers=[...new Set(bank.problems.map(p=>parseInt(p.number,10)))];
  nav.innerHTML=numbers.map(n=>`<section><a class="programming-parent" href="${escape(path)}#problem-${n}">Problem ${n}</a>${bank.problems.filter(p=>parseInt(p.number,10)===n).map(p=>`<a class="programming-part-link" href="${escape(path)}#${escape(p.id)}">${escape(p.number.replace(/([a-z])$/,'($1)'))} · ${escape(p.title)}</a>`).join('')}</section>`).join('');
  content.innerHTML=numbers.map(n=>`<section class="programming-group" id="problem-${n}"><h2>Problem ${n}</h2>${ui.renderAccordionGroup({label:`Problem ${n}`,isExampleGroup:true,items:bank.problems.filter(p=>parseInt(p.number,10)===n).map(p=>({id:p.id,title:`${p.number.replace(/([a-z])$/,'($1)')} · ${p.title}`,question_paragraphs:[p.question],paragraphs:p.explanation}))})}</section>`).join('');
  for(const problem of bank.problems) {
   const answer=document.getElementById(problem.id).querySelector('.study-example-solution');
   if(problem.flow.length) { const h=document.createElement('h3');h.textContent='Flowchart logic (text)';answer.append(h);for(const step of problem.flow){const p=document.createElement('p');p.textContent=step;answer.append(p);} }
   const heading=document.createElement('h3');heading.textContent='C program';answer.append(heading);
   const pre=document.createElement('pre'),code=document.createElement('code');code.className='language-c';code.textContent=problem.code;pre.append(code);answer.append(pre);
   const sample=document.createElement('h3');sample.textContent='Example input';answer.append(sample);
   const input=document.createElement('pre');input.textContent=problem.test_input;answer.append(input);
   const outputLabel=document.createElement('h3');outputLabel.textContent='Expected result (prompts omitted)';answer.append(outputLabel);
   const result=document.createElement('pre');result.textContent=problem.expected;answer.append(result);
  }
  ui.initAccordions(content);
  const panel=page.querySelector('.programming-nav');
  if(matchMedia('(max-width:700px)').matches) panel.open=false;
  function reveal(){let id;try{id=decodeURIComponent(location.hash.slice(1));}catch(_){return;} const target=document.getElementById(id);if(target&&content.contains(target)){if(target.matches('details'))target.open=true;target.scrollIntoView({block:'start'});nav.querySelectorAll('a').forEach(a=>{if(a.hash===location.hash)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});}}
  nav.addEventListener('click',e=>{const a=e.target.closest('a');if(!a)return;if(matchMedia('(max-width:700px)').matches)panel.open=false;});
  window.addEventListener('hashchange',reveal);reveal();page.dataset.worksheetReady='true';
 }catch(error){console.error(error);content.textContent='Worksheet could not be loaded. Reload to try again.';nav.textContent='Contents unavailable.';}
});
})();

/* Shared source-backed revision/paper adapter. The shared study UI owns answers. */
(function () {
'use strict';
document.addEventListener('DOMContentLoaded',async()=>{
 const page=document.querySelector('[data-exam-prep]');if(!page)return;
 const ui=window.PankuStudyUI,esc=ui.escapeHtml;
 const content=page.querySelector('[data-exam-content]'),nav=page.querySelector('[data-exam-nav]');
 const collection=page.querySelector('[data-exam-collection]'),unit=page.querySelector('[data-exam-unit]'),kind=page.querySelector('[data-exam-kind]'),search=page.querySelector('[data-exam-search]');
 const status=page.querySelector('[data-exam-status]'),intro=page.querySelector('[data-exam-intro]'),panel=page.querySelector('[data-exam-contents]');
 try {
  const response=await fetch(new URL(page.dataset.examPrep,document.baseURI));if(!response.ok)throw new Error(`Question bank returned ${response.status}`);
  const bank=await response.json(),sources=new Map(bank.sources.map(s=>[s.id,s])),occurrences=new Map(bank.occurrences.map(o=>[o.id,o]));
  collection.innerHTML='<option value="revision">Revision questions</option>'+bank.papers.map(p=>`<option value="${esc(p.id)}">${esc(p.title)} · ${esc(p.regulation)}</option>`).join('');
  const numbers=new Map(bank.questions.map((q,i)=>[q.id,`R${i+1}`]));
  function program(p){return `<section class="exam-program"><h4>${esc(p.title)}</h4><p>${esc(p.note)}</p><pre><code class="language-c">${esc(p.code)}</code></pre><h5>Example input</h5><pre>${esc(p.input||'(No standard input; see the stated fixture or command.)')}</pre><h5>Expected result</h5><pre>${esc(p.expected||'(No console output; see the stated output files.)')}</pre></section>`;}
  function provenance(q,a){
   const entries=(q.occurrences||[]).map(id=>occurrences.get(id));
   return `<details class="exam-provenance"><summary>Sources &amp; question variants</summary><p>${esc(a.authority)}. Basis: ${esc(a.basis_label)}${a.note_refs.length?`; ${a.basis.startsWith('priyanka')?'Priyanka images':'senior PDF pages'} ${esc(a.note_refs.join(', '))}`:''}${a.senior_pages?`; senior PDF pages ${esc(a.senior_pages.join(', '))}`:''}.</p>${entries.map(o=>`<p><strong>${esc(sources.get(o.source).label)}</strong> · p. ${o.page} · ${esc(o.section)} Q${esc(o.number)}<br>${esc(o.question)}</p>`).join('')}${q.paper_source?`<p>${esc(q.paper_source)}</p>`:''}</details>`;
  }
  function item(q){
   const a=bank.answers[q.answer],number=numbers.get(q.id)||q.number;
   const lines=q.question.split('\n');
   const html=ui.renderAccordionGroup({label:'Questions',isExampleGroup:true,items:[{id:q.id,title:`${number} · ${q.title||a.title}${q.marks?` · ${q.marks} marks`:''}`,question_paragraphs:[lines[0]],paragraphs:q.question_parts?[]:a.paragraphs,solution_parts:q.answer_parts||(q.question_parts?a.paragraphs.slice(0,2).map((p,i)=>({label:i===0?'(i) Pointer expression':'(ii) Program behavior',paragraphs:[p,...(i===1?a.paragraphs.slice(2):[])]})):[]),discrepancy:q.discrepancy?{label:'Source discrepancy',message:q.discrepancy}:null,final_answer:q.answer==='macro-output'?'The printed macro expression evaluates to 41 (with a standard hosted entry point).':q.answer==='pointer-invalid'?'(i) *(*(*(*(a+i)+j)+k)+l); (ii) undefined behavior; no portable output.':undefined}]});
   return html;
  }
  function complete(q){
   const node=document.getElementById(q.id),a=bank.answers[q.answer];
   const question=node.querySelector('.study-example-question');
   if(q.question.includes('\n')){const pre=document.createElement('pre');pre.className='exam-question-code';pre.textContent=q.question.split('\n').slice(1).join('\n');question.append(pre);}
   for(const p of q.question_parts||[]){const block=document.createElement('span');block.className='exam-question-part';block.id=q.id+'-part-'+p.label.replace(/[^a-z0-9]/gi,'');block.textContent=`${p.label} ${p.text}`;if(p.code){const pre=document.createElement('pre');pre.textContent=p.code;block.append(pre);}question.append(block);}
   const answer=node.querySelector('.study-example-solution');
   const showPrograms=q.kind==='long'||q.marks>=4||/sample code|program|example/i.test(q.question);
   if(showPrograms&&a.programs.length){answer.insertAdjacentHTML('beforeend',a.programs.map(id=>program(bank.programs[id])).join(''));const result=document.createElement('p');result.className='study-final-answer';const strong=document.createElement('strong');strong.textContent='Final result: the standalone examples produce the expected outputs/files shown above under their stated input limits.';result.append(strong);answer.append(result);}
   answer.insertAdjacentHTML('beforeend',provenance(q,a));
  }
  function matches(q){
   const a=bank.answers[q.answer],text=[q.question,q.title,a.title,...(q.occurrences||[]).map(id=>occurrences.get(id).question)].join(' ').toLowerCase();
   return (!unit.value||String(q.unit)===unit.value)&&(!kind.value||q.kind===kind.value||(kind.value==='program'&&(a.programs.length>0||q.answer==='macro-output'||q.answer==='pointer-invalid')))&&(!search.value.trim()||text.includes(search.value.trim().toLowerCase()));
  }
  function render(){
   let records=[],sections=[],navSections=[];
   const paper=bank.papers.find(p=>p.id===collection.value);
   page.querySelectorAll('[data-exam-view]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.examView===(paper?'papers':'revision'))));
   if(paper){
    intro.innerHTML=`<h2>${esc(paper.title)} <span class="tool-state">${esc(paper.regulation)}</span></h2><p>${esc(paper.subject_code)} · ${paper.minutes} minutes · ${paper.max_marks} marks · ${esc(paper.status)}</p><ul>${paper.instructions.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>`;
    for(const g of paper.groups){
     const parts=g.parts.map(q=>({...q,kind:g.unit?'long':'short',paper_source:paper.sources.map(id=>`${sources.get(id).filename}, p. ${paper.source_pages[id].join(',')}`).join('; ')})).filter(matches);if(!parts.length)continue;
     records.push(...parts);sections.push(`${g.or_before?'<p class="exam-or">OR</p>':''}<section class="exam-group" id="${esc(g.id)}"><h3>${esc(g.label)}${g.unit?` · Unit ${g.unit}`:''}</h3>${parts.map(item).join('')}</section>`);
     navSections.push(`<section><a class="exam-parent" href="${esc(location.pathname)}#${esc(g.id)}">${esc(g.label)}${g.unit?` · Unit ${g.unit}`:''}</a>${parts.map(q=>`<a href="${esc(location.pathname)}#${esc(q.id)}">${esc(q.number)} · ${esc(bank.answers[q.answer].title)}</a>`).join('')}</section>`);
    }
   }else{
    intro.innerHTML=`<h2>Revision questions</h2><p>${esc(bank.scope)}</p><p>Questions are grouped by topic; original question numbers and wording variants are in each answer’s source details.</p>`;
    for(const n of [3,4,5]){
     const qs=bank.questions.filter(q=>q.unit===n&&matches(q));if(!qs.length)continue;records.push(...qs);
     sections.push(`<section class="exam-group" id="revision-unit-${n}"><h3>Unit ${n} · ${esc({3:'Functions & recursion',4:'Structures & pointers',5:'Preprocessor & files'}[n])}</h3>${qs.map(item).join('')}</section>`);
     navSections.push(`<section><a class="exam-parent" href="${esc(location.pathname)}#revision-unit-${n}">Unit ${n}</a>${qs.map(q=>`<a href="${esc(location.pathname)}#${esc(q.id)}">${numbers.get(q.id)} · ${esc(q.title)} <small>(${esc(q.kind)})</small></a>${(q.question_parts||[]).map(part=>`<a class="exam-subpart-link" href="${esc(location.pathname)}#${esc(q.id+'-part-'+part.label.replace(/[^a-z0-9]/gi,''))}">${esc(part.label)} · ${esc(part.text.slice(0,60))}</a>`).join('')}`).join('')}</section>`);
    }
   }
   content.innerHTML=sections.join('')||'<p>No questions match. Clear the search or change the filters.</p>';nav.innerHTML=navSections.join('')||'<p>No matching questions.</p>';
   records.forEach(complete);ui.initAccordions(content);status.textContent=`${records.length} ${paper?'paper questions/subparts':'revision entries'} shown`;
   page.dataset.examReady='true';
  }
  function reveal(){
   let id;try{id=decodeURIComponent(location.hash.slice(1));}catch(_){return;}
   if(!id||id==='exam-top')return;
   const owner=bank.papers.find(p=>id===p.id||p.groups.some(g=>g.id===id||g.parts.some(q=>q.id===id)));
   const desired=owner?owner.id:'revision';if(collection.value!==desired||!document.getElementById(id)){collection.value=desired;unit.value='';kind.value='';search.value='';render();}
   const target=document.getElementById(id);if(target&&page.contains(target)){const answer=target.closest('details.study-accordion-item');if(answer)answer.open=true;target.scrollIntoView({block:'start'});nav.querySelectorAll('a').forEach(a=>a.toggleAttribute('aria-current',a.hash===location.hash));}
  }
  for(const control of [collection,unit,kind])control.addEventListener('change',render);
  search.addEventListener('input',render);
  page.querySelector('[data-exam-clear]').addEventListener('click',()=>{unit.value='';kind.value='';search.value='';render();});
  page.querySelectorAll('[data-exam-view]').forEach(button=>button.addEventListener('click',()=>{collection.value=button.dataset.examView==='revision'?'revision':bank.papers[0].id;unit.value='';kind.value='';search.value='';render();}));
  nav.addEventListener('click',e=>{if(e.target.closest('a')&&matchMedia('(max-width:700px)').matches)panel.open=false;});
  if(matchMedia('(max-width:700px)').matches)panel.open=false;
  window.addEventListener('hashchange',reveal);render();reveal();
 }catch(error){console.error(error);content.textContent='Questions could not be loaded. Reload to try again.';nav.textContent='Contents unavailable.';status.textContent='Loading failed.';}
});
})();

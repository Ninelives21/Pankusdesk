/* Source-backed paper Q&A. Shared study UI supplies the answer dropdowns. */
(function () {
    'use strict';
    document.addEventListener('DOMContentLoaded', async () => {
        const page = document.querySelector('[data-exam-prep]');
        if (!page) return;
        const ui = window.PankuStudyUI, esc = ui.escapeHtml;
        const content = page.querySelector('[data-exam-content]');
        const nav = page.querySelector('[data-exam-nav]');
        const panel = page.querySelector('[data-exam-contents]');
        try {
            const response = await fetch(new URL(page.dataset.examPrep, document.baseURI));
            if (!response.ok) throw new Error(`Question bank returned ${response.status}`);
            const bank = await response.json();
            const sources = new Map(bank.sources.map(source => [source.id, source]));
            const records = [];
            const aliases = new Map();
            const path = location.pathname + location.search;

            function item(question) {
                records.push(question);
                const answer = bank.answers[question.answer];
                const firstLine = question.question.split('\n')[0];
                const answerParts = question.answer_parts || (question.question_parts && question.answer === 'pointer-invalid'
                    ? answer.paragraphs.slice(0, 2).map((paragraph, index) => ({
                        label: index === 0 ? '(i) Pointer expression' : '(ii) Program behavior',
                        paragraphs: [paragraph, ...(index === 1 ? answer.paragraphs.slice(2) : [])]
                    })) : []);
                return ui.renderAccordionGroup({
                    label: 'Questions and answers', isExampleGroup: true,
                    items: [{
                        id: question.id,
                        title: `${question.number}. ${firstLine}${question.marks ? ` (${question.marks} marks)` : ''}`,
                        // A blank explicit question slot prevents answer text becoming closed-state text.
                        // It is used only for supplied code or labelled question subparts below.
                        question_paragraphs: [''],
                        paragraphs: answerParts.length ? [] : answer.paragraphs,
                        solution_parts: answerParts,
                        discrepancy: question.discrepancy ? { label: 'Source discrepancy', message: question.discrepancy } : null,
                        final_answer: question.answer === 'macro-output'
                            ? 'The printed macro expression evaluates to 41 (with a standard hosted entry point).'
                            : question.answer === 'pointer-invalid'
                                ? '(i) *(*(*(*(a+i)+j)+k)+l); (ii) undefined behavior; no portable output.' : undefined
                    }]
                });
            }

            function program(example) {
                return `<section class="exam-program"><h4>${esc(example.title)}</h4><p>${esc(example.note)}</p><pre><code class="language-c">${esc(example.code)}</code></pre><h5>Example input</h5><pre>${esc(example.input || '(No standard input; see the stated fixture or command.)')}</pre><h5>Expected result</h5><pre>${esc(example.expected || '(No console output; see the stated output files.)')}</pre></section>`;
            }

            function complete(question) {
                const node = document.getElementById(question.id);
                const answer = bank.answers[question.answer];
                const slot = node.querySelector('.study-example-question');
                if (question.question.includes('\n') && !question.question_parts) {
                    const pre = document.createElement('pre');
                    pre.textContent = question.question.split('\n').slice(1).join('\n');
                    slot.append(pre);
                }
                for (const part of question.question_parts || []) {
                    const block = document.createElement('span');
                    block.className = 'exam-question-part';
                    block.id = `${question.id}-part-${part.label.replace(/[^a-z0-9]/gi, '')}`;
                    block.textContent = `${part.label} ${part.text}`;
                    if (part.code) {
                        const pre = document.createElement('pre');
                        pre.textContent = part.code;
                        block.append(pre);
                    }
                    slot.append(block);
                }
                if (!slot.textContent.trim()) slot.remove();
                const body = node.querySelector('.study-example-solution');
                body.querySelector('.study-solution-label').textContent = 'Answer';
                const asksForProgram = /program|sample code|example|illustrat/i.test(question.question)
                    && !/pseudo\s*code/i.test(question.question);
                if (asksForProgram && answer.programs.length) {
                    body.insertAdjacentHTML('beforeend', answer.programs.map(id => program(bank.programs[id])).join(''));
                    const final = document.createElement('p');
                    final.className = 'study-final-answer';
                    const strong = document.createElement('strong');
                    strong.textContent = 'Final result: the examples produce the outputs/files shown above under their stated input limits.';
                    final.append(strong);
                    body.append(final);
                }
                const notePages = answer.note_refs.length
                    ? `; ${answer.basis.startsWith('priyanka') ? 'Priyanka images' : 'senior PDF pages'} ${answer.note_refs.join(', ')}` : '';
                const seniorPages = answer.senior_pages ? `; senior PDF pages ${answer.senior_pages.join(', ')}` : '';
                body.insertAdjacentHTML('beforeend', `<details class="exam-provenance"><summary>Source</summary><p>${esc(answer.authority)}. Basis: ${esc(answer.basis_label + notePages + seniorPages)}.</p><p>${esc(question.source_label)}</p></details>`);
            }

            const sections = [], paperLinks = [], revisionLinks = [];
            for (const paper of bank.papers) {
                paperLinks.push(`<a href="${esc(path)}#${esc(paper.id)}">${esc(paper.title)} · ${esc(paper.regulation)}</a>`);
                const sourceLabel = paper.sources.map(id => `${sources.get(id).filename}, p. ${paper.source_pages[id].join(', ')}`).join('; ');
                const groups = paper.groups.map(group => {
                    const heading = group.unit
                        ? (!group.or_before ? `<h3>Part B · Unit ${group.unit}</h3>` : '')
                        : '<h3>Part A</h3>';
                    return `${group.or_before ? '<p class="exam-or">OR</p>' : ''}<section class="exam-group" id="${esc(group.id)}">${heading}${group.parts.map(part => item({ ...part, source_label: sourceLabel })).join('')}</section>`;
                }).join('');
                sections.push(`<section class="exam-paper" id="${esc(paper.id)}"><h2>${esc(paper.title)}</h2><p>${esc(paper.regulation)} · ${esc(paper.subject_code)} · ${paper.minutes} minutes · ${paper.max_marks} marks</p><ul>${paper.instructions.map(instruction => `<li>${esc(instruction)}</li>`).join('')}</ul>${groups}</section>`);
            }

            // Restore every original source question, rather than using topic-level merged entries.
            // Internal canonical IDs remain aliases so previously shared links still work.
            for (const source of bank.sources) {
                const occurrences = bank.occurrences.filter(item => item.source === source.id);
                if (!occurrences.length) continue;
                revisionLinks.push(`<a href="${esc(path)}#${esc(source.id)}">${esc(source.label)}</a>`);
                let previousGroup = '';
                const questions = occurrences.map(occurrence => {
                    const canonical = bank.questions.find(question => question.occurrences.includes(occurrence.id));
                    if (canonical && !aliases.has(canonical.id)) aliases.set(canonical.id, occurrence.id);
                    if (!aliases.has(`revision-unit-${occurrence.unit}`)) aliases.set(`revision-unit-${occurrence.unit}`, occurrence.id);
                    const question = {
                        ...occurrence,
                        source_label: `${source.label} · p. ${occurrence.page} · ${occurrence.section} Q${occurrence.number}`
                    };
                    // Retain structural subparts for the two compound source questions.
                    if (canonical?.question_parts && (occurrence.answer === 'pointer-invalid' || /^Explain the following statement/i.test(occurrence.question))) {
                        question.question = canonical.question;
                        question.question_parts = canonical.question_parts;
                        question.answer_parts = canonical.answer_parts;
                        question.discrepancy = canonical.discrepancy;
                    }
                    const key = `${occurrence.unit}-${occurrence.section}`;
                    const heading = key !== previousGroup
                        ? `<h3>Unit ${occurrence.unit} · ${occurrence.section === 'short' ? 'Short questions' : 'Long questions'}</h3>` : '';
                    previousGroup = key;
                    return heading + item(question);
                }).join('');
                sections.push(`<section class="exam-paper" id="${esc(source.id)}"><h2>${esc(source.label)}</h2>${questions}</section>`);
            }
            content.innerHTML = sections.join('');
            nav.innerHTML = `<h3>Past papers</h3>${paperLinks.join('')}<h3>Revision sets</h3>${revisionLinks.join('')}`;
            records.forEach(complete);
            ui.initAccordions(content);

            function reveal() {
                let id;
                try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
                if (!id || id === 'exam-top') return;
                // Preserve old revision and compound-subpart links without displaying topic headings.
                for (const [from, to] of aliases) {
                    if (id === from || id.startsWith(`${from}-part-`)) {
                        id = to + id.slice(from.length);
                        break;
                    }
                }
                const target = document.getElementById(id);
                if (!target || !content.contains(target)) return;
                const answer = target.closest('details.study-accordion-item');
                if (answer) answer.open = true;
                target.scrollIntoView({ block: 'start' });
                const paper = target.closest('.exam-paper');
                nav.querySelectorAll('a').forEach(link => {
                    if (link.hash === `#${paper?.id}`) link.setAttribute('aria-current', 'location');
                    else link.removeAttribute('aria-current');
                });
            }
            if (matchMedia('(max-width:700px)').matches) panel.open = false;
            nav.addEventListener('click', event => {
                const link = event.target.closest('a');
                if (!link) return;
                if (matchMedia('(max-width:700px)').matches) panel.open = false;
                if (link.hash === location.hash) reveal();
            });
            window.addEventListener('hashchange', reveal);
            page.dataset.examReady = 'true';
            reveal();
        } catch (error) {
            console.error(error);
            content.textContent = 'Questions could not be loaded. Reload to try again.';
            nav.textContent = 'Papers unavailable.';
        }
    });
})();

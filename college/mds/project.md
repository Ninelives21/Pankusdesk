# PankusDesk — Master Project Instructions

## 1. Purpose and governing principle

PankusDesk is Priyanka's study portal for VNR VJIET R25 coursework.

These instructions apply globally across all PankusDesk subjects, including BEE, Matrices & Calculus (MAC), Engineering Chemistry, and future subjects.

The goal is to build accurate, textbook-faithful, class-note-integrated study material while maintaining one consistent PankusDesk architecture and user experience.

Do not redesign established patterns independently for different subjects. Once a convention has been established globally, reuse it unless explicitly instructed otherwise.

Accuracy and source fidelity are more important than adding content or making material look complete.

**Never hallucinate.** If something is missing, unclear, illegible, contradictory, or unavailable in the supplied sources, identify the uncertainty rather than inventing the missing content.

---

# 2. Source hierarchy

Use the following hierarchy when deciding what belongs in PankusDesk.

## 2.1 R25 syllabus controls scope

The current VNR VJIET R25 syllabus is authoritative for:

- what topics belong in a unit;
- what is out of scope;
- which topics must ultimately be covered.

Do not include textbook material merely because it appears in the prescribed book if it falls outside the R25 scope.

## 2.2 Prescribed textbook controls the main teaching content

For topics that are within R25 scope, the prescribed textbook is the authoritative source for:

- teaching sequence;
- definitions;
- explanations;
- notation;
- equations;
- derivations;
- worked examples;
- example numbering;
- textbook questions;
- printed answers where supplied.

The textbook portion of PankusDesk should essentially reproduce the relevant textbook material, filtered through the R25 syllabus.

Minor correction of grammar, awkward English and obvious typographical errors is allowed.

Do not unnecessarily paraphrase, summarise or simplify away textbook detail.

Do not add student-facing commentary such as:

- “the textbook says”
- “according to the textbook”
- “the author now explains”
- descriptions of our extraction process or source mapping.

Source provenance belongs in the backend/provenance system, not in the student's study prose.

## 2.3 Class material supplements the textbook

Priyanka's class notes and lecture material are an additional source.

They do not replace the textbook.

Class material should be integrated at the corresponding concept where useful while retaining its identity as class material.

Never silently convert class-note material into textbook material.

---

# 3. Canonical unit architecture

The established PankusDesk unit structure is:

1. **Text**
2. **Textbook Questions**
3. **Priyanka's Class Notes**

This is the global unit-page pattern unless explicitly changed.

Each unit should therefore have separate student-facing destinations for:

### Text

The cumulative textbook-faithful study material for that unit.

### Textbook Questions

Relevant textbook exercise questions, chapter-end questions and associated solutions/answers.

### Priyanka's Class Notes

Dated class-note material and access to the class-note history/calendar.

These three links should appear consistently at the top of relevant unit pages.

If a destination has not yet been built, retain the navigation item using the established dummy-link convention rather than deleting the link.

---

# 4. Cumulative theory pages

The main Text page is cumulative.

New class material should not result in duplicated versions of the same theory being appended endlessly.

Instead:

1. locate the correct existing textbook/topic section;
2. integrate genuinely useful additional explanation there;
3. maintain one coherent cumulative treatment of the topic;
4. retain provenance internally.

Avoid duplicated theory.

The canonical reference implementation for future unit construction is the established PankusDesk Unit I architecture and workflow. Reuse its patterns rather than inventing a different implementation per unit or subject.

---

# 5. Textbook examples

Every worked textbook example must be complete.

Do not provide only the answer or skip intermediate reasoning.

Worked examples should use the established expandable Q&A/dropdown presentation.

Inside a solution, show all meaningful steps, including where applicable:

- row operations;
- algebra;
- substitutions;
- equations;
- iterations;
- intermediate matrices;
- transformations;
- calculations;
- final result.

The student should be able to learn the method from the solution without reconstructing missing steps herself.

Final answers should be clearly identifiable.

Printed textbook answers should be preserved when available.

---

# 6. Class-note integration

Priyanka's class notes require special handling.

## 6.1 Preserve dated source history

Class notes must retain their date and source identity.

Maintain the established chain:

**class material → dated class-note entry/log → calendar → cumulative unit material**

The dated notes must remain accessible even after useful content is integrated into cumulative theory.

Do not destroy the historical class-note record merely because material has been incorporated elsewhere.

## 6.2 Compare class questions with the textbook first

Before independently solving any question or worked example from Priyanka's class notes:

1. compare it against the prescribed textbook's worked examples;
2. compare it against section-end questions;
3. compare it against chapter-end/textbook questions.

If it is an **exact textbook match**:

- retain the class-note entry;
- identify that it corresponds to the textbook problem;
- link to a stable anchor on the canonical Text or Textbook Questions page;
- do not create a second duplicate worked solution.

If it is only a **near-match**, treat it as a separate question and clearly preserve the distinction.

Never assume two questions match merely because they look similar.

## 6.3 Class-note labels

Class-derived material must remain identifiable as class material using the established visual/source conventions.

Do not blur textbook and class provenance.

---

# 7. NRS — Notebook Redraw Standard

Use the established NRS style for redrawing Priyanka's handwritten class notes and lecture diagrams.

NRS means:

- clean white ruled notebook-paper background;
- faint blue horizontal ruling;
- subtle pink/red notebook margin where appropriate;
- blue-ink handwritten-style text and diagram lines;
- compact, space-efficient layout;
- clean alignment;
- faithful reproduction of the original meaning;
- no unnecessary decorative additions;
- no added theory that is absent from the source.

The objective is **a clean version of Priyanka's notebook**, not a generic textbook illustration.

Technical fidelity takes priority over visual prettiness.

## NRS workflow

Before producing a redraw:

1. inspect and understand the source;
2. determine what every symbol, number, arrow, terminal, branch and label represents;
3. compare with relevant theory/textbook where necessary;
4. resolve semantic uncertainty before redrawing;
5. generate/redraw;
6. visually audit the result against the original.

Do not “fix” a class-note circuit or diagram simply because it appears unusual unless there is evidence that it is wrong.

If a correction is necessary, distinguish between:

- what Priyanka wrote;
- what is technically correct;
- what has been corrected in PankusDesk.

Never invent missing voltages, resistor values, arrows, equations or labels merely to make a diagram look complete.

For embedded images, use meaningful descriptive `alt` text based on the electrical/mathematical/technical content. Do not use merely the filename, figure number, or generic text such as “image”.

---

# 8. Figures and textbook images

Textbook figures should appear at the correct conceptual location rather than being collected separately without context.

Use explicit anchors/placement rules so that figures remain attached to the appropriate discussion.

Where a textbook figure has not yet been supplied or prepared, use the established figure placeholder convention containing sufficient identification, such as:

- figure number;
- figure name/description;
- textbook page number.

Do not fabricate the missing figure.

Tables should be constructed as proper HTML `<table>` content where appropriate rather than rendered as inaccessible screenshots.

---

# 9. Mathematics and LaTeX

Mathematical correctness and rendering quality are global requirements.

Use LaTeX/MathJax for mathematical notation rather than plain-text approximations where formatted mathematics is appropriate.

Use proper display formatting for working that should appear line-by-line.

Do not cram multi-step calculations onto a single line merely to save space.

For fractions, use the established `\dfrac` convention where appropriate.

### Critical escaping rule

Never emit malformed LaTeX or MathJax escaping.

When mathematics appears inside JSON, JavaScript or another escaped string format, ensure the stored string produces the correct LaTeX after parsing.

In particular:

- matrix row separators must render as `\\`;
- commands must not become accidental JavaScript/JSON escape sequences;
- no stray single backslashes;
- no hidden control characters generated by bad escaping.

Before packaging a delta, scan generated mathematical strings for malformed escaping/control characters.

A page that contains mathematically correct source text but broken rendered LaTeX is not considered complete.

---

# 10. SIMPLER sections

SIMPLER boxes are a global PankusDesk teaching feature.

Their purpose is to explain a concept in intuitive language after the formal treatment.

A SIMPLER section should:

- preserve technical correctness;
- assume the student may return later with little context;
- explain the conceptual “why”;
- connect terminology to something understandable;
- be concise enough to reread quickly;
- retain enough detail to reconstruct understanding.

It should not simply repeat a definition in fewer words.

It should not replace the formal textbook explanation.

Place SIMPLER sections at the conceptually useful point established for that topic, normally after formal explanation and before subsequent worked/practice material where appropriate.

---

# 11. Navigation and UI consistency

PankusDesk is one system, not a collection of unrelated subject websites.

Global UI behaviour must remain consistent across subjects.

Reuse shared generic renderers, styles and components wherever possible.

Do not create subject-specific implementations when the existing generic mechanism can support the requirement.

Preserve established behaviour for:

- left navigation;
- unit/topic navigation;
- accordions;
- textbook questions;
- class-note access;
- calendar/log navigation;
- Quick Recall;
- Check Yourself;
- practice links;
- top-of-unit links;
- Back-to-top behaviour;
- typography and spacing.

Topic navigation should link to valid local anchors within the relevant unit/page.

Avoid unnecessary vertical scrollbars inside normal content components.

The main page should perform normal document scrolling unless a component specifically requires otherwise.

---

# 12. Provenance

PankusDesk must preserve where content came from even when the provenance is not shown prominently to the student.

Use the established manifests/indexes/source-reference mechanism rather than inserting editorial source commentary into study text.

Relevant provenance categories include:

- prescribed textbook;
- textbook page/section;
- Priyanka's dated class notes;
- lecture material;
- PankusDesk explanatory addition;
- verified correction.

Never label an assistant-generated explanation as textbook content.

---

# 13. Discrepancies and corrections

If a supplied class note, textbook image, printed answer or existing PankusDesk implementation appears inconsistent:

1. investigate before altering it;
2. compare against authoritative available sources;
3. distinguish definite errors from suspected errors;
4. do not silently rewrite uncertain source material.

Verified mismatches/corrections should use the established PankusDesk visual convention, including amber highlighting where that convention is applicable.

Do not conceal the existence of a meaningful discrepancy.

---

# 14. Source-of-truth rule for code work

For implementation work, the **latest workspace supplied by the user in that task is the code source of truth**.

Do not reconstruct the site from memory when the current workspace is available.

Do not use an older ZIP/delta/workspace as the base merely because it contains a familiar implementation.

Never overwrite cumulative improvements from a newer workspace with stale files from an earlier copy.

Before editing:

1. identify the latest workspace;
2. inspect the relevant current files;
3. understand the existing architecture;
4. make the smallest coherent change required;
5. preserve unrelated improvements.

Conversation memory tells you **why things were designed a certain way**.

The latest workspace tells you **what the code actually is now**.

When the two disagree, inspect the current workspace rather than blindly imposing remembered implementation details.

---

# 15. Build workflow

For substantial unit/build work, follow this general sequence:

1. Read the current design/architecture rules.
2. Inspect the latest workspace.
3. Lock the source material.
4. Map the R25 syllabus.
5. Determine the corresponding prescribed-textbook content and sequence.
6. Build cumulative textbook-faithful topics.
7. Build complete worked examples.
8. Integrate verified class material at the appropriate concepts.
9. Process/redraw class-note visuals using NRS only after semantic verification.
10. Place textbook figures/tables at explicit appropriate locations.
11. Add SIMPLER explanations or other clearly identified PankusDesk teaching aids where requested.
12. Build the Textbook Questions layer.
13. Maintain dated class logs/calendar links.
14. Audit LaTeX/MathJax.
15. Check navigation/anchors.
16. Run visual/content/subject/generic verification appropriate to the change.
17. Only consider a page/unit complete when those checks pass.

Do not mark content as ready merely because files were generated.

Where the project uses a `publicationStatus` or equivalent readiness flag, set it to `ready` only after required completion checks have actually passed.

---

# 16. Handoff and delta rules

When the user asks for a PankusDesk “handoff”, provide a genuine usable handoff rather than merely describing intended changes.

A handoff should identify:

- the source workspace used;
- what was changed;
- files added/modified where relevant;
- important decisions/corrections;
- verification actually performed;
- anything genuinely unresolved.

Do not claim to have tested something that was not tested.

When producing a delta ZIP:

- create a real valid ZIP;
- it should contain exactly one appropriate top-level delta folder;
- verify/test-unzip it;
- ensure required JSON/JS/KB/college assets/provenance files are present as applicable;
- verify generated mathematical content for broken escaping;
- do not package unrelated stale files.

---

# 17. rsync convention

When giving rsync commands for a delta, assume the unzipped delta folder is beside `Pankusdesk/`.

Always give the dry run and real sync as **separate copy-paste commands**.

Dry run:

`rsync -avhn <delta>/ Pankusdesk/`

Real sync:

`rsync -avh <delta>/ Pankusdesk/`

Do not use placeholder paths such as `/path/to/...`.

Do not add `--delete` unless the user explicitly requests deletion behaviour.

Never combine the dry-run and real command into one command line or one chained command.

---

# 18. Subject-specific rules

## BEE

Use the confirmed VNR VJIET R25 BEE syllabus as the scope authority.

The prescribed textbook is V. Ramesh Babu.

Preserve established BEE Unit I architecture as a key reference implementation for subsequent BEE units.

Electrical diagrams must be technically verified before redraw.

Circuit arrows, polarities, resistor values, terminal labels and source values must not be guessed.

## Matrices & Calculus (MAC)

R25 determines syllabus scope.

The prescribed textbook/Grewal sequence determines the teaching order for in-scope material.

Examples must retain complete mathematical working.

Matrix operations, row operations, substitutions and iteration steps must not be compressed into unexplained jumps.

Preserve the established separation between textbook content, textbook questions and Priyanka's class notes.

## Engineering Chemistry

Follow the R25 syllabus and mapped prescribed textbook content.

Preserve textbook content closely while correcting only awkward grammar, obvious language issues and typographical mistakes.

Use proper HTML tables for tabular content.

Use LaTeX for formulae/equations.

Where textbook figures have not yet been provided, use explicit placeholders containing figure number/name/page rather than inventing images.

Apply the same three-page unit architecture and global PankusDesk UI conventions.

---

# 19. What NOT to do

Do not:

- invent missing theory;
- invent textbook wording;
- invent page references;
- invent questions;
- invent answers;
- invent figures;
- invent values or labels in diagrams;
- invent class-note content;
- fabricate source provenance;
- silently change questionable source material without verification;
- duplicate textbook solutions unnecessarily in class notes;
- collapse detailed worked examples into final answers;
- create a new UI pattern merely because a new subject is being built;
- overwrite newer workspace content with an older copy;
- claim verification that was not performed;
- expose backend editorial/source commentary as student-facing prose;
- allow malformed LaTeX/MathJax to ship.

When uncertain, preserve the source faithfully and identify the uncertainty.

---

# 20. Context and memory behaviour

Use previous chats within the PankusDesk Project as historical context for:

- prior decisions;
- corrections;
- design choices;
- terminology;
- established patterns;
- why an implementation was changed.

Do not assume that an old chat represents the latest state of the code.

For code changes, the latest workspace supplied in the current task remains authoritative.

When a new PankusDesk chat begins, first recover relevant project context rather than asking the user to repeat established PankusDesk rules that are already available in the Project.

If a user refers to an earlier PankusDesk decision, class-note correction, implementation convention or handoff, retrieve the relevant project history before guessing.

---

# 21. Governing principle

When there is tension between completeness and certainty:

**Choose certainty.**

When there is tension between redesigning and preserving an established global convention:

**Preserve the established convention.**

When there is tension between remembered implementation state and the latest workspace:

**Use the latest workspace.**

When adding content:

**R25 decides scope.
The prescribed textbook supplies the canonical teaching material and sequence.
Class notes supplement it.
PankusDesk additions must remain identifiable as additions.**

The result should be accurate enough that Priyanka can rely on PankusDesk as her primary study interface without unknowingly studying assistant-invented material.

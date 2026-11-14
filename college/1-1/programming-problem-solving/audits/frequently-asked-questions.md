# Frequently Asked Questions — supplied Claude file snapshot

## Scope and source lock

The PPS index gains a separate **Frequently Asked Questions** card and HTML page. This snapshots the current supplied `pps_claude_unit3,4.zip` member `PPS_Unit3_SecondHalf_Unit4_QA.pdf` (20 pages), captured 14 November 2026. SHA256: `f8099c249ecc5333b68e59c51203579874d84d493b103ee3ce86059b7b41967c`.

All 31 numbered body questions are included once, with exact source wording, original A/Q numbering, order, starting page and answer continuation-page references. The duplicated contents on pages 1–2 do not create additional questions. All eight final topic rows on page 20 are also included, separately labelled T1–T8 for navigation; these labels are authored and are not source question numbers. There are 39 answer dropdowns total.

This is a question-complete FAQ with authored answers, not a verbatim republication of the PDF. Source front matter, unverified paper claims, original filename, checksum, source locators and snapshot/update policy are metadata. The page identifies the answer policy and fixed snapshot. A future version of the live file requires a deliberate source comparison/update; the page does not fetch a changing external file. Existing anchors should remain stable on subsequent updates.

No PDF, notebook photographs or figure assets are added. Only small text/JSON assets are published (FAQ data approximately 104 KB); the supplied PDF remains intake material. The source pages contain prose, tables and code, not technical figures requiring redraws. No unit publication states change. Mid-II and Worksheet & Solutions 1 remain intact.

## Coverage

| Source block | Original labels | Body pages | Dropdowns |
| --- | --- | --- | --- |
| Unit III, Part A | A1–A7 | 3–4 | 7 |
| Unit III, Part B | Q1–Q11 | 4–13 | 11 |
| Unit IV, Part A | A1–A5 | 14 | 5 |
| Unit IV, Part B | Q1–Q8 | 14–20 | 8 |
| Final topic list | Eight unnumbered source rows | 20 | 8 |

Unit III includes function types, actual/formal parameters, syntax, recursion, advantages, libraries, auto/register, declaration/call/definition, four categories, value/address arguments, recursive factorial/Fibonacci/natural-number sum/Ackermann, storage classes, scope/lifetime and array parameters.

Unit IV includes declarations, pointers, arrow access, union tradeoffs, typedef, student details, structure/union allocation, variable student/subject counts, nested birthdays, structure pointers, structure value/address parameters and indirection.

Final rows: allocation functions; reading/printing arrays through pointers and arrays versus pointers; bit-fields; self-referential structures; arrays of pointers; pointers to strings; sizeof a structure; initialization at declaration. The full prompt variants and source examples are covered by explanations and 29 standalone authored C11 examples. Explicit source examples include four function categories with sums/factorials, value/pointer swap, recursion traces, auto/static/extern/register demonstrations, array elements/search/sort, string libraries, two student records, per-student means, birthdays, complex addition and pointer-based display. Additional gap-topic code is identified as an authored completion. Stated bounds, fixed-input adaptations and marks assumptions are explicit in each program note.

## Answer authority and source discrepancies

The user's answer priority applies: **Priyanka → senior → general PPS knowledge for gaps**. This overrides the attachment's instruction to use only the senior notebook. The compilation supplies questions, not verified historical-paper identity or solution authority. Its “Asked in” text is retained as `supplied_provenance_claim`, not promoted to verified PYQs, dates, marks or frequency statistics. In particular, its “8 of 9 papers” assertion is not displayed as evidence.

Answers carry notes/image locators and PankusDesk-authored attribution. Priyanka supplies functions, pointer/value arguments, array parameter/search/sort methods, structures, structure parameters, pointer arithmetic and self-reference. Senior notes supplement storage, scope, unions, nested structures, recursive sum, Ackermann and typedef detail. Priyanka image 83 explicitly covers recursive Fibonacci and is now correctly the primary citation for that answer. General knowledge fills allocation, bit-fields, string pointers, structure-size/initialization detail and standards clarifications; these are labelled in provenance. The final topic list's “not covered” claim is superseded where Priyanka supplies the subject (notably self-reference and pointer arithmetic).

The source-review findings below remain in audit metadata. The FAQ prompts contain no erroneous supplied numerical givens or printed code requiring correction. The previous page attached warning badges to our independently authored answers simply because they differed from the supplied compilation’s answers. Those badges and repeated source-comparison paragraphs are removed from the study flow. Correct C11 facts are taught directly; verified discrepancies in actual question givens would still use the shared amber treatment.

Review findings:

- `void main`, conio/clrscr/getch and unspecified no-parameter prototypes are replaced in authored programs by hosted standard C11; the page identifies the modernization. The four category panels explain that every function has a return type.
- gets is removed in C11; strrev/strlwr/strupr are not ISO C functions. strlen returns size_t, requiring %zu.
- register does not guarantee hardware-register placement; C11 itself forbids taking the address of a register object. No uninitialized-int “garbage output” example is executed.
- All arguments, including pointers, pass by value. Object pointers must be printed with %p and (void*) rather than %d or an invented address 100.
- Recursive factorial includes the 0! case and a representable bound. Naive recursion is not guaranteed to optimize performance.
- Structure/union sizes can include alignment padding. typedef is an alias, not a distinct type created by the typedef declaration.

These are recorded corrections/clarifications to the supplied answer material; original question wording is unchanged. The existing Mid-II JSON is not modified.

## Shared presentation contract

The existing exam-preparation renderer gains optional `sections` containing question records. The FAQ uses that path; the existing Mid-II paper/occurrence path remains unchanged. The FAQ uses the existing shared study accordions, code styling, mobile contents and Back to top. Navigation lists section headings and every question number with a short description; selecting a question opens its answer. Compound explanations use separate shared solution-part panels. Main examples address the question directly. Additional pre-existing variants are retained under a closed “More worked examples” disclosure; they no longer crowd the main answer. Standard snippets, lists and semantic tables use ordered answer blocks in the shared study UI. Each substantive subpart remains a separate shared solution panel. Answer and program data are stored in the FAQ snapshot itself so future Mid-II edits cannot silently alter it.

## Validation

- `python3 scripts/tools/verify_pps_faq.py --source-text <local supplied text>`: PASS. All 31 complete question wordings, labels, order and starting pages match the source; 8 final topics, anchors, references and index card checked. All 29 programs compile warning-free using `-std=c11 -Wall -Wextra -Werror -pedantic`, and sample outputs plus selected valid/invalid boundary cases match.
- `python3 scripts/tools/verify_pps_mid2.py`: PASS, including all 26 existing Mid-II program samples.
- `python3 scripts/tools/verify_college.py`: PASS.
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`: PASS.
- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`: PASS.
- `node --check scripts/new/exam-prep.js`, Python syntax, JSON parse and `git diff --check`: PASS.
- Local Chromium at 1440 px and 390 px: FAQ card, all 39 dropdowns, section/question links, answer reveal, numbered advantages, syntax snippets, comparison tables, C examples, optional extra examples, subpart panels, phone navigation collapse/Back to top, original Mid-II behavior and GitHub Pages `/Pankusdesk/` routes checked. Desktop/phone screenshots reviewed. No page errors or horizontal document overflow.

The PR handoff provides its exact preview commit, deployment status and unchecked user acceptance steps. No automatic merge.

## Detailed answer review — 14 November 2026

All 39 answers were rewritten after reading the relevant ingested records in the Priyanka and senior knowledge bases. Definitions come first; advantages and procedures use numbered points with bold labels; comparisons use actual HTML tables; syntax uses readable code blocks; numerical recursion answers show the call/return steps and a distinct final result. Ordinary answers contain no critique of the source file, unrequested optimisation discussion or repeated warning boxes. Source information remains in a closed disclosure.

The five advantages in A5 are an authored exam-answer expansion of the functions/task-organization material, not a verbatim five-item list in Priyanka images 70–72. The ingested topic records support the concepts and are recorded below. This distinction corrects the earlier chat handoff’s overly broad attribution. The Fibonacci citation is corrected from senior-only to Priyanka image 83. Structure sizeof uses Priyanka’s sizeof material plus explicitly identified general structure-padding detail. Structure initialization remains general supplementation because the ingested declaration/input material does not directly supply that explanation.

Program review: all 26 existing examples remain available. Addition now illustrates the main four-category explanation following Priyanka’s input/output responsibilities; the original sum/factorial variant is retained as extra practice. Two focused examples (scope/static lifetime and pointer indirection) replace unrelated code in their respective main answers. There are 29 tested program records in total. Unused common includes were removed from displayed examples; necessary headers remain. Main program notes state only useful input limits and operation details, without source-management prose.

| FAQ | Primary ingested record(s) / gap basis |
| --- | --- |
| faq-u3-a1 | `pri-functions-core` |
| faq-u3-a2 | `pri-functions-core` |
| faq-u3-a3 | `pri-functions-core` |
| faq-u3-a4 | `pri-recursive-fibonacci`, `recursion-fundamentals` |
| faq-u3-a5 | `pri-program-organization`, `pri-functions-core` |
| faq-u3-a6 | `pri-basic-io`, `pri-string-library-portability` |
| faq-u3-a7 | `storage-classes-overview`, `storage-classes-examples` |
| faq-u3-q1 | `pri-functions-core`, `pri-factorial-four-categories` |
| faq-u3-q2 | `pri-function-four-categories` |
| faq-u3-q3 | `pri-pointer-arguments`, `pri-swap-value-pointer` |
| faq-u3-q4 | `pri-recursive-fibonacci`, `recursive-sum-factorial-fibonacci` |
| faq-u3-q5 | `pri-recursive-fibonacci` |
| faq-u3-q6 | `recursive-sum-factorial-fibonacci` |
| faq-u3-q7 | `ackermann-recursion` |
| faq-u3-q8 | `storage-classes-overview`, `storage-classes-examples` |
| faq-u3-q9 | `storage-classes-overview`, `storage-classes-examples` |
| faq-u3-q10 | `pri-array-element-function`, `pri-array-search-sort-functions` |
| faq-u3-q11 | `pri-basic-io`, `pri-string-library-portability`, `pri-string-copy-methods`, `pri-string-concat-compare-reverse` |
| faq-u4-a1 | `pri-structure-introduction`, `pri-structure-objects-members` |
| faq-u4-a2 | `pri-pointer-arguments` |
| faq-u4-a3 | `pri-structure-pointer-access` |
| faq-u4-a4 | `unions-shared-storage` |
| faq-u4-a5 | `pri-structures-function-values`, `typedef-enum` |
| faq-u4-q1 | `pri-structure-objects-members` |
| faq-u4-q2 | `unions-shared-storage` |
| faq-u4-q3 | `pri-student-structure-averages` |
| faq-u4-q4 | `nested-student-structure` |
| faq-u4-q5 | `pri-structure-pointer-access`, `pri-structures-function-values` |
| faq-u4-q6 | `pri-structures-function-values` |
| faq-u4-q7 | `pri-pointer-arguments` |
| faq-u4-q8 | `pri-structures-function-values`, `typedef-enum` |
| faq-extra-1 | General PPS knowledge; no direct supplied-note coverage |
| faq-extra-2 | `pri-pointer-arithmetic-array-sum` |
| faq-extra-3 | General PPS knowledge; no direct supplied-note coverage |
| faq-extra-4 | `pri-self-referential-structure` |
| faq-extra-5 | General PPS knowledge; no direct supplied-note coverage |
| faq-extra-6 | General PPS knowledge; no direct supplied-note coverage |
| faq-extra-7 | `pri-sizeof-conversions` |
| faq-extra-8 | `pri-structure-objects-members` |

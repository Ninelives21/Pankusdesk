# Frequently Asked Questions — supplied Claude file snapshot

## Scope and source lock

The PPS index gains a separate **Frequently Asked Questions** card and HTML page. This snapshots the current supplied `pps_claude_unit3,4.zip` member `PPS_Unit3_SecondHalf_Unit4_QA.pdf` (20 pages), captured 14 November 2026. SHA256: `f8099c249ecc5333b68e59c51203579874d84d493b103ee3ce86059b7b41967c`.

All 31 numbered body questions are included once, with exact source wording, original A/Q numbering, order, starting page and answer continuation-page references. The duplicated contents on pages 1–2 do not create additional questions. All eight final topic rows on page 20 are also included, separately labelled T1–T8 for navigation; these labels are authored and are not source question numbers. There are 39 answer dropdowns total.

This is a question-complete FAQ with authored answers, not a verbatim republication of the PDF. Source front matter, unverified paper claims, original filename, checksum, source locators and snapshot/update policy are metadata. The page identifies the answer policy and fixed snapshot. A future version of the live file requires a deliberate source comparison/update; the page does not fetch a changing external file. Existing anchors should remain stable on subsequent updates.

No PDF, notebook photographs or figure assets are added. Only small text/JSON assets are published (FAQ data approximately 89 KB); the supplied PDF remains intake material. The source pages contain prose, tables and code, not technical figures requiring redraws. No unit publication states change. Mid-II and Worksheet & Solutions 1 remain intact.

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

Final rows: allocation functions; reading/printing arrays through pointers and arrays versus pointers; bit-fields; self-referential structures; arrays of pointers; pointers to strings; sizeof a structure; initialization at declaration. The full prompt variants and source examples are covered by explanations and 26 standalone authored C11 examples. Explicit source examples include four function categories with sums/factorials, value/pointer swap, recursion traces, auto/static/extern/register demonstrations, array elements/search/sort, string libraries, two student records, per-student means, birthdays, complex addition and pointer-based display. Additional gap-topic code is identified as an authored completion. Stated bounds, fixed-input adaptations and marks assumptions are explicit in each program note.

## Answer authority and source discrepancies

The user's answer priority applies: **Priyanka → senior → general PPS knowledge for gaps**. This overrides the attachment's instruction to use only the senior notebook. The compilation supplies questions, not verified historical-paper identity or solution authority. Its “Asked in” text is retained as `supplied_provenance_claim`, not promoted to verified PYQs, dates, marks or frequency statistics. In particular, its “8 of 9 papers” assertion is not displayed as evidence.

Answers carry notes/image locators and PankusDesk-authored attribution. Priyanka supplies functions, pointer/value arguments, array parameter/search/sort methods, structures, structure parameters, pointer arithmetic and self-reference. Senior notes supplement storage, scope, unions, nested structures, Fibonacci, recursive sum, Ackermann and typedef detail. General knowledge fills allocation, bit-fields, string pointers, structure-size/initialization detail and standards clarifications; these are labelled in provenance. The final topic list's “not covered” claim is superseded where Priyanka supplies the subject (notably self-reference and pointer arithmetic).

Meaningful source discrepancies use the shared amber treatment:

- `void main`, conio/clrscr/getch and unspecified no-parameter prototypes are replaced in authored programs by hosted standard C11; the page identifies the modernization. The four category panels explain that every function has a return type.
- gets is removed in C11; strrev/strlwr/strupr are not ISO C functions. strlen returns size_t, requiring %zu.
- register does not guarantee hardware-register placement; C11 itself forbids taking the address of a register object. No uninitialized-int “garbage output” example is executed.
- All arguments, including pointers, pass by value. Object pointers must be printed with %p and (void*) rather than %d or an invented address 100.
- Recursive factorial includes the 0! case and a representable bound. Naive recursion is not guaranteed to optimize performance.
- Structure/union sizes can include alignment padding. typedef is an alias, not a distinct type created by the typedef declaration.

These are explicit corrections/clarifications, not silent changes to original question wording. The existing Mid-II JSON is not modified.

## Shared presentation contract

The existing exam-preparation renderer gains optional `sections` containing question records. The FAQ uses that path; the existing Mid-II paper/occurrence path remains unchanged. The FAQ uses the existing shared study accordions, code styling, mobile contents and Back to top. Navigation lists section headings and every question number with a short description; selecting a question opens its answer. Compound explanations use separate shared solution-part panels. All selected example programs appear even when a question only says “explain”. Answer and program data are stored in the FAQ snapshot itself so future Mid-II edits cannot silently alter it.

## Validation

- `python3 scripts/tools/verify_pps_faq.py --source-text <local supplied text>`: PASS. All 31 complete question wordings, labels, order and starting pages match the source; 8 final topics, anchors, references and index card checked. All 26 programs compile warning-free using `-std=c11 -Wall -Wextra -Werror -pedantic`, and sample outputs plus selected valid/invalid boundary cases match.
- `python3 scripts/tools/verify_pps_mid2.py`: PASS, including all 26 existing Mid-II program samples.
- `python3 scripts/tools/verify_college.py`: PASS.
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`: PASS.
- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`: PASS.
- `node --check scripts/new/exam-prep.js`, Python syntax, JSON parse and `git diff --check`: PASS.
- Local Chromium at 1440 px and 390 px: FAQ card, all 39 dropdowns, section/question links, answer reveal, source discrepancy, C examples, subpart panels, phone navigation collapse/Back to top, original Mid-II behavior and GitHub Pages `/Pankusdesk/` routes checked. Desktop/phone screenshots reviewed. No page errors or horizontal document overflow.

The PR handoff provides its exact preview commit, deployment status and unchecked user acceptance steps. No automatic merge.

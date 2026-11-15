# Frequently Asked Questions — formatted supplied PDF

## Final scope

The PPS **Frequently Asked Questions** card opens a readable HTML transcription of the supplied `pps_claude_unit3,4.zip` member `PPS_Unit3_SecondHalf_Unit4_QA.pdf` (20 pages). Source snapshot captured 14 November 2026; formatting reviewed 15 November 2026. SHA256: `f8099c249ecc5333b68e59c51203579874d84d493b103ee3ce86059b7b41967c`.

The page publishes the **answers already in the PDF**, with their original explanations, examples, programs, sample outputs, tables and notes. It does not replace them with independently authored answers or knowledge-base summaries. The user's explicit instruction to format the supplied answers defines this page's publication scope; the Priyanka → senior → general answering policy remains relevant to independent PPS answers, not a reason to rewrite this source transcription.

There are 31 complete question/answer dropdowns. The final eight topics have no answers in the PDF and appear as the original eight-row table, not invented Q&A. All prior question and topic deep-link IDs are retained; T1–T8 are navigation labels only, not printed source question numbers. Back to top remains above the left navigation and outside the mobile contents disclosure.

The original introductory material, syllabus bullets and paper-short-form legend are available under “Original introduction (as supplied).” Paper labels, marks, frequency statements and teacher-note references are attributed source claims, not independently verified historical-paper metadata. Repeating page headers/footers and the duplicated printed contents are omitted; left navigation supplies the contents function.

## Source coverage

| Source block | Original labels | Body pages | Presentation |
| --- | --- | --- | --- |
| Unit III, Part A | A1–A7 | 3–4 | 7 source Q&A dropdowns |
| Unit III, Part B | Q1–Q11 | 4–13 | 11 source Q&A dropdowns |
| Unit IV, Part A | A1–A5 | 14 | 5 source Q&A dropdowns |
| Unit IV, Part B | Q1–Q8 | 14–20 | 8 source Q&A dropdowns |
| Final topic list | Eight unnumbered rows | 20 | Source table, with stable row anchors |

All source body text is retained, including the two section-end notices: the Unit III note about structured design/function signature and the Unit IV Part-A note about pointer arrays, self-reference and allocation. Statements about missing notes are faithfully attributed to this document, not assertions about the current ingested corpus.

Examples preserved include the source’s fact declaration/call/definition; four separate sum/factorial category programs; value and address swap; recursive factorial/Fibonacci/sum/Ackermann; auto/static/extern/register examples; scope/lifetime examples; individual elements, array search and bubble sort; string functions; two student records; structure/union memory tables; n-student averages; nested birthdays; structure pointers; complex addition; indirection and typedef.

For a concrete fidelity check, A5 contains the PDF’s three points — **Reusability, Optimisation, Reduces complexity** — rather than an expanded five-point authored answer. A3 contains the PDF’s `fact` syntax example. Source-supplied notes and corrections remain in their original positions.

## Formatting and code policy

- Paragraphs reflow naturally. Bold source emphasis and inline code are retained as escaped rich-text spans.
- Lists become HTML lists; comparisons, storage-class data and traces become semantic tables with column headers.
- Programs and sample outputs use separate preformatted blocks; physical page breaks inside a program are joined. Separate examples remain separate blocks. Source-labelled subparts use shared separated panels.
- Only obvious extraction-spacing defects are normalized: `defin ition`, `defin ed`, `diffe rent`, `fla g`, `flo at`, `afte r`. No numerical value, algorithm, example input or program logic is silently changed.
- Original code retains the PDF’s Turbo C conventions (`void main`, `clrscr`, `getch`, and legacy library examples) and deliberately invalid illustrations. The page identifies these as original source examples, not certified portable C11 programs. No new corrective essay or source-discrepancy badge is inserted into the answer flow.
- Earlier authored answers/programs are retained in the JSON's explicitly unrendered `authored_reference` for regression history. The existing 29 C11 example compilation/output/boundary tests still run against those reference records. **Those tests do not certify the displayed source code.**

No PDF binary, notebook photo or figure is published or redrawn. No unit publication state changes. Existing Mid-II and worksheet resources are preserved. Storage consists of a small HTML shell and a text JSON snapshot (under 400 KB including the unrendered reference records).

## Data and rendering

`exam-prep/frequently-asked-questions.json` uses `kind: source-transcription`. Each answer contains source blocks, original provenance text and a normalized text digest. The snapshot records filename, hash, page count, capture date and the manual-update policy. Future live-file updates require a source comparison rather than silently changing this snapshot.

The shared study UI renders ordered blocks, inline emphasis/code and stable table-row IDs. The shared exam adapter handles source intros, section-end notes and final topic navigation. Original answer blocks are the only content rendered inside the FAQ answers. Existing Mid-II rendering follows its prior data path.

## Validation

- `python3 scripts/tools/verify_pps_faq.py --source-text <supplied text>`: PASS. An independent text comparison checks **all 31 complete source answers**, including code, outputs, tables and unit-end notices, in addition to original question wording/numbers/order/start pages. Whitespace, list markers and the documented typography repairs are the only comparison normalizations. All answer text digests, block/table shapes, references and stable anchors are checked.
- The same verifier retains all 29 earlier authored-C11 compilation/sample/boundary tests; PASS with `-std=c11 -Wall -Wextra -Werror -pedantic`. Displayed source listings are not passed off as tested C11 examples.
- `python3 scripts/tools/verify_pps_mid2.py`: PASS, including its 26 C11 programs.
- `python3 scripts/tools/verify_college.py`: PASS.
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`: PASS.
- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`: PASS.
- JavaScript/Python syntax, JSON parsing and `git diff --check`: PASS.
- Local Chromium at 1440 px and 390 px checks every rendered answer's text against its complete source blocks. It checks 31 dropdowns, 44 navigation targets, original code and outputs, four category subparts, the final eight-row table, absence of authored replacement programs, phone collapse/Back to top and `/Pankusdesk/` routing. Desktop/phone screenshots inspected; no page errors or horizontal document overflow.

The PR description identifies the current preview commit/deployment status and leaves user acceptance checks unchecked. No automatic merge.

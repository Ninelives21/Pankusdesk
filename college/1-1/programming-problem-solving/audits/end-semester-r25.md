# End-Semester Papers — January 2026 R25

## Scope and verified paper

Adds an End-Semester Papers card and an HTML Q&A page for the latest supplied **Programming for Problem Solving** R25 end-semester paper: printed **January 2026**, subject **25ES1CS101**, 180 minutes, 60 marks. No exact exam day is printed, so none is invented.

Source: `vnt_pps_pyq/2025_PROGRAMMING FOR PROBLEM SOLVING.pdf`, SHA256 `1928b6abafcffcd0fa18fd88d570e6fc31847e888d54d6542c27981d7beba704`. Both pages were inspected; all questions are on page 1, while page 2 contains the closing marker only. The printed 2026 date takes precedence over the filename’s 2025. The other R25 file is **Problem Solving Through C, 25ES1DS101 (AE)** and is not silently mixed into this PPS paper. Older R22 papers remain intake material for later work.

All original question wording, order, numbers, unit grouping, marks and OR placement are retained. Nineteen questions/subparts have answers. Part A has five 2-mark questions; Part B requires one 10-mark alternative from each of five units, for a total attempted 60 marks. Both alternatives are answered for revision; summing every displayed alternative is not the exam’s maximum.

| Unit | First alternative | OR alternative | Attempted marks |
| --- | --- | --- | --- |
| I | 1(a) 5 + 1(b) 5 | 2: 10 | 10 |
| II | 3: 10 | 4: 10 | 10 |
| III | 5(a) 5 + 5(b) 5 | 6: 10 | 10 |
| IV | 7(a) 5 + 7(b) 5 | 8: 10 | 10 |
| V | 9(a) 5 + 9(b) 5 | 10: 10 | 10 |

The left navigation links to the paper, Part A/units and every question with a short description (26 links). Selecting a question opens its dropdown answer. Back to top sits above navigation and remains available with mobile contents collapsed. No filters or topic-based merged questions are introduced.

## Answer authority and depth

The strict order is **Priyanka’s ingested notes → senior KB → general PPS knowledge for missing coverage**. Each answer records real topic IDs and image/page references; gaps and authored applications are explicit in data, with provenance in a closed Source disclosure. Student-facing answers teach the subject directly, without source-comparison essays or unnecessary discrepancy badges.

Short answers give the required definition/syntax and a compact example where useful. Five-mark answers include explanation, procedure and a relevant example/program. Ten-mark answers supply the requested breadth, algorithms, worked traces, comparisons or full C programs. No invented official submark split is assigned to a multi-topic 10-mark question.

| Question | Primary evidence | Completion / application |
| --- | --- | --- |
| a | Priyanka 21–24, 33–34 | Nested-if and ladder syntax |
| b | Priyanka 63, 67–68 | Initialized three-word illustration of row-array strings |
| c | Priyanka 70–72 | General syntax, component explanations and sum example |
| d | No direct array-of-pointers coverage in either KB | General PPS; distinguished from row arrays and pointer-to-array syntax |
| e | No file API coverage in either KB | General PPS definitions of ferror, feof, clearerr, perror |
| 1(a) | Senior prime-test p47; Priyanka flowchart meanings 13–14 | Algorithm, text flowchart logic and prime/composite traces |
| 1(b) | Priyanka 37–39, 66–67 | Implicit/explicit conversions; accurate floating division and truncation |
| 2 | Priyanka 19–26, 33–34, 36–37 | Six branching forms with short worked C examples |
| 3 | Priyanka 42, 47–48, 50 | 1D/2D declaration, full/partial/inferred initialization and row-major access; source 3×3 initializer retained |
| 4 | Priyanka 27–32, 40–42 | while, do–while, for syntax and examples; correct 20-even-number sum 420 from the corrected ingested record |
| 5(a) | Priyanka 79–82 | Pointer swap updates original integers |
| 5(b) | Priyanka 72–74 | Four argument/return categories; no-argument variants read internally |
| 6 | Priyanka sorting context 64 and explicit prompt 66; senior overview p73 | Neither supplies a complete selection-sort implementation. General PPS fills algorithm, code, trace and complexity; selection is not replaced with bubble sort |
| 7(a), 7(b) | Priyanka 79–81 | Pointer declaration/initialization and focused indirection example |
| 8 | Priyanka 95–97 | Apply her value/pointer structure-passing methods to the paper’s time record; the exam-specific conversion is an authored application, not a claim that the notes contain that exact program |
| 9(a) | Priyanka 4–6, 40 | #include/#define and PI=3.14 are grounded in her notes; header search wording is standard-C clarification |
| 9(b) | No file API coverage | General PPS filename input and file display |
| 10 | Senior program-entry form pp3–4 | General PPS supplies file error APIs, positioning rules and argc/argv behaviour |

The concrete Q8 record contains hours, minutes and seconds and computes the actual requested total, rather than reusing a student/complex-number program as a substitute. Both value and pointer methods give 3723 seconds for 1:02:03.

## Code, examples and figures

Five complete program examples cover pointer swap, selection sort, pointer indirection, time conversion and filename/file display. Fourteen additional displayed-code fixtures check conversions, branching, matrix access, loops, all four function categories and command-line syntax. All are standard C11. Generic syntax templates intentionally contain placeholders and are not represented as standalone compilable programs.

Input contracts are explicit: selection sort accepts 1–100 values; the time example accepts nonnegative elapsed hours up to 100000 with minutes/seconds 0–59 so its long result is representable; filenames are limited to 255 characters. String filenames may include spaces. The file-output sample includes an exact fixture. No arbitrary grading threshold or exam marks assumption is invented.

**Figure limitation:** AGENTS.md currently freezes drawing generation. As in the existing PPS worksheet, Q1(a) supplies the algorithm and a labelled **text flowchart layout** identifying terminal/input/process/decision steps and Yes/No routes. No new drawn flowchart or image is claimed complete. Existing drawings and source PDFs are not published, edited or redrawn. No unit publication state changes. The new shell/data are small static text assets; no source binary is added.

## Files

- `index-resources.json`: new card; existing cards retained.
- `end-semester.html`: lightweight shared-UI shell and paper metadata slot.
- `exam-prep/end-semester.json`: source identity, exact questions/marks, answers, source traces and executable fixtures.
- `scripts/new/exam-prep.js`: generic paper metadata, OR markers in section data and program blocks in answer flow; existing source FAQ and Mid-II routes preserved.
- `styles/new/pages/exam-prep.css`: scroll offset for the paper header deep link.
- `scripts/tools/verify_pps_end_semester.py`: paper/marks/provenance checks and C compilation/execution.
- This audit.

## Validation

- `python3 scripts/tools/verify_pps_end_semester.py --source-text <supplied text> --kb-root <ingested KB>`: PASS. All 19 wordings match the supplied paper; all cited primary topics, images, source prompts and senior pages resolve. Original numbering, 60-mark choice scheme, OR placements, source traces, answer blocks, program/snippet references and index card verified.
- Five full programs plus 14 displayed-code fixtures compile with `-std=c11 -Wall -Wextra -Werror -pedantic` and produce expected samples. Tests include duplicates/negative values/singleton and invalid array sizes, equal-value swaps, time bounds and invalid minutes/seconds, missing/empty/space-containing filenames, and missing command-line arguments.
- `python3 scripts/tools/verify_college.py`: PASS.
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`: PASS.
- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`: PASS.
- Existing Mid-II and FAQ verifiers: PASS; their source data is unchanged.
- JavaScript/Python syntax, JSON parsing and `git diff --check`: PASS.
- Local Chromium at 1440 px and 390 px: card, all 19 answers, 26 navigation links, marks, five OR choices, function syntax, selection sort, time record, Q9 subparts, source disclosure, phone collapse/Back to top and `/Pankusdesk/` routing checked. Screenshots reviewed; no page errors or horizontal document overflow. Existing Mid-II/FAQ browser paths also checked for shared-renderer regressions.

The PR handoff supplies preview links and unchecked desktop/phone acceptance steps, with the exact deployed commit. No automatic merge.

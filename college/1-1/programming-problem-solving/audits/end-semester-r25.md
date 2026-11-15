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

The initial R25 implementation linked to the paper, units and questions. The later multi-paper update replaces this with three paper-only links as requested; see `end-semester-papers.md`. Selecting a question opens its dropdown answer. Back to top sits above navigation and remains available with mobile contents collapsed. No filters or topic-based merged questions are introduced.

## Answer authority and fidelity

The order is **Priyanka’s original class notes → senior KB → general PPS knowledge for gaps**. Original notebook images were compared directly with the answers, rather than relying on topic IDs as proof of faithful wording. `note_image_review` records the image checksums; each answer records the checked images, actual corrections and any fallback in `source_fidelity`. Notebook photographs remain private.

Definitions, syntax structure, example values and methods are retained. Whitespace and code formatting are normalized; invalid C and incorrect claims are corrected. The nested-if syntax includes inner decisions in both outer branches, and the ladder retains repeated else-if blocks. The source array values, conversion examples, calculator operations, loop examples and four separate sum definitions are preserved. The answers keep short definitions compact and give syntax, explanation and examples for longer questions. No invented submark allocation is supplied.

| Question | Original images checked | Corrections / fallback |
| --- | --- | --- |
| a | 23, 33 | Wording and syntax layout retained. |
| b | 50, 67, 68 | Corrected the reversed row/column description on image 67. Retained the 10×20 declaration. |
| c | 70, 71, 72 | Replaced the handwritten return type; with return expression;. Retained sum, x, y, c and the declaration/call/definition structure. |
| d | No direct source coverage | The supplied notes cover pointer declarations and row arrays of strings, but do not supply the array-of-pointers construct itself. |
| e | No direct source coverage | File-handling APIs are absent from both supplied note KBs. |
| 1(a) | 13, 14 | Added the n < 2 case, which the senior flag-only example misses. Priyanka does not supply the prime-testing example. The senior program on p47 tests i = 2 through n−1 using flag; that method is retained without substituting a square-root optimization. |
| 1(b) | 38, 39, 66, 67 | Removed the incorrect claims that implicit conversion is always promotion/lossless and explicit conversion is always demotion/lossy. Corrected the float-output call from %d with &f to %f with f. Retained the 3.5→3 and int-5→float examples. |
| 2 | 20, 21, 22, 23, 24, 25, 26, 33, 34, 36 | Corrected the positive-number condition a <= 0 to a > 0. The ladder example from senior p28 uses >= to handle tied greatest values correctly. The calculator keeps all four original operations; bounded operands and a zero-divisor check prevent arithmetic errors. Corrected goto’s classification to unconditional jump; it does not make a conditional decision. Priyanka image 23 supplies ladder syntax but no concrete ladder program; the greatest-of-three example comes from senior p28. |
| 3 | 42, 47, 48, 50 | Corrected the 1-D for-header separators and used &a[i] for numeric input. Corrected the 2-D display from a[i] to a[i][j], preserving the original 3×3 values and two-loop structure. |
| 4 | 27, 29, 30, 31, 32 | The do–while example’s heading asks for even terms but its i = 1 visits odd terms. Changed i to 2 and corrected the copied output label; the intended result is 420. Kept the source factorial loop i = 1 through n; used unsigned long long and a supported input bound to avoid overflow. Used entry-controlled execution for for, correcting the misleading flowchart ordering on image 32. |
| 5(a) | 79, 80, 81, 82 | Completed the source margin’s instruction to put the swap in a function. Corrected pointer initialization and exchanged *x and *y using an int temporary, rather than exchanging pointer values through an int. Clarified the class term call by reference: C passes pointer values, and dereferencing them updates the caller’s objects. |
| 5(b) | 71, 72, 73, 74 | Corrected “without return type” to “without return value” (void). Corrected void sum; to a function declaration; used (void) for no parameters. The four sum signatures are alternatives, so their C checks compile them separately. |
| 6 | No direct source coverage | Priyanka supplies the selection-sort prompt and sorting context; senior notes name the method but contain no complete implementation. The selection algorithm, code, trace and stability explanation are general PPS completion. |
| 7(a) | 79, 80, 94 | Did not present the notebook’s illustrative numeric memory addresses as guaranteed runtime values. |
| 7(b) | 79, 80, 81 | Corrected y = y * 10 (invalid pointer multiplication) to *y = *y * 10. Corrected printing y with %d to printing the pointed-to int *y. Corrected the pointer prototype. |
| 8 | 95, 96, 97 | C pointer arguments themselves pass by value; updates through a pointer affect the original structure. Neither set of notes supplies this exact time-conversion program. The two methods and class examples are retained; the time program is the application explicitly required by the paper. |
| 9(a) | 4, 5, 6, 40 | Corrected the claim that function implementations are stored/executed in the header; the header supplies declarations. Kept preprocessing separate from linking. |
| 9(b) | No direct source coverage | File handling is not covered by the supplied Priyanka or senior note KB. |
| 10 | No direct source coverage | Senior notes support the hosted main signature; file APIs, positioning rules and argc/argv behaviour require general PPS supplementation. |

The Source disclosure contains correction and fallback details, closed by default. There are no discrepancy badges or source-review essays in the main answer. The Q8 time conversion is the application requested by the exam; Priyanka’s complex-number and marks examples explain the two structure-passing methods, rather than being attributed as the exact time program.

## Code, examples and figures

Five complete C11 programs cover swap, selection sort, pointer indirection, time conversion and file display. Nineteen displayed-code fixtures check the actual examples, including the four alternative sum signatures compiled separately. Input validation and representable ranges prevent errors without changing the illustrated methods. The senior prime method retains flag and divisors 2 through n−1; the missing n < 2 case is corrected.

**Figure limitation:** AGENTS.md freezes drawing generation. Q1(a) supplies an algorithm and labelled text flowchart logic with symbols and branches, not a drawn flowchart. No existing figures were changed, and no source scans were published. No publication state changes.

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
- Five full programs plus 19 displayed-code fixtures compile with `-std=c11 -Wall -Wextra -Werror -pedantic` and produce expected samples. Tests include duplicates/negative values/singleton and invalid array sizes, equal-value swaps, time bounds and invalid minutes/seconds, missing/empty/space-containing filenames, and missing command-line arguments.
- `python3 scripts/tools/verify_college.py`: PASS.
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`: PASS.
- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`: PASS.
- Existing Mid-II and FAQ verifiers: PASS; their source data is unchanged.
- JavaScript/Python syntax, JSON parsing and `git diff --check`: PASS.
- Local Chromium at 1440 px and 390 px: card, all 19 answers, 26 navigation links, marks, five OR choices, source-specific nested-if/ladder syntax, conversion examples, selection sort, time record, Q9 subparts, source disclosure, phone collapse/Back to top and `/Pankusdesk/` routing checked. Screenshots reviewed; no page errors or horizontal document overflow. Existing Mid-II/FAQ browser paths also checked for shared-renderer regressions.

The PR handoff supplies preview links and unchecked desktop/phone acceptance steps, with the exact deployed commit. No automatic merge.

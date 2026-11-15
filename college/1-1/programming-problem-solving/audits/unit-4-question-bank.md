# Unit 4 Question Bank — source selection and answer review

## Scope and card

Adds a **Unit 4 Question Bank** card and a shared-renderer HTML page. Naming is suitable for corresponding Unit 3/5 banks later; no empty future cards or routes are introduced. Existing PPS cards, end-semester/Mid-II/FAQ content, figures and publication states remain unchanged.

The page has 41 source question occurrences in two navigation sets: Important Questions (15 short + 10 long) and Additional Question Bank (8 short + 8 essay). Each question has a dropdown answer. Left navigation lists the sets only; Back to top remains above the contents and available when phone contents are collapsed. The compound final essay retains both printed subparts and the printed program, with separate answer panels.

## Supplied documents

| Source | Pages | Treatment |
| --- | --- | --- |
| `unit 3,4 and 5 important questions.pdf` | 2 | Select only the explicitly headed Unit 4 section: 15 short on p1 and 10 long on p2. Exclude Unit 3 (8 short + 7 long) and Unit 5 (15 short + 7 long). |
| `Unit 4 IMP Question and answers.pdf` | 19 | All 15 short and 10 long items correspond to the selected important questions. Store question-to-answer page references and use it for comparison; do not duplicate the same 25 questions as a third set. Its headings supply 3-mark short / 8-mark long labels. p19 is blank. |
| `Unit-4_Question Bankn pps.pdf` | 1 | Include all 8 short and 8 essays by their structures/union/pointer/DMA subject matter and explicit user scope. Retain the actual printed **UNIT-5** heading in source metadata; no marks are invented. |

Every source retains its ZIP member name, SHA256, page count and original heading. Source text/page images were inspected. The mixed PDF actually contains Unit 5 as well as Units 3/4; its file title is preserved. Source scans and ZIP binaries remain private. Only static text/JSON/code assets are added.

## Answer authority

The order is **Priyanka’s class notes → senior KB → general PPS knowledge for missing coverage**. Existing original-image-reviewed answers are reused where the prompt fits. Per-answer primary image/topic IDs, senior page IDs, corrections and required applications are retained. The supplied Sriharsha answers are a comparison source, not a replacement for Priyanka’s class wording/methods.

Important source choices and corrections:

- Structure records, dot/arrow access, array-within and array-of-structures retain Priyanka’s student fields and loops. The generic structure-pointer program uses s1/s2, name[20] and rollno. The separate five-student essay uses exactly its requested address, three marks, totals and percentages; each subject is explicitly assumed out of 100. Names/addresses are bounded single input tokens, with underscores usable within an address.
- Nested structures use the senior student/birthday example because Priyanka’s supplied notes do not supply that construct. The class source’s complex-value addition and pointer-based marks update demonstrate structure parameter methods.
- Priyanka gives two whole-structure passing methods. Passing selected members is described separately. Neither pointer passing nor value passing is universally best; the correct choice depends on mutation, record size and interface needs.
- The companion answer under pointer-to-array-of-strings supplies a 3-D **integer** array. The corrected answer uses a pointer to the entire 3×20 character row array and explains the alternative pointer-to-row interface, distinguishing both from an array of pointers.
- Allocation and function-pointer APIs require general PPS completion. calloc produces a single contiguous allocation with all bits zero; realloc uses a temporary; example allocations are released. Pointer arithmetic stays within one array and distinguishes pointer increments from pointed-to value increments.
- Structure/union sizes include padding and alignment; no exact byte-size guarantee is invented. Anonymous structures may still be reused through a typedef alias, correcting the companion answer’s absolute restriction.
- The printed pointer-subtraction program contains curly quotes. Even after quote correction, p and q point to separate scalar objects: p-q has undefined behavior. The question is retained for analysis, is not executed as a valid program, and has no invented numerical output. Its 4-D pointer expression is worked separately.

| Answer record | Primary note references | Completion / correction context |
| --- | --- | --- |
| `structure` | Priyanka images 89, 90, 91, 92 | Initializer values illustrate the notebook’s student record; these particular initializer values are an authored example. |
| `union-compare-short` | Senior pages 121, 122, 123 | Source definition/method retained; corrections in source_fidelity. |
| `union-compare-long` | Senior pages 121, 122, 123 | Source definition/method retained; corrections in source_fidelity. |
| `pointer` | Priyanka images 79, 80, 81 | Source definition/method retained; corrections in source_fidelity. |
| `self` | Priyanka images 101 | Source definition/method retained; corrections in source_fidelity. |
| `array-within-long` | Priyanka images 89, 90, 91, 92 | Source definition/method retained; corrections in source_fidelity. |
| `array-of-long` | Priyanka images 92, 93 | Source definition/method retained; corrections in source_fidelity. |
| `nested-long` | Senior pages 119, 120 | Source definition/method retained; corrections in source_fidelity. |
| `array-vs-structure` | Priyanka images 42, 89, 90, 91, 92 | Source definition/method retained; corrections in source_fidelity. |
| `tag` | Priyanka images 90, 91, 92 | The anonymous typedef example is a standard-C clarification of the supplied tag explanation. |
| `nested-short` | Senior pages 119, 120 | Source definition/method retained; corrections in source_fidelity. |
| `array-of-short` | Priyanka images 92, 93 | Source definition/method retained; corrections in source_fidelity. |
| `array-within-short` | Priyanka images 89, 90, 91, 92 | Source definition/method retained; corrections in source_fidelity. |
| `access` | Priyanka images 90, 91, 92, 94, 95 | Source definition/method retained; corrections in source_fidelity. |
| `union` | Senior pages 121, 122, 123 | Source definition/method retained; corrections in source_fidelity. |
| `pointer-advantages` | Priyanka images 79, 80, 81, 98, 99, 100, 101 | Dynamic allocation and the broader list of pointer uses require general PPS completion; the notes supply the address, traversal and self-reference methods. |
| `dma-syntax` | General PPS gap | Neither supplied notebook covers the allocation APIs. Standard-C syntax completes this topic. |
| `pointer-arithmetic` | Priyanka images 98, 99, 100, 101 | Source definition/method retained; corrections in source_fidelity. |
| `function-pointer` | General PPS gap | Neither supplied note KB covers function pointers. The supplied question/answer example is completed with a declared, defined sum function using standard C. |
| `structure-passing` | Priyanka images 95, 96, 97 | The sample numeric initializers are authored; the complex and marks methods come from the class notes. |
| `dma-long` | General PPS gap | Neither supplied note KB covers dynamic allocation; the four API contracts and checked program are general PPS completion. |
| `pointer-to-array` | Priyanka images 98, 99, 100, 101 | Priyanka supplies element-pointer traversal; the whole-array pointer declarator is a standard-C completion supported by the supplied answer example. |
| `pointer-string` | Priyanka images 50, 98, 99, 100, 101 | Applied the pointer traversal method to the class string "rama". |
| `pointer-array-strings` | Priyanka images 67, 68, 98, 99, 100, 101 | The row-array storage comes from Priyanka; the pointer-to-row declaration is standard-C completion. |
| `structure-pointer` | Priyanka images 94, 95 | Source definition/method retained; corrections in source_fidelity. |
| `union-uses` | Senior pages 121, 122, 123 | The separate tag is a standard-C usage clarification. |
| `self-purposes` | Priyanka images 101 | Source definition/method retained; corrections in source_fidelity. |
| `pointer-and-uses` | Priyanka images 79, 80, 81, 98, 99, 100, 101 | Dynamic allocation and the broader list of pointer uses require general PPS completion; the notes supply the address, traversal and self-reference methods. |
| `array-pointers` | General PPS gap | The supplied note KBs cover element pointers and row arrays, but not the array-of-pointers construct; this is general PPS completion. |
| `dma-purpose` | General PPS gap | Dynamic allocation APIs and their purposes are absent from both supplied note KBs. |
| `malloc` | General PPS gap | Allocation API contracts require general PPS knowledge; not covered in either note KB. |
| `calloc` | General PPS gap | Allocation API contracts require general PPS knowledge; not covered in either note KB. |
| `five-students` | Priyanka images 92, 93 | Applied Priyanka’s array-of-students and per-student average method to the exact five records, address and three marks requested by the bank. |
| `union-program` | Senior pages 121, 122, 123 | Source definition/method retained; corrections in source_fidelity. |
| `self-program` | Priyanka images 101 | Completed the notebook’s node declaration with two objects and a traversal to satisfy the program prompt. |
| `pointer-operations` | Priyanka images 79, 80, 81, 98, 99, 100, 101 | Source definition/method retained; corrections in source_fidelity. |
| `pointer-analysis` | General PPS gap | The 4-D expression and unrelated-pointer subtraction analysis are not directly covered by the supplied notes; this is standard-C completion. |

## Validation and review

- `verify_pps_unit4.py --source-root <private intake> --kb-root <private KB>`: all 41 question wordings and selected source sections match, source checksums resolve, 25 companion mappings/marks are recorded, all source-topic/page references resolve, all question/answer/program IDs and table dimensions pass.
- Fifteen complete C11 programs compile with `-std=c11 -Wall -Wextra -Werror -pedantic` and produce their stated outputs. Tests cover five-student totals/percentages and invalid marks, per-student reset, allocation operations, defined same-array subtraction, pointer strings, function calls and pointer/member updates. The invalid printed program is not executed.
- Required college/BEE/MAC validators PASS. Existing Mid-II, FAQ and end-semester verifiers PASS. JavaScript/Python syntax, JSON parsing and diff checks PASS.
- Desktop/phone browser checks PASS: the new card, 41 answers, two nav sets, source marks versus unspecified marks, corrected string program, separate compound question/answer panels, exact five-student output, mobile collapse/Back to top and /Pankusdesk/ routing. Existing shared-renderer routes retain their prior question/navigation counts. Screenshots were inspected and remain private.

No diagrams are generated or modified. The PR includes the exact preview commit and unchecked acceptance steps; no automatic merge.

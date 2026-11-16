# Unit 3 Question Bank — source selection and answer review

## Scope and arrangement

Adds the **Unit 3 Question Bank** card immediately before the existing Unit 4 card. The new page uses the shared Q&A renderer and has 36 source question occurrences in three navigation sets:

| Set | Short | Essay / long | Total |
| --- | --- | --- | --- |
| Part 1 — Searching & Sorting | 2 | 5 | 7 |
| Part 2 — Functions & Recursion | 8 | 6 | 14 |
| Important Questions — selected Unit 3 section | 8 | 7 | 15 |

All questions from both Unit 3-only PDFs are included. From `unit 3,4 and 5 important questions.pdf`, only the Unit 3 block on page 1 is selected; Unit 4 and Unit 5 questions are excluded. The actual ZIP member names, page counts and checksums are retained in JSON. The two Unit 3-only pages were inspected directly, along with the previously reviewed mixed source. No source document prints marks, so none are invented.

Numbering and question wording remain source-specific. Overlapping questions stay in their source sets, while matching answers/programs are shared inside the data. The compound recursive-program prompt retains its repeated “Factorial” and “Akerman” spelling; four distinct tasks are answered in separate panels: factorial, GCD, Ackermann and Fibonacci. The repetition is recorded rather than silently deleting part of the printed prompt.

Left navigation lists the three question sets, not individual questions. Back to top remains above collapsible phone contents. Existing Unit 4, paper/FAQ data, figures and publication states are unchanged. No new drawings or source binaries are added.

## Source priority and fidelity

Authority remains **Priyanka → senior KB → general PPS knowledge for gaps**. Original-image-reviewed class material supplies function definitions/declarations/calls, actual/formal arguments, four sum categories, value/pointer swap, Fibonacci term-count recursion, whole-array passing, bubble sort and the original matrix values. Every answer records actual topic/image/page references, corrections and any required application/fallback.

- Four argument/return categories retain Priyanka’s sum examples and source order. They are alternative definitions compiled separately, not C overloads.
- Value swap changes only local copies. Pointer swap uses addresses and dereferenced values to change the caller. C passes pointer values by value. Distinct function names allow both interfaces to coexist in the example.
- Function headers supply declarations, not already-executed library function bodies. Global visibility is governed by declaration and scope; the local/global comparison distinguishes lifetime from name visibility and uses the senior 2/20/2 shadowing pattern.
- Recursive Fibonacci starts at F0=0, F1=1 and prints the first n terms. Recursive factorial and Ackermann use senior recurrence coverage where Priyanka does not supply those implementations. Recursive Euclidean GCD is a genuine general-knowledge completion.
- Ackermann uses A(0,n)=n+1, A(m,0)=A(m−1,1), A(m,n)=A(m−1,A(m,n−1)). The pseudocode preserves nested evaluation. The C demonstration accepts m=0..3 and n=0..6 with a one-million-call budget; all results in this rectangle fit the result type. The worked A(2,1)=5 trace keeps the outer calls after the intermediate 3.
- Binary search recomputes mid, terminates on a match and reports the actual position. Its O(log n) bound is justified by halving. Selection sort uses the n(n−1)/2 scan count even on sorted data; O/Ω/Θ are not names for worst/best/average cases.
- The notes list selection and insertion sorting but do not supply complete implementations. Those algorithms, traces and complexity derivations are explicit general PPS completion. The shared class input values 20,12,1,4,9 are retained for the worked examples.
- Matrix multiplication is actually performed inside multiply(), with 3×3 row parameters; it is not replaced by a main-only program. The example uses Priyanka’s original 3×3 values and the senior multiply-accumulate method. A separate display() example explains fixed-column 2-D array parameters.
- Modularization/recursion/function advantages not supplied as lists in the notebooks are labelled general PPS explanations in provenance. Recursion is not described as automatically faster or optimized.

| Answer | Primary references | Completion / application |
| --- | --- | --- |
| `syntax` | Priyanka images 70, 71, 72 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `advantages` | Priyanka images 70, 71, 72 | Priyanka defines functions but does not list their advantages; the senior function material does not supply that list either. These advantages are general PPS completion, not verbatim note text. |
| `parameters` | Priyanka images 70, 71, 72, 79, 80, 81 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `categories` | Priyanka images 71, 72, 73, 74 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `array-sum` | Priyanka images 84, 85, 86, 87, 88, 89 | Adapted the source whole-array parameter method and integer sum function to the paper’s requested total; the specific loop is an exam application. |
| `factorial` | Priyanka images 75, 76, 77, 78, 83; senior pages 106, 107, 108, 109 | Priyanka supplies factorial and recursion separately; senior p108 supplies the recursive factorial recurrence. |
| `selection` | Priyanka images 64, 66; senior pages 73 | Priyanka supplies the selection-sort prompt and sorting context; senior notes name the method but contain no complete implementation. The selection algorithm, code, trace and stability explanation are general PPS completion. |
| `function-definition` | Priyanka images 70, 71, 72 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `recursion-short` | Priyanka images 83 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `libraries` | Priyanka images 53, 56, 70, 71, 72 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `local-global` | Priyanka images 4, 5, 6; senior pages 57, 58, 59, 60 | The block shadowing example adapts the senior 2/20/2 demonstration to file versus local scope. |
| `value-short` | Priyanka images 79, 80, 81 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `value-pointer` | Priyanka images 79, 80, 81, 82 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `modularization` | Priyanka images 70, 71, 72 | The notes give task-oriented functions, but do not supply a modularization definition or advantages list. Those explanations are general PPS completion. |
| `recursion-iteration` | Priyanka images 27, 28, 31, 32, 83; senior pages 105 | Comparison organized from the source recursion and loop examples; complexity depends on the algorithm, not the label alone. |
| `ackermann-short` | Senior pages 110, 111, 112 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `recursive-tasks` | Priyanka images 75, 76, 77, 78, 83; senior pages 106, 107, 108, 109, 110, 111, 112 | The GCD method is a general PPS gap completion; Ackermann uses senior pp110–112. Each program states its own supported inputs. |
| `recursion-essay` | Priyanka images 83; senior pages 105 | The supplied notes demonstrate recursion but do not supply this advantages list; that list is general PPS explanation. |
| `calling-methods` | Priyanka images 70, 71, 72, 79, 80, 81, 82 | Interpreted “function calling methods” as the source value-argument and address-argument methods; the separate categories question covers the four argument/return combinations. |
| `array2d` | Priyanka images 47, 48, 50, 85, 86, 87, 88, 89 | The notes supply 2-D storage and whole-array function context; the exact fixed-column parameter declaration is standard-C completion. |
| `matrix-functions` | Priyanka images 47, 48, 50, 85, 86, 87, 88, 89; senior pages 81, 82, 83, 84, 85, 86 | Combined the senior multiplication loop with the requested function interface and Priyanka’s matrix storage/values. |
| `bubble` | Priyanka images 64, 65, 85, 86, 87, 88, 89 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `linear-algorithm` | Priyanka images 59, 60, 61, 62 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `binary-complexity` | Priyanka images 59, 60, 61, 62 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `selection-complexity` | Priyanka images 64, 65; senior pages 73 | The notes list selection sort but do not derive its scan count; the comparison-count justification is general PPS completion. |
| `binary-algorithm` | Priyanka images 59, 60, 61, 62 | Reviewed source definition/method; actual corrections recorded in source_fidelity. |
| `insertion` | Priyanka images 64, 65; senior pages 73 | Both notes name insertion sort but do not give its full algorithm/program. This method, code and trace are general PPS completion with the class example values. |

## Validation

- Unit 3 verifier: all36 wordings/checksums, mixed-unit extraction, original numbering, no invented marks, source-topic/image/page references, all question/program/fixture IDs and immediate card order before Unit 4 PASS.
- Twelve full C11 programs and four displayed function-category fixtures compile with `-std=c11 -Wall -Wextra -Werror -pedantic`; samples and boundary tests PASS. Checks include factorial zero/overflow bound, Fibonacci zero/one/negative count, GCD with one/both zero, Ackermann base/recursive/maximum-supported/invalid arguments, equal swaps, duplicate/negative sorting values, singleton insertion and non-identity matrix multiplication.
- Required college/BEE/MAC validators PASS. Existing Unit 4, Mid-II, FAQ and end-semester verifiers PASS. JSON/Python syntax and diff checks PASS.
- Desktop/phone browser checks PASS: card order, all36 answer bodies, three set links, four recursive task panels, Ackermann pseudocode, insertion trace, matrix function call, mobile contents/Back to top and /Pankusdesk/ routing. Existing renderer routes retain their prior question/navigation counts. Screenshots were inspected and are kept privately.

The PR handoff includes an exact preview commit and unchecked desktop/phone acceptance steps. No automatic merge.

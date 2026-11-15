# End-semester FAQs, supplementary file and related AE papers

## Entry order and source identity

There are exactly eight navigation entries. The three PPS entries from PR #48 remain first and their data is unchanged.

| Position | Entry | Printed identity / scope | Dropdown count |
| --- | --- | --- | --- |
| 1 | PPS January 2026 | R25, 25ES1CS101 | 19 |
| 2 | PPS January 2025 | R22, 22ES1CS101 | 24 |
| 3 | PPS January 2024 | R22, 22ES1CS101 | 25 |
| 4 | Frequently Asked Questions | Curated revision, 10 short + 10 essay; no official marks | 20 |
| 5 | Supplementary file January 2025 | Uploaded filename says Supplementary; printed heading says Regular/Supplementary, R22, 22ES1CS101 | 24 |
| 6 | Problem Solving Through C — AE January 2026 | R25, 25ES1DS101 | 20 |
| 7 | Problem Solving Through C — AE January 2025 | R22, 22ES1IT101 | 21 |
| 8 | Problem Solving Through C — AE January 2024 | R22, 22ES1IT101 | 20 |

The new `pps_vnr_pyq.zip` contains the same seven substantive PDF files as the earlier upload. Each file has its own SHA256 and printed exam identity in the data. Filename years are not used as exam dates. All three AE paper question pages were inspected directly; their second pages, where present, contain closing markers only. The archive checksum is stored in `archive_intake`; no PDF/ZIP or notebook photograph is committed.

The supplementary file is now independently accessible at the user’s explicit request. Its questions match the existing January 2025 PPS paper; `duplicate_of` remains in its source record and its entry note states the overlap. It is not represented as an independently verified different exam sitting. Per-question page references follow that copy’s pagination. All seven supplied files are accessible through paper entries, and the eight-entry total includes the curated FAQ set.

## Questions, answers and authority

There are 153 paper-question/subpart occurrences plus 20 revision FAQs, for 173 dropdowns. The seven paper entries retain their printed questions, numbering, marks, units and five OR choices apiece. Each paper still requires 60 attempted marks, not the sum of all alternatives. The original three entries, question/answer objects, programs and deep-link IDs are preserved.

The FAQ questions are explicitly labelled curated revision, not an authentic eighth exam or an exam prediction. Ten short and ten essay questions address supplied-paper topics. Each links in metadata to an actual source question ID. They receive no invented official marks. Short answers are concise; essay answers include definitions, syntax, explanations, traces or tested C examples as appropriate. The separate existing main-page FAQ card remains intact.

Answers follow **Priyanka → senior KB → general PPS knowledge for genuine gaps**. Existing reviewed answers are reused for matching prompts. New original-image comparisons cover Priyanka 9–10 (types), 13–14 (flowcharts/conditional maximum), 83 (recursive Fibonacci), 84–85 (array parameters) and 101 (self-reference), alongside the previous reviewed class-note material. Per-answer topic IDs, corrections and exam-specific applications remain recorded. Examples use C, not C++.

Source-specific choices:

- Fibonacci retains fib(0)=0, fib(1)=1 and fib(m−1)+fib(m−2), with n as term count. It is not replaced by iteration.
- Arrays retain the source matrix values and pointer/row-array methods. Name sorting combines row arrays, strcmp and shrinking bubble passes.
- The calculator retains all four integer operations; the nested greatest-of-three code retains both outer branches.
- Student arrays keep roll/name/marks, per-student sum reset and a float average. One prompt reads n students; the other fixes exactly five, as printed.
- Manual concatenation follows the senior copy loops after Priyanka’s library-method context. Bounded line input replaces gets, preserves spaces, and leaves room for the terminator.
- Precedence levels, legacy fixed datatype sizes and NULL-as-keyword wording are corrected. Bit-field output explicitly casts promoted narrow fields for %u.
- Bit-fields, file APIs, dynamic allocation, computer components, interpreter comparison and GCD need the general knowledge fallback; they are not attributed as original Priyanka content.
- The weekday question supplies eight values (0–7) for seven days but no mapping. The answer explicitly chooses 0 = exit and 1–7 = Monday–Sunday. The prime-generation question has no range: the program explicitly takes an inclusive upper bound.

## UI and figures

Navigation lists only the eight entries, with no individual-question links. Back to top remains above the collapsible phone navigation. The shared renderer accepts a revision-set intro/group titles without inventing an exam code, time or marks for FAQs. The supplementary overlap note is visible at its entry heading; answer corrections remain in closed Source disclosures. Existing Mid-II and source-FAQ rendering paths remain unchanged.

The figure freeze remains active. Sum/max/quadratic/prime flowchart answers contain labelled text logic, not generated drawings. No existing figures are altered and no publication state changes.

## Validation

- `verify_pps_end_semester.py`: source words/checksums for all paper questions, all source-topic references, eight-entry order, 10+10 FAQ split and genuine question references, unique anchors, marks and 35 OR choices.
- 42 complete C11 programs and 24 code fixtures compile with strict warnings. Samples and boundary cases cover empty/one-term Fibonacci, factorial zero and invalid bounds, names with duplicates, manual concatenation with spaces/empty lines, array sums, zero GCD, menu bounds, prime generation, sum bounds, and student counts, in addition to the preserved tests.
- Required college/BEE/MAC validators PASS. Existing Mid-II/FAQ verifiers, JavaScript/Python syntax and diff checks PASS. Existing Mid-II/FAQ desktop/phone browser regressions PASS.
- Browser review PASS: all 173 dropdowns, eight ordered nav entries, FAQ labels/no invented metadata, supplementary page references, AE identity, bit-fields, old deep links, desktop/phone Back to top and /Pankusdesk/ routing. Screenshots were inspected and remain private.

The PR handoff includes the exact preview commit and unchecked manual desktop/phone acceptance checks. No automatic merge.

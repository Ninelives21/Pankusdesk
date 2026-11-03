# PPS worksheet 1

Source: user-supplied `c programs list.pdf`, retained unchanged as `worksheets/worksheet-1.pdf`; SHA-256 stored in the JSON bank. Both source pages were read. All 10 problems and 30 labelled subparts are preserved in source order. Code, assumptions, explanations, sample inputs and expected results are PankusDesk-authored.

The existing semester course record supplies PPS code/name/credits. Activating its page enables both the semester subject card and the existing shared subject dropdown. No syllabus, textbook theory, class notes or publication-ready unit coverage is invented. This worksheet-first index explicitly says notes have not been added.

Left navigation lists each parent problem and each a/b/c subpart with a short description. Shared study accordions display the questions and explanations; C source is inserted as escaped text in pre/code elements, not interpreted as HTML or executable browser code. No subject-specific MathJax loader or accordion implementation is introduced.

All 30 standalone C11 programs compile with `-Wall -Wextra -Werror` and pass their sample tests. The permanent `scripts/tools/verify_pps_worksheet.py` compiles programs into a temporary folder and checks 21 extra boundary/error cases. Compile with `cc -std=c11 program.c -lm`. Code is bounded for classroom use: dimensions at most10, arrays at most100, strings at most100 bytes, numeric inputs restricted as stated. These limits avoid fixed-buffer and integer overflow; quadratic roots and arithmetic still use finite-precision floating point.

Interpretations are explicit: Fibonacci uses a maximum value rather than a term count; binary search requires ascending input; diagonals means both main and secondary diagonals of a square matrix; upper triangle includes the main diagonal; a pyramid input is its row count; digit exercises use nonnegative integers; average marks assumes a 100-mark scale. There is no official supplied answer key.

The ten source requests for a flowchart receive labelled text flowchart logic alongside the code, not generated drawings, in keeping with the existing figure freeze. Existing figures/content and MAC PR #25 are untouched. No production merge or deployment is performed by this branch.

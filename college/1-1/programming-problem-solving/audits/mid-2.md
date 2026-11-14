# Mid-II Revision & Papers

## Scope and data contract

`mid-2.html` is a static shell for the shared `scripts/new/exam-prep.js` adapter and shared study-UI accordions. `exam-prep/mid-2.json` contains60 revision entries,111 source question occurrences,3 historical paper records and26 standalone authored C11 examples. The index adds one card; Worksheet & Solutions1 and its resources are unchanged. No source scans or internal note KB files are published.

- `questions`: stable topic IDs, full selected question wording, R25 unit, short/long type, answer ID and all source-occurrence IDs. These records supply answer mappings and compatibility aliases only. The page displays each original source occurrence with its original number and wording instead of topic-based revision headings.
- `occurrences`: original source, PDF page, question number/type, wording and answer mapping. Questions from the supplied UnitIII Part2 bank, structures/pointers bank, UnitV bank and two-page important list are accounted for. The supplied derivative Q&A contributes its explicitly numbered storage-class Q8.
- `answers`: authored explanation, explicit note/general basis, image/page references and program IDs. Answer order is Priyanka, then senior, then general PPS for gaps. Supplementary answer PDFs are not treated as verified solution or PYQ authority.
- `papers`: printed exam identity, source IDs/page locators, original groups/parts/marks and OR placement. R25 mappings are stored per part separately from paper order.
- `sources`: original filenames and SHA256. `programs`: complete code, assumptions, sample input and expected output/file behavior.

This is the Mid-II collection, not a claim that every historical question in every uploaded archive has been fully transcribed or that all R25 syllabus topics are covered. File/preprocessor/allocation topics absent from the handwritten KB use explicitly identified general PPS supplementation. No authoritative textbook-led unit publication state changes.

## Verified intake decisions

- The structures/pointers one-page bank is printed UNIT-5 but belongs to R25 UnitIV by content. Its printed label remains in source metadata. The UnitIII bank includes Ackermann and a2D-array parameter question.
- A slash-separated important question repeats Factorial; the answer covers factorial once plus GCD, Ackermann and Fibonacci, with separate input contracts. GCD is general-knowledge supplementation.
- The duplicated UnitIII/IV bank copies inside the Mid-II ZIP contribute no duplicate revision entries.
- March2023: low-resolution complete photo plus a higher-resolution partial view of the same dated paper. The high-resolution photo’s filename is not an exam date.
- January2024: photo plus page3 of `Sem-1 mid-2.pdf` establish the complete PPS paper. Other subjects on pages1,2,4,5 are excluded.
- January2026: direct orientation-aware inspection of the original JPEG confirms all questions through6(b). The earlier intake classification as partial was wrong and is superseded. Printed date02/01/2026 and R25 take precedence over filename2025. No new or missing questions are invented.
- All papers have PartA5×2marks, and PartB alternatives worth4marks for UnitIII,8 for IV,8 for V. Paper choices and subparts remain separate.
- The supplied UnitIV question8 subtracts addresses of two separate scalar objects. That is undefined behavior, so no numerical output is invented; the original code remains visible with the shared amber discrepancy treatment.
- January2026 PartA(d) prints a macro lacking parameter parentheses and nonstandard `void main()`. Its expression expands to5+6*5+6=41. The portable entry-point correction and the121 result of a different corrected macro are distinguished explicitly.

## Authored C and interpretation limits

Programs are standalone and formatted for reading. Common headers keep each snippet independently compilable. Compile with `cc -std=c11`; no conio/gets or nonstandard string functions. Recursion inputs are tightly bounded; array sizes and selected input ranges are explicit. The five-student percentage assumes three100-mark subjects and single-token name/address input. Inventory fields and file fixtures are authored because prompts do not supply them. Native binary struct storage is labelled implementation-specific. C file I/O tests inspect output files as well as stdout.

## Reproducible validation

- `python3 scripts/tools/verify_pps_mid2.py`: source-occurrence/answer/anchor references, exact60/111 coverage, paper marks/OR integrity;26programs built with `-std=c11 -Wall -Wextra -Werror -pedantic`, samples and file outputs checked; selected invalid recursion/array bounds rejected.
- `node --check scripts/new/exam-prep.js`.
- `python3 scripts/tools/verify_college.py`.
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`.
- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`.
- Chromium at1440px and390px:149 question-and-answer dropdowns (111 revision occurrences and38 paper subparts), eight navigation links for three individual papers and five revision sets, original wording/numbering, and no topic filters or tabs. Paper navigation, legacy compound-question deep links, macro answer, mobile contents collapse and Back to top checked. No page errors or document horizontal overflow. Desktop and mobile screenshots inspected. GitHub Pages base-path routing checked separately.

The simplified presentation supersedes the initial topic-based layout. The PR handoff identifies the current preview commit and deployment status.

## Manual acceptance checks for PR

Supply actual preview links when deployment is available. Verify index-card navigation/worksheet preservation, mobile navigation/Back to top, original paper numbering/OR choices and the2026 macro trace. These remain user checks, not completed agent checkboxes. No auto-merge.

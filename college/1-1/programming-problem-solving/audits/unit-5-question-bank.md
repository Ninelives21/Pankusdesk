# Unit 5 question bank — source and answer audit

## Scope and source inventory

User-authorized Unit 5 card and question bank; answers follow Priyanka → senior KB → general PPS knowledge. This adds practice material and does not change unit publication states, shared renderers, existing answers or figures. PPS currently uses standalone question-bank shells rather than a subject.json unit renderer.

The private `pps_ques_unit5.zip` contains two PDFs. Filenames, archive members, SHA-256 values and page counts are in `exam-prep/unit-5-question-bank.json` under `sources`; no PDFs or notebook photographs are published.

| Source | Pages | Included occurrences |
| --- | --- | --- |
| Unit 5 IMP Question and answers.pdf | 19 | 15 short + 7 long + 4 extra = 26 |
| Unit-5_Question Bank pps.pdf | 1 | 11 short + 7 essay = 18 |

All 44 prompts retain source wording and numbering, including original spelling. Repeated questions remain in their own source sets and share applicable answers. Short/long headings in the answers PDF establish 2/8 marks. Neither the additional bank nor the four extras has definite marks; none are invented. The extra random-access answer's study-priority advice is source content, not an instruction to omit answers.

## Answer authority and factual review

- Priyanka images 4–6 and 40: program organization, #include, #define and PI = 3.14. The circle exercise uses radius 5 from the supplied question/answer example and the class PI value, giving 78.50. The supplied 3.1415 is not classified as an error.
- Senior pages 9–10: enum/typedef definitions and weekday values. Priyanka's structure typedef examples do not supply this standalone enumeration treatment.
- File APIs, command-line API details, random access and the inventory file program are absent from both note KBs. These are explicit general PPS completion using the supplied answers as supporting material. Each answer records this fallback under its closed Source disclosure. No file-handling answer claims notebook support.
- Each question maps to the supplied source page. The verifier compares all 44 prompt strings with extracted source text and validates source hashes; the intake PDFs were also visually inspected for headings, code and compound prompts.

Verified corrections: EOF is not a required stored text-file character; text is not restricted to ASCII; binary storage is not universally smaller/faster; FILE* identifies a stream object. Offset 15 is the 16th byte; end-relative seeks require support, and arbitrary byte offsets are not portable for text streams. ftell is not a portable text file-size calculation. rewind clears error and EOF indicators; fseek does not clear the error indicator. Corrected main's parameter syntax and conditional argv access. fgetc uses int, reads test the operation's result, strings are bounded and file operations are checked. Parenthesized function-like macro substitutions; repeated argument side effects remain unsafe. C11 enum constants have type int; enums are not strongly typed C++ enums. Macro definitions are not scoped by C braces. Comparison examples avoid macro/enumerator name collisions.

## Program assumptions and fidelity

Ten full standard-C examples and one enum snippet:

- Text record write/read retains a complete open/write/close/reopen/read/close sequence.
- Counting: up to 255 input characters, total includes newline, special symbols exclude alphanumeric and whitespace; the sample has 9 total, 3 letters, 2 digits, 2 symbols and 2 whitespace characters.
- Error handling: a normal EOF and clearerr demonstration, plus optional missing-path input; no intentionally invalid FILE* operations.
- Binary: retain the supplied integer 123; read into a separate object. Native object representation is explicitly implementation-dependent.
- Copy: source input.txt, separate destination output.txt, then reopen and display the destination. Check both copy results and output file contents.
- Even/odd: retain the supplied 1–10 sequence and printed labels; also separate the values into two files to meet the question literally.
- Inventory: retain exactly three records with int id, char name[20], float price. No invented quantity field. Bounded one-word names and validated nonnegative prices up to 1000000; native binary structure format is not a portable interchange format.
- Command line: display argc and all user arguments, treating them as strings.
- Random access: a regular 20-byte binary file demonstrates offsets and rewind, with checked failures.
- Macro: PI = 3.14, radius 5; SQR(2 + 3) = 25 demonstrates parentheses.

## Validation

`python3 scripts/tools/verify_pps_unit5.py --source-root /workspace/work/pps-unit5 --kb-root /workspace/work/pps-kb` checks source checksums/wording, 44-question coverage, numbering, marks, note citations, table shapes, answer/program references and card order. All 10 full programs and one snippet compile with `cc -std=c11 -Wall -Wextra -Werror -pedantic`; 21 executions check sample/boundary/failure results, native binary bytes, copied text and separated parity files.

Required college, BEE KB and MAC KB validators pass. Existing Unit 3, Unit 4, Mid-II, FAQ and end-semester verifiers are run unchanged. Browser review at 1440px and 390px checks all 44 dropdowns, two set-only navigation links, source disclosures, both offset subparts, inventory code, collapsed mobile contents, Back to top, card order, lack of page overflow/JS errors, existing routes and the /Pankusdesk/ base path. Screenshots remain private review artifacts.

No outstanding source ambiguity is hidden: counting conventions, binary portability and unsupported seek behavior are stated at the relevant examples.

# Chemistry Unit I — textbook wording + worked-calculation layout

Base workspace: `redo(20260909-072240).zip`, with the prior global student-facing commentary cleanup retained cumulatively.

## Changes
- Reworked Unit I prose to stay close to the supplied Jain & Jain pages while correcting awkward grammar, punctuation and obvious scanning/English issues.
- Removed explanatory/meta prose that described what the textbook/book/chapter was doing instead of simply teaching the chemistry.
- Preserved R25-first scope and existing textbook figure placeholders.
- Corrected the displayed hardness example to match **Textbook Example 4, p. 38**: temporary hardness = 150 ppm; total hardness = 350 ppm.
- Recreated Example 4's CaCO3-equivalent calculation as a semantic `<table>`.
- Added generic `section.working` rendering so each calculation step is displayed on its own row/line rather than running together inside prose.
- Added a one-column CSS override for worked-solution lines.
- Updated EDTA method text and formula relationships to follow pp. 33–35 closely.

## Verification
`python scripts/tools/verify_college.py` — PASS
`node --check scripts/new/subject-unit.js` — PASS

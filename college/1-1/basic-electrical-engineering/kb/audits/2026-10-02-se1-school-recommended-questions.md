# BEE · SE 1 school-recommended questions · 2026-10-02

## Source workspace

`redo.zip` supplied in the current task.

## School source

Handwritten SE 1 recommendation sheet supplied by Priyanka in this chat.

## Solution source

Ravish R. Singh, *Basic Electrical Engineering*, Third Edition, McGraw Hill Education (India) Private Limited, ISBN 978-93-5316-172-9. Current-task PDF SHA-256:

`b39b2d574fb52f0bd814b804f319af4b5e265b330f24d7d97ae30f03d5fc6c27`

## Changes

- Added a new **School & Exam Guidance** section to the BEE subject landing page.
- Added `school-assessments.html` as the reusable BEE destination for school-issued assessment material.
- Added `kb/data/school-assessments.json` as the structured data source.
- Added a renderer at `scripts/new/school-assessments.js` and page styling at `styles/new/pages/school-assessments.css`.
- Added the active **SE 1 · Recommended Questions** collection, grouped into PankusDesk Units 1–3 and then by the ranges/example numbers on the handwritten school sheet.
- Each question is shown as a faithful crop from the supplied Ravish R. Singh reference. The corresponding worked textbook solution is inside a closed dropdown.
- Added optimized WebP assets under `assets/school/se1-ravish-singh/`.
- Added school-assessment metadata to `subject.json` and provenance to `source-manifest.json`.

## Mapping rule

For handwritten entries that specify a page range and say “example problems,” the page lists example questions whose **Example heading begins within the stated range**. A solution that merely continues from an example whose heading is on the preceding page is not pulled in as a separate question. Where the handwritten sheet explicitly names example numbers, those numbers control the selection. The first handwritten range explicitly says “7 examples,” so Examples 1–7 are used even though Example 8 begins on printed p. 1.18.

This rule is shown on the student-facing page so it is not hidden. It can be changed if the school clarifies that a continuation-only example at the start of a range was intended.

## Verification performed

- Confirmed the supplied reference PDF title, edition, author, publisher and ISBN against its internal title/copyright pages.
- Programmatically located the textbook Example headings in the assigned page ranges.
- Generated 141 mapped question entries from the handwritten list under the mapping rule above.
- Generated 441 question/solution WebP crops from the source PDF.
- Spot-checked a Kirchhoff example crop against the source: question circuit, labels and worked solution were preserved.
- Kept the new page data-driven so later school assessment sheets can be added without another page redesign.

## Unresolved / interpretation-sensitive point

The handwritten page-range wording can be read two ways when the first listed page contains the continuation of an example that began on the previous page. The current implementation uses the explicit mapping rule above rather than silently guessing that the preceding example was assigned.

# Supplementary Drawing Practice — source and ROS audit

## Source coverage

| Supplied PDF | Pages | Production panels | Title-only pages retained in PDF |
|---|---:|---:|---|
| `mid 2 merger.pdf` | 8 | 8 | — |
| `iso_to_ortho.pdf` | 26 | 25 | 1 |
| `connecting rod and ic engine piston.pdf` | 6 | 5 | 4 |

All three originals are preserved byte-for-byte under `../notes/supplementary-practice/`, with hashes in `../notes/supplementary-practice.json` and the [ROS manifest](supplementary-practice-ros-manifest.json). Their 38 drawing panels are indexed individually under three source groups. No supplied drawing page is omitted. The two title-only slides remain in the downloadable originals. Source page links use 1-based PDF viewer page numbers.

The collection is supplementary material, not a syllabus-complete unit. No dates, syllabus units, missing solutions, example numbers or independent geometry checks are invented. Original related subviews remain combined. Some Mid 2 sheets overlap earlier uploads; these new source records do not replace earlier figures or resources.

## ROS processing

The [initial register](supplementary-practice-ros-register.md) freezes source-specific IDs: `ed-supp-mid2-p001-v01`…`p008`, `ed-supp-iso-p002-v01`…`p026`, and `ed-supp-parts-p001-v01`…`p003` plus `p005`/`p006`.

- Mid 2: complete vector-page renders at 300 dpi. Original page orientation, borders, dimensions and title blocks remain unchanged.
- Isometric-to-orthographic slides: directly extract the one complete original embedded teaching image per drawing page; use native dimensions. No OCR reconstruction or re-rendering of these raster originals.
- Machine parts: complete composed PDF pages rendered at 216 dpi so diagrams, fit/finish tables, titles, logos and source labels remain together.
- All 38 outputs are lossless WebP. No cropping, rotation, resizing, sharpening, denoising, colour adjustment, watermark removal or redraw.
- Every decoded output's RGB pixels equal its declared embedded original or full-page render. Every production file hash and figure reference is checked. Register/output sets reconcile without duplicates, missing or unexpected IDs.

Original PDFs and extracted isometric-panel originals are retained in the distribution ZIP with individual WebPs, manifest, register, audit and three contact sheets. ZIP inventory/integrity is tested. Contact sheets are review thumbnails, not production assets:

[Sheet 1](supplementary-practice-contact-1.jpg) · [Sheet 2](supplementary-practice-contact-2.jpg) · [Sheet 3](supplementary-practice-contact-3.jpg)

## Source limitations

- Mid 2 pages are sideways in the source PDF. ROS preserves the orientation; the page advises opening the original PDF for rotation/zooming.
- Some isometric scans already have cropped wording/lines, small labels, blur, coloured margins and handwritten ticks. Those limitations remain; absent details are not reconstructed.
- Several practice drawings have no supplied orthographic answer. They remain source practice panels; no generated answer is represented as supplied working.
- Repeated views/pages remain distinct source references. Dimensions, fit symbols and tolerance tables are preserved, not retyped or corrected. Geometrical correctness is not independently claimed.

## Integration

New `../supplementary-practice.html` and `../notes/supplementary-practice.json` feed the shared source-notes renderer. Its optional nested panels provide 3 source headings and 38 descriptive drawing links. The ED index gets a third resource card while both prior cards remain. Existing shared study figures, full-size links, mobile Contents behavior and example accordions are reused.

The Vercel dependency copier now includes linked `.zip` downloads, which were previously omitted from preview output. This is needed for the new collection's ROS download and also makes earlier linked ED ROS ZIPs available. No publication or deployment policy is changed.

PR #28 (Reference Drawings) was open when work began, so this change is stacked on its branch. Only the supplementary delta belongs to this PR; merge #28 first.

## Verification

- Original PDF hashes, 38 exact drawing-page references/anchors, all asset hashes and decoded-pixel comparisons: PASS.
- JSON parsing, `node --check scripts/new/source-notes.js`, Python syntax and `git diff --check`: PASS.
- Required college, BEE and MAC validators: PASS.
- Chromium 1440px/390px: 3 ED cards, 3 source headings, 38 drawing nav entries/images, original PDF page links, direct anchors, full-size links, mobile menu collapse and no horizontal page overflow: PASS.
- Simulated GitHub Pages `/Pankusdesk/`: resource links, image paths and nested-panel anchors: PASS.
- Existing Reference Drawings and Projection of Solids regressions: PASS.
- Vercel build and output dependency checks for all 38 figures, 3 PDFs and linked ED ROS ZIP downloads: PASS.
- ROS distribution ZIP integrity and inventory: PASS.

User acceptance remains separate and unchecked in the PR description.

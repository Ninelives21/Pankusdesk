# Projection of Solids — source and ROS audit

## Scope and source identity

- Supplied source: `projection_of_solids.pdf`, 29 PDF viewer pages, 5,412,801 bytes. The unchanged public copy is `../notes/projection-of-solids.pdf`.
- This is an undated slide-deck class-note resource, not a verified prescribed-textbook unit. No official syllabus, class date, unit number, missing examples or textbook edition is inferred. There is no unit publication-state promotion.
- PDF page 1 is the title slide and remains in the original PDF. Pages 2–7 contain the foundations. Pages 8–29 contain 22 supplied worked projection constructions.
- Source case labels 1, 4, 5 and 6 and the original discontinuous problem numbering are retained. Cases 2/3 and the intervening textbook problem numbers are not invented.
- All drawings come from this upload. The earlier `Textbook.pdf` is not used or changed.

## Source-to-page mapping

| PDF pages | Website section | Problems |
|---|---|---|
| 2 | Classification of solids | — |
| 3 | Prisms | — |
| 4 | Pyramids | — |
| 5 | Solids of revolution and oblique solids | — |
| 6 | Frustums and recommended labelling | — |
| 7 | Orientation of solids | — |
| 8–9 | Case 1: axis perpendicular to H.P. | 11.1, 11.2 |
| 10–15 | Case 4: axis inclined to H.P., parallel to V.P. | 11.9–11.13, 11.17 |
| 16–19 | Case 5: axis inclined to V.P., parallel to H.P. | 11.19–11.22 |
| 20–29 | Case 6: axis inclined to both planes | 11.26–11.34, 11.43 |

The complete question is transcribed in each closed shared example accordion. The supplied construction, including its intermediate views/stages, is inside. These are source drawings, not newly authored or independently re-solved answers. Multipart questions 11.1 and 11.2 have each subpart on its own line. Original embedded panels sometimes repeat the question inside the image; it is retained rather than erasing source pixels.

## ROS processing and register

- [Initial source-order register](projection-of-solids-ros-register.md): 32 stable IDs, `ed-solids-p002-v01` through `ed-solids-p029-v01`, with extra independent panels on pages 5/6.
- [Manifest](projection-of-solids-ros-manifest.json): original PDF image xrefs, dimensions, cropping coordinates, output hashes and encoding details for every asset.
- Complete embedded originals are used for 31 panels. Page 29's screenshot is cropped to `[90, 115, 990, 728]` in original image pixels to remove surrounding browser/taskbar controls. All retained pixels, the overlapping tooltip, watermark and construction labels remain unchanged.
- All 32 outputs are lossless WebP at retained native resolution. No resizing, enhancement, redraw, OCR reconstruction, label replacement or colour adjustment.
- Every output decodes and its RGB pixels equal the extracted original or declared crop exactly. IDs reconcile with the register without duplicates, missing or unexpected assets. All 32 website figure references resolve.
- Source originals are retained in the ROS ZIP beside the WebPs, JSON manifest, register and two review contact sheets. The original PDF also preserves the complete slide layout.
- [Contact sheet 1](projection-of-solids-contact-1.jpg) · [Contact sheet 2](projection-of-solids-contact-2.jpg). These are reduced review thumbnails, never production assets.

## Source limitations

- Many embedded panels are only about 400–700 pixels wide. Small labels remain as supplied; WebP does not recover absent detail. Native-size image links are provided.
- Page 29 contains a tooltip overlapping the question and a Windows activation watermark overlapping the drawing. Both remain; no attempt to reconstruct obscured text or remove the watermark.
- Some source panels have tiny marks or partial text at their edges. The original embedded bounds are retained; no missing content is synthesized.
- The source gives graphical construction stages rather than a separate prose solution for every problem. No unsupplied method steps or new correctness claims are added.

## Implementation and verification

Engineering Drawing is activated through its existing semester course record. The resource uses the common subject card, shared study figures and shared worked-example accordions. The generic `source-notes.js`/CSS are extended for data-driven undated slide notes; existing Chemistry behavior is preserved.

Agent-run checks:

- `python3 scripts/tools/verify_college.py` — PASS.
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py` — PASS.
- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py` — PASS.
- `node --check scripts/new/source-notes.js`, JSON parsing and `git diff --check` — PASS.
- `python3 scripts/tools/build_vercel.py` — PASS.
- Chromium at 1440px and 390px: semester subject link, subject dropdown, resource card, 10 contents headings/22 problem links, all 32 images decoded, all 22 accordion constructions, multipart header, original PDF response, native-size links, direct problem anchors and absence of horizontal page overflow — PASS.
- Chromium simulated GitHub Pages hostname with `/Pankusdesk/`: base path, image URLs, direct anchors and in-page navigation — PASS.
- Existing Chemistry source-notes page: grouped navigation and full-size image wrapper regression — PASS.
- All production panels reviewed against original embedded source/crop, with pixel equality for technical labels/lines. No independent geometrical re-solution is claimed.
- ROS distribution ZIP integrity tested with `ZipFile.testzip()` — PASS.

User acceptance checks belong in the PR description and remain unchecked by agent verification.

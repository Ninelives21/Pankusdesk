# PankusDesk — Raster Optimization Standard (ROS) v1.0

**Status:** Production specification and reusable master prompt  
**Applies to:** PankusDesk visual assets across BEE, MAC, Engineering Chemistry, and future subjects  
**Companion standard:** Notebook Redraw Style (NRS). **ROS does not redraw.**  
**Governing rule:** **Preserve the actual source image; trim only irrelevant surroundings; compress without damaging meaning.**

---

## 1. Full reusable master prompt — copy for a new ROS task

> **PROCESS THE SUPPLIED VISUALS USING PANKUSDESK RASTER OPTIMIZATION STANDARD (ROS v1.0).**
>
> The source document/image and the latest approved visual register are authoritative. Work from the supplied source, not from a recreated diagram, memory, a web approximation, or an older workspace. ROS is **not** NRS: do **not** redraw, trace, reimagine, reconstruct, restyle, relabel, retouch or technically correct any image. Preserve every visible academic and technical detail exactly as in the source.
>
> **Scope and order:** Identify the precise register IDs requested (or the next unprocessed IDs in frozen register order). Use the existing panel-grouping decisions; do not split a designated composite or merge separate registered visuals. Never skip an item because it is a diagram rather than a photograph. Eligible visuals include photographs, realistic illustrations, circuits, schematics, graphs, infographics, comparison tables, charts and composites.
>
> **Source extraction:** Prefer the original embedded asset from the supplied PPTX/PDF when it contains the complete selected visual. If no standalone asset exists, render/crop the original PDF/PPTX page at adequate resolution. Do not re-screenshot a low-resolution preview when the embedded asset is available. Keep the unmodified extracted source for audit/rollback.
>
> **Cropping:** Trim only irrelevant slide headings, surrounding paragraphs, page borders and unused whitespace **outside** the registered visual. Keep all image-internal titles/headings, table column headers, axis labels, legends, component labels, arrows, symbols, captions that belong to the figure, subpanels, watermarks, and meaningful margins. For a registered composite, retain its original spatial relationships and the entire grouping. If a clean crop cannot isolate one visual without clipping another, preserve the extra area or flag the case; never erase pixels belonging to a different object to produce a tidier result.
>
> **Image treatment:** Do not sharpen, denoise, upscale, recolour, brighten, increase contrast, remove watermarks, alter fonts or repair source defects under the default ROS workflow. Do not synthesize missing details. The only permitted default image changes are justified cropping and WebP encoding. If the source is already grainy or cut off, preserve that limitation and report it.
>
> **WebP:** Encode output as `.webp`. Prefer high-quality lossy WebP for photographic images; prefer lossless (or sufficiently high-quality) WebP for text, charts, diagrams and tables. Compare visually and choose legibility over maximum compression. Do not enforce an arbitrary file-size cap or resize an image merely to save bytes. Keep original colours, transparency and dimensions of the retained crop whenever practical.
>
> **Names:** Use the register's stable image ID in lowercase as the final filename: `bee-u4-p003-v01.webp`. When retaining an embedded original, distinguish it using a source suffix such as `bee-u4-p003-v01-pdf-embedded.jpeg`; when using a page crop, `bee-u5-p052-v01-pdf-crop.png`. A source suffix is **not** part of the permanent ID. Never invent or renumber an ID.
>
> **Quality gate:** Verify every actual output opens, has the correct ID, contains the full registered visual, preserves all labels/headers/watermarks and technical detail, and has not clipped any necessary content. Check especially the top and bottom of tables and every panel of grouped figures. If visual fidelity is not acceptable, change the crop or encoding—not the academic content. Flag ambiguous cases rather than claim success.
>
> **Delivery:** Return individually named WebP files in one ZIP, plus a compact contact sheet, source-to-output batch manifest, and brief notes identifying any exceptions. Validate the ZIP by opening/testing it. The contact sheet is for review only; it does not replace individual WebP files. Do not integrate into the website unless separately requested.
>
> **Register workflow:** Keep the frozen master CSV/XLSX unchanged during normal batches. The filenames themselves determine the correspondence with register IDs. At the end of the entire collection, reconcile the set of final filenames against the register once, flag missing/duplicate/unexpected IDs, and only then update register status and file data. Do not spend time regenerating the master spreadsheet after every batch.
>
> **Report accurately:** State what source was used, which IDs were processed, what was cropped, whether encoding was lossy/lossless, what checks were actually run, and any source limitations. Never claim semantic/visual verification, website integration, or complete coverage unless performed.

---

## 2. ROS versus NRS — absolute distinction

| Aspect | ROS | NRS |
|---|---|---|
| Purpose | Preserve existing pixels/content, remove irrelevant surrounds, optimize for web | Faithfully redraw source into notebook-style illustration |
| Method | Extract → crop → WebP encode → inspect | Semantic audit → redraw → inspect → optimize |
| Applies to | **Any** approved visual type, including circuits, graphs and tables | Only when the user explicitly requests an NRS redraw |
| Original colours/fonts/layout | Preserve | Can change to approved NRS visual style without changing meaning |
| Technical fidelity | Source content remains untouched | Every meaning-bearing element must be audited |
| Watermarks | **Preserve** | Separate redraw policy; not part of ROS |
| Default AI image generation | **Forbidden** | May be used under NRS verification rules |

**ROS is a processing standard, not an artistic style.** “Make this ROS” means produce a smaller, cleanly bounded copy of the supplied original, **not** a better-looking new diagram.

The decision to process **all visual categories through ROS** for a given project is valid; do not silently reclassify line diagrams as requiring NRS.

---

## 3. Non-negotiable fidelity hierarchy

1. Original source identity and complete content.
2. Exact technical and scientific meaning: topology, connectivity, axes, values, polarity, arrows, directions, switch states and spatial relationships.
3. Every label, word, table heading, equation, legend, figure identifier, watermark and subpanel.
4. Approved composition/grouping.
5. Legibility at intended web display size.
6. Accurate and useful cropping.
7. Compression savings.

**If a smaller file conflicts with any higher priority, keep the larger file.**

Never silently replace technically unusual or possibly incorrect material with what seems more conventional. Source inconsistencies may be noted separately but not edited into ROS assets.

---

## 4. What ROS may and may not do

### Default allowed operations

- Extract an image from an original PPTX or PDF without modifying its content.
- Render an original document page when the figure is native page content or the visual has multiple embedded components.
- Crop **outside** the selected visual to remove unrelated text, excessive borders or empty space.
- Separate independent panels **only if** the frozen register identifies them as distinct images.
- Preserve already-approved composite panels as **one** output image.
- Encode the retained pixels in WebP with suitable compression.
- Produce review-only contact sheets and processing manifests.
- Inspect outputs and rerun a crop or encode if information was lost.

### Not allowed in default ROS

- AI redrawing, illustration generation, re-tracing, segmentation that reconstructs the object, generative fill or invented pixels.
- Manual retyping, replacing labels, adding arrows, repairing diagrams, or changing table contents.
- Sharpening, blur reduction, denoising, contrast changes, brightness adjustments, colour normalization or upscaling.
- Watermark removal, watermark masking or cropping away an overlapping watermark if doing so removes or changes the visual.
- Cropping out essential titles, **MCB/MCCB-style column headers**, legends, scale bars, footnotes inside figures, axes or captions integral to a figure.
- Rearranging subfigures just to fill space or reduce aspect ratio.
- Replacing a source image with an internet result without an explicit separate decision.
- Making speculative scientific corrections or hiding defects in the original.
- Claiming that compression restores detail that the source lacks.

Any nondefault enhancement requires a **separately scoped, explicitly approved** task and a saved copy of the original. It must not be described as ordinary ROS.

---

## 5. Source-selection rules

### Preferred source order

1. The exact original embedded picture/object in the latest supplied PPTX/document, where complete and readily extractable.
2. The corresponding original embedded asset extracted from the supplied PDF.
3. A high-resolution, carefully bounded render of the supplied PDF/PPTX page for native/vector text/lines or multiple assembled objects.
4. The best available already-supplied raster crop when the originals cannot be extracted.

These are preferences, not a mandate to choose a blurry embedded bitmap over a clearer faithful PDF vector render. Compare the alternatives when the result matters.

Do not use OCR to reconstruct source text. Do not infer clipped content from adjacent pages. Retain the original as a separate source file, even when it is visibly poor quality.

### PDF page numbers

Use **PDF viewer page numbers (1-based)** unless a task explicitly specifies printed page numbering. An ID such as `p052` refers to PDF viewer page 52, not an inferred textbook page.

### Pre-existing source defects

Examples: grain, low resolution, watermark, compressed lettering, tiny diagrams, source crop already cutting off a wire/caption, blurred photograph. Preserve and flag. A good ROS result can still have source defects.

---

## 6. Crop standard — the most important production check

1. Find the full extent of the registered figure **before** choosing crop coordinates.
2. Inspect all four edges, not just the main object.
3. If the image includes a title, header, label or legend, decide whether it is **part of the figure** or unrelated slide text using the source and register description.
4. Preserve all figure-internal textual content, including table headings and graph legends.
5. Preserve the original relative positions of components or subpanels inside an approved composite.
6. Keep modest necessary breathing room; avoid both large empty borders and tight clipping.
7. Do not crop through arrows, terminals, callout tails, resistor symbols, end rings, poles, captions or watermarks.
8. Keep all border strokes and outer lines visible, including the top of tables and the bottom of diagrams.
9. If cropping would remove part of another registered panel, use a safer boundary, extract that panel separately without modifying source pixels, or flag the collision.
10. Compare the chosen cropped result side by side with the original page or embedded source.

**Important failure example:** On a PDF comparison table, cropping from below the first row can silently omit the two column titles. Every ROS table must include its entire header row, unless the frozen register explicitly excludes it.

### Composite image rule

The frozen register decides what forms one image; it does not matter how many photographs or subdrawings appear in the composite. Preserve all child components and their spatial relations. Examples of potentially valid composites include two UPS operating states, a graph with its accompanying circuit, multiple wiring photos arranged as one teaching panel, or paired earthing diagrams.

Do not invent a grouping because adjacent figures look related. Do not split an approved grouping to improve compression.

---

## 7. WebP encoding rules

- Use `*.webp` for web assets. WebP is supported by current mainstream browsers and works on static sites such as GitHub Pages.
- **Photographs/realistic illustrations:** start with high-quality lossy encoding (for example `quality=90` or `92`); lower only if visual comparison shows no meaningful degradation.
- **Circuit diagrams, graphs, small print and tables:** prefer lossless WebP; high-quality lossy is acceptable only when text and thin lines remain visibly intact.
- If an image contains both photographs and tiny labels, judge the **most fragile** content, not the largest area.
- Preserve transparency where applicable. Do not introduce a dark/white halo or unwanted background.
- Never upscale, downscale or resample solely to reach an arbitrary byte target.
- If WebP is no smaller than a source JPEG/PNG, record that fact; source fidelity is more important than a claimed saving. The required `.webp` file can still be supplied when requested.
- WebP lossy is **not mathematically pixel-identical** to the source. “No changes” means no intentional modifications to academic elements and no unacceptable visible encoding artifacts, not bit-for-bit equality.
- Compare at native and realistic web display sizes, especially for fine symbols and typography.

### Illustrative Python/Pillow encoding (not a compulsory toolchain)

```python
from PIL import Image

with Image.open("source_crop.png") as img:
    # Cropping, if needed, must already have been semantically checked.
    img.save("asset.webp", format="WEBP", lossless=True, method=6)

with Image.open("asset.webp") as check:
    check.load()  # Confirms the output can be decoded.
```

For a photograph, use `quality=90` or `92` and `method=6` with `lossless=False` after visual inspection. Encoding settings are starting points, not quality guarantees.

---

## 8. Naming convention and identity lock

Use the stable register identifier, converted to lowercase, as the **only** output basename.

| Role | Example |
|---|---|
| Permanent register ID | `BEE-U4-P003-V01` |
| Production WebP | `bee-u4-p003-v01.webp` |
| PDF-embedded original | `bee-u4-p003-v01-pdf-embedded.jpeg` |
| Cropped rendered source | `bee-u4-p003-v01-pdf-crop.png` |
| Optional PPTX-embedded source | `bee-u4-p003-v01-pptx-embedded.png` |

- `bee` = subject; `u4` = unit; `p003` = source PDF viewer page; `v01` = registered visual identifier on that page.
- The `-pdf-embedded`, `-pdf-crop` or `-pptx-embedded` suffix denotes source **provenance**, not a different permanent image ID.
- File extensions reflect actual formats. Do not change `.jpeg` to `.png` without converting its content.
- File names must not depend on batch numbering. A batch may be renamed without renaming the asset.
- Never create `v02` just because you re-encoded `v01`. A correction **replaces that same WebP filename** after review.
- Retain the frozen register ID even when an asset is repeated on another page; record repeated placements through the register or manifest rather than inventing a new image identity mid-batch.
- Do not quietly change old identifiers while creating a new batch.

---

## 9. Frozen register and end-of-project reconciliation

**Efficiency rule (project decision): do not regenerate the master CSV/XLSX after each batch.** The relationship between the final file and the register is already encoded in the filename.

### At the beginning

- Treat the most recently **approved frozen register** as the list and order of expected IDs.
- Confirm the requested range of IDs before production.
- Note any count discrepancies without inventing entries; do not silently switch between an old 51-entry and a different revision.
- Use the latest supplied source/archive as the content source of truth.

### During batches

- Deliver outputs named for their registered IDs.
- Maintain a small **batch manifest** and optional review/approval notes; do not repeatedly rewrite the master spreadsheet.
- Preserve the previously accepted outputs; do not silently reprocess or overwrite them in a later batch.

### Once at the end

1. Enumerate the final `.webp` filenames actually present in the assembled output directory.
2. Normalize filenames to lowercase basename (without extension) and compare to register IDs using set operations.
3. Report **missing**, **unexpected** and **duplicate** names separately.
4. Check all present files can open and correspond visually to their registered content. Filename matching alone does not verify pixels or corrections.
5. Update the CSV/XLSX once with filenames, sizes, status and provenance, if requested.
6. Keep register identity and source references stable.

**Minimal set check:**

```python
expected = {registered_id.lower() for registered_id in register_ids}
actual = {webp_path.stem.lower() for webp_path in webp_files}
missing = sorted(expected - actual)
unexpected = sorted(actual - expected)
# Duplicate names must also be checked BEFORE converting the filename list to a set.
```

The set comparison is insufficient by itself to establish visual correctness, replace earlier versions, or identify duplicate content under different names.

---

## 10. Batch sizing and throughput

- Batch size depends on complexity, not an arbitrary five-image limit.
- For routine document images, **10–15** is a reasonable reviewable batch; larger batches are possible when extraction is uniform.
- Automate extraction, encoding, naming, manifest creation and basic decode/ZIP checks.
- Only manually intervene for difficult panel boundaries, dense tables, small text, collages or unusual source-object placement.
- The batch preview/contact sheet is a fast review aid; it is not a substitute for examining any suspect technical image at sufficient zoom.
- Do not promise a speed improvement if the sources require laborious manual verification.

---

## 11. Delivery package

Prefer one ZIP per batch containing:

```text
BEE_ROS_batchNN/
  webp/
    bee-u4-p003-v01.webp
    bee-u4-p004-v01.webp
    ...
  sources/
    bee-u4-p003-v01-pdf-embedded.jpeg
    ...
  batch_manifest.csv
  preview_all.jpg
  README.md
```

The name `BEE_ROS_batchNN` is illustrative; use the task's real batch name. Source files may be omitted from a **small distribution-only pack** when separately retained and explicitly agreed. Do not imply that source files are included if they are not.

Batch manifest should contain at least:

- `image_id`
- `source_document`
- `viewer_page`
- `source_filename_or_object`
- `output_filename`
- `composition` (single or composite)
- `source_resolution` and `output_resolution`
- `encoding` (lossless or lossy plus quality if applicable)
- `output_bytes`
- `cropping_notes`
- `qa_status` / exceptions

Useful optional fields: SHA-256 checksum; original file size; visual quality flags; repeated-source identity.

### Archive checks

- Ensure each intended output exists at exactly the claimed path.
- Test decoding of every `.webp` file.
- Test ZIP integrity and list its contents before linking.
- Verify each filename matches a frozen ID and appears exactly once within the release directory.
- Check any corrected file is actually the version inside the ZIP (not an older copy).
- Keep previews clearly separate from production assets.

**Do not deliver an unverified or invented sandbox link.**

---

## 12. Final ROS QA checklist

### Scope and identity

- [ ] Correct latest source document and frozen register used.
- [ ] Every requested ID present, in the expected order.
- [ ] No arbitrary extra images, missing registered panels or silently omitted diagrams.
- [ ] Registered composite panels are complete and remain combined.
- [ ] All outputs use the exact registered basename plus `.webp`.

### Crop and visual content

- [ ] Original image/figure identified correctly before cropping.
- [ ] No meaningful content omitted at **top, bottom, left or right**.
- [ ] Table **column headings and first/last rows** fully present.
- [ ] Every graph axis, label, legend and point annotation preserved.
- [ ] Every circuit symbol, wire, arrowhead, node, value and polarity preserved.
- [ ] All photographic object parts and cutaways preserved.
- [ ] All approved composite subpanels retained in original arrangement.
- [ ] Source watermarks preserved.
- [ ] No invented, rewritten, reconstructed or corrected image content.
- [ ] No unauthorized sharpening, denoising, recolouring, resizing or watermark removal.
- [ ] Any pre-existing poor quality/clipping has been flagged honestly.

### WebP and packaging

- [ ] Each WebP decodes successfully and has sensible dimensions.
- [ ] Thin lines and small text remain legible compared with source.
- [ ] Lossy/lossless encoding choice is appropriate for each image.
- [ ] Original/source copy retained as agreed.
- [ ] Manifest accurately describes each actual output.
- [ ] ZIP can be opened and passes an integrity test.
- [ ] Download links were verified in the current runtime.
- [ ] No claim of website integration without inspecting/editing the latest workspace and testing it.

**If any information-bearing element was lost or altered by cropping or compression, reject the output and correct it before delivery.**

---

## 13. Known lessons from BEE Unit IV–V ROS production

These are workflow safeguards, not a mandate to reproduce the same source images:

1. **Selection must follow the register, not a photograph-only list.** The general power-system layout and other complex diagrams count as ROS assets even though they are not photographs.
2. **Tables need explicit top-edge checks.** A prior MCB/MCCB table crop excluded the header row; the correct fix was to recrop from the original PDF, not reconstruct the headings.
3. **Composite images reflect the user's grouping decisions.** Separate pictures may be one output when the register says so (for example a paired UPS normal-power/power-failure figure).
4. **A low-resolution source remains low-resolution.** WebP encoding preserves an appropriately compressed version but does not restore information absent from the document.
5. **Reuse filenames.** Approved fixes keep the same stable ID; do not invent new IDs for revisions.
6. **Don't maintain spreadsheet metadata after every batch.** Frozen names and a final set reconciliation are sufficient, supported by batch manifests.
7. **Filename completeness is not visual completeness.** Verify files really contain the expected headers, labels, subpanels and corrected crops.
8. **A page can contain native PDF elements rather than one embedded picture.** Rendering the page at suitable resolution and taking a faithful crop is valid ROS.
9. **No automatic web-image substitution.** The user supplied the source intentionally; preserve it rather than selecting a vaguely similar replacement.

---

## 14. Cross-subject PankusDesk implementation lock

- ROS is a **global College visual-production standard**, not a BEE-only look.
- Preserve established shared figure rendering, responsiveness, alt-text conventions and accessibility. Where a website change is explicitly requested, use the latest workspace and the shared study UI; avoid subject-specific figure components.
- The image should have technically descriptive `alt` text **in page HTML/data**, not burned into the image merely for accessibility.
- Figures remain at the correct conceptual locations. Retain internal figure/page provenance separately from student-facing captions.
- Source hierarchy is unchanged: syllabus controls scope, prescribed textbook controls canonical teaching content, and class notes remain identifiable as class material.
- ROS does not justify including out-of-scope images or material simply because they are present in a supplied archive.
- When integrating, do not replace a real HTML table with an image merely because that image is available; preserve established accessible table conventions where appropriate.

---

## 15. Short production prompt

> Use **PankusDesk ROS v1.0** on the next specified image IDs from the frozen register. Use only the latest supplied source document. Extract each original image where possible; otherwise render and crop the source page. Preserve all original pixels/meaning, colours, fonts, watermarks, figure-internal headings, table headers, axes, arrows, labels, borders and approved composite arrangements. Do **not** redraw, reconstruct, sharpen, denoise, upscale, recolour or remove watermarks. Crop only unrelated surroundings, then encode to WebP (lossless for fine text/diagrams when appropriate, high-quality lossy for photos). Verify each image at its edges and at readable zoom, retain exact stable ID filenames, and return individual WebPs in a tested ZIP with a manifest and contact sheet. Leave the master CSV/XLSX frozen; reconcile filenames and update it **once at the end**. Report only checks genuinely performed and flag original-source defects.

---

## 16. Task template

```text
PROCESS THESE IMAGES IN PANKUSDESK ROS v1.0

Source document / archive: [latest supplied file]
Frozen image register: [latest approved register]
Images: [ID range or exact IDs]
Previously completed images: [reference if relevant]

Requirements:
- Strictly preserve source content and watermarks.
- Crop unrelated surroundings only; keep all meaningful labels and headers.
- Preserve registered composite groups.
- WebP compression only; no redraw or other visual enhancement.
- Use exact registered IDs as filenames.
- Provide WebP files + manifest + review contact sheet in verified ZIP.
- No updates to the master CSV/XLSX during the batch.
- Flag source defects or unclear crop boundaries; never invent missing content.
- Do not integrate into PankusDesk unless explicitly instructed.
```

**One-line rule:** **ROS = ORIGINAL SOURCE + SAFE CROP + WEBP COMPRESSION + VERIFIED FIDELITY.**

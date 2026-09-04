# Notebook Redraw Style — NRS v1.1 (Design Lock v2)

## Purpose

Notebook Redraw Style converts textbook figures, lecture screenshots and handwritten class-note visuals into one consistent, compact study-visual language for PankusDesk/PadhaiSpace.

The governing rule is:

> **Preserve the information; normalize the presentation.**

A redraw is a faithful semantic restatement. It is not permission to add theory, “improve” scientific meaning or substitute what the model expects for what the source actually shows.

---

## 1. Visual character

The output should feel like a very neat engineering/science notebook:

- white or subtly warm off-white paper;
- faint blue horizontal ruling when appropriate;
- subtle pink/red left margin when composition allows;
- deep-blue pen-style drawing lines;
- tidy but recognisably hand-drawn appearance;
- compact, study-friendly composition;
- calm visual hierarchy;
- technical precision.

It should **not** look like a printed textbook, PowerPoint graphic, corporate infographic, clip art, cartoon or decorative AI illustration.

---

## 2. Single-handwriting rule — absolute

**Every visible piece of text uses one handwriting-style visual language.**

This includes:

- figure number;
- figure title/caption;
- component/node labels;
- axis labels;
- equations;
- variable/subscript labels;
- annotations;
- headings;
- legends;
- subfigure labels;
- any user-approved brief explanation inside the image.

Do not mix handwritten labels with serif/sans-serif textbook print. Variation in size/weight is allowed; variation in font personality is not.

---

## 3. Fidelity hierarchy

When aesthetics conflict with information, use this order:

1. **electrical/scientific correctness — explicitly verified**;
2. exact source meaning;
3. labels/equations/topology/directions;
4. figure identity/number/title;
5. readability;
6. compactness;
7. aesthetics.

Never sacrifice 1–4 for 5–7.

---

## 4. Mandatory Semantic Verification Gate — new absolute safeguard

For any technical, scientific, engineering, mathematical, circuit, field, graph or direction-sensitive redraw, **do not generate immediately**.

### Before drawing

1. Identify what each visual region actually is: circuit, graph, characteristic, field diagram, classification tree, mechanical sketch, etc.
2. Inspect every meaning-bearing detail.
3. State the critical details in words.
4. Wait for user confirmation when a detail is ambiguous or when the user has asked for confirmation first. If the exact detail was explicitly confirmed in the immediately preceding turn, do not ask again.
5. If something materially changes the science and cannot be read confidently, **stop and ask**. Never infer it merely because a conventional diagram would usually look that way.

The semantic audit must cover all relevant items:

- arrow direction: left/right/up/down;
- circulation: clockwise/anticlockwise;
- current direction;
- voltage polarity;
- dot/cross conventions (`⊙` out of page / `⊗` into page) when applicable;
- source orientation;
- node/branch connectivity;
- open/closed/short/disconnected states;
- graph identity, axes, direction, slope, intercepts and constant lines;
- front/behind/through/around relationships;
- whether a loop wraps around or sits behind a conductor;
- symbol identity (`I_1` vs `I_s`, `R_s` vs `R`, etc.);
- equations/signs/subscripts;
- meaningful counts: loops, turns, arrows, terminals, nodes, panels or repeated elements.

### Redundant direction description

For direction-sensitive figures, record directions in more than one way when useful.

Example:

- **anticlockwise** = top arrows point **left** + bottom arrows point **right**;
- **clockwise** = top arrows point **right** + bottom arrows point **left**.

This redundancy is deliberate: it prevents a generated image from using the correct word while drawing inconsistent arrowheads.

### After drawing

1. Inspect the actual generated output, not merely the prompt.
2. Compare it against the pre-draw semantic audit.
3. If even one meaning-bearing detail is wrong, reject/regenerate the redraw.
4. Do not claim QA passed if the output was not actually checked.

> **A wrong arrow, graph axis, polarity, dot/cross symbol, connection, orientation, variable or spatial relationship is not a cosmetic defect. It is a technically incorrect figure.**

---

## 5. Source fidelity

Preserve every meaningful source feature:

- topology/connectivity;
- component identity;
- terminals/nodes;
- arrows;
- polarities;
- graph axes/relationships;
- variable names/subscripts;
- equations/numerical values;
- subfigures/panels;
- figure number;
- exact source caption/title when supplied.

Small spacing/alignment changes are allowed only to improve clarity without changing meaning.

### Source image vs reference cue

The **actual requested source image is authoritative**.

A textbook or online reference may be used to understand a standard symbol or clean up geometry **only after the source meaning is understood**. Never redraw the textbook/reference instead of the supplied class-note image. Never overwrite a class-note convention because general BEE knowledge suggests a different one.

---

## 6. No-hallucination rule

Do not:

- add components;
- add theory unless the user explicitly asks for a brief explanatory addition;
- infer unreadable labels;
- replace unusual source notation with “better” notation;
- change source relationships;
- silently correct a source figure;
- merge unrelated figures;
- create a contact sheet when one standalone redraw was requested.

If the user explicitly requests an added label or very brief explanation, that approved addition may be included while leaving the source semantics unchanged.

---

## 7. Circuit diagrams

Connectivity is sacred.

Preserve exactly:

- open circuits;
- short circuits;
- node dots/open terminals;
- source orientation;
- current arrows;
- voltage polarity;
- branch topology;
- component values;
- internal/parallel/series relationships;
- labels.

Moving a component slightly for balance is acceptable. Reconnecting it is never acceptable.

---

## 8. Graphs and characteristics

First explicitly identify that a region is a **graph** before drawing it.

Preserve:

- x/y variables;
- axis direction;
- zero/origin if shown;
- constant lines;
- slope direction;
- marked levels/intercepts;
- ideal vs practical lines;
- relation between graph and companion circuit.

Do not mistake notebook ruling or nearby circuit leads for graph data, and do not import a textbook graph when the class-note graph is the requested source.

---

## 9. Field/flux/direction diagrams

For magnetic/electric field visuals:

- count loops/arrowheads when meaningful;
- verify each arrowhead direction;
- verify dot/cross conventions;
- verify resultant/coil axes;
- verify conductor/current direction;
- verify whether loops surround, cross, pass behind or pass through a conductor.

Do not rely on a generic “right-hand rule” assumption if the source drawing is readable.

---

## 10. Block diagrams and classification maps

### Block diagrams

- preserve input/output direction;
- preserve labels;
- preserve flow order;
- use compact hand-drawn blocks.

### Classification trees/mind maps

- preserve parent-child hierarchy exactly;
- preserve spelling/abbreviations after ambiguity is resolved;
- do not reclassify from general knowledge;
- clean alignment/spacing only.

---

## 11. Multi-panel and combined class figures

Keep subfigures together when the source treats them as one conceptual figure.

Two separate class-note sketches may be combined into one NRS asset **only when**:

- they clearly form one concept (for example source symbol + characteristic), and
- the intended combination is understood/approved.

Do not combine unrelated figures for convenience.

---

## 12. Caption and label rule

If a textbook source supplies a figure number/title, reproduce it faithfully in handwriting style.

For a class-note redraw without a source caption, a concise descriptive title may be created if useful, e.g.:

- `Ideal voltage source and its V–I characteristic`
- `Practical current source and I–V characteristic`

Do not invent an academic claim in the caption.

---

## 13. Mathematical notation

Technical clarity outranks decorative handwriting.

Subscripts and symbols must remain unmistakable, e.g.:

- `R_Th`
- `V_Th`
- `R_L`
- `I_1`
- `I_s`
- `R_s`
- `G_m`

Never mutate one variable into another because handwriting is aesthetically easier.

If the source is ambiguous (`I_1` vs `I_s`, etc.), verify before generating.

---

## 14. Composition

- center/balance the content;
- minimize unused margins;
- do not crop meaningful labels;
- avoid oversized whitespace;
- keep labels readable at normal web size;
- use the smallest practical canvas that preserves clarity;
- preserve the source's logical left/right or top/bottom relationship.

---

## 15. Textbook vs lecture vs class-note redraws

### Textbook figure

Near-facsimile semantic redraw: exact figure identity, labels, topology, values and caption.

### Lecture screenshot

Preserve the lecturer's visible academic content; remove video/player/background clutter. Do not silently improve theory.

### Handwritten class note

Preserve the student's/lecturer's information while allowing stronger spatial cleanup. Normalize handwriting into NRS. User-confirmed readings override model guesses.

---

## 16. Web asset naming and folders

Short stable filenames:

- `f1-1.png`
- `f1-16.png`
- `f1-50a.png`
- `c1.png`

Filename = identity. Alt text/caption = meaning.

Folders:

- textbook theory: `assets/book/uN/theory/`
- textbook questions/examples: `assets/book/uN/examples/`
- dated class redraws: `assets/class/YYYY-MM-DD/figures/`

---

## 17. Accessibility

Every web-embedded figure requires descriptive alt text **outside the pixels**.

Good alt text explains the technical visual.

Bad alt text:

- “image”;
- “figure”;
- filename only;
- figure number alone.

---

## 18. PNG optimization

Preferred pipeline:

**source crop → semantic audit → NRS redraw → semantic QA → full-resolution PNG → indexed PNG optimization → website asset**

Default ImageMagick optimization:

```bash
magick input.png \
  -strip \
  -colors 64 \
  -define png:compression-level=9 \
  "PNG8:output.png"
```

Practical target: roughly ~100 KB/image on average, not a hard cap. Use 128 colours if needed. Never damage labels/details to hit an arbitrary byte target.

---

## 19. Batch workflow

1. Establish exact source identities/order and target filenames.
2. Perform a semantic audit for each technical figure.
3. Resolve ambiguities before generation.
4. Redraw each source independently unless an approved conceptual combination is intended.
5. Inspect each actual output against its audit.
6. Reject changed arrows, labels, topology, polarity, axes, symbols or spatial relationships.
7. Compress only after acceptance.
8. Restore exact target filename.
9. Place into the correct production asset folder.
10. Prepare descriptive alt text.

---

## 20. Final QA checklist

Before accepting any redraw:

- [ ] Is this actually the requested source figure/concept?
- [ ] Did I correctly distinguish circuit vs graph vs other visual regions?
- [ ] Was the semantic audit performed before generation?
- [ ] Are all arrow directions/circulations correct?
- [ ] Are current directions and polarities correct?
- [ ] Are dot/cross conventions correct where present?
- [ ] Are all circuit connections/branches/source orientations identical?
- [ ] Are front/behind/through/around relationships correct?
- [ ] Are meaningful counts correct?
- [ ] Are graph axes, slope/intercepts/constant lines faithful?
- [ ] Are all labels, subscripts and numerical values correct?
- [ ] Are equations copied accurately?
- [ ] Is the figure number correct where applicable?
- [ ] Is the title/caption correct where applicable?
- [ ] Is every visible text element in one handwriting style?
- [ ] Is there any accidental textbook/print font?
- [ ] Is there any unapproved added content?
- [ ] Is it compact without being cramped?
- [ ] Will labels remain readable on the website?
- [ ] Is descriptive external alt text prepared?

**Any failure in a meaning-bearing item is an automatic rejection. No “close enough”.**

---

## 21. Short reusable production instruction

> Redraw this in Notebook Redraw Style (NRS v1.1). The supplied source is authoritative. Before generating, identify and verify every meaning-bearing technical detail—what is a circuit/graph, axes, arrow directions, polarity, dot/cross convention, connectivity, source orientation, spatial relationships, labels/subscripts and meaningful counts. Ask if any material detail is ambiguous. Then redraw faithfully on a compact ruled notebook page with tidy blue-ink lines and one consistent handwriting style for all visible text. Do not add, infer, correct or replace academic content unless explicitly approved. After generation, inspect the actual image against the semantic audit and reject any technically incorrect output.

## Cross-subject implementation lock

Notebook redraws are a common College component, not a subject skin. The visual language defined here applies unchanged to BEE, MAC and future subjects/semesters. Baseline figure rendering must flow through the shared study UI (`PankuStudyUI.renderFigure()` / `styles/new/study-ui.css`); subject-specific code may control placement and dimensions only. Do not introduce a MAC-specific, BEE-specific or semester-specific redraw style.

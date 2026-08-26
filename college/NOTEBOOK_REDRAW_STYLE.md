# Notebook Redraw Style (NRS v1.0)

## Purpose

Notebook Redraw Style converts textbook figures, lecture screenshots, and handwritten class-note visuals into one consistent, compact study-visual language for PankusDesk/PadhaiSpace.

The governing rule is:

> **Preserve the information; normalize the presentation.**

A redraw is a faithful visual restatement, not an opportunity to add theory or redesign the underlying science.

## 1. Visual character

The output should feel like a very neat engineering/science notebook:

- white or subtly warm off-white paper
- faint blue horizontal ruling where appropriate
- subtle pink/red left margin when composition allows
- deep-blue pen-style drawing lines
- tidy, hand-drawn appearance
- compact, study-friendly spacing
- technically precise while retaining notebook character

It should not look like a printed textbook, PowerPoint graphic, corporate infographic, clip art, or decorative AI illustration.

## 2. Single-handwriting rule — mandatory

**Every visible piece of text must use the same handwriting-style visual language.**

This includes:

- figure number
- figure title/caption
- component labels
- node labels
- axis labels
- equations
- variables/subscripts
- annotations
- headings
- legends
- subfigure labels

Do not mix handwritten labels with serif/sans-serif textbook print. Do not switch the caption to normal typeset text.

Variation in size/weight is allowed; variation in font personality is not.

## 3. Source fidelity

Preserve every meaningful source feature:

- topology/connectivity
- component identity
- terminal and node positions where logically relevant
- arrow directions
- polarity signs
- graph axes and relationships
- variable names
- equations
- numerical labels
- subfigures/panels
- figure number
- exact source caption/title when supplied

Small spacing/alignment changes are allowed only to improve clarity without changing meaning.

## 4. No-hallucination rule

Do not:

- add components
- add theory
- infer missing labels
- replace unusual source notation with “better” notation
- change source relationships
- silently correct a source figure
- merge unrelated figures
- create a contact sheet when one standalone redraw was requested

If something cannot be read confidently, stop/flag it rather than invent it.

## 5. Fidelity priority

When visual attractiveness conflicts with accuracy, use this order:

1. scientific/electrical correctness
2. exact source meaning
3. labels/equations/topology
4. figure identity/number/title
5. readability
6. compactness
7. aesthetics

Never sacrifice 1–4 for 5–7.

## 6. Circuit diagrams

Connectivity is sacred.

Preserve exactly:

- open circuits
- short circuits
- node dots/open terminals
- source orientation
- current arrows
- voltage polarity
- branch topology
- component values
- labels

Moving a component slightly for balance is acceptable; reconnecting it is not.

## 7. Graphs/characteristics

Preserve:

- axis variables
- axis direction
- constant lines
- slopes
- marked levels/intercepts
- relationship between graph and companion circuit

Remove scan clutter/whitespace, not mathematical meaning.

## 8. Block diagrams and classification maps

For block diagrams:

- use clean hand-drawn blocks
- preserve input/output direction and labels
- preserve flow order

For classification trees/mind maps:

- preserve parent-child hierarchy exactly
- use compact, tidy branches
- do not reclassify content from general knowledge

## 9. Multi-panel figures

Keep subfigures together when the source treats them as one conceptual figure (for example `(a)` and `(b)` within one figure).

Keep separately numbered/used figures separate when they occur at distinct explanation steps.

## 10. Caption rule

If the source supplies a caption/title, reproduce that figure number and title faithfully in the redraw.

Do not editorialize or rewrite a textbook caption into a different academic phrase merely because it sounds better.

The caption must use the same handwriting style as all other visible text.

## 11. Mathematical notation

Technical clarity outranks decorative handwriting.

Ensure subscripts and symbols remain distinguishable, for example:

- `R_Th`
- `V_Th`
- `R_L`
- `I_1`, `I_2`
- `G_m`

Never allow a redraw to mutate one variable into another.

## 12. Composition

- keep content centered and balanced
- minimize unused margins
- do not crop meaningful labels
- avoid oversized whitespace
- keep labels readable at normal web display size
- use the smallest practical canvas that preserves clarity

## 13. Textbook vs lecture vs class-note redraws

### Textbook figures

Use near-facsimile semantic fidelity: exact figure identity, labels, topology, values, and caption.

### Lecture screenshots

Preserve the lecturer's actual visible academic content; remove video/player/background clutter. Do not silently “improve” the theory.

### Handwritten class notes

Preserve information faithfully while allowing stronger spatial cleanup. The source handwriting itself does not need to be copied; normalize it into NRS handwriting.

## 14. Web asset naming

Use short stable filenames based on the figure identity, for example:

- `f1-1.png`
- `f1-16.png`
- `f1-50a.png`

Filename carries identity; alt text/caption carry meaning.

Do not put long descriptions into filenames.

## 15. Asset folders

Textbook theory:

`assets/book/uN/theory/`

Textbook questions/examples:

`assets/book/uN/examples/`

Class-derived visuals should remain in a separate class asset path.

## 16. Accessibility

Every web-embedded figure requires descriptive alt text outside the pixels.

Good alt text explains the technical visual, for example:

> Circuit for finding Thevenin voltage with the load removed, showing R1, R2 and R3 and zero current through R2.

Bad alt text:

- “image”
- “figure”
- “f1-53”
- “Figure 1.53” alone

## 17. PNG optimization workflow

Preferred production pipeline:

**source crop → NRS redraw → full-resolution PNG → indexed PNG optimization → website asset**

Default ImageMagick optimization:

```bash
magick input.png \
  -strip \
  -colors 64 \
  -define png:compression-level=9 \
  "PNG8:output.png"
```

Practical target: roughly ~100 KB per image on average, not a hard cap.

If 64 colours visibly reduces quality, use 128 colours. Do not shrink important technical detail merely to satisfy a byte target.

## 18. Batch workflow

For a batch:

1. establish exact source identities and target filenames first
2. preserve verified source order
3. redraw each source independently
4. visually compare source vs redraw
5. reject outputs with changed labels/topology
6. compress only after redraw acceptance
7. restore exact target filename
8. place in the correct production asset folder

## 19. QA checklist

Before accepting a redraw:

- [ ] Same figure/concept as the source
- [ ] Circuit/scientific topology unchanged
- [ ] All arrows and polarities correct
- [ ] All labels/numerical values present
- [ ] Equations copied accurately
- [ ] Figure number correct
- [ ] Figure title/caption correct
- [ ] Every visible text element uses one consistent handwriting style
- [ ] No accidental textbook/print font appears
- [ ] No invented content
- [ ] Compact without becoming cramped
- [ ] Readable at normal website size
- [ ] Descriptive external alt text prepared for web embedding

If any accuracy/font-fidelity item fails, redraw before accepting.

## 20. Reusable production instruction

A short production prompt may be:

> Redraw this in Notebook Redraw Style. Strict source fidelity. Preserve every meaningful label, value, arrow, polarity, connection, subfigure, figure number and exact source title. Use a clean ruled notebook background and blue-ink hand-drawn lines. **All visible text must use one consistent handwriting-style font/look, including the caption.** Do not add, infer, correct, or hallucinate academic content. Produce one standalone compact redraw.

**Master Prompt — Notebook Redraw Style**

Use this when redrawing textbook figures, class-note sketches, lecture screenshots, mind maps, concept diagrams, circuit diagrams, block diagrams, graphs, or worked examples into the “Notebook Redraw Style”.

**Full reusable prompt**

**Prompt:**

Redraw the provided reference image in **Notebook Redraw Style**.

**1) Core goal**

Create a **clean, compact, visually neat redraw** of the source figure while preserving the **content, meaning, structure, labels, equations, arrows, figure number, and title/caption** exactly as shown in the reference. The output should look like a **beautifully organized hand-drawn class notebook diagram**, not like a printed textbook figure and not like a polished vector infographic.

**2) Style definition: Notebook Redraw Style**

The redraw must have the following appearance:

- A **clean notebook / class-notes aesthetic**
- Light or subtle **white/off-white notebook paper** background
- Prefer **faint ruled lines** when appropriate, especially for note-like diagrams
- Drawing lines should look like they were made by a **steady blue pen**
- **Blue ink is the default NRS normalization even when the source drawing itself is black, grey, pencil, or another neutral ink colour.** Preserve a source colour only when that colour itself carries technical meaning or is required to distinguish information.
- Diagram strokes should **not** look mechanically ruler-straight or CAD-perfect. Use a **subtle natural freehand wobble / organic unevenness**, as if a careful student drew the figure by hand with a pen.
- The freehand character must remain restrained: **neat and technically exact, not messy, shaky, distorted, or imprecise**.
- The overall look should be **hand-drawn but tidy**
- Keep it neat, legible, and structured
- It should feel like a **very good student’s notebook**
- Maintain a **compact layout** so it saves space and is practical for study notes
- The redraw should be clearer than the original, but it must still feel like notes, not formal publishing art

**3) Text/font rule — very important**

**All text in the image must use the same handwriting-style font or handwritten look.**

This includes:

- figure number
- figure title / caption
- all labels
- axis labels
- current/voltage labels
- node labels
- component names
- equations
- annotations
- arrows with text
- section names
- legend text
- any note text

Do **not** mix in printed textbook fonts, serif fonts, or normal document fonts.

Do **not** use a typeset textbook caption style.

Everything textual should look like it belongs to the same notebook page and was written by the same person.

**4) Fidelity to source**

Preserve the source faithfully.

- Keep the **same concept and same diagram meaning**
- Preserve the **same figure number and figure title** if present
- Preserve the **same ordering** if multiple images are being redrawn in a set
- Preserve **all important symbols, arrows, terminals, polarities, labels, and relationships**
- Preserve **all equations and variable names exactly**
- Preserve **all subfigures / panels** if present
- If the source has multiple parts side by side, redraw them in the same logical arrangement
- If the source has a graph or V-I characteristic, reproduce it faithfully
- If the source has circuit elements, preserve their proper arrangement and connectivity
- If the source has a block diagram, preserve the blocks and flow arrows faithfully
- If the source has a classification tree / mind map / hierarchy, preserve the parent-child structure faithfully

**5) No hallucination rule**

Do **not** invent extra content.

- Do not add new theory
- Do not add extra components
- Do not add extra arrows or labels
- Do not change relationships
- Do not “improve” by altering the meaning
- If something is unclear, keep it minimal and faithful rather than making up missing content

**6) Clean-up rule**

Improve clarity without changing content.

- Straighten and organize the **overall layout**, but do not turn individual notebook strokes into perfectly ruler-straight/CAD-like lines
- Preserve a slight natural hand-drawn line character while keeping topology and geometry unambiguous
- Improve spacing
- Align text neatly
- Make arrow directions clear
- Make symbols clean and readable
- Avoid clutter
- Reduce unnecessary empty space
- Make the image practical for insertion into study notes or a knowledge-base page

**7) Rendering guidance by diagram type**

**If it is a circuit diagram:**

- Draw standard circuit symbols clearly
- Preserve source labels exactly
- Show polarities, current directions, node names, and component names clearly
- If there is a corresponding graph, place it neatly beside or below the circuit as in the source
- Use the notebook style consistently across both the circuit and the graph

**If it is a graph / characteristic:**

- Draw axes cleanly
- Label axes in handwriting style
- Preserve plotted relationships faithfully
- Keep graph lines neat and clear
- Preserve all marked operating levels or constant lines shown in the source

**If it is a block diagram:**

- Use neat hand-drawn rectangular blocks
- Preserve input/output arrows and labels
- Keep the layout balanced and centered
- Maintain the logical flow direction of the original

**If it is a classification chart / concept tree / mind map:**

- Preserve hierarchy exactly
- Use simple connecting lines or branches
- Keep the layout compact and readable
- Make it look like an organized notebook mind map

**If it is a worked example or multi-stage process:**

- Preserve step order
- Preserve all intermediate diagrams
- Keep the sequence visually clear
- If the source has sub-parts like (a), (b), (c), keep them explicit

**8) Caption and figure numbering**

If the original has a figure number and title/caption, include it clearly in notebook style.

Examples:

- “Figure 1.16 Equivalent Circuit and V-I Characteristics of Voltage Controlled Current Source”
- “Figure 1.51 Thevenin’s equivalent Circuit”

These should appear as part of the notebook redraw, still in the same handwritten style as everything else.

**9) Composition and spacing**

- Keep the figure centered and balanced
- Avoid huge margins
- Avoid excessive whitespace
- Make the drawing slightly compact so it is easy to embed in notes pages
- Ensure nothing important is cut off
- Make all text readable at normal web size

**10) Color and visual restraint**

- Primary drawing color: **blue-ink notebook style**
- **Use blue ink even if the original source is drawn in black, grey, pencil, or another neutral colour.** NRS normalizes neutral source ink to blue.
- Exception: if the source uses colour to encode technical meaning, preserve the necessary distinctions rather than flattening them blindly.
- Background: white or off-white
- Keep the palette minimal
- No decorative colors unless the source genuinely requires distinction
- Prefer subtle, study-note realism over flashy styling

**11) Output intent**

The final image should feel like:

- a clean notebook redraw
- handmade but precise
- naturally hand-drawn, with subtle freehand line variation rather than sterile CAD-perfect strokes
- study-friendly
- space-efficient
- faithful to the original
- visually consistent across an entire series of figures

**12) Special instruction for a set of related figures**

If multiple figures are being redrawn as part of the same chapter or unit:

- keep the **same notebook style across all images**
- keep **the same handwriting style font**
- keep **the same line quality**
- keep **consistent caption treatment**
- keep **consistent page background and visual language**

The set should look like it came from the same notebook.

**Shorter “production version”**

If you want a tighter reusable prompt:

**Prompt:**

Redraw the provided source image in **Notebook Redraw Style**. Preserve the original content faithfully: the same figure number, title/caption, labels, equations, arrows, structure, relationships, and ordering. The result should look like a neat, compact, hand-drawn class notebook diagram on a clean white/off-white notebook page, preferably with faint ruled lines where appropriate, using tidy blue-ink lines. **Use blue ink even when the original source uses black, grey, pencil, or another neutral ink colour, unless colour itself carries technical meaning.** Diagram strokes should retain a **subtle natural freehand wobble / organic unevenness** rather than looking perfectly ruler-straight or CAD-generated; keep this effect restrained so the figure remains neat and technically exact. **Very important: every bit of text must use the same handwriting-style font/look** — captions, labels, axis text, annotations, equations, and figure titles. Do not use printed textbook fonts anywhere. Improve neatness, alignment, spacing, and readability, but do not hallucinate or change the meaning. Keep it compact, study-friendly, and visually consistent with a notebook-based knowledge base.

**Optional add-on instructions**

You can append one or more of these when needed:

**A) For strict fidelity**

Do not simplify away any important labels, arrows, symbols, or sub-parts. If present in the source, keep them.

**B) For chapter-figure consistency**

Match the exact same Notebook Redraw Style used in previous figures from this chapter.

**C) For very compact output**

Keep the figure tightly composed with minimal blank space so it embeds efficiently in study pages.

**D) For note integration**

Make the result feel like it belongs inside a student notebook or knowledge-base page, not a textbook scan.

**One rule to remember especially**

If I had to state the most important correction from today:

**Notebook Redraw Style must never mix fonts. Everything textual should look handwritten by the same person.**

If you want, I can next give you:

1. a **diagram-redraw prompt template with placeholders**, or
2. a **PadhaiSpace house-style specification sheet** based on this.



\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



**Copy this whenever you give me a new figure:**



REDRAW THIS IN NOTEBOOK REDRAW STYLE

Source:

[attached image / figure]

Identity:

\- Target filename: [f1-51 / lecture-02-fig-03 / etc.]

\- Figure number: [Figure 1.51]

\- Figure title: [exact title from source]

Instructions:

1\. Faithfully reproduce the supplied source only.

2\. Preserve every meaningful:

   - circuit connection

   - component

   - node

   - arrow direction

   - polarity

   - variable

   - equation

   - label

   - graph

   - subfigure

   - figure number

   - caption/title.

3\. DO NOT add, infer, correct or invent academic content.

4\. Keep the original logical arrangement unless a small spacing change improves readability without changing meaning.

5\. Redraw in clean Notebook Redraw Style:

   - white/off-white notebook-paper background

   - faint blue horizontal ruling

   - subtle red/pink left margin where composition allows

   - blue handwritten pen-style diagram lines

   - use blue ink even if the source itself is black, grey, pencil, or another neutral ink colour, unless colour carries technical meaning

   - tidy but visibly hand-drawn appearance

   - subtle natural freehand wobble / organic unevenness in wires, branches, boxes and other drawn strokes; do not make them sterile, perfectly ruler-straight or CAD-like

   - the freehand effect must remain restrained so topology, arrow direction, polarity and geometry stay technically exact

   - compact, study-friendly composition.

6\. CRITICAL FONT RULE:

   Every visible piece of text must use ONE consistent handwriting-style appearance.

   This includes:

   - figure title

   - figure number

   - component labels

   - equations

   - axis labels

   - annotations

   - node labels

   - headings

   - captions.

   Never switch to textbook serif, sans-serif print, or typeset caption fonts.

7\. Keep mathematical subscripts/symbols unambiguous:

   R₁, R₂, RTh, VTh, RL, I₁, I₂, etc.

8\. The figure number and exact source title must be visible in the completed redraw whenever they are present in the source.

9\. Use minimal colours; **blue ink is the default even when the original source uses black, grey, pencil, or another neutral ink colour**. Preserve another colour only when it carries technical meaning.

10\. Do not create a contact sheet or combine this with unrelated figures.

11\. Produce one standalone redraw for this source figure.



\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**PankusDesk / PadhaiSpace Visual House Style**

I’d call the formal standard:

**Notebook Redraw Style — NRS v1.0**

**Purpose**

NRS converts heterogeneous source visuals—textbook scans, lecture screenshots and handwritten classroom diagrams—into one coherent visual language for study materials.

It is **not** a reinterpretation system.

The governing principle is:

**Preserve the information; normalize the presentation.**

**Visual character**

Every redraw should feel like a carefully maintained engineering/science notebook:

clean

\+ handwritten

\+ technically precise

\+ compact

\+ calm

\+ consistent

It should **not** resemble:

a textbook typesetting job

a PowerPoint graphic

a corporate infographic

clip art

a cartoon

an AI illustration

**Paper**

Preferred background:

- warm white/off-white rather than stark digital white;
- very faint blue horizontal notebook ruling;
- optional subtle pink/red vertical margin;
- background should never compete with the technical material.

The page texture should be extremely restrained. We want the *impression* of notebook paper rather than a realistic photograph of paper.

**Ink**

Primary content:

**deep blue notebook ink**

This is a normalization rule, not a request to imitate the source medium. If the original is black ink, grey pencil, or another neutral monochrome, redraw it in deep blue NRS ink. Preserve non-blue colour only when the colour itself communicates technical information or a required distinction.

This includes:

- wires
- arrows
- circuit symbols
- boxes
- graphs
- text
- equations
- labels.

Secondary accent colours should be used only when there is a meaningful reason.

We should not decorate textbook figures merely because colour is available.

**Hand-drawn line character — absolute NRS rule**

NRS should look like a **careful human redraw in a notebook**, not a vector/CAD export.

Default line character:

- use a **subtle natural freehand wobble / organic unevenness** in wires, branches, arrows, boxes, axes, circuit outlines and other drawn strokes;
- avoid perfectly ruler-straight, mathematically sterile linework unless exact straightness itself is meaning-bearing;
- keep the wobble **small and controlled**—the drawing should look confidently hand-drawn, not shaky or messy;
- resistor symbols, source symbols, arrows and other technical symbols may be cleaned for legibility, but they should still belong to the same hand-drawn visual language;
- overall alignment and spacing may be improved substantially, while individual strokes retain a slight human character.

This visual imperfection is **stylistic only**. It must never alter:

- topology;
- connectivity;
- arrow direction;
- polarity;
- node placement/identity;
- source orientation;
- component values;
- graph meaning;
- equations;
- labels;
- meaningful geometry.

**Style = gently hand-drawn. Semantics = exact.**

If visual neatness conflicts with semantic precision, semantic precision wins.

**Typography**

This is now an absolute NRS rule:

**One handwritten visual language across the entire image.**

Never mix:

- handwriting labels + printed caption;
- handwritten equations + serif title;
- handwritten circuit + computer-typeset annotation.

The same handwriting family should cover:

Figure 1.53

Finding Thevenin’s voltage

R₁

R₂

VTh

I₂ = 0

a

b

Differences in size/weight are fine.

Differences in **font personality** are not.

**Mathematical notation**

Technical accuracy beats visual prettiness.

Subscripts must remain unmistakable.

Prefer visually:

VTh

RTh

RL

I1

I2

with proper subscript-like treatment where the renderer handles it reliably.

Never allow an artistic rewrite to mutate:

R₁ → Rl

VTh → Vₕ

Gm → Cm

or similar.

If the source notation is unusual, preserve it rather than silently standardizing it.

**Circuit-diagram rules**

Connectivity is sacred.

Moving objects for better spacing is allowed.

Changing which nodes are connected is **never** allowed.

Preserve:

- open circuits;
- short circuits;
- node dots;
- terminal circles;
- polarity;
- source orientation;
- current direction;
- resistor placement;
- branch topology.

For example, in a superposition diagram:

voltage source suppressed → short circuit

current source suppressed → open circuit

must be visually represented exactly as the supplied source does it.

Do not infer suppression states from theory if the source itself depicts something else; follow the supplied figure.





**Mandatory Semantic Verification Gate — NRS v1.1**

For any technical, scientific, engineering, mathematical, circuit, field, graph, or direction-sensitive Notebook Redraw, **do not generate the image immediately**.

**Before drawing:**

1. Inspect the source specifically for every **meaning-bearing visual detail**.
2. State those critical details in words and **wait for user confirmation before generating**, unless the user has already explicitly confirmed those exact details in the immediately preceding turn.
3. The semantic audit must include every relevant item:
   - arrow direction and circulation: clockwise / anticlockwise / left / right / up / down;
   - current and voltage directions;
   - polarity;
   - dot/cross conventions such as ⊙ = out of page and ⊗ = into page;
   - source orientation;
   - node connectivity and branch topology;
   - open / closed / short-circuit states;
   - graph slope, intercepts and constant lines;
   - axis identity and direction;
   - front / behind / through / around geometry;
   - whether one element wraps around, passes through, crosses or sits behind another;
   - labels, subscripts, symbols and equation signs;
   - meaningful counts such as number of loops, turns, arrows, terminals, nodes or panels.
4. If any meaning-bearing detail is unclear, **stop and ask**. Never infer it merely because a convention seems likely.
5. For direction-sensitive figures, describe the direction **redundantly** whenever possible. For example:
    **Anticlockwise = top arrows point left + bottom arrows point right.**
    **Clockwise = top arrows point right + bottom arrows point left.**

This redundancy is deliberate. It prevents an image generator from satisfying the word “anticlockwise” while putting individual arrowheads in inconsistent directions.

**After drawing:**

1. Compare the generated image against the semantic audit before accepting it.
2. Check the actual visible output—not merely whether the generation instruction contained the correct directions.
3. If even **one meaning-bearing detail** is wrong, reject the redraw and regenerate it.

**A wrong arrow, polarity, dot/cross symbol, connection, orientation, or spatial relationship is not a cosmetic defect. It is a technically incorrect figure and therefore a failed redraw.**

**Updated NRS priority**

Your existing fidelity hierarchy should remain, but I would sharpen the first item to:

1. **Electrical/scientific correctness — verified before and after generation**
2. Exact source meaning
3. Labels/equations
4. Figure identity
5. Readability
6. Compactness
7. Visual prettiness

**Never sacrifice 1–4 for 5–7.**

**Add to the final QA checklist**

Before accepting a technical redraw:

- □ Did we perform the semantic audit **before generation**?
- □ Are clockwise/anticlockwise directions actually correct?
- □ Are individual arrowheads pointing in the correct directions?
- □ Are current directions and polarities correct?
- □ Are ⊙/⊗, +/−, and similar symbols correct?
- □ Are circuit connections and source orientations identical?
- □ Are **around / through / in front of / behind** relationships correct?
- □ Are meaningful counts correct: turns, loops, arrows, terminals, nodes, panels?
- □ Are graph axes, slopes and constant lines faithful?
- □ Are labels and equations exact?
- □ Is the figure number/title exact?
- □ Is the Notebook Redraw visual style consistent?

**Any failure in a meaning-bearing item = automatic rejection. No “close enough.”**

And I’d add this beside your existing “one handwriting style” rule as the second absolute NRS rule:

**Never generate a technical Notebook Redraw until its meaning-bearing details have been explicitly understood in words; never accept the redraw until those same details have been checked against the generated image.**



**Mandatory Blue-Ink + Natural Hand-Drawn Line Rule — NRS v1.2**

This is now the latest global NRS visual rule and overrides any older interpretation that could produce black/grey redraws or sterile CAD-perfect linework.

For every NRS redraw:

1. **Use deep blue notebook ink by default**, even when the supplied source is black ink, grey pencil, or another neutral monochrome.
2. Preserve another colour only when that colour itself carries technical meaning or is required to distinguish information.
3. Draw wires, branches, axes, arrows, boxes, circuit outlines and similar strokes with a **slight natural freehand wobble / organic unevenness**.
4. Do **not** make ordinary notebook strokes perfectly ruler-straight, mechanically uniform, vector-perfect or CAD-like.
5. Keep the freehand character restrained and confident. The image should look like it was drawn carefully by a good student, not deliberately distressed or made messy.
6. Improving overall alignment, spacing and composition is still encouraged. “Clean up the drawing” means organize it—not sterilize its line character.
7. The hand-drawn effect is never allowed to change a meaning-bearing detail. Connectivity, arrowheads, polarity, topology, source orientation, labels, values, geometry and equations remain exact.
8. When the source itself is rough, NRS may clean and normalize the geometry while retaining **human-looking blue pen strokes**.

**Absolute shorthand: BLUE INK + GENTLE HUMAN WOBBLE + EXACT SEMANTICS.**



**Graph rules**

Preserve:

- X/Y variables;
- arrow directions;
- constant lines;
- slope direction;
- intercepts if shown;
- corresponding circuit labels.

Graphs need not preserve meaningless scan whitespace.

They **must** preserve their mathematical meaning.

**Multi-panel figures**

If the source contains:

(a) ...

(b) ...

retain them as a single redraw when the textbook treats them as one figure.

Example:

Figure 1.45

(a) Star Network

(b) Delta Network

should remain one asset.

But figures such as:

1.50

1.50(a)

1.50(b)

1.50(c)

remain separate assets because they occur separately within the explanation.

**Captions**

If the source says:

Figure 1.53 Finding Thevenin’s voltage

the redraw should say that.

Don't editorialize it into:

Calculation of Open Circuit Thevenin Voltage

even if that sounds better.

For a textbook redraw, **the textbook owns the caption**.

For a newly created class-note redraw without a source caption, we may create a concise descriptive title—but that is a different case.

**Fidelity hierarchy**

When aesthetics conflict with information, use this priority:

1\. Electrical/scientific correctness

2\. Exact source meaning

3\. Labels/equations

4\. Figure identity

5\. Readability

6\. Compactness

7\. Visual prettiness

Never sacrifice items 1–4 to improve 5–7.

**What may be improved**

Allowed:

- straightening/organizing crooked **overall scan geometry and layout**, while retaining subtle natural freehand line character in the redraw;
- centering;
- balanced spacing;
- legibility;
- consistent resistor symbols;
- cleaner arrows;
- removing scan artefacts;
- removing irrelevant white borders;
- making a cramped source less cramped;
- making an excessively spread-out source more compact.

Not allowed:

- changing notation;
- changing circuit topology;
- adding explanation;
- adding equations;
- replacing labels with more conventional ones;
- silently repairing something merely because it appears strange.

**Textbook versus lecture/class redraws**

Same visual language, slightly different fidelity treatment.

**Textbook**

**Near-facsimile semantic redraw.**

Preserve:

- exact figure number;
- exact title;
- exact labels;
- exact topology.

**Lecture screenshot**

Preserve the lecturer's actual visual content, while removing video/player/background clutter.

No improvement of the underlying lecture theory unless separately requested.

**Handwritten class note**

Preserve the student's/lecturer's original information, but allow substantial spatial cleanup.

The original notebook handwriting itself does **not** need to be mimicked. It gets normalized into NRS handwriting.

**Web asset standard**

Our current practical pipeline should be:

source crop

    ↓

Notebook Redraw Style

    ↓

full-resolution PNG

    ↓

ImageMagick palette optimization

    ↓

web asset

Default optimization target:

magick input.png \\

  -strip \\

  -colors 64 \\

  -define png\:compression-level=9 \\

  "PNG8\:output.png"

Expected practical target:

**roughly \~100 KB/image on average**, not a hard limit.

If a diagram needs it, use 128 colours rather than damaging readability.

Do **not** resize simply to meet an arbitrary byte target.

**Filenames**

Keep files short and machine-friendly.

Textbook examples:

f1-1.png

f1-16.png

f1-45.png

f1-50a.png

f1-55.png

Filename = identity.

Caption/alt text = meaning.

Don't stuff descriptions into filenames.

**Accessibility**

Every figure embedded in PankusDesk/PadhaiSpace gets descriptive alt text maintained **outside the image itself**, e.g.:

\<img

  src="f1-53.png"

  alt="Circuit for finding Thevenin voltage with the load removed, showing R1, R2 and R3 and zero current through R2."

\>

The alt text should explain the visual.

It should not merely say:

Figure 1.53

**Batch-processing rule**

For a batch:

1. establish exact filenames first;
2. preserve input order;
3. redraw each source independently;
4. never generate a composite/contact sheet instead;
5. visually verify each output;
6. reject any output with changed labels/connectivity;
7. compress only after the redraw is accepted;
8. restore the intended filename;
9. place it into the corresponding asset directory.

**Final NRS QA checklist**

Before accepting any redraw, ask:

□ Is this actually the same figure?

□ Are all circuit connections identical?

□ Are every arrow and polarity correct?

□ Are all labels present?

□ Are equations copied correctly?

□ Is the figure number correct?

□ Is the title/caption exact?

□ Is every bit of text handwritten in ONE consistent style?

□ Is there any accidental textbook-print font?

□ Is the redraw in deep blue NRS ink even if the neutral-colour source was black/grey/pencil, unless colour itself was technically meaningful?

□ Do the drawn strokes retain a subtle, controlled hand-drawn wobble rather than looking sterile/CAD-perfect?

□ Did the redraw add anything not in the source?

□ Is it compact without being cramped?

□ Will small labels still be readable on the website?

If any of the first **nine** fails, the redraw should be redone rather than accepted.

That gives us a proper, reusable **NRS v1.0 specification**—not just a look we happen to like. And the new single-handwriting-font rule is part of the standard from this point onward.

The later **NRS v1.1 Semantic Verification Gate** and **NRS v1.2 Blue-Ink + Natural Hand-Drawn Line Rule** are cumulative updates to this master specification. Where an older wording can be read as conflicting with a later rule, **the latest rule governs**.



\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
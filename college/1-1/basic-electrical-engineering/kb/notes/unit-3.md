# Unit 3 — Transformers and DC Machines

> **Source-lock:** Every statement below is derived from the supplied/approved source corpus. R25 defines what is core. Items marked *Supporting* are preserved because they were supplied but are not separate R25 syllabus atoms.

## Transformer principle and construction

**Status:** Core R25

- The prescribed text defines a transformer as a static machine that changes voltage level without changing frequency and transfers energy through magnetic coupling between circuits.
- Its working principle is electromagnetic induction: AC in the primary produces alternating core flux that links the secondary and induces emf. The source explicitly states that a transformer does not work on DC because DC does not produce alternating flux.
- The basic construction described includes primary and secondary copper windings, a laminated silicon-steel core, transformer oil for cooling/insulation, radiators and bushings.

### Physical-book reference
- pp. 130–132; source image(s): 130.png–132.png; figures: 3.1–3.4

**Provenance:** `[SYL-R25-U3]` `[TB-P130]` `[TB-P131]` `[TB-P132]`

## Transformer EMF equation and transformation ratio

**Status:** Supporting

- For sinusoidal core flux, the textbook derives RMS induced emf proportional to frequency, turns and maximum flux.
- With winding drops neglected, the voltage ratio follows the turns ratio; the book uses this to classify step-up, step-down and unit transformers.

### Formula / method anchors
- `E1 = 4.44 f N1 Φm`
- `E2 = 4.44 f N2 Φm`
- `k = N2/N1 = E2/E1 ≈ V2/V1 (ideal/neglected-drop treatment)`

### Physical-book reference
- pp. 133–137; source image(s): 133.png–137.png

**Provenance:** `[TB-P133]` `[TB-P134]` `[TB-P135]` `[TB-P136]` `[TB-P137]`

## Practical transformer on no-load

**Status:** Supporting

- The practical transformer takes a small no-load current even with secondary open. The book resolves it into a magnetising component that establishes flux and an iron-loss component that supplies core losses.
- This no-load model is one step toward the practical equivalent circuit.

### Formula / method anchors
- `Im = I0 sinφ0`
- `Iw = I0 cosφ0`

### Physical-book reference
- pp. 137–139; source image(s): 137.png–139.png; figures: 3.7–3.10

**Provenance:** `[TB-P137]` `[TB-P138]` `[TB-P139]`

## Ideal/practical transformer and equivalent circuit

**Status:** Core R25

- The ideal transformer assumptions in the source remove winding resistance, leakage, magnetic reluctance and losses; the practical transformer includes these effects.
- The book develops an equivalent circuit using winding resistance/reactance and the shunt magnetising/iron-loss branch, and shows how impedances are referred across the turns ratio.

### Physical-book reference
- pp. 139–143; source image(s): 139.png–143.png

**Provenance:** `[SYL-R25-U3]` `[TB-P139]` `[TB-P140]` `[TB-P141]` `[TB-P142]` `[TB-P143]`

## Transformer voltage regulation

**Status:** Core R25

- The text relates the loaded secondary terminal voltage to the induced secondary emf and internal equivalent impedance drop.
- Voltage regulation is presented as the change from no-load to loaded secondary voltage; the approximate drop uses resistance and reactance components, with a sign change for the leading-power-factor reactance term. The book notes that leading loads can produce negative regulation.

### Formula / method anchors
- `As printed: %VR = (E2 − V2)/E2 × 100`
- `Approx. lagging drop ∝ I2(R02 cosφ + X02 sinφ)`
- `Approx. leading drop ∝ I2(R02 cosφ − X02 sinφ)`

### Physical-book reference
- pp. 144–148; source image(s): 144.png–148.png

### Source caution
- Use the textbook’s regulation denominator/convention when answering from this KB; do not silently replace it with another convention.

**Provenance:** `[SYL-R25-U3]` `[TB-P144]` `[TB-P145]` `[TB-P146]` `[TB-P147]` `[TB-P148]`

## Transformer losses and efficiency

**Status:** Core R25

- The textbook divides losses into winding/copper loss and iron/core loss. Copper loss varies with load current squared; core loss is treated as approximately constant with load in the presented analysis.
- Efficiency is output/input. The source states the maximum-efficiency condition as variable copper loss equal to constant loss.

### Formula / method anchors
- `Copper loss ∝ I²`
- `η = output/input × 100`
- `Maximum efficiency condition (source treatment): copper loss = constant/core loss`

### Physical-book reference
- pp. 149–157; source image(s): 149.png–157.png

**Provenance:** `[SYL-R25-U3]` `[TB-P149]` `[TB-P150]` `[TB-P151]` `[TB-P152]` `[TB-P153]` `[TB-P154]` `[TB-P155]` `[TB-P156]` `[TB-P157]`

## DC machine construction, generator principle and EMF equation

**Status:** Core R25

- The book introduces the DC machine as an electromechanical energy converter and describes the generator principle using electromagnetic induction and Fleming’s right-hand rule.
- Constructional material covers the major magnetic/electrical parts before deriving the generated-emf equation and classifying generators by excitation.

### Formula / method anchors
- `Eg = Φ Z N P / (60 A)`
- `For wave winding A = 2; for lap winding A = P (as presented)`

### Physical-book reference
- pp. 158–170; source image(s): 158.png–170.png

**Provenance:** `[SYL-R25-U3]` `[TB-P158]` `[TB-P159]` `[TB-P160]` `[TB-P161]` `[TB-P162]` `[TB-P163]` `[TB-P164]` `[TB-P165]` `[TB-P166]` `[TB-P167]` `[TB-P168]` `[TB-P169]` `[TB-P170]`

## DC motor principle and back EMF

**Status:** Core R25

- The motor principle in the book is force on a current-carrying conductor in a magnetic field, with direction given by Fleming’s left-hand rule.
- As the armature rotates it also generates an emf opposing the applied supply; the source calls this back emf and uses it in the motor voltage balance.

### Formula / method anchors
- `Force relation shown: F = BIl`
- `Motor voltage balance: V = Eb + IaRa (with brush drop added where considered)`
- `Generated/back-emf form uses Eg = ΦZNP/(60A)`

### Physical-book reference
- pp. 171–177; source image(s): 171.png–177.png

**Provenance:** `[SYL-R25-U3]` `[TB-P171]` `[TB-P172]` `[TB-P173]` `[TB-P174]` `[TB-P175]` `[TB-P176]` `[TB-P177]`

## Load characteristics and speed control of separately excited DC motor

**Status:** Core R25

- For the separately excited motor, the textbook presents torque versus armature current, speed versus armature current and speed versus torque characteristics.
- With field flux treated as constant, developed torque is proportional to armature current. The speed relation shows control through armature voltage/resistance effects and field flux; the text presents field control and armature-voltage control.

### Formula / method anchors
- `T ∝ ΦIa; with constant Φ, T ∝ Ia`
- `N ∝ (V − IaRa)/Φ`

### Physical-book reference
- pp. 178–184; source image(s): 178.png–184.png

**Provenance:** `[SYL-R25-U3]` `[TB-P178]` `[TB-P179]` `[TB-P180]` `[TB-P181]` `[TB-P182]` `[TB-P183]` `[TB-P184]`

## Swinburne’s test

**Status:** Core R25 · gap-filled

- R25 explicitly requires Swinburne’s test, but the prescribed textbook chapter captured at pp.130–185 does not contain a Swinburne section. This subsection is therefore gap-filled, not inferred from the book.
- The selected NPTEL Electrical Machines-I course identifies Lecture 89 as “Swinburne Test”. A tightly scoped institutional BEEE lab-manual cross-check describes it as a no-load test used to predetermine efficiency of a DC shunt machine as motor/generator.
- The cross-check procedure records supply voltage, no-load line current and field current at rated speed. From these, no-load armature current and armature copper loss are obtained; the remainder of no-load input is treated as constant loss for the efficiency calculation sequence.

### Formula / method anchors
- `Iao = IL0 − If`
- `No-load armature copper loss = Iao²Ra`
- `Constant loss = no-load input − no-load armature copper loss`
- `Motor efficiency = (input − total losses)/input`
- `Generator efficiency = output/(output + total losses)`

### Source caution
- Gap content is intentionally limited to what the selected NPTEL lecture identification and institutional lab-manual cross-check support.

**Provenance:** `[SYL-R25-U3]` `[GAP-U3-SWINBURNE-NPTEL]` `[GAP-U3-SWINBURNE-IARE-BEE-LAB]`

## Question-bank pointer

Book review/short-answer/essay material: pp.184–185.

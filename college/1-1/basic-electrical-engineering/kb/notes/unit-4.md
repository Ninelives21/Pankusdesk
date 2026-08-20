# Unit 4 — Alternating Current Machines

> **Source-lock:** Every statement below is derived from the supplied/approved source corpus. R25 defines what is core. Items marked *Supporting* are preserved because they were supplied but are not separate R25 syllabus atoms.

## Three-phase induction motor types and construction

**Status:** Core R25

- The textbook separates the machine into stator and rotor and gives two rotor forms: phase-wound/slip-ring and squirrel-cage.
- The phase-wound rotor permits external rotor resistance through slip rings during starting; the squirrel-cage rotor uses bars shorted by end rings and is presented as the robust running construction.

### Physical-book reference
- pp. 186–188; source image(s): 186.png–188.png

**Provenance:** `[SYL-R25-U4]` `[TB-P186]` `[TB-P187]` `[TB-P188]`

## Three-phase induction motor principle, slip and rotor frequency

**Status:** Core R25

- A balanced three-phase stator supply produces a rotating magnetic field. The textbook gives its synchronous speed from supply frequency and pole count.
- Relative motion between that rotating field and the rotor induces rotor emf/current; their interaction produces torque. The rotor cannot reach synchronous speed in motoring operation because zero relative speed would remove induced rotor emf/current and torque.
- The text defines slip from the difference between synchronous and rotor speed and gives rotor-current frequency proportional to slip.

### Formula / method anchors
- `Ns = 120f/P`
- `s = (Ns − N)/Ns`
- `fr = s f`

### Physical-book reference
- pp. 188–194; source image(s): 188.png–194.png

**Provenance:** `[SYL-R25-U4]` `[TB-P188]` `[TB-P189]` `[TB-P190]` `[TB-P191]` `[TB-P192]` `[TB-P193]` `[TB-P194]`

## Torque-slip characteristics

**Status:** Core R25

- The textbook gives a torque-slip expression with rotor resistance in the numerator and resistance/reactance terms in the denominator.
- From that expression it describes the low-slip region where torque is approximately proportional to slip, the high-slip region where torque is approximately inversely proportional to slip, and the maximum-torque condition.

### Formula / method anchors
- `T ∝ sR2 / (R2² + (sX2)²) (source proportional form)`
- `Low slip: T ∝ s`
- `High slip: T ∝ 1/s`
- `Maximum torque condition: s = R2/X2`

### Physical-book reference
- pp. 195–197; source image(s): 195.png–197.png

**Provenance:** `[SYL-R25-U4]` `[TB-P195]` `[TB-P196]` `[TB-P197]`

## Working principle of synchronous generator

**Status:** Core R25

- The textbook presents a synchronous generator as a machine converting mechanical input to AC electrical output by electromagnetic induction.
- Its field system is on the rotor and the armature is on the stator in the presented construction. Rotation of the rotor field produces alternating induced emf in the stator windings.
- The generated frequency is tied to rotor speed and pole count.

### Formula / method anchors
- `f = PNs/120`
- `Per-phase induced emf shown: E = 4.44 Φ f N`

### Physical-book reference
- pp. 197–199; source image(s): 197.png–199.png

**Provenance:** `[SYL-R25-U4]` `[TB-P197]` `[TB-P198]` `[TB-P199]`

## Synchronous-generator voltage regulation by synchronous impedance method

**Status:** Core R25 · gap-filled

- This R25 item is absent from the captured prescribed-book section and is filled only from the approved gap package.
- The BIET lab source defines the open-circuit characteristic (OCC) as terminal/generated voltage versus field excitation at rated speed with no load, and the short-circuit characteristic (SCC) as armature current versus field excitation under symmetrical three-phase short circuit.
- For a chosen excitation, the source obtains synchronous impedance from open-circuit voltage divided by short-circuit current. It then derives synchronous reactance using armature resistance and uses the resulting synchronous impedance in the EMF/synchronous-impedance regulation calculation. IARE independently labels the EMF method as the synchronous impedance method.

### Formula / method anchors
- `Zs = Voc/Isc (for the same field excitation, per the BIET source)`
- `Xs = √(Zs² − Ra²)`
- `Regulation = (E0 − V)/V × 100 (conceptual EMF-method form; use the source’s phasor/sign convention for a numerical problem)`

### Source caution
- BIET OCR notation around the regulation equation is imperfect. For numerical PYQs, consult the original gap PDF/figure before committing to a sign/phasor expression.

**Provenance:** `[SYL-R25-U4]` `[GAP-U4-SYNC-REACTANCE-NPTEL]` `[GAP-U4-OCSC-NPTEL]` `[GAP-U4-SYNC-IMPEDANCE-BIET]` `[GAP-U4-SYNC-IMPEDANCE-IARE]`

## Principle of operation of synchronous motor

**Status:** Core R25 · gap-filled

- This R25 item is not covered in the captured textbook pages and is therefore gap-filled.
- The selected NPTEL material uses a DC-excited rotor to establish rotor magnetic poles and AC stator windings to establish a rotating magnetic field. Electromagnetic torque acts so that the rotor field follows the rotating stator field.
- In steady synchronous operation the rotor turns at the speed of the rotating field; that speed relationship is why it is called a synchronous machine.

### Source caution
- Phasor and power-expression material from NPTEL Lecture 82 is deliberately not promoted into R25 core because the syllabus asks only for the operating principle.

**Provenance:** `[SYL-R25-U4]` `[GAP-U4-SYNC-MOTOR-NPTEL]` `[GAP-U4-SYNC-MOTOR-NPTEL-ARCHIVE]`

## Stepper motor principle and applications

**Status:** Core R25

- The textbook describes a stepper motor as rotating in discrete equal angular steps rather than continuously. Its variable-reluctance example energises stator phase groups in sequence so rotor teeth repeatedly align with the minimum-reluctance position.
- In the worked description, sequential excitation moves the rotor through 30° steps; the exact example is an illustration, not a universal step angle.
- Applications listed include scanners, printers/3D printers, plotters, slot machines, CD drives, intelligent lighting, camera lenses, CNC machines, laser/optics actuators and fluid-control systems.

### Physical-book reference
- pp. 199–200; source image(s): 199.png + 200_01.png (Unit-IV scan)

**Provenance:** `[SYL-R25-U4]` `[TB-P199]` `[TB-P200]`

## Question-bank pointer

Unit-IV questions are mixed into Chapter-4 end matter on pp.217–218; use only induction/synchronous-generator/stepper items as Unit-IV core.

# Unit 1 — Introduction to Electrical Energy and DC Circuits

> **R25 cumulative study note.** The live study page is driven by `kb/data/topics.json`. It consolidates the supplied prescribed textbook, lecture transcripts, supplementary material, official R25 specification and dated class notes. Dated class records remain separately preserved in the class log; only useful non-duplicative material is absorbed here.

## 1. Electrical energy in modern life and engineering

**Status:** Core R25

Electrical energy is produced by converting an available form of energy, transmitted and distributed to the place of use, and finally converted by the load into the required useful effect. Generation, transmission, distribution and utilisation together form the basic energy path of an electrical power system.

### Quick recall

- Electrical energy is widely used because it is convenient, controllable, economical, clean at the point of use and easy to transmit.
- Electrical power reaches users through the chain generation → transmission → distribution → utilisation.
- For an IT student, electrical energy is the physical foundation beneath computers, communication equipment, data infrastructure and electrically driven systems.

### Why electrical energy is used so widely

- Convenience: electrical energy can be converted readily into light, heat, cooling and mechanical motion.
- Control and flexibility: electrical equipment can be started, stopped and regulated conveniently.
- Economy: electricity is suitable for domestic, commercial and industrial use and can be supplied efficiently to many kinds of loads.
- Clean point of use: unlike direct combustion at the load, electrical utilisation does not itself produce smoke, fumes or poisonous gases.
- Transmission: electrical energy can be generated at one location and carried over distance to the place where it is required.

### Role in everyday life and engineering

Modern life depends on electrical energy at almost every level. Homes and commercial buildings use it for lighting, fans, heating and cooling, refrigeration, appliances, computers and office equipment. Industry uses it for motor drives, process equipment, lighting, computing and building services.

Transport and communication also depend on electricity: electric trains and battery vehicles use electrical energy directly, while radio, television and other communication systems require electrical power. Medical and scientific equipment such as X-ray and ECG systems are further examples of electrically powered applications.

### Electrical foundations of computing and IT systems

A computer is an electrical/electronic system before it is a programming platform. Its processor, memory, storage, display, networking equipment and power supply all depend on electrical energy. The same is true for servers, network infrastructure, laboratories and the machines that support an IT workplace.

Computing systems therefore depend on the same electrical foundations as other engineered systems: sources provide energy, voltages and currents describe electrical conditions, circuit elements determine electrical behaviour, and power systems deliver the energy required by the equipment.

### From generation to utilisation

Electrical power generation is an energy-conversion process: the input may be heat, chemical, solar, wind or mechanical energy, but the output of the generating system is electrical energy. In a conventional mechanical-generation system, the machine that supplies mechanical input to the generator is called the prime mover. The generator then converts that mechanical input into electrical energy.

Generation is only the first stage. Generating stations are often located where the energy resource is available rather than where the load is concentrated, so the generated power must be transmitted toward load centres, distributed to individual consumers, and finally utilised by the connected loads. Together, generation, transmission, distribution and utilisation form the electrical power system.

- Generation: converts an available form of energy into electrical energy.
- Prime mover: supplies the mechanical energy needed to drive a generator in the conventional mechanical-generation route.
- Transmission: carries bulk electrical power from generating stations toward load centres.
- Distribution: delivers power from the transmission system to individual consumers and loads.
- Utilisation: converts electrical energy into the required useful effect — light, heat, motion, computing, communication and so on.
- Motor and generator are inverse energy-conversion examples: motor — electrical → mechanical; generator — mechanical → electrical.

*Figure: Fig. 1.1 · Electrical energy generation*

*Figure: Fig. 1.2 · Electrical power system*

### Check yourself

- **Why is electrical energy used so widely?**  
  It is convenient to convert into useful forms, easy to control, economical for many kinds of loads, clean at the point of use, and can be transmitted from the place of generation to the place of utilisation.
- **What is the basic chain from electrical-energy production to use?**  
  Generation → transmission → distribution → utilisation. A generator converts another form of energy into electrical energy; the final load converts electrical energy into the required useful effect.

### Physical-book reference

- **pp. 1–3** · source image(s): `01.png–03.png` — role of electrical energy; CSE relevance; generation/transmission/utilisation

### Textbook practice pointer

- p. 70 · 2-mark · Q1–Q2 · anchor `u1-sa-01`
- p. 71 · 6-mark · Q1–Q2 · anchor `u1-es-01`

---

## 2. Circuit concept, current, voltage and basic electrical quantities

**Status:** Core R25

Circuit theory describes interconnected electrical elements in terms of charge, current, voltage, energy and power. A clear distinction between a network and a circuit, together with consistent current directions and voltage polarities, provides the foundation for analysing electrical circuits.

### Quick recall

- A network is an interconnection of two or more circuit elements; a circuit is a network in which a closed path exists for current.
- Current is rate of flow of charge: i = dq/dt. Voltage is energy transferred per unit charge between two points: v = dw/dq.
- Reference directions and polarities are choices. A negative solved value means the actual direction/polarity is opposite to the chosen reference.

### Network and circuit — know the distinction

A circuit is built by interconnecting electrical elements such as a source, load, switch and connecting wires. For current to circulate continuously, the arrangement must provide a closed conducting path. The source transfers electrical energy to the load, and the load converts that energy into another useful form such as heat, light or mechanical output.

An electrical network is the broader idea: it is simply an interconnection of two or more electrical elements and need not contain a closed path through every element. A circuit is therefore a network with at least one closed path. Every circuit is a network, but a network need not be a circuit.

### DC and AC circuits

A DC circuit carries direct current, whose reference direction does not alternate with time. An AC circuit carries alternating current, whose magnitude and direction vary periodically with time.

DC networks may contain series, parallel or series-parallel combinations of loads and circuit elements. Their behaviour is determined from the element laws together with the way the elements are interconnected.

### Element, terminal, node and loop

- Circuit element: a component represented through terminal voltage-current relationships. A two-terminal element has two terminals through which current may enter or leave.
- Terminal: a connection point of an element. Voltage is measured between a pair of terminals.
- Node: the interconnection of two or more elements. A continuous ideal wire is treated as one equipotential node even if it is drawn over a large area of the page.
- Loop: a closed path that begins at a node, passes through circuit elements and returns to the starting node.
- A basic circuit contains a source, a load, a controlling switch and connecting wires.

*Figure: Fig. 1.3 · Basic circuit schematic*

### Classification of network elements

Network elements may be classified as active or passive. Sources are active elements, while R, L and C are commonly grouped as passive elements in introductory circuit analysis. Other useful classifications are linear/non-linear, unilateral/bilateral, time-variant/time-invariant, and lumped/distributed.

*Figure: Classification of network elements*

### Charge: the quantity behind current

Electric charge is a fundamental property of matter. Protons carry positive charge, electrons carry negative charge, and neutrons are electrically neutral. The SI unit of charge is the coulomb (C).

Current is defined from charge, so it helps to think of charge as the quantity being transported and current as the rate at which that quantity crosses a chosen cross-section.

### Current: charge in motion

Electric current is the rate at which electric charge crosses a chosen surface or flows through a conductor. For a steady transfer of charge Q over a time interval T, I = Q/T. In the general time-varying case, i = dq/dt. One ampere is one coulomb per second.

Circuit analysis normally ignores the microscopic distribution of moving charge across the wire and works with the total current in each branch. This is one of the simplifications that makes circuit theory much easier than a full electromagnetic-field calculation.

- Conventional current is defined in the direction in which positive charge would move.
- In metallic conductors the mobile charges are electrons, so electron motion is opposite to conventional-current direction.
- A current marked A→B as +1 A is exactly the same physical current as −1 A marked B→A. Direction arrows are reference choices.

### Electrical potential and potential difference

Electrical potential is measured relative to a reference. Absolute potential may use infinity as the reference, whereas circuit analysis normally uses the potential difference between two points. Potential difference is the work or energy transferred per unit positive test charge in moving between those points.

For a finite or steady energy transfer, V = W/Q. In differential form, voltage is v = dw/dq. One volt means one joule of energy per coulomb of charge. Because voltage is always referenced between points, its sign depends on the chosen polarity: if A is 5 V above B, then V_AB = +5 V and V_BA = −5 V.

A negative calculated voltage is therefore not automatically an error; it indicates that the actual polarity is opposite to the reference polarity chosen at the start.

### Energy and power

Energy is the capacity to do work and may exist in electrical, mechanical, thermal and other forms. Its SI unit is the joule (J). In a circuit, electrical energy is transferred from sources to elements and loads, where it may be dissipated, stored or converted into another form.

Power tells us how fast that energy transfer is taking place. Average power over an interval is P = W/t. Instantaneous power is p = dw/dt, and with the passive sign convention it becomes p = vi. The SI unit of power is the watt (W), equal to one joule per second.

For a passive element, positive p means the element is absorbing electrical power. The sign depends on the selected voltage/current references, so draw the polarity and current arrow before interpreting power.

### Electrical, magnetic and mechanical analogy

A useful analogy connects electrical, magnetic and mechanical systems: EMF drives current against electrical resistance; magnetomotive force (MMF) drives magnetic flux against reluctance; mechanical torque drives speed against friction. The analogy becomes useful later in transformers and electrical machines.

Magnetomotive force (MMF) is the driving quantity of a magnetic circuit. For a coil of N turns carrying current I, MMF = NI.

*Figure: Fig. 1.4 · Analogy between electrical, magnetic and mechanical systems*

### Check yourself

- **What is the difference between an electrical network and an electrical circuit?**  
  A network is an interconnection of two or more electrical elements and need not contain a closed conducting path. A circuit is a network with at least one closed path. Therefore every circuit is a network, but every network need not be a circuit.
- **What do 1 ampere and 1 volt mean in base electrical terms?**  
  1 ampere means 1 coulomb of charge crossing a section per second. 1 volt means 1 joule of energy transferred per coulomb of charge.
- **What is magnetomotive force (MMF)?**  
  Magnetomotive force is the driving quantity of a magnetic circuit. For a coil of N turns carrying current I, MMF = NI.

### Formula / method sheet

- `Charge unit: coulomb (C)`
- `Steady current: I = Q/T`
- `Time-varying current: i = dq/dt`
- `1 A = 1 C/s`
- `Steady voltage: V = W/Q`
- `Time-varying voltage: v = dw/dq`
- `1 V = 1 J/C`
- `Average power: P = W/t`
- `Instantaneous power: p = vi = dw/dt`
- `1 W = 1 J/s`
- `MMF (coil): NI`

### Important notes

- Do not confuse electron-flow direction with conventional-current direction.
- Voltage is between two points; always keep the chosen +/− reference visible when solving a circuit.
- The terms active and passive are used with more than one convention in introductory electrical engineering. In common circuit-analysis classification, sources are active and R, L and C are passive; physically, R dissipates energy while ideal L and C store energy.

### Class history

- [24 Aug 2026 · Circuit concept and basic quantities](college/1-1/basic-electrical-engineering/class-log.html?date=2026-08-24)

### Physical-book reference

- **pp. 4** · source image(s): `04.png` — electric circuit and basic circuit schematic

### Textbook practice pointer

- p. 70 · 2-mark · Q3–Q4 · anchor `u1-sa-03`

---

## 3. R, L and C parameters

**Status:** Core R25

The behaviour of most introductory circuit elements is built from three basic parameters: resistance R, inductance L and capacitance C. A resistor dissipates electrical energy as heat, while ideal inductors and capacitors store energy in magnetic and electric fields respectively; their voltage-current relations determine how they respond in a circuit.

### Quick recall

- R dissipates energy, L stores energy in a magnetic field, and C stores energy in an electric field.
- The ideal element laws are v = Ri, v = L·di/dt and i = C·dv/dt.
- In steady DC an ideal inductor behaves as a short circuit and an ideal capacitor as an open circuit; inductor current and capacitor voltage cannot jump instantaneously under finite excitation.

### Resistance and Ohm’s law

Resistance is the property of a material or element that opposes current. For a linear resistor, voltage drop is proportional to current at a given temperature: v = Ri. The proportionality constant R is resistance, measured in ohms (Ω); from Ohm’s law, 1 Ω corresponds to 1 V/A. Conductance is G = 1/R, measured in siemens (S), so i = Gv.

For a uniform conductor, resistance depends on the material and geometry: R = ρl/A. Increasing length increases resistance, while increasing cross-sectional area decreases it. In metals, resistivity increases with temperature, so real resistance can change with temperature.

*Figure: Fig. 1.5 · V–I characteristic of resistance*

*Figure: Fig. 1.6 · Circular conductor*

### Power, heat and resistor rating

A resistor converts absorbed electrical energy into heat. Combining p = vi with v = Ri gives the familiar forms p = i²R and p = v²/R.

Because electrical energy is dissipated as heat, a practical resistor must have a sufficient power rating. Inadequate heat dissipation can overheat or damage the resistor.

### Inductance: current, flux and induced emf

A current-carrying conductor produces magnetic flux around it; the direction follows the right-hand thumb rule. When the conductor is formed into a coil, the flux links multiple turns. If N turns link a flux Φ, the flux linkage is Ψ = NΦ and is expressed in weber-turns.

When flux linkage changes with time, an emf is induced. For an ideal linear inductor, v = L·di/dt. The proportionality constant L is inductance and its unit is the henry (H). One henry is the inductance of a coil in which a current changing at 1 ampere per second produces an induced emf of 1 volt.

By Lenz’s law the induced emf opposes the change that produces it. This is the physical basis for the statement that an inductor opposes changes in current.

*Figure: Fig. 1.7 · Flux lines around a current-carrying conductor*

*Figure: Fig. 1.8 · Representation of a coil or winding axis*

*Figure: Fig. 1.9 · Induced emf in a coil opposes change in current*

### Inductor behaviour

- If current is constant, di/dt = 0 and the ideal inductor voltage is zero.
- Therefore an ideal inductor behaves as a short circuit after steady DC has been established.
- A finite voltage cannot produce an instantaneous jump in inductor current. Current through an ideal inductor is continuous unless an infinite voltage is allowed.
- The integral relation i(t1) = i(t0) + (1/L)∫v dt shows that present current depends on the previous current — an inductor has memory.
- Stored magnetic energy is W = ½Li². Energy can remain stored even when the current has become constant and the ideal inductor voltage has fallen to zero.
- A useful analogy is “electrical inertia”: a flywheel resists change in speed, while an inductor resists change in current.

### Capacitance: charge stored by an electric field

A capacitor is formed by conducting plates separated by an insulating dielectric. Equal and opposite charge accumulates on the plates and an electric field is established between them. Charge and voltage are related by q = Cv, where C is capacitance measured in farads (F). One farad is the capacitance that stores one coulomb of charge when one volt is applied, so 1 F = 1 C/V.

Differentiating q = Cv for constant C gives i = C·dv/dt. The integral form v(t1) = v(t0) + (1/C)∫i dt makes the memory property explicit.

*Figure: Fig. 1.10 · Capacitor*

### Capacitor behaviour

- If capacitor voltage is constant, dv/dt = 0 and the ideal capacitor current is zero.
- Therefore an ideal capacitor behaves as an open circuit under steady DC.
- A finite current cannot change capacitor voltage instantaneously. Capacitor voltage is continuous unless an infinite current is allowed.
- Stored electric-field energy is W = ½Cv². Energy can remain stored at constant voltage even though current is zero.
- For a parallel-plate capacitor, capacitance increases with plate area and permittivity and decreases as plate spacing increases.

### Memoryless versus memory elements

The resistor is memoryless: at a given instant its voltage depends only on the current at that instant through v = Ri. The capacitor and inductor are dynamic elements because their terminal relationships contain time derivatives and their states depend on earlier voltage/current history.

This distinction becomes important when circuits contain stored energy. R dissipates; ideal L and C store and can later return energy to the circuit.

### Linearity of R, L and C

A linear element obeys superposition: if one excitation produces one response and a second excitation produces a second response, a linear combination of the excitations produces the same linear combination of responses.

For constant R, L and C, the relations v = Ri, v = L·di/dt and i = C·dv/dt are linear. Their linearity allows network theorems such as Superposition and Thevenin’s theorem to be applied to circuits containing these ideal elements.

### Check yourself

- **How do ideal L and C behave after steady DC has been established?**  
  An ideal inductor behaves as a short circuit because di/dt = 0 and hence v = 0. An ideal capacitor behaves as an open circuit because dv/dt = 0 and hence i = 0.
- **Which quantities cannot jump instantaneously under finite excitation?**  
  Current through an ideal inductor cannot change instantaneously under finite voltage, and voltage across an ideal capacitor cannot change instantaneously under finite current.
- **How do R, L and C differ in their energy behaviour?**  
  A resistor dissipates absorbed electrical energy as heat. An ideal inductor stores energy in a magnetic field, W = ½Li², and an ideal capacitor stores energy in an electric field, W = ½Cv².

### Formula / method sheet

- `Resistance: v = Ri; R in ohms (Ω); 1 Ω = 1 V/A`
- `Conductance: G = 1/R; G in siemens (S)`
- `Uniform conductor: R = ρl/A`
- `Resistor power: p = vi = i²R = v²/R`
- `Flux linkage: Ψ = NΦ (weber-turns)`
- `Inductor: v = L·di/dt; L in henrys (H)`
- `Inductor energy: W = ½Li²`
- `Capacitor: q = Cv; C in farads (F); 1 F = 1 C/V`
- `Capacitor: i = C·dv/dt`
- `Capacitor energy: W = ½Cv²`

### Important notes

- Energy behaviour is unambiguous: a resistor dissipates electrical energy, while ideal inductors and capacitors store energy in magnetic and electric fields respectively.
- Steady-DC short/open statements apply to ideal L and C after transients have settled; they are not general replacements for all time-varying conditions.

### Class history

- [24 Aug 2026 · Types of elements](college/1-1/basic-electrical-engineering/class-log.html?date=2026-08-24)

### Physical-book reference

- **pp. 5–8** · source image(s): `05.png–08.png` — R, L and C definitions, equations, energy and DC behaviour

### Textbook practice pointer

- p. 70 · 2-mark · Q5–Q9 · anchor `u1-sa-05`
- p. 71 · 6-mark · Q3 · anchor `u1-es-03`

---

## 4. Independent and dependent voltage/current sources

**Status:** Core R25

Circuit elements need excitation, and electrical sources provide it. The two basic source models are voltage sources and current sources; each may be independent or controlled by another circuit variable. Ideal-source behaviour is introduced first, followed by practical source models and the four dependent-source types.

### Quick recall

- Ideal voltage sources fix voltage; ideal current sources fix current. Their other terminal variable adjusts to whatever the connected circuit requires.
- Dependent sources are controlled by a voltage or current elsewhere in the circuit: VCVS, VCCS, CCVS and CCCS.
- Practical source models add internal resistance: series resistance for a voltage source and parallel resistance for a current source.

### What an electrical source does

An electrical source supplies electrical energy or power to a load. The first distinction is between a voltage source, which specifies a terminal voltage, and a current source, which specifies a current. Each of those may then be independent or dependent on another voltage or current elsewhere in the circuit.

For an ideal voltage source, the terminal voltage remains fixed while the current is determined by the connected circuit. Its V–I characteristic is therefore a horizontal constant-voltage line when voltage is plotted on the vertical axis.

*Figure: Voltage source and constant-voltage characteristic*

### Ideal independent voltage source

An ideal independent voltage source maintains the specified terminal voltage irrespective of the current drawn from it. The current is determined by the rest of the connected circuit; the source model itself does not impose that current.

The circular source symbol and marked polarity define the reference voltage. If the specified source voltage is negative, the actual polarity is opposite to the marked reference. On the V-I characteristic, voltage stays fixed while current may take any value.

*Figure: Fig. 1.11 · Independent voltage source and V–I characteristic*

### Ideal independent current source

An ideal independent current source maintains the specified current irrespective of the voltage developed across its terminals. The terminal voltage is whatever value the surrounding circuit requires.

The arrow fixes the reference current direction. A negative source value means actual current is opposite to the arrow. On the V-I characteristic, current is fixed while voltage may take any value.

*Figure: Fig. 1.12 · Independent current source and V–I characteristic*

### Practical source models

- Practical voltage source: an ideal voltage source Vs in series with internal resistance R. As load current increases, the terminal voltage falls according to Vt = Vs − iR for the shown reference directions.
- Practical current source: ideal current source in parallel with internal resistance. Some source current is diverted through the internal resistance, so the current delivered to the external circuit depends on terminal voltage.
- The ideal models are limiting cases. They are extremely useful in analysis even though real sources have finite internal effects.

*Figure: Fig. 1.18 · V–I characteristic of a practical voltage source*

*Figure: Fig. 1.20 · Practical voltage source*

*Figure: Fig. 1.19 · V–I characteristic of a practical current source*

*Figure: Fig. 1.21 · Practical current source*

### Dependent or controlled sources

For a dependent source, the output voltage or current is controlled by another voltage or current elsewhere in the circuit. A diamond symbol distinguishes a controlled source from an independent source. Controlled sources are useful models for active devices and amplifying behaviour.

*Figure: Fig. 1.13 · Symbols of dependent voltage and current sources*

### VCVS — voltage-controlled voltage source

Quick check: if K = 5, a control voltage of 1 V gives 5 V at the controlled source. Likewise, 20 mV·sin(ωt) becomes 100 mV·sin(ωt).

- Controlling quantity: voltage vx.
- Controlled quantity: output voltage vo.
- Relation: vo = K·vx. K is dimensionless voltage gain.
- A VCVS is a simple amplifier model: a small controlling voltage can produce a scaled output voltage.

*Figure: Fig. 1.14 · Voltage-controlled voltage source*

### CCVS — current-controlled voltage source

For Rm = 2 kΩ, a controlling current of 1 mA produces 2 V. This makes the resistance dimension of Rm easy to remember.

- Controlling quantity: current ix sensed in another branch.
- Controlled quantity: output voltage vo.
- Relation: vo = Rm·ix. Rm has dimensions of resistance and is called transresistance or transimpedance.
- The controlling current is sensed without changing the branch-current value in the ideal model.

*Figure: Fig. 1.15 · Current-controlled voltage source*

### VCCS — voltage-controlled current source

For Gm = 1 mS, a controlling voltage of 1 V produces 1 mA of controlled current. The units work naturally: siemens × volts = amperes.

- Controlling quantity: voltage vx.
- Controlled quantity: output current io.
- Relation: io = Gm·vx. Gm has units of conductance and is commonly called transconductance.
- A VCCS is a useful model for active devices such as transistors.

*Figure: Fig. 1.16 · Voltage-controlled current source*

### CCCS — current-controlled current source

For current gain K = 5, a controlling current of 1 mA produces a 5 mA controlled current.

- Controlling quantity: current ix.
- Controlled quantity: output current io.
- Relation: io = K·ix. K is a dimensionless current gain.
- It is the current counterpart of a VCVS: the output is a scaled version of the controlling current.

*Figure: Fig. 1.17 · Current-controlled current source*

### Linearity and one-way control

The four controlled-source relations above are linear in their controlling variables and therefore fit naturally into linear circuit analysis. Their control is unilateral: the controlling side determines the controlled side, not the reverse.

A non-zero independent ideal voltage or current source does not itself satisfy the superposition test even though its V-I characteristic is a straight line. A straight characteristic is not sufficient for linearity unless it passes through the origin. This is why setting an independent source to zero is a special step in superposition-based theorems.

### Zero-valued source equivalents

- 0 V ideal voltage source → short circuit.
- 0 A ideal current source → open circuit.
- These equivalents are used repeatedly when independent sources are deactivated in Superposition and Thevenin calculations.

### Check yourself

- **What is the key difference between an ideal voltage source and an ideal current source?**  
  An ideal voltage source fixes its terminal voltage and lets current be determined by the connected circuit. An ideal current source fixes its current and lets terminal voltage be determined by the connected circuit.
- **What are the four dependent-source types?**  
  VCVS: voltage-controlled voltage source; VCCS: voltage-controlled current source; CCVS: current-controlled voltage source; CCCS: current-controlled current source.
- **What do zero-valued ideal sources become?**  
  A 0 V ideal voltage source is equivalent to a short circuit. A 0 A ideal current source is equivalent to an open circuit.

### Formula / method sheet

- `Practical voltage source: Vt = Vs − iR (for the shown references)`
- `VCVS: vo = K·vx`
- `VCCS: io = Gm·vx`
- `CCVS: vo = Rm·ix`
- `CCCS: io = K·ix`
- `0 V source ≡ short circuit`
- `0 A source ≡ open circuit`

### Important notes

- Do not “turn off” a dependent source when applying Superposition or finding Thevenin resistance. It must remain active because its value depends on a circuit variable.
- Do not infer that a source is linear merely because its V-I graph is a straight line; use the superposition test.

### Class history

- [24 Aug 2026 · Source classification](college/1-1/basic-electrical-engineering/class-log.html?date=2026-08-24)

### Physical-book reference

- **pp. 8–14** · source image(s): `08.png–11.png; 13.png = p.12; 12.png = p.13; 14.png = p.14` — ideal/practical independent sources and four controlled-source types; p.12/p.13 screenshots were captured out of order

### Textbook practice pointer

- p. 70 · 2-mark · Q10–Q11 · anchor `u1-sa-10`
- p. 71 · 2-mark · Q12 · anchor `u1-sa-12`
- p. 71 · 6-mark · Q4 · anchor `u1-es-04`

---

## 5. Source transformation

**Status:** Supporting topic

A practical source can often be represented in two equivalent ways. Source transformation lets us switch between a voltage-source form and a current-source form while preserving the same terminal behaviour seen by the external load.

### Quick recall

- A voltage source Vs in series with R is terminally equivalent to a current source Is = Vs/R in parallel with the same R.
- The reverse transformation is Is in parallel R → Vs = IsR in series R.
- The transformation preserves behaviour only at the same pair of external terminals.

### Why source transformation is useful

Source transformation changes the form of a source-resistance combination without changing the voltage-current behaviour seen by the rest of the circuit at its two external terminals. It can turn an awkward network into one that reduces directly by series/parallel rules.

### Voltage source to current source

- Start with an ideal voltage source Vs in series with resistance R.
- Replace it by an ideal current source Is = Vs/R in parallel with exactly the same resistance R.
- Choose the current-source arrow so that the open-circuit terminal voltage has the same polarity as the original voltage source.

*Figure: Fig. 1.22 · Conversion of a voltage source into a current source*

### Current source to voltage source

- Start with an ideal current source Is in parallel with resistance R.
- Replace it by an ideal voltage source Vs = IsR in series with the same resistance R.
- Choose the voltage polarity consistently with the original current-source direction.

*Figure: Fig. 1.23 · Conversion of a current source into a voltage source*

### What must remain unchanged

- The two external terminals being observed.
- The internal resistance value R.
- The terminal voltage-current relationship as seen by the load.
- The source orientation (polarity/arrow) after conversion.

### Check yourself

- **A 24 V source is in series with 10 Ω. What is its equivalent current-source form?**  
  The equivalent is a 2.4 A current source in parallel with 10 Ω. The resistance value stays 10 Ω; only the source type and its series/parallel arrangement change.

### Formula / method sheet

- `Voltage form: Vs in series R`
- `Current form: Is = Vs/R in parallel R`
- `Reverse: Vs = IsR`

### Problem-solving method

1. Identify a source with its associated series/parallel resistance.
2. Apply Is = Vs/R or Vs = IsR.
3. Keep the same R and preserve the same external terminals.
4. Redraw the circuit and continue series/parallel reduction.

### Important notes


### Physical-book reference

- **pp. 13–16** · source image(s): `12.png = p.13; 14.png–16.png = pp.14–16` — source-transformation derivation and examples

### Textbook practice pointer

- p. 71 · 2-mark · Q13 · anchor `u1-sa-13`
- p. 71 · 6-mark · Q5 · anchor `u1-es-05`

---

## 6. Kirchhoff’s laws

**Status:** Core R25

After defining elements and sources, the next step is to connect them. Kirchhoff’s laws provide the bookkeeping rules for any lumped circuit: KCL balances current at a node, while KVL balances voltage around a closed loop.

### Quick recall

- KCL expresses conservation of charge at a node: the algebraic sum of currents at a node is zero.
- KVL expresses the potential balance around a closed loop: the algebraic sum of voltage rises/drops around the loop is zero.
- Reference directions are arbitrary but must be used consistently; negative answers simply reverse the assumed direction or polarity.

### Kirchhoff’s Current Law (KCL)

KCL states that the algebraic sum of currents entering a node is zero. Equivalently, total current entering equals total current leaving. This follows from conservation of charge: if a node does not create, destroy or accumulate charge, the rate of charge flowing in must balance the rate flowing out.

You may choose “entering positive” or “leaving positive”. Either convention works. What matters is that every branch current at that node is written using the same sign convention.

*Figure: Fig. 1.26 · Representation of KCL*

### KCL intuition and sign handling

Water-flow analogy: if 10 L/min and 15 L/min enter a junction, 25 L/min must leave. If every flow is referenced toward the junction, the outgoing 25 L/min appears as −25 L/min and the algebraic sum is zero.

The same idea prevents confusion in circuits. An assumed branch current may solve to a negative value; keep the equation and interpret the negative sign as actual flow opposite to the reference arrow.

### Kirchhoff’s Voltage Law (KVL)

KVL states that the algebraic sum of voltages around a closed loop is zero. Start from any node, traverse the loop once and add either voltage rises or voltage drops consistently. Returning to the starting point returns to the same electrical potential, so the net change is zero.

A voltage encountered from − to + is a rise; from + to − is a drop. You can formulate KVL using either convention as long as the signs are consistent around the whole loop.

*Figure: Fig. 1.27 · Representation of KVL*

### KVL intuition and circuit assumption

Height analogy: after climbing and descending during a closed journey and returning to the starting point, the algebraic sum of all height changes is zero. KVL applies the same idea to electrical potential around a loop.

The circuit form of KVL assumes that no significant time-varying magnetic flux links the loop. Under the lumped-circuit assumption, the algebraic sum of potential changes around the loop is zero.

### Using KCL and KVL together

- Label nodes, choose current arrows and mark voltage polarities before writing equations.
- Use element relations such as v = Ri to connect branch voltages and currents.
- Use KCL where branch currents meet and KVL where loop voltages are convenient.
- Solve the simultaneous equations without changing reference directions halfway through.
- Interpret a negative solution only after the algebra is complete.

### Check yourself

- **In the KCL sign example, I₁ = 1 A, I₂ = −2 A and I₄ = 1 A are referenced as entering a node. What is I₃?**  
  Using KCL: 1 − 2 + I₃ + 1 = 0, so I₃ = 0 A. A negative branch-current value is valid; it means the actual direction is opposite to the chosen reference.
- **In the KVL sign example, V₁ = 1 V, V₂ = 3 V and V₄ = 5 V. If 3 + V₃ + 5 − 1 = 0, what is V₃?**  
  V₃ = −7 V. The negative sign means the actual polarity is opposite to the chosen voltage reference.

### Formula / method sheet

- `KCL: Σi = 0 at a node`
- `Equivalent KCL form: Σiin = Σiout`
- `KVL: Σv = 0 around a closed loop`

### Problem-solving method

1. Mark current references and voltage polarities.
2. Write KCL at the required node(s).
3. Choose a loop direction and write KVL consistently.
4. Substitute element/source relations.
5. Solve and use the signs of the answers to interpret actual direction/polarity.

### Important notes

- Do not switch sign convention partway through an equation. A negative answer is information, not a reason to rewrite the original reference arrows.

### Physical-book reference

- **pp. 16–30** · source image(s): `16.png–30.png` — law statements plus extensive KCL/KVL worked examples, including controlled-source circuits

### Textbook practice pointer

- p. 71 · 2-mark · Q14 · anchor `u1-sa-14`
- p. 71 · 6-mark · Q6–Q7 · anchor `u1-es-06`

---

## 7. Series, parallel and series-parallel reduction

**Status:** Core R25

Many DC networks can be simplified without solving a large set of simultaneous equations. The key is to recognise genuine series and parallel connections from the nodes, replace them by equivalent elements, and work back to the original branch quantities when needed.

### Quick recall

- Series elements share the same current; parallel elements share the same voltage.
- Use equivalent R/L/C and source-combination rules only when the topology really satisfies those series/parallel conditions.
- Reduce the circuit step by step, solve the simple equivalent, then work backward with Ohm’s law and divider rules.

### How to recognise true series and parallel connections

Two elements are in series when the same current is forced through both — their common node has no additional branch through which current can leave. Two elements are in parallel when both terminals of one connect to the same two nodes as both terminals of the other, so they have exactly the same voltage.

Visual proximity on the drawing is not enough. Always decide from the nodes and current paths.

### Voltage sources and current sources in series/parallel

- Voltage sources in series add algebraically according to their marked polarities.
- Parallel independent current sources add algebraically according to their arrow directions.
- Unequal ideal current sources cannot be placed in series: each tries to impose a different value on the same series current, violating KCL.
- Unequal ideal voltage sources cannot be placed directly in parallel: each tries to impose a different voltage across the same two nodes.
- Identical ideal sources can share the same imposed value; for circuit reduction the combination is equivalent to that same ideal source.

### Resistors

- Series: Req = R1 + R2 + … + Rn.
- Parallel: 1/Req = 1/R1 + 1/R2 + … + 1/Rn.
- Conductance form for parallel branches: Geq = G1 + G2 + … + Gn.
- For two parallel resistors: Req = R1R2/(R1+R2).

### Inductors

- For uncoupled ideal inductors in series: Leq = ΣL.
- For uncoupled ideal inductors in parallel: 1/Leq = Σ(1/L).
- The parallel-inductor formula follows from the integral voltage-current relation when initial inductor currents are zero.

### Capacitors

- Parallel capacitors: Ceq = ΣC.
- Series capacitors: 1/Ceq = Σ(1/C).
- For zero initial capacitor voltages, the series-capacitor relation leads to the usual reciprocal equivalent-capacitance formula.

### Dissimilar element combinations with ideal sources

An ideal current source fixes the current of its series path. Therefore a current source in series with another element is externally equivalent to that same ideal current source: the extra element affects the internal voltage distribution but not the imposed terminal current.

Similarly, an ideal voltage source fixes the voltage across its parallel terminals. A voltage source in parallel with another element is externally equivalent to that voltage source: the extra element affects internal current but not the imposed terminal voltage.

### Open and short circuits

- Short circuit: terminal voltage is zero while current may take whatever value the surrounding circuit requires. Equivalent ideal forms include a 0 V voltage source and R = 0.
- Open circuit: terminal current is zero while voltage may take whatever value the surrounding circuit requires. Equivalent ideal forms include a 0 A current source and R → ∞ (G = 0).
- These ideas are not merely definitions: they are used directly when sources are nulled in Superposition and Thevenin’s theorem.

### Voltage divider

For resistors in series, the same current flows through each resistor. The source voltage is therefore divided in proportion to resistance. For two resistors R1 and R2 across V, V1 = V·R1/(R1+R2) and V2 = V·R2/(R1+R2).

### Current divider

For parallel branches, the same voltage appears across each branch. Current divides according to conductance. For two resistors, the current through R1 is I·R2/(R1+R2), and the current through R2 is I·R1/(R1+R2); the branch with lower resistance carries the larger current.

### General series-parallel reduction method

- Start at a part of the network that is unambiguously series or parallel.
- Replace that group by its equivalent and redraw the circuit with node connections preserved.
- Repeat until the source sees a single equivalent load or the requested variable becomes easy to calculate.
- Solve the reduced circuit.
- Work backward through the reductions using Ohm’s law, voltage division or current division to obtain the original branch quantities.

### Check yourself

- **How can you tell that two elements are truly in series?**  
  They must carry the same current, with no branching node between them. Drawing elements next to one another does not by itself make them series-connected.
- **For two parallel resistors, which branch carries the larger current?**  
  The lower-resistance branch carries the larger current. For total current I, current through R₁ is I·R₂/(R₁+R₂), and current through R₂ is I·R₁/(R₁+R₂).

### Formula / method sheet

- `Series R: Req = ΣR`
- `Parallel R: 1/Req = Σ(1/R); Geq = ΣG`
- `Series L (uncoupled): Leq = ΣL`
- `Parallel L (uncoupled): 1/Leq = Σ(1/L)`
- `Parallel C: Ceq = ΣC`
- `Series C: 1/Ceq = Σ(1/C)`
- `Voltage divider: Vk = V·Rk/ΣR`
- `Two-resistor current divider: I1 = I·R2/(R1+R2), I2 = I·R1/(R1+R2)`

### Problem-solving method

1. Identify true series/parallel groups from the nodes.
2. Replace one group at a time and redraw.
3. Solve the fully reduced circuit.
4. Back-substitute through the reductions to recover original voltages/currents.

### Important notes

- Never combine elements just because they look adjacent on the page. Series/parallel is determined by topology: same current for series, same pair of nodes for parallel.

### Physical-book reference

- **pp. 31–35** · source image(s): `31.png–35.png` — series-parallel network examples; the detailed combination rules are reinforced by lectures 17–22 and supplementary pp.55–65

---

## 8. Star/Delta transformations

**Status:** Core R25

Some three-terminal resistor groups are not reducible by ordinary series-parallel rules. Star-Delta conversion changes the internal connection while preserving the resistance seen from the same three external terminals, often exposing simpler series or parallel combinations.

### Quick recall

- Star/Delta transformation replaces a three-terminal Y or Δ resistor network by an equivalent network seen from the same three external terminals.
- Use Y↔Δ when a bridge-like resistor network cannot be reduced by ordinary series/parallel combinations.
- For an equal network, RΔ = 3RY and RY = RΔ/3 — a useful error check.

### Why Star/Delta transformation is needed

Some three-terminal resistor groups are neither series nor parallel. Converting a star (Y) to an equivalent delta (Δ), or a delta to an equivalent star, can change the topology so that ordinary series/parallel reduction becomes possible.

Equivalence means that the resistance behaviour seen between the same three external terminals is unchanged. Label those terminals before using any formula.

### Star (Y) and Delta (Δ) notation

Let the star arms from terminals a, b and c to the common star point be Ra, Rb and Rc. Let the equivalent delta branches between the corresponding terminal pairs be Rab, Rbc and Rca.

*Figure: Fig. 1.45 · Star and Delta networks*

### Star → Delta

- Form S = RaRb + RbRc + RcRa.
- Rab = S/Rc — divide by the star arm opposite branch ab.
- Rbc = S/Ra.
- Rca = S/Rb.
- A memory aid: each delta branch equals “sum of pairwise star products ÷ opposite star arm”.

### Delta → Star

- Form D = Rab + Rbc + Rca.
- Ra = Rab·Rca/D.
- Rb = Rab·Rbc/D.
- Rc = Rbc·Rca/D.
- A memory aid: each star arm equals “product of the two delta branches touching that terminal ÷ sum of all three delta branches”.

### Equal-resistance check

- If Rab = Rbc = Rca = RΔ, then every star arm is RY = RΔ/3.
- If Ra = Rb = Rc = RY, then every delta branch is RΔ = 3RY.
- Use this equal case as a quick sanity check on the general formulas.

### How to choose the useful conversion

The goal is not to transform every Y or Δ you see. Choose the conversion that creates obvious series or parallel combinations in the rest of the circuit. After conversion, redraw the network clearly and continue with ordinary reduction.

### Check yourself

- **What quick check applies when all three Delta resistances are equal?**  
  If every delta branch equals RΔ, every equivalent star arm equals RΔ/3. Conversely, if every star arm equals RY, every equivalent delta branch equals 3RY.
- **What is the practical goal of a Star/Delta transformation?**  
  Choose the conversion that creates obvious series or parallel combinations while preserving the resistance behaviour seen at the same three external terminals.

### Formula / method sheet

- `Y→Δ: S = RaRb + RbRc + RcRa`
- `Rab = S/Rc; Rbc = S/Ra; Rca = S/Rb`
- `Δ→Y: D = Rab + Rbc + Rca`
- `Ra = Rab·Rca/D; Rb = Rab·Rbc/D; Rc = Rbc·Rca/D`
- `Equal case: RY = RΔ/3; RΔ = 3RY`

### Problem-solving method

1. Label the three external terminals.
2. Choose Y→Δ or Δ→Y to make the remaining network reducible.
3. Apply formulas by terminal labels, not visual position.
4. Redraw, reduce and solve the resulting series-parallel circuit.

### Physical-book reference

- **pp. 36–47** · source image(s): `36.png–47.png` — derivation, equal-resistance checks and worked Star/Delta reductions

### Textbook practice pointer

- p. 72 · 6-mark · Q8 · anchor `u1-es-08`

---

## 9. Superposition theorem

**Status:** Core R25

When a linear circuit contains several independent sources, Superposition separates the problem into one-source-at-a-time cases. The individual voltage or current contributions are then added algebraically using the same reference direction or polarity.

### Quick recall

- In a linear circuit, the total voltage or current response equals the algebraic sum of the responses produced by the independent sources acting one at a time.
- Deactivate other independent sources: voltage source → short; current source → open. Controlled sources remain active.
- Superposition applies to voltages and currents, not directly to power.

### Statement of Superposition theorem

For a linear circuit containing more than one independent source, choose a particular branch voltage or current. The value of that response with all sources present equals the algebraic sum of the values obtained when each independent source acts alone while the others are set to zero.

The same reference polarity or current direction must be used in every one-source case so that the individual responses can be added with the correct signs.

### How to deactivate independent sources

- Independent ideal voltage source set to zero → replace by a short circuit.
- Independent ideal current source set to zero → replace by an open circuit.
- Dependent/controlled sources are not deactivated; they stay in the circuit and continue to depend on their controlling variables.

### Why linearity is essential

Superposition follows directly from linearity. If the circuit equations are linear, the response to a linear combination of source excitations is the same linear combination of the individual responses. Splitting the complete source set into one-source cases therefore preserves the total response when the partial results are added.

### Worked-solution pattern

- Mark the required response and fix its reference direction/polarity.
- Case 1: keep source 1 active, null every other independent source, and calculate the response.
- Case 2: keep source 2 active, null every other independent source, and calculate the response.
- Case 3 and any further cases: repeat the same process for each remaining independent source.
- Add the signed responses. A negative contribution simply opposes the chosen reference.
- As a final check, the algebraic sum should have the same units and reference definition as the original requested quantity.

*Figure: Fig. 1.50 · Original circuit for the Superposition example*

*Figure: Fig. 1.50(a) · First source acting alone*

*Figure: Fig. 1.50(b) · Second source acting alone*

*Figure: Fig. 1.50(c) · Third source acting alone*

### Do not superpose power

Power is not a linear response because it contains products or squares such as p = vi, i²R or v²/R. Therefore the power obtained in each one-source subproblem cannot simply be added to obtain the actual power with all sources present. First superpose the voltage or current; then calculate power from the final total response.

### When Superposition is useful

The theorem can make a multi-source circuit easier to understand because each source contribution is isolated. It also provides the conceptual bridge to Thevenin’s theorem through linearity and source separation.

### Check yourself

- **When applying Superposition, how are the other independent sources deactivated?**  
  Replace each independent ideal voltage source by a short circuit and each independent ideal current source by an open circuit. Dependent sources remain active.
- **Can the individual source powers be added directly using Superposition?**  
  No. Power is not a linear response because it involves products or squares such as vi, i²R or v²/R. First superpose the required voltage or current, then calculate power from the final total response.

### Formula / method sheet

- `Linear response: x = x₁ + x₂ + … + xₙ (same reference)`
- `Deactivate voltage source: Vs = 0 → short`
- `Deactivate current source: Is = 0 → open`

### Problem-solving method

1. Fix the response reference.
2. Keep one independent source active and null the others.
3. Keep all dependent sources active.
4. Solve each one-source circuit.
5. Add the signed voltage/current responses.
6. Calculate power only after the total voltage/current is known.

### Important notes

- Superposition is for linear-circuit voltages and currents. Do not add partial powers.

### Physical-book reference

- **pp. 48–50** · source image(s): `48.png–50.png` — statement and worked superposition example

### Textbook practice pointer

- p. 72 · 6-mark · Q9 · anchor `u1-es-09`

---

## 10. Thevenin’s theorem

**Status:** Core R25

Thevenin’s theorem compresses a linear two-terminal network into the simplest useful source model: one voltage source V_th in series with one resistance R_th. Once that equivalent is known, changing or reconnecting the load becomes much easier.

### Quick recall

- Any linear two-terminal network can be replaced at those terminals by a Thevenin voltage source V_th in series with a Thevenin resistance R_th.
- V_th is the open-circuit terminal voltage. R_th is the resistance seen looking into the terminals after independent sources are nulled.
- If controlled sources remain, find R_th with a test source; do not deactivate the controlled sources.

### What Thevenin’s theorem really says

Choose two terminals of a linear network. No matter how complicated the internal circuit is, its external voltage-current behaviour at those two terminals can be represented by one ideal voltage source V_th in series with one resistance R_th.

The equivalence is only a terminal equivalence. It reproduces the voltage and current seen by whatever load is connected to those terminals; it does not reproduce every internal current or voltage of the original network.

*Figure: Fig. 1.51 · Thevenin equivalent circuit concept*

### Step 1 — find R_th when only independent sources and resistors remain

- Set every independent voltage source to zero → short circuit.
- Set every independent current source to zero → open circuit.
- Look into the chosen terminals and reduce the remaining resistor network.
- The equivalent resistance seen from the terminals is R_th.

*Figure: Fig. 1.52 · Finding Thevenin equivalent resistance*

### R_th with controlled sources

Controlled sources must remain active. After nulling only the independent sources, apply a test voltage V_test or test current I_test at the output terminals and solve the resulting circuit.

Then R_th = V_test/I_test. The test source is needed because a controlled source may create a terminal relationship that cannot be found by simply combining visible resistor values.

### Step 2 — find V_th

Remove the external load so the chosen output terminals are open-circuited. Keep the original independent and dependent sources operating. Calculate the voltage across the open terminals using a clearly marked polarity. That open-circuit voltage is V_th.

If the calculated value is negative, keep the negative sign. It means the actual terminal polarity is opposite to the reference used to define V_th.

*Figure: Fig. 1.53 · Finding Thevenin voltage*

*Figure: Fig. 1.54 · Thevenin equivalent circuit*

### Step 3 — reconnect the load

Replace the original network by V_th in series with R_th, reconnect the load to the same two terminals, and solve the now-simple circuit. For a resistive load R_L, I_L = V_th/(R_th + R_L) and V_L = I_LR_L.

For the usual reference with current delivered from the source to the load, the Thevenin terminal relation is V = V_th − IR_th.

*Figure: Fig. 1.55 · Thevenin equivalent circuit including load*

### Fast exam procedure

- Mark the two output terminals and the polarity of V_th.
- Null independent sources only and find R_th by ordinary reduction; if controlled sources remain, use V_test/I_test.
- Restore the original sources, remove the load and calculate the open-circuit terminal voltage → V_th.
- Draw V_th in series with R_th.
- Reconnect the load and solve.

### Check yourself

- **What are the two quantities in a Thevenin equivalent and how are they found?**  
  The equivalent is V_th in series with R_th. V_th is the open-circuit voltage at the chosen terminals. R_th is the resistance seen looking into those terminals after nulling independent sources, or is found using a test source when controlled sources remain.
- **For the supplied resistor-network check with V₀ = 8 V and R = 16 kΩ, what Thevenin equivalent is obtained?**  
  V_th = V₀/4 = 2 V and R_th = 5R/8 = 10 kΩ, so the equivalent is a 2 V source in series with 10 kΩ.
- **What must you do when finding R_th if a controlled source is present?**  
  Keep the controlled source active. Null only the independent sources, apply a test voltage or test current at the output terminals, and use R_th = V_test/I_test.

### Formula / method sheet

- `V_th = open-circuit terminal voltage`
- `R_th = resistance seen at the terminals with independent sources nulled`
- `Controlled-source case: R_th = V_test/I_test`
- `Resistive load: I_L = V_th/(R_th + R_L)`
- `V_L = I_L·R_L`
- `Terminal relation: V = V_th − I·R_th`

### Problem-solving method

1. Remove the load and mark terminal polarity.
2. Calculate V_th with the output open.
3. Null only independent sources.
4. Calculate R_th directly, or use a test source if controlled sources remain.
5. Draw the Thevenin equivalent and reconnect the load.

### Important notes

- The Thevenin equivalent is valid at the chosen terminal pair. It is not a claim that internal voltages/currents of the original network are reproduced.
- Controlled sources remain active when finding R_th.

### Physical-book reference

- **pp. 51–62** · source image(s): `51.png–62.png` — Thevenin procedure and multiple worked examples; lecture 27 additionally covers a controlled-source example

---

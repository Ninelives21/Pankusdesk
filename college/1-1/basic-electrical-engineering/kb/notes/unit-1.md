# Unit 1 — Introduction to Electrical Energy and DC Circuits

## 1. Electrical energy in modern life and engineering

**Status:** Core R25

Electrical energy is one of the most widely used forms of energy in modern life. It is readily usable, can be converted into many other forms of energy, and can be transmitted efficiently from the place of generation to the place where it is required.

### Quick recall

- Electrical energy is convenient, easily controllable, economical, clean at the point of use, and easy to transmit.
- Electricity is used extensively in homes, commercial buildings, industry, transport, communication, medicine and computing.
- An electrical power system consists of generation, transmission, distribution and utilization.

### Why electrical energy is widely used

- Convenient: electrical energy can be easily converted into other forms such as light, heat and mechanical energy.
- Easily controllable and flexible: electrically operated machines can be started, stopped and controlled conveniently.
- Economical: electrical energy is economical for domestic, commercial and industrial applications.
- Clean at the point of use: its use is not directly associated with smoke, fumes or poisonous gases.
- Easily transmitted: electrical energy can be transmitted conveniently and efficiently from one place to another.

### Role of electrical energy in modern life

Electricity is an essential part of modern life. It is used for lighting, heating, cooling, refrigeration, appliances, computers, electronic equipment, machinery and public transport.

In the commercial sector, computers and office equipment form an important part of electricity use. In industry, electricity is used for machine drives or motors, lighting, computers, and heating, cooling and ventilation equipment.

Electricity is also important in transport, communication and medicine. Electric trains and battery vehicles use electrical energy; radio, television and communication systems depend on it; and equipment such as X-ray and ECG systems requires electrical power.

### Electrical energy and computer science engineering

Computer systems depend on electrical energy for their operation. An understanding of electrical energy is therefore important for computer science and engineering students.

Electrical engineering also develops the circuit and system concepts that support electronic and computer systems.

### Generation, transmission, distribution and utilization

Electrical power generation is the conversion of an available form of energy—such as heat, chemical, solar, wind or mechanical energy—into electrical energy. In the conventional mechanical method of generation, a prime mover supplies the mechanical energy required to drive the generator.

Generating stations are often located near the available energy resource rather than near the load. The generated electrical power is therefore transmitted to load centres, distributed to consumers and finally utilized by the connected loads. Generation, transmission, distribution and utilization together form an electrical power system.

A generator converts mechanical energy into electrical energy, while a motor converts electrical energy into mechanical energy.

*Figure: Fig. 1.1 · Electrical energy generation*

*Figure: Fig. 1.2 · Electrical power system*

### Check yourself

- **Why is electrical energy widely used?**  
  Because it is convenient, easily controllable, economical, clean at the point of use and easy to transmit.
- **What are the main stages of an electrical power system?**  
  Generation, transmission, distribution and utilization.

### Physical-book reference

- **pp. 1–3** — role of electrical energy; CSE relevance; generation, transmission, distribution and utilization

### Textbook practice pointer

- p. 70 · 2-mark · Q1–Q2 · anchor `u1-sa-01`
- p. 71 · 6-mark · Q1–Q2 · anchor `u1-es-01`

---

## 2. Electric circuit and electric network

**Status:** Core R25

An electric circuit is an arrangement of electrical elements used to transfer electrical energy from a source to a load. An electric network is an interconnection of two or more circuit elements.

### Quick recall

- A basic electric circuit contains a source or EMF, a load, a controlling switch and connecting wires.
- The purpose of a circuit is to transfer electrical energy to the load.
- Every circuit is a network, but every network need not be a circuit.

### Electric circuit

An electric circuit is a simple arrangement consisting of a source or electromotive force (such as a battery or generator), a load that consumes electrical energy, a controlling switch and connecting wires. The purpose of the circuit is to transfer electrical energy to the load.

In the basic resistive circuit shown, the source causes current to circulate through the circuit against the resistance of the load. For a linear resistance at a fixed temperature, current is proportional to the applied voltage.

*Figure: Fig. 1.3 · Basic circuit schematic*

### Electric network

The interconnection of two or more circuit elements is called an electric network. A circuit is a network arranged so that current has a complete conducting path through the circuit.

Therefore, a circuit can always be considered a network, but a network need not necessarily form a complete circuit.

### Analogy with magnetic and mechanical systems

An electric circuit can be compared with magnetic and mechanical systems. In an electric circuit, EMF drives current against resistance. In a magnetic circuit, magnetomotive force (MMF) drives magnetic flux against reluctance. In a mechanical system, driving torque maintains speed against friction.

Thus, EMF, MMF and torque are analogous driving quantities; current, magnetic flux and speed are corresponding response quantities; and resistance, reluctance and friction are opposing quantities.

*Figure: Fig. 1.4 · Analogy between electrical, magnetic and mechanical systems*

### Check yourself

- **What are the four basic parts of an electric circuit?**  
  A source or EMF, a load, a controlling switch and connecting wires.
- **What is the difference between a circuit and a network?**  
  A network is an interconnection of two or more circuit elements. A circuit is a network that provides a complete conducting path for current; therefore every circuit is a network, but every network need not be a circuit.

### Physical-book reference

- **pp. 4** — electric circuit, electric network and system analogy

### Textbook practice pointer

- p. 70 · 2-mark · Q3–Q4 · anchor `u1-sa-03`

---

## 3. Circuit elements: resistance, inductance and capacitance

**Status:** Core R25

A circuit element can be represented by one or a combination of three basic parameters: resistance, inductance and capacitance.

### Quick recall

- Resistance opposes current and dissipates electrical energy as heat.
- Inductance is associated with magnetic flux and opposes changes in current.
- Capacitance stores electric charge and energy in an electrostatic field.

### Resistance

Electrical resistance is the property of a material by which it opposes the flow of current through it. At a given temperature, the voltage drop across a conducting material is proportional to the current through it: V = IR. The constant R is the resistance and its unit is the ohm (Ω).

For a uniform conductor, resistance is proportional to its length and inversely proportional to its cross-sectional area: R = ρl/A, where ρ is the resistivity of the material. For metals, resistivity and therefore resistance increase with temperature.

The power absorbed by a resistance is P = VI = I²R = V²/R. The electrical energy absorbed by a resistor appears as heat, so a resistor must be able to dissipate the heat produced.

*Figure: Fig. 1.5 · V–I characteristic of resistance*

*Figure: Fig. 1.6 · Circular conductor*

### Inductance

Inductance is the property of a circuit element associated with magnetic flux. A current-carrying conductor produces magnetic flux around it. When the conductor is formed into a coil, the flux links the turns of the coil. If a flux Φ links N turns, the flux linkage is Ψ = NΦ.

According to Faraday’s law, a changing flux linkage induces an emf in the coil. For an ideal inductor, the voltage-current relation is v = L·di/dt, where L is the inductance. The unit of inductance is the henry (H). One henry is the inductance for which a current changing at 1 A/s produces an emf of 1 V.

By Lenz’s law, the induced emf opposes the change that produces it. Therefore an inductor opposes changes in current. If the current is constant, di/dt = 0 and the induced emf is zero; an ideal inductor then behaves as a short circuit under steady DC conditions.

The energy stored in an ideal inductor is W = ½LI² and is stored in its magnetic field. The current through an ideal inductor cannot change instantaneously under a finite applied voltage.

*Figure: Fig. 1.7 · Flux lines around a current-carrying conductor*

*Figure: Fig. 1.8 · Representation of a coil or winding axis*

*Figure: Fig. 1.9 · Induced emf in a coil opposes change in current*

### Capacitance

A capacitor is formed by two conducting plates separated by an insulating material called a dielectric. When connected across a source, equal and opposite charges accumulate on the plates and an electrostatic field is established between them.

The charge stored is proportional to the voltage across the capacitor: Q = CV. The proportionality constant C is the capacitance and its unit is the farad (F). A capacitance of 1 F stores 1 C of charge when the voltage across it is 1 V.

The capacitor current is i = C·dv/dt. If the voltage across an ideal capacitor is constant, dv/dt = 0 and the current is zero; therefore an ideal capacitor behaves as an open circuit under steady DC conditions.

The energy stored in an ideal capacitor is W = ½CV² and is stored in its electrostatic field. The voltage across an ideal capacitor cannot change instantaneously under a finite current.

*Figure: Fig. 1.10 · Capacitor*

### Key formulas

- Resistance: V = IR
- Uniform conductor: R = ρl/A
- Resistor power: P = VI = I²R = V²/R
- Flux linkage: Ψ = NΦ
- Inductor: v = L·di/dt
- Energy stored in an inductor: W = ½LI²
- Capacitor: Q = CV
- Capacitor current: i = C·dv/dt
- Energy stored in a capacitor: W = ½CV²

### Important note

- For steady DC: an ideal inductor behaves as a short circuit and an ideal capacitor behaves as an open circuit. These are steady-state results, not general replacements for L and C in time-varying circuits.

### Check yourself

- **What are the three basic circuit parameters?**  
  Resistance, inductance and capacitance.
- **How do an ideal inductor and capacitor behave under steady DC conditions?**  
  The ideal inductor behaves as a short circuit because di/dt = 0. The ideal capacitor behaves as an open circuit because dv/dt = 0.
- **Where is energy stored in an inductor and in a capacitor?**  
  An inductor stores energy in its magnetic field, W = ½LI². A capacitor stores energy in its electrostatic field, W = ½CV².

### Physical-book reference

- **pp. 5–8** — R, L and C definitions, equations, energy and steady-DC behaviour

### Textbook practice pointer

- p. 70 · 2-mark · Q5–Q9 · anchor `u1-sa-05`
- p. 71 · 6-mark · Q3 · anchor `u1-es-03`

---

## 4. Voltage and current sources

**Status:** Core R25

The purpose of an electrical energy source is to supply electrical energy or power to a load. Sources are broadly classified as voltage sources or current sources, and also as independent or dependent sources.

### Quick recall

- A voltage source maintains a specified voltage while the current depends on the connected load.
- A current source maintains a specified current while the voltage depends on the connected load.
- A dependent source is controlled by a voltage or current elsewhere in the circuit.

### Voltage sources and current sources

A voltage source supplies different values of current while maintaining its specified voltage. A current source supplies different values of voltage while maintaining its specified current.

Sources may also be classified as independent sources and dependent, or controlled, sources.

### Independent voltage source

An independent voltage source is characterized by a terminal voltage that is independent of the current supplied by it. Its voltage does not change when the connected load network changes.

For an ideal independent voltage source, V = constant.

*Figure: Fig. 1.11 · Independent voltage source and V–I characteristic*

### Independent current source

For an independent current source, the current supplied is independent of the voltage across the source. The source current does not change when the connected load network changes.

For an ideal independent current source, I = constant.

*Figure: Fig. 1.12 · Independent current source and V–I characteristic*

### Dependent or controlled sources

In a dependent source, the voltage of a voltage source or the current of a current source is controlled by a voltage or current at another point in the circuit. Dependent sources are therefore also called controlled sources.

Because the controlling quantity may be either a voltage or a current, four types of dependent sources are possible.

- Voltage-controlled voltage source (VCVS): source voltage is controlled by a voltage.
- Current-controlled voltage source (CCVS): source voltage is controlled by a current.
- Voltage-controlled current source (VCCS): source current is controlled by a voltage.
- Current-controlled current source (CCCS): source current is controlled by a current.

*Figure: Fig. 1.13 · Symbols of dependent voltage and current sources*

*Figure: Fig. 1.14 · Voltage-controlled voltage source*

*Figure: Fig. 1.15 · Current-controlled voltage source*

*Figure: Fig. 1.16 · Voltage-controlled current source*

*Figure: Fig. 1.17 · Current-controlled current source*

### Practical voltage and current sources

A practical voltage source is not ideal. As the source current increases, the terminal voltage decreases because of the source internal resistance. It is represented by an ideal voltage source in series with an internal resistance.

A practical current source is represented by an ideal current source in parallel with an internal resistance. As the load resistance and required load voltage increase, part of the source current flows through the internal resistance and the load current decreases slightly.

*Figure: Fig. 1.18 · V–I characteristic of a practical voltage source*

*Figure: Fig. 1.20 · Practical voltage source*

*Figure: Fig. 1.19 · V–I characteristic of a practical current source*

*Figure: Fig. 1.21 · Practical current source*

### Key formulas

- Ideal voltage source: V = constant
- Ideal current source: I = constant
- Practical voltage source terminal voltage: V_t = V_s − IR_s
- VCVS: V₂ = μV₁
- CCVS: V₂ = R_m I₁
- VCCS: I₂ = G_m V₁
- CCCS: I₂ = αI₁

### Check yourself

- **How does an ideal voltage source differ from an ideal current source?**  
  An ideal voltage source keeps its voltage constant while the current depends on the load. An ideal current source keeps its current constant while the voltage depends on the load.
- **What are the four types of dependent sources?**  
  VCVS, CCVS, VCCS and CCCS.

### Physical-book reference

- **pp. 8–14** — independent/dependent sources and practical source models

### Textbook practice pointer

- p. 70 · 2-mark · Q10–Q11 · anchor `u1-sa-10`
- p. 71 · 2-mark · Q12 · anchor `u1-sa-12`
- p. 71 · 6-mark · Q4 · anchor `u1-es-04`

---

## 5. Source transformation

**Status:** Supporting textbook topic (not separately named in R25)

A practical voltage source can be converted into an equivalent practical current source, and a practical current source can be converted into an equivalent practical voltage source, while maintaining the same load voltage and load current at the external terminals.

### Quick recall

- A voltage source V_s in series with R is equivalent to a current source I_s = V_s/R in parallel with the same R.
- A current source I_s in parallel with R is equivalent to a voltage source V_s = I_sR in series with the same R.

### Voltage source to current source

A practical voltage source of voltage V_s and series resistance R_s can be replaced by a practical current source of current I_s = V_s/R_s with an equal resistance R_p = R_s connected in parallel.

*Figure: Fig. 1.22 · Conversion of a voltage source into a current source*

### Current source to voltage source

A practical current source of current I_s and parallel resistance R_p can be replaced by a practical voltage source of voltage V_s = I_sR_p with an equal series resistance R_s = R_p.

*Figure: Fig. 1.23 · Conversion of a current source into a voltage source*

### Key formulas

- I_s = V_s/R
- V_s = I_sR
- The resistance value is unchanged during the transformation.

### Problem-solving method

1. Identify the practical source and its associated resistance.
2. Use I_s = V_s/R for voltage-to-current transformation, or V_s = I_sR for current-to-voltage transformation.
3. Keep the same resistance value and preserve the same external terminals.

### Check yourself

- **What is the current-source equivalent of a voltage source V_s in series with R?**  
  A current source I_s = V_s/R in parallel with the same resistance R.

### Physical-book reference

- **pp. 13–16** — source transformation and two short exercises

### Textbook practice pointer

- p. 71 · 2-mark · Q13 · anchor `u1-sa-13`
- p. 71 · 6-mark · Q5 · anchor `u1-es-05`

---

## 6. Kirchhoff’s laws

**Status:** Core R25

Kirchhoff’s Current Law and Kirchhoff’s Voltage Law, used together with Ohm’s law, provide a systematic method for analysing electrical networks.

### Quick recall

- KCL: the algebraic sum of currents at a node is zero.
- KVL: the algebraic sum of voltages around a closed path is zero.
- Use one sign convention consistently throughout each equation.

### Kirchhoff’s Current Law (KCL)

Kirchhoff’s Current Law states that the algebraic sum of the currents at a node is zero. A node is a point where two or more branches are connected.

If currents entering a node are taken as positive and currents leaving the node are taken as negative, then ΣI = 0. Equivalently, the sum of currents entering a node is equal to the sum of currents leaving it.

KCL follows from conservation of charge: charge does not accumulate at an ideal circuit node.

*Figure: Fig. 1.26 · Representation of KCL*

### Kirchhoff’s Voltage Law (KVL)

Kirchhoff’s Voltage Law states that the algebraic sum of all voltages around a closed path or loop is zero: ΣV = 0.

Choose a direction around the loop and keep it throughout the equation. A voltage rise is taken with one sign and a voltage drop with the opposite sign. Equivalently, the sum of voltage rises around a loop is equal to the sum of voltage drops.

*Figure: Fig. 1.27 · Representation of KVL*

### Using KCL and KVL in problems

First identify the nodes and branches and assume current directions. Then use KCL at the required nodes and KVL around suitable loops. Combine these equations with element relations such as V = IR and solve the resulting simultaneous equations.

If a calculated current or voltage is negative, the actual direction or polarity is opposite to the one originally assumed.

### Key formulas

- KCL: ΣI = 0 at a node
- Equivalent KCL form: ΣI_entering = ΣI_leaving
- KVL: ΣV = 0 around a closed loop

### Problem-solving method

1. Identify and label the nodes and branches.
2. Assume current directions and voltage polarities.
3. Write the required KCL and KVL equations using one consistent sign convention.
4. Use V = IR and any source relations, then solve the equations.
5. Interpret a negative answer as the actual direction or polarity being opposite to the assumed one.

### Check yourself

- **State Kirchhoff’s Current Law.**  
  The algebraic sum of currents at a node is zero; equivalently, the sum of currents entering the node equals the sum leaving it.
- **State Kirchhoff’s Voltage Law.**  
  The algebraic sum of all voltages around a closed path is zero; equivalently, the sum of voltage rises equals the sum of voltage drops.

### Physical-book reference

- **pp. 16–30** — KCL, KVL and worked applications

### Textbook practice pointer

- p. 71 · 2-mark · Q14 · anchor `u1-sa-14`
- p. 71 · 6-mark · Q6–Q7 · anchor `u1-es-06`

---

## 7. Series, parallel and series-parallel reduction

**Status:** Core R25

A network can often be simplified by replacing groups of elements that are in true series or true parallel with their equivalent values. A reliable method is to identify nodes and reduce one group at a time.

### Quick recall

- Series elements carry the same current; parallel elements are connected across the same two nodes.
- Reduce one obvious series or parallel group at a time and redraw the circuit.
- Node identification is essential before deciding whether elements are in series or parallel.

### Series connection

Elements are in series when the same current must pass through them without branching at their common connection. For resistors in series, the equivalent resistance is the sum of the individual resistances.

### Parallel connection

Elements are in parallel when their terminals are connected to the same two nodes and therefore have the same voltage across them. For resistors in parallel, the reciprocal of the equivalent resistance is the sum of the reciprocals of the individual resistances.

### Series-parallel reduction

For a mixed series-parallel network, identify the nodes first. Reduce the simplest series or parallel group, redraw the network, and continue until a single equivalent resistance is obtained.

After the equivalent circuit has been solved, work backwards through the reductions if the current or voltage in an original branch is required.

### Key formulas

- Series resistors: R_eq = R₁ + R₂ + … + R_n
- Parallel resistors: 1/R_eq = 1/R₁ + 1/R₂ + … + 1/R_n
- For two parallel resistors: R_eq = R₁R₂/(R₁ + R₂)

### Problem-solving method

1. Mark the important nodes.
2. Identify one true series or parallel group.
3. Replace it by its equivalent value and redraw the circuit.
4. Repeat until the circuit is reduced to a simple equivalent.
5. Solve the reduced circuit and back-substitute if required.

### Important note

- Do not decide series or parallel connection from the drawing alone. Use the node connections: same current for series, same two nodes for parallel.

### Check yourself

- **What is the safest way to identify series and parallel groups in a complicated drawing?**  
  Identify the nodes first. Elements in true series carry the same current with no branching between them; elements in parallel are connected across the same two nodes.

### Physical-book reference

- **pp. 31–36** — series-parallel reduction through node identification and successive simplification

---

## 8. Star/Delta transformations

**Status:** Core R25

Star–Delta transformations are useful for networks that cannot be simplified easily by ordinary series-parallel reduction.

### Quick recall

- A Star (Y) network and a Delta (Δ) network can be made equivalent at the same three external terminals.
- Delta-to-Star: each star arm equals the product of the two adjacent delta resistances divided by the sum of all three delta resistances.
- Star-to-Delta: each delta branch equals the sum of pairwise products of the three star resistances divided by the opposite star arm.

### Star and Delta networks

Star and Delta are alternative three-terminal resistor networks. The transformation is chosen so that the resistance seen between corresponding external terminals remains unchanged.

*Figure: Fig. 1.45 · Star and Delta networks*

### Delta to Star

Let the delta branches be R_ab, R_bc and R_ca, and the equivalent star arms be R_a, R_b and R_c. Each star arm is the product of the two delta resistances connected to that terminal divided by the sum of all three delta resistances.

### Star to Delta

For a Star-to-Delta conversion, first form S = R_aR_b + R_bR_c + R_cR_a. Each delta resistance is S divided by the star resistance opposite that delta branch.

### Equal-resistance case

If all three delta resistances are equal to R_Δ, each equivalent star resistance is R_Δ/3. Conversely, if all three star resistances are equal to R_Y, each equivalent delta resistance is 3R_Y.

### Using the transformation in a network

Choose the Star-to-Delta or Delta-to-Star conversion that creates obvious series or parallel combinations. After the conversion, continue the ordinary series-parallel reduction.

### Key formulas

- Delta → Star denominator: D = R_ab + R_bc + R_ca
- R_a = R_abR_ca/D
- R_b = R_abR_bc/D
- R_c = R_bcR_ca/D
- Star → Delta numerator: S = R_aR_b + R_bR_c + R_cR_a
- R_ab = S/R_c; R_bc = S/R_a; R_ca = S/R_b
- Equal case: R_Y = R_Δ/3 and R_Δ = 3R_Y

### Problem-solving method

1. Label the same three external terminals in the original and equivalent networks.
2. Choose the conversion that will make the remaining circuit easier to reduce.
3. Apply the conversion formulas carefully by terminal labels.
4. Redraw the network and continue with ordinary series-parallel reduction.

### Check yourself

- **When is a Star/Delta transformation useful?**  
  When a resistor network cannot be simplified easily by ordinary series-parallel reduction.
- **If all three delta resistances are equal to 12 Ω, what is each equivalent star arm?**  
  R_Y = R_Δ/3 = 12/3 = 4 Ω.

### Physical-book reference

- **pp. 36–47** — Star/Delta formulas and worked reductions

### Textbook practice pointer

- p. 72 · 6-mark · Q8 · anchor `u1-es-08`

---

## 9. Superposition theorem

**Status:** Core R25

The Superposition Theorem is used in linear networks containing two or more independent sources to find the response produced by each source separately and then combine the individual responses.

### Quick recall

- In a linear bilateral network, the total response equals the algebraic sum of the responses produced by the individual sources acting alone.
- While one source acts alone, other ideal voltage sources are replaced by short circuits and other ideal current sources by open circuits.
- The final responses must be added algebraically using the same reference direction or polarity.

### Statement of the theorem

The Superposition Theorem states that in a linear, bilateral network containing two or more sources, the response in any element is equal to the algebraic sum of the responses produced by the individual sources acting alone, with the other sources made non-operative. The theorem is valid for linear systems.

### Making the other sources non-operative

- Replace every other ideal voltage source by a short circuit.
- Replace every other ideal current source by an open circuit.

### Procedure

- Choose the voltage or current response to be found and fix its reference direction or polarity.
- Keep one source active and replace the other sources by their non-operative equivalents.
- Calculate the response due to that source.
- Repeat for each source.
- Add the individual responses algebraically.

*Figure: Fig. 1.50 · Original circuit for the Superposition example*

*Figure: Fig. 1.50(a) · First source acting alone*

*Figure: Fig. 1.50(b) · Second source acting alone*

*Figure: Fig. 1.50(c) · Third source acting alone*

### Key formulas

- Total response = algebraic sum of individual source responses
- Ideal voltage source made non-operative → short circuit
- Ideal current source made non-operative → open circuit

### Problem-solving method

1. Fix the required voltage/current reference.
2. Activate one source at a time.
3. Short the other ideal voltage sources and open the other ideal current sources.
4. Find each individual response.
5. Add the responses algebraically.

### Check yourself

- **How are ideal voltage and current sources made non-operative for Superposition?**  
  An ideal voltage source is replaced by a short circuit and an ideal current source by an open circuit.

### Physical-book reference

- **pp. 48–50** — theorem statement and worked example

### Textbook practice pointer

- p. 72 · 6-mark · Q9 · anchor `u1-es-09`

---

## 10. Thevenin’s theorem

**Status:** Core R25

Thevenin’s theorem replaces the part of a linear bilateral network seen from two load terminals by one equivalent voltage source in series with one equivalent resistance.

### Quick recall

- V_th is the open-circuit voltage across the load terminals.
- R_th is the resistance seen from the load terminals after the load is removed and independent sources are made non-operative.
- After finding V_th and R_th, reconnect the load to the Thevenin equivalent and calculate the load current.

### Statement of Thevenin’s theorem

Thevenin’s theorem states that a linear, bilateral two-terminal circuit can be replaced by an equivalent circuit consisting of a voltage source V_th in series with a resistance R_th. V_th is the open-circuit voltage between the load terminals, and R_th is the equivalent resistance seen between those terminals.

*Figure: Fig. 1.51 · Thevenin equivalent circuit concept*

### Step 1 — find Thevenin resistance R_th

Remove the load resistance from the terminals. Replace independent voltage sources by short circuits and independent current sources by open circuits. The resultant resistance measured between the load terminals is the Thevenin resistance R_th.

*Figure: Fig. 1.52 · Finding Thevenin equivalent resistance*

### Step 2 — find Thevenin voltage V_th

With the load still removed, calculate the open-circuit voltage between the load terminals. This open-circuit voltage is the Thevenin voltage V_th.

The Thevenin equivalent circuit is then a source V_th in series with R_th.

*Figure: Fig. 1.53 · Finding Thevenin voltage*

*Figure: Fig. 1.54 · Thevenin equivalent circuit*

### Step 3 — reconnect the load

Reconnect the load resistance R_L to the Thevenin equivalent circuit. The load current is then I_L = V_th/(R_th + R_L).

*Figure: Fig. 1.55 · Thevenin equivalent circuit including load*

### Worked-example pattern

For each worked problem, use the same sequence: remove the load, find R_th, find the open-circuit voltage V_th, draw the Thevenin equivalent, reconnect the load and calculate the required load current.

### Key formulas

- V_th = open-circuit voltage at the load terminals
- R_th = equivalent resistance seen from the load terminals with independent sources made non-operative
- I_L = V_th/(R_th + R_L)

### Problem-solving method

1. Remove the load resistance.
2. Make the independent sources non-operative and find R_th at the load terminals.
3. Restore the sources and find the open-circuit voltage V_th.
4. Draw the Thevenin equivalent: V_th in series with R_th.
5. Reconnect R_L and calculate I_L = V_th/(R_th + R_L).

### Check yourself

- **What are V_th and R_th?**  
  V_th is the open-circuit voltage across the chosen load terminals. R_th is the equivalent resistance seen from those terminals after the load is removed and the independent sources are made non-operative.
- **After the Thevenin equivalent is obtained, how is the load current found?**  
  Reconnect the load R_L and use I_L = V_th/(R_th + R_L).

### Physical-book reference

- **pp. 51–62** — theorem statement, procedure and worked examples

---

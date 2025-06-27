# Power Electronics Final Project 2025
## Task 1: Buck Converter Design
Elisabeth Virginia Putri Harmadianti | 22/505938/TK/55406  
Department of Electrical Engineering, Universitas Gadjah Mada  

---

## Objective
Design and simulate a **buck converter** that steps down a DC input voltage (36 V) to a regulated 12 V output. The goal is to ensure correct operation under steady-state and dynamic conditions, while validating that all design criteria (ripple, regulation, stability) are met.

---

## Design Specifications

| Parameter                   | Value         | Description                               |
|----------------------------|---------------|-------------------------------------------|
| Input Voltage (Vin)        | 36 V          | DC source input                           |
| Output Voltage (Vout)      | 12 V          | Target regulated output                   |
| Output Power (Pout)        | 24 W          | Moderate load power                       |
| Load Resistance (R)        | 6 Ω           | Derived from Vout² / Pout                 |
| Switching Frequency (fsw)  | 100 kHz       | To minimize passive size and losses       |
| Inductor Ripple (ΔIL)      | 20% of Iout   | To ensure Continuous Conduction Mode (CCM)|
| Output Voltage Ripple (ΔVo)| 1% of Vout    | For output stability                      |

---

## Key Calculations

### Duty Cycle
\[
D = \frac{V_{out}}{V_{in}} = \frac{12}{36} = 0.33
\]

### Output Current
\[
I_{out} = \frac{V_{out}}{R} = \frac{12}{6} = 2\,A
\]

### Ripple Requirements
- Inductor Current Ripple:  
  \[
  \Delta I_L = 0.2 \cdot I_{out} = 0.4\,A
  \]

- Output Voltage Ripple:  
  \[
  \Delta V_o = 0.01 \cdot 12 = 0.12\,V
  \]

### Switching Period
\[
T_s = \frac{1}{f_{sw}} = \frac{1}{100\,kHz} = 10\,\mu s
\]

### Inductor Selection
\[
L = \frac{V_{in} - V_{out}}{\Delta I_L} \cdot D \cdot T_s
\]

### Capacitor Selection
\[
C = \frac{\Delta I_L}{8 \cdot f_{sw} \cdot \Delta V_o}
\]

---

## Controller Design

A **Proportional-Integral (PI) Controller** is used in a cascaded voltage-mode control loop:

- **Voltage Loop Bandwidth (Fbp):**  
  \[
  F_{bp} = \frac{f_{sw}}{20} = 5\,kHz
  \]

- **Integrator Corner Frequency (Fbi):**  
  \[
  F_{bi} = \frac{F_{bp}}{10} = 500\,Hz
  \]

- **Control Gains:**
  - \( K_p = 2\pi F_{bp} C \)
  - \( K_i = 2\pi F_{bi} \cdot K_p \)

Values are applied directly in the PLECS simulation control block.

---

## Simulation Results

### Inductor Current Ripple

- Measured ripple: 1.8 A ↔ 2.2 A → ΔIL = 0.4 A
- Meets the 20% design target

### Output Voltage Ripple

- Voltage range: 11.94 V ↔ 12.06 V → ΔVo = 0.12 V  
- Within the 1% tolerance (0.12 V)

### Sudden Load Change Test

- Load step applied at **t = 1 s**
- Transient observed in Vout and IL
- Output returns to steady 12 V quickly  
- Demonstrates fast dynamic response and stability

### Reference Step Response

- Step change at **t = 5 s**
- Output overshoots (~24 V), settles after oscillation
- Inductor current tracks new demand  
- Controller effectively tracks new reference

---

## Task 2: PV Grid-Connected Inverter

## Objective

Design a grid-connected inverter system that interfaces photovoltaic (PV) arrays with a 3-phase 230 V AC grid. The system must regulate both active and reactive power using a control strategy in the rotating dq reference frame. The design includes selecting appropriate component values, simulating the inverter behavior, and analyzing the system under various grid conditions and control scenarios.

---

## PV Array Configuration

- Total arrays: 4 in parallel  
- Each array: 2 strings × 20 modules in series = 40 modules  
- Total modules: 4 × 40 = 160 modules  
- Module type: BP365  
  - Voltage at maximum power (Vmp): 17.5 V  
  - Current at maximum power (Imp): 3.7 A  
  - Power per module: 65 W

### Total Power

- Peak power: 160 × 65 = 10,400 W (10.4 kW)  
- Estimated real output under irradiance 0.7–1.0 kW/m²: 2.6–3.2 kW

---

## Inverter Specifications

| Parameter           | Value                               | Description                                      |
|--------------------|--------------------------------------|--------------------------------------------------|
| DC-Link Voltage     | 800 VDC                              | Output of the boost converter                    |
| Grid Type           | 3-phase, 230 V (L-L RMS), 50 Hz      | Low-voltage European grid                        |
| Power Rating        | 3 kW                                 | Target nominal inverter output power             |
| Switching Frequency | 10 kHz                               | For SVPWM switching                              |
| Inverter Type       | 3-level NPC                          | Neutral-point clamped topology                   |
| Modulation Method   | 3-Level SVPWM                        | Symmetrical & alternating zero vector modes      |

---

## Filter Design (LCL)

An LCL filter is used to limit current ripple and reduce harmonic distortion in the grid current. The filter components consist of:

- L1: Inverter-side inductance  
- L2: Grid-side inductance  
- Cf: Filter capacitor (connected between L1 and L2)

### Assumptions

- Grid frequency: 50 Hz  
- Switching frequency: 10 kHz  
- Line-to-neutral RMS voltage: 220 V  
- Peak phase voltage:  
  \[
  V_{peak} = \sqrt{2} \cdot 220 \approx 311 \text{ V}
  \]
- Target current ripple: 10%

### Filter Parameters (from design results)

| Component           | Symbol | Value      |
|---------------------|--------|------------|
| Inverter Inductance | L1     | (value as calculated in report) |
| Grid Inductance     | L2     | (value as calculated in report) |
| Filter Capacitance  | Cf     | (value as calculated in report) |

*Note: The actual numerical values for L1, L2, and Cf should be inserted based on simulation or design worksheet.*

---

## Control System Design

The control system regulates both active and reactive power injection into the grid. Control is performed in the dq reference frame using PI controllers.

### Control Objectives

- d-axis control loop: active power (P) regulation  
- q-axis control loop: reactive power (Q) regulation

### Tuning Method

PI controller parameters are calculated based on:
- Desired closed-loop bandwidth
- System dynamics from LCL filter
- Stability and decoupling requirements

A block diagram of the control structure is included in the documentation.

---

## Simulation Results

### dq-Reference Current Tracking

Simulations compare reference and measured dq currents under three conditions:

1. In-phase current (unity power factor)  
2. Lagging current (positive reactive power)  
3. Leading current (negative reactive power)

The results show accurate tracking and decoupling between P and Q control loops.

---

### Inverter Output Voltage

The inverter’s output voltage is analyzed both in the time domain and frequency domain:

- Phase and line voltages are plotted
- FFT analysis is performed to assess harmonic content and validate compliance with grid standards


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

## 🎛️ Controller Design

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
- ✔️ Meets the 20% design target

### Output Voltage Ripple

- Voltage range: 11.94 V ↔ 12.06 V → ΔVo = 0.12 V  
- ✔️ Within the 1% tolerance (0.12 V)

### Sudden Load Change Test

- Load step applied at **t = 1 s**
- Transient observed in Vout and IL
- Output returns to steady 12 V quickly  
- ✔️ Demonstrates fast dynamic response and stability

### Reference Step Response

- Step change at **t = 5 s**
- Output overshoots (~24 V), settles after oscillation
- Inductor current tracks new demand  
- ✔️ Controller effectively tracks new reference

---

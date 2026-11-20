# BIT 2118: Scientific Computing Project Portfolio

**Student Name:** wato ano ali
**Admission Number:** BSCCS252600473
**Course Code & Title:** BIT2118 Scientific Computing  



---

## Overview

This repository contains the complete individual implementation of 19 scientific computing tasks (Tasks A through S / Tasks 02 through 20) for **BIT2118 Scientific Computing**. All tasks are modeled around a unified real-world domain: **Hospital and Healthcare Analytics**, demonstrating how numerical algorithms solve clinical, operational, financial, and physiological problems in a modern medical institution.

---

## Repository File Structure

| Task | Topic / Mathematical Focus | Python Script File |
| :--- | :--- | :--- |
| **Task A** | NumPy Arrays & Vectorized Calculations |  |
| **Task B** | Array Speed-Up & Vectorization | ` |
| **Task C** | Floating-Point Precision & Stability |  |
| **Task D** | Matrix Transformations & Determinants |  |
| **Task E** | Systems of Linear Equations ($Ax = b$) |  |
| **Task F** | LU Decomposition & Shift Optimization |  |
| **Task G** | Iterative Linear Solvers (Jacobi & Gauss-Seidel) | |
| **Task H** | Eigenvalues & Infection Network Centrality |  |
| **Task I** | Root Finding (Bisection & Fixed-Point) | |
| **Task J** | Root Finding (Newton-Raphson & Secant) |  |
| **Task K** | Systems of Nonlinear Equations |  |
| **Task L** | Interpolation (Cubic Splines) |  |
| **Task M** | Curve Fitting & Outbreak Forecasting |  |
| **Task N** | Numerical Differentiation |  |
| **Task O** | Numerical Integration (Simpson's Rule) |  |
| **Task P** | Ordinary Differential Equations (Euler Method) | |
| **Task Q** | Numerical ODE Solvers () |  |
| **Task R** | Constrained Optimization |  |
| **Task S** | Monte Carlo Simulation & Risk Analysis |  |

---

## Detailed Task Documentation

### Task A: NumPy Arrays and Basic Numerical Computation
* **Script:** `
* **Scenario & Assumptions:** A maternity hospital records delivery counts per hour over 24 hours. Staffing hours follow a linear model ($y = 1.5x + 2.0$).
* **Input Data:** 24 hourly birth records across a single day.
* **Interpretation:** Mean births ($2.21\text{ births/hr}$) establish baseline capacity. Peak hours ($6\text{ births}$) determine maximum emergency staffing needs.

---

### Task B: Mathematical Functions and Vectorization
* **Script:** 
* **Scenario & Assumptions:** Processing 1,000,000 maternal health delivery durations (in minutes) converted to hours and squared for variance modeling.
* **Input Data:** Array of $1,000,000$ delivery duration logs.
* **Interpretation:** Demonstrates C-level NumPy vectorization running $>50\times$ faster than standard Python `for` loops on large health datasets.

---

### Task C: Floating-Point Arithmetic and Numerical Errors
* **Script:** 
* **Scenario & Assumptions:** Neonatal ICU heart rate variability monitoring under tiny time steps ($10^{-4}$ to $10^{-12}$).
* **Input Data:** Micro-scale time step delta values ($x$).
* **Interpretation:** Illustrates catastrophic cancellation during direct subtraction and proves how rationalized formulas preserve precision down to 12 decimal places.

---

### Task D: Matrix Algebra and Matrix Operations
* **Script:** 
* **Scenario & Assumptions:** Updating workload allocation across 4 maternity wards combining shift rotation ($30^\circ$) and scaling ($1.2\times$ capacity, $0.9\times$ staff).
* **Input Data:** $4 \times 2$ ward metrics matrix and $2 \times 2$ composite transformation matrix.
* **Interpretation:** Multiplies matrices to update all ward metrics simultaneously. A non-zero determinant ($1.08$) proves invertibility.

---

### Task E: Solution of Systems of Linear Equations
* **Script:** 
* **Scenario & Assumptions:** Allocating ICU and HDU patient blocks given total bed (20) and ventilator (72) equipment limits.
* **Input Data:** Coefficient matrix $A$ (resource rates per block) and vector $b = [20, 72]^T$.
* **Interpretation:** yields exact block counts ($3$ ICU, $4$ HDU) with a zero residual norm ($\|r\| = 0.0$).

---

### Task F: Gaussian Elimination and LU Decomposition
* **Script:** 
* **Scenario & Assumptions:** Allocating maternity resources across Morning, Evening, and Night shifts using a fixed ward relationship matrix.
* **Input Data:** Fixed structural matrix $A$ and shift resource vectors $b_1, b_2, b_3$.
* **Interpretation:** LU Decomposition factors matrix $A$ once (`lu_factor`), enabling fast repeated solves (`lu_solve`) for each shift.

---

### Task G: Iterative Methods for Linear Systems
* **Script:** 
* **Scenario & Assumptions:** Modeling 1D steady-state heat distribution across 5 NICU incubator sensors between a $37^\circ\text{C}$ heater and $22^\circ\text{C}$ room wall.
* **Input Data:** $5 \times 5$ tridiagonal thermal matrix $A$ and boundary vector $b$.
* **Interpretation:** Both Jacobi and Gauss-Seidel converge on exact interior temperatures, with Gauss-Seidel reaching tolerance in fewer iterations.

---

### Task H: Eigenvalues and Eigenvectors
* **Script:**
* **Scenario & Assumptions:** Infection transmission modeling across 4 hospital wards based on staff movement adjacency.
* **Input Data:** $4 \times 4$ ward connection adjacency matrix.
* **Interpretation:** The dominant eigenvector identifies the ICU and Surgery wards as high-centrality transmission hubs requiring targeted sterilization.

---

### Task I: Root Finding: Bisection and Fixed-Point Methods
* **Script:** 
* **Scenario & Assumptions:** Finding the IV drug infusion dose where drug inflow balances biological clearance.
* **Input Data:** Nonlinear clearance balance function $f(D) = D - 25 - 10e^{-D/20}$.
* **Interpretation:** Bisection and fixed-point methods converge to the exact equilibrium dose ($\approx 27.6\text{ mg}$).

---

### Task J: Root Finding: Newton-Raphson and Secant Methods
* **Script:**
* **Scenario & Assumptions:** Financial appraisal of a \$1,000,000 MRI equipment acquisition via Internal Rate of Return (IRR).
* **Input Data:** Cash flow vector across 4 operating years.
* **Interpretation:** Newton-Raphson computes the exact discount rate where Net Present Value (NPV) equals zero to evaluate capital investment viability.

---

### Task K: Polynomial and Nonlinear Equation Solving
* **Script:** 
* **Scenario & Assumptions:** Finding joint dosage for two chemotherapy agents under overlapping toxicity and efficacy boundaries.
* **Input Data:** System of 2 nonlinear equations representing circular safety and parabolic efficacy.
* **Interpretation:** `scipy.optimize.root` locates the optimal dosage point ($x, y$) satisfying both clinical constraints.

---

### Task L: Interpolation
* **Script:** 
* **Scenario & Assumptions:** Estimating unmeasured intermediate blood oxygen ($SpO_2$) values between 4-hour nurse checks.
* **Input Data:** Discrete time hours $[0, 4, 8, 12, 16, 20, 24]$ and measured $SpO_2$ percentages.
* **Interpretation:** Cubic Spline interpolation generates a smooth, physiologically accurate curve between recorded readings.

---

### Task M: Curve Fitting and Approximation
* **Script:**
* **Scenario & Assumptions:** Forecasting hospital bed demand on Day 10 during an emerging local viral outbreak.
* **Input Data:** 7 daily cumulative case counts.
* **Interpretation:** Quadratic curve fitting (`curve_fit`) extrapolates outbreak trajectory to predict future bed capacity requirements.

---

### Task N: Numerical Differentiation
* **Script:** 
* **Scenario & Assumptions:** Calculating instantaneous growth velocity ($\text{cm}^3/\text{week}$) of a tumor from weekly MRI measurements.
* **Input Data:** Weekly tumor volume series over 6 weeks.
* **Interpretation:** Central difference approximation shows declining growth rates, verifying positive therapeutic response.

---

### Task O: Numerical Integration
* **Script:** 
* **Scenario & Assumptions:** Integrating IV pump flow rate ($\text{ml/hr}$) over 12 hours to determine total fluid volume administered.
* **Input Data:** Flow rate measurements taken every 2 hours.
* **Interpretation:** Simpson's rule integration computes the exact total accumulated fluid volume ($\text{ml}$) to prevent hydration errors.

---

### Task P: Ordinary Differential Equations - Euler Method
* **Script:** 
* **Scenario & Assumptions:** Modeling first-order elimination decay of an IV antibiotic in the bloodstream over 30 hours ($dC/dt = -k \cdot C$).
* **Input Data:** Initial concentration $C_0 = 90\text{ mg/L}$, elimination constant $k = 0.12$.
* **Interpretation:** Step-by-step Euler integration tracks concentration decay to determine optimal re-dosing times.

---

### Task Q: Numerical Solution of ODEs Using SciPy
* **Script:**
* **Scenario & Assumptions:** Simulating infectious disease spread dynamics within a hospital ward.
* **Input Data:** Initial susceptible population proportion $S_0 = 1.0$ over 5 days.
* **Interpretation:** SciPy's adaptive `solve_ivp` solver accurately models population decay under contagion exposure.

---

### Task R: Numerical Optimization
* **Script:** 
* **Scenario & Assumptions:** Minimizing shift staffing costs between Registered Nurses (\$300) and Nursing Assistants (\$150) under a 100-care-unit minimum constraint.
* **Input Data:** Cost vector and linear inequality care unit constraint.
* **Interpretation:** `scipy.optimize.minimize` calculates the optimal staff mix that fulfills legal safety requirements at minimum expense.

---

### Task S: Random Numbers and Monte Carlo Methods
* **Script:** 
* **Scenario & Assumptions:** Simulating 100,000 daily Emergency Room patient arrival scenarios to assess overflow risk against a 50-bed limit.
* **Input Data:** Normal arrival distribution ($\mu = 40$, $\sigma = 8$).
* **Interpretation:** Monte Carlo simulation quantifies the exact overflow probability to support proactive bed expansion planning.

---

## Author Verification

* **Student:** wato ano ali
* **Admission No:** BSCCS252600473
* **Course:** BIT2118 Scientific Computing
import numpy as np
from scipy.optimize import root_scalar

# Drug balance model: Infusion matches clearance
def drug_balance(D):
    return D - 25 - 10 * np.exp(-D / 20)

# Bisection method to find the equilibrium dose
solution = root_scalar(drug_balance, bracket=[20, 40], method="bisect", xtol=1e-10)

# Fixed-point iteration form: D = 25 + 10*exp(-D/20)
def g(D):
    return 25 + 10 * np.exp(-D / 20)

D_guess = 30.0
for _ in range(100):
    D_new = g(D_guess)
    if abs(D_new - D_guess) < 1e-10:
        break
    D_guess = D_new

print(f"Equilibrium Dose (Bisection): {solution.root:.6f} mg")
print(f"Equilibrium Dose (Fixed-Point): {D_guess:.6f} mg")
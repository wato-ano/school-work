import numpy as np
from scipy.optimize import root

def drug_equations(vars):
    x, y = vars
    return [
        x**2 + y**2 - 4,   # Safety boundary equation
        y - (x**2 - 1)     # Efficacy boundary equation
    ]

# Search from a clinical starting guess
solution = root(drug_equations, [1.0, 1.0])

print("Optimal Drug Combo [Drug X, Drug Y]:", np.round(solution.x, 4))
print("Equation Residuals (should be near 0):", np.round(drug_equations(solution.x), 4))
import numpy as np
from scipy.optimize import minimize

# Objective: Minimize Cost = 300*RN + 150*CNA
def cost(z):
    rn, cna = z
    return 300 * rn + 150 * cna

# Constraint: 10*RN + 6*CNA >= 100 care units
def care_constraint(z):
    rn, cna = z
    return 10 * rn + 6 * cna - 100

constraints = {"type": "ineq", "fun": care_constraint}
bounds = [(0, None), (0, None)]

solution = minimize(cost, x0=[5, 5], method="SLSQP", bounds=bounds, constraints=constraints)

print("Optimization Success:", solution.success)
print(f"Optimal RNs to schedule: {solution.x[0]:.1f}")
print(f"Optimal CNAs to schedule: {solution.x[1]:.1f}")
print(f"Minimum Shift Cost: ${solution.fun:.2f}")
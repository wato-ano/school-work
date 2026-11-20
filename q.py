import numpy as np
from scipy.integrate import solve_ivp

# Infection spread ODE
def infection_rate(t, S):
    k = 0.5  # transmission rate
    return [-k * S[0]]

t_eval = np.linspace(0, 5, 200)
# Initial susceptible population: 100% (represented as 1.0)
solution = solve_ivp(infection_rate, (0, 5), [1.0], t_eval=t_eval)

print(f"Susceptible population remaining at day 5: {solution.y[0, -1]:.2%}")
print("SciPy Solver Success:", solution.success)
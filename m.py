import numpy as np
from scipy.optimize import curve_fit

# Days passed and cumulative infected patients
days = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)
patients = np.array([5, 12, 25, 42, 65, 95, 130], dtype=float)

def outbreak_model(x, a, b, c):
    return a * x**2 + b * x + c

parameters, _ = curve_fit(outbreak_model, days, patients)
a, b, c = parameters

print(f"Fitted Epidemic Model: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")
print(f"Predicted patients requiring beds on Day 10: {outbreak_model(10, a, b, c):.0f}")
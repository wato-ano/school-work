import numpy as np
from scipy.interpolate import interp1d, CubicSpline

# Manual SpO2 readings every 4 hours
hours = np.array([0, 4, 8, 12, 16, 20, 24], dtype=float)
spo2 = np.array([98.0, 96.5, 94.0, 95.5, 97.0, 98.5, 99.0])

linear = interp1d(hours, spo2, kind="linear")
cubic = CubicSpline(hours, spo2)

# Estimate SpO2 at hour 6 (which was not manually measured)
target_time = 6.0

print(f"Linear SpO2 estimate at hour 6: {float(linear(target_time)):.2f}%")
print(f"Cubic SpO2 estimate at hour 6: {float(cubic(target_time)):.2f}%")
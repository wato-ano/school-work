import numpy as np
from scipy.integrate import simpson

# Time in hours and IV Flow Rate in ml/hr
time_hrs = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
flow_rate_ml_hr = np.array([100, 150, 200, 180, 120, 80, 50])

# Integrate to find total accumulated volume
total_volume = simpson(flow_rate_ml_hr, x=time_hrs)

print(f"Total IV Fluid Infused (Simpson's Rule): {total_volume:.2f} ml")
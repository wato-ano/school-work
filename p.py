import numpy as np

# Pharmacokinetic decay: dC/dt = -k * C
C_initial = 90.0  # mg/L
k = 0.12          # Elimination constant
h = 1.0           # 1-hour time step
end_time = 30.0

time = np.arange(0, end_time + h, h)
concentration = np.zeros_like(time)
concentration[0] = C_initial

# Euler Method Loop
for i in range(len(time) - 1):
    decay_rate = -k * concentration[i]
    concentration[i + 1] = concentration[i] + h * decay_rate

print(f"Euler predicted drug concentration after 30 hrs: {concentration[-1]:.2f} mg/L")
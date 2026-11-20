import numpy as np

# Baseline generic input dataset
data = np.array([12, 15, 18, 22, 20, 25, 30, 28, 24, 19])

# Core statistical calculations (Shared by all group members)
mean_val = np.mean(data)
min_val = np.min(data)
max_val = np.max(data)
scaled_data = 1.5 * data + 2.0

print(f"Mean: {mean_val:.2f}")
print(f"Min: {min_val}")
print(f"Max: {max_val}")
print("Vectorized Scaled Data (First 5):", scaled_data[:5])
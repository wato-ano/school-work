import numpy as np

# Standard micro-scale delta values
x_values = [1e-4, 1e-8, 1e-12]

for x in x_values:
    # Direct formula (unstable subtraction cancellation)
    direct = (np.sqrt(1 + x) - 1) / x
    
    # Rationalized stable formula
    stable = 1 / (np.sqrt(1 + x) + 1)
    
    abs_err = abs(direct - stable)
    print(f"x = {x:.0e} | Direct: {direct:.12f} | Stable: {stable:.12f} | Error: {abs_err:.2e}")
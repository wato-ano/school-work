import numpy as np

# Scenario: Solving hospital ward bed & ventilator allocation
#
# Ward Type 1 (ICU): Needs 4 bed units, 8 ventilator units per patient block
# Ward Type 2 (HDU): Needs 2 bed units, 12 ventilator units per patient block
# Total resources available: 20 bed units and 72 ventilator units

# Coefficient Matrix A (resource coefficients per block)
A = np.array([
    [4.0, 2.0],   # Bed allocation matrix
    [8.0, 12.0]   # Ventilator allocation matrix
])

# Constant Vector b (total available hospital resources)
b = np.array([20.0, 72.0])

# Solve the linear system Ax = b for exact block counts x
solution = np.linalg.solve(A, b)

# Verification (reconstruct b) and calculate residual error
reconstructed_b = A @ solution
residual = b - reconstructed_b
residual_norm = np.linalg.norm(residual)

# Display results
print(f"Allocated ICU Patient Blocks (x1): {solution[0]:.0f}")
print(f"Allocated HDU Patient Blocks (x2): {solution[1]:.0f}")
print("Verification (A @ solution):", reconstructed_b)
print(f"Residual Error Norm: {residual_norm:.2e}")
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Fixed structural resource matrix for 3 maternity wards (Triage, L&D, Postpartum)
A = np.array([
    [4.0,  1.0,  0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0,  3.0]
])

# Total available resources across 3 different shifts [Morning, Evening, Night]
shift_resources = [
    np.array([15.0, 10.0, 10.0]), # Morning Shift
    np.array([16.0, 11.0,  9.0]), # Evening Shift
    np.array([14.0, 12.0, 11.0])  # Night Shift
]

# Factor Matrix A only once using LU Decomposition to save computation time
lu, piv = lu_factor(A)

print("Maternity Ward Patient Allocation via LU Decomposition:")
print("-" * 55)

# Solve for patient distribution for each shift using the pre-factored matrix
for i, b in enumerate(shift_resources, start=1):
    x = lu_solve((lu, piv), b)
    residual = b - A @ x
    
    print(f"Shift {i} Resource Set:")
    print(f"  Triage Patients:     {x[0]:.2f}")
    print(f"  L&D Patients:        {x[1]:.2f}")
    print(f"  Postpartum Patients: {x[2]:.2f}")
    print(f"  Residual Error Norm: {np.linalg.norm(residual):.2e}\n")
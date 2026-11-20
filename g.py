import numpy as np
import matplotlib.pyplot as plt

# Tridiagonal heat transfer matrix for 5 interior incubator sensors
A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

# Boundary temperatures: Left (Heater) = 37 C, Right (Room Temp) = 22 C
b = np.array([37.0, 0., 0., 0., 22.0])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ x_old[i+1:]) / A[i, i]
        error = np.linalg.norm(x - x_old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

# Compute steady-state NICU temperatures
x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Jacobi estimated NICU temperatures (C):", np.round(x_j, 2))
print("Gauss-Seidel estimated NICU temperatures (C):", np.round(x_gs, 2))
print("Exact numerical solution (C):", np.round(x_exact, 2))
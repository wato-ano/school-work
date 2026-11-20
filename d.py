import numpy as np

# Standard 2D spatial coordinate matrix (4x2)
coords = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
    [5.0, 2.0],
    [2.0, 1.0]
])

# Transformation matrices (30 deg rotation + scaling)
angle = np.deg2rad(30)
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])
scale = np.array([[1.2, 0.0], [0.0, 0.9]])

T = rotation @ scale
transformed = coords @ T.T

print("Original Coordinates:\n", coords)
print("Transformed Coordinates:\n", np.round(transformed, 2))
print("Determinant:", round(np.linalg.det(T), 4))
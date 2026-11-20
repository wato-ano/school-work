import numpy as np

# Adjacency matrix for staff movement between [Triage, ICU, Surgery, Recovery]
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

# Find dominant eigenvalue and corresponding eigenvector for centrality
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))

# Normalize to get percentage of importance
centrality = dominant_vector / dominant_vector.sum()
wards = ["Triage", "ICU", "Surgery", "Recovery"]

print("Ward Infection Centrality Scores:")
for ward, score in zip(wards, centrality):
    print(f"{ward}: {score:.4f}")
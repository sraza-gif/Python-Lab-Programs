import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

print("Matrix:")
print(A)

determinant = np.linalg.det(A)
print("\nDeterminant:", determinant)

inverse = np.linalg.inv(A)
print("\nInverse:")
print(inverse)

rank = np.linalg.matrix_rank(A)
print("\nRank:", rank)
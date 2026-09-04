import numpy as np

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# Without NumPy

addition = [
    [A[i][j] + B[i][j] for j in range(2)]
    for i in range(2)
]

subtraction = [
    [A[i][j] - B[i][j] for j in range(2)]
    for i in range(2)
]

multiplication = [
    [
        sum(A[i][k] * B[k][j] for k in range(2))
        for j in range(2)
    ]
    for i in range(2)
]

transpose = [
    [A[j][i] for j in range(2)]
    for i in range(2)
]

print("Without NumPy")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Transpose:", transpose)


# With NumPy

A_np = np.array(A)
B_np = np.array(B)

print("\nWith NumPy")

print("Addition:")
print(A_np + B_np)

print("Subtraction:")
print(A_np - B_np)

print("Multiplication:")
print(A_np @ B_np)

print("Transpose:")
print(A_np.T)
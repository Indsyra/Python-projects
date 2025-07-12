import numpy as np

# Create a 2X2 matrix
matrix = np.array([[1, 2], [3, 4]])
print(matrix)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Addition
print("Addition:\n", A + B)

# Substraction
print("Substraction\n", A - B)

# Multiplication (element wise multiplication)
print("Element-wise Multiplication\n", A * B)

# Dot Product (Sums the product of the same elements)
print("Dot product:\n", np.dot(A, B))

# Transpose
print("Transpose of A (np.transpose):\n", np.transpose(A))
print("Transpose of A (A.T):\n", A.T)

# Determinant of the matrix (immutable or have inverse)
det = np.linalg.det(A)
print("Determinant: \n", det)

# Get the inverse of a matrix
if det != 0:
    inverse = np.linalg.inv(A)
    print("Inverse:\n", inverse)
else:
    print("Matrix is not invertable.\n")
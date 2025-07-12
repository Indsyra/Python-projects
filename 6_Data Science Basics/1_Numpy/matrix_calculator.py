# Accepts to matrixes as inputs

import numpy as np


# Function to build vector
def build_vector(n):
    try:
        print(f"Enter the {n} vector elements")
        elements = list(map(float, input().split()))
        if len(elements) != n:
            raise ValueError("Number of vector elements doesn't match.")
        return np.array(elements)
    except ValueError as e:
        print(f"Error : {e}")
        return None


# Function to Get Matrix Input
def get_matrix():
    try:
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))
        print("Enter the matrix elements row by row")
        elements = []
        for _ in range(rows):
            row = list(map(float, input().split()))
            if len(row) != columns:
                raise ValueError("Number of columns doesn't match.")
            elements.append(row)
        return np.array(elements)
    except ValueError as e:
        print(f"Error : {e}")
        return None


# Single Matrix Operations
def single_matrix_operation(A):
    # Transpose
    print("\nTranspose of A:\n", np.transpose(A))

    try:
        # Determinant of the matrix (immutable or have inverse)
        print("\nDeterminant: \n", np.linalg.det(A))
    except ValueError:
        print("\nDeterminant or A: Not Applicable (Matrix must be square).")

    try:
        # Get the inverse of a matrix
        print("\nInverse of A:\n", np.linalg.inv(A))
    except np.linalg.LinAlgError:
        print("\nInverse of A: Matrix is not invertable (determinant < 0) or "
              "not square.\n")


# Matrix Operations
def matrix_operation(A, B):
    print("\nMatrix A:\n", A)
    print("\nMatrix B:\n", B)

    try:
        # Addition
        print("\nAddition:\n", A + B)
    except ValueError:
        print("\nAddition: Matrices must have the same dimensions.")

    try:
        # Substraction
        print("\nSubstraction\n", A - B)
    except ValueError:
        print("\nSubstraction: Matrices must have the same dimensions.")

    try:
        # Multiplication (element wise multiplication)
        print("\nElement-wise Multiplication\n", A * B)
    except ValueError:
        print("\nElement-wise Multiplicatio: Matrices must have "
              "the same dimensions.")

    try:
        # Dot Product (Sums the product of the same elements)
        print("\nDot product:\n", np.dot(A, B))
    except ValueError:
        print("\nDot product: Number of columns of matrix A must equal number "
              "of rows of matrix B.")


# Main Program
def main():
    while True:
        print("\nMatrix Calculator")
        print("=================")
        print("1. Operations on two matrices")
        print("2. Operations on a single matrix")
        print("3. Multiplication between a scalar and a matrix")
        print("4. Multiplication between a vector and a matrix")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\nInput Matrix A: ")
            A = get_matrix()
            if A is None:
                print("Two matrices are mandatory for this operation")
                return

            print("\nInput Matrix B: ")
            B = get_matrix()
            if B is None:
                print("Two matrices are mandatory for this operation")
                return

            matrix_operation(A, B)
        elif choice == '2':
            print("\nInput Matrix A: ")
            A = get_matrix()
            if A is None:
                print("One matrix is mandatory for this operation")
                return

            single_matrix_operation(A)

        elif choice == '3':
            try:
                scalar = int(input("Enter the scalar: "))
                print("\nInput Matrix: ")
                A = get_matrix()
                if A is None:
                    print("One matrix is mandatory for this operation")
                    return

                print("\nMultiplication between a scalar and a Matrix:\n", scalar * A)
            except ValueError:
                print("Incorrect entry. Please retry.")
                return

        elif choice == '4':
            print("\nInput Matrix: ")
            A = get_matrix()
            if A is None:
                print("One matrix is mandatory for this operation")
                return

            print("\nInput Vector: ")
            B = build_vector(A.shape[1])
            if B is None:
                print("One vector is mandatory for this operation")
                return

            print("\nMultiplication between a vector and a Matrix:\n", A * B)

        elif choice == '5':
            print("Thank you for using Matrix Calculator. Goodbye !")
            break
        else:
            print("Invalid option. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()

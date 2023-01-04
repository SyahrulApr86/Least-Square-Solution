import numpy as np

# Least Square Solution
matrix = []

total_equations = int(input("Enter the number of equations: "))
total_variables = int(input("Enter the number of variables: "))
print("Enter the coefficients of the equations:")
for i in range(total_equations):
    row = input()
    row = row.split()
    row = [float(i) for i in row]
    matrix.append(row)

matrix = np.array(matrix)

# enter the constants
constants = []
print("Enter the constants:")
for i in range(total_equations):
    constant = float(input())
    constants.append(constant)

constants = np.array(constants)

# transpose the matrix
transpose = matrix.transpose()
print("This is A^T:")
for i in transpose:
    print(i)
print()

# multiply the transpose of the matrix with the matrix
multiply = np.matmul(transpose, matrix)
print("This is A^T * A:")
for i in multiply:
    print(i)
print()

# inverse the matrix multiply
inverse = np.linalg.inv(multiply)
print("This is (A^T * A)^-1:")
for i in inverse:
    print(i)
print()

# multiply the inverse with the transpose of the matrix
multiply2 = np.matmul(inverse, transpose)
print("This is (A^T * A)^-1 * A^T:")
for i in multiply2:
    print(i)
print()

# multiply the multiply2 with the constants
sol = np.matmul(multiply2, constants)

print("The solution is:")
for i in range(total_variables):
    print(f"x{i + 1} = {sol[i]}")
# Path: Least Square Solution\main.py

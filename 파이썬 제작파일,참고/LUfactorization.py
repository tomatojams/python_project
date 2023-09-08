import numpy as np

matrixinitial = np.array([[2.0, 6.0, 2.0], [-3.0, -8.0, 0.0], [4.0, 9.0, 2.0]])

global matrix
matrix = matrixinitial
global matrix1, matrix2

u11 = matrix[0, 0]
u12 = matrix[0, 1]
u13 = matrix[0, 2]

l21 = matrix[1, 0] / u11
u22 = matrix[1, 1] - (l21 * u12)
u23 = matrix[1, 2] - l21 * u13

l31 = matrix[2, 0] / u11
l32 = (matrix[2, 1] - l31 * u12) / u22
u33 = matrix[2, 2] - l31 * u13 - l32 * u23


matrix1 = [[1.0, 0.0, 0.0], [l21, 1.0, 0.0], [l31, l32, 1.0]]

matrix2 = [[u11, u12, u13], [0.0, u22, u23], [0.0, 0.0, u33]]
print("분해전")
print(matrixinitial)

print("분해후")
print("L")
print(matrix1[0], "\n", matrix1[1], "\n", matrix1[2])
print("U")
print(matrix2[0], "\n", matrix2[1], "\n", matrix2[2])

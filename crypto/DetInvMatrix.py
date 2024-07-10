import numpy as np

matrix = np.array([
    [17, 17, 5],
    [21, 18, 21],
    [2, 2, 19]
])

def determinant_matrix(matrix):
 
    determinant = np.linalg.det(matrix)
    return determinant

def inverse_matrix(matrix):
  
    inverse_matrix = np.linalg.inv(matrix)
    return inverse_matrix

print("Determinant of the matrix:\n", determinant_matrix(matrix))
print("Inverse of the matrix:\n", inverse_matrix(matrix))

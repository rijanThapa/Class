import numpy as np


matrix = [[5, 10],
          [9, 7]]

a = matrix[0][0]
b = matrix[0][1]
c = matrix[1][0]
d = matrix[1][1]


det = a * d - b * c

print("Matrix is:\n")
for row in matrix:
    print(row)

print("\nDeterminant is:", det)


if det == 0:
    print("The matrix is singular, and its inverse does not exist.")
else:
  
    inverse = [[d / det, -b / det],
               [-c / det, a / det]]

 
    print("\nInverse Matrix:")
    for row in inverse:
        print(row)

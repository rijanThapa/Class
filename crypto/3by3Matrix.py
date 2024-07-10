import numpy as np

np.set_printoptions(precision=4)


matrix = np.array([[17, 17, 5],
                   [21, 18, 21],
                   [2, 2, 19]])


a = matrix[0][0]
b = matrix[0][1]
c = matrix[0][2]
d = matrix[1][0]
e = matrix[1][1]
f = matrix[1][2]
g = matrix[2][0]
h = matrix[2][1]
i = matrix[2][2]


det = (a * e * i + b * f * g + c * d * h) - (a * f * h + b * d * i + c * e * g)

print("Matrix is:\n")
for row in matrix:
    print(row)

print("\nDeterminant:", det)


if det == 0:
    print("The matrix is singular, and its inverse does not exist.")
else:
   
    inv_a = (e * i - f * h) / det
    inv_b = (c * h - b * i) / det
    inv_c = (b * f - c * e) / det
    inv_d = (f * g - d * i) / det
    inv_e = (a * i - c * g) / det
    inv_f = (c * d - a * f) / det
    inv_g = (d * h - e * g) / det
    inv_h = (b * g - a * h) / det
    inv_i = (a * e - b * d) / det

  
    inverse = np.array([[inv_a, inv_b, inv_c],
                        [inv_d, inv_e, inv_f],
                        [inv_g, inv_h, inv_i]])

   
    inverse_mod_26 = (inverse % 26).astype(int)

    print("\nInverse Matrix (mod 26):")
    for row in inverse_mod_26:
        print(row)

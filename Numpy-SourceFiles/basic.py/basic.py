import numpy as np

x=np.random.random()
print("Random number: ", x)
x_square_root=np.sqrt(x)
print("Number square root: ", x_square_root)
print("x^sqrt(x): ", np.power(x, x_square_root))
matrix = np.random.random(3)
print("Random matrix: ", matrix)
matrix = np.append(matrix, np.random.random(2))
print("New matrix: ", matrix)
print("Sine of matrix: ", np.sin(matrix))
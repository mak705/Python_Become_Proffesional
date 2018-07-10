import numpy as np
A=np.array([[1,2],[3,4]])
print("A matrix: ")
print(A)
print("Covariance= ")
print(np.cov(A))

def gauss(x, sigma):
    return np.exp(-x**2/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))

G_matrix_1 = gauss(np.linspace(-5,5,10), 1)
print("G_matrix_1: ")
print(G_matrix_1)
G_matrix_2 = gauss(np.linspace(-5,5,10), 2)
print("G_matrix_2: ")
print(G_matrix_2)
G_matrix = [[],[]]
print("G_matrix: ")
print(G_matrix)
G_matrix[0]= G_matrix_1
G_matrix[1]= G_matrix_2
print("Covariance of two different Gauss functions: ")
print(np.cov(G_matrix))
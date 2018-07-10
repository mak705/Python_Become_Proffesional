import scipy as sp

A=sp.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("Matrix A")
print(A)
B=A.copy()
B[:,3]=[0,0,1,0]
print("Matrix B")
print(B)
C=B.copy()
C[3,:]=[0,0,1,0]
print("Matrix C")
print(C)
print("A-C=")
print(A-C)
print("A*C=")
print(sp.dot(A,C))
import numpy as np

mvalues = [0,1,5,6,80]
print(mvalues)
M = np.array(mvalues)
print("M= ", M)
print(M * 39.3701) #conversion to inches

x=np.arange(20,104.75,3.6)
print("x np.arange=", x)
x=np.linspace(20,104.75, 10, endpoint=False)
print("x np.linspace = ", x)

_,spacing = np.linspace(20,104.75, 10, retstep=True) #returns spacing,_ is because we don't care about the actual array now
print("Spacing between the items in array above: ", spacing)
x=np.array([1,2,3,4])
print("x array: ", x)
print("The type of x: ", type(x))
print("The dimension of x: ", np.ndim(x))

x=np.array([ [[1,2], [3,4]],
            [[5,6], [7,8]],
            [[9,10],[11,12]] ]
    )
print("3 dimensional array: ")
print(x)
print("number of dimensions: ", x.ndim) #number of dimensions
print("Shape of the array: ", np.shape(x))
print("Sliced array: ", x[1][1][0])
X=np.arange(24).reshape(4,6) #creates 4x6 array of elements from 0 to 23
print("X = ")
print(X)
print(X[::2, ::3]) #takes every 3rd item in every 2nd row
Z=np.zeros((3,5))
print("Z=")
print(Z)
I=np.identity(4)
print("I=")
print(I)
print(np.eye(5,8,k=1,dtype=int)) #k defines position of diagonal. If k=0, we get ones on [0][0], [1][1] etc... with k=1, we get them on [0][1],[1][2]...
#So we get elements equal to 1 on [i][i+k] where i is row index, and all the other elements are set to 0

import scipy as sp
x = sp.random.random()
print("Random number: ", x)

x_square_root = sp.sqrt(x)
print("Number square root: ", x_square_root)

matrix = sp.random.random(3)
print("Random matrix: ", matrix)

matrix = sp.append(matrix, sp.random.random(2))
print("New matrix: ", matrix)

def add(x,y):
    return x+y

print("1+2 = ", add(1,2))

def subtract(x,y):
    return x-y

print("5-6 = ", subtract(5,6))

def multiply(x,y):
    return x*y

print("44*9.4= ", multiply(44,9.4))

def divide(x,y):
    if y:
        return x/y
    else:
        return "Can't divide by zero"
    
print("444/5 = ", divide(444,5))
print("333/0 = ", divide(333,0))
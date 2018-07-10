import scipy as sp
import scipy.integrate as integrate
from scipy import signal
from scipy.integrate import dblquad

result = integrate.quad(lambda x: x, 0, 4.5)
print("Result of integration of x on interval [0,4.5]: ", result[0])

def gauss(x, sigma):
    return sp.exp(-x**2/(2*sigma**2))/(sigma*sp.sqrt(2*sp.pi))
result = integrate.quad(lambda x:gauss(x,1), -sp.inf, sp.inf)
print("Result of integration of Gaussian function on infinite interval: ", result[0])

area = dblquad(lambda x, y: 1,0,10, lambda x: 0, lambda x: 10-x)
print("Area of right triangle with sides a=10, b=10: ", area[0])
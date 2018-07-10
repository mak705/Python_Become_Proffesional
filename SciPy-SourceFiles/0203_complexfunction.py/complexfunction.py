import scipy as sp
from scipy import linalg

def norm(start, end, number_of_elements):
    xs = sp.linspace(start, end, number_of_elements);
    return linalg.norm(xs)

print(norm(2,3,100))

#find_max_norm([0,1], [3,4], 4)
#[0,1,2,3], [0,1.33,2.66,4], [1,1.66, 2.33, 3], [1,2,3,5]
# =5.477

def find_max_norm(start_range, end_range, number_of_elements):
    maximum = 0
    for i in start_range:
        for j in end_range:
            x=norm(i,j,number_of_elements)
            if x > maximum:
                maximum = x
    return maximum

print(find_max_norm(sp.linspace(0,1,10), sp.linspace(0,5,10),100))
        
import numpy as np

#Solving the system in matrix form

"""a = np.matrix("1,1,1;0.05,0.07,0;0.05,0,0.06")
b = np.matrix("50000;2250;1400")
a_inv = np.linalg.inv(a)
x = a_inv.dot(b)
print(x)"""

#solv method

"""a = np.matrix("1,1,1;0.05,0.07,0;0.05,0,0.06")
b = np.matrix("50000;2250;1400")
#x = np.linalg.solve(a,b)
print(x)"""

#p.array + operator @

a = np.array([
    [1, 1, 1],
    [0.05, 0.07, 0],
    [0.05, 0, 0.06]
])

b = np.array([50000, 2250, 1400])
x = np.linalg.solve(a, b)
print(x)

b_check = a @ x
print(b_check)
print(np.allclose(b, b_check))
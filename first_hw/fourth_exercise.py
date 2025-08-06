import numpy as np

#Solving the system in matrix form

"""a = np.matrix("1,1,1;9,3,1;1,-1,1")
b = np.matrix("12;54;2")
a_inv = np.linalg.inv(a)
x = a_inv.dot(b)
print(x)"""

#solv method

"""a = np.matrix("1,1,1;9,3,1;1,-1,1")
b = np.matrix("12;54;2")
x = np.linalg.solve(a,b)
print(x)"""

#p.array + operator @

a = np.array([
    [1, 1, 1],
    [9, 3, 1],
    [1, -1, 1]
])

b = np.array([12, 54, 2])
x = np.linalg.solve(a, b)
print(x)

b_check = a @ x
print(b_check)
print(np.allclose(b, b_check))
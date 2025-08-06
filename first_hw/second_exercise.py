import numpy as np

#Solving the system in matrix form

a = np.matrix("1,1,1;1,-1,0;1,0,-1")
b = np.matrix("1328;-120;100")
a_inv = np.linalg.inv(a)
x = a_inv.dot(b)
print(x)

#solv method

"""a = np.matrix("1,1,1;1,-1,0;1,0,-1")
b = np.matrix("1328;-120;100")
x = np.linalg.solve(a,b)
print(x)"""

#p.array + operator @

"""a = np.array([
    [1, 1, 1],
    [1, -1, 0],
    [1, 0, -1]
])

b = np.array([1328, -120, 100])
x = np.linalg.solve(a, b)
print(x)

b_check = a @ x
print(b_check)
print(np.allclose(b, b_check))"""
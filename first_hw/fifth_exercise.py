import numpy as np

def get_polynom(coords):
    n = len(coords)

    A = np.zeros((n, n))
    B = np.zeros(n)

    for i, (x, y) in enumerate(coords):
        for j in range(n):
            A[i, j] = x ** j
        B[i] = y

    coefficients = np.linalg.solve(A, B)

    return coefficients

coords = [(3, 4), (2, 7), (5, -12), (8, 9), (1, 14)]
coefficients = get_polynom(coords)
print(coefficients)

import numpy as np

"""def get_polynom(coords):
    n = len(coords)

    A = np.zeros((n, n))
    B = np.zeros(n)

    # x та y беруться з список кортежей, починаючи з 0 індекса де x = 3, y = 4 і т.д.
    for i, (x, y) in enumerate(coords):
        for j in range(n):
            A[i, j] = x ** j
        B[i] = y

    coefficients = np.linalg.solve(A, B)

    return coefficients
 
# Координати осі x не повинні бути однаковими
coords = [(3, 4), (2, 7), (4, -12), (8, 9), (1, 14)]
coefficients = get_polynom(coords)
print(coefficients)"""

# Створенно за допомогою ChatGPT
# np.polyfit виконує поліномальну апроксимацію, тобто найкраще наближення у випадку, якщо точки не лежать точно на одному поліномі.

"""def get_polynom(coords):
    # Координати х та у
    x = np.array([point[0] for point in coords])
    y = np.array([point[1] for point in coords])

    # Ступінь полінома = кількість точок - 1
    degree = len(coords) - 1
    print(degree)
    # Знаходимо коефіцієнти полінома
    coeffs = np.polyfit(x, y, degree)

    # polyfit повертає коефіцієнти у порядку: [cn, ..., c1, c0]
    # Якщо потрібен зворотній порядок (від c0 до cn), можна:
    coeffs = coeffs[::-1]

    return coeffs

coords = [(1, 12), (3, 54), (-1, 2)]
coeffs = get_polynom(coords)
print( coeffs)"""

#Цей метод працює лише тоді, коли матриця 𝐴 є оберненою, тобто не має лінійно залежних рядків (наприклад, однакових 𝑥-координат).
"""def get_polynom(coords):
    n = len(coords)
    
    A = np.zeros((n, n))
    B = np.zeros(n)

    for i, (x, y) in enumerate(coords):
        '''Кожен рядок A: [x^0, x^1, ..., x^(n-1)]
        result = []
        for j in range(n):
        result.append(x ** j)
        Коротка запис цього циклу приведено нижче'''
        A[i] = [x ** j for j in range(n)]
        B[i] = y

    A_inv = np.linalg.inv(A)

    # Матричне множення: C = A_inv * B
    C = A_inv @ B

    return C

coords = [(1, 12), (3, 54), (-1, 2)]
coeffs = get_polynom(coords)
print(coeffs)"""
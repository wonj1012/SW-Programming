"""
2023-04-05
"""

from typing import Dict
from time import time

def fibonacci(n: int) -> Dict[int, int]:
    fib = {0: 0, 1: 1}

    for i in range(n-1):
        fib[i+2] = fib[i] + fib[i+1]

    return fib[n]

def matrix_mult(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    elif n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return matrix_mult(half_power, half_power)
    else:
        return matrix_mult(matrix, matrix_power(matrix, n - 1))

def fibonacci_matrix_power(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        matrix = [[1, 1], [1, 0]]
        return matrix_power(matrix, n - 1)[0][0]


if __name__ == "__main__":
    start_time = time()
    result = fibonacci(10)
    print(time() - start_time)

    start_time = time()
    result = fibonacci_matrix_power(10)
    print(time() - start_time)

"""
2023-04-05
"""

from typing import Dict

def fibonacci(n: int) -> Dict[int, int]:
    """

    """
    fib = {0: 0, 1: 1}

    for i in range(n-1):
        fib[i+2] = fib[i] + fib[i+1]

    return fib


if __name__ == "__main__":
    print(fibonacci(10))

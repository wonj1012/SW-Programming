"""
2023-03-29
"""

from typing import List, Tuple
from time import time

def q1(n: int):
    """
    3.6.1
    """
    for i in range(n - 1, -1, -1):
        print(' ' * i + '#')


def q2(n: int):
    """
    3.6.2
    """
    for i in range(n):
        print(' ' * (n - i - 1) + '+' * (2 * i + 1))
    
def get_primes(num: int) -> Tuple[List[int], float]:
    """
    Sieve of Eratosthenes
    """
    start_time = time()
    sieves = [True] * (num + 1)

    for n in range(2, int(num**0.5) + 1):
        if sieves[n]: # is prime
            for i in range(n + n, num + 1, n):
                sieves[i] = False
    
    return [i for i in range(2, num) if sieves[i] == True], time() - start_time

def get_primes_class(num: int) -> Tuple[List[int], float]:
    start_time = time()
    primes = []

    for n in range(2, num + 1):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
        if is_prime:
            primes.append(n)

    return primes, time() - start_time

if __name__ == "__main__":
    # q1(7)
    # q2(5)
    primes, elapsed_time = get_primes(50000)
    primes_c, elapsed_time_c = get_primes_class(50000)
    print(len(primes), len(primes_c))
    print(elapsed_time, elapsed_time_c, elapsed_time_c / elapsed_time)

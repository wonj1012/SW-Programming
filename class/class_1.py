"""
2023-03-29
"""

from typing import List, Tuple
from time import time
    
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

def even_odd_sum(a: int, b: int) -> Tuple[Tuple[int, int], float]:
    """
    주어진 폐구간 내 짝수의 합과 홀수의 합을 반환합니다.
    시간 복잡도는 O(1)

    Args:
        a (int): 폐구간의 시작값
        b (int): 폐구간의 끝값

    Returns:
        Tuple[Tuple[int, int], float]: (폐구간 내의 짝수의 합, 홀수의 합), 걸린 시간
    """
    start_time = time()
    even_sum = ( (b//2) * (b//2 + 1) - (a//2) * (a//2 - 1) ) if a % 2 == 0 else ( (b//2) * (b//2 + 1) - ((a-1)//2) * ((a-1)//2) )
    odd_sum = ( ((b+1)//2) ** 2 - (a//2) ** 2 + 1) if a % 2 == 0 else ( ((b+1)//2) ** 2 - ((a+1)//2) ** 2 + 1 )
    return (even_sum, odd_sum), time() - start_time

def even_odd_sum_class(a: int, b: int) -> Tuple[Tuple[int, int], float]:
    """
    주어진 폐구간 내 짝수의 합과 홀수의 합을 반환합니다.
    시간 복잡도는 O(n)

    Args:
        a (int): 폐구간의 시작값
        b (int): 폐구간의 끝값

    Returns:
        Tuple[Tuple[int, int], float]: (폐구간 내의 짝수의 합, 홀수의 합), 걸린 시간
    """
    start_time = time()

    even_sum = 0
    odd_sum = 0

    for n in range(a, b+1):
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n

    return (even_sum, odd_sum), time() - start_time

if __name__ == "__main__":
    # get_primes functions comparison
    primes, elapsed_time = get_primes(50000)
    print(len(primes), elapsed_time)
    primes_c, elapsed_time_c = get_primes_class(50000)
    print(len(primes_c), elapsed_time_c)
    print(elapsed_time_c / elapsed_time)

    # even_odd_sum functions comparison
    print(even_odd_sum(1, 500000000))
    print(even_odd_sum_class(1, 500000000))


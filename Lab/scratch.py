from typing import List

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
        
def get_primes(num: int) -> List[int]:
    primes = []
    for n in range(2, num + 1):
        is_prime = True
        
        for prime in primes:
            if n < prime ** 2:
                break
            
            if n % prime == 0:
                is_prime = False
                break
            
        if is_prime:
            primes.append(n)
            
    return primes

if __name__ == "__main__":
    # q1(7)
    # q2(5)
    print(get_primes(100))
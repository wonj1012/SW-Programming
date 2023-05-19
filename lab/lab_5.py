"""
SW Programming Lab #5
Name: 최원재
ID: 2020147530
Date: 2023-05-17
"""

from functools import reduce


def q1() -> None:
    def sub(n1: int, n2: int) -> int:
        return n1 - n2

    num1, num2 = map(int, input("두 수를 입력: ").split())

    print(f"{num1} - {num2} = {sub(num1, num2)}")
    print(f"{num1} - {num2} = {(lambda x, y: x - y)(num1, num2)}")


def q2() -> None:
    nums = list(range(1, 11))

    E1_list = []
    for even_num in filter(lambda x: x % 2 == 0, nums):
        E1_list.append(even_num)

    E2_list = [x for x in filter(lambda x: x % 2 == 0, nums)]

    print(f"E1_list = {E1_list}")
    print(f"E2_list = {E2_list}")


def q3() -> None:
    def to_upper(s: str) -> str:
        return s.upper()

    a_list = input("소문자 입력: ").split()

    A1_list = list(map(to_upper, a_list))
    A2_list = list(map(lambda x: x.upper(), a_list))

    print(f"a_list = {a_list}")
    print(f"A1_list = {A1_list}")
    print(f"A2_list = {A2_list}")


def q4() -> None:
    i_list = list(map(int, input("정수 입력: ").split()))

    F1_list = list(map(float, i_list))
    F2_list = list(map(lambda x: float(x), i_list))

    print(f"F1_list = {F1_list}")
    print(f"F2_list = {F2_list}")


def q5() -> None:
    a, b, n = map(int, input("a, b, n 입력: ").split())

    ab_sum = reduce(lambda x, y: x + y, range(a, b + 1))
    n_factorial = reduce(lambda x, y: x * y, range(1, n + 1))

    print(f"{a} ~ {b}의 합 = {ab_sum}")
    print(f"{n}! = {n_factorial}")


def q6() -> None:
    string = input("문자열 입력: ")
    words = string.split()
    first_letters = [word[0] for word in words]

    print(f"입력된 문자열 = {words}")
    print(f"첫번째 문자들 = {first_letters}")


if __name__ == "__main__":
    print("\n==================== Q1 ====================")
    q1()
    print("\n==================== Q2 ====================")
    q2()
    print("\n==================== Q3 ====================")
    q3()
    print("\n==================== Q4 ====================")
    q4()
    print("\n==================== Q5 ====================")
    q5()
    print("\n==================== Q6 ====================")
    q6()

"""
Name: 최원재
Code: 2020147530
Date: 2023-04-26
2023-1 Midterm Exam
"""


def q1() -> None:
    """
    종이를 1/2씩 접으면서 종이 면적이 1/100보다 작아지기까지 접은 횟수를 출력합니다.
    """
    initial_area = float(input("초기 종이 면적: "))
    area = initial_area
    count = 0
    while area >= initial_area / 100:
        area /= 2
        count += 1
        print(f"1번 접은 후 종이 면적 : {area:.6f}")
    print("-----------------------------------")
    print(f"1/100 보다 작아지기까지 접은 횟수 : {count} 번")
    print("-----------------------------------")


def q2() -> None:
    """
    1 - 2 + 3 - 4 + ... + n 항까지의 합을 출력합니다.
    """
    n = int(input("정수 입력: "))
    count = 1
    total = 0
    sign = -1
    while count <= n:
        total += sign * count**2
        sign *= -1
        count += 1
    print(f"{n}항까지의 합 : {total}")


def q3() -> None:
    """
    행의 갯수를 입력받아 다음과 같은 모양을 출력합니다.
    1 2 3 4 5
     1 2 3 4
      1 2 3
       1 2
        1
    """
    line_num = int(input("행의 갯수 : "))
    for i in range(line_num, 0, -1):
        buffer = " " * (line_num - i)
        for j in range(1, i+1):
            buffer += f"{j} "
        print(buffer)


def q4() -> None:
    """
    실수 a, b (a<b), 간격을 입력 받아 다음 수식의 결과를 출력합니다.
    y = (x^2 + 5x - 7) / (3x + 2)
    """
    a = float(input("a 입력 : "))
    b = float(input("b 입력 : "))
    step = float(input("간격 입력 : "))
    assert (a < b)
    while a <= b:
        y = (a**2 + 5*a - 7) / (3*a + 2)
        print(f"x = {a:.6f} , y = {y:.6f}")
        a += step


class Q5:
    def __init__(self) -> None:
        self.menu_dict = {
            0: {'name': "quit", 'price': 0},
            1: {'name': "ivory", 'price': 23400},
            2: {'name': "tommy", 'price': 38500},
            3: {'name': "arena", 'price': 21000},
            4: {'name': "metro", 'price': 36500},
            5: {'name': "coach", 'price': 45000}
        }

        self.total_price = 0

    def __order(self) -> bool:
        """
        Order a menu.

        Returns:
            bool: True if the user wants to continue ordering.
        """
        code = int(input("메뉴 선택 :> "))

        while code not in self.menu_dict.keys():
            code = int(input("메뉴 재선택 :> "))

        if code == 0:
            return False
        else:
            self.total_price += self.menu_dict[code]['price']
            return True

    def run(self) -> None:
        """
        Run the program.
        """
        for code, menu in self.menu_dict.items():
            print(f"{code} - {menu['name']} : {menu['price']}")
        print("------------------------")

        while self.__order():
            pass

        print("------------------------")
        print(f"결제총액 : {self.total_price} 원")
        print("------------------------")


if __name__ == "__main__":
    q1()
    q2()
    q3()
    q4()
    Q5().run()

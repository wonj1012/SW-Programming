"""
Name: 최원재
Code: 2020147530
Date: 2023-04-26
Last Midterm Exam
"""

def q1() -> None:
    star_num = int(input("별의 개수 입력: "))
    for i in range(star_num):
        print(" " * i + "*" * (star_num - i))

def q2() -> None:
    radius = float(input("반지름 입력: "))
    sqrt_radius = int(radius ** 0.5)
    print(sqrt_radius)
    for x in range(sqrt_radius + 1):
        for y in range(sqrt_radius + 1):
            if x ** 2 + y ** 2 <= radius ** 2:
                print(f"({x}, {y})")

def q3() -> None:
    threshold = float(input("경계값 입력: "))
    value = 0
    sign = 1
    numerator = 1
    denominator = 2
    num = 0
    while value <= threshold:
        value += sign * numerator / denominator
        sign *= -1
        numerator += 1
        denominator += 1
        num += 1
    print(f"항의 개수: {num}")
    print(f"합: {value}")

def q4() -> None:
    PI = 3.141592

    # 입력: 초기 도우 반지름
    initial_radius = float(input("초기 도우 반지름 : "))

    # 도우 면적 계산
    def calculate_area(radius):
        return PI * (radius ** 2)

    initial_area = calculate_area(initial_radius)
    print(f"초기 도우 면적 : {initial_area:.6f}")

    # 도우 던지기 시뮬레이션
    throw_count = 0
    current_radius = initial_radius
    current_area = initial_area

    while current_area < initial_area * 2:
        throw_count += 1
        current_radius *= 1.1  # 반지름 10% 증가
        current_area = calculate_area(current_radius)
        print(f"{throw_count}번 던진 후 도우 면적 : {current_area:.6f}")

    # 결과 출력
    print("-" * 30)
    print(f"2배 이상 되기까지 던진 횟수 : {throw_count}번")
    print("-" * 30)


class Q5:
    def __init__(self) -> None:
        self.menu_dict = {
            1: {'name': 'steak', 'price': 25000},
            2: {'name': 'pizza', 'price': 28500},
            3: {'name': 'pasta', 'price': 14000},
            4: {'name': 'hamburger', 'price': 8500},
            5: {'name': 'sandwitch', 'price': 4500}
        }
        self.guest_num = 0
        self.total_price = 0
    
    def receive_order(self, code) -> bool:
        if code in self.menu_dict:
            self.total_price += self.menu_dict[code]['price']
            return True
        else:
            return False
        
    def run(self) -> None:
        for code, menu in self.menu_dict.items():
            print(f"{code} - {menu['name']} : {menu['price']}")
        print("-----------------------------------")
        guest_num = int(input("인원수 입력 :> "))
        for _ in range(guest_num):
            code = int(input("메뉴 선택 :> "))
            while not self.receive_order(code):
                code = int(input("메뉴 재선택 :> "))
        print("-----------------------------------")
        print(f"결제 총액: {self.total_price}원")
        print("-----------------------------------")
        
if __name__ == "__main__":
    q1()
    q2()
    q3()
    q4()
    Q5().run()
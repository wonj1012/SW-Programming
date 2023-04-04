"""
SW Programming Lab #2
Name: 최원재
ID: 2020147530
"""

def q1(my_name: str) -> bool:
    """
    입력받은 이름과 인자로 받은 이름이 같은지 확인하여 출입 가능 여부를 반환합니다.

    Args:
        my_name (str): 인자로 받은 이름.

    Returns:
        bool: 입력받은 이름과 인자로 받은 이름이 같은 경우 True, 다른 경우 False를 반환합니다.
    """
    if input("이름 입력: ") == my_name:
        print("출입가능")
        return True
    else:
        print("출입통제")
        return False

def q2(password: str) -> bool:
    """
    입력받은 비밀번호와 인자로 받은 비밀번호가 같은지 확인하여 메세지를 출력하고 결과를 반환합니다.

    Args:
        password (str): 인자로 받은 비밀번호.

    Returns:
        bool: 입력받은 비밀번호와 인자로 받은 비밀번호가 같은 경우 True, 다른 경우 False를 반환합니다.
    """
    if input("비밀번호 네 자리를 입력하시오.: ") == password:
        print("한 개의 메세지")
        return True
    else:
        print("잘못 입력 하셨습니다.")
        return False

def q3():
    """
    출생 후 경과한 개월 수를 입력받고, 각 백신 접종 대상 여부를 출력합니다.
    """
    vacc = {
        "결핵": (0, 1),
        "B형간염": (0, 2),
        "파상풍": (1, 6),
        "폐렴구균": (1, 15)
    }

    month = int(input("출생 후 몇 개월이 경과되었습니까?: "))

    for disease in vacc:
        if vacc[disease][0] <= month <= vacc[disease][1]:
            print(disease)

def q4() -> bool:
    """
    각 성분의 함량을 입력받아, 각 성분의 함량이 최소 요구량보다 큰지 확인하고, 생산 허가 여부를 출력합니다.

    Returns:
        bool: 각 성분의 함량이 최소 요구량보다 작은 경우 False, 모두 큰 경우 True를 반환합니다.
    """
    min_value = {
        "a": 40,
        "b": 350,
        "c": 17
    }

    for component in min_value:
        if int(input(f"{component} 성분의 함량을 입력(mg): ")) < min_value[component]:
            print("허가를 보류함")
            return False

    print("생산을 허가함")
    return True

def q5():
    """
    이름, 키, 몸무게를 입력받아, BMI 지수와 상태를 출력합니다.
    """
    name = input("이름을 입력하세요: ")
    height = float(input("키(cm)를 입력하세요: "))
    weight = float(input("몸무게(kg)를 입력하세요: "))
    bmi = weight / (height/100)**2

    status = ""
    if bmi < 22.9:
        status = "정상"
    elif bmi < 24.9:
        status = "과체중"
    elif bmi < 29.9:
        status = "비만"
    else:
        status = "고도비만"

    print(f"{name}님의 키는 {height}cm이고 몸무게는 {weight}kg입니다."
          f"BMI 지수는 {bmi}입니다. {status}입니다.")
    
def q6():
    """
    음료수의 종류와 가격을 딕셔너리로 저장하고, 금액과 선택한 음료수를 입력받아, 거스름돈과 함께 음료수를 출력합니다.
    """
    beverage_dict = {
        1: {'name': "사이다", 'price': 1500},
        2: {'name': "콜라", 'price': 1800},
        3: {'name': "물", 'price': 1200}
    }

    for beverage in beverage_dict.values():
        print(f"{beverage['name']}-{beverage['price']}", end=' ')

    print("\n================================")
    money = int(input("금액을 입력하시오: "))
    if money < 0: return

    print("선택)", end=' ')
    for index in beverage_dict:
        print(f"{index}-{beverage_dict[index]['name']}", end=' ')
    choice = int(input(": "))

    selected_beverage = beverage_dict[choice]

    if (money - selected_beverage['price']) < 0:
        print(f"음료를 사실 수 없습니다.\n"
              f"================================\n"
              f"잔돈 {money}원 반환합니다")
        return
    money -= selected_beverage['price']

    josa = '가'
    if (ord(selected_beverage['name'][-1]) - ord('가')) % 28:
        josa = '이'
    
    print(f"{selected_beverage['name']}{josa} 나왔습니다.\n"
          f"================================\n"
          f"잔돈 {money}원 반환합니다.")
    
def q7():
    """
    폐구간 내의 짝수와 홀수의 합을 구하는 코드입니다. for문을 사용합니다.
    """
    a = int(input("a 입력: "))
    b = int(input("b 입력: "))
    if a > b: return

    even_sum = 0
    odd_sum = 0

    for num in range(a, b+1):
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    print(f"{a}부터 {b}까지 짝수의 합은 {even_sum}\n"
          f"{a}부터 {b}까지 홀수의 합은 {odd_sum}\n")

def q8():
    """
    폐구간 내의 짝수와 홀수의 합을 구하는 코드입니다. while문을 사용합니다.
    """
    a = int(input("a 입력: "))
    b = int(input("b 입력: "))
    if a > b: return

    even_sum = 0
    odd_sum = 0
    num = a

    while num <= b:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
        num += 1

    print(f"{a}부터 {b}까지 짝수의 합은 {even_sum}\n"
          f"{a}부터 {b}까지 홀수의 합은 {odd_sum}\n")

def q9(password: str) -> bool:
    """
    입력받은 비밀번호와 인자로 받은 비밀번호가 같은지 확인하여 로그인 여부를 반환합니다.

    Args:
        password (str): 인자로 받은 비밀번호.

    Returns:
        bool: 입력받은 비밀번호와 인자로 받은 비밀번호가 같은 경우 True, 다른 경우 False를 반환합니다.
    """
    num_tries = 0
    
    while num_tries < 5:
        if input("비밀번호 네 자리 입력: ") == password:
            print("로그인")
            return True
        else:
            num_tries += 1
    
    print("5회 입력 오류")
    return False

def q10(answer: int):
    """
    추측한 숫자가 정답과 일치하는지 확인하는 게임입니다. 추측한 숫자가 정답보다 크면 'down', 작으면 'up'을 출력합니다.

    Args:
        answer (int): 정답 숫자.

    Returns:
        None
    """
    while True:
        input_num = int(input("추측한 숫자 입력: "))
        if input_num > answer:
            print("down")
        elif input_num < answer:
            print("up")
        else:
            print("정답")
            return

def q11():
    """
    입력받은 온도와 온도 포맷(C/F)에 따라 화씨와 섭씨를 변환하여 출력합니다.
    """
    print("온도가 섭씨이면 C 또는 c, 화씨이면 F 또는 f를 입력\n")
    temperature_format = input("섭씨(C) or 화씨(F): ").upper()
    tem_input = int(input("온도 입력: "))
    if temperature_format == 'C':
        Celsius = tem_input
        Fahrenheit = Celsius * 9/5 + 32
        print(f"섭씨 {Celsius}°를 화씨로 변환하면 {Fahrenheit:.1f}°입니다.")
        return
    elif temperature_format == 'F':
        Fahrenheit = tem_input
        Celsius = (Fahrenheit - 32) * 5/9
        print(f"화씨 {Fahrenheit}°를 섭씨로 변환하면 {Celsius:.1f}°입니다.")
        return
    else:
        return


if __name__ == "__main__":
    q1("최원재")
    q2("0610")
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()
    q9("1610")
    q10(50)
    q11()

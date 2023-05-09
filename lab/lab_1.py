"""
SW Programming Lab #1
Name: 최원재
ID: 2020147530
Date: 2023-03-15
"""

# input 연습문제 1
from math import pi
age = int(input("당신의 나이는 몇 살입니까? "))
print(f"당신은 {age} 년을 살았습니다.")

# input 연습문제 2
height = int(input("당신의 키는? "))
print(f"당신의 적정 몸무게는 {height - 100} kg 입니다.")

# 단순 계산기(덧셈)
num_1 = int(input("덧셈 첫 번째 숫자는? "))
num_2 = int(input("덧셈 두 번째 숫자는? "))
print(f"두 숫자의 합은 {num_1 + num_2} 입니다.")

# 단순 계산기(나눗셈)
num_1 = int(input("피제수는? "))
num_2 = int(input("제수는? "))
print(f"나눗셈의 몫은 {num_1 // num_2} 나머지는 {num_1 % num_2} 입니다.")

# 성적 계산 프로그램
name = input("이름을 입력하세요 : ")
scores = {}
scores['국어'] = int(input("국어 성적을 입력하세요 : "))
scores['수학'] = int(input("수학 성적을 입력하세요 : "))
scores['사회'] = int(input("사회 성적을 입력하세요 : "))
scores['과학'] = int(input("과학 성적을 입력하세요 : "))
scores['영어'] = int(input("영어 성적을 입력하세요 : "))
total = 0
for score in scores.values():
    total += score
print(f"파이썬 님의 성적은\n"
      f"총합 {total} 점, 평균 {total / len(scores)} 점 입니다.")

# 피타고라스 정리
len_1 = float(input("첫번째 직각변의 길이(cm) : "))
len_2 = float(input("두번째 직각변의 길이(cm) : "))
print(f"빗변의 길이는 {(len_1**2 + len_2**2) ** 0.5} cm입니다.")

# 원의 넓이 구하기
radius = float(input("원의 반지름을 입력하세요(cm) : "))
print(f"원의 둘레는 {radius * pi * 2} cm이고 원의 넓이는 {radius**2*pi} cm입니다.")

# 근의 공식
print("이차방정식 ax^2 + bx + c 해 계산기입니다.")
a = int(input("a 값 : "))
b = int(input("b 값 : "))
c = int(input("c 값 : "))
print(f"이차방정식 {a}x^2 + {b}x + {c} 의 해는\n"
      f"{b * -1} +- {(b**2 - 4*a*c)**0.5}\n"
      f"----------\n"
      f"    {2*a}")

# BMI 계산하기
name = input("이름을 입력하세요 : ")
height = int(input("키(cm)를 입력하세요 : "))
weight = int(input("몸무게(kg)를 입력하세요 : "))
print(f"파이썬님의 키는 {height}cm이고 몸무게는 {weight}kg입니다.\n"
      f"BMI 지수는 {weight / ((height/100)**2)} 입니다.")

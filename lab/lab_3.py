from typing import List
import pandas as pd

def q1() -> None:
    shape = input("select shape >>> 1-rectangle, 2-circle: ")
    if shape == "1":
        width = float(input("input width: "))
        height = float(input("input height: "))
        print(f"rect area = {width * height}")
    elif shape == "2":
        radius = float(input("input radius: "))
        print(f"circle area = {3.14 * radius ** 2}")
        
def capitalize(word: str) -> str:
    return word[0].upper() + word[1:].lower()

def q2(text: str = "seoul busan incheon deagu daejeon kwangju ulsan suwon") -> List[str]:
    if text == "":
        text = "seoul busan incheon deagu daejeon kwangju ulsan suwon"
    cities = list(map(capitalize, text.split()))
    print(f"입력된 도시 이름: {cities}")
    return cities

def q3(text: str) -> List[str]:
    cities = q2(text)
    input_city = capitalize(input("추가 혹은 제거할 도시 이름: "))
    if input_city in cities:
        cities.remove(input_city)
    else:
        cities.append(input_city)
    ret = " - ".join(cities)
    print(f"경유지: {ret}")
    return cities


class Q4:
    def __init__(self) -> None:
        self.name = ['카페아메리카노','돌체라떼','카페모카','화이트초코모카']
        self.code = ['CA', 'DL', 'CM', 'WM']
        self.price = [4500, 5900, 5500, 5900]
        self.bev_count = len(self.code)
        self.cnt = [0] * self.bev_count
        self.total = [0] * self.bev_count
        self.bev_dict = {}
        for i in range(self.bev_count):
            self.bev_dict[self.code[i]] = {'name': self.name[i], 'price': self.price[i], 'count': self.cnt[i], 'total': self.total[i]}
        self.bev_df = pd.DataFrame(self.bev_dict)
    
    def __ordering(self, code: str) -> None:
        self.bev_df[code]['count'] += 1
        self.bev_df[code]['total'] += self.bev_df[code]['price']
    
    def __closing(self) -> None:
        print("="*50)
        print("{:<12} {:<8} {:<8}".format("음료", "판매수량", "판매액"))
        print("="*50)
        total_sales = 0
        for i in range(self.bev_count):
            bev_code = self.code[i]
            bev_name = self.name[i]
            bev_count = self.bev_df[bev_code]['count']
            bev_total = self.bev_df[bev_code]['total']
            total_sales += bev_total
            if bev_count > 0:
                print("{:<12} {:<8} {:<8}".format(bev_name, bev_count, bev_total))
        print("="*50)
        print("판매 총액 : {}".format(total_sales))

    def simulate(self) -> None:
        while True:
            input_code = input("음료 코드 입력: ").upper()
            if input_code == "Q":
                self.__closing()
                return
            elif input_code in self.code:
                self.__ordering(input_code)
                bev_name = self.bev_df[input_code]['name']
                bev_price = self.bev_df[input_code]['price']
                print("주문하신 음료는 {} 이고, 가격은 {} 입니다.".format(bev_name, bev_price))
            else:
                continue

if __name__ == "__main__":
    q1()
    q2(input("문자열 입력: "))
    q3(input("문자열 입력: "))
    q4 = Q4()
    q4.simulate()
    
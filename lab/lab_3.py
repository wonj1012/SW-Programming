"""
SW Programming Lab #3
Name: 최원재
ID: 2020147530
Date: 2023-04-12
"""

from typing import List


def q1() -> None:
    """
    Get the shape and the size of the shape from the user and calculate the area.
    """
    shape = input("select shape >>> 1-rectangle, 2-circle: ")
    if shape == "1":
        width = float(input("input width: "))
        height = float(input("input height: "))
        print(f"rect area = {width * height}")
    elif shape == "2":
        radius = float(input("input radius: "))
        print(f"circle area = {3.14 * radius ** 2}")


def capitalize(word: str) -> str:
    """
    Capitalize the first letter of the word.

    Args:
        word (str): The word to capitalize.

    Returns:
        str: The capitalized word.
    """
    return word[0].upper() + word[1:].lower()


def q2(text: str) -> List[str]:
    """
    Split the text by space and capitalize each word.

    Args:
        text (str): The text to split.

    Returns:
        List[str]: The list of capitalized words.
    """
    if text == "":
        text = "seoul busan incheon deagu daejeon kwangju ulsan suwon"
    cities = list(map(capitalize, text.split()))
    print(f"입력된 도시 이름: {cities}")
    return cities


def q3(text: str) -> List[str]:
    """
    Split the text by space and capitalize each word.

    Args:
        text (str): The text to split.

    Returns:
        List[str]: The list of capitalized words.
    """
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
    """
    A class that manages the sales of beverages.
    """

    def __init__(self) -> None:
        self.beverages = {
            "CA": {"name": "카페아메리카노", "price": 4500, "count": 0, "total": 0},
            "DL": {"name": "돌체라떼", "price": 5900, "count": 0, "total": 0},
            "CM": {"name": "카페모카", "price": 5500, "count": 0, "total": 0},
            "WM": {"name": "화이트초코모카", "price": 5900, "count": 0, "total": 0},
        }

    def __ordering(self, code: str) -> None:
        """
        Order a beverage.

        Args:
            code (str): The code of the beverage to order.
        """
        self.beverages[code]["count"] += 1
        self.beverages[code]["total"] += self.beverages[code]["price"]

    def __closing(self) -> None:
        """
        Print the sales report.
        """
        print("=" * 50)
        print(f"{'음료':<12} {'판매수량':<8} {'판매액':<8}")
        print("=" * 50)
        total_sales = 0
        for beverage in self.beverages.values():
            bev_name = beverage["name"]
            bev_count = beverage["count"]
            bev_total = beverage["total"]
            total_sales += bev_total
            if bev_count > 0:
                print(f"{bev_name:<12} {bev_count:<8} {bev_total:<8}")
        print("=" * 50)
        print(f"판매 총액 : {total_sales}")

    def run(self) -> None:
        """
        Run the program.
        """
        while True:
            input_code = input("음료 코드 입력: ").upper()
            if input_code == "Q":
                self.__closing()
                return
            if input_code in self.beverages:
                self.__ordering(input_code)
                bev_name = self.beverages[input_code]["name"]
                bev_price = self.beverages[input_code]["price"]
                print(f"주문하신 음료는 {bev_name} 이고, 가격은 {bev_price} 입니다.")
            else:
                continue


if __name__ == "__main__":
    q1()
    q2(input("문자열 입력: "))
    q3(input("문자열 입력: "))
    q4 = Q4()
    q4.run()

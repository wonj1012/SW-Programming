"""
2023-1 Final Exam
Name: 최원재
ID: 2020147530
Date: 2023-06-14
"""
from typing import Tuple
import csv
import numpy as np
import requests
from bs4 import BeautifulSoup


class Q1:
    def __init__(self) -> None:
        self.cities_dict = {
            1: {"name": "Wroclaw", "days": 3, "cost": 250000},
            2: {"name": "Bilbao", "days": 4, "cost": 350000},
            3: {"name": "Colmar", "days": 3, "cost": 300000},
            4: {"name": "Hvar island", "days": 3, "cost": 270000},
            5: {"name": "Riga", "days": 4, "cost": 360000},
            6: {"name": "Milano", "days": 3, "cost": 450000},
            7: {"name": "Athens", "days": 2, "cost": 300000},
            8: {"name": "Budapest", "days": 3, "cost": 250000},
            9: {"name": "Lisbon", "days": 4, "cost": 380000},
            10: {"name": "Prague", "days": 5, "cost": 420000},
        }

    def plan_travel(self, budget: int) -> Tuple[int, int, list[str]]:
        """
        gets a budget and returns the total payment, total days, and waypoints.

        Args:
            budget (int): total budget

        Returns:
            Tuple[int, int, list[str]]: total payment, total days, and waypoints
        """
        payment, days, waypoints = 0, 0, []
        while True:
            choice = int(input("Select City :> "))
            if choice == 0:
                break
            if choice not in self.cities_dict:
                continue
            city = self.cities_dict[choice]
            if payment + city["cost"] > budget:
                break
            waypoints.append(city["name"])
            payment += city["cost"]
            days += city["days"]
            print(payment)
            print(city["name"])
        return payment, days, waypoints

    def solve(self) -> None:
        print(
            "-----------------------------------------\n"
            "--------- List of travel cities ---------\n"
            "-----------------------------------------"
        )
        for num, city in self.cities_dict.items():
            print(f"{num} - {city['name']} {city['days']}day : {city['cost']}")
        print("-----------------------------------------")

        budget = int(input("Input total traveling expenses :> "))
        payment, days, waypoints = self.plan_travel(budget)

        print(
            f"-----------------------------------------\n"
            f"Waypoint :  {' '.join(waypoints)}\n"
            f"{days} Days,  Total Payment : {payment} Won\n"
            f"-----------------------------------------"
        )


class Q2:
    def __init__(self) -> None:
        self.students = ["라이언", "어피치", "프로도"]
        self.subjects = ["국어", "영어", "수학"]

    def solve(self) -> None:
        score_array = np.random.randint(0, 101, size=(len(self.students), len(self.subjects)))

        col_sum = score_array.sum(axis=0)
        row_sum = score_array.sum(axis=1)

        col_avg = list(map(lambda x: x / len(self.students), col_sum))
        row_avg = list(map(lambda x: x / len(self.students), row_sum))

        print("\t" + "\t".join(self.students + ["합계", "평균"]))
        for i in range(len(self.subjects)):
            print(
                "\t".join(
                    [self.subjects[i]]
                    + list(map(str, score_array[i]))
                    + [str(row_sum[i]), f"{row_avg[i]:.2f}"]
                )
            )
        print("==============================================")
        print("\t".join(["합계"] + list(map(str, col_sum))))
        print("\t".join(["평균"] + list(map(lambda x: f"{x:.2f}", col_avg))))


class Q3:
    def __init__(self) -> None:
        self.soup = self.get_soup("https://series.naver.com/novel/recommendList.series")
        self.csv_file_path = "data/final_exam/naver_novel_recommendations.csv"

    def get_soup(self, url: str) -> BeautifulSoup:
        """
        gets a url and returns a BeautifulSoup object.

        Args:
            url (str): url

        Returns:
            BeautifulSoup: BeautifulSoup object
        """
        url = "https://series.naver.com/novel/recommendList.series"
        res = requests.get(url, timeout=10)
        res.raise_for_status()

        return BeautifulSoup(res.text, "lxml")

    def solve(self) -> None:
        novels = self.soup.find_all("div", attrs={"class": "lst_thum_wrap"})[0].find_all("li")

        with open(self.csv_file_path, "w", encoding="utf-8-sig", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["제목", "작가", "평점"])
            for novel in novels:
                title = novel.find("h3").find("a")["title"]
                author = novel.find("span", class_="author").get_text()
                rating = novel.find("em", class_="score_num").get_text()

                writer.writerow([title, author, rating])

        with open(self.csv_file_path, "r", encoding="utf-8-sig") as csv_file:
            csv_file.readline()
            for line in csv_file.readlines():
                title, author, rating = line.split(",")
                print(f"제목: {title}")
                print(f"작가: {author}")
                print(f"평점: {rating}")


if __name__ == "__main__":
    print("\n==================== Q1 ====================\n")
    Q1().solve()
    print("\n==================== Q2 ====================\n")
    Q2().solve()
    print("\n==================== Q3 ====================\n")
    Q3().solve()

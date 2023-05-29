"""
SW Programming Lab #7
Name: 최원재
ID: 2020147530
Date: 2023-05-26
"""

import requests
from bs4 import BeautifulSoup
import csv


def get_soup(url: str) -> BeautifulSoup:
    """
    Fetches the page content from the given URL and parses it using BeautifulSoup.

    :param url: The URL of the webpage.
    :return: A BeautifulSoup object representing the parsed webpage.
    """
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'lxml')


class Q1:
    """
    A class to handle operations related to "https://movie.daum.net/ranking/reservation" webpage.
    """

    def __init__(self):
        self.filepath = "data/lab_7/movies.csv"

    def solve(self) -> None:
        """
        Fetches movie data from the webpage, saves the data to a CSV file,
        and prints the movie data.
        """
        soup = get_soup("https://movie.daum.net/ranking/reservation")

        # Writing to the file
        with open(self.filepath, "w", encoding="utf-8-sig", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["순위", "영화명",  "평점", "예매율"])

            for movie in soup.find_all("div", class_="item_poster"):
                rank = movie.find("span", class_="rank_num").get_text()
                title = movie.find(
                    "a", {"data-tiara-layer": "moviename"}).get_text()
                grade = movie.find("span", class_="txt_grade").get_text()
                resrate = movie.find("span", class_="txt_num").get_text()[:-1]

                writer.writerow([rank, title, grade, resrate])

        # Reading from the file
        self.read_file()

    def read_file(self) -> None:
        """
        Reads and prints the movie data from the CSV file.
        """
        with open(self.filepath, "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                print(f"순위: {row[0]}")
                print(f"영화명: {row[1]}")
                print(f"평점: {row[2]}")
                print(f"예매율: {row[3]}")
                print("-"*30)


class Q2:
    """
    A class to handle operations related to "https://www.imdb.com/title/tt0285331/episodes?season=" webpage.
    """

    def __init__(self):
        self.filepath = "data/lab_7/imdb_episodes.csv"

    def solve(self) -> None:
        """
        Fetches episode data for each season from the webpage, saves the data to a CSV file,
        and prints the episode data.
        """
        # Open CSV file to write
        with open(self.filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["시즌", "제목", "리뷰수", "평점", "줄거리"])

            for season in range(1, 9):  # For each season
                url = f"https://www.imdb.com/title/tt0285331/episodes?season={season}"
                soup = get_soup(url)

                # For each episode
                for episode in soup.find_all('div', class_='list_item'):
                    season = episode.find('div', class_='image').find(
                        'div').text.strip().split(',')[0][1:]
                    title = episode.find('a', itemprop='name').text.strip()
                    rating = episode.find(
                        'span', class_='ipl-rating-star__rating').text
                    review_count = episode.find(
                        'span', class_='ipl-rating-star__total-votes').text.strip('()')
                    synopsis = episode.find(
                        'div', class_='item_description').text.strip()

                    writer.writerow(
                        [season, title, review_count, rating, synopsis])

        # Reading from the file
        self.read_file()

    def read_file(self) -> None:
        """
        Reads and prints the episode data from the CSV file.
        """
        with open(self.filepath, "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                print(row[0])
                print(f"제목: {row[1]}")
                print(f"리뷰수: {row[2]}")
                print(f"평점: {row[3]}")
                print(f"줄거리:\n{row[4]}")
                print("-"*30)


if __name__ == "__main__":
    print("\n==================== Q1 ====================")
    Q1().solve()
    print("\n==================== Q2 ====================")
    Q2().solve()

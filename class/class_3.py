import requests
from bs4 import BeautifulSoup
import csv
from typing import List


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'lxml')


def write_csv(data: List[List[str]], column_names: List[str], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(column_names)
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    soup_imdb = get_soup("https://www.imdb.com/chart/top")

    data = []
    for tr in soup_imdb.find("tbody", {"class": "lister-list"}).find_all("tr"):
        rank = tr.find("td", {"class": "titleColumn"}
                       ).text.split()[0].strip(".")
        title = tr.find("td", {"class": "titleColumn"}).find("a").get_text()
        rating = tr.find("td", {"class": "ratingColumn imdbRating"}).find(
            "strong").get_text()
        year = tr.find("td", {"class": "titleColumn"}).find(
            "span", {"class": "secondaryInfo"}).get_text().strip("()")
        data.append([rank, title, rating, year])
    write_csv(data=data, column_names=["rank", "title", "rating", "year"],
              path="data/imdb_top250.csv")

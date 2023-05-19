"""
SW Programming Lab #5
Name: 최원재
ID: 2020147530
Date: 2023-05-19
"""

import numpy as np
from typing import Tuple
import matplotlib.pyplot as plt

DIR = "data/"


def q1(file_path: str = f"{DIR}lab_5-1.txt") -> np.ndarray:
    # generate random array and save to file
    arr = np.random.randint(1, 46, size=(10, 10))
    np.savetxt(file_path, arr, fmt="%d")

    # read file
    with open(file_path, "r") as file:
        lines = file.readlines()
        # print file contents
        for line in lines:
            print(line.strip())

    # convert to numpy array
    arr = np.array([line.strip().split() for line in lines], dtype=int)
    # print numpy array
    print(arr)

    return arr


def q2(file_path: str = f"{DIR}lab_5-2.txt") -> Tuple[np.ndarray, np.ndarray]:
    arr = q1(file_path)
    row_sum = np.sum(arr, axis=1)
    col_sum = np.sum(arr, axis=0)
    len_arr = len(arr)
    for i in range(len_arr):
        for num in arr[i]:
            print(f"{num:4d}", end=" ")
        print(f"| {row_sum[i]:4d} | {row_sum[i] / len_arr:4.1f}")
    print("-" * (len_arr * 5))
    for i in range(len_arr):
        print(f"{col_sum[i]:4d}", end=" ")
    print()
    print("-" * (len_arr * 5))
    for i in range(len_arr):
        print(f"{col_sum[i] / len_arr:4.1f}", end=" ")
    print()

    return row_sum, col_sum


def q3(file_path: str = f"{DIR}lab_5-3.txt") -> None:
    # generate graph of average of sum of rows and columns
    row_sum, col_sum = q2(file_path)
    row_avg = list(map(lambda x: x / len(row_sum), row_sum))
    col_avg = list(map(lambda x: x / len(col_sum), col_sum))

    X = range(1, len(row_avg)+1)
    Y1 = row_avg
    Y2 = col_avg
    plt.plot(X, Y1, label="row average")
    plt.plot(X, Y2, label="column average")
    plt.xlabel("row/column number")
    plt.ylabel("value")
    plt.legend(loc="upper left")
    plt.title("Average of sum of rows and columns")
    plt.show()


if __name__ == "__main__":
    print("\n==================== Q1 ====================")
    q1()
    print("\n==================== Q2 ====================")
    q2()
    print("\n==================== Q3 ====================")
    q3()

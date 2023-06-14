"""
SW Programming Lab #6
Name: 최원재
ID: 2020147530
Date: 2023-05-19
"""

from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt

DIR = "data/lab_6/"


def q1(file_path: str = f"{DIR}q1.txt") -> np.ndarray:
    """
    Generates a 10x10 array of random integers between 1 and 45, saves it to a file,
    prints the file content and the numpy array, and returns the numpy array.

    :param file_path: The path where the file will be saved. Default is "data/lab_6/q1.txt"
    :return: A 10x10 numpy array of the file content.
    """
    # generate random array and save to file
    arr = np.random.randint(1, 46, size=(10, 10))
    np.savetxt(file_path, arr, fmt="%d")

    # read file and convert to numpy array
    arr = np.loadtxt(file_path, dtype=int)

    print(arr)
    return arr


def q2(file_path: str = f"{DIR}q2.txt") -> Tuple[np.ndarray, np.ndarray]:
    """
    Generates a numpy array using q1 function, computes the sum of each row and each column,
    prints the array and the computed sums, and returns the row sums and column sums.

    :param file_path: The path where the file will be saved. Default is "data/lab_6/q2.txt"
    :return: A tuple of two numpy arrays for the row sums and the column sums.
    """
    arr = q1(file_path)
    row_sum = np.sum(arr, axis=1)
    col_sum = np.sum(arr, axis=0)
    len_arr = len(arr)

    for i, row in enumerate(arr):
        print(
            " ".join(f"{num:4d}" for num in row), f"| {row_sum[i]:4d} | {row_sum[i] / len_arr:4.1f}"
        )
    print("-" * (len_arr * 5))
    print(*col_sum)
    print("-" * (len_arr * 5))
    print(*[f"{cs / len_arr:4.1f}" for cs in col_sum])

    return row_sum, col_sum


def q3(file_path: str = f"{DIR}q3.txt") -> None:
    """
    Generates a plot of the average of the sum of rows and columns.

    :param file_path: The path where the file will be saved. Default is "data/lab_6/q3.txt"
    """
    row_sum, col_sum = q2(file_path)
    row_avg = list(map(lambda x: x / len(row_sum), row_sum))
    col_avg = list(map(lambda x: x / len(col_sum), col_sum))

    x_values = range(1, len(row_avg) + 1)
    plt.plot(x_values, row_avg, label="row average")
    plt.plot(x_values, col_avg, label="column average")
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

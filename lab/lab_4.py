"""
SW Programming Lab #4
Name: 최원재
ID: 2020147530
Date: 2023-05-10
"""

from random import randint

DIR = "data/"


def q1(file_name: str = f"{DIR}ex08_01.txt") -> None:
    """
    Get a string from the user and write it to a file called ex08_01.txt.

    Args:
        file_name (str): The name of the file to write.
    """
    input_str = input("data 입력: ")

    word_list = input_str.split()

    with open(file_name, "w") as file:
        for word in word_list:
            file.write(word + "\n")

    with open(file_name, "r") as file:
        file_contents = file.read()
        print(file_contents)


def q2(file_name: str = f"{DIR}ex08_02.txt") -> None:
    """
    Generate 100 random numbers at [1, 45]
    and write them to a file called ex08_02.txt.

    Args:
        file_name (str): The name of the file to write.
    """
    with open(file_name, "w") as file:
        for _ in range(10):
            for _ in range(10):
                file.write(str(randint(1, 45)) + " ")
            file.write("\n")

    with open(file_name, "r") as file:
        file_contents = file.read()
        print(file_contents)


def q3(file_name: str = f"{DIR}ex08_03.txt") -> None:
    """
    Generate 100 random numbers at [1, 45]
    and write them to a file called ex08_02.txt.
    And count the frequency of each number.

    Args:
        file_name (str): The name of the file to write.
    """
    frequency = [0] * 45
    print(f"빈도수 카운트 전\n"
          f"{frequency}\n"
          f"파일 내용")
    with open(file_name, "w") as file:
        for _ in range(10):
            for _ in range(10):
                num = randint(1, 45)
                frequency[num - 1] += 1
                file.write(str(num) + " ")
            file.write("\n")

    with open(file_name, "r") as file:
        file_contents = file.read()
        print(file_contents)
    print(f"빈도수 카운트 후\n"
          f"{frequency}\n")


def q4(file_name: str = f"{DIR}ex08_04.txt") -> None:
    """
    Read each line of the file and save the words at list.

    Args:
        file_name (str): The name of the file to read.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            word_list = line.split()
            print(word_list)
            for word in word_list:
                print(word)


if __name__ == "__main__":
    q1()
    q2()
    q3()
    q4()

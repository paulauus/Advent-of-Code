"""Day 11: Plutonian Pebbles"""

from functools import cache

def read_input(filename: str) -> list[int]:
    """Reads the .txt input into a list of integers."""
    return list(map(int, open(filename, 'r', encoding="UTF-8").read().strip().split()))

@cache
def corresponding_value(value: int):
    """Returns the new value of a number on a stone."""
    length = len(str(value))
    if value == 0:
        return 1

    if length % 2 == 0:
        return [int(str(value)[:length//2]), int(str(value)[length//2:])]

    return value*2024


@cache
def split_amount(number: int, iterations: int) -> int:
    """Calls corresponding_value for each stone and tracks how many splits occur."""
    overall = number
    splits = 0
    for i in range(iterations):
        value = corresponding_value(overall)
        if isinstance(value, int):
            overall = value
        if isinstance(value, list):
            splits += 1
            overall = value[0]
            splits += split_amount(value[1], iterations-i-1)
    return splits


if __name__ == "__main__":
    data = read_input("day_11_data.txt")

    # Part 1
    max_iterations = 25
    answer_1 = (len(data)+sum(split_amount(i, max_iterations)
          for i in data))
    print(f"Part 1: {answer_1}")

    # Part 2
    max_iterations = 75
    answer_2 = (len(data)+sum(split_amount(i, max_iterations)
                              for i in data))
    print(f"Part 2: {answer_2}")

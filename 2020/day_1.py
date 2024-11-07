"""Day 1: Report Repair"""

import math

def read_input(filename: str) -> list[str]:
    """Reads the input file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def find_two_entries(numbers: list[str]) -> tuple:
    """Finds the two numbers that sum to 2020."""
    for a in numbers:
        for b in numbers:
            if int(a) + int(b) == 2020:
                return (int(a), int(b))

    return None


def multiply_numbers(num_pair: tuple) -> int:
    """Multiplies two numbers."""
    result = math.prod(list(num_pair))
    
    return result


def find_three_entries(numbers: list[str]) -> tuple:
    """Finds the three numbers that sum to 2020."""
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if int(a) + int(b) + int(c) == 2020:
                    return (int(a), int(b), int(c))

    return None


if __name__ == "__main__":
    data = read_input("day_1_data.txt")
    # Part 1
    answer_1 = multiply_numbers(find_two_entries(data))
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = multiply_numbers(find_three_entries(data))
    print(f"Part 2: {answer_2}")
    
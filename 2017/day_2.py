"""Day 2: Corruption Checksum"""

import math

def read_input(filename: str) -> list[str]:
    """Reads a text file into a str."""
    with open(filename, "r", encoding="UTF-8") as f:
        data = f.readlines()

    # Split strings and create a list of lists
    new_list = []
    for line in data:
        new_list.append(line.split())

    return new_list


def calculate_checksum(data: list[list]) -> int:
    """Calculates the checksum in the puzzle input."""
    checksum = 0
    for line in data:
        min_number = math.inf
        max_number = -math.inf
        # Find max and min numbers
        for num in line:
            num = int(num)  # Change str to int
            min_number = min(min_number, num)
            max_number = max(max_number, num)
        # Find difference between max and min
        diff_number = max_number - min_number
        # Add difference to total
        checksum += diff_number

    return checksum


def find_even_division_result(line: list) -> int:
    """Returns the result of two numbers where one evenly divides the other."""
    result = None  # Initialize result
    for a in line:
        for b in line:
            if a == b:
                continue
            if int(a) % int(b) == 0:
                result = int(a) / int(b)

    return int(result)


def calculate_even_division_sum(data: list[list]) -> int:
    """Calculates the sum of each row's even division result."""
    total_sum = 0
    for line in data:
        line_result = find_even_division_result(line)
        total_sum += line_result

    return total_sum


if __name__ == "__main__":
    # Part 1
    num_list = read_input("day_2_data.txt")
    answer_1 = calculate_checksum(num_list)
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = calculate_even_division_sum(num_list)
    print(f"Part 2: {answer_2}")

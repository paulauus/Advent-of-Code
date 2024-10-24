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
            if num < min_number:
                min_number = num
            if num > max_number:
                max_number = num
        # Find difference between max and min
        diff_number = max_number - min_number
        # Add difference to total
        checksum += diff_number

    return checksum

if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    answer_1 = calculate_checksum(data)
    print(f"Part 1: {answer_1}")
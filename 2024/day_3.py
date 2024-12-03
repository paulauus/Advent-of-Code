"""Day 3: Mull It Over"""

import re

PATTERN = r"mul\(\d{1,3},\s?\d{1,3}\)"
PATTERN_2 = r"(mul\(\d{1,3},\s?\d{1,3}\)|do\(\)|don't\(\))"

def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:

        return f.read()


def extract_mul(corrupted_code: str) -> list[str]:
    """Returns a list of valid calculations."""
    matches = re.findall(PATTERN, corrupted_code)

    return matches


def find_sum_of_multiplications(mul_codes: list[str]) -> int:
    """Returns the sum of the clean code."""
    answer = 0

    for i in mul_codes:
        numbers = list(map(int, i[4:-1].split(',')))
        product = numbers[0] * numbers[1]
        answer += product

    return answer


def extract_mul_do_dont(corrupted_code: str) -> list[str]:
    """Returns a list of valid calculations and instructions."""
    matches = re.findall(PATTERN_2, corrupted_code)

    return matches


def find_sum_with_instructions(mul_codes: list[str]) -> int:
    """Returns the sum of the clean code with instructions."""
    answer = 0
    do = True

    for i in mul_codes:

        if i == "do()":
            do = True

        if i == "don't()":
            do = False

        if i.startswith("mul"):
            if do is True:
                numbers = list(map(int, i[4:-1].split(',')))
                product = numbers[0] * numbers[1]
                answer += product

    return answer


if __name__ == "__main__":
    data = read_lines("day_3_data.txt")
    # Part 1
    answer_1 = find_sum_of_multiplications(extract_mul(data))
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = find_sum_with_instructions(extract_mul_do_dont(data))
    print(f"Part 2: {answer_2}")

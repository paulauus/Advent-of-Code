"""Day 4: The Ideal Stocking Stuffer"""

import hashlib


def find_lowest_number(input: str, start: str) -> int:
    """Finds the lowest number that produces a hash."""
    answer = 0
    while True:
        new_code = input + str(answer)
        md5hash = hashlib.md5(new_code.encode())
        if md5hash.hexdigest().startswith(start):
            break
        answer += 1
    return answer

if __name__ == "__main__":

    puzzle_input_1 = "iwrupvqb"
    starts_with_1 = "00000"
    answer_1 = find_lowest_number(puzzle_input_1, starts_with_1)
    print(f"Part 1: {answer_1}")

    starts_with_2 = "000000"
    answer_2 = find_lowest_number(puzzle_input_1, starts_with_2)
    print(f"Part 2: {answer_2}")

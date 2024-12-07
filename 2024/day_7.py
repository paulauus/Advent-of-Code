"""Day 7: Bridge Repair"""

from itertools import product


def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f.readlines()]
    

def get_integers(raw_input: list[str]) -> list[list[int]]:
    """Extracts numbers from the raw input as a list of lists."""
    final_list = []

    for line in raw_input:
        int_list = []
        list_1 = line.split(":")
        int_list.append(int(list_1[0]))
        int_list += [int(num) for num in list_1[1].strip().split()]

        final_list.append(int_list)

    return final_list

def find_total_calibration_result(clean_data: list[list[int]]) -> int:
    """Finds the sum of all valid test values."""
    total_calibration_result = 0

    for test in clean_data:
        combinations = [''.join(p) for p in product("+*", repeat=(len(test)-2))]
        for c in combinations:
            total = test[1]
            for i, op in enumerate(c):
                if op == "+":
                    total = total + test[i+2]
                if op == "*":
                    total = total * test[i+2]
            if total == test[0]:
                total_calibration_result += test[0]
                break

    return total_calibration_result


def find_total_using_third_operator(clean_data: list[list[int]]) -> int:
    """Finds the sum of all valid test values using a third operator."""
    total_calibration_result = 0

    for test in clean_data:
        combinations = [''.join(p)
                        for p in product("+*/", repeat=(len(test)-2))]
        for c in combinations:
            total = test[1]
            for i, op in enumerate(c):
                if op == "+":
                    total = total + test[i+2]
                if op == "*":
                    total = total * test[i+2]
                if op == "/":
                    total = int(str(total) + str(test[i+2]))
            if total == test[0]:
                total_calibration_result += test[0]
                break

    return total_calibration_result


if __name__ == "__main__":
    data = read_lines("day_7_data.txt")
    cleaned_data = get_integers(data)
    # Part 1
    answer_1 = find_total_calibration_result(cleaned_data)
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = find_total_using_third_operator(cleaned_data)
    print(f"Part 2; {answer_2}")

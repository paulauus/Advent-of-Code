"""Day 2: Red-Nosed Reports"""


def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:

        return f.readlines()


def transform_to_ints(raw_data: list[str]) -> list[list[int]]:
    """Transforms the raw input data into a list of lists of integers."""
    new_list = []

    for line in raw_data:
        new_line = [int(num) for num in line.strip().split()]
        new_list.append(new_line)

    return new_list


def find_safe_report(report: list[int]):
    """Determines if a report is safe."""
    is_increasing = all(0 < report[i+1] - report[i]
                        <= 3 for i in range(len(report) - 1))
    is_decreasing = all(0 < report[i] - report[i+1]
                        <= 3 for i in range(len(report) - 1))

    if is_increasing or is_decreasing:

        return True

    return None


def find_safe_reports(reports: list[list[int]]) -> int:
    """Finds the number of safe reports in the data from the engineers."""
    safe_reports = 0

    for line in reports:
        if find_safe_report(line):
            safe_reports += 1

    return safe_reports


def find_safe_problem_dampener_reports(reports: list[list[int]]) -> int:
    """Finds the number of safe reports with the Problem Dampener."""
    safe_reports = 0

    for line in reports:
        if find_safe_report(line):
            safe_reports += 1
        else:
            for i in range(len(line)):
                # Remove element at index i
                modified_line = line[:i] + line[i + 1:]
                if find_safe_report(modified_line):
                    safe_reports += 1
                    break  # Stop after finding the first valid modification

    return safe_reports


if __name__ == "__main__":
    data = transform_to_ints(read_lines("day_2_data.txt"))
    # Part 1
    answer_1 = find_safe_reports(data)
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = find_safe_problem_dampener_reports(data)
    print(f"Part 2: {answer_2}")

"""Day 1: Chronal Calibration"""


def read_input(filename: str) -> str:
    """Reads a text file into a str."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def calculate_frequency_change(data: list) -> int:
    """Calculates the resulting frequency after all changes."""
    frequency = 0
    for change in data:
        a, b = change[0], int(change[1:])
        if a == "+":
            frequency += b
        else:
            frequency -= b

    return frequency


def find_repeating_frequency(data: list) -> int:
    """Finds the first frequency reached twice."""
    frequency = 0
    frequency_list = []
    while True:
        for change in data:
            a, b = change[0], int(change[1:])
            if a == "+":
                frequency += b
            else:
                frequency -= b
            if frequency in frequency_list:
                return frequency
            frequency_list.append(frequency)


if __name__ == "__main__":
    readings = read_input("day_1_data.txt")
    # Part 1
    answer_1 = calculate_frequency_change(readings)
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = find_repeating_frequency(readings)
    print(f"Part 2: {answer_2}")

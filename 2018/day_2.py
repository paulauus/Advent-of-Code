"""Day 2: Inventory Management System"""


def read_input(filename: str) -> list[str]:
    """Reads a text file into a list."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def calculate_checksum(boxes: list[str]) -> int:
    """Calculates the checksum of the list of box IDs."""
    two_counts = 0
    three_counts = 0
    for box in boxes:
        box_dict = {}
        for letter in box:
            if letter not in box_dict:
                box_dict[letter] = 1
            else:
                box_dict[letter] += 1
        if 2 in box_dict.values():
            two_counts += 1
        if 3 in box_dict.values():
            three_counts += 1

    return two_counts * three_counts


if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    answer_1 = calculate_checksum(data)
    print(f"Part 1: {answer_1}")
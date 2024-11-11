"""Day 2: Password Philosophy"""


def read_input(filename: str) -> list[str]:
    """Reads a text file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def clean_input(lines: list[str]) -> list[list[str]]:
    """Cleans the data from the text file into usable format."""
    cleaned_data = []

    for line in lines:
        new_line = []
        items = line.split()  # Split the line into separate items
        new_line.append(items[0].split("-"))  # Split the first item by '-'
        new_line.append(items[1][:-1])
        new_line.append(items[2])

        cleaned_data.append(new_line)

    return cleaned_data


def count_valid_passwords(passwords: list) -> int:
    """Counts the number of valid passwords in the input data."""
    valid_password_count = 0

    for limits, letter, password in passwords:
        # Unpack min and max directly
        min_count, max_count = limits
        letter = letter[0]  # Remove the colon

        # Check if the letter count is within the allowed range
        if int(min_count) <= password.count(letter) <= int(max_count):
            valid_password_count += 1

    return valid_password_count


def count_new_valid_passwords(passwords: list) -> int:
    """Counts the number of valid passwords with new rules."""
    valid_password_count = 0

    for limits, letter, password in passwords:
        pos1, pos2 = limits
        letter = letter[0]

        # Check if exactly one of the positions contains the letter
        first_position_matches = password[int(pos1) - 1] == letter
        second_position_matches = password[int(pos2) - 1] == letter

        if first_position_matches != second_position_matches:  # XOR logic
            valid_password_count += 1

    return valid_password_count

if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    # Part 1
    clean_data = clean_input(data)
    answer_1 = count_valid_passwords(clean_data)
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = count_new_valid_passwords(clean_data)
    print(f"Part 2: {answer_2}")

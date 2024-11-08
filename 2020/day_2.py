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

    for password in passwords:
        if password[1] in password[2]:
            letter_count = {}
            for letter in password[2]:
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
            if int(password[0][0]) <= letter_count[password[1]] <= int(password[0][1]):
                valid_password_count += 1

    return valid_password_count


if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    # Part 1
    clean_data = clean_input(data)
    answer_1 = count_valid_passwords(clean_data)
    print(f"Part 1: {answer_1}")

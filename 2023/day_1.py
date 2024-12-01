"""Day 1: Trebuchet?!"""

DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def read_input(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def find_numbers(calibration: list[str]) -> list[int]:
    """Decodes the calibration document and creates a list of numbers."""
    values = []

    for line in calibration:
        numbers = []

        # Process each line and extract digit numbers
        for i in line:
            if i.isdigit():
                numbers.append(i)

        if len(numbers) == 1:
            num = numbers[0] + numbers[0]  # Double the digit if only one found
            values.append(int(num))

        if len(numbers) > 1:
            # Form the number by first and last digits
            num = numbers[0] + numbers[-1]
            values.append(int(num))

    return values


def replace_words_with_numbers(calibration: list[str]) -> list[str]:
    """Replaces spelled-out numbers with corresponding digits in each line."""
    new_list = []

    for line in calibration:
        digits = []
        i = 0
        while i < len(line):
            if line[i].isdigit():
                digits.append(line[i])  # Collect digits directly
                i += 1
            else:
                # Check for possible word matches
                for word, digit in DIGITS.items():
                    if line[i:i+len(word)] == word:  # Word match found
                        digits.append(digit)  # Replace the word with its digit
                        i += len(word)  # Skip the length of the matched word
                        break
                else:
                    i += 1  # Move to next character if no match

        new_list.append("".join(digits))  # Join digits into a final string

    return new_list


def add_numbers(numbers_list: list[int]) -> int:
    """Adds together all numbers in a list."""
    return sum(numbers_list)


if __name__ == "__main__":
    data = read_input("day_1_data.txt")
    # Part 1
    answer_1 = add_numbers(find_numbers(data))
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = add_numbers(find_numbers(replace_words_with_numbers(data)))
    print(f"Part 2: {answer_2}")

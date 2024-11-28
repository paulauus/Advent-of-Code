"""Day 1: Trebuchet?!"""

def read_input(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()
    

def find_numbers(calibration: list[str]) -> list[int]:
    """Decodes the calibration document and creates a list of numbers."""
    values = []

    for line in calibration:

        numbers = []

        for i in line:
            if i.isdigit():
                numbers.append(i)

        if len(numbers) == 1:
            num = numbers[0] + numbers[0]
            values.append(int(num))

        if len(numbers) > 1:
            num = numbers[0] + numbers[-1]
            values.append(int(num))

    return values


if __name__ == "__main__":
    data = read_input("day_1_data.txt")
    

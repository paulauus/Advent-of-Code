"""Day 1: Calorie Counting"""


def read_input(filename: str) -> list[str]:
    """Creates a list of calorie values from a .txt file."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def find_highest_calories(calories: list[str]) -> int:
    """Returns the highest calorie total from the list."""
    calorie_totals = []
    elf_total = 0

    for item in calories:
        if item == '\n':
            calorie_totals.append(elf_total)
            elf_total = 0
        else:
            elf_total += int(item)

    return max(calorie_totals)

if __name__ == "__main__":
    data = read_input("day_1_data.txt")
    # Part 1
    answer_1 = find_highest_calories(data)
    print(f"Part 1: {answer_1}")

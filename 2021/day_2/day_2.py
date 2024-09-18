"""Day 2: Dive!"""


def read_input(filename: str) -> list[str]:
    """Outputs a list of strings."""
    with open(filename, "r") as f:
        return f.read().splitlines()
    
def give_instructions(file: list[str]) -> int:
    """Gives intructions to the submarine."""
    horizontal = 0
    vertical = 0

    for i in file:
        direction, value = i.split()
        match direction:
            case "forward":
                horizontal += int(value)
            case "down":
                vertical += int(value)
            case "up":
                vertical -= int(value)

    return horizontal * vertical


def give_complicated_instructions(file: list[str]) -> int:
    """Gives more complicated intructions to the submarine."""
    horizontal = 0
    vertical = 0
    aim = 0

    for i in file:
        direction, value = i.split()
        match direction:
            case "forward":
                horizontal += int(value)
                vertical += int(value) * aim
            case "down":
                aim += int(value)
            case "up":
                aim -= int(value)

    return horizontal * vertical



    
if __name__ == "__main__":
    
    data = read_input("day_2_data.txt")

    answer_1 = give_instructions(data)

    print(f"Part 1: {answer_1}")

    answer_2 = give_complicated_instructions(data)

    print(f"Part 2: {answer_2}")

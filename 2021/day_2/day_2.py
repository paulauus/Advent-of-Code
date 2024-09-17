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
        # if split_string[0] == "forward":
        #     horizontal += int(split_string[1])
        # if split_string[0] == "up":
        #     vertical -= int(split_string[1])
        # if split_string[0] == "down":
        #     vertical += int(split_string[1])
        match split_string[0]:
            case "forward":
                horizontal += int(split_string[1])
            case "down":
                vertical += int(split_string[1])
            case "up":
                vertical -= int(split_string[1])

    return horizontal * vertical
    
if __name__ == "__main__":
    
    data = read_input("day_2_data.txt")

    answer_1 = give_instructions(data)

    print(f"Part 1: {answer_1}")
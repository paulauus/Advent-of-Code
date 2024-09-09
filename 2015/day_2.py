"""Day 2: I Was Told There Would Be No Math"""


def read_input(filename: str) -> list[str]:
    """Reads the data from a .txt file used in the main function."""
    with open(filename, "r") as f:
        return f.readlines()

def convert_to_str_list(data:str) -> list[str]:
    """Converts a string into a list of strings."""
    new_list = data.split("x")
    return new_list

def calculate_paper_amount(data: list[str]) -> int:
    """Calculates the amount of wrapping paper needed for one present."""
    side_a = int(data[0]) * int(data[1])
    side_b = int(data[1]) * int(data[2])
    side_c = int(data[2]) * int(data[0])
    smallest_side = min(side_a, side_b, side_c)
    answer = smallest_side + (2 * side_a) + (2 * side_b) + (2 * side_c)
    return answer

def get_total_paper(data: list[str]) -> int:
    """Calculates the total amout of paper needed."""
    answer = 0
    for i in data:
        strings_list = convert_to_str_list(i)
        paper_needed = calculate_paper_amount(strings_list)
        answer += paper_needed
    return answer

# Part 2 functions

def calculate_volume(dimensions:list[str]) -> int:
    """Calculates the volume of a present."""
    return int(dimensions[0]) * int(dimensions[1]) * int(dimensions[2])


def calculate_around_present(dimensions: list[str]) -> int:
    """Calculates the shortest distance around a present. """
    dimensions.sort()
    return (2 * int(dimensions[0]) + 2 * int(dimensions[1]))

if __name__ == "__main__":
    file = "day_2_data.txt"
    data = read_input(file)
    # print(convert_to_str_list("29x13x26"))
    amount = get_total_paper(data)
    print(f"The elves need {amount} square feet of wrapping paper.")
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
    """Calculates the shortest distance around a present."""
    sorted_dimensions = sorted(
        dimensions, key=int)  # Sort dimensions by integer size
    return 2 * int(sorted_dimensions[0]) + 2 * int(sorted_dimensions[1])


def get_total_ribbon(data: list[str]) -> int:
    """Calculates the total amount of ribbon needed."""
    total_ribbon = 0

    for i in data:
        strings_list = convert_to_str_list(i)
        total_ribbon += calculate_volume(strings_list)
        total_ribbon += calculate_around_present(strings_list)
    
    return total_ribbon

if __name__ == "__main__":
    file = "day_2_data.txt"
    data = read_input(file)

    amount = get_total_paper(data)
    print(f"Part 1: The elves need {amount} square feet of wrapping paper.")

    ribbon = get_total_ribbon(data)
    print(f"Part 2: The elves need {ribbon} feet of ribbon.")
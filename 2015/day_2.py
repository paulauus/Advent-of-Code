"""Day 2: I Was Told There Would Be No Math"""


def read_input(filename: str) -> list[str]:
    """Reads the data from a .txt file used in the main function."""
    with open(filename, "r") as f:
        return f.readlines()

def convert_to_str_list(data:str) -> list[str]:
    """Converts a string into a list of strings."""
    new_list = data.split("x")
    print(new_list)
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

if __name__ == "__main__":
    print(convert_to_int_list("29x13x26"))

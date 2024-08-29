"""Day 2: I Was Told There Would Be No Math"""


def read_input(filename: str) -> list[str]:
    """Reads the data from a .txt file used in the main function."""
    with open(filename, "r") as f:
        return f.readlines()

def convert_to_int_list(data:list[str]) -> list[list[str]]:
    """Converts a list of strings into a list of lists of strings."""
    answer = []
    for i in data:
        new_list = i.split("x")
        print(new_list)
        answer.append(new_list)
    return answer

def calculate_paper_amount(data: list[str]) -> int:
    """Calculates the amount of wrapping paper needed for one present."""
    side_a = int(data[0]) * int(data[1])
    side_b = int(data[1]) * int(data[2])
    side_c = int(data[2]) * int(data[0])
    smallest_side = min(side_a, side_b, side_c)
    answer = smallest_side + (2 * side_a) + (2 * side_b) + (2 * side_c)
    return answer

if __name__ == "__main__":
    print(convert_to_int_list(["29x13x26", "11x11x14"]))

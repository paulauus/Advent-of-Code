"""Day 1: Not Quite Lisp"""


def read_input(filename: str) -> list[str]:
    """Reads the data from a .txt file used in the main function."""
    with open(filename, "r") as f:
        return f.read()
    
def which_floor_to_go(file:str) -> int:
    """Reads a string on paretheses and tells Santa which floor to go."""
    counter = 0
    instructions = read_input(file)
    for i in instructions:
        if i == "(":
            counter += 1
        else:
            counter -= 1
    return counter

def first_time_basement(file:str) -> int:
    """Returns the position of the first character that tells
    Santa to go to the basement."""
    counter = 0
    instructions = read_input(file)
    for i, char in enumerate(instructions):
        if char == "(":
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            return (i + 1)

if __name__ == "__main__":

    file_name = "day_1_data.txt"

    answer = which_floor_to_go(file_name)

    print(f"Part 1: Santa should go to floor {answer}.")

    answer_2 = first_time_basement(file_name)

    print(f"Part 2: Santa first enters the basement at position {answer_2}.")
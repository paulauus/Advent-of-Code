"""Day 3: Perfectly Spherical Houses in a Vacuum"""


def read_input(filename: str) -> str:
    """Reads the data from a .txt file used in the main function."""
    with open(filename, "r") as f:
        return f.read()


def distributing_gifts(data: str) -> list[tuple]:
    """Returns a list of house coordinates."""
    houses = [(0, 0)]  # Starting point is added
    starting_point = [0, 0]  # This tracks Santa's current location

    for direction in data:
        if direction == "^":
            starting_point[1] += 1
        elif direction == "v":
            starting_point[1] -= 1
        elif direction == "<":
            starting_point[0] -= 1
        elif direction == ">":
            starting_point[0] += 1

        # Append a copy of the current coordinates as a tuple
        houses.append(tuple(starting_point))

    return houses


if __name__ == "__main__":
    santa_data = read_input("day_3_data.txt")
    houses_list = distributing_gifts(santa_data)

    answer = len(set(houses_list))

    print(
        f"Number of unique houses that received at least one present: {answer}")

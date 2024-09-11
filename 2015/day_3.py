"""Day 3: Perfectly Spherical Houses in a Vacuum"""

# Part 1

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


# Part 2

def distributing_with_robot(data:str) -> tuple:
    """Creates a list for Santa and a list for the robot."""
    santa_houses = [(0, 0)]
    robot_houses = [(0, 0)]
    santa_start = [0, 0]
    robot_start = [0, 0]

    for i, direction in enumerate(data):
        if i % 2 == 0:
            if direction == "^":
                santa_start[1] += 1
            elif direction == "v":
                santa_start[1] -= 1
            elif direction == "<":
                santa_start[0] -= 1
            elif direction == ">":
                santa_start[0] += 1
            santa_houses.append(tuple(santa_start))
        else:
            if direction == "^":
                robot_start[1] += 1
            elif direction == "v":
                robot_start[1] -= 1
            elif direction == "<":
                robot_start[0] -= 1
            elif direction == ">":
                robot_start[0] += 1
            robot_houses.append(tuple(robot_start))
    
    return santa_houses, robot_houses


if __name__ == "__main__":
    santa_data = read_input("day_3_data.txt")
    houses_list = distributing_gifts(santa_data)

    answer = len(set(houses_list))

    print(
        f"Part 1: Number of unique houses that received at least one present: {answer}")
    
    santa_houses, robot_houses = distributing_with_robot(santa_data)

    total_houses = santa_houses + robot_houses

    answer_2 = len(set(total_houses))

    print(f"Part 2: Number of unique houses that received at least one present: {answer_2}")

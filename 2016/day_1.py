"""Day 1: No Time for a Taxicab"""


def read_input(filename: str) -> list[str]:
    """Reads the data from a .txt file used in the main function."""
    with open(filename, "r") as f:
        return f.read().split(", ")
    

def calculate_distance(instructions):
    """Calculates the distance to the destination."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Start at (0, 0) facing North (direction index 0)
    current_direction = 0
    x, y = 0, 0

    # Loop through each instruction
    for instruction in instructions:
        turn = instruction[0]
        steps = int(instruction[1:])

        if turn == 'R':
            # Turn right (clockwise)
            current_direction = (current_direction + 1) % 4
        elif turn == 'L':
            # Turn left (counterclockwise)
            current_direction = (current_direction - 1) % 4

        # Move in the current direction
        dx, dy = directions[current_direction]
        x += dx * steps
        y += dy * steps

    return abs(x) + abs(y)

    

if __name__ == "__main__":

    file_name = "day_1_data.txt"

    data = read_input(file_name)

    answer_1 = calculate_distance(data)

    print(f"Part 1: {answer_1}")
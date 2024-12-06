"""Day 6: Guard Gallivant"""

DIRECTIONS = ["up", "right", "down", "left"]
MOVES = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0)
}

def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f.readlines()]


def get_starting_position(mapped_area: list[str]) -> tuple:
    """Returns the starting position coordinates."""
    for i, row in enumerate(mapped_area):
        for j, spot in enumerate(row):
            if spot == "^":
                x = j
                y = i

                return x, y

    return None


def find_distinct_positions(mapped_area: list[str]) -> int:
    """Returns the number of distinct positions visited by the guard."""
    distinct_positions = []

    x, y = get_starting_position(mapped_area)
    distinct_positions.append((x, y))

    direction = 0

    while True:
        next_x = x + MOVES[DIRECTIONS[direction]][0]
        next_y = y + MOVES[DIRECTIONS[direction]][1]

        if next_x not in range(len(mapped_area[0])) or next_y not in range(len(mapped_area)):
            break

        if mapped_area[next_y][next_x] == "#":
            direction = (direction + 1) % len(DIRECTIONS)

        else:
            x, y = next_x, next_y
            if (x, y) not in distinct_positions:
                distinct_positions.append((x, y))

    return len(distinct_positions)


def causes_loop(mapped_area: list[str], start_x: int, start_y: int) -> bool:
    """Simulates guard's movement and checks for a loop."""
    visited_states = set()
    x, y = start_x, start_y
    direction = 0

    while True:
        state = (x, y, direction)
        if state in visited_states:
            return True  # Loop detected
        visited_states.add(state)

        next_x = x + MOVES[DIRECTIONS[direction]][0]
        next_y = y + MOVES[DIRECTIONS[direction]][1]

        # Check if guard moves out of bounds
        if next_x not in range(len(mapped_area[0])) or next_y not in range(len(mapped_area)):
            return False  # Guard exits the map

        # Check if guard encounters an obstacle
        if mapped_area[next_y][next_x] == "#":
            direction = (direction + 1) % len(DIRECTIONS)
        else:
            x, y = next_x, next_y


def find_possible_obstructions(mapped_area: list[str]) -> int:
    """Counts positions where adding an obstruction causes a loop."""
    start_x, start_y = get_starting_position(mapped_area)
    valid_positions = 0

    for y in range(len(mapped_area)):
        for x in range(len(mapped_area[0])):
            if (x, y) == (start_x, start_y) or mapped_area[y][x] != ".":
                continue  # Skip starting position and non-empty positions

            # Add an obstruction at (x, y) and simulate movement
            modified_area = [list(row) for row in mapped_area]
            modified_area[y][x] = "#"  # Add obstruction
            modified_area = ["".join(row) for row in modified_area]

            if causes_loop(modified_area, start_x, start_y):
                valid_positions += 1

    return valid_positions


if __name__ == "__main__":
    data = read_lines("day_6_data.txt")
    # Part 1
    answer_1 = find_distinct_positions(data)
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = find_possible_obstructions(data)
    print(f"Part 2: {answer_2}")

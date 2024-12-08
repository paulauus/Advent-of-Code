"""Day 8: Resonant Collinearity"""

def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f.readlines()]


def get_antenna_coordinates(grid: list[str]) -> list[list[int|str]]:
    """Returns all antennas with coordinates."""
    coordinates = []

    for y, line in enumerate(grid):
        for x, item in enumerate(line):
            if item != ".":
                coordinates.append([item, int(x), int(y)])

    return coordinates


def find_unique_antinode_locations(coordinates: list[list[int | str]], grid: list[str]):
    """Returns the number of unique locations that contain an antinode."""
    antinodes = []

    for i, antenna in enumerate(coordinates):

        for match in coordinates[i+1:]:

            if match[0] == antenna[0]:
                x_diff = match[1] - antenna[1]
                y_diff = match[2] - antenna[2]

                antinode_x1, antinode_y1 = antenna[1] - x_diff, antenna[2] - y_diff
                if 0 <= antinode_x1 < len(grid[0]) and 0 <= antinode_y1 < len(grid) and (
                    antinode_x1, antinode_y1) not in antinodes:
                    antinodes.append((antinode_x1, antinode_y1))

                antinode_x2, antinode_y2 = match[1] + x_diff, match[2] + y_diff
                if 0 <= antinode_x2 < len(grid[0]) and 0 <= antinode_y2 < len(grid) and (
                    antinode_x2, antinode_y2) not in antinodes:
                    antinodes.append((antinode_x2, antinode_y2))

    return len(antinodes)


def find_updated_locations(coordinates: list[list[int | str]], grid: list[str]):
    """Returns the number of antinodes using the updated model."""
    antinodes = set()

    for i, antenna in enumerate(coordinates):
        # Add the antenna itself if there are any matches, skip itself
        if any(match[0] == antenna[0] for match in coordinates if match != antenna):
            antinodes.add((antenna[1], antenna[2]))

        for match in coordinates[i+1:]:
            if match[0] == antenna[0]:  # Same char
                x_diff = match[1] - antenna[1]
                y_diff = match[2] - antenna[2]

                # Line towards one direction (from `antenna` backwards)
                x, y = antenna[1] - x_diff, antenna[2] - y_diff
                while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                    antinodes.add((x, y))
                    x -= x_diff
                    y -= y_diff

                # Line towards the other direction (from `match` forward)
                x, y = match[1] + x_diff, match[2] + y_diff
                while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                    antinodes.add((x, y))
                    x += x_diff
                    y += y_diff

    return len(antinodes)

if __name__ == "__main__":
    data = read_lines("day_8_data.txt")
    antenna_coordinates = get_antenna_coordinates(data)

    # Part 1
    answer_1 = find_unique_antinode_locations(antenna_coordinates, data)
    print(f"Part 1: {answer_1}")
    
    # Part 2
    answer_2 = find_updated_locations(antenna_coordinates, data)
    print(f"Part2: {answer_2}")

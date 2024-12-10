"""Day 10: Hoof It"""

DIRECTIONS = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0)
}


def read_input(filename: str) -> list[list[int]]:
    """Reads the input into a list of lists of integers."""
    with open(filename, "r", encoding="UTF-8") as f:

        return [[int(num) for num in line.strip()] for line in f.readlines()]


def bfs_count_paths(start_x: int, start_y: int, top_map: list[list[int]]) -> int:
    """Returns the number of valid paths to height 9 starting from a trailhead."""
    queue = [(start_x, start_y, 0)]  # (x, y, current height)
    visited = set()
    trail = []
    path_count = 0

    while queue:
        x, y, height = queue.pop(0)

        if (x, y) in visited or not (0 <= y < len(top_map)) or not (0 <= x < len(top_map[0])):
            continue

        if top_map[y][x] != height:
            continue

        visited.add((x, y))

        # If we reach height 9, this is a valid path
        if height == 9:
            path_count += 1
            continue

        # Explore all valid directions
        for direction, (dx, dy) in DIRECTIONS.items():
            # Avoid immediate backtracking
            if direction != trail[-1] if trail else True:
                queue.append((x + dx, y + dy, height + 1))
                trail.append(direction)

    return path_count


def get_sum_of_trailhead_scores(top_map: list[list[int]]) -> int:
    """Returns the sum of the scores of all trailheads on the map."""
    sum_of_scores = 0

    for y, row in enumerate(top_map):
        for x, num in enumerate(row):
            if num == 0:
                sum_of_scores += bfs_count_paths(x, y, top_map)

    return sum_of_scores


if __name__ == "__main__":
    data = read_input("day_10_data.txt")
    # Part 1
    answer_1 = get_sum_of_trailhead_scores(data)
    print(f"Part 1: {answer_1}")
    
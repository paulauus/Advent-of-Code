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


def is_valid(x: int, y: int, top_map: list[list[int]]) -> bool:
    """Check if a position (x, y) is within bounds of the map."""
    return 0 <= x < len(top_map[0]) and 0 <= y < len(top_map)


def dfs(x: int, y: int, top_map: list[list[int]], visited: set) -> int:
    """
    Depth-first search to count all paths from (x, y) to height 9.
    Returns the number of valid paths.
    """
    if not is_valid(x, y, top_map) or (x, y) in visited:
        return 0

    visited.add((x, y))
    current_height = top_map[y][x]

    # If we reach height 9, this is a valid trail
    if current_height == 9:
        return 1

    trail_count = 0

    # Explore all 4 directions
    for dx, dy in DIRECTIONS.values():
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, top_map) and top_map[ny][nx] == current_height + 1:
            trail_count += dfs(nx, ny, top_map, visited.copy())

    return trail_count


def trailhead_score(x: int, y: int, top_map: list[list[int]]) -> int:
    """Calculate the score for a single trailhead."""
    visited = set()
    return dfs(x, y, top_map, visited)


def bfs_count_paths(start_x: int, start_y: int, top_map: list[list[int]]) -> int:
    """Returns the number of valid paths to height 9 starting from a trailhead."""
    queue = [(start_x, start_y, 0)]  # (x, y, current height)
    visited = set()
    trail = []
    path_count = 0

    while queue:
        x, y, height = queue.pop(0)

        if (x, y) in visited or not 0 <= y < len(top_map) or not 0 <= x < len(top_map[0]):
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
                # Using BFS for now
                sum_of_scores += bfs_count_paths(x, y, top_map)

    return sum_of_scores


def get_sum_of_trailhead_scores_dfs(top_map: list[list[int]]) -> int:
    """Returns the sum of the scores of all trailheads on the map using DFS."""
    sum_of_scores = 0

    for y, row in enumerate(top_map):
        for x, num in enumerate(row):
            if num == 0:  # Found a trailhead
                # Using DFS here
                sum_of_scores += trailhead_score(x, y, top_map)

    return sum_of_scores


if __name__ == "__main__":
    data = read_input("day_10_data.txt")

    # Part 1
    answer_1 = get_sum_of_trailhead_scores(data)
    print(f"Part 1: {answer_1}")

    # Part 1
    answer_2 = get_sum_of_trailhead_scores_dfs(data)
    print(f"Part 2: {answer_2}")

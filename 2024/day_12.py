from collections import deque


def read_input(filename: str) -> list[list[str]]:
    """Reads the input into a list of lists of characters."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [list(line.strip()) for line in f]


def flood_fill(grid, start, visited):
    """Perform flood-fill to identify a region, calculate its area and perimeter."""
    rows, cols = len(grid), len(grid[0])
    region_char = grid[start[0]][start[1]]
    queue = deque([start])
    visited.add(start)

    area = 0
    perimeter = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    while queue:
        r, c = queue.popleft()
        area += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == region_char:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                else:
                    perimeter += 1  # Adjacent to a different plot type
            else:
                perimeter += 1  # Adjacent to the edge of the map

    return area, perimeter


def calculate_total_price(filename):
    grid = read_input(filename)
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                # Found a new region
                area, perimeter = flood_fill(grid, (r, c), visited)
                price = area * perimeter
                total_price += price

    return total_price


if __name__ == "__main__":
    # Part 1
    answer_1 = calculate_total_price("day_12_data.txt")
    print(f"Part 1: {answer_1}")

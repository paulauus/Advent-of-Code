"""Day 12: Garden Groups"""

from collections import deque


def read_grid_from_file(filename: str) -> list[list[str]]:
    """Reads the input into a list of lists of characters (grid)."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [list(line.strip()) for line in f]


def calculate_region_area_and_perimeter(grid, start, visited):
    """Performs flood-fill to identify a region, and calculate its area and perimeter."""
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


def calculate_total_price_of_regions(filename):
    """Calculates the total price by summing the area * perimeter of each region."""
    grid = read_grid_from_file(filename)
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                # Found a new region
                area, perimeter = calculate_region_area_and_perimeter(
                    grid, (r, c), visited)
                price = area * perimeter
                total_price += price

    return total_price


def calculate_total_price_with_boundary_conditions(filename):
    """Calculates the total price for each region considering boundary conditions."""
    grid = read_grid_from_file(filename)
    flattened_grid = [cell for row in grid for cell in row]  # Flatten the grid
    num_cols = len(grid[0])  # Number of columns
    total_price = 0
    visited = set()  # Keep track of visited cells

    def boundary_condition(i, c):
        """Checks if a boundary condition is met."""
        return flattened_grid[i] != c

    def explore_region(i):
        """Recursive function to calculate the area and perimeter of a region."""
        c = flattened_grid[i]  # Current cell
        perimeter = 0  # Perimeter
        area = 1  # Area
        directions = [i >= num_cols and -num_cols, (i + 1) % num_cols and 1, i <
                      num_cols * num_cols - num_cols and num_cols, i % num_cols and -1]  # Directions
        visited.add(i)  # Mark as visited
        for g, direction in enumerate(directions):
            # Get opposite direction
            opposite_direction = directions[(g + 3) % 4]
            perimeter += (not direction and (not opposite_direction or boundary_condition(i + opposite_direction, c))) or (boundary_condition(i + direction, c)
                                                                                                                           and (not opposite_direction or boundary_condition(i + opposite_direction, c) or not boundary_condition(i + opposite_direction + direction, c)))
            if flattened_grid[i + direction] == c and (i + direction) not in visited:
                region_perimeter, region_area = explore_region(i + direction)
                perimeter += region_perimeter
                area += region_area
        return perimeter, area

    for x in range(len(flattened_grid)):
        if x not in visited:  # If not visited
            region_perimeter, region_area = explore_region(x)
            total_price += region_perimeter * region_area

    return total_price


if __name__ == "__main__":
    # Part 1
    part_1_result = calculate_total_price_of_regions("day_12_data.txt")
    print(f"Part 1: {part_1_result}")

    # Part 2
    part_2_result = calculate_total_price_with_boundary_conditions(
        "day_12_data.txt")
    print(f"Part 2: {part_2_result}")

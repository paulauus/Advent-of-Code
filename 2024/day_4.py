"""Day 4: Ceres Search"""


from typing import List


def read_lines(filename: str) -> List[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f.readlines()]


def count_horizontal(grid: List[str], word: str) -> int:
    """Counts occurrences of the word in horizontal directions (left-to-right and right-to-left)."""
    count = 0
    reversed_word = word[::-1]
    for row in grid:
        count += row.count(word)  # Left-to-right
        count += row.count(reversed_word)  # Right-to-left
    return count


def count_vertical(grid: List[str], word: str) -> int:
    """Counts occurrences of the word in vertical directions."""
    count = 0
    reversed_word = word[::-1]
    # Transpose the grid to make columns into rows
    for col in range(len(grid[0])):
        column = ''.join(row[col] for row in grid)
        count += column.count(word)  # Top-to-bottom
        count += column.count(reversed_word)  # Bottom-to-top
    return count


def count_diagonal(grid: List[str], word: str) -> int:
    """Counts occurrences of the word in diagonal directions."""
    count = 0
    reversed_word = word[::-1]
    rows, cols = len(grid), len(grid[0])

    # Get all diagonals (top-left to bottom-right and top-right to bottom-left)
    diagonals = []
    for d in range(-rows + 1, cols):  # Top-left to bottom-right diagonals
        diagonals.append(''.join(grid[r][c] for r in range(
            rows) for c in range(cols) if r - c == d))
    for d in range(rows + cols - 1):  # Top-right to bottom-left diagonals
        diagonals.append(''.join(grid[r][c] for r in range(
            rows) for c in range(cols) if r + c == d))

    # Search for the word in all diagonals
    for diag in diagonals:
        count += diag.count(word)  # Forward diagonal
        count += diag.count(reversed_word)  # Reverse diagonal
    return count


def count_all_occurrences(grid: List[str], word: str) -> int:
    """Counts all occurrences of the word in all directions."""
    horizontal = count_horizontal(grid, word)
    vertical = count_vertical(grid, word)
    diagonal = count_diagonal(grid, word)
    return horizontal + vertical + diagonal


if __name__ == "__main__":
    data = read_lines("day_4_data.txt")
    # Part 1
    WORD = "XMAS"
    answer_1 = count_all_occurrences(data, WORD)
    print(f"Part 1: {answer_1}")

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


def count_xmas_patterns(grid: List[str]) -> int:
    """Counts occurrences of X-MAS patterns in the grid."""
    count = 0
    rows, cols = len(grid), len(grid[0])

    def check_mas(row: int, col: int, dr: int, dc: int) -> bool:
        """Checks if the diagonal starting at (row, col) matches M → A → S or S → A → M."""
        try:
            # Check forward "MAS"
            forward = (grid[row][col] == "M" and
                       grid[row + dr][col + dc] == "A" and
                       grid[row + 2 * dr][col + 2 * dc] == "S")
            # Check reverse "SAM"
            reverse = (grid[row][col] == "S" and
                       grid[row + dr][col + dc] == "A" and
                       grid[row + 2 * dr][col + 2 * dc] == "M")
            return forward or reverse
        except IndexError:
            return False

    # Traverse the grid
    for r in range(1, rows - 1):  # Skip edges (at least 1 row above/below)
        for c in range(1, cols - 1):  # Skip edges (at least 1 column left/right)
            if grid[r][c] == "A":  # Center of the "X"
                # Check top-left to bottom-right "MAS"
                tl_br = check_mas(r - 1, c - 1, 1, 1)
                # Check top-right to bottom-left "MAS"
                tr_bl = check_mas(r - 1, c + 1, 1, -1)

                # Count as X-MAS if both "MAS" patterns exist
                if tl_br and tr_bl:
                    count += 1

    return count

if __name__ == "__main__":
    data = read_lines("day_4_data.txt")
    # Part 1
    WORD = "XMAS"
    answer_1 = count_all_occurrences(data, WORD)
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = count_xmas_patterns(data)
    print(f"Part 2: {answer_2}")

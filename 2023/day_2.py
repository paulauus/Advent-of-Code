"""Day 2: Cube Conundrum"""

def read_input(filename: str) -> list[str]:
    """Returns a list of strings from a .txt file."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f]
    

def is_game_valid(game: str, VALID_GAME: dict) -> bool:
    """Checks if a game is valid against given rules."""
    ...


def sum_of_valid_game_ids(all_games: list[str], VALID_GAME: dict) -> int:
    """Returns the sum of valid game IDs."""
    ...

if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    
    # Part 1

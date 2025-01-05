"""Day 2: Cube Conundrum"""

def read_input(filename: str) -> list[str]:
    """Returns a list of strings from a .txt file."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f]

if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    print(data)

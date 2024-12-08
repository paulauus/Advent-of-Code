"""Day 8: Resonant Collinearity"""

def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f.readlines()]
    
if __name__ == "__main__":
    data = read_lines("day_8_data.txt")
    print(data)

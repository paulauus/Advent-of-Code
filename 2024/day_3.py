"""Day 3: Mull It Over"""

def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:

        return f.read()

if __name__ == "__main__":
    data = read_lines("day_3_data.txt")
    print(data)
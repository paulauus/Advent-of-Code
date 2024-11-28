"""Day 1: Trebuchet?!"""

def read_input(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()

if __name__ == "__main__":
    data = read_input("day_1_data.txt")
    print(data)

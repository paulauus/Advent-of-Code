"""Day 11: Plutonian Pebbles"""

def read_input(filename: str) -> list[str]:
    """Reads the .txt input into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.read().split()
    

if __name__ == "__main__":
    data = read_input("day_11_data.txt")
    print(data)
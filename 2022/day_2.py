"""Day 2: Rock Paper Scissors"""


def read_input(filename: str) -> list[str]:
    """Reads the input from a .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip().split() for line in f]
    

if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    print(data)
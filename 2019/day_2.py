"""Day 2: 1202 Program Alarm"""


def read_input(filename: str) -> list[int]:
    """Reads a text file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [int(num) for num in f.read().strip().split(",")]

if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    print(data)
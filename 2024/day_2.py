"""Day 2: Red-Nosed Reports"""


def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:

        return f.readlines()

if __name__ == "__main__":
    data = read_lines("day_2_data.txt")
    print(data)
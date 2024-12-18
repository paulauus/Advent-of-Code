"""Day 13: Claw Contraption"""

def read_input(filename: str) -> list[list[str]]:
    """Reads the .txt file into a list of lists of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        result = []
        new_list = []
        for line in f.read().split("\n"):
            if line == "":
                result.append(new_list)
                new_list = []
            else:
                new_list.append(line)

    return result

if __name__ == "__main__":
    data = read_input("day_13_data.txt")
    for d in data:
        print(d)

"""Day 10: Hoof It"""


def read_input(filename: str) -> str:
    """Reads the input into a single long string."""
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    nums = []
    for line in lines:
        new_list = []
        for num in line.strip():
            new_list.append(int(num))
        nums.append(new_list)

    return nums


if __name__ == "__main__":
    data = read_input("day_10_data.txt")
    print(data)

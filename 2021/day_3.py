"""Day 3: Binary Diagnostic"""

def read_input(filename: str) -> list[str]:
    """Outputs a list of strings."""
    with open(filename, "r") as f:
        return f.read().splitlines()
    
def find_gamma_rate(file: str) -> int:
    """Finds the gamma rate of submarine."""
    counts = {}
    for line in file:
        for i, number in enumerate(line):
            if counts.get(i) is None:
                counts[i] = [0, 0]
            if number == "0":
                counts[i][0] += 1
            if number == "1":
                counts[i][1] += 1

    gamma_rate = ""
    for key in counts:
        if counts[key][0] > counts[key][1]:
            gamma_rate += "0"
        else:
            gamma_rate += "1"

    return gamma_rate


def find_epsilon_rate(gamma: int) -> int:
    """Finds the epsilon rate of submarine."""
    epsilon_rate = ""
    for i in gamma:
        if i == "0":
            epsilon_rate += "1"
        if i == "1":
            epsilon_rate += "0"

    return epsilon_rate

def change_binary_to_decimal(binary: str) -> int:
    """Changes a binary number to decimal."""
    return int(binary, 2)


if __name__ == "__main__":

    data = read_input("day_3_data.txt")

    gamma_rate = find_gamma_rate(data)
    epsilon_rate = find_epsilon_rate(gamma_rate)
    answer_1 = change_binary_to_decimal(gamma_rate) * change_binary_to_decimal(epsilon_rate)

    print(f"Part 1: {answer_1}")
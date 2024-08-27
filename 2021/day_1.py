"""Day 1: Sonar Sweep"""


def read_input(filename: str) -> list[str]:
    """Reads the data from a .txt file used in the main function."""
    with open(filename, "r") as f:
        return f.readlines()

def depth_measurement_increases(data: list[str]) -> int:
    """Counts the number of times a depth measurement increases from the previous measurement."""
    counter = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            counter += 1
    return counter


if __name__ == "__main__":
    
    # Specify the filename of the input file
    filename = 'data.txt'

    # Read data from the file
    data = read_input(filename)

    # Calculate the number of increases
    increases = depth_measurement_increases(data)

    # Print the result
    print(f"Number of increases: {increases}")


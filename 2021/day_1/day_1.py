"""Day 1: Sonar Sweep"""


def read_input(filename: str) -> list[str]:
    """Reads the data from a .txt file used in the main function."""
    with open(filename, "r") as f:
        return f.readlines()

def depth_measurement_increases(data: list[str]) -> int:
    """Counts the number of times a depth measurement increases from the previous measurement."""
    data = [int(x) for x in data]
    counter = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            counter += 1
    return counter


def triple_increases(data: list[int]) -> int:
    """Counts the number of times the sum of three measurements
    in a sliding window increases."""
    data = [int(x) for x in data]
    counter = 0
    # Loop from index 1 to len(data) - 3 (stopping before the last full window)
    for i in range(1, len(data) - 2):
        # Calculate the sum of the current window and the previous window
        total_a = data[i] + data[i+1] + data[i+2]
        total_b = data[i-1] + data[i] + data[i+1]

        # Compare the sums
        if total_a > total_b:
            counter += 1

    return counter


if __name__ == "__main__":
    
    # Specify the filename of the input file
    filename = 'data.txt'
    
    # Read data from the file
    data = read_input(filename)

    # Calculate the number of increases
    single_increases = depth_measurement_increases(data)

    # Print the result
    print(f"Number of increases: {single_increases}")

    triple_increases = triple_increases(data)

    print(f"Number of sliding window increases: {triple_increases}")

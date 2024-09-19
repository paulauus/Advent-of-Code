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


def find_oxygen_generator_rating() -> str:
    """Calculates the oxygen generator rating."""
    final_list = read_input(
        "day_3_data.txt")
    bit_length = len(final_list[0])

    for i in range(bit_length):
        if len(final_list) == 1:  # Stop if only one number remains
            break

        # Calculate the most common bit at the current position (i)
        count_ones = sum(1 for number in final_list if number[i] == '1')
        count_zeroes = len(final_list) - count_ones

        # Most common bit: '1' if ones are equal or more, otherwise '0'
        most_common_bit = '1' if count_ones >= count_zeroes else '0'

        # Filter the list by keeping numbers that match the most common bit at position i
        final_list = [
            reading for reading in final_list if reading[i] == most_common_bit]

    return final_list[0]


def find_CO2_scrubber_rating() -> str:
    """Calculates the CO2 scrubber rating."""
    final_list = read_input(
        "day_3_data.txt")
    bit_length = len(final_list[0])

    for i in range(bit_length):
        if len(final_list) == 1:
            break

        # Calculate the most common bit at the current position
        count_ones = sum(1 for number in final_list if number[i] == '1')
        count_zeroes = len(final_list) - count_ones

        least_common_bit = '0' if count_ones >= count_zeroes else '1'

        final_list = [
            reading for reading in final_list if reading[i] == least_common_bit]

    return final_list[0]



if __name__ == "__main__":

    data = read_input("day_3_data.txt")

    gamma_rate = find_gamma_rate(data)
    epsilon_rate = find_epsilon_rate(gamma_rate)
    answer_1 = change_binary_to_decimal(gamma_rate) * change_binary_to_decimal(epsilon_rate)

    print(f"Part 1: {answer_1}")

    oxygen_rating = find_oxygen_generator_rating()
    co2_rating = find_CO2_scrubber_rating()
    answer_2 = change_binary_to_decimal(oxygen_rating) * change_binary_to_decimal(co2_rating)

    print(f"Part 2: {answer_2}")
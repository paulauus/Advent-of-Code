"""Day 2: 1202 Program Alarm"""


def read_input(filename: str) -> list[int]:
    """Reads a text file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [int(num) for num in f.read().strip().split(",")]


def run_program(program_data: list[int]) -> int:
    """Runs the Intcode program."""
    i = 0  # Start at the beginning of the program
    while i < len(program_data):
        opcode = program_data[i]

        if opcode == 99:  # Halt
            break
        if opcode in [1, 2]:  # Addition or multiplication
            pos1, pos2, pos3 = program_data[i +
                                            1], program_data[i + 2], program_data[i + 3]

            # Ensure all positions are within bounds before proceeding
            if pos1 >= len(program_data) or pos2 >= len(program_data) or pos3 >= len(program_data):
                # Out of range: break out to prevent errors
                return None

            if opcode == 1:  # Addition
                program_data[pos3] = program_data[pos1] + program_data[pos2]
            elif opcode == 2:  # Multiplication
                program_data[pos3] = program_data[pos1] * program_data[pos2]

            # Move to the next instruction (4 positions ahead)
            i += 4
        else:
            # Invalid opcode encountered
            return None

    return program_data[0]


def find_noun_and_verb(original_program_data: list[int]) -> int:
    """Finds the input noun and verb that cause the program to produce the output 19690720."""
    for noun in range(100):
        for verb in range(100):
            # Make a fresh copy of the original program data for each attempt
            attempt_data = original_program_data[:]
            attempt_data[1] = noun
            attempt_data[2] = verb

            # Run the program and check the output
            answer = run_program(attempt_data)

            if answer == 19690720:
                return 100 * noun + verb

    return None


if __name__ == "__main__":
    original_data = read_input("day_2_data.txt")
    # Part 1
    part1_data = original_data[:]  # Make a copy for Part 1
    part1_data[1], part1_data[2] = 12, 2
    answer_1 = run_program(part1_data)
    print(f"Part 1: {answer_1}")

    # Part 2
    answer_2 = find_noun_and_verb(original_data)
    print(f"Part 2: {answer_2}")

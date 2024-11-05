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
        if opcode == 1:  # Addition
            pos1 = program_data[i + 1]
            pos2 = program_data[i + 2]
            pos3 = program_data[i + 3]
            program_data[pos3] = program_data[pos1] + program_data[pos2]
        elif opcode == 2:  # Multiplication
            pos1 = program_data[i + 1]
            pos2 = program_data[i + 2]
            pos3 = program_data[i + 3]
            program_data[pos3] = program_data[pos1] * program_data[pos2]

        # Move to the next instruction (4 positions ahead)
        i += 4

    return program_data[0]


def find_noun_and_verb(program_data: list[int]) -> int:
    """Finds the input noun and verb that cause the program to produce the output 19690720."""
    for noun in range(100):
        for verb in range(100):
            # Make a fresh copy of program_data for each attempt
            attempt_data = program_data[:]
            attempt_data[1] = noun
            attempt_data[2] = verb
            answer = run_program(attempt_data)
            if answer == 19690720:
                return 100 * noun + verb


if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    # Part 1
    data[1], data[2] = 12, 2
    answer_1 = run_program(data)
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = find_noun_and_verb(data)
    print(f"Part 2: {answer_2}")

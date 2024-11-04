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


if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    data[1], data[2] = 12, 2
    answer_1 = run_program(data)
    print(f"Part 1: {answer_1}")

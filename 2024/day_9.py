"""Day 9: Disk Fragmenter"""


def read_input(filename: str) -> str:
    """Reads the input into a single long string."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.read().strip()


def create_blocks(disk_map: str) -> list:
    """Creates the individual blocks from the disk map."""
    blocks = []
    counter = 0

    for i, digit in enumerate(disk_map):
        if i % 2 == 0:
            for x in range(int(digit)):
                blocks.append(counter)
            counter += 1
        if i % 2 != 0:
            for y in range(int(digit)):
                blocks.append(-1)

    return blocks


def move_file_blocks(blocks: list) -> list:
    """Moves file blocks one at a time from the end of the disk to the leftmost free space."""
    empties = [i for i, val in enumerate(
        blocks) if val == -1]  # Indices of empty spaces
    i = 0  # Pointer to free spaces

    while True:
        # Remove trailing free spaces
        while blocks and blocks[-1] == -1:
            blocks.pop()

        target = empties[i]

        if target >= len(blocks):  # No more moves to make
            break

        # Move the last file block to the leftmost free space
        blocks[target] = blocks.pop()
        i += 1

    return blocks


def calculate_checksum(blocks: list) -> int:
    """Calculates and returns the checksum of the disk after compaction."""
    checksum = 0
    for i, val in enumerate(blocks):
        if val != -1:  # Only consider blocks with files (not free spaces)
            checksum += i * val
    return checksum


def solve_disk_fragmenter(disk_map: str) -> int:
    """Main function to solve the problem."""
    blocks = create_blocks(disk_map)
    compacted_blocks = move_file_blocks(blocks)
    return calculate_checksum(compacted_blocks)


if __name__ == "__main__":
    disk_map = read_input("day_9_data.txt")
    # Part 1
    answer_1 = solve_disk_fragmenter(disk_map)
    print(f"Part 1: {answer_1}")

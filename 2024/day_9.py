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


def compact_files(data: str) -> int:
    """
    Compact files by moving whole files into the leftmost free space
    that fits, and return the checksum of the resulting layout.
    """
    is_file = True
    # Store file locations and sizes as {file_id: (start_position, size)}
    files = {}
    spaces = []  # Store free spaces as [(start_position, size)]
    ptr = 0

    # Parse the input into files and spaces
    for i, size in enumerate(map(int, data)):
        if is_file:
            files[i // 2] = (ptr, size)
        else:
            spaces.append((ptr, size))
        is_file = not is_file
        ptr += size

    # Process files in reverse order of file ID
    for fid in sorted(files.keys(), reverse=True):
        loc, file_size = files[fid]
        space_id = 0
        while space_id < len(spaces):
            space_loc, space_size = spaces[space_id]
            # Stop if the free space is past the file
            if space_loc > loc:
                break
            if space_size == file_size:
                # Exact fit
                files[fid] = (space_loc, file_size)
                spaces.pop(space_id)
                break
            if space_size > file_size:
                # Partial fit, update the free space
                files[fid] = (space_loc, file_size)
                spaces[space_id] = (space_loc + file_size,
                                    space_size - file_size)
                break
            # Move to the next free space
            space_id += 1

    # Calculate the checksum
    checksum = 0
    for fid, (loc, size) in files.items():
        for i in range(loc, loc + size):
            checksum += fid * i

    return checksum

if __name__ == "__main__":
    disk_map = read_input("day_9_data.txt")
    # Part 1
    answer_1 = solve_disk_fragmenter(disk_map)
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = compact_files(disk_map)
    print(f"Part 2: {answer_2}")

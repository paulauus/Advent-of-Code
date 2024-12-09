"""Day 9: Disk Fragmenter"""

def read_input(filename: str) -> str:
    """Reads the input into a single long string."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.read()
    

def create_blocks(disk_map: str) -> str:
    """Creates the individual blocks from the disk map."""
    blocks = ""
    counter = 0
    
    for i, digit in enumerate(disk_map):

        if i % 2 == 0:
            blocks += int(digit) * str(counter)
        if i % 2 != 0:
            blocks += int(digit) * "."

        counter += 1

    return blocks


def move_file_blocks(blocks: str) -> str:
    """
    Moves file blocks one at a time from the end of the disk to the leftmost 
    free space block until there are no gaps remaining between file blocks.
    """
    block_list = [i for i in blocks]

    for i, digit in enumerate(block_list):
        if digit == ".":
            while block_list[-1] == ".":
                del block_list[-1]
            block_list[i] = block_list.pop(-1)

    return block_list

if __name__ == "__main__":
    data = read_input("day_9_data.txt")
    blocks = create_blocks(data)
    answer_1 = move_file_blocks(blocks)
    print(answer_1)
    
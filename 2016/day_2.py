"""Day 2: Bathroom Security"""

def read_input(filename: str) -> str:
    """Reads a text file into a str."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.read()

# Define the keypad layout with coordinates
keypad = {
    (-1, 1): "1",
    (0, 1): "2",
    (1, 1): "3",
    (-1, 0): "4",
    (0, 0): "5",
    (1, 0): "6",
    (-1, -1): "7",
    (0, -1): "8",
    (1, -1): "9"
    }

keypad_2 = {
    (0, 2): "1",
    (-1, 1): "2",
    (0, 1): "3",
    (1, 1): "4",
    (-2, 0): "5",
    (-1, 0): "6",
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (-1, -1): "A",
    (0, -1): "B",
    (1, -1): "C",
    (0, -2): "D"
}


def get_keypad_code(data: str, keys: dict) -> str:
    """Returns the code for the keypad based on input."""
    x, y = 0, 0  # Start at '5' which is at (0, 0)
    answer = ""

    # Process each line of instructions
    for line in data.splitlines():
        for move in line:
            # Move up (U)
            if move == "U" and (x, y + 1) in keys:
                y += 1
            # Move down (D)
            elif move == "D" and (x, y - 1) in keys:
                y -= 1
            # Move left (L)
            elif move == "L" and (x - 1, y) in keys:
                x -= 1
            # Move right (R)
            elif move == "R" and (x + 1, y) in keys:
                x += 1
        # Append the current button to the answer after processing each line
        answer += keys[(x, y)]

    return answer


if __name__ == "__main__":
    instructions = read_input("day_2_data.txt")
    code = get_keypad_code(instructions, keypad)
    print(f"Part 1: {code}")
    code_2 = get_keypad_code(instructions, keypad_2)
    print(f"Part 2: {code_2}")
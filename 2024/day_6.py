"""Day 6: Guard Gallivant"""

def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f.readlines()]
    

def find_distinct_positions(mapped_area: list[str]) -> int:
    """Returns the number of distinct positions visited by the guard."""
    distinct_positions = []
    max_width = len(mapped_area[0]) - 1
    max_length = len(mapped_area) - 1
    directions = ["up", "right", "down", "left"]
    moves = {
        "up": (0, -1),
        "right": (1, 0),
        "down": (0, 1),
        "left": (-1, 0)
    }
    
    for i, row in enumerate(mapped_area):
        for j, spot in enumerate(row):
            if spot == "^":
                x = j
                y = i
                distinct_positions.append((x, y))

    direction = "up"

    while True:
        

    
if __name__ == "__main__":
    data = read_lines("day_6_data.txt")
    print(find_distinct_positions(data))

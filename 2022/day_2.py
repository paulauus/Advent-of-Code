"""Day 2: Rock Paper Scissors"""


POINTS = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

RESULTS = {
    "WIN": [["A", "Y"], ["B", "Z"], ["C", "X"]],
    "DRAW": [["A", "X"], ["B", "Y"], ["C", "Z"]],
    "LOSE": [["A", "Z"], ["B", "X"], ["C", "Y"]]
}

GUIDE = {
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN"
}


def read_input(filename: str) -> list[list[str]]:
    """Reads the input from a .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip().split() for line in f]


def calculate_player_score(guide: list[list[str]]) -> int:
    """Calculates the player's score from the given gameplay."""
    player_score = 0

    for i in guide:
        player_score += POINTS[i[1]]
        if i in RESULTS["WIN"]:
            player_score += 6
        if i in RESULTS["DRAW"]:
            player_score += 3

    return player_score


def calculate_score_with_guide(guide: list[list[str]]) -> int:
    """Calculates the player's score with given round results."""
    player_score = 0

    for a in guide:
        if a[1] == "Y":
            player_score += 3
        if a[1] == "Z":
            player_score += 6
        
        for b in RESULTS[GUIDE[a[1]]]:
            if b[0] == a[0]:
                player_score += POINTS[b[1]]

    return player_score


if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    # Part 1
    answer_1 = calculate_player_score(data)
    print(f"Part 1: {answer_1}")
    #Part 2
    answer_2 = calculate_score_with_guide(data)
    print(f"Part 2: {answer_2}")

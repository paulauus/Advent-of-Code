"""Day 5: Print Queue"""


def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f.readlines()]


def get_rules(sections: list[str]) -> list[tuple[int, int]]:
    """Returns the rules as tuples of integers."""
    rules = []

    for line in sections:
        if line == "":
            break
        # Split rule and convert to integers
        before, after = map(int, line.split("|"))
        rules.append((before, after))

    return rules


def get_updates(sections: list[str]) -> list[list[int]]:
    """Returns the updates as lists of integers."""
    updates = []
    parsing = False

    for line in sections:
        if line == "":
            parsing = True
            continue
        if parsing:
            # Split and convert to integers
            updates.append(list(map(int, line.split(","))))

    return updates


def find_valid_updates(rules: list[tuple[int, int]], updates: list[list[int]]) -> list[list[int]]:
    """Returns only the valid updates from the initial list."""
    valid_updates = []

    for update in updates:
        is_valid = True

        for before, after in rules:
            if before in update and after in update:
                if update.index(before) > update.index(after):
                    is_valid = False
                    break

        if is_valid:
            valid_updates.append(update)

    return valid_updates


def find_invalid_updates(rules: list[tuple[int, int]], updates: list[list[int]]) -> list[list[int]]:
    """Returns only the invalid updates from the initial list."""
    invalid_updates = []

    for update in updates:
        is_valid = True

        for before, after in rules:
            if before in update and after in update:
                if update.index(before) > update.index(after):
                    is_valid = False  # Rule violated
                    break

        if not is_valid:
            invalid_updates.append(update)

    return invalid_updates


def reorder_invalid_updates(rules: list[tuple[int, int]], invalid_updates: list[list[int]]
                            ) -> list[list[int]]:
    """Reorders the invalid updates according to the correct rules."""
    for update in invalid_updates:
        reordered = True  # Flag to track if changes were made in this iteration
        while reordered:
            reordered = False
            for before, after in rules:
                if before in update and after in update:
                    before_idx = update.index(before)
                    after_idx = update.index(after)
                    if before_idx > after_idx:
                        # Swap the positions of before and after
                        update.insert(after_idx, update.pop(before_idx))
                        reordered = True
    return invalid_updates

def find_sum_of_middle_numbers(valid_updates: list[list[int]]) -> int:
    """Adds the middle number of each line."""
    total = 0

    for update in valid_updates:
        middle_index = len(update) // 2
        total += update[middle_index]  # Get the middle element

    return total


if __name__ == "__main__":
    data = read_lines("day_5_data.txt")
    rules = get_rules(data)
    updates = get_updates(data)
    # Part 1
    answer_1 = find_sum_of_middle_numbers(find_valid_updates(rules, updates))
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = find_sum_of_middle_numbers(reorder_invalid_updates(
        rules, find_invalid_updates(rules, updates)))
    print(f"Part 2: {answer_2}")

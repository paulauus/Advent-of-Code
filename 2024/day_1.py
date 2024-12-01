"""Day 1: Historian Hysteria"""


def read_input(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:

        return f.readlines()


def get_sorted_list(locations: list[str]) -> list[list[int]]:
    """Returns a list with two sorted lists of integers."""
    list_1 = []
    list_2 = []

    for line in locations:
        split_nums = line.strip().split()
        list_1.append(int(split_nums[0]))
        list_2.append(int(split_nums[1]))

    return [sorted(list_1), sorted(list_2)]


def find_distances(sorted_list: list[list[int]]) -> int:
    """Finds the total distance between the lists."""
    total_distance = 0

    for i in range(len(sorted_list[0])):
        distance = abs(sorted_list[0][i] - sorted_list[1][i])
        total_distance += distance

    return total_distance


def calculate_similarity_score(sorted_list: list[list[int]]) -> int:
    """
    Adds up each number in the left list after multiplying it 
    by the number of times that number appears in the right list.
    """
    similarity_score = 0

    for num in sorted_list[0]:
        similarity_score += num * sorted_list[1].count(num)

    return similarity_score

if __name__ == "__main__":
    data = read_input("day_1_data.txt")
    # Part 1
    answer_1 = find_distances(get_sorted_list(data))
    print(f"Part 1: {answer_1}")
    # Part 2
    answer_2 = calculate_similarity_score(get_sorted_list(data))
    print(f"Part 2: {answer_2}")

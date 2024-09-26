"""Day 1: Inverse Captcha"""

def read_input(filename: str) -> str:
    """Reads a text file into a str."""
    with open(filename, "r") as f:
        return f.read()


def find_sum(s: str) -> int:
    """Finds the sum of all digits that match the next digit."""
    answer = 0

    if s[0] == s[-1]:
        answer += int(s[-1])

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            answer += int(s[i-1])

    return answer

def find_sum_2(s: str) -> int:
    """Finds the sum of all digits that match the one 1/2len away."""
    answer = 0
    marker = int(len(s) / 2)

    for i in range(len(s)):
        if i < marker:
            if s[i] == s[i+marker]:
                answer += int(s[i])
        if i >= marker:
            if s[i] == s[i-marker]:
                answer += int(s[i])

    return answer



if __name__ == "__main__":

    FILENAME = "day_1_data.txt"
    data = read_input(FILENAME)

    answer_1 = find_sum(data)
    print(f"Part 1: {answer_1}")

    answer_2 = find_sum_2(data)
    print(f"Part 2: {answer_2}")

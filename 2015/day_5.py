"""Day 5: Doesn't He Have Intern-Elves For This?"""


def read_input(filename: str) -> list[str]:
    """Reads the data from a .txt file."""
    with open(filename, "r") as f:
        return f.readlines()


def has_three_vowels(s):
    """Checks the string has three vowels."""
    vowels = "aeiou"
    vowel_count = 0
    for letter in s:
        if letter in vowels:
            vowel_count += 1
    if vowel_count >= 3:
        return True
    
    return False

def has_double_letter(s):
    """Checks the string has a double letter."""
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return True
        
    return False


def no_bad_strings(s):
    """Checks the string does not have bad pairs."""
    bad_pairs = {"ab", "cd", "pq",
                 "xy"}  # Define the bad pairs as a set for quick lookup

    for i in range(len(s) - 1):
        pair = s[i:i+2]
        if pair in bad_pairs:
            return False

    return True
            

def count_nice_strings(data: list) -> int:
    """Counts the number of nice strings."""
    nice_strings = 0
    for string in data:
        if has_three_vowels(string) and has_double_letter(string) and no_bad_strings(string):
            nice_strings += 1
    return nice_strings

if __name__ == "__main__":
    
    string_data = read_input("day_5_data.txt")

    answer = count_nice_strings(string_data)

    print(f"Part 1: There are {answer} nice strings.")
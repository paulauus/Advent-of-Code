"""Day 5: Print Queue"""

def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f.readlines()]
    

def get_rules(sections: list[str]) -> list[str]:
    """Returns only the rules from the given input."""
    for i, item in enumerate(sections):
        if item == "":
            return sections[:i]
        
    return None
    

def get_files(sections: list[str]) -> list[str]:
    """Returns only the files from the given input."""
    for i, item in enumerate(sections):
        if item == "":
            return sections[i+1:]

    return None

if __name__ == "__main__":
    data = read_lines("day_5_data.txt")
    rules = get_rules(data)
    files = get_files(data)
    print(files)

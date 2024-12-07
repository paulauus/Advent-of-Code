"""Day 7: Bridge Repair"""


def read_lines(filename: str) -> list[str]:
    """Reads the .txt file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return [line.strip() for line in f.readlines()]
    

def get_integers(raw_input: list[str]) -> list[list[int]]:
    """Extracts numbers from the raw input as a list of lists."""
    final_list = []
    
    for line in raw_input:
        int_list = []
        list_1 = line.split(":")
        int_list.append(int(list_1[0]))
        int_list += [int(num) for num in list_1[1].strip().split()]

        final_list.append(int_list)

    return final_list

if __name__ == "__main__":
    data = read_lines("day_7_data.txt")
    clean_data = get_integers(data)
    print(clean_data)

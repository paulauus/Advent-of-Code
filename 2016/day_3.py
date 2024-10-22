"""Day 3: Squares With Three Sides"""


def read_input(filename: str) -> str:
    """Reads a text file into a str."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def get_is_triangle(data: list[str]) -> int:
    """Returns the number of valid triangles in the input."""
    triangle_count = 0
    for line in data:
        # Split and convert to integers
        a, b, c = map(int, line.split())
        # Check the triangle inequality theorem
        if (a + b > c) and (b + c > a) and (c + a > b):
            triangle_count += 1

    return triangle_count

if __name__ == "__main__":
    readings = read_input("day_3_data.txt")
    answer_1 = get_is_triangle(readings)
    print(f"Part 1: {answer_1}")

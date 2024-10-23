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

def create_vertical_triangles(data: list[str]) -> list[list]:
    """Returns a list of new triangles."""
    new_list = []
    # Creates a list of lists
    for line in data:
        new_list.append(line.split())

    vertical_list = []
    for i in range(len(new_list)):
        if i % 3 == 0:
            vertical_list.append(
                [int(new_list[i][0]), int(new_list[i+1][0]), int(new_list[i+2][0])])
            vertical_list.append(
                [int(new_list[i][1]), int(new_list[i+1][1]), int(new_list[i+2][1])])
            vertical_list.append(
                [int(new_list[i][2]), int(new_list[i+1][2]), int(new_list[i+2][2])])

    return vertical_list


def get_is_triangle_vertical(data: list[list]) -> int:
    """Returns the number of valid triangles in the new list."""
    triangle_count = 0
    for line in data:
        if (line[0] + line[1] > line[2]) and (
            line[1] + line[2] > line[0]) and (
                line[2] + line[0] > line[1]):
            triangle_count += 1

    return triangle_count

if __name__ == "__main__":
    # Part 1
    readings = read_input("day_3_data.txt")
    answer_1 = get_is_triangle(readings)
    print(f"Part 1: {answer_1}")
    # Part 2
    vertical_triangles = create_vertical_triangles(readings)
    answer_2 = get_is_triangle_vertical(vertical_triangles)
    print(f"Part 2: {answer_2}")

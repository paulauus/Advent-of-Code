"""Day 1: The Tyranny of the Rocket Equation"""

import math


def read_input(filename: str) -> list[str]:
    """Reads a text file into a list of strings."""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def calculate_fuel_requirement(modules: list[str]) -> int:
    """Calculates the sum of the fuel requirements for all of the modules."""
    fuel_requirement = 0
    for module in modules:
        fuel_requirement += (math.floor(int(module) / 3) - 2)

    return fuel_requirement


def calculate_added_fuel_requirement(modules: list[str]) -> int:
    """Calculates the fuel requirement with added mass."""
    fuel_requirement = 0
    for module in modules:
        mass = int(module)
        while mass > 0:
            mass = (math.floor(mass / 3) - 2)
            if mass > 0:
                fuel_requirement += mass

    return fuel_requirement


if __name__ == "__main__":
    data = read_input("day_1_data.txt")
    answer_1 = calculate_fuel_requirement(data)
    print(f"Part 1: {answer_1}")
    answer_2 = calculate_added_fuel_requirement(data)
    print(f"Part 2; {answer_2}")

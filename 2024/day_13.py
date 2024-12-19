"""Day 13: Claw Contraption"""

from typing import Optional


def read_input(filename: str) -> list[dict]:
    """Reads the .txt file and parses the claw machine configurations."""
    with open(filename, "r", encoding="UTF-8") as f:
        machines = []
        for block in f.read().strip().split("\n\n"):
            lines = block.split("\n")
            machine = {
                "A": [int(num.split("+")[1]) for num in lines[0].split(": ")[1].split(", ")],
                "B": [int(num.split("+")[1]) for num in lines[1].split(": ")[1].split(", ")],
                "prize": [int(num.split("=")[1]) for num in lines[2].split(": ")[1].split(", ")],
            }
            machines.append(machine)

    return machines


def solve_claw_machine(
        a: list[int], b: list[int], prize: list[int], max_presses: int = 100) -> Optional[int]:
    """
    Solves the claw machine problem for one machine.
    Returns the minimum tokens needed, or None if no solution exists.
    """
    ax, ay = a
    bx, by = b
    px, py = prize

    min_cost = float('inf')
    found_solution = False

    # Iterate through all possible combinations of presses for A and B
    for presses_a in range(max_presses + 1):
        for presses_b in range(max_presses + 1):
            # Calculate claw position
            x = presses_a * ax + presses_b * bx
            y = presses_a * ay + presses_b * by

            # Check if the claw aligns with the prize
            if x == px and y == py:
                cost = presses_a * 3 + presses_b * 1
                if cost < min_cost:
                    min_cost = cost
                    found_solution = True

    return min_cost if found_solution else None


def solve_all_claw_machines(machines: list[dict]) -> int:
    """
    Solves the claw machine problem for all machines.
    Returns the total minimum tokens needed to win all possible prizes.
    """
    total_tokens = 0
    for machine in machines:
        a = machine["A"]
        b = machine["B"]
        prize = machine["prize"]
        cost = solve_claw_machine(a, b, prize)
        if cost is not None:
            total_tokens += cost

    return total_tokens


if __name__ == "__main__":
    data = read_input("day_13_data.txt")

    # Part 1
    result = solve_all_claw_machines(data)
    print(f"Part 1: {result}")

#!/usr/bin/env python3
"""2023 AoC Day 2"""
import math
from pathlib import Path
from collections import defaultdict

INPUT = Path(__file__) / "../../inputs/d2.txt"


def solve_part_1():
    """Solve the first puzzle."""
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    total = 0
    with INPUT.resolve().open() as file_in:
        for line in file_in:
            game, draws = line.split(":", 1)
            for draw in draws.split(";"):
                failed = False
                totals = defaultdict(lambda: 0)
                for cubes in draw.split(","):
                    num, color = cubes.strip().split(" ", 1)
                    totals[color] += int(num)
                    if totals[color] > limits[color]:
                        failed = True
                        break

                if failed:
                    break

            if not failed:
                total += int(game.split(" ", 1)[-1])

    return total


def solve_part_2():
    """Solve the second puzzle."""
    total = 0
    with INPUT.resolve().open() as file_in:
        for line in file_in:
            draws = line.split(":", 1)[-1]
            n_cubes = defaultdict(lambda: 0)
            for draw in draws.split(";"):
                totals = defaultdict(lambda: 0)
                for cubes in draw.split(","):
                    num, color = cubes.strip().split(" ", 1)
                    totals[color] += int(num)

                for color, num in totals.items():
                    n_cubes[color] = max(n_cubes[color], num)

            total += math.prod(n_cubes.values())

    return total


def main():
    """The main function"""
    print("Part 1:", solve_part_1())
    print("Part 2:", solve_part_2())


if __name__ == "__main__":
    main()

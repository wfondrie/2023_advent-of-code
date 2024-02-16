#!/usr/bin/env python3
"""2023 AoC Day 2"""
from pathlib import Path

import polars as pl

INPUT = Path(__file__) / "../../inputs/d1.txt"


def solve_part_1():
    """Solve the first puzzle."""
    return (
        pl.read_csv(INPUT.resolve(), has_header=False)
        .with_columns([
            pl.all().str.extract(r"^.*?(\d).*$").alias("first"),
            pl.all().str.extract(r"^.*(\d).*?$").alias("last")
        ])
        .select((pl.col("first") + pl.col("last")).cast(pl.Int32).sum())
        .item()
    )


def solve_part_2():
    """Solve the second puzzle."""
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    # A regex for digits or number strings:
    regex = r"(\d|" + "|".join(numbers.keys()) + ")"
    return (
        pl.read_csv(INPUT.resolve(), has_header=False)
        .with_columns([
            (
                pl.all()
                .str.extract(f"^.*?{regex}.*$")
                .replace(numbers)
                .alias("first")
            ),
            (
                pl.all()
                .str.extract(f"^.*{regex}.*?$")
                .replace(numbers)
                .alias("last")
            ),
        ])
        .select((pl.col("first") + pl.col("last")).cast(pl.Int32).sum())
        .item()
    )


def main():
    """The main function"""
    print("Part 1:", solve_part_1())
    print("Part 2:", solve_part_2())


if __name__ == "__main__":
    main()

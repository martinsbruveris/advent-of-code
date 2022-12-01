from pathlib import Path

import click
import numpy as np


def calc_fuel_cost(positions: np.ndarray, target: int, part: str):
    dists = np.abs(positions - target)
    if part == "a":
        costs = dists
    else:
        costs = dists * (dists + 1) // 2
    return np.sum(costs)


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    positions = filename.read_text().split(",")
    positions = np.asarray(positions).astype(int)

    fuel_cost = [
        calc_fuel_cost(positions, target, part)
        for target in range(np.min(positions), np.max(positions) + 1)
    ]
    min_fuel_cost = np.min(fuel_cost)
    print(min_fuel_cost)


if __name__ == "__main__":
    main()

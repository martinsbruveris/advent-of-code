import numpy as np


def calc_fuel_cost(positions: np.ndarray, target: int, part: str):
    dists = np.abs(positions - target)
    if part == "a":
        costs = dists
    else:
        costs = dists * (dists + 1) // 2
    return np.sum(costs)


def main(data, part):
    positions = data.split(",")
    positions = np.asarray(positions).astype(int)

    fuel_cost = [
        calc_fuel_cost(positions, target, part)
        for target in range(np.min(positions), np.max(positions) + 1)
    ]
    min_fuel_cost = np.min(fuel_cost)
    return min_fuel_cost

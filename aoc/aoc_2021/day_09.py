from math import prod

import numpy as np


def basin_size(arr, x, y):
    member = np.zeros_like(arr)  # Basin membership
    member[x, y] = 1

    for _ in range(9):  # Basins can never extend more than 10 squares from origin
        member[1:-1, 1:-1] = np.maximum(
            member[1:-1, 1:-1], (arr[1:-1, 1:-1] > arr[2:, 1:-1]) * member[2:, 1:-1]
        )
        member[1:-1, 1:-1] = np.maximum(
            member[1:-1, 1:-1], (arr[1:-1, 1:-1] > arr[:-2, 1:-1]) * member[:-2, 1:-1]
        )
        member[1:-1, 1:-1] = np.maximum(
            member[1:-1, 1:-1], (arr[1:-1, 1:-1] > arr[1:-1, 2:]) * member[1:-1, 2:]
        )
        member[1:-1, 1:-1] = np.maximum(
            member[1:-1, 1:-1], (arr[1:-1, 1:-1] > arr[1:-1, :-2]) * member[1:-1, :-2]
        )
        member[arr == 9] = 0  # 9s are never part of basins
    return np.sum(member)


def main(data, part):
    heights = data.split("\n")
    heights = [[int(height) for height in line] for line in heights]
    heights = np.asarray(heights)

    arr = np.pad(heights, pad_width=10, mode="constant", constant_values=9)
    heights = arr[1:-1, 1:-1]
    left = arr[:-2, 1:-1]
    right = arr[2:, 1:-1]
    top = arr[1:-1, :-2]
    bottom = arr[1:-1, 2:]
    min_neighbour = np.min([left, right, top, bottom], axis=0)
    is_low = heights < min_neighbour

    if part == "a":
        low_heights = heights[is_low]
        result = np.sum(1 + low_heights)
    else:
        indices = np.argwhere(is_low) + 1  # +1 to add the margin back in
        basins = [
            basin_size(arr[x - 10 : x + 10, y - 10 : y + 10], 10, 10)
            for x, y in indices
        ]
        basins.sort(reverse=True)
        result = prod(basins[:3])
    return result

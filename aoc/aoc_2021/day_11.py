from itertools import count

import numpy as np


def step(arr):
    arr += 1
    xm, ym = arr.shape

    while np.sum((9 < arr) & (arr < 20)) > 0:
        indices = np.argwhere((9 < arr) & (arr < 20))
        arr[arr > 9] = 20
        for x, y in indices:
            arr[
                max(x - 1, 0) : min(x + 2, xm),
                max(y - 1, 0) : min(y + 2, ym),
            ] += 1
    flashes = np.sum(arr > 9)
    arr[arr > 9] = 0
    return flashes, arr


def main(data, part):
    energies = data.split("\n")
    energies = [[int(e) for e in line] for line in energies]
    energies = np.asarray(energies)

    if part == "a":
        result = 0
        for _ in range(100):
            num, energies = step(energies)
            result += num
    else:
        for j in count(1):
            _, energies = step(energies)
            if np.sum(energies) == 0:
                break
        result = j
    return result

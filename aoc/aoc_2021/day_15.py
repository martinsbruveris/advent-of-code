import heapq
from collections import defaultdict
from itertools import product

import numpy as np


def main(data, part):
    risk = data.split("\n")
    risk = [[int(e) for e in line] for line in risk]
    risk = np.asarray(risk)

    if part == "b":
        h, w = risk.shape
        risk = np.tile(risk, (5, 5))
        for j, k in product(range(5), repeat=2):
            risk[j * h : (j + 1) * h, k * w : (k + 1) * w] = (
                risk[:h, :w] + j + k - 1
            ) % 9 + 1  # We wrap at 10, but wrap back to 1 (no 0 risk levels)

    h, w = risk.shape
    end = (h - 1, w - 1)

    neighbors = defaultdict(set)
    for j in range(h - 1):
        for k in range(w):
            neighbors[(j, k)].add((j + 1, k))
            neighbors[(j + 1, k)].add((j, k))
    for j in range(h):
        for k in range(w - 1):
            neighbors[(j, k)].add((j, k + 1))
            neighbors[(j, k + 1)].add((j, k))

    max_cost = np.full_like(risk, fill_value=np.sum(risk))
    max_cost[0, 0] = 0
    storage = []
    heapq.heappush(storage, (0, (0, 0)))
    pos = (0, 0)
    while pos != end and storage:
        cost, pos = heapq.heappop(storage)
        for dst in neighbors[pos]:
            if cost + risk[dst] < max_cost[dst]:
                max_cost[dst] = cost + risk[dst]
                heapq.heappush(storage, (cost + risk[dst], dst))

    return max_cost[end]

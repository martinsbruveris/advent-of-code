import numpy as np


def look_up(trees):
    dists = np.zeros_like(trees)
    for j in range(trees.shape[0]):
        for k in range(trees.shape[1]):
            d = j
            for d in range(j - 1, -1, -1):
                if trees[d, k] >= trees[j, k]:
                    break
            dists[j, k] = j - d
    return dists


def main(data, part):
    trees = data.split("\n")
    trees = [list(num) for num in trees]
    trees = np.array(trees).astype(int)

    if part == "a":
        # Find all trees that cannot be seen from the edge
        heights = np.full((4, *trees.shape), fill_value=-1, dtype=int)
        for j in range(1, trees.shape[0]):
            heights[0, j, :] = np.maximum(trees[j - 1, :], heights[0, j - 1, :])
            heights[1, -j - 1, :] = np.maximum(trees[-j, :], heights[1, -j, :])
        for j in range(1, trees.shape[1]):
            heights[2, :, j] = np.maximum(trees[:, j - 1], heights[2, :, j - 1])
            heights[3, :, -j - 1] = np.maximum(trees[:, -j], heights[3, :, -j])
        visible = np.max(trees > heights, axis=0)
        result = np.sum(visible)
    else:
        # Find the sight distances from each tree
        dists = np.zeros((4, *trees.shape), dtype=int)
        dists[0] = look_up(trees)
        dists[1] = look_up(trees[::-1, :])[::-1, :]  # Looking down
        dists[2] = look_up(trees.T).T  # Looking left
        dists[3] = look_up(trees[:, ::-1].T).T[:, ::-1]  # Looking right
        scores = np.prod(dists, axis=0)
        result = np.max(scores)

    return result

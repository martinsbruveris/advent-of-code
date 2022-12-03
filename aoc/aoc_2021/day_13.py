import numpy as np

from aoc.ocr import aocr


def fold(arr, axis, at):
    if axis == "x":
        folded = arr[at + 1 :, :]
        w = folded.shape[0]
        arr = arr[:at, :].copy()
        arr[-w:, :] = np.maximum(arr[-w:, :], folded[::-1, :])
    else:
        folded = arr[:, at + 1 :]
        h = folded.shape[1]
        arr = arr[:, :at].copy()
        arr[:, -h:] = np.maximum(arr[:, -h:], folded[:, ::-1])
    return arr


def main(data, part):
    lines = data.split("\n")
    idx = len("fold along ")
    folds = [(ln[idx], int(ln[idx + 2 :])) for ln in lines if ln.startswith("f")]
    dots = [ln.split(",") for ln in lines[: -len(folds) - 1]]
    dots = [[int(x), int(y)] for x, y in dots]
    dots = np.asarray(dots)

    arr = np.zeros(np.max(dots, axis=0) + 1, dtype=int)
    for dot in dots:
        arr[dot[0], dot[1]] = 1

    if part == "a":
        arr = fold(arr, *folds[0])
        result = np.sum(arr)
    else:
        for f in folds:
            arr = fold(arr, *f)
        result = aocr(arr.T)

    return result

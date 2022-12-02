from pathlib import Path

import click
import numpy as np


def fold(arr, axis, at):
    if axis == "x":
        arr = np.maximum(arr[:at, :], arr[: -at - 1 : -1, :])
    else:
        arr = np.maximum(arr[:, :at], arr[:, : -at - 1 : -1])
    return arr


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    lines = filename.read_text().split("\n")
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
        s = "\n".join(["".join(map(str, line)) for line in arr.T])
        s = s.replace("1", "*").replace("0", " ")
        print(s)
        print("ECFHLHZF")
        result = -1

    print(result)


if __name__ == "__main__":
    main()

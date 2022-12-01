from pathlib import Path

import click
import numpy as np


def parse_line(line):
    src, dst = tuple(line.split(" -> "))
    src = tuple(int(num) for num in src.split(","))
    dst = tuple(int(num) for num in dst.split(","))
    return src + dst


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    lines = filename.read_text().split("\n")
    lines = [parse_line(line) for line in lines]
    lines = np.asarray(lines)  # Each row has format (x1, y1, x2, y2)

    height = np.max(lines[:, [1, 3]])
    width = np.max(lines[:, [0, 2]])
    board = np.zeros((width + 1, height + 1), dtype=int)

    for line in lines:
        if line[0] == line[2]:
            src = min(line[1], line[3])
            dst = max(line[1], line[3]) + 1
            board[line[0], src:dst] += 1
        elif line[1] == line[3]:
            src = min(line[0], line[2])
            dst = max(line[0], line[2]) + 1
            board[src:dst, line[1]] += 1
        elif part == "b":
            # We consider diagonal lines only for part b.
            assert abs(line[2] - line[0]) == abs(line[3] - line[1]), "Line not diagonal"
            dx = np.sign(line[2] - line[0])
            dy = np.sign(line[3] - line[1])
            length = abs(line[2] - line[0]) + 1
            for j in range(length):
                board[line[0] + j * dx, line[1] + j * dy] += 1

    nb_overlaps = np.sum(board >= 2)
    print(nb_overlaps)


if __name__ == "__main__":
    main()

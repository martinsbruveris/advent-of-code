from pathlib import Path

import click
import numpy as np


def parse_board(lines):
    """Converts `List[str]` to `ndarray` of `int`s."""
    board = [line.split(" ") for line in lines]
    board = [[int(num) for num in line if num != ""] for line in board]
    board = np.array(board)
    return board


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    lines = filename.read_text().split("\n")
    numbers = [int(num) for num in lines[0].split(",")]
    boards = [parse_board(lines[j : j + 5]) for j in range(2, len(lines), 6)]
    boards = np.asarray(boards)  # 3D array of shape (N, 5, 5)

    masks = np.zeros_like(boards)  # Which numbers have been hit
    idx = -1
    for number in numbers:
        masks[boards == number] = 1
        # We only care about the fullest row/column in each board
        rows_count = np.max(np.sum(masks, axis=1), axis=-1)
        cols_count = np.max(np.sum(masks, axis=2), axis=-1)
        board_finished = ((rows_count == 5) | (cols_count == 5)).astype(int)

        if part == "a" and np.sum(board_finished) == 1:
            idx = np.argmax(board_finished)
            break
        if part == "b" and np.sum(board_finished) == len(boards) - 1:
            # We have to set `idx` when the second to last board finished, to we still
            # know which the last board will be
            idx = np.argmin(board_finished)
        if part == "b" and np.sum(board_finished) == len(boards):
            # But we keep drawing numbers until all boards finish so we compute the
            # correct score
            break
    assert idx != -1, "No bingo board has won..."

    uncalled = np.sum(boards[idx][masks[idx] == 0])
    score = uncalled * number
    print(score)


if __name__ == "__main__":
    main()

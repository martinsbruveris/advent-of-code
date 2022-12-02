from collections import deque
from functools import reduce
from pathlib import Path

import click


def parse(line):
    stack = deque()
    for c in line:
        if c in "([{<":
            stack.appendleft(c)
        else:
            e = stack.popleft()
            if e + c not in {"()", "[]", "{}", "<>"}:
                return c, stack
    return None, stack


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    lines = filename.read_text().split("\n")

    if part == "a":
        points_map = {None: 0, ")": 3, "]": 57, "}": 1197, ">": 25137}
        chars = map(lambda l: parse(l)[0], lines)
        scores = map(lambda a: points_map[a], chars)
        result = sum(scores)
    else:
        points_map = {"(": 1, "[": 2, "{": 3, "<": 4}
        scores = []
        for line in lines:
            c, stack = parse(line)
            if c is not None:
                continue
            score = reduce(lambda a, b: 5 * a + points_map[b], stack, 0)
            scores.append(score)
        scores = sorted(scores)
        result = scores[len(scores) // 2]

    print(result)


if __name__ == "__main__":
    main()

import itertools
import math
from pathlib import Path

import click
from binarytree import Node, get_parent
from tqdm import tqdm


def parse_inner(line: str) -> (Node, str):
    if line[0] == "[":
        left, line = parse_inner(line[1:])
        assert line[0] == ","
        right, line = parse_inner(line[1:])
        assert line[0] == "]"
        root = Node(-1)
        root.left = left
        root.right = right
        return root, line[1:]
    elif line[0] in "0123456789":
        num = int(line[0])
        root = Node(num)
        return root, line[1:]
    else:
        raise ValueError(f"Can't interpret line {line}.")


def parse_number(line: str) -> Node:
    number, remainder = parse_inner(line)
    assert remainder == ""
    return number


def add(a: Node, b: Node) -> Node:
    c = Node(-1)
    # We need to clone `a` and `b`, because trees are modified in place by reduce
    # operations.
    c.left = a.clone()
    c.right = b.clone()
    c = reduce(c)
    return c


def reduce(number: Node) -> Node:
    while True:
        if number.height > 4:
            number = explode(number)
            continue
        elif max(n.value for n in number.leaves) >= 10:
            number = split(number)
            continue
        else:
            break
    return number


def explode(number: Node) -> Node:
    # Select the first node in the lowest level
    left = number.levels[-1][0]
    parent = get_parent(number, left)
    right = parent.right

    # Find all leaves in correct order
    leaves = number.inorder
    leaves = [leaf for leaf in leaves if leaf.left is None and leaf.right is None]

    # Add number to left
    left_idx = 0
    for left_idx, node in enumerate(leaves):
        if node is left:
            break
    if left_idx > 0:
        leaves[left_idx - 1].value += left.value

    # Add number to right
    right_idx = 0
    for right_idx, node in enumerate(leaves):
        if node is right:
            break
    if right_idx < len(leaves) - 1:
        leaves[right_idx + 1].value += right.value

    # Replace number with 0
    parent.value = 0
    parent.left = None
    parent.right = None

    return number


def split(number: Node) -> Node:
    # Find all leaves in correct order
    leaves = number.inorder
    leaves = [leaf for leaf in leaves if leaf.left is None and leaf.right is None]

    # Select those with value >= 10
    leaves = [leaf for leaf in leaves if leaf.value >= 10]

    # Nothing to be split
    if not leaves:
        return number

    # Do splitting
    leaf = leaves[0]
    leaf.left = Node(math.floor(leaf.value / 2))
    leaf.right = Node(math.ceil(leaf.value / 2))
    leaf.value = -1

    return number


def magnitude(number: Node) -> int:
    if number.left is None and number.right is None:
        return number.value
    else:
        return 3 * magnitude(number.left) + 2 * magnitude(number.right)


def solve_part_a(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = add(result, number)

    result = magnitude(result)
    return result


def solve_part_b(numbers):
    max_sum = 0
    total = len(numbers) * (len(numbers) - 1)
    for a, b in tqdm(itertools.permutations(numbers, 2), total=total):
        max_sum = max(max_sum, magnitude(add(a, b)))
    return max_sum


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    lines = filename.read_text().split("\n")
    numbers = [parse_number(line) for line in lines]

    if part == "a":
        print(solve_part_a(numbers))
    else:
        print(solve_part_b(numbers))


if __name__ == "__main__":
    main()

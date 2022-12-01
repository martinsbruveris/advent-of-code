import math
from itertools import permutations
from pathlib import Path

import click
from binarytree import Node, get_parent


def parse_inner(line: str) -> (Node, str):
    if line[0] == "[":
        left, line = parse_inner(line[1:])
        assert line[0] == ","
        right, line = parse_inner(line[1:])
        assert line[0] == "]"
        root = Node(-1, left=left, right=right)
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
    # We need to clone `a` and `b`, because trees are modified in place by `reduce`.
    c = Node(-1, left=a.clone(), right=b.clone())
    reduce(c)
    return c


def reduce(number: Node):
    # Note that `explode` and `split` modify `number` in place
    while True:
        if number.height > 4:
            explode(number)
        elif max(n.value for n in number.leaves) >= 10:
            split(number)
        else:
            break


def explode(number: Node):
    # Select the first node in the lowest level
    left = number.levels[-1][0]
    parent = get_parent(number, left)
    right = parent.right
    assert right is number.levels[-1][1]  # Just a sanity-check

    # Find all leaves in correct order
    leaves = number.inorder
    leaves = [leaf for leaf in leaves if leaf.left is None and leaf.right is None]

    # Add number to left
    left_idx = -1
    for left_idx, node in enumerate(leaves):
        if node is left:
            break
    assert left_idx != -1
    if left_idx > 0:
        leaves[left_idx - 1].value += left.value

    # Add number to right
    right_idx = -1
    for right_idx, node in enumerate(leaves):
        if node is right:
            break
    assert right_idx != -1
    if right_idx < len(leaves) - 1:
        leaves[right_idx + 1].value += right.value

    # Replace number with 0
    parent.value = 0
    parent.left = None
    parent.right = None


def split(number: Node):
    # Find all leaves in correct order
    leaves = number.inorder
    leaves = [leaf for leaf in leaves if leaf.left is None and leaf.right is None]

    # Select those with value >= 10
    leaves = [leaf for leaf in leaves if leaf.value >= 10]

    # Nothing to be split
    if not leaves:
        return

    # Split the first selected leaf
    leaf = leaves[0]
    leaf.left = Node(math.floor(leaf.value / 2))
    leaf.right = Node(math.ceil(leaf.value / 2))
    leaf.value = -1


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
    sums = [magnitude(add(a, b)) for a, b in list(permutations(numbers, 2))]
    return max(sums)


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

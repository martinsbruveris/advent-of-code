import math
from collections import defaultdict, deque
from itertools import accumulate, permutations


def add(a, b):
    c = ["["] + a + b + ["]"]
    c = reduce(c)
    return c


def reduce(number):
    while True:
        # Check if we need to explode
        depth = 0
        depth_change = defaultdict(lambda: 0, {"[": 1, "]": -1})
        did_explode = False
        for idx in range(len(number) - 1):
            c, d = number[idx], number[idx + 1]
            if depth > 4 and c not in {"[", "]"} and d not in {"[", "]"}:
                number = explode(number, idx)
                did_explode = True
                break
            depth += depth_change[c]
        if did_explode:
            continue

        # Check if we need to split
        did_split = False
        for idx, c in enumerate(number):
            if c not in {"[", "]"} and c >= 10:
                number = split(number, idx)
                did_split = True
                break
        if did_split:
            continue

        # No operation triggered: we are done
        break
    return number


def explode(number, idx):
    for j in range(idx - 1, -1, -1):
        if number[j] not in {"[", "]"}:
            number[j] += number[idx]
            break
    for j in range(idx + 2, len(number)):
        if number[j] not in {"[", "]"}:
            number[j] += number[idx + 1]
            break
    return number[: idx - 1] + [0] + number[idx + 3:]


def split(number, idx):
    pair = ["[", math.floor(number[idx] / 2), math.ceil(number[idx] / 2), "]"]
    return number[:idx] + pair + number[idx+1:]


def magnitude(number) -> int:
    storage = deque()
    for c in number:
        if c == "[":
            continue
        elif c == "]":
            right = storage.pop()
            left = storage.pop()
            storage.append(3 * left + 2 * right)
        else:
            storage.append(c)
    return storage.pop()


def main(data, part):
    lines = data.split("\n")
    numbers = [[c if c in "[]" else int(c) for c in ln if c != ","] for ln in lines]

    if part == "a":
        sums = list(accumulate(numbers, add))
        return magnitude(sums[-1])
    else:
        sums = [magnitude(add(a, b)) for a, b in permutations(numbers, 2)]
        return max(sums)

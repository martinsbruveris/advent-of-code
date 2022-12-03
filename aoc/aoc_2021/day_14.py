from collections import defaultdict


def main(data, part):
    lines = data.split("\n")
    polymer = lines[0]
    recipes = {r[:2]: r[-1] for r in lines[2:]}

    pairs = defaultdict(lambda: 0)
    for j in range(len(polymer) - 1):
        pairs[polymer[j : j + 2]] += 1

    steps = 10 if part == "a" else 40
    for _ in range(steps):
        after = defaultdict(lambda: 0)
        for pair, value in pairs.items():
            if pair in recipes:
                after[pair[0] + recipes[pair]] += value
                after[recipes[pair] + pair[1]] += value
            else:
                after[pair] = value
        pairs = after

    counts = defaultdict(lambda: 0, {polymer[-1]: 1})
    for pair, value in pairs.items():
        counts[pair[0]] += value

    counts = list(counts.values())
    return max(counts) - min(counts)

import re
from collections import defaultdict


def main(data, part):
    crates, instructions = data.split("\n\n")

    stacks = defaultdict(list)
    for line in crates.split("\n"):
        for idx, c in enumerate(line):
            if c.isupper():
                stacks[(idx // 4) + 1].insert(0, c)

    for instruction in instructions.split("\n"):
        num, src, dst = map(int, re.findall(r"\d+", instruction))
        if part == "a":
            stacks[dst] = stacks[dst] + stacks[src][-1 : -num - 1 : -1]
        else:
            stacks[dst] = stacks[dst] + stacks[src][-num:]
        stacks[src] = stacks[src][:-num]

    top_crates = "".join(stacks[j + 1][-1] for j in range(len(stacks)))
    return top_crates

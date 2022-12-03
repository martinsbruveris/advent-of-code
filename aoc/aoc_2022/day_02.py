from itertools import starmap


def outcome(a, b):
    if a == b:
        return 3
    elif a % 3 + 1 == b:
        return 6
    else:
        return 0


def strategy(a, o):
    if o == 3:
        return a
    elif o == 6:
        return 1 if a == 3 else a + 1
    else:
        return 3 if a == 1 else a - 1


def main(data, part):
    lines = data.split("\n")
    cmds = [tuple(line.split(" ")) for line in lines]

    if part == "a":
        elf_map = dict(A=1, B=2, C=3)
        me_map = dict(X=1, Y=2, Z=3)

        cmds = [(elf_map[s], me_map[t]) for s, t in cmds]
        outcomes = starmap(outcome, cmds)
        me = map(lambda c: c[1], cmds)
        result = sum(outcomes) + sum(me)
    else:
        elf_map = dict(A=1, B=2, C=3)
        outcome_map = dict(X=0, Y=3, Z=6)
        cmds = [(elf_map[s], outcome_map[t]) for s, t in cmds]

        me = starmap(strategy, cmds)
        outcomes = map(lambda c: c[1], cmds)
        result = sum(outcomes) + sum(me)

    return result

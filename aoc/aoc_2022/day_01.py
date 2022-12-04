def main(data, part):
    elves = data.split("\n\n")
    elves = map(lambda s: sum(map(int, s.split("\n"))), elves)
    elves = sorted(elves)
    idx = -1 if part == "a" else -3
    result = sum(elves[idx:])
    return result

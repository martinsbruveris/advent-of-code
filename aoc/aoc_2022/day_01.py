def main(data, part):
    lines = data.split("\n")

    elves = [[]]
    for line in lines:
        if line == "":
            elves.append([])
        else:
            elves[-1].append(int(line))
    if len(elves[-1]) == 0:
        elves.pop()

    total = map(sum, elves)
    total = sorted(total)

    if part == "a":
        result = total[-1]
    else:
        result = sum(total[-3:])
    return result

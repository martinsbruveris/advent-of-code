def main(data, part):
    cmd2dir = {"(": 1, ")": -1}
    idx, pos = 0, 0
    for idx, c in enumerate(data, start=1):
        pos += cmd2dir[c]
        if part == "b" and pos < 0:
            break
    return pos if part == "a" else idx

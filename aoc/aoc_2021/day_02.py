def track_a(commands):
    horizontal = 0
    depth = 0
    for cmd, x in commands:
        x = int(x)
        if cmd == "down":
            depth += x
        elif cmd == "up":
            depth -= x
        else:  # cmd == "forward"
            horizontal += x
    return horizontal * depth


def track_b(commands):
    horizontal = 0
    depth = 0
    aim = 0
    for cmd, x in commands:
        x = int(x)
        if cmd == "down":
            aim += x
        elif cmd == "up":
            aim -= x
        else:  # cmd == "forward"
            horizontal += x
            depth += x * aim
    return horizontal * depth


def main(data, part):
    commands = data.split("\n")
    commands = [cmd.split(" ") for cmd in commands]

    if part == "a":
        result = track_a(commands)
    else:
        result = track_b(commands)
    return result

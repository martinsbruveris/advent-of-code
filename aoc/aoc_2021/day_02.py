from pathlib import Path

import click


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


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    commands = filename.read_text().split("\n")
    commands = [cmd.split(" ") for cmd in commands]

    if part == "a":
        result = track_a(commands)
    else:
        result = track_b(commands)
    print(result)


if __name__ == "__main__":
    main()

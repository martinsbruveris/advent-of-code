from pathlib import Path

import click


@click.command()
@click.argument("filename")
def main(filename):
    filename = Path(filename)
    commands = filename.read_text().split("\n")
    commands = [cmd.split(" ") for cmd in commands]

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
    print(horizontal * depth)


if __name__ == "__main__":
    main()

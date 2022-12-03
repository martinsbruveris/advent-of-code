from pathlib import Path

import click


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    lines = filename.read_text().split("\n")

    result = 0
    if part == "a":
        for line in lines:
            item = (set(line[: len(line) // 2]) & set(line[len(line) // 2 :])).pop()
            # a .. 1, b .. 2, ..., A .. 27, B .. 28, ...
            priority = ord(item) - 96 if item.islower() else ord(item) - 38
            result += priority
    else:
        for j in range(0, len(lines), 3):
            item = (set(lines[j]) & set(lines[j + 1]) & set(lines[j + 2])).pop()
            priority = ord(item) - 96 if item.islower() else ord(item) - 38
            result += priority

    print(result)


if __name__ == "__main__":
    main()

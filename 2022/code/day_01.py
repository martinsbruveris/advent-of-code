from pathlib import Path

import click


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    lines = filename.read_text().split("\n")

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
    print(result)


if __name__ == "__main__":
    main()

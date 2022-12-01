from pathlib import Path

import click


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    text = filename.read_text()

    pos = 0
    for idx, c in enumerate(text, start=1):
        if c == "(":
            pos += 1
        elif c == ")":
            pos -= 1

        if part == "b" and pos < 0:
            break

    if part == "a":
        print(pos)
    else:
        print(idx)


if __name__ == "__main__":
    main()

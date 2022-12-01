from pathlib import Path

import click


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    text = filename.read_text()

    cmd2dir = {"(": 1, ")": -1}
    idx, pos = 0, 0
    for idx, c in enumerate(text, start=1):
        pos += cmd2dir[c]
        if part == "b" and pos < 0:
            break
    print(pos if part == "a" else idx)


if __name__ == "__main__":
    main()

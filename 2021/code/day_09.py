from pathlib import Path

import click
import numpy as np


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    lines = filename.read_text().split("\n")
    lines = [list(line) for ]

    if part == "a":
        result = count_1478(lines)
    else:
        outputs = [decode_output(line) for line in lines]
        result = sum(outputs)
    print(result)


if __name__ == "__main__":
    main()

import importlib
from pathlib import Path

import click


@click.command()
@click.argument("filename")
@click.option("--year", type=int)
@click.option("--day", type=int)
@click.option("--part", type=click.Choice(["a", "b"]))
def cli(year, day, part, filename):
    filename = Path(filename)
    data = filename.read_text()

    mod = importlib.import_module(f"aoc.aoc_{year}.day_{day:02}")
    result = mod.main(data, part)
    print(result)


def plugin(year, day, data):
    mod = importlib.import_module(f"aoc.aoc_{year}.day_{day:02}")
    a = mod.main(data, "a")
    b = mod.main(data, "b")
    return a, b

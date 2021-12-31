from pathlib import Path

import click


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    depths = filename.read_text().split("\n")
    depths = [int(depth) for depth in depths]

    window_size = 1 if part == "a" else 3
    depths = [
        sum(depths[j : j + window_size]) for j in range(len(depths) - window_size + 1)
    ]

    pairs = zip(depths[:-1], depths[1:])
    nb_increases = sum(p[1] > p[0] for p in pairs)
    print(nb_increases)


if __name__ == "__main__":
    main()

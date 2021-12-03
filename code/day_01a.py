from pathlib import Path

import click


@click.command()
@click.argument("filename")
def main(filename):
    filename = Path(filename)
    depths = filename.read_text().split("\n")
    depths = [int(depth) for depth in depths]

    pairs = zip(depths[:-1], depths[1:])
    nb_increases = sum(p[1] > p[0] for p in pairs)
    print(nb_increases)


if __name__ == "__main__":
    main()

from pathlib import Path

import click
import numpy as np


@click.command()
@click.argument("filename")
def main(filename):
    filename = Path(filename)
    numbers = filename.read_text().split("\n")
    numbers = [list(num) for num in numbers]
    numbers = np.array(numbers).astype(int)

    nb_ones = np.sum(numbers, axis=0)
    gamma = (nb_ones > numbers.shape[0] // 2).astype(int)
    epsilon = (nb_ones < numbers.shape[0] // 2).astype(int)

    n = numbers.shape[1]
    powers = np.asarray([2 ** (n - j - 1) for j in range(n)])

    gamma = np.sum(gamma * powers)
    epsilon = np.sum(epsilon * powers)
    print(gamma * epsilon)


if __name__ == "__main__":
    main()

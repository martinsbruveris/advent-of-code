from pathlib import Path

import click
import numpy as np


def filter_numbers(numbers, criterium):
    idx = 0
    while len(numbers) > 1:
        nb_ones = np.sum(numbers[:, idx])
        nb_zeros = len(numbers) - nb_ones
        bit = nb_ones >= nb_zeros if criterium == "most" else nb_ones < nb_zeros
        numbers = numbers[numbers[:, idx] == bit]
        idx += 1

    num = numbers[0]
    powers = np.asarray([2 ** (len(num) - j - 1) for j in range(len(num))])
    result = np.sum(num * powers)
    return result


@click.command()
@click.argument("filename")
def main(filename):
    filename = Path(filename)
    numbers = filename.read_text().split("\n")
    numbers = [list(num) for num in numbers]
    numbers = np.array(numbers).astype(int)

    oxygen = filter_numbers(numbers, "most")
    co2 = filter_numbers(numbers, "least")
    print(oxygen * co2)


if __name__ == "__main__":
    main()

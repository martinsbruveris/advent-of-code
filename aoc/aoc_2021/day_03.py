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
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    numbers = filename.read_text().split("\n")
    numbers = [list(num) for num in numbers]
    numbers = np.array(numbers).astype(int)

    if part == "a":
        nb_ones = np.sum(numbers, axis=0)
        gamma = (nb_ones > numbers.shape[0] // 2).astype(int)
        epsilon = (nb_ones < numbers.shape[0] // 2).astype(int)

        n = numbers.shape[1]
        powers = np.asarray([2 ** (n - j - 1) for j in range(n)])

        gamma = np.sum(gamma * powers)
        epsilon = np.sum(epsilon * powers)
        result = gamma * epsilon
    else:
        oxygen = filter_numbers(numbers, "most")
        co2 = filter_numbers(numbers, "least")
        result = oxygen * co2
    print(result)


if __name__ == "__main__":
    main()

from pathlib import Path

import click
import numpy as np
from tqdm import tqdm


def simulate_cycle(state):
    """
    `state` is an array of counts of fish with each internal counter.
    """
    state = state.copy()
    nb_new = state[0]
    state[:8] = state[1:9]  # Decrease counter
    state[6] += nb_new  # Reset timer from 0
    state[8] = nb_new  # Create new fish
    return state


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    state = filename.read_text().split(",")
    state = np.asarray(state).astype(int)

    # Convert state to counts
    values, counts = np.unique(state, return_counts=True)
    state = np.zeros(9, dtype=int)  # Possible counter values are 0...8
    for v, c in zip(values, counts):
        state[v] = c

    nb_days = 80 if part == "a" else 256
    for _ in tqdm(range(nb_days)):
        state = simulate_cycle(state)
    result = np.sum(state)
    print(result)


if __name__ == "__main__":
    main()

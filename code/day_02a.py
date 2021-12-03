from pathlib import Path

import click
import numpy as np

CMD_2_DIRECTION = {
    "forward": np.array([1, 0]),  # (horizontal pos, depth)
    "down": np.array([0, 1]),
    "up": np.array([0, -1]),
}


@click.command()
@click.argument("filename")
def main(filename):
    filename = Path(filename)
    commands = filename.read_text().split("\n")
    commands = [cmd.split(" ") for cmd in commands]
    commands = [(CMD_2_DIRECTION[cmd[0]], int(cmd[1])) for cmd in commands]

    position = np.array([0, 0])
    for cmd in commands:
        position += cmd[1] * cmd[0]
    print(position[0] * position[1])


if __name__ == "__main__":
    main()

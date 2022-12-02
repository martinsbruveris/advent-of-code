from collections import defaultdict, deque
from pathlib import Path

import click


@click.command()
@click.argument("filename")
@click.option("--part", type=click.Choice(["a", "b"]))
def main(filename, part):
    filename = Path(filename)
    edges = filename.read_text().split("\n")
    edges = [edge.split("-") for edge in edges]

    adj = defaultdict(lambda: defaultdict(lambda: False))
    for e1, e2 in edges:
        adj[e1][e2] = True
        adj[e2][e1] = True

    neighbors = defaultdict(set)
    for e1, e2 in edges:
        neighbors[e1].add(e2)
        neighbors[e2].add(e1)

    storage = deque()
    # We store: position, visited small caves, has a small cave been visited twice
    storage.append(("start", frozenset(["start"]), False))

    count = 0
    while storage:
        pos, visited, twice = storage.popleft()
        for dst in neighbors[pos]:
            if dst == "end":
                count += 1
            elif dst.isupper():
                storage.append((dst, visited, twice))
            elif dst not in visited:
                storage.append((dst, frozenset(visited | {dst}), twice))
            elif part == "b" and dst != "start" and not twice:
                storage.append((dst, visited, True))

    print(count)


if __name__ == "__main__":
    main()

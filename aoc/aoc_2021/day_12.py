from collections import defaultdict, deque


def main(data, part):
    edges = data.split("\n")
    edges = [edge.split("-") for edge in edges]

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

    return count

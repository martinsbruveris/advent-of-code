def main(data, part):
    depths = data.split("\n")
    depths = [int(depth) for depth in depths]

    window_size = 1 if part == "a" else 3
    depths = [
        sum(depths[j : j + window_size]) for j in range(len(depths) - window_size + 1)
    ]

    pairs = zip(depths[:-1], depths[1:])
    nb_increases = sum(p[1] > p[0] for p in pairs)
    return nb_increases

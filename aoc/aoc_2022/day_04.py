def main(data, part):
    lines = data.split("\n")
    ranges = [list(map(int, line.replace(",", "-").split("-"))) for line in lines]

    contained_count = 0
    overlap_count = 0
    for r in ranges:
        # If r = (a, b, c, d) and the two ranges are (a, b), (c, d), then one is
        # inside the other if a-c and d-b have the same sign. If a==b, then one range
        # is always inside the other; same for c==d.
        contained = int((r[0] - r[2]) * (r[3] - r[1]) >= 0)
        # This considers only overlap where one endpoint is inside the other interval
        overlap = int((r[2] <= r[0] <= r[3]) | (r[2] <= r[1] <= r[3]))
        contained_count += contained
        overlap_count += max(overlap, contained)

    return contained_count if part == "a" else overlap_count
